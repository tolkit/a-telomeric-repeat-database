#!/usr/bin/env python3
"""Build the database from the tidk 0.3.0 calls, keeping the tidk 0.2
entries for species the 0.3.0 run doesn't cover, and write the README and
per-class tables.

Inputs (run src/import_tidk_v03.py first):
  data/tidk_v0.3/telo_calls.tsv   tidk 0.3.0, one curated assembly per
                                  Darwin species, checked at chromosome ends
  data/telo_database.tsv          tidk 0.2 (2021-2023), raw: the most
                                  abundant repeats in an assembly or PacBio
                                  reads, not checked at chromosome ends

Outputs:
  data/telo_database_v2.tsv       one row per species and source
  README.md                       summary by class, then the full table
  clades/<class>/README.md        the table for each class

Run from src/: python3 make_database_v2.py
"""
import csv
import re
import shutil
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import import_tidk_v03

ROOT = Path(__file__).resolve().parent.parent
CALLS = ROOT / "data" / "tidk_v0.3" / "telo_calls.tsv"
OLD_DB = ROOT / "data" / "telo_database.tsv"
OUT_DB = ROOT / "data" / "telo_database_v2.tsv"
CLADES = ROOT / "clades"

RANKS = ["species", "genus", "family", "order", "class", "phylum", "kingdom", "superkingdom"]
COLS = ["taxon_id", *RANKS, "telomere_unit", "support", "ends_with_telomere",
        "ends_checked", "t2t_sequences", "source", "assembly", "telo_seq_2"]
SOURCE_V03 = "tidk 0.3.0 assembly"
SUPPORT_TEXT = {
    "strong": "strong",
    "weak": "weak",
    "none": "none",
    "unchecked": "not checked",
}


def norm(name):
    return re.sub(r"[^a-z]", "", name.lower())


def is_dna(s):
    return bool(s) and set(s) <= set("ACGT")


def load_rows():
    with open(CALLS) as fh:
        new = list(csv.DictReader(fh, delimiter="\t"))
    rows = []
    for r in new:
        rows.append({**{k: r[k] for k in ["taxon_id", *RANKS]},
                     "telomere_unit": r["telomere_unit"], "support": r["support"],
                     "ends_with_telomere": r["ends_with_telomere"],
                     "ends_checked": r["ends_checked"],
                     "t2t_sequences": r["t2t_sequences"],
                     "source": SOURCE_V03, "assembly": r["assembly"], "telo_seq_2": ""})
    covered = {norm(r["species"]) for r in new}
    with open(OLD_DB) as fh:
        old = [r for r in csv.DictReader(fh, delimiter="\t")
               if norm(r["species"]) not in covered]
    lineages = ncbi_lineages({norm(r["species"]) for r in old})
    for r in old:
        lin = lineages.get(norm(r["species"]))
        if lin is None and not r["genus"]:
            # no taxonomy anywhere: misnamed entries (e.g. ANDRENA HAEM)
            continue
        if lin is not None:
            taxonomy = {"taxon_id": lin["taxid"], **{k: lin[k] for k in RANKS}}
        else:
            taxonomy = {k: r[k].strip('"') for k in ["taxon_id", *RANKS]}
        rows.append({**taxonomy,
                         "telomere_unit": r["telo_seq_1"] if is_dna(r["telo_seq_1"]) else "",
                         "support": "unchecked", "ends_with_telomere": "",
                         "ends_checked": "", "t2t_sequences": "",
                         "source": f"tidk 0.2 {r['type']}", "assembly": "",
                         "telo_seq_2": r["telo_seq_2"] if is_dna(r["telo_seq_2"]) else ""})
    keys = ("superkingdom", "kingdom", "phylum", "class", "order", "family", "species", "source")
    rows.sort(key=lambda r: tuple(r[k] or "~" for k in keys))
    return rows


def ncbi_lineages(names):
    """Normalised species name -> NCBI lineage (as in import_tidk_v03.py),
    so the tidk 0.2 rows are classified the same way as the 0.3.0 calls
    rather than by the 2021 GoaT taxonomy."""
    merged = import_tidk_v03.load_merged()
    taxids = import_tidk_v03.load_taxids()
    taxids = {n: merged.get(taxids[n], taxids[n]) for n in names if n in taxids}
    lineages = import_tidk_v03.load_lineages(set(taxids.values()))
    # names ToLQC doesn't know, or knows by a taxid NCBI no longer has
    # (Colpoda steinii): NCBI names, then synonyms
    rest = {n for n in names if taxids.get(n) not in lineages}
    for n, t in import_tidk_v03.ncbi_names(rest).items():
        taxids[n] = merged.get(t, t)
    lineages.update(import_tidk_v03.load_lineages(
        {taxids[n] for n in rest if n in taxids} - lineages.keys()))
    return {n: lineages[t] for n, t in taxids.items() if t in lineages}


def ends_text(r):
    if r["ends_checked"] in ("", "0"):
        return ""
    return f"{r['ends_with_telomere']}/{r['ends_checked']}"


def table(rows, with_class=True):
    head = ["Species", "Family", "Order"] + (["Class"] if with_class else []) + \
           ["Telomeric repeat", "Support", "Ends with repeat", "Source"]
    out = ["| " + " | ".join(head) + " |", "|" + " --- |" * len(head)]
    for r in rows:
        cells = [f"*{r['species']}*", r["family"], r["order"]] + \
                ([r["class"]] if with_class else []) + \
                [r["telomere_unit"], SUPPORT_TEXT[r["support"]], ends_text(r), r["source"]]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def class_summary(rows):
    by = defaultdict(list)
    for r in rows:
        if r["source"] == SOURCE_V03:
            by[r["class"] or r["phylum"] or "(unclassified)"].append(r)
    out = ["| Class | Species | Strong | Weak | None | Commonest strong calls |",
           "| --- | --- | --- | --- | --- | --- |"]
    for cls, rs in sorted(by.items(), key=lambda x: (-len(x[1]), x[0])):
        s = Counter(r["support"] for r in rs)
        common = Counter(r["telomere_unit"] for r in rs if r["support"] == "strong")
        calls = ", ".join(f"{u} ({n})" for u, n in common.most_common(3))
        out.append(f"| {cls} | {len(rs)} | {s['strong']} | {s['weak']} | {s['none']} | {calls} |")
    return "\n".join(out)


INTRO = """# A Telomeric Repeat Database

Telomeric repeats of Darwin Tree of Life species, found de novo with
[tidk](https://github.com/tolkit/telomeric-identifier).

Since {today}, the database is built from a tidk 0.3.0 run over one
curated assembly for each of {n_v03:,} Darwin Tree of Life species. For each
assembly, `tidk explore` finds tandem repeats, and `tidk ends` checks
candidates at every chromosome end (sequences of at least 1 Mb): the top
five explore units, plus known telomeric units
([list](data/tidk_v0.3/known_telomere_units.tsv)).
The telomeric repeat is the candidate found at the most chromosome ends.

Earlier entries (tidk 0.2, 2021-2023) were the most abundant repeat in an
assembly or in PacBio reads, and were not checked at chromosome ends, so
many were satellites. They are kept, marked "not checked", only for the
{n_old:,} species the 0.3.0 run doesn't cover; the original table is in
`data/telo_database.tsv`.

**Support** is how much of the assembly backs the call:

- **strong**: the repeat is at 25% or more of the chromosome ends checked
- **weak**: at fewer, but at least one
- **none**: at no chromosome end; the repeat shown is then the most
  abundant tandem repeat in the assembly, which is not a telomere call

Weak or no support is often the assembly rather than the biology: few
vertebrate chromosomes, for example, are assembled end to end. Taxa without
a canonical telomere (most Diptera, for example) also fall here.

Repeats are written as tidk reports them: the lexicographically smallest
rotation of the repeat or its reverse complement, so AAACCCT is the
TTTAGGG telomere and AACCT is TTAGG.

See `src/README.md` for the pipeline, and the `clades` directory for a
table per class. The data are in `data/telo_database_v2.tsv`.

## Summary by class (tidk 0.3.0)

{summary}

## All species

{table}
"""


def main():
    rows = load_rows()
    with open(OUT_DB, "w") as out:
        print("\t".join(COLS), file=out)
        for r in rows:
            print("\t".join(r[c] for c in COLS), file=out)

    n_v03 = sum(r["source"] == SOURCE_V03 for r in rows)
    n_old = len({r["species"] for r in rows if r["source"] != SOURCE_V03})
    with open(ROOT / "README.md", "w") as out:
        out.write(INTRO.format(today=date.today().isoformat(), n_v03=n_v03, n_old=n_old,
                               summary=class_summary(rows), table=table(rows)))

    # per class, replacing the old tables
    by_class = defaultdict(list)
    for r in rows:
        # some lineages have no class rank (e.g. haptophytes): use the phylum
        cls = r["class"] or r["phylum"]
        if cls:
            by_class[cls].append(r)
    for d in CLADES.iterdir():
        if d.is_dir() and d.name not in by_class:
            shutil.rmtree(d)
    for cls, rs in by_class.items():
        (CLADES / cls).mkdir(parents=True, exist_ok=True)
        with open(CLADES / cls / "README.md", "w") as out:
            out.write(f"# {cls}\n\n{table(rs, with_class=False)}\n")

    print(f"[make_database_v2] {len(rows)} rows ({n_v03} tidk 0.3.0, "
          f"{len(rows) - n_v03} tidk 0.2 for {n_old} species), {len(by_class)} classes")


if __name__ == "__main__":
    main()
