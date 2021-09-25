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

Both raw data (PacBio) and Darwin Tree of Life assemblies are used to de-novo identify telomeric repeat sequences.

The program used to infer telomeric repeats is <a href="https://github.com/tolkit/telomeric-identifier">tidk</a>.

See `/src/README.md` for pipeline details.

To note this is not a curated list, it is raw output from tidk, and as such, the values may not be accurate. The list is also being actively updated. The main list is below, but see the `clades` directory to get breakdown by eukaryotic class. It will be immediately noticed that for some clades, tidk is not catching the telomeric repeats.

A curated list is being worked on currently, and can be seen in `./data/curated/`.

| Species | Family | Order | Class | Telomeric repeat 1 | Telomeric repeat 2 | Data type |
| -- | --- | --- | --- | --- | --- | --- |
}")

for (i in seq_len(nrow(data))) {
    species <- data[i, ]$species
    genus <- data[i, ]$genus
    family <- data[i, ]$family
    order <- data[i, ]$order
    class <- data[i, ]$class
    telo_1 <- data[i, ]$telo_seq_1
    telo_2 <- data[i, ]$telo_seq_2
    type <- data[i, ]$type

    if (!is.na(genus)) {
        cat(paste(
            "|", paste0("*", species, "*", collapse = ""),
            "|", family, "|", order, "|", class,
            "|", telo_1, "|", telo_2, "|", type,
            "|\n"
        ))
    }
}