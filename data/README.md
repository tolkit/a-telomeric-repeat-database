# Taxa with tricky TR's

There are a few species for which no telomeric repeat has been found, or for which the current estimate does not look right. This could either be genuine; some species will not have typical telomeric repeats (e.g. *Drosophila melanogaster*). However, the parameters used for the initial run on TIDK are not optimised to find long telomeric repeats, as you may find in fungi for example.

Note if the second most common telomeric repeat looks credible, that species will not appear in this list.

## List to correct

I'm going to manually go through these.

```bash
mbMem=5000; bsub -n 30 -q long -R"span[hosts=1] select[mem>${mbMem}] rusage[mem=${mbMem}]" -M${mbMem} -Is bash
```

### Agaricomycetes 
- Laetiporus sulphureus (AACCT)
### Arachnida
- Amaurobius ferox (no clear telomeric repeat)
- Atypus affinis (AAAATTGTTGATGGAGATCATAC)
### Bryopsida
- Hylocomiadelphus triquetrus (AAACCCT)
- Rhytidiadelphus loreus (AAACCCT)
- Thamnobryum alopecurum (AAACCCT)
- Thuidium delicatulum (AAACCCT)
- Thuidium tamariscinum (AAACCCT)
### Chlorophyceae
- Brachiomonas submarina (AAGGATGGAC)
- Dunaliella primolecta (AACCCT)
### Colpodea
- Colpoda steinii (not resolved)
### Enoplea
- Dioctophyme renale (still unknown)
### Gastropoda
- Patella pellucida (check)
- Gibbula magus	(check)
### Gymnolaemata (all look a bit off)
- Bugulina stolonifera (ACTACT, AATGCTCATATAGT?)
- Cryptosula pallasiana (AATAAT, AAATACGCACACGGT?)
- Membranipora membranacea
### Hexanauplia
- Sacculina carcini	(check)
### Insecta
- Dromius quadrimaculatus (AACCT)
- Chilocorus renipustulatus
- Melolontha melolontha (AAATCCG, AGATCCG)
#### Diptera
- Acrocera orbiculus (AACAAGC, ACTGCTCCG?)
- Bibio marci (not resolved)
- Bombylius discolor (AAGTG)
- Clusia tigrina (AGAGAT, AAATTAATTCCAACATTGTGT?)
- Cheilosia pagana (not convinced about any Cheilosia yet...)
- Cheilosia soror
- Cheilosia vulpina
- Scaeva pyrastri (assembly)
#### Ephemeroptera
- Cloeon dipterum (not resolved)
- Ecdyonurus torrentis (ACTCACTC, AATGAATG?)
- Rhithrogena germanica (ACCGCGGACGGCGC?)
#### Hemiptera
- Gonocerus acuteangulatus (AACCATCCCT)
- Pantilius tunicatus (AACCATCCCT)
- Aelia acuminata (pacbio)
- Eurydema oleracea (AACCATCCCT)
#### Hymenoptera
- Andrena dorsata (AAAGGGCATGAGGGT)
- Andrena hattorfiana
- Hylaeus communis (AACCAACCT, AACCCAGACCT)
- Ectemnius continuus (AACCCAGACCT)
- Mimumesa dahlbomi (ACCTG, AACCT)

Something going on with the Lasioglossums

- Lasioglossum calceatum
- Lasioglossum leucozonium (AAGTGGTC, AACCCAGACCT, AAACCAGACCGCTCTAAGTCGTCCGAG)
- Lasioglossum pauxillum
- Buathra laborator

The Megachiles have second best hit as the common telomeric repeat.

- Megachile ligniseca (ACAGAG)
- Megachile willughbiella
- Macropis europaea (AACCC?)
- Anoplius nigerrimus (AACCCAGACCT)

Symphyta has really poor TR estimates for some reason.

- Athalia cordata (ACGATG)
- Athalia rosae (not)
- Tenthredo notha (AACCT)
- Ancistrocerus nigricornis (AACCCAGACCC)
#### Lepidoptera
- Ectropis crepuscularia (AACCT)
#### Magnoliopsida
- Lathyrus linifolius
- Filipendula ulmaria
#### Mammalia
- Cervus elaphus
#### Mucoromycetes
- Mucor piriformis (AACCCTCGCAGGCCGTAGGCCGTGGGTGCT)
#### Saccharomycetes
- Metschnikowia zobellii
#### Sordariomycetes
- Trichoderma pseudokoningii