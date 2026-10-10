#!/usr/bin/env bash
set -euo pipefail

# ----------------------------------------------------------------------
# worker_tidk.bash <todo list>
#
# One species (line $LSB_JOBINDEX of the todo list, species<TAB>fasta),
# run by run_tidk.bash as an LSF array element:
#   1. tidk explore -> $EXPLORE_DIR/<species>.explore.tsv
#      (stderr, including strand-bias warnings, -> <species>.explore.err)
#   2. tidk ends with the top explore unit as --string (or discovering the
#      unit itself if explore found nothing)
#      -> $ENDS_DIR/<species>.ends.{tsv,bed,json}
#   3. tidk ends for each of the top N_CANDIDATES explore units
#      -> $ENDS_DIR/candidates/<species>.<rank>.<unit>.ends.{tsv,bed,json}
# then touches $ENDS_DIR/<species>.done. A finished explore output is
# reused, so a rerun after a failure in steps 2-3 doesn't repeat it.
#
# Settings come from the environment (exported by run_tidk.bash):
# TIDK, MINLEN, MAXLEN, THRESH, DIST, MIN_SEQ, N_CANDIDATES,
# EXPLORE_DIR, ENDS_DIR.
# ----------------------------------------------------------------------

todo="$1"
line=$(sed -n "${LSB_JOBINDEX}p" "$todo")
species=$(cut -f1 <<< "$line")
fasta=$(cut -f2 <<< "$line")
[[ -n "$species" && -n "$fasta" ]] || { echo "no species at index ${LSB_JOBINDEX} of ${todo}" >&2; exit 1; }
echo "[worker_tidk] ${species} ${fasta}"

explore_out="${EXPLORE_DIR}/${species}.explore.tsv"
explore_err="${EXPLORE_DIR}/${species}.explore.err"
cand_dir="${ENDS_DIR}/candidates"

# write to a temporary file first, so a killed job doesn't leave a
# partial output that later runs would take as done
if [[ ! -s "${explore_out}" ]]; then
    "${TIDK}" explore \
        -m "${MINLEN}" -x "${MAXLEN}" \
        --threshold "${THRESH}" \
        --distance "${DIST}" \
        "${fasta}" > "${explore_out}.tmp" 2> "${explore_err}"
    mv "${explore_out}.tmp" "${explore_out}"
fi

unit=$(awk -F'\t' 'NR == 2 { print $1 }' "${explore_out}")
string_arg=()
if [[ -n "${unit}" ]]; then
    string_arg=(--string "${unit}")
fi

# with no explore unit, ends discovers one from the sequence ends, and
# exits with an error if there isn't one: that's a result (no tandem
# repeat at the ends), not a failure, so the species is still done
if ! "${TIDK}" ends \
    "${string_arg[@]}" \
    --min-sequence-length "${MIN_SEQ}" \
    -o "${species}" -d "${ENDS_DIR}" \
    "${fasta}" 2> "${ENDS_DIR}/${species}.ends.err"; then
    if [[ -n "${unit}" ]] || ! grep -q "No candidate telomeric repeat found" "${ENDS_DIR}/${species}.ends.err"; then
        exit 1
    fi
    echo "[worker_tidk] ${species}: no repeat from explore or at the sequence ends"
fi

rank=0
while read -r unit; do
    rank=$(( rank + 1 ))
    "${TIDK}" ends \
        --string "${unit}" \
        --min-sequence-length "${MIN_SEQ}" \
        -o "${species}.${rank}.${unit}" -d "${cand_dir}" \
        "${fasta}" 2> /dev/null
done < <(awk -F'\t' -v n="${N_CANDIDATES}" 'NR > 1 && NR <= n + 1 { print $1 }' "${explore_out}")

touch "${ENDS_DIR}/${species}.done"
