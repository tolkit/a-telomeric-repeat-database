# Taxa with tricky TR's

There are a few species for which no telomeric repeat has been found, or for which the current estimate does not look right. This could either be genuine; some species will not have typical telomeric repeats (e.g. *Drosophila melanogaster*). However, the parameters used for the initial run on TIDK are not optimised to find long telomeric repeats, as you may find in fungi for example.

Note if the second most common telomeric repeat looks credible, that species will not appear in this list.

## List to correct

I'm going to manually go through these.

```bash
mbMem=5000; bsub -n 30 -q long -R"span[hosts=1] select[mem>${mbMem}] rusage[mem=${mbMem}]" -M${mbMem} -Is bash
```

Agaricomycetes 
- Laetiporus sulphureus (/lustre/scratch116/tol/projects/darwin/data/fungi/Laetiporus_sulphureus/genomic_data/gfLaeSulp1/pacbio/fasta/m64229e_210602_121910.ccs.bc1020_BAK8B_OA--bc1020_BAK8B_OA.filtered.fasta.gz) - AACCT
Arachnida
- Amaurobius ferox (no clear telomeric repeat.)
- Atypus affinis (AAAATTGTTGATGGAGATCATAC)
Bryopsida
- Hylocomiadelphus triquetrus (AAACCCT)
- Rhytidiadelphus loreus (AAACCCT)
- Thamnobryum alopecurum (AAACCCT)
- Thuidium delicatulum (AAACCCT)
- Thuidium tamariscinum (AAACCCT)
Chlorophyceae
- Brachiomonas submarina (AAGGATGGAC)
- Dunaliella primolecta (AAACCCT)
Colpodea
- Colpoda steinii (still unknown)
Enoplea
- Dioctophyme renale (?)
Gastropoda
- Patella pellucida (check)
- Gibbula magus	(check)
Gymnolaemata (all look a bit off)
- Bugulina stolonifera
- Cryptosula pallasiana
- Membranipora membranacea
Hexanauplia
- Sacculina carcini	(check)
Insecta
- Dromius quadrimaculatus
- Chilocorus renipustulatus
- Melolontha melolontha (check)
    Diptera
- Acrocera orbiculus
- Bibio marci
- Bombylius discolor
- Clusia tigrina
- Cheilosia pagana
- Cheilosia soror
- Cheilosia vulpina
- Scaeva pyrastri (assembly)
- Cloeon dipterum
- Ecdyonurus torrentis
- Rhithrogena germanica
- Gonocerus acuteangulatus
- Pantilius tunicatus
- Aelia acuminata (pacbio)
- Eurydema oleracea
- Andrena dorsata
- Andrena hattorfiana
- Hylaeus communis
- Ectemnius continuus (pacbio & assembly)
- Mimumesa dahlbomi
Something going on with the Lasioglossums
- Lasioglossum calceatum
- Lasioglossum leucozonium
- Lasioglossum pauxillum
- Buathra laborator
The Megachiles have second best hit as the common telomeric repeat.
- Megachile ligniseca
- Megachile willughbiella
- Macropis europaea
- Anoplius nigerrimus
Symphyta has really poor TR estimates for some reason.
- Athalia cordata
- Athalia rosae
- Tenthredo notha
- Ancistrocerus nigricornis
Lepidoptera (very boring)
- Ectropis crepuscularia
Magnoliopsida
- Lathyrus linifolius
- Filipendula ulmaria
Mammalia
- Cervus elaphus
Mucoromycetes
- Mucor piriformis
Saccharomycetes
- Metschnikowia zobellii
Sordariomycetes
- Trichoderma pseudokoningii