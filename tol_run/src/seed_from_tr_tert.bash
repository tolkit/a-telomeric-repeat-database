#!/usr/bin/env bash
set -euo pipefail

# ----------------------------------------------------------------------
# seed_from_tr_tert.bash
#
# Copy finished tidk 0.3.0 results from the tr_tert plant and
# clade_discovery runs into outputs/, for species whose assembly path in
# inputs/tol_latest_assemblies.txt is the same as in that run, and mark
# them done so run_tidk.bash skips them. The settings and binary are the
# same (tidk 0.3.0, sha256 0d3aa468...), so the results are too.
#
# Species whose assembly changed (mostly hap1/hap2 swaps: the tr_tert
# lists predate the assembly finder following ToL's designated reference)
# are left for run_tidk.bash.
# ----------------------------------------------------------------------

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
TR_TERT="${TR_TERT:-/lustre/scratch122/tol/teams/blaxter/users/mb39/tr_tert}"
LIST="${PROJECT_ROOT}/inputs/tol_latest_assemblies.txt"
EXPLORE_DIR="${PROJECT_ROOT}/outputs/explore"
ENDS_DIR="${PROJECT_ROOT}/outputs/ends"
mkdir -p "$EXPLORE_DIR" "$ENDS_DIR/candidates"

# <assembly list> <explore dir> <ends dir>, per tr_tert run
runs=(
  "${TR_TERT}/inputs/dtol_plant_paths.txt ${TR_TERT}/outputs/tidk_v0.3 ${TR_TERT}/outputs/tidk_ends"
)
for clade in coleoptera araneae myriapoda; do
  runs+=("${TR_TERT}/clade_discovery/inputs/${clade}_paths.txt ${TR_TERT}/clade_discovery/outputs/tidk_v0.3 ${TR_TERT}/clade_discovery/outputs/tidk_ends")
done

declare -A path
while IFS=$'\t' read -r species fasta; do
    path["$species"]="$fasta"
done < "$LIST"

seeded=0
changed=0
for run in "${runs[@]}"; do
    read -r list explore ends <<< "$run"
    while IFS=$'\t' read -r species fasta; do
        [[ -z "$species" ]] && continue
        if [[ "${path[$species]:-}" != "$fasta" ]]; then
            changed=$(( changed + 1 ))
            continue
        fi
        [[ -s "${explore}/${species}.explore.tsv" && -s "${ends}/${species}.ends.json" ]] || continue
        compgen -G "${ends}/candidates/${species}.1.*.ends.json" > /dev/null || continue
        cp "${explore}/${species}".explore.{tsv,err} "$EXPLORE_DIR/"
        cp "${ends}/${species}".ends.* "$ENDS_DIR/"
        cp "${ends}/candidates/${species}".[0-9]*.ends.* "$ENDS_DIR/candidates/"
        touch "${ENDS_DIR}/${species}.done"
        seeded=$(( seeded + 1 ))
    done < "$list"
done

echo "[seed_from_tr_tert] seeded ${seeded} species; ${changed} have a different assembly now and will be rerun"
