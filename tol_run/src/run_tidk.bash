#!/usr/bin/env bash
set -euo pipefail

# ----------------------------------------------------------------------
# run_tidk.bash
#
# Run tidk 0.3.0 across every species in the assembly list as one LSF job
# array (see worker_tidk.bash): explore, ends for the top explore unit,
# and ends for the top N_CANDIDATES units, so the telomere can be called
# as the candidate at the most chromosome ends (src/summary.py).
#
# Reads species<TAB>fasta from: inputs/tol_latest_assemblies.txt (or ASSEMBLY_LIST)
# Outputs: outputs/explore/<species>.explore.{tsv,err}
#          outputs/ends/<species>.ends.{tsv,bed,json}
#          outputs/ends/candidates/<species>.<rank>.<unit>.ends.{tsv,bed,json}
# Species with an outputs/ends/<species>.done marker are skipped (unless
# FORCE=1); the worker writes it once all three steps have finished.
#
# Settings are those of the tr_tert plant and clade_discovery runs, so the
# results can be pooled with them (src/seed_from_tr_tert.bash).
# ----------------------------------------------------------------------

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="${PROJECT_ROOT}/outputs"

ASSEMBLY_LIST="${ASSEMBLY_LIST:-${PROJECT_ROOT}/inputs/tol_latest_assemblies.txt}"
export EXPLORE_DIR="${EXPLORE_DIR:-${OUTPUT_DIR}/explore}"
export ENDS_DIR="${ENDS_DIR:-${OUTPUT_DIR}/ends}"
LOGDIR="${LOGDIR:-${OUTPUT_DIR}/logs}"
mkdir -p "$EXPLORE_DIR" "$ENDS_DIR/candidates" "$LOGDIR"

# a fixed 0.3.0 binary, so results don't change if tidk is rebuilt
export TIDK="${TIDK:-${PROJECT_ROOT}/bin/tidk-0.3.0}"

# tidk explore parameters, as the tr_tert runs
export MINLEN="${MINLEN:-4}"      # -m
export MAXLEN="${MAXLEN:-30}"     # -x
export THRESH="${THRESH:-100}"    # --threshold
export DIST="${DIST:-0.01}"       # --distance
# tidk ends: skip unplaced scaffolds and organelles
export MIN_SEQ="${MIN_SEQ:-1000000}"
export N_CANDIDATES="${N_CANDIDATES:-5}"

nCPU="${nCPU:-8}"
memGB="${memGB:-8}"
QUEUE="${QUEUE:-normal}"
MAX_RUNNING="${MAX_RUNNING:-300}"
memMB=$(( memGB * 1024 ))

"${TIDK}" --version | grep -q "tidk 0.3" || { echo "[run_tidk] ${TIDK} is not tidk 0.3.x" >&2; exit 1; }

# the species still to do, one per array index
todo="${LOGDIR}/todo.$(date +%Y%m%d%H%M%S).txt"
while IFS=$'\t' read -r species fasta; do
    [[ -z "$species" || -z "$fasta" ]] && continue
    if [[ -e "${ENDS_DIR}/${species}.done" && "${FORCE:-0}" != "1" ]]; then
        continue
    fi
    printf '%s\t%s\n' "$species" "$fasta"
done < "$ASSEMBLY_LIST" > "$todo"

n=$(wc -l < "$todo")
echo "[run_tidk] assembly list: $ASSEMBLY_LIST"
echo "[run_tidk] tidk:          $TIDK ($("$TIDK" --version))"
echo "[run_tidk] explore:       -m $MINLEN -x $MAXLEN --threshold $THRESH --distance $DIST"
echo "[run_tidk] ends:          --min-sequence-length $MIN_SEQ, top $N_CANDIDATES candidates"
if (( n == 0 )); then
    echo "[run_tidk] nothing to do"
    rm "$todo"
    exit 0
fi

bsub \
  -J "tidktol[1-${n}]%${MAX_RUNNING}" \
  -q "$QUEUE" \
  -n "$nCPU" \
  -R "span[hosts=1] select[mem>${memMB}] rusage[mem=${memMB}]" \
  -M "$memMB" \
  -o "${LOGDIR}/%J.%I.out" \
  -e "${LOGDIR}/%J.%I.err" \
  bash "${SCRIPT_DIR}/worker_tidk.bash" "$todo"

echo "[run_tidk] Submitted an array of ${n} species (todo list: ${todo})."
