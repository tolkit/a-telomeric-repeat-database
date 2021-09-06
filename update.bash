#!/usr/bin/env bash

# fetch data
cd src
bash fetch_data.bash
# generate the higher taxon data
bash goat_names.bash
# make tabular data from rsync'd data
bash get_telo_seqs.bash > ../data/telo_seqs.tsv
# update the README.md
Rscript make_database_and_README.R > ../README.md