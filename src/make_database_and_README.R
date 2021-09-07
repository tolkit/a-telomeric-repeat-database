# make the database
# save this
# also print out a github markdown formatted table.

library(data.table)

options(scipen = 999)

taxons <- fread("../data/taxons.csv")
telos <- fread("../data/telo_seqs.tsv")

data <- taxons[telos, on = .(species)]

keycols <- c("species", "genus", "family", "order", "class", "phylum")
setorderv(data, rev(keycols))

data <- unique(data)

fwrite(data, file = "../data/telo_database.tsv", sep = "\t")

# print github table
cat(r"{# A Telomeric Repeat Database

There are other telomeric repeat databases out there. This one uses both raw data (PacBio), and assemblies to de-novo identify telomeric repeat sequences from data generated by the Darwin Tree of Life.

The program used to infer telomeric repeats is <a href="https://github.com/tolkit/telomeric-identifier">tidk</a>.

See `/src/README.md` for pipeline details.

To note this is not a curated list, it is raw output from tidk, and the values may not be accurate.

}")

cat("| Species | Family | Order | Class | Telomeric repeat 1 | Telomeric repeat 2 | Data type |\n")
cat("| -- | --- | --- | --- | --- | --- | --- |\n")

for (i in seq_len(nrow(data))) {
    species <- data[i, ]$species
    family <- data[i, ]$family
    order <- data[i, ]$order
    class <- data[i, ]$class
    telo_1 <- data[i, ]$telo_seq_1
    telo_2 <- data[i, ]$telo_seq_2
    type <- data[i, ]$type

    genus <- data[i, ]$genus

    if (!is.na(genus)) {
        cat(paste(
            "|*",
            species,
            "*|",
            family,
            "|",
            order,
            "|",
            class,
            "|",
            telo_1,
            "|",
            telo_2,
            "|",
            type,
            "|\n"
        ))
    }
}