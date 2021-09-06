#!/usr/bin/env bash

python3 ./generate_goat_string.py > taxons.csv
# filter taxons.csv
awk -F, '!/Zaprionus/' taxons.csv > taxons2.csv
sed '2,$s/"taxon_id","taxon_rank","scientific_name","species","genus","family","order","class","phylum","kingdom","superkingdom","genome_size"//g' taxons2.csv > taxons3.csv

# tidy
rm ./taxons.csv ./taxons2.csv
mv ./taxons3.csv ../data/taxons.csv