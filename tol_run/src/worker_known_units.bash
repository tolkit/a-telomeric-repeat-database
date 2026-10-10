#!/usr/bin/env bash
set -euo pipefail

# ----------------------------------------------------------------------
# worker_known_units.bash <todo list>
#
# One species (line $LSB_JOBINDEX of the todo list, species<TAB>fasta):
# tidk ends for each unit in $KNOWN_UNITS that isn't already among its top
# $N_CANDIDATES explore units (those were checked by worker_tidk.bash)
#   -> $CAND_DIR/<species>.known.<unit>.ends.{tsv,bed,json}
# then touches $CAND_DIR/<species>.known.done.
#
# Settings from the environment (exported by run_known_units.bash):
# TIDK, MIN_SEQ, N_CANDIDATES, KNOWN_UNITS, EXPLORE_DIR, CAND_DIR,
# MAX_LOCAL_GZ.
# ----------------------------------------------------------------------

todo="$1"
line=$(sed -n "${LSB_JOBINDEX}p" "$todo")
species=$(cut -f1 <<< "$line")
fasta=$(cut -f2 <<< "$line")
[[ -n "$species" && -n "$fasta" ]] || { echo "no species at index ${LSB_JOBINDEX} of ${todo}" >&2; exit 1; }
echo "[worker_known_units] ${species} ${fasta}"

explore_out="${EXPLORE_DIR}/${species}.explore.tsv"
mapfile -t top < <(awk -F'\t' -v n="${N_CANDIDATES}" 'NR > 1 && NR <= n + 1 { print $1 }' "${explore_out}")

# read the assembly once from local scratch, not once per unit from lustre
input="${fasta}"
local_dir=""
if [[ "${fasta}" == *.gz && $(stat -c %s "${fasta}") -le ${MAX_LOCAL_GZ} ]]; then
    local_dir=$(mktemp -d "${TMPDIR:-/tmp}/known_units.XXXXXX")
    trap 'rm -rf "${local_dir}"' EXIT
    input="${local_dir}/assembly.fa"
    gzip -dc "${fasta}" > "${input}"
fi

while read -r unit _; do
    [[ "${unit}" == "unit" || -z "${unit}" ]] && continue
    for t in "${top[@]}"; do
        [[ "${t}" == "${unit}" ]] && continue 2
    done
    "${TIDK}" ends \
        --string "${unit}" \
        --min-sequence-length "${MIN_SEQ}" \
        -o "${species}.known.${unit}" -d "${CAND_DIR}" \
        "${input}" 2> /dev/null
done < "${KNOWN_UNITS}"

touch "${CAND_DIR}/${species}.known.done"
