#!/usr/bin/env bash

# if we don't have the ncbi.nw
# download, otherwise skip
# as this takes a few minutes

[ ! -f ./ncbi.nw ] && \
./gotree_amd64_darwin download ncbitax --tips-taxid -o ncbi.nw && \
printf "Downloading the entire NCBI tax tree.\n"

printf "NCBI tax tree already downloaded.\n"

# get unique taxids from the database
awk '{print $1}' ../../data/telo_database.tsv | tail -n +6 | sort | uniq > taxids.txt

printf "Made taxids.\n"

# prune the newick to our taxids
./gotree_amd64_darwin prune -f taxids.txt -i ncbi.nw -r -o pruned_ncbi.nw

printf "Pruned NCBI tax tree.\n"

# make a sed script from the taxids, then feed this to another sed command
sed 's/\([^ ]*\) \(.*\)/s\/\1\/\2\/g/' taxids_key.txt | tr -d '\t' > sed.script
sed -f sed.script pruned_ncbi.nw > pruned_ncbi_names.nw

printf "Replaced taxids with species names.\n"

# clean up
rm taxids.txt sed.script pruned_ncbi.nw

printf "Done!\n"