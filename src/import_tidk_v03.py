#!/usr/bin/env python3
"""Import the ToL-wide tidk 0.3.0 telomere calls into the database, with
NCBI taxonomy, and compare them with the earlier tidk 0.2 entries.

The tidk 0.3.0 run (one curated assembly per Darwin Tree of Life species,
2026-10-08) lives in its own project, TOL_DIR. For each species tidk
explore finds tandem repeats, and tidk ends checks the top five at each
chromosome end; the telomere call is the candidate at the most ends. That
end check is what the 0.2 entries here lacked: they are the most abundant
repeat in the assembly or reads, telomeric or not.

Writes, under data/tidk_v0.3/:
  telo_calls.tsv   one row per species: taxonomy, the telomere call and its
                   support (chromosome ends with it out of those checked)
  comparison.tsv   species with both a 0.3.0 call and a 0.2 entry (raw
                   assembly / raw PacBio / manually curated), and how the
                   calls relate
and prints a summary.

Run from src/: python3 import_tidk_v03.py

Support levels (telo_calls.tsv `support`):
  strong   the call is at >= 25% of chromosome ends checked
  weak     at fewer, but at least one
  none     at no chromosome end (telomere_unit is then the top explore
           unit, or empty if explore found nothing)
Chromosome ends are those of sequences >= 1 Mb. Few vertebrate
chromosomes are assembled end to end, so "weak" there is often assembly
rather than biology.

Units are as tidk reports them: the lexicographically smallest rotation of
the repeat or its reverse complement (AAACCCT for TTTAGGG), so they compare
directly with the 0.2 entries once those are reduced to their primitive
unit (AAACCCTAAACCCT -> AAACCCT).
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOL_DIR = Path("/lustre/scratch122/tol/teams/blaxter/users/mb39/tol_telomeres")
TAX_DIR = Path("/data/tol/resources/taxonomy/2026-10-03")
OUT_DIR = ROOT / "data" / "tidk_v0.3"
OLD_DB = ROOT / "data" / "telo_database.tsv"
CURATED = ROOT / "data" / "curated" / "manually_curated_2021-09-24.tsv"

RANKS = ["species", "genus", "family", "order", "class", "phylum", "kingdom", "superkingdom"]
STRONG = 0.25

COMPLEMENT = str.maketrans("ACGT", "TGCA")


def lex_min(s):
    """Lexicographically smallest rotation of s or its reverse complement."""
    rc = s.translate(COMPLEMENT)[::-1]
    return min(min(x[i:] + x[:i] for i in range(len(x))) for x in (s, rc))


def primitive_unit(s):
    """As tidk 0.3.0: canonicalise, reduce to the smallest exact period,
    canonicalise again."""
    canon = lex_min(s)
    n = len(canon)
    for p in range(1, n + 1):
        if n % p == 0 and canon == canon[:p] * (n // p):
            return lex_min(canon[:p])
    return canon


def relation(old, new):
    """same: the 0.2 entry reduces to the 0.3.0 unit; compound: it contains
    a full copy of it in a longer, mixed string; different: neither."""
    old_unit = primitive_unit(old)
    if old_unit == new:
        return "same"
    rc = old.translate(COMPLEMENT)[::-1]
    rotations = {new[i:] + new[:i] for i in range(len(new))}
    if any(r in s for r in rotations for s in (old, rc)):
        return "compound"
    return "different"


def norm(name):
    """Species names differ in punctuation between the Darwin directories
    (Acaena_novae_zelandiae) and NCBI (Acaena novae-zelandiae)."""
    return re.sub(r"[^a-z]", "", name.lower())


def is_dna(s):
    return bool(s) and set(s) <= set("ACGT")


def load_taxids():
    """Normalised species name -> NCBI taxid, from the ToLQC species names
    (the names the Darwin directories are made from), then NCBI scientific
    names for any left over."""
    taxids = {}
    with open(TAX_DIR / "tolqc_species_names.tsv") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            taxids.setdefault(norm(row["id"]), row["taxon_id"])
    return taxids


def ncbi_names(wanted):
    """Normalised name -> taxid from names.dmp, for the names in `wanted`:
    scientific names first, then synonyms (Inachis io -> Aglais io)."""
    found, synonyms = {}, {}
    with open(TAX_DIR / "new_taxdump" / "names.dmp") as fh:
        for line in fh:
            parts = line.split("\t|\t")
            n = norm(parts[1])
            if n not in wanted:
                continue
            if parts[3].startswith("scientific name"):
                found.setdefault(n, parts[0])
            elif parts[3].startswith(("synonym", "equivalent name", "authority")):
                synonyms.setdefault(n, parts[0])
    return {**synonyms, **found}


def load_merged():
    merged = {}
    with open(TAX_DIR / "new_taxdump" / "merged.dmp") as fh:
        for line in fh:
            old, new = line.rstrip("\t|\n").split("\t|\t")
            merged[old] = new
    return merged


def load_lineages(taxids):
    """taxid -> {rank: name} from rankedlineage.dmp (tax_id, tax_name,
    species, genus, family, order, class, phylum, kingdom, superkingdom)."""
    lineages = {}
    with open(TAX_DIR / "new_taxdump" / "rankedlineage.dmp") as fh:
        for line in fh:
            taxid = line[:line.index("\t")]
            if taxid not in taxids:
                continue
            # fields end "\t|"; empty ranks are empty fields, trailing ones too
            parts = [p.strip() for p in line.rstrip("\n").split("\t|")][:-1]
            lin = dict(zip(["taxid", "tax_name"] + RANKS, parts))
            # a species' own name is tax_name; `species` is filled only below species rank
            lin["species"] = lin["species"] or lin["tax_name"]
            lineages[taxid] = lin
    return lineages


def load_old():
    """Normalised species name -> {type: telo_seq_1}, for the raw 0.2
    entries (type assembly / pacbio) and the curated list (type curated)."""
    old = {}
    for path, kind in ((OLD_DB, None), (CURATED, "curated")):
        with open(path) as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                seq = row["telo_seq_1"].strip()
                if not is_dna(seq):
                    continue
                name = row["species"] or row.get("scientific_name", "")
                old.setdefault(norm(name), {})[kind or row["type"]] = seq
    return old


def main():
    assemblies = {}
    with open(TOL_DIR / "inputs" / "tol_latest_assemblies.txt") as fh:
        for line in fh:
            species, fasta = line.rstrip("\n").split("\t")
            m = re.search(r"/curated/([^/]+)/", fasta)
            assemblies[species] = m.group(1) if m else ""
    with open(TOL_DIR / "outputs" / "summary.tsv") as fh:
        calls = list(csv.DictReader(fh, delimiter="\t"))

    taxids = load_taxids()
    missing = {norm(c["species"]) for c in calls} - taxids.keys()
    taxids.update(ncbi_names(missing))
    merged = load_merged()
    wanted = {merged.get(t, t) for t in taxids.values()}
    lineages = load_lineages(wanted)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cols = ["taxon_id", *RANKS, "darwin_group", "assembly", "telomere_unit",
            "support", "ends_with_telomere", "ends_checked", "t2t_sequences",
            "minor_strand", "telomere_rank", "top_explore_unit"]
    out_rows, no_taxonomy = [], []
    for c in calls:
        n = norm(c["species"])
        taxid = taxids.get(n, "")
        taxid = merged.get(taxid, taxid)
        lin = lineages.get(taxid)
        if lin is None:
            no_taxonomy.append(c["species"])
            lin = {r: "" for r in RANKS}
            lin["species"] = c["species"].replace("_", " ")
        seqs = int(c["sequences"] or 0)
        t2t, one = int(c["t2t"] or 0), int(c["one_end"] or 0)
        present, checked = 2 * t2t + one, 2 * seqs
        if present == 0:
            support = "none"
        elif present >= STRONG * checked:
            support = "strong"
        else:
            support = "weak"
        unit = c["telomere_unit"] if present else c["top_unit"]
        out_rows.append(dict(
            taxon_id=taxid if lin.get("taxid") else "", **{r: lin[r] for r in RANKS},
            darwin_group=c["group"], assembly=assemblies.get(c["species"], ""),
            telomere_unit=unit, support=support,
            ends_with_telomere=present, ends_checked=checked, t2t_sequences=t2t,
            minor_strand=c["telomere_minor_strand"] if present else c["top_minor_strand"],
            telomere_rank=c["telomere_rank"] if present else "",
            top_explore_unit=c["top_unit"],
            _norm=n,
        ))
    out_rows.sort(key=lambda r: tuple(r[k] for k in
                  ("superkingdom", "kingdom", "phylum", "class", "order", "family", "species")))
    with open(OUT_DIR / "telo_calls.tsv", "w") as out:
        print("\t".join(cols), file=out)
        for r in out_rows:
            print("\t".join(str(r[k]) for k in cols), file=out)

    # compare with the 0.2 entries
    old = load_old()
    comp_cols = ["species", "class", "order", "support", "telomere_unit",
                 "old_type", "old_telo_seq_1", "old_unit", "relation"]
    comp = []
    for r in out_rows:
        for kind, seq in sorted(old.get(r["_norm"], {}).items()):
            rel = relation(seq, r["telomere_unit"]) if r["telomere_unit"] else "none"
            comp.append(dict(species=r["species"], **{"class": r["class"]}, order=r["order"],
                             support=r["support"], telomere_unit=r["telomere_unit"],
                             old_type=kind, old_telo_seq_1=seq,
                             old_unit=primitive_unit(seq), relation=rel))
    with open(OUT_DIR / "comparison.tsv", "w") as out:
        print("\t".join(comp_cols), file=out)
        for r in comp:
            print("\t".join(str(r[k]) for k in comp_cols), file=out)

    print(f"[import_tidk_v03] {len(out_rows)} species -> {OUT_DIR / 'telo_calls.tsv'}", file=sys.stderr)
    print(f"  no NCBI taxonomy: {len(no_taxonomy)} {no_taxonomy[:10]}", file=sys.stderr)
    print(f"  support: {dict(Counter(r['support'] for r in out_rows))}", file=sys.stderr)
    old_species = set(old)
    new_species = {r["_norm"] for r in out_rows}
    print(f"  0.2 species: {len(old_species)}; also in 0.3.0: {len(old_species & new_species)}; "
          f"new in 0.3.0: {len(new_species - old_species)}", file=sys.stderr)
    for kind in ("assembly", "pacbio", "curated"):
        rel = Counter((r["support"], r["relation"]) for r in comp if r["old_type"] == kind)
        print(f"  vs {kind}: " + ", ".join(f"{s}/{x}:{n}" for (s, x), n in sorted(rel.items())),
              file=sys.stderr)


if __name__ == "__main__":
    main()
