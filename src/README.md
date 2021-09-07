# Rough pipeline for assemblies:

```bash
find /lustre/scratch116/tol/projects/darwin/data/ -name genome_assembly_stats.txt -printf '%h\n' > assembly_paths1.txt

# add /genome.fasta.gz to the end
sed -e 's/$/\/genome.fasta.gz/' -i assembly_paths1.txt
# remove alt haps
sed -n '/alternate/!p' assembly_paths1.txt > assembly_paths2.txt

while read F; do
	# get name
	nm=$(echo "$F" | cut -d / -f 9)
	# copy genome to current dir
	cp $F .
	gunzip genome.fasta.gz
        ../../telomeric-identifier/target/release/tidk explore -f genome.fasta -m 5 -x 12 -o $nm
	rm genome.fasta
done <assembly_paths2.txt

```

And for PacBio HiFi reads:

```bash 
find /lustre/scratch116/tol/projects/darwin/data/ -regextype posix-extended -regex '.*pacbio.*\.fasta\.gz$' > pbio_read_paths.txt

# I did try a job array but couldnt get it to work
while read F; do
	# get name
	nm=$(echo "$F" | cut -d / -f 9)
	printf "Processing %s\n" "${nm}"
	# copy genome to current dir
	cp $F ./genome.fasta.gz
	gunzip genome.fasta.gz
	# increase threshold value.
       ../../../telomeric-identifier/target/release/tidk explore -f genome.fasta -t 1000 -m 5 -x 12 -o $nm
	rm genome.fasta
done <pbio_read_paths.txt
```

All of this gets output in an `explore` directory. I am only interested really in the telomeric repeat estimated by the program, hence only syncing the `.txt` files.

```bash
# fetch data
cd src
bash fetch_data.bash
# generate the higher taxon data
bash goat_names.bash
# make tabular data from rsync'd data
bash get_telo_seqs.bash > ../data/telo_seqs.tsv
# update the README.md
Rscript make_database_and_README.R > ../README.md
```