# A Telomeric Repeat Database

Both raw data (PacBio) and Darwin Tree of Life assemblies are used to de-novo identify telomeric repeat sequences.

The program used to infer telomeric repeats is <a href="https://github.com/tolkit/telomeric-identifier">tidk</a>.

See `/src/README.md` for pipeline details.

To note this is not a curated list, it is raw output from tidk, and as such, the values may not be accurate. The list is also being actively updated. The main list is below, but see the `clades` directory to get breakdown by eukaryotic class. It will be immediately noticed that for some clades, tidk is not catching the telomeric repeats.

| Species                          | Family             | Order             | Class           | Telomeric repeat 1 | Telomeric repeat 2 | Data type |
| -------------------------------- | ------------------ | ----------------- | --------------- | ------------------ | ------------------ | --------- |
| *Eimeria tenella*                | Eimeriidae         | Eucoccidiorida    | Conoidasida     | AAACCCT            |                    | assembly  |
| *Apoderus coryli*                | Attelabidae        | Coleoptera        | Insecta         | AACCC              | AACCCAACCC         | assembly  |
| *Apoderus coryli*                | Attelabidae        | Coleoptera        | Insecta         | AAATAATT           |                    | pacbio    |
| *Cantharis rustica*              | Cantharidae        | Coleoptera        | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Cantharis rustica*              | Cantharidae        | Coleoptera        | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Podabrus alpinus*               | Cantharidae        | Coleoptera        | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Rhagonycha fulva*               | Cantharidae        | Coleoptera        | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Rhagonycha fulva*               | Cantharidae        | Coleoptera        | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Dromius quadrimaculatus*        | Carabidae          | Coleoptera        | Insecta         |                    |                    | pacbio    |
| *Nebria brevicollis*             | Carabidae          | Coleoptera        | Insecta         | AAATAACT           | AAACATAC           | pacbio    |
| *Nebria salina*                  | Carabidae          | Coleoptera        | Insecta         |                    |                    | pacbio    |
| *Pterostichus madidus*           | Carabidae          | Coleoptera        | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Pterostichus madidus*           | Carabidae          | Coleoptera        | Insecta         | AATAAT             | ATCCATCC           | pacbio    |
| *Adalia bipunctata*              | Coccinellidae      | Coleoptera        | Insecta         | AAAAATTC           | AACCT              | assembly  |
| *Adalia bipunctata*              | Coccinellidae      | Coleoptera        | Insecta         | AACCT              |                    | pacbio    |
| *Chilocorus renipustulatus*      | Coccinellidae      | Coleoptera        | Insecta         | ACTCTG             | AAATATT            | pacbio    |
| *Coccinella septempunctata*      | Coccinellidae      | Coleoptera        | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Coccinella septempunctata*      | Coccinellidae      | Coleoptera        | Insecta         | AAGTCG             | AACCT              | pacbio    |
| *Harmonia axyridis*              | Coccinellidae      | Coleoptera        | Insecta         | AACCT              |                    | pacbio    |
| *Hippodamia variegata*           | Coccinellidae      | Coleoptera        | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Propylea quattuordecimpunctata* | Coccinellidae      | Coleoptera        | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Rhinocyllus conicus*            | Curculionidae      | Coleoptera        | Insecta         | AGATAGAT           | AGATAGATAGAT       | pacbio    |
| *Agrypnus murinus*               | Elateridae         | Coleoptera        | Insecta         | AACCT              | AAACTAT            | pacbio    |
| *Malachius bipustulatus*         | Melyridae          | Coleoptera        | Insecta         | ACCTG              | ACCTGACCTG         | assembly  |
| *Malachius bipustulatus*         | Melyridae          | Coleoptera        | Insecta         | ACCTG              | ACCTGACCTG         | pacbio    |
| *Oedemera lurida*                | Oedemeridae        | Coleoptera        | Insecta         | ACCTG              | ACCTGACCTG         | pacbio    |
| *Pyrochroa serraticornis*        | Pyrochroidae       | Coleoptera        | Insecta         | ACCTG              | ACCTGACCTG         | assembly  |
| *Pyrochroa serraticornis*        | Pyrochroidae       | Coleoptera        | Insecta         | ACCTG              | ACCTGACCTG         | pacbio    |
| *Melolontha melolontha*          | Scarabaeidae       | Coleoptera        | Insecta         | AAGTAATC           | AAAGAT             | pacbio    |
| *Phosphuga atrata*               | Silphidae          | Coleoptera        | Insecta         | AAGACAGAC          | ACAGACTAG          | pacbio    |
| *Ocypus olens*                   | Staphylinidae      | Coleoptera        | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Ocypus olens*                   | Staphylinidae      | Coleoptera        | Insecta         | AACCT              |                    | pacbio    |
| *Philonthus cognatus*            | Staphylinidae      | Coleoptera        | Insecta         | AACCT              | ACAGACAG           | pacbio    |
| *Acrocera orbiculus*             | Acroceridae        | Diptera           | Insecta         |                    |                    | pacbio    |
| *Machimus atricapillus*          | Asilidae           | Diptera           | Insecta         | ACAGACAG           | AATAC              | pacbio    |
| *Bibio marci*                    | Bibionidae         | Diptera           | Insecta         |                    |                    | assembly  |
| *Bibio marci*                    | Bibionidae         | Diptera           | Insecta         |                    |                    | pacbio    |
| *Bombylius discolor*             | Bombyliidae        | Diptera           | Insecta         |                    |                    | pacbio    |
| *Bombylius major*                | Bombyliidae        | Diptera           | Insecta         | ACTACT             | AATAAT             | pacbio    |
| *Lucilia richardsi*              | Calliphoridae      | Diptera           | Insecta         | AGATAGAT           | ACATACAT           | pacbio    |
| *Clusia tigrina*                 | Clusiidae          | Diptera           | Insecta         |                    |                    | pacbio    |
| *Physocephala rufipes*           | Conopidae          | Diptera           | Insecta         | ACAGACAG           | AAAGACAAGAC        | pacbio    |
| *Sicus ferrugineus*              | Conopidae          | Diptera           | Insecta         | AAGTC              | AAGTCAAGTC         | pacbio    |
| *Thecophora atra*                | Conopidae          | Diptera           | Insecta         | AACCAGCACACG       |                    | pacbio    |
| *Callomyia amoena*               | Platypezidae       | Diptera           | Insecta         | AAATG              | AACAAC             | pacbio    |
| *Stomorhina lunata*              | Rhiniidae          | Diptera           | Insecta         | AACTAGAACTG        | AACAGAACTAG        | pacbio    |
| *Sarcophaga crassimargo*         | Sarcophagidae      | Diptera           | Insecta         | AATAG              | AATAGAATAG         | pacbio    |
| *Sarcophaga variegata*           | Sarcophagidae      | Diptera           | Insecta         | AATAG              | AATAGAATAG         | pacbio    |
| *Scathophaga stercoraria*        | Scathophagidae     | Diptera           | Insecta         | AAGAAT             | AAATC              | pacbio    |
| *Coremacera marginata*           | Sciomyzidae        | Diptera           | Insecta         | AAATT              | AAGAAT             | pacbio    |
| *Baccha elongata*                | Syrphidae          | Diptera           | Insecta         | AACAAC             | ACATGTC            | pacbio    |
| *Cheilosia pagana*               | Syrphidae          | Diptera           | Insecta         |                    |                    | pacbio    |
| *Cheilosia soror*                | Syrphidae          | Diptera           | Insecta         |                    |                    | pacbio    |
| *Cheilosia vulpina*              | Syrphidae          | Diptera           | Insecta         |                    |                    | pacbio    |
| *Chrysotoxum bicinctum*          | Syrphidae          | Diptera           | Insecta         | AAATACAATAC        | AATAC              | assembly  |
| *Chrysotoxum bicinctum*          | Syrphidae          | Diptera           | Insecta         | AAATACAATAC        | AACAAG             | pacbio    |
| *Chrysotoxum verralli*           | Syrphidae          | Diptera           | Insecta         | ATCATC             | ATCATCATC          | pacbio    |
| *Criorhina berberina*            | Syrphidae          | Diptera           | Insecta         | AGGAT              |                    | pacbio    |
| *Epistrophe grossulariae*        | Syrphidae          | Diptera           | Insecta         | ACAGTG             | AAATT              | pacbio    |
| *Episyrphus balteatus*           | Syrphidae          | Diptera           | Insecta         | AATAG              | AAATT              | pacbio    |
| *Eristalinus sepulchralis*       | Syrphidae          | Diptera           | Insecta         | AATAAT             | AAATAAT            | pacbio    |
| *Eristalis arbustorum*           | Syrphidae          | Diptera           | Insecta         | AATAAT             | AAATAAAT           | pacbio    |
| *Eristalis horticola*            | Syrphidae          | Diptera           | Insecta         | AACATGC            | AAGCATC            | pacbio    |
| *Eristalis pertinax*             | Syrphidae          | Diptera           | Insecta         | AACTG              | AAACAAAT           | assembly  |
| *Eristalis pertinax*             | Syrphidae          | Diptera           | Insecta         | AAATAC             | AAGAAT             | pacbio    |
| *Eristalis tenax*                | Syrphidae          | Diptera           | Insecta         | AAGAAT             | AAGAATAAGAAT       | assembly  |
| *Eristalis tenax*                | Syrphidae          | Diptera           | Insecta         | AAGAAT             | ACCATCC            | pacbio    |
| *Eupeodes latifasciatus*         | Syrphidae          | Diptera           | Insecta         | ACCATG             | AATAG              | pacbio    |
| *Melanostoma mellinum*           | Syrphidae          | Diptera           | Insecta         | AACAAC             | AACAACAAC          | pacbio    |
| *Melanostoma scalare*            | Syrphidae          | Diptera           | Insecta         | AATAAT             | AACAAC             | pacbio    |
| *Myathropa florea*               | Syrphidae          | Diptera           | Insecta         | AGCCAGCC           | AAATACAT           | pacbio    |
| *Platycheirus albimanus*         | Syrphidae          | Diptera           | Insecta         | ACGTAG             | ACACAC             | pacbio    |
| *Rhingia campestris*             | Syrphidae          | Diptera           | Insecta         | ACCATCT            | AAATATAG           | pacbio    |
| *Scaeva pyrastri*                | Syrphidae          | Diptera           | Insecta         |                    |                    | assembly  |
| *Scaeva pyrastri*                | Syrphidae          | Diptera           | Insecta         | AACTT              | AATAG              | pacbio    |
| *Sphaerophoria taeniata*         | Syrphidae          | Diptera           | Insecta         | ATCATC             | AAAAA              | pacbio    |
| *Syritta pipiens*                | Syrphidae          | Diptera           | Insecta         | ACACAT             |                    | assembly  |
| *Volucella inanis*               | Syrphidae          | Diptera           | Insecta         | ACAGGTG            | AAATAAC            | assembly  |
| *Volucella inanis*               | Syrphidae          | Diptera           | Insecta         | AAATAAC            | AAATAAT            | pacbio    |
| *Xanthogramma pedissequum*       | Syrphidae          | Diptera           | Insecta         | ACAGACTG           | AATAG              | assembly  |
| *Xanthogramma pedissequum*       | Syrphidae          | Diptera           | Insecta         | ACAGACTG           | ATCATC             | pacbio    |
| *Xylota sylvarum*                | Syrphidae          | Diptera           | Insecta         | AGGATG             | AGGATGAGGATG       | assembly  |
| *Xylota sylvarum*                | Syrphidae          | Diptera           | Insecta         | ACTGACTG           | AGGATG             | pacbio    |
| *Cistogaster globosa*            | Tachinidae         | Diptera           | Insecta         | AATAT              | AATAAT             | pacbio    |
| *Gymnosoma rotundatum*           | Tachinidae         | Diptera           | Insecta         | AATAAT             | ACTAT              | pacbio    |
| *Tachina fera*                   | Tachinidae         | Diptera           | Insecta         | ACTAT              | ACTATACTAT         | assembly  |
| *Tachina fera*                   | Tachinidae         | Diptera           | Insecta         | AATAG              | AATAGAATAG         | pacbio    |
| *Thecocarcelia acutangulata*     | Tachinidae         | Diptera           | Insecta         | AATCAT             | AATCATAATCAT       | pacbio    |
| *Anomoia purmunda*               | Tephritidae        | Diptera           | Insecta         | AATGAT             | AATAAT             | pacbio    |
| *Merzomyia westermanni*          | Tephritidae        | Diptera           | Insecta         | AAAAG              | AAAGT              | pacbio    |
| *Nephrotoma flavescens*          | Tipulidae          | Diptera           | Insecta         | AAAATATG           | AAGTAAT            | pacbio    |
| *Tipula paludosa*                | Tipulidae          | Diptera           | Insecta         | AGATATAT           | AGATAT             | pacbio    |
| *Cloeon dipterum*                | Baetidae           | Ephemeroptera     | Insecta         |                    |                    | pacbio    |
| *Ecdyonurus torrentis*           | Heptageniidae      | Ephemeroptera     | Insecta         |                    |                    | pacbio    |
| *Rhithrogena germanica*          | Heptageniidae      | Ephemeroptera     | Insecta         |                    |                    | pacbio    |
| *Acanthosoma haemorrhoidale*     | Acanthosomatidae   | Hemiptera         | Insecta         | AAACCACCCT         |                    | pacbio    |
| *Gonocerus acuteangulatus*       | Coreidae           | Hemiptera         | Insecta         |                    |                    | pacbio    |
| *Pantilius tunicatus*            | Miridae            | Hemiptera         | Insecta         |                    |                    | pacbio    |
| *Notonecta glauca*               | Notonectidae       | Hemiptera         | Insecta         | AAACCTATCC         |                    | pacbio    |
| *Aelia acuminata*                | Pentatomidae       | Hemiptera         | Insecta         | AACCATCCCT         |                    | assembly  |
| *Aelia acuminata*                | Pentatomidae       | Hemiptera         | Insecta         |                    |                    | pacbio    |
| *Eurydema oleracea*              | Pentatomidae       | Hemiptera         | Insecta         |                    |                    | pacbio    |
| *Andrena dorsata*                | Andrenidae         | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Andrena haemorrhoa*             | Andrenidae         | Hymenoptera       | Insecta         | AAACGAGTC          | AACGAGTCG          | assembly  |
| *Andrena haemorrhoa*             | Andrenidae         | Hymenoptera       | Insecta         | AACGAGTCG          | AAACGAGTC          | pacbio    |
| *Andrena hattorfiana*            | Andrenidae         | Hymenoptera       | Insecta         | AAAAAC             | ACGACG             | pacbio    |
| *Bombus campestris*              | Apidae             | Hymenoptera       | Insecta         | AACCCCAACCT        | AACGTAT            | assembly  |
| *Bombus campestris*              | Apidae             | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Bombus hortorum*                | Apidae             | Hymenoptera       | Insecta         | AACCCCAACCT        | AACGTAT            | assembly  |
| *Bombus hortorum*                | Apidae             | Hymenoptera       | Insecta         | AACCCCAACCT        | AACCT              | pacbio    |
| *Bombus hypnorum*                | Apidae             | Hymenoptera       | Insecta         | AACCCCAACCT        | ACTCT              | assembly  |
| *Bombus pascuorum*               | Apidae             | Hymenoptera       | Insecta         | AAAAAC             | AAAAACGAAAAC       | assembly  |
| *Bombus pascuorum*               | Apidae             | Hymenoptera       | Insecta         | AAAACG             | AACCCCAACCT        | pacbio    |
| *Bombus pratorum*                | Apidae             | Hymenoptera       | Insecta         | AACGAACG           | AACCCCAACCT        | pacbio    |
| *Bombus sylvestris*              | Apidae             | Hymenoptera       | Insecta         | AACCCGAACCT        | AACGTAT            | assembly  |
| *Bombus sylvestris*              | Apidae             | Hymenoptera       | Insecta         | AACCCGAACCT        |                    | pacbio    |
| *Bombus terrestris*              | Apidae             | Hymenoptera       | Insecta         | AACGTAT            | AACCCCAACCT        | assembly  |
| *Bombus terrestris*              | Apidae             | Hymenoptera       | Insecta         | AACCCCAACCT        | AACCT              | pacbio    |
| *Nomada fabriciana*              | Apidae             | Hymenoptera       | Insecta         | AACCT              |                    | assembly  |
| *Nomada fabriciana*              | Apidae             | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Hylaeus communis*               | Colletidae         | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Cerceris rybyensis*             | Crabronidae        | Hymenoptera       | Insecta         | AACCCAGACCT        | AAAAT              | assembly  |
| *Cerceris rybyensis*             | Crabronidae        | Hymenoptera       | Insecta         | AACCCAGACCT        | ACCACT             | pacbio    |
| *Ectemnius continuus*            | Crabronidae        | Hymenoptera       | Insecta         |                    |                    | assembly  |
| *Ectemnius continuus*            | Crabronidae        | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Ectemnius lituratus*            | Crabronidae        | Hymenoptera       | Insecta         | AACCCAGACCT        |                    | assembly  |
| *Ectemnius lituratus*            | Crabronidae        | Hymenoptera       | Insecta         | ACTCACTC           |                    | pacbio    |
| *Mimumesa dahlbomi*              | Crabronidae        | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Nysson spinosus*                | Crabronidae        | Hymenoptera       | Insecta         | AACCCAGACCT        | AACAT              | assembly  |
| *Trypoxylon clavicerum*          | Crabronidae        | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Myrmica ruginodis*              | Formicidae         | Hymenoptera       | Insecta         | AACCT              | AGCAGC             | pacbio    |
| *Lasioglossum calceatum*         | Halictidae         | Hymenoptera       | Insecta         | AACGTAT            | AACGTAC            | pacbio    |
| *Lasioglossum lativentre*        | Halictidae         | Hymenoptera       | Insecta         | AACCCAGACCT        | ACAGACAG           | pacbio    |
| *Lasioglossum leucozonium*       | Halictidae         | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Lasioglossum malachurum*        | Halictidae         | Hymenoptera       | Insecta         | ACATCGT            | AATGAATG           | pacbio    |
| *Lasioglossum morio*             | Halictidae         | Hymenoptera       | Insecta         | AACGTAT            | AACGCAT            | pacbio    |
| *Lasioglossum pauxillum*         | Halictidae         | Hymenoptera       | Insecta         | AGCAGC             | AACCT              | pacbio    |
| *Seladonia tumulorum*            | Halictidae         | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Sphecodes ephippius*            | Halictidae         | Hymenoptera       | Insecta         | AACCCAGACCT        | AGAGATATG          | pacbio    |
| *Sphecodes monilicornis*         | Halictidae         | Hymenoptera       | Insecta         | AACCCAGACCT        | AGATAT             | pacbio    |
| *Amblyteles armatorius*          | Ichneumonidae      | Hymenoptera       | Insecta         | ACGACG             | ATCATC             | pacbio    |
| *Buathra laborator*              | Ichneumonidae      | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Ichneumon xanthorius*           | Ichneumonidae      | Hymenoptera       | Insecta         | AACGAC             | ACGATG             | pacbio    |
| *Scambus nigricans*              | Ichneumonidae      | Hymenoptera       | Insecta         | ACACAC             | ACACAG             | pacbio    |
| *Megachile ligniseca*            | Megachilidae       | Hymenoptera       | Insecta         | ACAGAG             | AACCT              | pacbio    |
| *Megachile willughbiella*        | Megachilidae       | Hymenoptera       | Insecta         | ACAGAG             | AACCT              | pacbio    |
| *Macropis europaea*              | Melittidae         | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Anoplius nigerrimus*            | Pompilidae         | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Evagetes crassicornis*          | Pompilidae         | Hymenoptera       | Insecta         | AACCCAGACCT        |                    | pacbio    |
| *Athalia circularis*             | Tenthredinidae     | Hymenoptera       | Insecta         | ACGACG             | ACGACGACG          | pacbio    |
| *Athalia cordata*                | Tenthredinidae     | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Athalia rosae*                  | Tenthredinidae     | Hymenoptera       | Insecta         | AAAAA              | AAAAAA             | pacbio    |
| *Tenthredo livida*               | Tenthredinidae     | Hymenoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Tenthredo notha*                | Tenthredinidae     | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Ancistrocerus nigricornis*      | Vespidae           | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Dolichovespula media*           | Vespidae           | Hymenoptera       | Insecta         | AACCCAGACGC        | AACGACGATATT       | assembly  |
| *Dolichovespula media*           | Vespidae           | Hymenoptera       | Insecta         | AACCCAGACGC        | ACAGT              | pacbio    |
| *Dolichovespula saxonica*        | Vespidae           | Hymenoptera       | Insecta         | AACCCAGACGC        | AACAGT             | assembly  |
| *Dolichovespula saxonica*        | Vespidae           | Hymenoptera       | Insecta         | AACCCAGACGC        |                    | pacbio    |
| *Vespa crabro*                   | Vespidae           | Hymenoptera       | Insecta         | AATAAT             | AACCCTGACGC        | assembly  |
| *Vespa crabro*                   | Vespidae           | Hymenoptera       | Insecta         |                    |                    | pacbio    |
| *Vespula germanica*              | Vespidae           | Hymenoptera       | Insecta         | AACCCAGACGC        |                    | assembly  |
| *Vespula germanica*              | Vespidae           | Hymenoptera       | Insecta         | AACCCAGACGC        |                    | pacbio    |
| *Vespula vulgaris*               | Vespidae           | Hymenoptera       | Insecta         | AACCCAGACGC        |                    | assembly  |
| *Vespula vulgaris*               | Vespidae           | Hymenoptera       | Insecta         | AACCCAGACGC        |                    | pacbio    |
| *Argyresthia goedartella*        | Argyresthiidae     | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Blastobasis adustella*          | Blastobasidae      | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Blastobasis adustella*          | Blastobasidae      | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Blastobasis lacticolella*       | Blastobasidae      | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Zeuzera pyrina*                 | Cossidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Zeuzera pyrina*                 | Cossidae           | Lepidoptera       | Insecta         | AACCT              | AACAAC             | pacbio    |
| *Agriphila geniculea*            | Crambidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Agriphila straminella*          | Crambidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Catoptria pinella*              | Crambidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Chrysoteuchia culmella*         | Crambidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Chrysoteuchia culmella*         | Crambidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Ostrinia nubilalis*             | Crambidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Parapoynx stratiotata*          | Crambidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Parapoynx stratiotata*          | Crambidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Agonopterix heracliana*         | Depressariidae     | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Habrosyne pyritoides*           | Drepanidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Habrosyne pyritoides*           | Drepanidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Thyatira batis*                 | Drepanidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Eilema depressum*               | Erebidae           | Lepidoptera       | Insecta         | AACCT              | ACAGACAG           | pacbio    |
| *Euproctis similis*              | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Euproctis similis*              | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Hypena proboscidalis*           | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Hypena proboscidalis*           | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Laspeyria flexula*              | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Laspeyria flexula*              | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Lymantria monacha*              | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Lymantria monacha*              | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Orgyia antiqua*                 | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Phragmatobia fuliginosa*        | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Schrankia costaestrigalis*      | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Schrankia costaestrigalis*      | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Spilosoma lubricipeda*          | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Spilosoma lubricipeda*          | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Thumatha senex*                 | Erebidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Psoricoptera gibbosella*        | Gelechiidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Agriopis aurantiaria*           | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Apeira syringaria*              | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Aplocera efformata*             | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Biston betularia*               | Geometridae        | Lepidoptera       | Insecta         | AACCT              | ACCTACCT           | assembly  |
| *Biston betularia*               | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Campaea margaritaria*           | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Camptogramma bilineatum*        | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Chloroclysta siterata*          | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Chloroclystis v-ata*            | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Colostygia pectinataria*        | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Crocallis elinguaria*           | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Ecliptopera silaceata*          | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Ectropis crepuscularia*         | Geometridae        | Lepidoptera       | Insecta         |                    |                    | pacbio    |
| *Ennomos fuscantarius*           | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Ennomos fuscantarius*           | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Ennomos quercinarius*           | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Ennomos quercinarius*           | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Epirrhoe alternata*             | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Erannis defoliaria*             | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Erannis defoliaria*             | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Eulithis prunata*               | Geometridae        | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Eupithecia centaureata*         | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Eupithecia tripunctaria*        | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Gymnoscelis rufifasciata*       | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Hydriomena furcata*             | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Hylaea fasciaria*               | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Hylaea fasciaria*               | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Idaea aversata*                 | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Idaea aversata*                 | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Lobophora halterata*            | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Macaria notata*                 | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Operophtera brumata*            | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Opisthograptis luteolata*       | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AAATAG             | pacbio    |
| *Peribatodes rhomboidaria*       | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Peribatodes rhomboidaria*       | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Perizoma alchemillatum*         | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Perizoma flavofasciatum*        | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Philereme vetulata*             | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Scotopteryx chenopodiata*       | Geometridae        | Lepidoptera       | Insecta         | ACTCTG             | AACCT              | pacbio    |
| *Selenia dentaria*               | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Xanthorhoe fluctuata*           | Geometridae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Erynnis tages*                  | Hesperiidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Hesperia comma*                 | Hesperiidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Hesperia comma*                 | Hesperiidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Ochlodes sylvanus*              | Hesperiidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Ochlodes sylvanus*              | Hesperiidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Pyrgus malvae*                  | Hesperiidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Pyrgus malvae*                  | Hesperiidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Thymelicus lineola*             | Hesperiidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Thymelicus sylvestris*          | Hesperiidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Thymelicus sylvestris*          | Hesperiidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Aricia agestis*                 | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Aricia agestis*                 | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Aricia artaxerxes*              | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Celastrina argiolus*            | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Cupido minimus*                 | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Cyaniris semiargus*             | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Cyaniris semiargus*             | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Glaucopsyche alexis*            | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Glaucopsyche alexis*            | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | ACAGACAG           | pacbio    |
| *Lycaena phlaeas*                | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Lycaena phlaeas*                | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Plebejus argus*                 | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Plebejus argus*                 | Lycaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Polyommatus icarus*             | Lycaenidae         | Lepidoptera       | Insecta         | AACTCG             | AACCT              | pacbio    |
| *Abrostola tripartita*           | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Abrostola tripartita*           | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Acronicta aceris*               | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Acronicta aceris*               | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Agrochola circellaris*          | Noctuidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Agrochola macilenta*            | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Allophyes oxyacanthae*          | Noctuidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Amphipyra berbera*              | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Amphipyra berbera*              | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Amphipyra tragopoginis*         | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Amphipyra tragopoginis*         | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Apamea monoglypha*              | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Apamea monoglypha*              | Noctuidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Aporophyla lueneburgensis*      | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | ACAGACAG           | pacbio    |
| *Atethmia centrago*              | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Autographa gamma*               | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Autographa gamma*               | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Autographa pulchrina*           | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Autographa pulchrina*           | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Caradrina clavipalpis*          | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Caradrina kadenii*              | Noctuidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Cosmia trapezina*               | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Craniophora ligustri*           | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Craniophora ligustri*           | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Diachrysia chrysitis*           | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Dryobotodes eremita*            | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Euplexia lucipara*              | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | ACAGACAG           | pacbio    |
| *Eupsilia transversa*            | Noctuidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Griposia aprilina*              | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Hecatera dysodea*               | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Hecatera dysodea*               | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Hydraecia micacea*              | Noctuidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Luperina testacea*              | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Mamestra brassicae*             | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Mamestra brassicae*             | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Mesoligia furuncula*            | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Mythimna ferrago*               | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Mythimna ferrago*               | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | ACAGACAG           | pacbio    |
| *Mythimna impura*                | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Mythimna impura*                | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | ACCTACCT           | pacbio    |
| *Noctua comes*                   | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Noctua fimbriata*               | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Noctua fimbriata*               | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Noctua janthe*                  | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Noctua janthe*                  | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Noctua pronuba*                 | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Noctua pronuba*                 | Noctuidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Ochropleura plecta*             | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Ochropleura plecta*             | Noctuidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Omphaloscelis lunosa*           | Noctuidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Phlogophora meticulosa*         | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Phlogophora meticulosa*         | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Photedes minima*                | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Xestia c-nigrum*                | Noctuidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Xestia xanthographa*            | Noctuidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Xestia xanthographa*            | Noctuidae          | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Meganola albula*                | Nolidae            | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Clostera curtula*               | Notodontidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Clostera curtula*               | Notodontidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Furcula furcula*                | Notodontidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Furcula furcula*                | Notodontidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Notodonta dromedarius*          | Notodontidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Notodonta ziczac*               | Notodontidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Phalera bucephala*              | Notodontidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Pheosia gnoma*                  | Notodontidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Pheosia gnoma*                  | Notodontidae       | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Pheosia tremula*                | Notodontidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Pheosia tremula*                | Notodontidae       | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Ptilodon capucinus*             | Notodontidae       | Lepidoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Apatura iris*                   | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Boloria selene*                 | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Boloria selene*                 | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Erebia aethiops*                | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Erebia ligea*                   | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Euphydryas aurinia*             | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Fabriciana adippe*              | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Fabriciana adippe*              | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Lasiommata megera*              | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Limenitis camilla*              | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Limenitis camilla*              | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Maniola jurtina*                | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Maniola jurtina*                | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Melanargia galathea*            | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Melitaea cinxia*                | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Melitaea cinxia*                | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Mellicta athalia*               | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Mellicta athalia*               | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Nymphalis c-album*              | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Nymphalis polychloros*          | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Nymphalis polychloros*          | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Nymphalis urticae*              | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Nymphalis urticae*              | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Pararge aegeria*                | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Pararge aegeria*                | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Vanessa atalanta*               | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Vanessa cardui*                 | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Vanessa cardui*                 | Nymphalidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Papilio machaon*                | Papilionidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Carcina quercana*               | Peleopodidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Carcina quercana*               | Peleopodidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Anthocharis cardamines*         | Pieridae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Anthocharis cardamines*         | Pieridae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Aporia crataegi*                | Pieridae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Colias croceus*                 | Pieridae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Colias croceus*                 | Pieridae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Leptidea sinapis*               | Pieridae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Leptidea sinapis*               | Pieridae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Pieris brassicae*               | Pieridae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Pieris napi*                    | Pieridae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Pieris napi*                    | Pieridae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Pieris rapae*                   | Pieridae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Plutella xylostella*            | Plutellidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Emmelina monodactyla*           | Pterophoridae      | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Endotricha flammealis*          | Pyralidae          | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Hamearis lucina*                | Riodinidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Bembecia ichneumoniformis*      | Sesiidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Bembecia ichneumoniformis*      | Sesiidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Synanthedon vespiformis*        | Sesiidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Deilephila porcellus*           | Sphingidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Deilephila porcellus*           | Sphingidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Laothoe populi*                 | Sphingidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Laothoe populi*                 | Sphingidae         | Lepidoptera       | Insecta         | ACAGACAG           | AACCT              | pacbio    |
| *Mimas tiliae*                   | Sphingidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Mimas tiliae*                   | Sphingidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Sphinx pinastri*                | Sphingidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Tinea semifulvella*             | Tineidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Tinea semifulvella*             | Tineidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Tinea trinotella*               | Tineidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Tinea trinotella*               | Tineidae           | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Acleris emargana*               | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Acleris sparsana*               | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Apotomis betuletana*            | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | ACAGGC             | pacbio    |
| *Apotomis turbidana*             | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | ACTGATAGAT         | assembly  |
| *Apotomis turbidana*             | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AGATAGAT           | pacbio    |
| *Archips podanus*                | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Archips xylosteana*             | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Cydia splendana*                | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Cydia splendana*                | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Ditula angustiorana*            | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Epagoge grotiana*               | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Epinotia brunnichana*           | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Eucosma campoliliana*           | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Eucosma cana*                   | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Hedya salicella*                | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Hedya salicella*                | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | ACAGACAG           | pacbio    |
| *Neocochylis molliculana*        | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Notocelia uddmanniana*          | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Notocelia uddmanniana*          | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Pammene fasciana*               | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Pammene fasciana*               | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Ptycholomoides aeriferana*      | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Rhopobota naevana*              | Tortricidae        | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Yponomeuta plumbellus*          | Yponomeutidae      | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Yponomeuta sedellus*            | Yponomeutidae      | Lepidoptera       | Insecta         | AACCT              | ACAGACAG           | pacbio    |
| *Ypsolopha scabrella*            | Ypsolophidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Ypsolopha scabrella*            | Ypsolophidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Ypsolopha sequella*             | Ypsolophidae       | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Zygaena filipendulae*           | Zygaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | assembly  |
| *Zygaena filipendulae*           | Zygaenidae         | Lepidoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Chrysoperla carnea*             | Chrysopidae        | Neuroptera        | Insecta         | AACCC              | AACCCAACCC         | assembly  |
| *Ischnura elegans*               | Coenagrionidae     | Odonata           | Insecta         | AACCC              |                    | pacbio    |
| *Chorthippus brunneus*           | Acrididae          | Orthoptera        | Insecta         | AACCT              | ACACAG             | pacbio    |
| *Teleogryllus oceanicus*         | Gryllidae          | Orthoptera        | Insecta         | AACCT              | ACTACT             | pacbio    |
| *Meconema thalassinum*           | Tettigoniidae      | Orthoptera        | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Leuctra nigra*                  | Leuctridae         | Plecoptera        | Insecta         | AACCT              |                    | pacbio    |
| *Nemoura dubitans*               | Nemouridae         | Plecoptera        | Insecta         | AACCT              | AGAGC              | pacbio    |
| *Nemurella pictetii*             | Nemouridae         | Plecoptera        | Insecta         | AACCT              | AAGTAG             | pacbio    |
| *Limnephilus lunatus*            | Limnephilidae      | Trichoptera       | Insecta         | AACCT              |                    | pacbio    |
| *Limnephilus marmoratus*         | Limnephilidae      | Trichoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Polycentropus irroratus*        | Polycentropodidae  | Trichoptera       | Insecta         | AACCT              | AACCTAACCT         | pacbio    |
| *Metschnikowia zobellii*         | Metschnikowiaceae  | Saccharomycetales | Saccharomycetes |                    |                    | pacbio    |
| *Trichoderma pseudokoningii*     | Hypocreaceae       | Hypocreales       | Sordariomycetes | CCCCC              | CCCCCC             | pacbio    |
| *Armillaria gallica*             | Physalacriaceae    | Agaricales        | Agaricomycetes  | AAACCCT            | AACCCTG            | pacbio    |
| *Laetiporus sulphureus*          | Laetiporaceae      | Polyporales       | Agaricomycetes  | CCCCC              | CCCCCCC            | pacbio    |
| *Laetiporus sulphureus*          | Laetiporaceae      | Polyporales       | Agaricomycetes  | CCCCC              | CCCCCCC            | pacbio    |
| *Pycnococcus provasolii*         | Pycnococcaceae     |                   |                 |                    |                    | pacbio    |
| *Brachiomonas submarina*         | Chlamydomonadaceae | Chlamydomonadales | Chlorophyceae   | AAGGATGGAC         | ACAGACAG           | pacbio    |
| *Dunaliella primolecta*          | Dunaliellaceae     | Chlamydomonadales | Chlorophyceae   | ACACACAC           | ACACAC             | pacbio    |
| *Telmatherina bonti*             | Telmatherinidae    | Atheriniformes    | Actinopteri     | ACCAG              | AACCCT             | pacbio    |
| *Trachurus trachurus*            | Carangidae         | Carangiformes     | Actinopteri     | AAAAA              | AACCCT             | assembly  |
| *Barbus barbus*                  | Cyprinidae         | Cypriniformes     | Actinopteri     | AACCCT             | ACACAC             | pacbio    |
| *Danio rerio*                    | Danionidae         | Cypriniformes     | Actinopteri     | AACCCT             | AGATAGAT           | pacbio    |
| *Taurulus bubalis*               | Cottidae           | Perciformes       | Actinopteri     | AACCCT             | AACCCTAACCCT       | assembly  |
| *Taurulus bubalis*               | Cottidae           | Perciformes       | Actinopteri     | AACCCT             | ACACAC             | pacbio    |
| *Pholis gunnellus*               | Pholidae           | Perciformes       | Actinopteri     | AACCCT             | AACCCTAACCCT       | assembly  |
| *Pholis gunnellus*               | Pholidae           | Perciformes       | Actinopteri     | AACCCT             | AACCCTAACCCT       | pacbio    |
| *Bufo bufo*                      | Bufonidae          | Anura             | Amphibia        | AACCCT             | AACCCTAACCCT       | assembly  |
| *Rana temporaria*                | Ranidae            | Anura             | Amphibia        | AACCCT             | AACCCTAACCCT       | assembly  |
| *Aplidium turbinatum*            | Polyclinidae       | Aplousobranchia   | Ascidiacea      | AACCCT             | AACCCTAACCCT       | pacbio    |
| *Ascidia mentula*                | Ascidiidae         | Phlebobranchia    | Ascidiacea      | AACCCT             | AACCCTAACCCT       | pacbio    |
| *Caprimulgus europaeus*          | Caprimulgidae      | Caprimulgiformes  | Aves            | AACCCT             | AACCCTAACCCT       | assembly  |
| *Cervus elaphus*                 | Cervidae           | Artiodactyla      | Mammalia        | AAAAA              | AAAAAA             | assembly  |
| *Canis lupus*                    | Canidae            | Carnivora         | Mammalia        | AACCCT             | AACCCTAACCCT       | assembly  |
| *Rattus norvegicus*              | Muridae            | Rodentia          | Mammalia        | AACCCT             | AACCCTAACCCT       | assembly  |
| *Colpoda steinii*                | Colpodidae         | Colpodida         | Colpodea        | CCCCC              | CCCCCC             | pacbio    |
| *Diadumene lineata*              | Diadumenidae       | Actiniaria        | Anthozoa        | AACCCT             | AAGAGTGT           | pacbio    |
| *Nematostella vectensis*         | Edwardsiidae       | Actiniaria        | Anthozoa        | AACCCT             | ACCATC             | pacbio    |
| *Haliclystus octoradiatus*       | Haliclystidae      | Stauromedusae     | Staurozoa       | AATAAT             | ACTAT              | pacbio    |
| *Marthasterias glacialis*        | Asteriidae         | Forcipulatida     | Asteroidea      | AACCCT             | AACCCTAACCCT       | assembly  |
| *Marthasterias glacialis*        | Asteriidae         | Forcipulatida     | Asteroidea      | AACCCT             | AAAGGAC            | pacbio    |
| *Antedon bifida*                 | Antedonidae        | Comatulida        | Crinoidea       | AACCCT             | AACAAC             | pacbio    |
| *Tetramitus jugosus*             | Vahlkampfiidae     |                   |                 | AAACCC             | CCCCC              | pacbio    |
| *Gari tellinella*                | Psammobiidae       | Cardiida          | Bivalvia        | AACCCT             | AACCCTAACCCT       | pacbio    |
| *Patella depressa*               | Patellidae         |                   | Gastropoda      | AACCCT             | AACCCTAACCCT       | pacbio    |
| *Patella pellucida*              | Patellidae         |                   | Gastropoda      | AACTCTCTACT        | AACTCTACT          | pacbio    |
| *Gibbula magus*                  | Trochidae          | Trochida          | Gastropoda      | AACATG             | AACCCT             | pacbio    |
| *Phorcus lineatus*               | Trochidae          | Trochida          | Gastropoda      | AACCCT             | AACCCTAACCCT       | pacbio    |
| *Steromphala cineraria*          | Trochidae          | Trochida          | Gastropoda      | AACCCT             | AACCCTAACCCT       | pacbio    |
| *Mucor piriformis*               | Mucoraceae         | Mucorales         | Mucoromycetes   | AAAAA              | CCCCC              | pacbio    |
| *Dioctophyme renale*             | Dioctophymatidae   | Dioctophymatida   | Enoplea         | ACGATG             | ATCATC             | pacbio    |
| *Lineus longissimus*             | Lineidae           | Heteronemertea    | Pilidiophora    | AACCCT             | AACCCTAACCCT       | assembly  |
| *Carex depauperata*              | Cyperaceae         | Poales            | Magnoliopsida   | AAACCCT            | AACCCTG            | pacbio    |
| *Schoenoplectus lacustris*       | Cyperaceae         | Poales            | Magnoliopsida   | AAACCCT            | AATAAT             | pacbio    |
| *Juncus effusus*                 | Juncaceae          | Poales            | Magnoliopsida   | AAACCCT            | ATATAT             | pacbio    |
| *Danthonia decumbens*            | Poaceae            | Poales            | Magnoliopsida   | AAACCCT            | CCCCC              | pacbio    |
