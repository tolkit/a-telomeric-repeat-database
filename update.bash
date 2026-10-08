#!/usr/bin/env bash

# Since 2026-10: the database is built from the ToL-wide tidk 0.3.0 run
# (see src/README.md), keeping the tidk 0.2 entries only for species it
# doesn't cover.
cd src
# tidk 0.3.0 calls with NCBI taxonomy, and the comparison with tidk 0.2
python3 import_tidk_v03.py
# data/telo_database_v2.tsv, README.md and the clade tables
python3 make_database_v2.py

# The tidk 0.2 pipeline (fetch_data.bash, goat_names.bash,
# get_telo_seqs.bash, make_database_and_README.R, clade_README.py) built
# data/telo_database.tsv, which is kept as it was; running it again would
# overwrite README.md and the clade tables with the 0.2 table.
