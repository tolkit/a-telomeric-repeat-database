#!/usr/bin/python3

# Take a list of files
# Query the goat API for higher taxons

import os
from pathlib import Path

space = "%20"

# get file names
files = Path().cwd().glob("../data/*/*.txt")
f = []
for file in files:
    f.append(file.name)

# # edit these names
f2 = [x[:-4] for x in f]
f3 = [x.replace("_", space) for x in f2]

for taxon in f3:
    query = """
    curl -X GET -H "accept: text/csv" "https://goat.genomehubs.org/api/v0.0.1/search?query=tax_name%28{0}%29&result=taxon&fields=genome_size&includeEstimates=true&summaryValues=count&taxonomy=ncbi&ranks=species%2Cgenus%2Cfamily%2Corder%2Cclass%2Cphylum%2Ckingdom%2Csuperkingdom"
    """.format(
        taxon
    )
    os.system(query)
