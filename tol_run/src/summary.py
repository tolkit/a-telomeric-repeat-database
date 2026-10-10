#!/usr/bin/env python3
"""Per-species summary of the ToL-wide tidk 0.3.0 run (src/run_tidk.bash).

For each species in the assembly list with explore output:
  - its Darwin group (the directory under /data/tol/data/darwin)
  - the top explore unit, its copies and the proportion on the minor
    strand (a telomeric repeat reads both ways round, at the two
    chromosome ends)
  - the telomere call: of the top explore units and the known telomeric
    units (inputs/known_telomere_units.tsv) checked with tidk ends, the one
    at the most chromosome ends (2 x T2T + one end; ties go to
    the higher explore rank). The top explore unit isn't always the
    telomere - a long subterminal satellite can have more copies near the
    ends - so this, not top_unit, is the species' telomeric repeat. Falls
    back to the ends for the top explore unit if there are no candidates.
    telomere_source says which: explore (a top explore unit), discovered
    (found by tidk ends itself, when explore found nothing) or known;
    telomere_rank is the call's explore rank, empty if explore didn't
    report it.
  - tidk ends for the telomere call: sequences checked, T2T / one end /
    no ends, and flagged ends

This is tr_tert's src/tidk_v03_summary.py without the tidk 0.2.7
comparison, so the two agree on the shared columns.

Usage:
  summary.py [outfile]    # default outputs/summary.tsv

Columns:
  species  group  top_unit  top_copies  top_minor_strand  telomere_unit
  telomere_rank  telomere_source  telomere_copies  telomere_minor_strand  sequences  t2t
  one_end  no_ends  wrong_strand  not_terminal
"""
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def env_path(name, default):
    p = Path(os.environ.get(name, default))
    return p if p.is_absolute() else PROJECT_ROOT / p


ASSEMBLY_LIST = env_path("ASSEMBLY_LIST", "inputs/tol_latest_assemblies.txt")
EXPLORE_DIR = env_path("EXPLORE_DIR", "outputs/explore")
ENDS_DIR = env_path("ENDS_DIR", "outputs/ends")
DARWIN_ROOT = Path("/data/tol/data/darwin")


def group_of(fasta):
    try:
        return Path(fasta).relative_to(DARWIN_ROOT).parts[0]
    except ValueError:
        return ""


def load_explore_rows(species):
    """{unit: (copies, minor strand proportion)} and the units in rank
    order; None if there's no explore output."""
    path = EXPLORE_DIR / f"{species}.explore.tsv"
    if not path.exists():
        return None
    rows, order = {}, []
    with open(path) as fh:
        next(fh, None)
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            unit, copies, as_unit, as_revcomp = parts[:4]
            minor = None
            if as_unit != "NA" and int(as_unit) + int(as_revcomp) > 0:
                u, r = int(as_unit), int(as_revcomp)
                minor = min(u, r) / (u + r)
            rows[unit] = (int(copies), minor)
            order.append(unit)
    return rows, order


def fmt_minor(minor):
    return "NA" if minor is None else f"{minor:.3f}"


def present_ends(ends):
    return 2 * ends["t2t"] + ends["one_end"]


def candidate_files():
    """species -> [(file name, ends summary)] for the candidate ends JSONs,
    from one listing of the candidates directory, read concurrently: there
    are ~100,000, and one at a time they take ~30 min on lustre. Names are
    <species>.<rank or "known">.<unit>.ends.json, and species names
    contain no dots."""
    with os.scandir(ENDS_DIR / "candidates") as it:
        paths = [Path(e.path) for e in it if e.name.endswith(".ends.json")]
    with ThreadPoolExecutor(max_workers=64) as pool:
        summaries = pool.map(lambda p: json.loads(p.read_text()), paths)
    files = {}
    for path, ends in zip(paths, summaries):
        files.setdefault(path.name.split(".")[0], []).append((path.name, ends))
    return files


def telomere_call(species, order, candidates):
    """(explore rank, source, ends summary) of the candidate unit at the
    most chromosome ends. Candidates are:
      explore     the top explore units (<species>.<rank>.<unit>)
      discovered  the main run's ends (<species>.ends.json): the top explore
                  unit, or, if explore found nothing, the unit tidk ends
                  discovered at the sequence ends itself
      known       the known telomeric units (<species>.known.<unit>,
                  src/run_known_units.bash)
    A candidate's rank is its explore rank, or None if explore didn't
    report it. Ties go to the higher explore rank, then to explore, then
    discovered, then known units, so a species with no repeat at any end
    keeps the top explore (or discovered) unit."""
    ranks = {u: i + 1 for i, u in enumerate(order)}
    priority = {"explore": 2, "discovered": 1, "known": 0}
    cands = []
    for name, ends in candidates.get(species, []):
        tag = name[len(species) + 1:].split(".")[0]
        if tag.isdigit():
            cands.append((int(tag), "explore", ends))
        elif tag == "known" and present_ends(ends) > 0:
            # a known unit is a call only where it's at an end; otherwise a
            # species with no repeat at all would get an arbitrary one
            cands.append((ranks.get(ends["unit"]), "known", ends))
    path = ENDS_DIR / f"{species}.ends.json"
    if path.exists():
        ends = json.load(open(path))
        rank = ranks.get(ends["unit"])
        cands.append((rank, "explore" if rank else "discovered", ends))
    if not cands:
        return (None, "", {})
    return max(cands, key=lambda c: (present_ends(c[2]),
                                     -(c[0] if c[0] is not None else float("inf")),
                                     priority[c[1]]))


def main():
    outfile = sys.argv[1] if len(sys.argv) > 1 else PROJECT_ROOT / "outputs" / "summary.tsv"
    cols = ["species", "group", "top_unit", "top_copies", "top_minor_strand",
            "telomere_unit", "telomere_rank", "telomere_source", "telomere_copies",
            "telomere_minor_strand", "sequences", "t2t", "one_end", "no_ends",
            "wrong_strand", "not_terminal"]
    rows = []
    candidates = candidate_files()
    for line in open(ASSEMBLY_LIST):
        species, _, fasta = line.rstrip("\n").partition("\t")
        if not species:
            continue
        explore = load_explore_rows(species)
        if explore is None:
            continue
        rows_by_unit, order = explore
        top = order[0] if order else ""
        top_copies, top_minor = rows_by_unit[top] if top else (0, None)
        rank, source, ends = telomere_call(species, order, candidates)
        tel = ends.get("unit", "")
        tel_copies, tel_minor = rows_by_unit.get(tel, ("", None))
        rows.append(dict(
            species=species, group=group_of(fasta),
            top_unit=top, top_copies=top_copies,
            top_minor_strand=fmt_minor(top_minor),
            telomere_unit=tel, telomere_rank="" if rank is None else rank,
            telomere_source=source,
            telomere_copies=tel_copies,
            telomere_minor_strand=fmt_minor(tel_minor),
            sequences=ends.get("sequences", ""),
            t2t=ends.get("t2t", ""), one_end=ends.get("one_end", ""),
            no_ends=ends.get("no_ends", ""),
            wrong_strand=len(ends.get("wrong_strand", [])) if ends else "",
            not_terminal=len(ends.get("not_terminal", [])) if ends else "",
        ))
    with open(outfile, "w") as out:
        print("\t".join(cols), file=out)
        for r in rows:
            print("\t".join(str(r[c]) for c in cols), file=out)
    print(f"[summary] {len(rows)} species -> {outfile}", file=sys.stderr)


if __name__ == "__main__":
    main()
