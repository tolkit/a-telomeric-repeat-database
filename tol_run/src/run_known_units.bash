#!/usr/bin/env bash
set -euo pipefail

# ----------------------------------------------------------------------
# run_known_units.bash
#
# After run_tidk.bash: run tidk ends for each known telomeric unit
# (inputs/known_telomere_units.tsv) that isn't among a species' top
# N_CANDIDATES explore units, as one LSF array (worker_known_units.bash).
#
# Checking only the top explore units misses telomeres that rank just
# below them: in the first ToL-wide run, AACCCT was 6th in Arvicola, Bufo
# and Scyliorhinus, and AACCC 24th in Aphodius ater, under satellites with
# more copies. The known units are the literature telomeres plus the
# C-run units the first run called at >= 25% of chromosome ends in >= 3
# species; microsatellites (AAAT, ACAGAG) are left out, since they are
# common near ends without being telomeres.
#
# Outputs: outputs/ends/candidates/<species>.known.<unit>.ends.{tsv,bed,json}
# and a <species>.known.done marker; src/summary.py pools these with the
# top explore candidates.
# ----------------------------------------------------------------------

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="${PROJECT_ROOT}/outputs"

ASSEMBLY_LIST="${ASSEMBLY_LIST:-${PROJECT_ROOT}/inputs/tol_latest_assemblies.txt}"
export KNOWN_UNITS="${KNOWN_UNITS:-${PROJECT_ROOT}/inputs/known_telomere_units.tsv}"
export EXPLORE_DIR="${EXPLORE_DIR:-${OUTPUT_DIR}/explore}"
export CAND_DIR="${CAND_DIR:-${OUTPUT_DIR}/ends/candidates}"
LOGDIR="${LOGDIR:-${OUTPUT_DIR}/logs/known_units}"
mkdir -p "$CAND_DIR" "$LOGDIR"

export TIDK="${TIDK:-${PROJECT_ROOT}/bin/tidk-0.3.0}"
export MIN_SEQ="${MIN_SEQ:-1000000}"
export N_CANDIDATES="${N_CANDIDATES:-5}"
# decompress assemblies up to this size (gzipped) to local scratch once,
# rather than once per unit
export MAX_LOCAL_GZ="${MAX_LOCAL_GZ:-2000000000}"

memGB="${memGB:-4}"
QUEUE="${QUEUE:-normal}"
MAX_RUNNING="${MAX_RUNNING:-300}"
memMB=$(( memGB * 1024 ))

"${TIDK}" --version | grep -q "tidk 0.3" || { echo "[run_known_units] ${TIDK} is not tidk 0.3.x" >&2; exit 1; }

todo="${LOGDIR}/todo.$(date +%Y%m%d%H%M%S).txt"
while IFS=$'\t' read -r species fasta; do
    [[ -z "$species" || -z "$fasta" ]] && continue
    [[ -s "${EXPLORE_DIR}/${species}.explore.tsv" ]] || continue
    if [[ -e "${CAND_DIR}/${species}.known.done" && "${FORCE:-0}" != "1" ]]; then
        continue
    fi
    printf '%s\t%s\n' "$species" "$fasta"
done < "$ASSEMBLY_LIST" > "$todo"

n=$(wc -l < "$todo")
echo "[run_known_units] $(( $(wc -l < "$KNOWN_UNITS") - 1 )) known units, ${n} species"
if (( n == 0 )); then
    rm "$todo"
    exit 0
fi

bsub \
  -J "tidkknown[1-${n}]%${MAX_RUNNING}" \
  -q "$QUEUE" \
  -n 1 \
  -R "select[mem>${memMB}] rusage[mem=${memMB}]" \
  -M "$memMB" \
  -o "${LOGDIR}/%J.%I.out" \
  -e "${LOGDIR}/%J.%I.err" \
  bash "${SCRIPT_DIR}/worker_known_units.bash" "$todo"

echo "[run_known_units] Submitted an array of ${n} species (todo list: ${todo})."
