# ToL-wide telomeres with tidk 0.3.0

Telomeric repeats and telomere-to-telomere status for every Darwin Tree of
Life species with a curated host assembly: phase 4 of the tidk roadmap
(`/software/team301/telomeric-identifier/ROADMAP.md`). The plant
(`../tr_tert`) and clade_discovery (Coleoptera, Araneae, Myriapoda) runs
are subsets of this one, with the same binary and settings.

## Steps

1. **Assembly list.** `inputs/tol_latest_assemblies.txt` (species<TAB>fasta,
   3,422 species, 2026-10-08) from
   `/software/team301/user/mb39/scripts/any_latest_assemblies.bash all`
   (implementation `../irx/src/01_get_assemblies.py`): ToL's designated
   reference where there is one, otherwise the newest curated host
   assembly; never symbionts, hap1 for phased assemblies without a
   reference. 103 species without a usable host assembly are listed in
   `inputs/tol_latest_assemblies.log`.
2. **Reuse the tr_tert results.** `src/seed_from_tr_tert.bash` copies
   tr_tert's plant and clade_discovery outputs for the species whose
   assembly path is unchanged (681). The other 204 are mostly hap1/hap2
   swaps (the tr_tert lists predate the finder following the ToL
   reference) and are rerun.
3. **tidk.** `src/run_tidk.bash` submits one LSF array over the species
   not yet done (`src/worker_tidk.bash`): `tidk explore -m 4 -x 30
   --threshold 100 --distance 0.01`, `tidk ends --min-sequence-length
   1000000` for the top explore unit, and `tidk ends` for each of the top
   5 units. Binary: `bin/tidk-0.3.0` (sha256 0d3aa468..., gitignored).
   Outputs: `outputs/explore/`, `outputs/ends/`, `outputs/ends/candidates/`.
4. **Known telomeric units.** `src/run_known_units.bash` (array,
   `src/worker_known_units.bash`) runs `tidk ends` for each unit in
   `inputs/known_telomere_units.tsv` that isn't in a species' top 5: the
   literature telomeres plus the C-run units called at >= 25% of ends in
   >= 3 species by step 3 (28 units; microsatellites such as AAAT and
   ACAGAG left out). Checking only the top 5 missed telomeres ranked just
   below them (AACCCT 6th in *Scyliorhinus*, under satellites). Outputs:
   `outputs/ends/candidates/<species>.known.<unit>.ends.*`. *Viscum album*
   (27 GB gzipped, ~1 h per unit) was stopped after one unit; it has no
   AAACCCT at any end anyway.
5. **Summary.** `src/summary.py` -> `outputs/summary.tsv`, one row per
   species: Darwin group, top explore unit, and the telomere call (the
   candidate at the most chromosome ends, from the top 5, the main ends
   run, or a known unit found at >= 1 end; `telomere_source`) with its T2T
   counts. Same columns as tr_tert's `src/tidk_v03_summary.py`, minus the
   v0.2.7 comparison, plus `telomere_source`.

## Results (2026-10-08)

3,421 of 3,422 species ran; *Tetramitus jugosus* (protist) has no sequence
of at least 1 Mb, so `tidk ends` has nothing to check. 93 species have no
explore unit and nothing tidk ends can discover at the sequence ends:
recorded as no repeat, not as failures (`src/worker_tidk.bash`).

Telomere call at >=1 chromosome end in 2,990 species; at >=25% of ends in
2,292. Adding the known units (step 4) changed 54 calls, none for the
worse: 9 none -> strong, 7 weak -> strong, 16 none -> weak, and 22 to a
different unit at more ends (mostly AACCCT and AACCT). 24.4% of the 77,074 sequences >=1 Mb are T2T. Per Darwin group
(n; >=25% of ends; commonest calls at >=25% of ends):

| group | n | >=25% ends | calls |
|---|---|---|---|
| insects | 2056 | 1278 | AACCT 1020, ACCTG 29, AACCCAGACCT 23, AACCC 20 |
| dicots | 443 | 414 | AAACCCT 389, AACCCTG 6, AACCCT 5 |
| non-vascular plants | 194 | 179 | AAACCCT 179 |
| birds | 145 | 111 | AACCCT 110 |
| fungi | 111 | 28 | AACCCT 11, AAACCCT 9, AACCT 3 |
| monocots | 83 | 70 | AAACCCT 68, AACCCT 2 |
| other arthropods | 72 | 14 | AACCT 14 (spiders: none) |
| molluscs | 68 | 46 | AACCCT 45 |
| fish / mammals | 66 / 53 | 35 / 26 | AACCCT |
| other animals | ~90 | | AACCCT; bryozoans AAACCCC (5), sponges AGCCCT (2), nematodes AAGCCT (2, the *Caenorhabditis* TTAGGC) |

Insects by order (ToLID prefix; >=25% of ends): Lepidoptera 782/886
(AACCT); Diptera 14/403 (no shared unit: telomerase-less, as known);
Coleoptera 209/317 (AACCT, ACCTG, AACCC); Hymenoptera 186/295 (AACCT 52,
AACCCAGACCT 23 in bees and crabronid wasps, AAAGAACCT 16, AAACAAACCC 15);
Hemiptera 40/72 (AACCATCCCT 17, AACCT 17); Orthoptera 4/14 (AACCC);
Ephemeroptera 0/8.

Vertebrate chromosome ends are mostly not T2T (mammals 8.7%, fish 10.5%,
amphibians 0.1%), so the >=25% cut-off undercounts them: "no call" there is
assembly, not biology.

## Downstream

The calls, with NCBI taxonomy, are imported into
`../a-telomeric-repeat-database` (branch `tidk-0.3`,
`src/import_tidk_v03.py` and `src/make_database_v2.py`), which compares
them with its tidk 0.2 entries.

## Caveats

- "Most ends" can pick a terminal repeat other than the telomere: in
  *Aphodius ater* AAACGATAAT is at 15/62 ends (all correctly oriented) and
  AACCC at 6/62.
- Assemblies with few T2T chromosomes (most vertebrates) give weak calls
  whatever the biology.
