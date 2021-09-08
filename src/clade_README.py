#!/usr/bin/python3

import os
import csv
from collections import Counter

# read in the telo_database.tsv

with open("../data/telo_database.tsv") as telo_database:
    rd = csv.reader(telo_database, delimiter="\t", quotechar='"')
    next(rd, None)  # skip the headers

    # store classes in dict
    classes = []

    # first pass to get keys
    for row in rd:
        if row[7] == "":
            pass
        else:
            # to make the dirs
            classes.append(row[7])
    # get keys for dirs & dict later
    uniq_classes = Counter(classes).keys()
    # copy
    uniq_classes_c = list(uniq_classes)
    classes_dict = {key: [] for key in uniq_classes_c}

with open("../data/telo_database.tsv") as telo_database:
    rd = csv.reader(telo_database, delimiter="\t", quotechar='"')
    next(rd, None)  # skip the headers
    # second pass
    for row in rd:
        if row[7] == "":
            continue
        # the different columns
        species = row[2]
        family = row[5]
        order = row[6]
        _class = row[7]
        telo_1 = row[12]
        telo_2 = row[13]
        data_type = row[14]

        classes_dict[_class].append([species, family, order, telo_1, telo_2, data_type])

# make directories
for dir in uniq_classes:
    os.makedirs("../clades/{0}".format(dir), exist_ok=True)

for key in uniq_classes:
    with open("../clades/{0}/README.md".format(key), "w") as key_file:
        key_file.write("# " + str(key) + "\n\n")
        key_file.write(
            "| Species | Family | Order | Telomeric repeat 1 | Telomeric repeat 2 | Data type |\n"
        )
        key_file.write("| -- | --- | --- | --- | --- | --- |\n")
        # now the rows of the table
        for row in classes_dict[key]:
            key_file.write("| " + " | ".join(row) + " |\n")
