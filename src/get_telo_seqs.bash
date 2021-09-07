#!/usr/bin/env bash

# make a tsv from all of the files in the data/ dirs

# firstly for assemblies

printf "species\ttelo_seq_1\ttelo_seq_2\ttype\n"
for F in ../data/assemblies/*.txt; do
    sp=$(basename $F | cut -f 1 -d '.' | sed 's/_/ /')
    telo_seq1=$(awk -F\t 'NR==2 {print $1}' $F)
    telo_seq2=$(awk -F\t 'NR==3 {print $1}' $F)
    printf "$sp\t$telo_seq1\t$telo_seq2\tassembly\n"
done

# then for pacbio data estimates

for F in ../data/pacbio/*.txt; do
    sp=$(basename $F | cut -f 1 -d '.' | sed 's/_/ /')
    telo_seq1=$(awk -F\t 'NR==2 {print $1}' $F)
    telo_seq2=$(awk -F\t 'NR==3 {print $1}' $F)
    printf "$sp\t$telo_seq1\t$telo_seq2\tpacbio\n"
done
