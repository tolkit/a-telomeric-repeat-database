#!/usr/bin/env bash

# use the python script to query the goat API
python3 ./generate_goat_string.py > taxons.csv
# filter taxons.csv
# and remove extra column headers
awk -F, '!/Zaprionus/' taxons.csv > taxons2.csv
sed '2,$s/"taxon_id","taxon_rank","scientific_name","species","genus","family","order","class","phylum","kingdom","superkingdom","genome_size"//g' taxons2.csv > taxons3.csv
# another sed
sed '2,$s/"taxon_id","taxon_rank","scientific_name","species","genus","family","order","class","phylum","kingdom","superkingdom"//g' taxons3.csv > taxons4.csv

# tidy by re(moving) files
rm ./taxons.csv ./taxons2.csv ./taxons3.csv
mv ./taxons4.csv ../data/taxons.csv