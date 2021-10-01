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

## Pipeline updates (22.09.2021)

More for back-up really, these two scripts (plus helpers) pull all of the current assembly/pacbio paths on the farm, filter them if they've already been done, and then submit the jobs. I'm mainly putting these down for backup/I'll forget what they are and what they are for.

### Assemblies

`update_assembly_tidk.bash`

for file in ./explore/*; do basename $file | awk -F_ '{print $1"_"$2}' | grep -v "\.txt"; done

```bash
#!/usr/bin/env bash

date=$(date '+%Y-%m-%d')

readlink -f /lustre/scratch116/tol/projects/darwin/data/*/*/assembly/release/reference > assembly_paths_${date}_init.txt

# get the names of the species we have already proccessed.
for file in ./explore/*; do basename $file | awk -F_ '{print $1"_"$2}' | grep -v "\.txt"; done > species_names.txt

awk '{print $0"/insdc/genome.fasta.gz"}' assembly_paths_${date}_init.txt | sort >  assembly_paths_${date}.txt

grep -v -f species_names.txt assembly_paths_${date}.txt > assembly_paths_${date}_for_pipeline.txt

rm assembly_paths_${date}_init.txt
```

`all_dtol_tidk.bash`

```bash
#!/usr/bin/env bash

while read F; do
	# get name
	nm=$(echo "$F" | cut -d / -f 9)
	# copy genome to current dir
	cp $F .
	gunzip genome.fasta.gz
        ../../telomeric-identifier/target/release/tidk explore -f genome.fasta -m 5 -x 30 -o $nm -t 50
	rm genome.fasta
done < $1
```

Wrapper script - `assembly_pipeline.bash`. `$1` is required and should be the previous run's `assembly_paths_${date}_for_pipeline.txt`.

```bash
#!/usr/bin/env bash

date=$(date '+%Y-%m-%d')

# get the updated paths, requires a previous SORTED file of paths.

bash update_assembly_tidk.bash

# then submit the pipeline

PIPELINE=./all_dtol_tidk.bash
mbMem=5000

echo "bash ${PIPELINE} assembly_paths_${date}_for_pipeline.txt" | \

bsub -n 10 -q long -R"span[hosts=1] select[mem>${mbMem}] rusage[mem=${mbMem}]" -M${mbMem} -o %J.${date}.out -e %J.${date}.err
```

### PacBio data

Probably written slightly better than the one above:

```bash
# today's date
date=$(date '+%Y-%m-%d')

# get all of the most current pacbio paths
for dir in `ls -1d /lustre/scratch116/tol/projects/darwin/data/*/*`; do find $dir/genomic_data -mindepth 4 -maxdepth 4 -type f -iname "*ccs*.filtered.fasta.gz" 2>/dev/null; done > \
	all_pacbio_paths_${date}.txt

# replace pbio_read_paths2.txt with $1 later

for file in ./explore/*; do basename $file | awk -F_ '{print $1"_"$2}' | grep -v "\.txt"; done > path_pattern_file_${date}.txt

# filter the big path file
grep -v -f path_pattern_file_${date}.txt all_pacbio_paths_${date}.txt > filtered_paths_${date}.txt

# now get unique paths
python3 unique_paths.py filtered_paths_${date}.txt > filtered_paths_unique_${date}.txt

while read F; do
	# get name
	nm=$(echo "$F" | cut -d / -f 9)
	printf "Processing %s\n" "${nm}"
	# copy genome to current dir
	# now bsub this
	mbMem=6000; bsub -n 30 -q normal -R"span[hosts=1] select[mem>${mbMem}] rusage[mem=${mbMem}]" -M${mbMem} -o %J.out -e %J.err "
	cp ${F} ${nm}_genome.fasta.gz
        gunzip ${nm}_genome.fasta.gz
	# increase threshold value.
       ../../../telomeric-identifier/target/release/tidk explore -f ${nm}_genome.fasta -t 1000 -m 5 -x 30 -o $nm
	rm ${nm}_genome.fasta"
done < filtered_paths_unique_${date}.txt
```

Requires this python script (`unique_paths.py`).

```python
import sys
from collections import defaultdict
import os

with open(sys.argv[1]) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

my_list = lines
my_dict = defaultdict(list)

for item in my_list:
    if os.path.isdir(item):   # To check path is a directory
        _ = my_dict[item]   # will set default value as empty list
    else:
        path, file = os.path.split(item)
        my_dict[path].append(file)

for key in my_dict:
	print(key + "/" +  my_dict[key][0])
```

