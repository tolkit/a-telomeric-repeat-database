# A Telomeric Repeat Database

Both raw data (PacBio) and Darwin Tree of Life assemblies are used to de-novo identify telomeric repeat sequences.

The program used to infer telomeric repeats is <a href="https://github.com/tolkit/telomeric-identifier">tidk</a>.

See `/src/README.md` for pipeline details.

To note this is not a curated list, it is raw output from tidk, and as such, the values may not be accurate. The list is also being actively updated. The main list is below, but see the `clades` directory to get breakdown by eukaryotic class. It will be immediately noticed that for some clades, tidk is not catching the telomeric repeats.

A curated list is being worked on currently, and can be seen in `./data/curated/`.

| Species | Family | Order | Class | Telomeric repeat 1 | Telomeric repeat 2 | Data type |
| -- | --- | --- | --- | --- | --- | --- |
| *Rhodomonas baltica* | Pyrenomonadaceae | Pyrenomonadales | Cryptophyceae | AAACCCT | ACACTC | pacbio |
| *Pelvetia canaliculata* | Fucaceae | Fucales | Phaeophyceae | AACCCT | AACCCTAACCCT | pacbio |
| *Carpodesmia tamariscifolia* | Sargassaceae | Fucales | Phaeophyceae | ACACT | ACACAC | pacbio |
| *Halidrys siliquosa* | Sargassaceae | Fucales | Phaeophyceae | AACCCT | ACAGT | pacbio |
| *Alaria esculenta* | Alariaceae | Laminariales | Phaeophyceae | ACAGACAG | AAAGC | pacbio |
| *Aporrectodea caliginosa* | Lumbricidae | Crassiclitellata | Clitellata |  |  | pacbio |
| *Aporrectodea longa* | Lumbricidae | Crassiclitellata | Clitellata | AACCCT | AACCCTAACCCT | pacbio |
| *Eisenia fetida* | Lumbricidae | Crassiclitellata | Clitellata | ATCATC | AACCCT | pacbio |
| *Eiseniella tetraedra* | Lumbricidae | Crassiclitellata | Clitellata | AACCCT | ACATACAT | pacbio |
| *Lumbricus castaneus* | Lumbricidae | Crassiclitellata | Clitellata | ATCATC | AACCCT | pacbio |
| *Lumbricus rubellus* | Lumbricidae | Crassiclitellata | Clitellata | AAGGAC | AAGGACAAGGAC | assembly |
| *Lumbricus rubellus* | Lumbricidae | Crassiclitellata | Clitellata | AAGGAC | AACCCT | pacbio |
| *Lumbricus terrestris* | Lumbricidae | Crassiclitellata | Clitellata | AACTC | AACCCT | pacbio |
| *Octolasion cyaneum* | Lumbricidae | Crassiclitellata | Clitellata | AACCCT | ACCATC | pacbio |
| *Piscicola geometra* | Piscicolidae | Hirudinida | Clitellata | AACACGAGATG | AACCCT | assembly |
| *Piscicola geometra* | Piscicolidae | Hirudinida | Clitellata | AACACGAGATG | AACCCT | pacbio |
| *Glossiphonia complanata* | Glossiphoniidae | Rhynchobdellida | Clitellata | AATGAATG | AAGTAAGT | pacbio |
| *Helobdella stagnalis* | Glossiphoniidae | Rhynchobdellida | Clitellata | ACATACAT | AAATGAAT | pacbio |
| *Arenicola marina* | Arenicolidae |  | Polychaeta | AACCCT | AAGAGGC | pacbio |
| *Euclymene oerstedii* | Maldanidae |  | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Thalassema thalassema* | Thalassematidae | Echiuroidea | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Marphysa sanguinea* | Eunicidae | Eunicida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Goniada maculata* | Goniadidae | Phyllodocida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Nephtys cirrosa* | Nephtyidae | Phyllodocida | Polychaeta | AACCCT | AAGTAG | pacbio |
| *Alitta virens* | Nereididae | Phyllodocida | Polychaeta | AACCCT | AACCCTAACCCT | assembly |
| *Alitta virens* | Nereididae | Phyllodocida | Polychaeta | AACCCT | ACTACT | pacbio |
| *Acholoe squamosa* | Polynoidae | Phyllodocida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Harmothoe impar* | Polynoidae | Phyllodocida | Polychaeta | AACCCT | AACCCTAACCCT | assembly |
| *Harmothoe impar* | Polynoidae | Phyllodocida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Lepidonotus clava* | Polynoidae | Phyllodocida | Polychaeta | AACCCT | AACCCTAACCCT | assembly |
| *Lepidonotus clava* | Polynoidae | Phyllodocida | Polychaeta | AACCCT |  | pacbio |
| *Sthenelais limicola* | Sigalionidae | Phyllodocida | Polychaeta | AACCCT | AACCCTAACCCT | assembly |
| *Sthenelais limicola* | Sigalionidae | Phyllodocida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Sabellaria alveolata* | Sabellariidae | Sabellida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Myxicola infundibulum* | Sabellidae | Sabellida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Spirobranchus lamarcki* | Serpulidae | Sabellida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Amphicteis midas* | Ampharetidae | Terebellida | Polychaeta |  |  | pacbio |
| *Melinna palmata* | Melinnidae | Terebellida | Polychaeta | ACATACAT | ACATACATACAT | pacbio |
| *Neoamphitrite figulus* | Terebellidae | Terebellida | Polychaeta | ATCCC | ATCCATCC | pacbio |
| *Terebella lapidaria* | Terebellidae | Terebellida | Polychaeta | ACTGACTG | ACACAC | pacbio |
| *Eimeria maxima* | Eimeriidae | Eucoccidiorida | Conoidasida | AAGGAGGAGACAAT | ACACAT | pacbio |
| *Eimeria tenella* | Eimeriidae | Eucoccidiorida | Conoidasida | AAACCCT |  | assembly |
| *Agelena labyrinthica* | Agelenidae | Araneae | Arachnida | ACATACAT | AGATAGAT | pacbio |
| *Eratigena atrica* | Agelenidae | Araneae | Arachnida | ACACAC | ATATAT | pacbio |
| *Eratigena duellica* | Agelenidae | Araneae | Arachnida | AGATAGAT | ACTCACTC | pacbio |
| *Eratigena saeva* | Agelenidae | Araneae | Arachnida | AACAC | ACATACAT | pacbio |
| *Amaurobius ferox* | Amaurobiidae | Araneae | Arachnida | ATATAT | ATATATAT | pacbio |
| *Amaurobius similis* | Amaurobiidae | Araneae | Arachnida | ACACAC | ACACACAC | pacbio |
| *Agalenatea redii* | Araneidae | Araneae | Arachnida | ACAGACAG | ACATACAT | pacbio |
| *Araneus angulatus* | Araneidae | Araneae | Arachnida | ACAGACAG | AACCAACC | pacbio |
| *Araneus diadematus* | Araneidae | Araneae | Arachnida | AATAT |  | pacbio |
| *Argiope bruennichi* | Araneidae | Araneae | Arachnida |  |  | assembly |
| *Argiope bruennichi* | Araneidae | Araneae | Arachnida | ACACAC | AGATAGAT | pacbio |
| *Cyclosa conica* | Araneidae | Araneae | Arachnida | ACATACAT | ATCCATCC | pacbio |
| *Gibbaranea gibbosa* | Araneidae | Araneae | Arachnida | ACACAC | ACAGACAG | pacbio |
| *Mangora acalypha* | Araneidae | Araneae | Arachnida | ACATACAT | ACATACATACAT | pacbio |
| *Zygiella x-notata* | Araneidae | Araneae | Arachnida | AGATAGAT | CCCCC | pacbio |
| *Atypus affinis* | Atypidae | Araneae | Arachnida | AGATAGAT | ATCATC | pacbio |
| *Clubiona reclusa* | Clubionidae | Araneae | Arachnida | ATATAT | AAAAAA | pacbio |
| *Clubiona terrestris* | Clubionidae | Araneae | Arachnida |  |  | pacbio |
| *Dysdera crocata* | Dysderidae | Araneae | Arachnida | AGATAGAT | ACTCACTC | pacbio |
| *Zelotes latreillei* | Gnaphosidae | Araneae | Arachnida | AGATAGAT | AACAT | pacbio |
| *Linyphia triangularis* | Linyphiidae | Araneae | Arachnida | AATAAT | ATATAT | pacbio |
| *Alopecosa pulverulenta* | Lycosidae | Araneae | Arachnida | ATATAT | ACACAC | pacbio |
| *Pardosa saltans* | Lycosidae | Araneae | Arachnida | ACTAT | ACTATACTAT | pacbio |
| *Tibellus oblongus* | Philodromidae | Araneae | Arachnida | AACAT | ATATAT | pacbio |
| *Pholcus phalangioides* | Pholcidae | Araneae | Arachnida | AAAAA | AAAAAA | pacbio |
| *Dolomedes fimbriatus* | Pisauridae | Araneae | Arachnida | ACATACAT | ATATAT | pacbio |
| *Dolomedes plantarius* | Pisauridae | Araneae | Arachnida | ATATAT | ATATATAT | assembly |
| *Pisaura mirabilis* | Pisauridae | Araneae | Arachnida | ATATAT | AAAAA | pacbio |
| *Marpissa muscosa* | Salticidae | Araneae | Arachnida | AGATAGAT | AGATAGATAGAT | pacbio |
| *Scytodes thoracica* | Scytodidae | Araneae | Arachnida | ACATG | AAATTGTCTAATAAT | pacbio |
| *Segestria senoculata* | Segestriidae | Araneae | Arachnida | ACTCACTC | ACTCACTCACTC | pacbio |
| *Meta bourneti* | Tetragnathidae | Araneae | Arachnida | AATGG |  | assembly |
| *Meta bourneti* | Tetragnathidae | Araneae | Arachnida | ACCTACCT | ACATACAT | pacbio |
| *Metellina segmentata* | Tetragnathidae | Araneae | Arachnida | AAAAT | ACTAT | assembly |
| *Metellina segmentata* | Tetragnathidae | Araneae | Arachnida | AACTTGT | ACTATGG | pacbio |
| *Enoplognatha latimana* | Theridiidae | Araneae | Arachnida | AAAGC | ACACAC | pacbio |
| *Enoplognatha ovata* | Theridiidae | Araneae | Arachnida | ACACAC | ACACACAC | pacbio |
| *Parasteatoda lunata* | Theridiidae | Araneae | Arachnida | AAATAAAT | AGATAGAT | pacbio |
| *Steatoda bipunctata* | Theridiidae | Araneae | Arachnida |  |  | pacbio |
| *Steatoda grossa* | Theridiidae | Araneae | Arachnida | ACCTACCT | ACTCACTC | pacbio |
| *Misumena vatia* | Thomisidae | Araneae | Arachnida | ACACAC | ACATACAT | pacbio |
| *Xysticus cristatus* | Thomisidae | Araneae | Arachnida | ACACAC | ACACACAC | pacbio |
| *Uloborus plumipes* | Uloboridae | Araneae | Arachnida | ACACAC | ATATAT | pacbio |
| *Zoropsis spinimana* | Zoropsidae | Araneae | Arachnida | ATATAT | ATATATAT | pacbio |
| *Odiellus spinosus* | Phalangiidae | Opiliones | Arachnida | ACGAG | AACCT | pacbio |
| *Phalangium opilio* | Phalangiidae | Opiliones | Arachnida | AACCT | AAGCT | pacbio |
| *Stigmatogaster subterranea* | Himantariidae | Geophilomorpha | Chilopoda | AACCT | AACCTAACCT | pacbio |
| *Lithobius forficatus* | Lithobiidae | Lithobiomorpha | Chilopoda | AAAGTCG | AAAGTCGAAAGTCG | pacbio |
| *Lithobius melanops* | Lithobiidae | Lithobiomorpha | Chilopoda | AACCT | AACCTAACCT | pacbio |
| *Lithobius muticus* | Lithobiidae | Lithobiomorpha | Chilopoda | AACCT | AAATC | pacbio |
| *Lithobius piceus* | Lithobiidae | Lithobiomorpha | Chilopoda | AACCT | AACCTAACCT | pacbio |
| *Lithobius variegatus* | Lithobiidae | Lithobiomorpha | Chilopoda | AACCT | AACCTAACCT | pacbio |
| *Heterosminthurus bilineatus* | Bourletiellidae | Symphypleona | Collembola | AACCT | AACCTAACCT | pacbio |
| *Dicyrtomina minuta* | Dicyrtomidae | Symphypleona | Collembola | AACCT | ACAGACAG | pacbio |
| *Allacma fusca* | Sminthuridae | Symphypleona | Collembola | AACCT | AAACTCCAAGTT | assembly |
| *Allacma fusca* | Sminthuridae | Symphypleona | Collembola | AAACTTGGAATT | AAACTTGGAATTAAACTTGGAATT | pacbio |
| *Glomeris marginata* | Glomeridae | Glomerida | Diplopoda | AACCT | AAGTGTCCG | pacbio |
| *Petrobius brevistylis* | Machilidae | Archaeognatha | Insecta | AACTAACT | AACCT | pacbio |
| *Ectobius pallidus* | Ectobiidae | Blattodea | Insecta | AAGACC | AACCT | pacbio |
| *Aspidapion aeneum* | Apionidae | Coleoptera | Insecta | ACAGACAG | ACAGACAGACAG | pacbio |
| *Aspidapion radiolus* | Apionidae | Coleoptera | Insecta | AAACCTAACC | AAATTG | pacbio |
| *Betulapion simile* | Apionidae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Apoderus coryli* | Attelabidae | Coleoptera | Insecta | AACCC | AACCCAACCC | assembly |
| *Apoderus coryli* | Attelabidae | Coleoptera | Insecta | AAATAATT |  | pacbio |
| *Attelabus nitens* | Attelabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agrilus cyanescens* | Buprestidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agrilus cyanescens* | Buprestidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Byturus ochraceus* | Byturidae | Coleoptera | Insecta | AGCCAGCC | AACAG | pacbio |
| *Cantharis cryptica* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cantharis flavilabris* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cantharis nigricans* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cantharis rufa* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Cantharis rufa* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cantharis rustica* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Cantharis rustica* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Podabrus alpinus* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Podabrus alpinus* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Rhagonycha fulva* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Rhagonycha fulva* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Rhagonycha lutea* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agonum fuliginosum* | Carabidae | Coleoptera | Insecta | AAATGTG | AATGT | assembly |
| *Agonum fuliginosum* | Carabidae | Coleoptera | Insecta | ACACAC | ACACAT | pacbio |
| *Asaphidion curtum* | Carabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Bembidion guttula* | Carabidae | Coleoptera | Insecta | AACCT | AAACCTAACCT | pacbio |
| *Brachinus crepitans* | Carabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Clivina fossor* | Carabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Demetrias atricapillus* | Carabidae | Coleoptera | Insecta | ACATACAT | ACATACATACAT | pacbio |
| *Dromius quadrimaculatus* | Carabidae | Coleoptera | Insecta |  |  | pacbio |
| *Harpalus rubripes* | Carabidae | Coleoptera | Insecta | ACATACAT | ACATACATACAT | pacbio |
| *Harpalus rufipes* | Carabidae | Coleoptera | Insecta | ACATACAT | ACACAC | pacbio |
| *Leistus spinibarbis* | Carabidae | Coleoptera | Insecta | AACTAC | AACTACAACTAC | assembly |
| *Leistus spinibarbis* | Carabidae | Coleoptera | Insecta |  |  | pacbio |
| *Nebria brevicollis* | Carabidae | Coleoptera | Insecta | AAATAACT | AAATAACTAAATAACT | assembly |
| *Nebria brevicollis* | Carabidae | Coleoptera | Insecta | AAATAACT | AAACATAC | pacbio |
| *Nebria salina* | Carabidae | Coleoptera | Insecta | AAATAACT | AAATAACTAAATAACT | assembly |
| *Nebria salina* | Carabidae | Coleoptera | Insecta | AAATAACT | AAACTAACT | pacbio |
| *Notiophilus biguttatus* | Carabidae | Coleoptera | Insecta | AGATATAT | AGATATATAGATATAT | pacbio |
| *Notiophilus substriatus* | Carabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ocys tachysoides* | Carabidae | Coleoptera | Insecta | AACCT | AAATAAAT | pacbio |
| *Ophonus ardosiacus* | Carabidae | Coleoptera | Insecta | AACCT | ACATACAT | assembly |
| *Ophonus ardosiacus* | Carabidae | Coleoptera | Insecta | ACATACAT | ACATACATACAT | pacbio |
| *Oxypselaphus obscurus* | Carabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pterostichus madidus* | Carabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pterostichus madidus* | Carabidae | Coleoptera | Insecta | AATAAT | ATCCATCC | pacbio |
| *Pterostichus niger* | Carabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pterostichus niger* | Carabidae | Coleoptera | Insecta | AACCT | ACATAT | pacbio |
| *Pterostichus strenuus* | Carabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Syntomus foveatus* | Carabidae | Coleoptera | Insecta | AACCT | AAACATGAACATG | pacbio |
| *Clytus arietis* | Cerambycidae | Coleoptera | Insecta | AATAAT | AATAATAAT | pacbio |
| *Rutpela maculata* | Cerambycidae | Coleoptera | Insecta | AAACCCATCCTAATTTCATC | AACCT | assembly |
| *Rutpela maculata* | Cerambycidae | Coleoptera | Insecta | AATAAT | ACACAC | pacbio |
| *Cassida rubiginosa* | Chrysomelidae | Coleoptera | Insecta | AAATTC | AATCAT | pacbio |
| *Chrysolina americana* | Chrysomelidae | Coleoptera | Insecta | AACCT | ATCCATCC | pacbio |
| *Chrysolina oricalcia* | Chrysomelidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Chrysolina oricalcia* | Chrysomelidae | Coleoptera | Insecta | ATCCATCC | ATCCATCCATCC | pacbio |
| *Chrysolina polita* | Chrysomelidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Crepidodera aurea* | Chrysomelidae | Coleoptera | Insecta | ACACACAGAG | AACAGACACG | pacbio |
| *Crepidodera fulvicornis* | Chrysomelidae | Coleoptera | Insecta | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Crioceris asparagi* | Chrysomelidae | Coleoptera | Insecta |  |  | pacbio |
| *Cryptocephalus moraei* | Chrysomelidae | Coleoptera | Insecta | ACATGC | ACATGCACATGC | assembly |
| *Cryptocephalus moraei* | Chrysomelidae | Coleoptera | Insecta |  |  | pacbio |
| *Cryptocephalus primarius* | Chrysomelidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Gastrophysa viridula* | Chrysomelidae | Coleoptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Hermaeophaga mercurialis* | Chrysomelidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lilioceris lilii* | Chrysomelidae | Coleoptera | Insecta | ACACAC | AAACG | pacbio |
| *Lochmaea capreae* | Chrysomelidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lochmaea crataegi* | Chrysomelidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lochmaea crataegi* | Chrysomelidae | Coleoptera | Insecta | AACCT | AGATG | pacbio |
| *Longitarsus pellucidus* | Chrysomelidae | Coleoptera | Insecta | AACCT | ACCTG | pacbio |
| *Luperus longicornis* | Chrysomelidae | Coleoptera | Insecta | AACGAC | AACATCATCTCC | pacbio |
| *Oulema melanopus* | Chrysomelidae | Coleoptera | Insecta | ACAGACTG | ACAGACAGACTG | pacbio |
| *Phyllotreta exclamationis* | Chrysomelidae | Coleoptera | Insecta | ACTCT | ACCCT | pacbio |
| *Plateumaris sericea* | Chrysomelidae | Coleoptera | Insecta | ATATCC | AATAG | pacbio |
| *Timarcha tenebricosa* | Chrysomelidae | Coleoptera | Insecta | AAACGAT | AAACGATAAACGAT | pacbio |
| *Cis boleti* | Ciidae | Coleoptera | Insecta | ACCTG | ACAGACAGACAGG | pacbio |
| *Adalia bipunctata* | Coccinellidae | Coleoptera | Insecta | AAAAATTC | AACCT | assembly |
| *Adalia bipunctata* | Coccinellidae | Coleoptera | Insecta | AACCT |  | pacbio |
| *Adalia decempunctata* | Coccinellidae | Coleoptera | Insecta | AAGTC | ACATC | pacbio |
| *Anatis ocellata* | Coccinellidae | Coleoptera | Insecta | AACCT | ACACTG | pacbio |
| *Calvia quattuordecimguttata* | Coccinellidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Chilocorus renipustulatus* | Coccinellidae | Coleoptera | Insecta | ACTCTG | AAATATT | pacbio |
| *Coccinella septempunctata* | Coccinellidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Coccinella septempunctata* | Coccinellidae | Coleoptera | Insecta | AAGTCG | AACCT | pacbio |
| *Halyzia sedecimguttata* | Coccinellidae | Coleoptera | Insecta | AACTCC | AACTCCAACTCC | assembly |
| *Halyzia sedecimguttata* | Coccinellidae | Coleoptera | Insecta | AACTCC | AACTCCAACTCC | pacbio |
| *Harmonia axyridis* | Coccinellidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Harmonia axyridis* | Coccinellidae | Coleoptera | Insecta | AACCT |  | pacbio |
| *Hippodamia variegata* | Coccinellidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Propylea quattuordecimpunctata* | Coccinellidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Rhyzobius chrysomeloides* | Coccinellidae | Coleoptera | Insecta | AAACTAACTAACT | AACCT | pacbio |
| *Scymnus frontalis* | Coccinellidae | Coleoptera | Insecta | AAGACT | AAGACTAAGACT | pacbio |
| *Stethorus punctillum* | Coccinellidae | Coleoptera | Insecta | ACACACTACCTACCTATC | ACACACCCTATCACTACTCTACCTGTACT | pacbio |
| *Subcoccinella vigintiquattuorpunctata* | Coccinellidae | Coleoptera | Insecta | AACAT | AACATAACAT | pacbio |
| *Cryptophagus acutangulus* | Cryptophagidae | Coleoptera | Insecta | AAATAAAT | AAATAAATAAAT | pacbio |
| *Ceutorhynchus obstrictus* | Curculionidae | Coleoptera | Insecta | AAACTAACCC | AAACTAACCCAAACTAACCC | pacbio |
| *Curculio glandium* | Curculionidae | Coleoptera | Insecta | AACCC | AGATAGAT | pacbio |
| *Limnobaris t-album* | Curculionidae | Coleoptera | Insecta | ATATAT | ACACAC | pacbio |
| *Mecinus pascuorum* | Curculionidae | Coleoptera | Insecta | AAAAAT | AAAAAAT | pacbio |
| *Otiorhynchus atroapterus* | Curculionidae | Coleoptera | Insecta | AGATAGAT | AGATAGATAGAT | pacbio |
| *Otiorhynchus sulcatus* | Curculionidae | Coleoptera | Insecta | AAATAAAT | AAATAAATAAAT | pacbio |
| *Philopedon plagiatum* | Curculionidae | Coleoptera | Insecta | AGGATG | AGGATGAGGATG | pacbio |
| *Platypus cylindrus* | Curculionidae | Coleoptera | Insecta | AAACC | AAACCAAACC | pacbio |
| *Polydrusus cervinus* | Curculionidae | Coleoptera | Insecta | AACAGACCCG | AACAGACCCGAACAGACCCG | assembly |
| *Polydrusus cervinus* | Curculionidae | Coleoptera | Insecta | AACAGACCCG | AAATGC | pacbio |
| *Polydrusus tereticollis* | Curculionidae | Coleoptera | Insecta | AACCTGAACT | AACCTGAACTAACCTGAACT | pacbio |
| *Rhinocyllus conicus* | Curculionidae | Coleoptera | Insecta | AGATAGAT | AGATAGATAGAT | pacbio |
| *Strophosoma melanogrammum* | Curculionidae | Coleoptera | Insecta | ACATACAT | ACCACTC | pacbio |
| *Dascillus cervinus* | Dascillidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Adrastus pallens* | Elateridae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agriotes lineatus* | Elateridae | Coleoptera | Insecta | AAAGGTCACC | AAGCC | pacbio |
| *Agriotes sputator* | Elateridae | Coleoptera | Insecta | AATCAATC | AATAC | pacbio |
| *Agrypnus murinus* | Elateridae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agrypnus murinus* | Elateridae | Coleoptera | Insecta | AACCT | AAACTAT | pacbio |
| *Denticollis linearis* | Elateridae | Coleoptera | Insecta | AAAGGAC | AACCT | pacbio |
| *Limonius poneli* | Elateridae | Coleoptera | Insecta | ATCATCC | AACCT | pacbio |
| *Elmis aenea* | Elmidae | Coleoptera | Insecta | AAATT | AAAAATT | assembly |
| *Elmis aenea* | Elmidae | Coleoptera | Insecta | ACAGAG | ACATATGACATG | pacbio |
| *Endomychus coccineus* | Endomychidae | Coleoptera | Insecta | AACCT | ACACAT | pacbio |
| *Dorytomus taeniatus* | Erirhinidae | Coleoptera | Insecta | AAATC | AAATG | pacbio |
| *Peltodytes caesus* | Haliplidae | Coleoptera | Insecta | AAAAATAC |  | pacbio |
| *Hydrobius fuscipes* | Hydrophilidae | Coleoptera | Insecta |  |  | pacbio |
| *Sinodendron cylindricum* | Lucanidae | Coleoptera | Insecta | AATAAT | ACTACT | pacbio |
| *Platycis minutus* | Lycidae | Coleoptera | Insecta | AACCT | AGATAGAT | pacbio |
| *Anthocomus rufus* | Melyridae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Malachius bipustulatus* | Melyridae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | assembly |
| *Malachius bipustulatus* | Melyridae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Litargus connexus* | Mycetophagidae | Coleoptera | Insecta | ACCTG | ACTGACTG | pacbio |
| *Oedemera lurida* | Oedemeridae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Oedemera nobilis* | Oedemeridae | Coleoptera | Insecta | ACTATG | ACTATGACTATG | pacbio |
| *Oedemera virescens* | Oedemeridae | Coleoptera | Insecta | AACCCAGACCT | AACCCAGACCTAACCCAGACCT | pacbio |
| *Ptinus dubius* | Ptinidae | Coleoptera | Insecta | AGATAGAT | AAGAT | pacbio |
| *Pyrochroa serraticornis* | Pyrochroidae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | assembly |
| *Pyrochroa serraticornis* | Pyrochroidae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Salpingus planirostris* | Salpingidae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Anomala dubia* | Scarabaeidae | Coleoptera | Insecta | AACCT | ACCCTACCT | pacbio |
| *Melinopterus prodromus* | Scarabaeidae | Coleoptera | Insecta | AAATAAT | AAATAATAAATAAT | pacbio |
| *Cetonia aurata* | Scarabaeidae | Coleoptera | Insecta | AATAG | AGATAGAT | pacbio |
| *Melolontha melolontha* | Scarabaeidae | Coleoptera | Insecta | AAATCCG | AGATCCG | assembly |
| *Melolontha melolontha* | Scarabaeidae | Coleoptera | Insecta | AAGTAATC | AAAGAT | pacbio |
| *Anaspis maculata* | Scraptiidae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Nicrophorus humator* | Silphidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Phosphuga atrata* | Silphidae | Coleoptera | Insecta | AAGACTAGACAGAC | AAGACTAGACAGACAAGACTAGACAGAC | assembly |
| *Phosphuga atrata* | Silphidae | Coleoptera | Insecta | AAGACAGAC | ACAGACTAG | pacbio |
| *Silvanus unidentatus* | Silvanidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Uleiota planata* | Silvanidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Anotylus rugosus* | Staphylinidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lathrobium geminum* | Staphylinidae | Coleoptera | Insecta | AAAGGC | AAAGAC | pacbio |
| *Ocypus olens* | Staphylinidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ocypus olens* | Staphylinidae | Coleoptera | Insecta | AACCT |  | pacbio |
| *Philonthus cognatus* | Staphylinidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Philonthus cognatus* | Staphylinidae | Coleoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Stenus bimaculatus* | Staphylinidae | Coleoptera | Insecta | AACCT | AATCC | pacbio |
| *Tachyporus hypnorum* | Staphylinidae | Coleoptera | Insecta | ACCCT | AATAC | pacbio |
| *Xantholinus longiventris* | Staphylinidae | Coleoptera | Insecta | ACAGACAG | ACAGACAGACCG | pacbio |
| *Lagria hirta* | Tenebrionidae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | assembly |
| *Lagria hirta* | Tenebrionidae | Coleoptera | Insecta | ATCATC | ACAGACAG | pacbio |
| *Forficula auricularia* | Forficulidae | Dermaptera | Insecta | AAAAA | AAAAAA | pacbio |
| *Labia minor* | Spongiphoridae | Dermaptera | Insecta | AACCG | ACATACAT | pacbio |
| *Acrocera orbiculus* | Acroceridae | Diptera | Insecta |  |  | assembly |
| *Acrocera orbiculus* | Acroceridae | Diptera | Insecta |  |  | pacbio |
| *Anthomyia liturata* | Anthomyiidae | Diptera | Insecta | AAGATAGAT | AGATAGAT | pacbio |
| *Anthomyia pluvialis* | Anthomyiidae | Diptera | Insecta | ACATACAT | AGATAGAT | pacbio |
| *Botanophila fugax* | Anthomyiidae | Diptera | Insecta | AAATAAAT | ACAGACAG | pacbio |
| *Delia platura* | Anthomyiidae | Diptera | Insecta | ACAGACAG | AAGTGTATGGC | pacbio |
| *Eustalomyia histrio* | Anthomyiidae | Diptera | Insecta | ACATACAT | ACATACATACAT | pacbio |
| *Hylemya vagans* | Anthomyiidae | Diptera | Insecta | AAAATAT | AAATTAT | pacbio |
| *Hylemya variata* | Anthomyiidae | Diptera | Insecta | ACTAT | ACTATACTAT | pacbio |
| *Leucophora obtusa* | Anthomyiidae | Diptera | Insecta | AAATAAAT | AAATAAATAAAT | pacbio |
| *Leucophora personata* | Anthomyiidae | Diptera | Insecta | AAATAAAT | ACAGACAG | pacbio |
| *Pegoplata infirma* | Anthomyiidae | Diptera | Insecta | ACAGACAG | ACAGACAGACAG | pacbio |
| *Choerades marginata* | Asilidae | Diptera | Insecta |  |  | pacbio |
| *Dioctria rufipes* | Asilidae | Diptera | Insecta | AAAGGCG | AAAGGCGAAAGGCG | pacbio |
| *Dysmachus trigonus* | Asilidae | Diptera | Insecta |  |  | pacbio |
| *Leptogaster cylindrica* | Asilidae | Diptera | Insecta | AACGAT | ACTAGACTATG | pacbio |
| *Machimus atricapillus* | Asilidae | Diptera | Insecta |  |  | assembly |
| *Machimus atricapillus* | Asilidae | Diptera | Insecta | ACAGACAG | AATAC | pacbio |
| *Neoitamus cyanurus* | Asilidae | Diptera | Insecta | ACAGGACTC | ACTCAGG | assembly |
| *Neoitamus cyanurus* | Asilidae | Diptera | Insecta | ACAGGACTC | ACTCAGG | pacbio |
| *Tolmerus cingulatus* | Asilidae | Diptera | Insecta | AAAATAT | AAAATATAAAATAT | pacbio |
| *Bibio marci* | Bibionidae | Diptera | Insecta |  |  | assembly |
| *Bibio marci* | Bibionidae | Diptera | Insecta |  |  | pacbio |
| *Dilophus febrilis* | Bibionidae | Diptera | Insecta | AAATAG | AAATAAG | pacbio |
| *Bombylius discolor* | Bombyliidae | Diptera | Insecta | AAGTG | AAGATAC | assembly |
| *Bombylius discolor* | Bombyliidae | Diptera | Insecta |  |  | pacbio |
| *Bombylius major* | Bombyliidae | Diptera | Insecta | AATAT |  | assembly |
| *Bombylius major* | Bombyliidae | Diptera | Insecta | ACTACT | AATAAT | pacbio |
| *Villa cingulata* | Bombyliidae | Diptera | Insecta | AACCCT | AACCCTAACCCT | pacbio |
| *Villa modesta* | Bombyliidae | Diptera | Insecta | AATAAT | CCCCC | pacbio |
| *Bellardia bayeri* | Calliphoridae | Diptera | Insecta | ACATAT | AATTC | pacbio |
| *Bellardia pandia* | Calliphoridae | Diptera | Insecta | AATAAT | AATAATAAT | assembly |
| *Bellardia pandia* | Calliphoridae | Diptera | Insecta | ACATAT | AAATT | pacbio |
| *Calliphora vicina* | Calliphoridae | Diptera | Insecta | AACAGAACTAG | AACTAGAACTG | pacbio |
| *Calliphora vomitoria* | Calliphoridae | Diptera | Insecta | AAGAAGAAT | ACCAT | assembly |
| *Calliphora vomitoria* | Calliphoridae | Diptera | Insecta | AACAGAACTAG | AGATAGAT | pacbio |
| *Lucilia richardsi* | Calliphoridae | Diptera | Insecta | AGATAGAT | ACATACAT | pacbio |
| *Melinda gentilis* | Calliphoridae | Diptera | Insecta | ATCATC | ATCATCATC | pacbio |
| *Melinda viridicyanea* | Calliphoridae | Diptera | Insecta | AATGTATGT | AATGTATGTAATGTATGT | pacbio |
| *Protocalliphora azurea* | Calliphoridae | Diptera | Insecta | ACATAT | ACATATACATAT | assembly |
| *Protocalliphora azurea* | Calliphoridae | Diptera | Insecta | AGATAT | ACATAT | pacbio |
| *Protophormia terraenovae* | Calliphoridae | Diptera | Insecta | AGATAGAT | AAATAAAT | pacbio |
| *Chironomus plumosus* | Chironomidae | Diptera | Insecta | AAATT | ACTAGAG | pacbio |
| *Chlorops speciosus* | Chloropidae | Diptera | Insecta | AGATAGAT | AGATAGATAGAT | pacbio |
| *Clusia tigrina* | Clusiidae | Diptera | Insecta | ATATAT | ATATATATATATAT | assembly |
| *Clusia tigrina* | Clusiidae | Diptera | Insecta |  |  | pacbio |
| *Coelopa frigida* | Coelopidae | Diptera | Insecta | AAATGTCT | AAATGTCTAAATGTCT | pacbio |
| *Coelopa pilipes* | Coelopidae | Diptera | Insecta | AACAAT | AACAATAACAATAACAAT | assembly |
| *Coelopa pilipes* | Coelopidae | Diptera | Insecta | AACATT | AACAAT | pacbio |
| *Conops quadrifasciatus* | Conopidae | Diptera | Insecta | AAAAT | AAATT | pacbio |
| *Myopa tessellatipennis* | Conopidae | Diptera | Insecta | ACGCATG |  | assembly |
| *Myopa tessellatipennis* | Conopidae | Diptera | Insecta | ACGCATG | ACTCT | pacbio |
| *Myopa testacea* | Conopidae | Diptera | Insecta | ACGCATG | AAACATC | pacbio |
| *Physocephala rufipes* | Conopidae | Diptera | Insecta | ACAGACAG | AAAGACAAGAC | pacbio |
| *Sicus ferrugineus* | Conopidae | Diptera | Insecta | AAGTC | AAGTCAAGTC | assembly |
| *Sicus ferrugineus* | Conopidae | Diptera | Insecta | AAGTC | AAGTCAAGTC | pacbio |
| *Thecophora atra* | Conopidae | Diptera | Insecta | AACCAGCACACG | AACCAGCACACGAACCAGCACACG | assembly |
| *Thecophora atra* | Conopidae | Diptera | Insecta | AACCAGCACACG |  | pacbio |
| *Anopheles coluzzii* | Culicidae | Diptera | Insecta |  |  | pacbio |
| *Ochlerotatus annulipes* | Culicidae | Diptera | Insecta | ACTCACTC | ATCCGC | pacbio |
| *Poecilobothrus nobilitatus* | Dolichopodidae | Diptera | Insecta | AACAAT | AATGAT | assembly |
| *Poecilobothrus nobilitatus* | Dolichopodidae | Diptera | Insecta | AACAAT | AACAATAACAAT | pacbio |
| *Chymomyza fuscimana* | Drosophilidae | Diptera | Insecta | AAATAAT | AAATAAAT | pacbio |
| *Drosophila busckii* | Drosophilidae | Diptera | Insecta | ACTGACTG | AAGTAAT | pacbio |
| *Drosophila funebris* | Drosophilidae | Diptera | Insecta | AGATAT | ACACAT | pacbio |
| *Drosophila helvetica* | Drosophilidae | Diptera | Insecta |  |  | pacbio |
| *Drosophila histrio* | Drosophilidae | Diptera | Insecta | ACACAT | ACATAG | pacbio |
| *Drosophila kuntzei* | Drosophilidae | Diptera | Insecta | ACTGACTG | ACAGACAG | pacbio |
| *Drosophila limbata* | Drosophilidae | Diptera | Insecta | AAGTAT | AAATAT | pacbio |
| *Drosophila phalerata* | Drosophilidae | Diptera | Insecta | AAATAAGT | ACAGACAG | pacbio |
| *Drosophila testacea* | Drosophilidae | Diptera | Insecta | ACTGACTG | ACACAT | pacbio |
| *Hirtodrosophila cameraria* | Drosophilidae | Diptera | Insecta | ACACAT | AAATAAAT | pacbio |
| *Hirtodrosophila confusa* | Drosophilidae | Diptera | Insecta | ACAGAT | ACACAT | pacbio |
| *Hirtodrosophila trivittata* | Drosophilidae | Diptera | Insecta | AATCTATC | AAAGATAG | pacbio |
| *Empis aestiva* | Empididae | Diptera | Insecta | AAAATAT |  | pacbio |
| *Empis livida* | Empididae | Diptera | Insecta |  |  | pacbio |
| *Empis stercorea* | Empididae | Diptera | Insecta | AACAGC | ACTAT | pacbio |
| *Empis tessellata* | Empididae | Diptera | Insecta | AAAGAT | AAAATT | pacbio |
| *Empis trigramma* | Empididae | Diptera | Insecta | AAAATC | AAAATCAAAATC | pacbio |
| *Fannia armata* | Fanniidae | Diptera | Insecta | AAGTC | AAGTCAAGTC | pacbio |
| *Fannia lustrator* | Fanniidae | Diptera | Insecta | AAGACC | AAGACCAAGACC | pacbio |
| *Fannia serena* | Fanniidae | Diptera | Insecta |  |  | pacbio |
| *Suillia variegata* | Heleomyzidae | Diptera | Insecta | AAATAAAT | AAATAAATAAAT | pacbio |
| *Crataerina pallida* | Hippoboscidae | Diptera | Insecta | AAATC | AAACAAT | pacbio |
| *Hybos culiciformis* | Hybotidae | Diptera | Insecta | AAGTC | AAGTCAAGTC | pacbio |
| *Hybos femoratus* | Hybotidae | Diptera | Insecta |  |  | pacbio |
| *Sapromyzosoma quadripunctata* | Lauxaniidae | Diptera | Insecta | AAAAAC | AAAAACAAAAAC | pacbio |
| *Tricholauxania praeusta* | Lauxaniidae | Diptera | Insecta | AACTCACTC | AATAAT | pacbio |
| *Epiphragma ocellare* | Limoniidae | Diptera | Insecta | AAGATAG | AAGTCAGTC | pacbio |
| *Coenosia intermedia* | Muscidae | Diptera | Insecta | ACATATC | AACAAC | pacbio |
| *Hebecnema nigricolor* | Muscidae | Diptera | Insecta | ACATAT | ACATATACATAT | pacbio |
| *Hebecnema umbratica* | Muscidae | Diptera | Insecta | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Helina celsa* | Muscidae | Diptera | Insecta | AAGACAT | AAATAAAT | pacbio |
| *Helina depuncta* | Muscidae | Diptera | Insecta | AAATAAAT | AAAGTT | pacbio |
| *Helina evecta* | Muscidae | Diptera | Insecta | AAAGTT | AACATT | pacbio |
| *Helina quadrum* | Muscidae | Diptera | Insecta | AGATGAT | AATAG | pacbio |
| *Hydrotaea cyrtoneurina* | Muscidae | Diptera | Insecta | AATACT | AAATTAAT | pacbio |
| *Hydrotaea diabolus* | Muscidae | Diptera | Insecta | AAAAGGAT | ACAGGG | pacbio |
| *Lispe nana* | Muscidae | Diptera | Insecta |  |  | pacbio |
| *Lophosceles cinereiventris* | Muscidae | Diptera | Insecta | AAATG | AAATCTGAAATG | pacbio |
| *Mesembrina meridiana* | Muscidae | Diptera | Insecta | AAATAACT | ACAGACTG | pacbio |
| *Morellia simplex* | Muscidae | Diptera | Insecta | AATAAT | AAATAT | pacbio |
| *Musca autumnalis* | Muscidae | Diptera | Insecta | AAAATAT | AAAAT | pacbio |
| *Myospila meditabunda* | Muscidae | Diptera | Insecta | AATTAC | AATTACAATTAC | pacbio |
| *Neomyia cornicina* | Muscidae | Diptera | Insecta | ACATAT | ACATATACATAT | pacbio |
| *Phaonia gobertii* | Muscidae | Diptera | Insecta | AATTC | AGATAT | pacbio |
| *Phaonia pallida* | Muscidae | Diptera | Insecta | AATTC | AATTCAATTC | pacbio |
| *Phaonia palpata* | Muscidae | Diptera | Insecta | AGATAT | AATTC | pacbio |
| *Phaonia rufiventris* | Muscidae | Diptera | Insecta | AAGTC | AAGTCAAGTC | pacbio |
| *Phaonia subventa* | Muscidae | Diptera | Insecta | AATTC | AAAAT | pacbio |
| *Phaonia tuguriorum* | Muscidae | Diptera | Insecta | AAATAAAT | AAATAAATAAAT | pacbio |
| *Polietes domitor* | Muscidae | Diptera | Insecta | AAATAACT | AAATAACTAAATAACT | assembly |
| *Polietes domitor* | Muscidae | Diptera | Insecta | AAATAACT | AAATAACTAAATAACT | pacbio |
| *Polietes lardarius* | Muscidae | Diptera | Insecta | AAAGAACAT | AAATGAAT | pacbio |
| *Polietes meridionalis* | Muscidae | Diptera | Insecta | AAATGAAT | AAATGAATAAATGAAT | pacbio |
| *Thricops semicinereus* | Muscidae | Diptera | Insecta | ACAGACGG | ACAGACGGACAGACGG | pacbio |
| *Palloptera scutellata* | Pallopteridae | Diptera | Insecta | AAAGT | AAAGTAAAGT | pacbio |
| *Nephrocerus scutellatus* | Pipunculidae | Diptera | Insecta | AAACAAAC | AAACAAACC | assembly |
| *Nephrocerus scutellatus* | Pipunculidae | Diptera | Insecta | AAACAAAC | AAACAAACAAAC | pacbio |
| *Callomyia amoena* | Platypezidae | Diptera | Insecta | AAATG | AACAAC | pacbio |
| *Pollenia amentaria* | Polleniidae | Diptera | Insecta | AATGAT | AATGATAATGAT | assembly |
| *Pollenia amentaria* | Polleniidae | Diptera | Insecta | AATGAT | AATGATAATGAT | pacbio |
| *Pollenia angustigena* | Polleniidae | Diptera | Insecta | ACATACAT | ACATACATACAT | assembly |
| *Pollenia angustigena* | Polleniidae | Diptera | Insecta | ACATACAT | ACATACATACAT | pacbio |
| *Psila merdaria* | Psilidae | Diptera | Insecta | AATAG | AATACC | pacbio |
| *Chrysopilus cristatus* | Rhagionidae | Diptera | Insecta | AAATTAAT | AAATTAATAAATTAAT | pacbio |
| *Rhagio annulatus* | Rhagionidae | Diptera | Insecta | AATAAT | AAATAAAT | pacbio |
| *Rhagio lineola* | Rhagionidae | Diptera | Insecta | AAAATAT | AAAATATAAAATAT | pacbio |
| *Rhagio tringarius* | Rhagionidae | Diptera | Insecta | AAAATAAAT | AAATAAAT | pacbio |
| *Stomorhina lunata* | Rhiniidae | Diptera | Insecta | ACTAGACTATG | AATACT | assembly |
| *Stomorhina lunata* | Rhiniidae | Diptera | Insecta | AACTAGAACTG | AACAGAACTAG | pacbio |
| *Phyto melanocephala* | Rhinophoridae | Diptera | Insecta |  |  | assembly |
| *Phyto melanocephala* | Rhinophoridae | Diptera | Insecta | AAATT | AACAT | pacbio |
| *Rhinophora lepida* | Rhinophoridae | Diptera | Insecta | ACATACAT | ACATAT | pacbio |
| *Blaesoxipha plumicornis* | Sarcophagidae | Diptera | Insecta | AAAAC | AAAACAAAAC | pacbio |
| *Sarcophaga caerulescens* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | assembly |
| *Sarcophaga caerulescens* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga carnaria* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga crassimargo* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga haemorrhoa* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga nigriventris* | Sarcophagidae | Diptera | Insecta | AGATAT | AATAG | pacbio |
| *Sarcophaga rosellei* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | assembly |
| *Sarcophaga rosellei* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga subvicina* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | assembly |
| *Sarcophaga subvicina* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga variegata* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | assembly |
| *Sarcophaga variegata* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Cleigastra apicalis* | Scathophagidae | Diptera | Insecta | AAAAATT | AAATAAC | pacbio |
| *Scathophaga stercoraria* | Scathophagidae | Diptera | Insecta | AAGAAT | AAATC | pacbio |
| *Coremacera marginata* | Sciomyzidae | Diptera | Insecta | AAAAT | AAAATAAAAT | assembly |
| *Coremacera marginata* | Sciomyzidae | Diptera | Insecta | AAATT | AAGAAT | pacbio |
| *Dichetophora obliterata* | Sciomyzidae | Diptera | Insecta |  |  | pacbio |
| *Euthycera fumigata* | Sciomyzidae | Diptera | Insecta | AGATAT | AATATG | pacbio |
| *Hydromya dorsalis* | Sciomyzidae | Diptera | Insecta | AAATT | AAAATT | pacbio |
| *Pherbellia cinerella* | Sciomyzidae | Diptera | Insecta |  |  | pacbio |
| *Pherbellia dubia* | Sciomyzidae | Diptera | Insecta | ACTAT | AATGAT | pacbio |
| *Pherbina coryleti* | Sciomyzidae | Diptera | Insecta | AATGTC | AGAGAT | assembly |
| *Pherbina coryleti* | Sciomyzidae | Diptera | Insecta | AACATC | AGAGAT | pacbio |
| *Sepedon spinipes* | Sciomyzidae | Diptera | Insecta | AAGATAG | AAGATAGAAGATAG | pacbio |
| *Tetanocera arrogans* | Sciomyzidae | Diptera | Insecta | AAAGTT | AAAGTTAAAGTT | pacbio |
| *Beris chalybata* | Stratiomyidae | Diptera | Insecta | AAACATTTCAAATGATGGCTGAGGTT | AGATAGAT | pacbio |
| *Chloromyia formosa* | Stratiomyidae | Diptera | Insecta | ACAGACAG | ACAGACAGACAG | pacbio |
| *Microchrysa polita* | Stratiomyidae | Diptera | Insecta | AAAATTC | ACAGACAG | pacbio |
| *Nemotelus nigrinus* | Stratiomyidae | Diptera | Insecta | AATGATG | ACCGCATACCGT | assembly |
| *Nemotelus nigrinus* | Stratiomyidae | Diptera | Insecta | AGATAGAT | AGATAGATAGAT | pacbio |
| *Oplodontha viridula* | Stratiomyidae | Diptera | Insecta | ATATAT | ATATATAT | pacbio |
| *Oxycera rara* | Stratiomyidae | Diptera | Insecta | AACCCT | CCCCC | pacbio |
| *Oxycera trilineata* | Stratiomyidae | Diptera | Insecta |  |  | pacbio |
| *Pachygaster atra* | Stratiomyidae | Diptera | Insecta | ACAGACGG | AACGAATG | pacbio |
| *Sargus bipunctatus* | Stratiomyidae | Diptera | Insecta | AAGACAGAC | AAATG | pacbio |
| *Stratiomys potamida* | Stratiomyidae | Diptera | Insecta | AATACAG | AAAGTAAGTCTCTGT | pacbio |
| *Stratiomys singularior* | Stratiomyidae | Diptera | Insecta | AATCATC | AATCATCAATCATC | pacbio |
| *Baccha elongata* | Syrphidae | Diptera | Insecta | AACAAC | ACATGTC | pacbio |
| *Blera fallax* | Syrphidae | Diptera | Insecta |  |  | assembly |
| *Blera fallax* | Syrphidae | Diptera | Insecta | ACGATG | ACGATGACGATG | pacbio |
| *Brachypalpus laphriformis* | Syrphidae | Diptera | Insecta |  |  | assembly |
| *Brachypalpus laphriformis* | Syrphidae | Diptera | Insecta | ACTACT | AAATAAAT | pacbio |
| *Chalcosyrphus nemorum* | Syrphidae | Diptera | Insecta | ACTCT | AGAGGC | pacbio |
| *Cheilosia illustrata* | Syrphidae | Diptera | Insecta | AACAAC | AACAACAAC | pacbio |
| *Cheilosia impressa* | Syrphidae | Diptera | Insecta | AAAGGTTC | AAAGGTTCAAAGGTTC | pacbio |
| *Cheilosia pagana* | Syrphidae | Diptera | Insecta |  |  | assembly |
| *Cheilosia pagana* | Syrphidae | Diptera | Insecta |  |  | pacbio |
| *Cheilosia soror* | Syrphidae | Diptera | Insecta |  |  | pacbio |
| *Cheilosia urbana* | Syrphidae | Diptera | Insecta |  |  | assembly |
| *Cheilosia urbana* | Syrphidae | Diptera | Insecta | AACTCC | ACACCG | pacbio |
| *Cheilosia vulpina* | Syrphidae | Diptera | Insecta |  |  | assembly |
| *Cheilosia vulpina* | Syrphidae | Diptera | Insecta |  |  | pacbio |
| *Chrysogaster coemiteriorum* | Syrphidae | Diptera | Insecta | AACAAC | AACAACAAC | pacbio |
| *Chrysotoxum bicinctum* | Syrphidae | Diptera | Insecta | AAATACAATAC | AATAC | assembly |
| *Chrysotoxum bicinctum* | Syrphidae | Diptera | Insecta | AAATACAATAC | AACAAG | pacbio |
| *Chrysotoxum festivum* | Syrphidae | Diptera | Insecta | AGATAGAT | AAAGT | pacbio |
| *Chrysotoxum verralli* | Syrphidae | Diptera | Insecta | ATCATC | ATCATCATC | pacbio |
| *Criorhina berberina* | Syrphidae | Diptera | Insecta | AAATT | ACCCC | assembly |
| *Criorhina berberina* | Syrphidae | Diptera | Insecta | AGGAT |  | pacbio |
| *Criorhina floccosa* | Syrphidae | Diptera | Insecta | AACCT | AAAAT | pacbio |
| *Dasysyrphus albostriatus* | Syrphidae | Diptera | Insecta | AACAAT | AACAGC | assembly |
| *Dasysyrphus albostriatus* | Syrphidae | Diptera | Insecta | AACAAC | AACAACAAC | pacbio |
| *Dasysyrphus tricinctus* | Syrphidae | Diptera | Insecta | AACATGC | AACATGCAACATGC | pacbio |
| *Epistrophe eligans* | Syrphidae | Diptera | Insecta | AATTC | AAAAT | pacbio |
| *Epistrophe grossulariae* | Syrphidae | Diptera | Insecta | AAATT | AAATTAAATT | assembly |
| *Epistrophe grossulariae* | Syrphidae | Diptera | Insecta | ACAGTG | AAATT | pacbio |
| *Epistrophella euchroma* | Syrphidae | Diptera | Insecta | AGATAGAT | AGATAGATAGAT | assembly |
| *Epistrophella euchroma* | Syrphidae | Diptera | Insecta | AAAAT | AAAGT | pacbio |
| *Episyrphus balteatus* | Syrphidae | Diptera | Insecta | AAAATTC | AAGATGTCCCG | assembly |
| *Episyrphus balteatus* | Syrphidae | Diptera | Insecta | AATAG | AAATT | pacbio |
| *Eristalinus sepulchralis* | Syrphidae | Diptera | Insecta |  |  | assembly |
| *Eristalinus sepulchralis* | Syrphidae | Diptera | Insecta | AATAAT | AAATAAT | pacbio |
| *Eristalis arbustorum* | Syrphidae | Diptera | Insecta | AGCTATG | ATATAT | assembly |
| *Eristalis arbustorum* | Syrphidae | Diptera | Insecta | AATAAT | AAATAAAT | pacbio |
| *Eristalis horticola* | Syrphidae | Diptera | Insecta | AACATGC | AAGCATC | pacbio |
| *Eristalis pertinax* | Syrphidae | Diptera | Insecta | AACTG | AAACAAAT | assembly |
| *Eristalis pertinax* | Syrphidae | Diptera | Insecta | AAATAC | AAGAAT | pacbio |
| *Eristalis tenax* | Syrphidae | Diptera | Insecta | AAGAAT | AAGAATAAGAAT | assembly |
| *Eristalis tenax* | Syrphidae | Diptera | Insecta | AAGAAT | ACCATCC | pacbio |
| *Eumerus sabulonum* | Syrphidae | Diptera | Insecta |  |  | pacbio |
| *Eupeodes corollae* | Syrphidae | Diptera | Insecta | AAATC | AGATAT | assembly |
| *Eupeodes corollae* | Syrphidae | Diptera | Insecta | ACTATC | AATGAT | pacbio |
| *Eupeodes latifasciatus* | Syrphidae | Diptera | Insecta | ACCATG | ATCATC | assembly |
| *Eupeodes latifasciatus* | Syrphidae | Diptera | Insecta | ACCATG | AATAG | pacbio |
| *Eupeodes luniger* | Syrphidae | Diptera | Insecta | ACCATC | AATGAT | pacbio |
| *Ferdinandea cuprea* | Syrphidae | Diptera | Insecta | AACAAC | AACAACAAC | pacbio |
| *Helophilus pendulus* | Syrphidae | Diptera | Insecta | AATAAT | AACAAT | pacbio |
| *Leucozona laternaria* | Syrphidae | Diptera | Insecta | AATAGT | AATAGTAATAGT | assembly |
| *Leucozona laternaria* | Syrphidae | Diptera | Insecta | AATAG | AACAAC | pacbio |
| *Melangyna compositarum* | Syrphidae | Diptera | Insecta | AATGGC | AAGATT | pacbio |
| *Melangyna quadrimaculata* | Syrphidae | Diptera | Insecta | AATGGC | AAAGT | pacbio |
| *Melangyna umbellatarum* | Syrphidae | Diptera | Insecta | AAATT | AAGAGTGT | pacbio |
| *Melanostoma mellinum* | Syrphidae | Diptera | Insecta | AACAAC | AACAACAAC | assembly |
| *Melanostoma mellinum* | Syrphidae | Diptera | Insecta | AACAAC | AACAACAAC | pacbio |
| *Melanostoma scalare* | Syrphidae | Diptera | Insecta | AATAAT | AACAAC | pacbio |
| *Meliscaeva auricollis* | Syrphidae | Diptera | Insecta | ACATCGAGTATCG | ACAGACTG | pacbio |
| *Myathropa florea* | Syrphidae | Diptera | Insecta | AGCCAGCC | AAAATG | assembly |
| *Myathropa florea* | Syrphidae | Diptera | Insecta | AGCCAGCC | AAATACAT | pacbio |
| *Neoascia interrupta* | Syrphidae | Diptera | Insecta | AACAAT | AAAAAGT | pacbio |
| *Paragus haemorrhous* | Syrphidae | Diptera | Insecta | AATAAT | ATCATC | pacbio |
| *Pipizella viduata* | Syrphidae | Diptera | Insecta | AAATAAT | ACAGACTGACTG | pacbio |
| *Platycheirus albimanus* | Syrphidae | Diptera | Insecta | ACGTAG | ACACAC | assembly |
| *Platycheirus albimanus* | Syrphidae | Diptera | Insecta | ACGTAG | ACACAC | pacbio |
| *Platycheirus rosarum* | Syrphidae | Diptera | Insecta |  |  | pacbio |
| *Platycheirus scutatus* | Syrphidae | Diptera | Insecta |  |  | pacbio |
| *Portevinia maculata* | Syrphidae | Diptera | Insecta | ACGATG | AAGTCC | pacbio |
| *Rhingia campestris* | Syrphidae | Diptera | Insecta | ACCATCT | ACGGACGG | assembly |
| *Rhingia campestris* | Syrphidae | Diptera | Insecta | ACCATCT | AAATATAG | pacbio |
| *Rhingia rostrata* | Syrphidae | Diptera | Insecta | ACATACAT | ACATACATACAT | pacbio |
| *Scaeva pyrastri* | Syrphidae | Diptera | Insecta |  |  | assembly |
| *Scaeva pyrastri* | Syrphidae | Diptera | Insecta | AACTT | AATAG | pacbio |
| *Sericomyia silentis* | Syrphidae | Diptera | Insecta | ACAGACTG | ACAGACTGACAGACTG | pacbio |
| *Sphaerophoria scripta* | Syrphidae | Diptera | Insecta | AACTT | AATAAT | pacbio |
| *Sphaerophoria taeniata* | Syrphidae | Diptera | Insecta |  |  | assembly |
| *Sphaerophoria taeniata* | Syrphidae | Diptera | Insecta | ATCATC | AAAAA | pacbio |
| *Syritta pipiens* | Syrphidae | Diptera | Insecta | ACACAT |  | assembly |
| *Syritta pipiens* | Syrphidae | Diptera | Insecta | ATCATC | ACACAT | pacbio |
| *Syrphus ribesii* | Syrphidae | Diptera | Insecta | AACAAC | ATGCCC | pacbio |
| *Syrphus vitripennis* | Syrphidae | Diptera | Insecta | AACAAG | AACAAT | pacbio |
| *Volucella bombylans* | Syrphidae | Diptera | Insecta | AAATAAT | AAGTAAGT | pacbio |
| *Volucella inanis* | Syrphidae | Diptera | Insecta | ACAGGTG | AAATAAC | assembly |
| *Volucella inanis* | Syrphidae | Diptera | Insecta | AAATAAC | AAATAAT | pacbio |
| *Volucella inflata* | Syrphidae | Diptera | Insecta | AATAAT |  | assembly |
| *Volucella inflata* | Syrphidae | Diptera | Insecta | AATAAT |  | pacbio |
| *Volucella pellucens* | Syrphidae | Diptera | Insecta | AATAAT | AATAATAAT | pacbio |
| *Volucella zonaria* | Syrphidae | Diptera | Insecta | AACACC | AACAC | pacbio |
| *Xanthogramma pedissequum* | Syrphidae | Diptera | Insecta | ACAGACTG | AATAG | assembly |
| *Xanthogramma pedissequum* | Syrphidae | Diptera | Insecta | ACAGACTG | ATCATC | pacbio |
| *Xylota sylvarum* | Syrphidae | Diptera | Insecta | AGGATG | AGGATGAGGATG | assembly |
| *Xylota sylvarum* | Syrphidae | Diptera | Insecta | ACTGACTG | AGGATG | pacbio |
| *Tabanus autumnalis* | Tabanidae | Diptera | Insecta | ATCATC | ACACAC | pacbio |
| *Tabanus bromius* | Tabanidae | Diptera | Insecta | AAAACAT | ATCATC | pacbio |
| *Actia lamia* | Tachinidae | Diptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Cistogaster globosa* | Tachinidae | Diptera | Insecta | AAAAATGGCAT | AATGAT | assembly |
| *Cistogaster globosa* | Tachinidae | Diptera | Insecta | AATAT | AATAAT | pacbio |
| *Epicampocera succincta* | Tachinidae | Diptera | Insecta | ACACTACTGTACACTATAGGGT |  | assembly |
| *Epicampocera succincta* | Tachinidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Eriothrix rufomaculata* | Tachinidae | Diptera | Insecta | ACATAT | ACATATACATAT | pacbio |
| *Gymnocheta viridis* | Tachinidae | Diptera | Insecta | ATCATC | ATCATCATC | pacbio |
| *Gymnosoma rotundatum* | Tachinidae | Diptera | Insecta | AAAAAAAATT | AATAAT | assembly |
| *Gymnosoma rotundatum* | Tachinidae | Diptera | Insecta | AATAAT | ACTAT | pacbio |
| *Linnaemya tessellans* | Tachinidae | Diptera | Insecta | AAAAA | AAAAAA | pacbio |
| *Lypha dubia* | Tachinidae | Diptera | Insecta |  |  | assembly |
| *Lypha dubia* | Tachinidae | Diptera | Insecta | AATAG | AATAAT | pacbio |
| *Nowickia ferox* | Tachinidae | Diptera | Insecta | AATGAT | AATGATAATGAT | assembly |
| *Nowickia ferox* | Tachinidae | Diptera | Insecta | AATGAT | ACATAT | pacbio |
| *Panzeria rudis* | Tachinidae | Diptera | Insecta | ACATACAT | ACATACATACAT | pacbio |
| *Phasia barbifrons* | Tachinidae | Diptera | Insecta | ACATAT | ACACT | pacbio |
| *Phasia hemiptera* | Tachinidae | Diptera | Insecta | AATAGT | AATAGTAATAGT | pacbio |
| *Phasia obesa* | Tachinidae | Diptera | Insecta | ACATAT | AAATT | pacbio |
| *Tachina fera* | Tachinidae | Diptera | Insecta | ACTAT | ACTATACTAT | assembly |
| *Tachina fera* | Tachinidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Tachina grossa* | Tachinidae | Diptera | Insecta | ACATAT | AATAG | pacbio |
| *Tachina lurida* | Tachinidae | Diptera | Insecta | AACTAATACCAGACACCAGAT | ACTAT | assembly |
| *Tachina lurida* | Tachinidae | Diptera | Insecta | ACATAT | AATAG | pacbio |
| *Thecocarcelia acutangulata* | Tachinidae | Diptera | Insecta | AATCAT | AATGAT | assembly |
| *Thecocarcelia acutangulata* | Tachinidae | Diptera | Insecta | AATCAT | AATCATAATCAT | pacbio |
| *Thelaira solivaga* | Tachinidae | Diptera | Insecta | AACCATACC |  | assembly |
| *Thelaira solivaga* | Tachinidae | Diptera | Insecta | AAAAT | AACCATACC | pacbio |
| *Anomoia purmunda* | Tephritidae | Diptera | Insecta | AATGAT | AATAAT | pacbio |
| *Merzomyia westermanni* | Tephritidae | Diptera | Insecta | AAAAG | AAAGT | pacbio |
| *Sphenella marginata* | Tephritidae | Diptera | Insecta | AAAAT | AACATT | pacbio |
| *Tephritis neesii* | Tephritidae | Diptera | Insecta | AAAAT | AAGACC | pacbio |
| *Terellia serratulae* | Tephritidae | Diptera | Insecta | AATAAT | AAAAAT | pacbio |
| *Thereva unica* | Therevidae | Diptera | Insecta | AATACAT | AATACATAATACAT | pacbio |
| *Ctenophora pectinicornis* | Tipulidae | Diptera | Insecta | ACGAGG | AAAATAAAT | pacbio |
| *Nephrotoma appendiculata* | Tipulidae | Diptera | Insecta | AAAATATG | AAAATATGAAAATATG | assembly |
| *Nephrotoma appendiculata* | Tipulidae | Diptera | Insecta | AAAATATG | ACACAC | pacbio |
| *Nephrotoma flavescens* | Tipulidae | Diptera | Insecta | AAAATATG | AAAATATGAAAATATG | assembly |
| *Nephrotoma flavescens* | Tipulidae | Diptera | Insecta | AAAATATG | AAGTAAT | pacbio |
| *Nephrotoma flavipalpis* | Tipulidae | Diptera | Insecta | AGATAT | AAATAAATT | pacbio |
| *Tipula confusa* | Tipulidae | Diptera | Insecta |  |  | pacbio |
| *Tipula luna* | Tipulidae | Diptera | Insecta | AAATAAATT | AAGTCC | pacbio |
| *Tipula paludosa* | Tipulidae | Diptera | Insecta | AGATATAT | AGATAT | pacbio |
| *Tipula unca* | Tipulidae | Diptera | Insecta | AAATTCTT | AAATTCTTAAATTCTT | pacbio |
| *Tipula vernalis* | Tipulidae | Diptera | Insecta | AAAATGT | ACCATC | pacbio |
| *Herina lugubris* | Ulidiidae | Diptera | Insecta | AAATT | AATAAT | pacbio |
| *Xylophagus ater* | Xylophagaidae | Diptera | Insecta | AACATAT | AACATATAACATAT | pacbio |
| *Cloeon dipterum* | Baetidae | Ephemeroptera | Insecta |  |  | pacbio |
| *Ecdyonurus torrentis* | Heptageniidae | Ephemeroptera | Insecta |  |  | pacbio |
| *Rhithrogena germanica* | Heptageniidae | Ephemeroptera | Insecta |  |  | pacbio |
| *Rhithrogena semicolorata* | Heptageniidae | Ephemeroptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Siphlonurus alternatus* | Siphlonuridae | Ephemeroptera | Insecta | AACCAACC | AACCAACCAACC | pacbio |
| *Acanthosoma haemorrhoidale* | Acanthosomatidae | Hemiptera | Insecta | AAACCACCCT | AAACCACCCTAAACCACCCT | assembly |
| *Acanthosoma haemorrhoidale* | Acanthosomatidae | Hemiptera | Insecta | AAACCACCCT |  | pacbio |
| *Elasmostethus interstinctus* | Acanthosomatidae | Hemiptera | Insecta | AAACCACCCT | AGATAGAT | pacbio |
| *Elasmucha grisea* | Acanthosomatidae | Hemiptera | Insecta |  |  | pacbio |
| *Aphelocheirus aestivalis* | Aphelocheiridae | Hemiptera | Insecta | ACAGAGAGGC | AATAT | pacbio |
| *Drepanosiphum platanoidis* | Aphididae | Hemiptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Drepanosiphum platanoidis* | Aphididae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Philaenus spumarius* | Aphrophoridae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cercopis vulnerata* | Cercopidae | Hemiptera | Insecta | ACACAC | AACCT | pacbio |
| *Anoscopus histrionicus* | Cicadellidae | Hemiptera | Insecta | AATATAG | AATGG | pacbio |
| *Aphrodes makarovi* | Cicadellidae | Hemiptera | Insecta | AAGAAT | AAGAATAAGAAT | pacbio |
| *Evacanthus interruptus* | Cicadellidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ledra aurita* | Cicadellidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mocydia crocea* | Cicadellidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Opsius stactogalus* | Cicadellidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Rhytistylus proceps* | Cicadellidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cixius nervosus* | Cixiidae | Hemiptera | Insecta | AAAATTGTTGATGGAGATCATAC | AACCT | pacbio |
| *Tachycixius pilosus* | Cixiidae | Hemiptera | Insecta | AACCT | AAAAAA | pacbio |
| *Coreus marginatus* | Coreidae | Hemiptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Enoplops scapha* | Coreidae | Hemiptera | Insecta | ACAGAG | AGATAGAT | pacbio |
| *Gonocerus acuteangulatus* | Coreidae | Hemiptera | Insecta | AACCATCCCT | AACCATCCCTAACCATCCCT | assembly |
| *Gonocerus acuteangulatus* | Coreidae | Hemiptera | Insecta |  |  | pacbio |
| *Leptoglossus occidentalis* | Coreidae | Hemiptera | Insecta | ACACAC | AACCACCCCT | pacbio |
| *Canthophorus impressus* | Cydnidae | Hemiptera | Insecta | AAAAA | AAAAAA | pacbio |
| *Legnotus limbosus* | Cydnidae | Hemiptera | Insecta | AAATAACT | AAATAACTAAATAACT | pacbio |
| *Tritomegas bicolor* | Cydnidae | Hemiptera | Insecta | ACACAC | ACACACACAC | pacbio |
| *Conomelus anceps* | Delphacidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Stenocranus minutus* | Delphacidae | Hemiptera | Insecta | AACCT | ATCATC | pacbio |
| *Issus coleoptratus* | Issidae | Hemiptera | Insecta | AACCT | ACACAC | pacbio |
| *Kleidocerys resedae* | Lygaeidae | Hemiptera | Insecta | AATAC | ACTCTGAG | pacbio |
| *Centrotus cornutus* | Membracidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Loricula elegantula* | Microphysidae | Hemiptera | Insecta | AAATG | AAATGAAATG | pacbio |
| *Closterotomus norwegicus* | Miridae | Hemiptera | Insecta | AACCATCCCT | AACCATCCCTAACCATCCCT | pacbio |
| *Closterotomus trivialis* | Miridae | Hemiptera | Insecta | ACCGAG | AACCATCCCT | pacbio |
| *Grypocoris stysi* | Miridae | Hemiptera | Insecta | AACCATCCCT | AACCATCCCTAACCATCCCT | pacbio |
| *Lygus pratensis* | Miridae | Hemiptera | Insecta | AACACTCCCT |  | pacbio |
| *Neolygus contaminatus* | Miridae | Hemiptera | Insecta | AACAAGCACC | AACAAGCACCAACAAGCACC | pacbio |
| *Pantilius tunicatus* | Miridae | Hemiptera | Insecta |  |  | pacbio |
| *Pilophorus perplexus* | Miridae | Hemiptera | Insecta | AGAGGGATG | AACCATCCCT | pacbio |
| *Rhabdomiris striatellus* | Miridae | Hemiptera | Insecta | AACCATCCCT | AACCATCCCTAACCATCCCT | pacbio |
| *Stenodema laevigata* | Miridae | Hemiptera | Insecta | AACCATCCCT | ACATACAT | pacbio |
| *Icerya purchasi* | Monophlebidae | Hemiptera | Insecta | AATAAT | AATAATAAT | pacbio |
| *Himacerus apterus* | Nabidae | Hemiptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Himacerus mirmicoides* | Nabidae | Hemiptera | Insecta | AACCATCCCT | ACACAC | pacbio |
| *Nabis ferus* | Nabidae | Hemiptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Nabis limbatus* | Nabidae | Hemiptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Nabis rugosus* | Nabidae | Hemiptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Notonecta glauca* | Notonectidae | Hemiptera | Insecta | AAACCTATCC |  | pacbio |
| *Aelia acuminata* | Pentatomidae | Hemiptera | Insecta | AACCATCCCT |  | assembly |
| *Aelia acuminata* | Pentatomidae | Hemiptera | Insecta |  |  | pacbio |
| *Dolycoris baccarum* | Pentatomidae | Hemiptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Eurydema oleracea* | Pentatomidae | Hemiptera | Insecta |  |  | pacbio |
| *Eysarcoris venustissimus* | Pentatomidae | Hemiptera | Insecta | AACCATCCCT | AACCATCCCTAACCATCCCT | pacbio |
| *Pentatoma rufipes* | Pentatomidae | Hemiptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Podops inunctus* | Pentatomidae | Hemiptera | Insecta | AACCACCCCT |  | pacbio |
| *Rhaphigaster nebulosa* | Pentatomidae | Hemiptera | Insecta | AACCACCCCT | AGATAGAT | pacbio |
| *Troilus luridus* | Pentatomidae | Hemiptera | Insecta | AAATCCCTCTAGGGACCTAG | ACATACAT | pacbio |
| *Plea minutissima* | Pleidae | Hemiptera | Insecta | AAGAATATAGAAT | AAGAATATAGAATAAGAATATAGAAT | pacbio |
| *Planococcus citri* | Pseudococcidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cacopsylla fulguralis* | Psyllidae | Hemiptera | Insecta | AACCT | ACCATC | pacbio |
| *Corizus hyoscyami* | Rhopalidae | Hemiptera | Insecta | AACCATCCCT | ACAGACAG | pacbio |
| *Rhopalus parumpunctatus* | Rhopalidae | Hemiptera | Insecta | ACACAC | AAGCAT | pacbio |
| *Rhopalus subrufus* | Rhopalidae | Hemiptera | Insecta | ACTCACTC | ACTCACTCACTCACTC | pacbio |
| *Drymus ryeii* | Rhyparochromidae | Hemiptera | Insecta | AACCTACCT | AACCATCCCT | pacbio |
| *Rhyparochromus vulgaris* | Rhyparochromidae | Hemiptera | Insecta | AACCATCCCT | AATAAT | pacbio |
| *Andrena bicolor* | Andrenidae | Hymenoptera | Insecta | AACCTG | AAGCC | pacbio |
| *Andrena bucephala* | Andrenidae | Hymenoptera | Insecta | AAAAT | AACACTAACCC | assembly |
| *Andrena bucephala* | Andrenidae | Hymenoptera | Insecta | ACCAGTG | AAAATAATTG | pacbio |
| *Andrena chrysosceles* | Andrenidae | Hymenoptera | Insecta | ACTCATACTCAT | AACATG | pacbio |
| *Andrena dorsata* | Andrenidae | Hymenoptera | Insecta | AAAGGGCATGAGGGT |  | assembly |
| *Andrena dorsata* | Andrenidae | Hymenoptera | Insecta |  |  | pacbio |
| *Andrena fulva* | Andrenidae | Hymenoptera | Insecta | AAGTCGGCGGCGGGAC | AAAAAACCAG | assembly |
| *Andrena fulva* | Andrenidae | Hymenoptera | Insecta | AAACG | AATGGT | pacbio |
| *Andrena haemorrhoa* | Andrenidae | Hymenoptera | Insecta | AAACGAGTC | AACGAGTCG | assembly |
| *Andrena haemorrhoa* | Andrenidae | Hymenoptera | Insecta | AACGAGTCG | AAACGAGTC | pacbio |
| *Andrena hattorfiana* | Andrenidae | Hymenoptera | Insecta | AAAAAC | ACCCATGACCCCAG | assembly |
| *Andrena hattorfiana* | Andrenidae | Hymenoptera | Insecta | AAAAAC | ACGACG | pacbio |
| *Andrena helvola* | Andrenidae | Hymenoptera | Insecta | AACGAC | AAGGGTGAAGGGTGT | pacbio |
| *Andrena minutula* | Andrenidae | Hymenoptera | Insecta | AAATT | ACCCATACCGATACCCATACCGAT | assembly |
| *Andrena minutula* | Andrenidae | Hymenoptera | Insecta |  |  | pacbio |
| *Andrena nitida* | Andrenidae | Hymenoptera | Insecta | AAGTC | ACTGG | pacbio |
| *Andrena praecox* | Andrenidae | Hymenoptera | Insecta | AAAAT | AAACCCT | pacbio |
| *Andrena trimmerana* | Andrenidae | Hymenoptera | Insecta | ACCAGTG | AAAAATAATTG | pacbio |
| *Panurgus banksianus* | Andrenidae | Hymenoptera | Insecta | ACGACG | AACCT | pacbio |
| *Anthophora furcata* | Apidae | Hymenoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Anthophora plumipes* | Apidae | Hymenoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Bombus campestris* | Apidae | Hymenoptera | Insecta | AACCCCAACCT | AACGTAT | assembly |
| *Bombus campestris* | Apidae | Hymenoptera | Insecta |  |  | pacbio |
| *Bombus hortorum* | Apidae | Hymenoptera | Insecta | AACCCCAACCT | AACGTAT | assembly |
| *Bombus hortorum* | Apidae | Hymenoptera | Insecta | AACCCCAACCT | AACCT | pacbio |
| *Bombus hypnorum* | Apidae | Hymenoptera | Insecta | AACCCCAACCT | ACTCT | assembly |
| *Bombus hypnorum* | Apidae | Hymenoptera | Insecta | ACTCT | AACCCCAACCT | pacbio |
| *Bombus lapidarius* | Apidae | Hymenoptera | Insecta | AACCCCAACCT | AACCCCAACCTAACCCCAACCT | pacbio |
| *Bombus muscorum* | Apidae | Hymenoptera | Insecta | AAAGAC | AAAGACAAAGAC | pacbio |
| *Bombus pascuorum* | Apidae | Hymenoptera | Insecta | AAAAAC | AAAAACGAAAAC | assembly |
| *Bombus pascuorum* | Apidae | Hymenoptera | Insecta | AAAACG | AACCCCAACCT | pacbio |
| *Bombus pratorum* | Apidae | Hymenoptera | Insecta | AACGAACG | AACGAACGAACG | assembly |
| *Bombus pratorum* | Apidae | Hymenoptera | Insecta | AACGAACG | AACCCCAACCT | pacbio |
| *Bombus rupestris* | Apidae | Hymenoptera | Insecta | AACCCCAACCT | AACTG | pacbio |
| *Bombus sylvestris* | Apidae | Hymenoptera | Insecta | AACCCGAACCT | AACGTAT | assembly |
| *Bombus sylvestris* | Apidae | Hymenoptera | Insecta | AACCCGAACCT |  | pacbio |
| *Bombus terrestris* | Apidae | Hymenoptera | Insecta | AACGTAT | AACCCCAACCT | assembly |
| *Bombus terrestris* | Apidae | Hymenoptera | Insecta | AACCCCAACCT | AACCT | pacbio |
| *Bombus vestalis* | Apidae | Hymenoptera | Insecta | AACTG | AACCCCAACCT | pacbio |
| *Nomada fabriciana* | Apidae | Hymenoptera | Insecta | AACCT |  | assembly |
| *Nomada fabriciana* | Apidae | Hymenoptera | Insecta |  |  | pacbio |
| *Nomada ferruginata* | Apidae | Hymenoptera | Insecta | AGCCG | AAGTAAGT | pacbio |
| *Nomada flava* | Apidae | Hymenoptera | Insecta | ATCATC | ATCATCATC | pacbio |
| *Nomada fucata* | Apidae | Hymenoptera | Insecta | AAACCTAACCC | AGCCG | pacbio |
| *Nomada goodeniana* | Apidae | Hymenoptera | Insecta | AAACCTAACCC | AAACCTAACCCAAACCTAACCC | pacbio |
| *Nomada hirtipes* | Apidae | Hymenoptera | Insecta | AGCCG | AGCCGAGCCGAGCCG | pacbio |
| *Nomada lathburiana* | Apidae | Hymenoptera | Insecta | AAACCTAACCC | AAACCTAACCCAAACCTAACCC | pacbio |
| *Nomada panzeri* | Apidae | Hymenoptera | Insecta | AAACCTAACCC | AGCCG | pacbio |
| *Nomada ruficornis* | Apidae | Hymenoptera | Insecta | AAACCTAACC | AAACCTAACCAAACCTAACC | pacbio |
| *Athalia circularis* | Athaliidae | Hymenoptera | Insecta | ACGACG | ACGACGACG | pacbio |
| *Athalia cordata* | Athaliidae | Hymenoptera | Insecta |  |  | pacbio |
| *Athalia rosae* | Athaliidae | Hymenoptera | Insecta | AAAAA | AAAAAA | pacbio |
| *Homolobus annulicornis* | Braconidae | Hymenoptera | Insecta | ACGATG | AAGAGAC | pacbio |
| *Chalcis sispes* | Chalcididae | Hymenoptera | Insecta | ACGATG | ATCATC | pacbio |
| *Abia sericea* | Cimbicidae | Hymenoptera | Insecta |  |  | pacbio |
| *Hylaeus communis* | Colletidae | Hymenoptera | Insecta |  |  | pacbio |
| *Cerceris arenaria* | Crabronidae | Hymenoptera | Insecta | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Cerceris rybyensis* | Crabronidae | Hymenoptera | Insecta | AACCCAGACCT | AAAAT | assembly |
| *Cerceris rybyensis* | Crabronidae | Hymenoptera | Insecta | AACCCAGACCT | ACCACT | pacbio |
| *Crossocerus cetratus* | Crabronidae | Hymenoptera | Insecta | ACCAG | AAATT | pacbio |
| *Crossocerus megacephalus* | Crabronidae | Hymenoptera | Insecta | ACTGACTG | ACTGACTGACTG | pacbio |
| *Ectemnius cavifrons* | Crabronidae | Hymenoptera | Insecta | AACAG | ACTCT | pacbio |
| *Ectemnius continuus* | Crabronidae | Hymenoptera | Insecta |  |  | assembly |
| *Ectemnius continuus* | Crabronidae | Hymenoptera | Insecta |  |  | pacbio |
| *Ectemnius lituratus* | Crabronidae | Hymenoptera | Insecta | AACCCAGACCT |  | assembly |
| *Ectemnius lituratus* | Crabronidae | Hymenoptera | Insecta | ACTCACTC |  | pacbio |
| *Mimumesa dahlbomi* | Crabronidae | Hymenoptera | Insecta | ACCTG | ACCTGACCTG | assembly |
| *Mimumesa dahlbomi* | Crabronidae | Hymenoptera | Insecta |  |  | pacbio |
| *Nysson spinosus* | Crabronidae | Hymenoptera | Insecta | AACCCAGACCT | AACAT | assembly |
| *Nysson spinosus* | Crabronidae | Hymenoptera | Insecta | AACCCAGACCT |  | pacbio |
| *Pemphredon lugubris* | Crabronidae | Hymenoptera | Insecta | ACCCAG | ACTATCG | assembly |
| *Pemphredon lugubris* | Crabronidae | Hymenoptera | Insecta |  |  | pacbio |
| *Trypoxylon attenuatum* | Crabronidae | Hymenoptera | Insecta | ACCTG | ACTGGG | pacbio |
| *Trypoxylon clavicerum* | Crabronidae | Hymenoptera | Insecta |  |  | pacbio |
| *Lasius fuliginosus* | Formicidae | Hymenoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lasius niger* | Formicidae | Hymenoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Myrmica ruginodis* | Formicidae | Hymenoptera | Insecta | AACCT | AGCAGC | pacbio |
| *Gasteruption jaculator* | Gasteruptiidae | Hymenoptera | Insecta | AAAACCCTAGC | ACCATC | pacbio |
| *Lasioglossum calceatum* | Halictidae | Hymenoptera | Insecta | AACGTAT | AACGTAC | pacbio |
| *Lasioglossum fulvicorne* | Halictidae | Hymenoptera | Insecta |  |  | pacbio |
| *Lasioglossum lativentre* | Halictidae | Hymenoptera | Insecta | AATAT | AACCCAGACCT | assembly |
| *Lasioglossum lativentre* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | ACAGACAG | pacbio |
| *Lasioglossum leucozonium* | Halictidae | Hymenoptera | Insecta |  |  | pacbio |
| *Lasioglossum malachurum* | Halictidae | Hymenoptera | Insecta | ACATCGT | AATGAATG | pacbio |
| *Lasioglossum morio* | Halictidae | Hymenoptera | Insecta | AACGTAT | AACGCAT | assembly |
| *Lasioglossum morio* | Halictidae | Hymenoptera | Insecta | AACGTAT | AACGCAT | pacbio |
| *Lasioglossum pauxillum* | Halictidae | Hymenoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lasioglossum pauxillum* | Halictidae | Hymenoptera | Insecta | AGCAGC | AACCT | pacbio |
| *Lasioglossum villosulum* | Halictidae | Hymenoptera | Insecta | AACTGTG | AACTGTGAACTGTG | pacbio |
| *Seladonia tumulorum* | Halictidae | Hymenoptera | Insecta | AACCCT | AACCCTAACCCT | assembly |
| *Seladonia tumulorum* | Halictidae | Hymenoptera | Insecta |  |  | pacbio |
| *Sphecodes crassus* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | AACCCAGACCTAACCCAGACCT | pacbio |
| *Sphecodes ephippius* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | AGAGATATG | pacbio |
| *Sphecodes hyalinatus* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | AGATATG | pacbio |
| *Sphecodes monilicornis* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | AATATACTAG | assembly |
| *Sphecodes monilicornis* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | AGATAT | pacbio |
| *Alloplasta piceator* | Ichneumonidae | Hymenoptera | Insecta | ACGACGACT | ACGATG | assembly |
| *Alloplasta piceator* | Ichneumonidae | Hymenoptera | Insecta | ACGACG | ATCATC | pacbio |
| *Amblyjoppa fuscipennis* | Ichneumonidae | Hymenoptera | Insecta | ACGAGG | ACGCACGC | pacbio |
| *Amblyjoppa proteus* | Ichneumonidae | Hymenoptera | Insecta | ACACGC | ACGAGG | pacbio |
| *Amblyteles armatorius* | Ichneumonidae | Hymenoptera | Insecta | AACATCATCG | ACGGCAGCG | assembly |
| *Amblyteles armatorius* | Ichneumonidae | Hymenoptera | Insecta | ACGACG | ATCATC | pacbio |
| *Apechthis compunctor* | Ichneumonidae | Hymenoptera | Insecta | ACAGAG | ACAGAGAG | pacbio |
| *Buathra laborator* | Ichneumonidae | Hymenoptera | Insecta | AATGAATG | AATGAATGAATG | assembly |
| *Buathra laborator* | Ichneumonidae | Hymenoptera | Insecta |  |  | pacbio |
| *Campoletis raptor* | Ichneumonidae | Hymenoptera | Insecta | AAACAAACCC | ACTGACTG | pacbio |
| *Clistopyga incitator* | Ichneumonidae | Hymenoptera | Insecta | AAAGAACCT | AAAGAACCTAAAGAACCT | assembly |
| *Clistopyga incitator* | Ichneumonidae | Hymenoptera | Insecta | ACGATG | AAGTACTTGATGGGTACC | pacbio |
| *Cylloceria caligata* | Ichneumonidae | Hymenoptera | Insecta | ACATACAT | ACATACATACAT | pacbio |
| *Dyspetes luteomarginatus* | Ichneumonidae | Hymenoptera | Insecta | ACAGAGAG | ACCAG | pacbio |
| *Ephialtes manifestator* | Ichneumonidae | Hymenoptera | Insecta |  |  | pacbio |
| *Exephanes ischioxanthus* | Ichneumonidae | Hymenoptera | Insecta | ACACGC | AAAAGCCTTT | pacbio |
| *Heteropelma amictum* | Ichneumonidae | Hymenoptera | Insecta | AACGAACG | ACGACGATG | pacbio |
| *Ichneumon xanthorius* | Ichneumonidae | Hymenoptera | Insecta | ACGATG | AACGAC | assembly |
| *Ichneumon xanthorius* | Ichneumonidae | Hymenoptera | Insecta | AACGAC | ACGATG | pacbio |
| *Netelia dilatata* | Ichneumonidae | Hymenoptera | Insecta | AAAATAAAT | AAAAT | assembly |
| *Netelia dilatata* | Ichneumonidae | Hymenoptera | Insecta | AAAAT | AAAATAAAT | pacbio |
| *Netelia thomsonii* | Ichneumonidae | Hymenoptera | Insecta |  |  | pacbio |
| *Ophion crassicornis* | Ichneumonidae | Hymenoptera | Insecta | AATGG | ATCCATCC | pacbio |
| *Ophion ellenae* | Ichneumonidae | Hymenoptera | Insecta | ATCCATCC | AATGG | pacbio |
| *Ophion luteus* | Ichneumonidae | Hymenoptera | Insecta | ATCCATCC | AAACAAACCC | assembly |
| *Ophion luteus* | Ichneumonidae | Hymenoptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Polysphincta tuberosa* | Ichneumonidae | Hymenoptera | Insecta | AAACAC | ACACAG | pacbio |
| *Rhimphoctona megacephalus* | Ichneumonidae | Hymenoptera | Insecta | AACGAACG | AACGAACGAACG | pacbio |
| *Rhorus exstirpatorius* | Ichneumonidae | Hymenoptera | Insecta | AACGAACG | ACGATG | pacbio |
| *Scambus nigricans* | Ichneumonidae | Hymenoptera | Insecta | ACACAC | ACACAG | pacbio |
| *Sussaba pulchella* | Ichneumonidae | Hymenoptera | Insecta | AATCATC | AAGTGT | pacbio |
| *Venturia canescens* | Ichneumonidae | Hymenoptera | Insecta | AAATTC | AAATTCAAATTC | pacbio |
| *Coelioxys conoideus* | Megachilidae | Hymenoptera | Insecta | ACAGAG | ACAGACAG | pacbio |
| *Megachile leachella* | Megachilidae | Hymenoptera | Insecta | ACAGAG | AACCT | pacbio |
| *Megachile ligniseca* | Megachilidae | Hymenoptera | Insecta | ACAGAG | ACAGAGACAGAG | assembly |
| *Megachile ligniseca* | Megachilidae | Hymenoptera | Insecta | ACAGAG | AACCT | pacbio |
| *Megachile willughbiella* | Megachilidae | Hymenoptera | Insecta | ACAGAG | ACAGAGACAGAG | assembly |
| *Megachile willughbiella* | Megachilidae | Hymenoptera | Insecta | ACAGAG | AACCT | pacbio |
| *Stelis phaeoptera* | Megachilidae | Hymenoptera | Insecta | AAAGGC | AACCCT | assembly |
| *Stelis phaeoptera* | Megachilidae | Hymenoptera | Insecta | AAAGGC | AACCCT | pacbio |
| *Macropis europaea* | Melittidae | Hymenoptera | Insecta | AACCC |  | assembly |
| *Macropis europaea* | Melittidae | Hymenoptera | Insecta |  |  | pacbio |
| *Melitta haemorrhoidalis* | Melittidae | Hymenoptera | Insecta | AACCCAGACCT | AACCCAGACCTAACCCAGACCT | pacbio |
| *Anoplius nigerrimus* | Pompilidae | Hymenoptera | Insecta | AACCCAGACCT | AAAAA | assembly |
| *Anoplius nigerrimus* | Pompilidae | Hymenoptera | Insecta |  |  | pacbio |
| *Arachnospila anceps* | Pompilidae | Hymenoptera | Insecta | AACCCAGACCT | AACCCAGACCTAACCCAGACCT | pacbio |
| *Evagetes crassicornis* | Pompilidae | Hymenoptera | Insecta | AACCCAGACCT |  | pacbio |
| *Priocnemis perturbator* | Pompilidae | Hymenoptera | Insecta | AAGCACAGGCAGC | ACAGGCAGC | pacbio |
| *Gastracanthus pulcherrimus* | Pteromalidae | Hymenoptera | Insecta | AAAGATG | ACAGACAG | pacbio |
| *Ammophila pubescens* | Sphecidae | Hymenoptera | Insecta | AACTCACT | ACAGAG | pacbio |
| *Ammophila sabulosa* | Sphecidae | Hymenoptera | Insecta | AAGTC | ACTGG | pacbio |
| *Macrophya alboannulata* | Tenthredinidae | Hymenoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Macrophya annulata* | Tenthredinidae | Hymenoptera | Insecta | ACCTACCT | ACCCT | pacbio |
| *Macrophya punctumalbum* | Tenthredinidae | Hymenoptera | Insecta | ACCTG | AACCT | pacbio |
| *Phymatocera aterrima* | Tenthredinidae | Hymenoptera | Insecta | AACCT | AAGGG | pacbio |
| *Rhogogaster chlorosoma* | Tenthredinidae | Hymenoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Rhogogaster chlorosoma* | Tenthredinidae | Hymenoptera | Insecta | AACCT | AACGAC | pacbio |
| *Tenthredo distinguenda* | Tenthredinidae | Hymenoptera | Insecta | ACTCTG | AACCT | assembly |
| *Tenthredo distinguenda* | Tenthredinidae | Hymenoptera | Insecta | ACTCTG | ACTCTGACTCTG | pacbio |
| *Tenthredo livida* | Tenthredinidae | Hymenoptera | Insecta | AACCT |  | pacbio |
| *Tenthredo mesomela* | Tenthredinidae | Hymenoptera | Insecta | AGGGATATC | AGGGATATCAGGGATATC | assembly |
| *Tenthredo mesomela* | Tenthredinidae | Hymenoptera | Insecta | AGGGATATC | AATGCAG | pacbio |
| *Tenthredo notha* | Tenthredinidae | Hymenoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Tenthredo notha* | Tenthredinidae | Hymenoptera | Insecta |  |  | pacbio |
| *Tiphia femorata* | Tiphiidae | Hymenoptera | Insecta | AAAAGCT | AACCCT | assembly |
| *Tiphia femorata* | Tiphiidae | Hymenoptera | Insecta | AGAGAT |  | pacbio |
| *Ancistrocerus nigricornis* | Vespidae | Hymenoptera | Insecta | AACCCAGACCC | AACCCAGACCCAACCCAGACCC | assembly |
| *Ancistrocerus nigricornis* | Vespidae | Hymenoptera | Insecta |  |  | pacbio |
| *Dolichovespula media* | Vespidae | Hymenoptera | Insecta | AACCCAGACGC | AACGACGATATT | assembly |
| *Dolichovespula media* | Vespidae | Hymenoptera | Insecta | AACCCAGACGC | ACAGT | pacbio |
| *Dolichovespula norwegica* | Vespidae | Hymenoptera | Insecta | AACCCAGACGC | AACCCAGACGCAACCCAGACGC | pacbio |
| *Dolichovespula saxonica* | Vespidae | Hymenoptera | Insecta | AACCCAGACGC | AACAGT | assembly |
| *Dolichovespula saxonica* | Vespidae | Hymenoptera | Insecta | AACCCAGACGC |  | pacbio |
| *Dolichovespula sylvestris* | Vespidae | Hymenoptera | Insecta | AACCCAGACGC | AACCCAGACGCAACCCAGACGC | assembly |
| *Dolichovespula sylvestris* | Vespidae | Hymenoptera | Insecta | AACCCAGACGC |  | pacbio |
| *Vespa crabro* | Vespidae | Hymenoptera | Insecta | AATAAT | AACCCTGACGC | assembly |
| *Vespa crabro* | Vespidae | Hymenoptera | Insecta |  |  | pacbio |
| *Vespa velutina* | Vespidae | Hymenoptera | Insecta | AACCCTGACGC | AACCCTGACGCAACCCTGACGC | assembly |
| *Vespula germanica* | Vespidae | Hymenoptera | Insecta | AACCCAGACGC |  | assembly |
| *Vespula germanica* | Vespidae | Hymenoptera | Insecta | AACCCAGACGC |  | pacbio |
| *Vespula vulgaris* | Vespidae | Hymenoptera | Insecta | AACCCAGACGC |  | assembly |
| *Vespula vulgaris* | Vespidae | Hymenoptera | Insecta | AACCCAGACGC |  | pacbio |
| *Nematopogon swammerdamellus* | Adelidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Nematopogon swammerdamellus* | Adelidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Nemophora metallica* | Adelidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Argyresthia goedartella* | Argyresthiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Batrachedra praeangusta* | Batrachedridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Blastobasis adustella* | Blastobasidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Blastobasis adustella* | Blastobasidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Blastobasis lacticolella* | Blastobasidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Blastobasis lacticolella* | Blastobasidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Anthophila fabriciana* | Choreutidae | Lepidoptera | Insecta |  |  | pacbio |
| *Coleophora flavipennella* | Coleophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Coleophora flavipennella* | Coleophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Zeuzera pyrina* | Cossidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Zeuzera pyrina* | Cossidae | Lepidoptera | Insecta | AACCT | AACAAC | pacbio |
| *Acentria ephemerella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Acentria ephemerella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agriphila geniculea* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agriphila geniculea* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agriphila straminella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agriphila tristella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agriphila tristella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Anania crocealis* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Calamotropha paludella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Calamotropha paludella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Catoptria pinella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Chrysoteuchia culmella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Chrysoteuchia culmella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Crambus lathoniellus* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cydalima perspectalis* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Elophila nymphaeata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eudonia lacustrata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eudonia lacustrata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Evergestis limbata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mecyna flavalis* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Nymphula nitidulata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Nymphula nitidulata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ostrinia nubilalis* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Parapoynx stratiotata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Parapoynx stratiotata* | Crambidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Patania ruralis* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pyrausta purpuralis* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Udea olivalis* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Udea olivalis* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Udea prunalis* | Crambidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Agonopterix arenella* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agonopterix arenella* | Depressariidae | Lepidoptera | Insecta | AACCT | AGGAT | pacbio |
| *Agonopterix heracliana* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agonopterix ocellana* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agonopterix subpropinquella* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agonopterix subpropinquella* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Carcina quercana* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Carcina quercana* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Depressaria radiella* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Achlya flavicornis* | Drepanidae | Lepidoptera | Insecta | AACCT | AAATG | pacbio |
| *Drepana falcataria* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Drepana falcataria* | Drepanidae | Lepidoptera | Insecta |  |  | pacbio |
| *Habrosyne pyritoides* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Habrosyne pyritoides* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thyatira batis* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Thyatira batis* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Watsonalla binaria* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Watsonalla binaria* | Drepanidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Watsonalla cultraria* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Elachista subocellea* | Elachistidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Atolmis rubricollis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Catocala fraxini* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Catocala fraxini* | Erebidae | Lepidoptera | Insecta |  |  | pacbio |
| *Cybosia mesomella* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Cybosia mesomella* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Diaphora mendica* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eilema caniola* | Erebidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Eilema depressum* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eilema depressum* | Erebidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Eilema griseolum* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Euclidia mi* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Euclidia mi* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Euproctis similis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Euproctis similis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Herminia grisealis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Herminia tarsipennalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Herminia tarsipennalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hypena proboscidalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hypena proboscidalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Laspeyria flexula* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Laspeyria flexula* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Leucoma salicis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lygephila pastinum* | Erebidae | Lepidoptera | Insecta | AACCATCCCT | AACCATCCCTAACCATCCCT | pacbio |
| *Lymantria monacha* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lymantria monacha* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Macrochilo cribrumalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Miltochrista miniata* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Miltochrista miniata* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Orgyia antiqua* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Orgyia antiqua* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Phragmatobia fuliginosa* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Phragmatobia fuliginosa* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Schrankia costaestrigalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Schrankia costaestrigalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Scoliopteryx libatrix* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Spilarctia lutea* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Spilarctia lutea* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Spilosoma lubricipeda* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Spilosoma lubricipeda* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thumatha senex* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Tyria jacobaeae* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Tyria jacobaeae* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Anarsia innoxiella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Anarsia innoxiella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Aproaerema taeniolella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Athrips mouffetella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Athrips mouffetella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AAATG | pacbio |
| *Brachmia blandella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Carpatolechia fugitivella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Monochroa cytisella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Psoricoptera gibbosella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Recurvaria leucatella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Teleiodes luculella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acasis viretata* | Geometridae | Lepidoptera | Insecta | ACACCT | AACCT | pacbio |
| *Agriopis aurantiaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agriopis aurantiaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agriopis marginaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agriopis marginaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Alcis repandata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Alsophila aescularia* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Alsophila aescularia* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Anticlea derivata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Anticlea derivata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apeira syringaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Apeira syringaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Aplocera efformata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Aplocera efformata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apocheima hispidaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Apocheima hispidaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Biston betularia* | Geometridae | Lepidoptera | Insecta | AACCT | ACCTACCT | assembly |
| *Biston betularia* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Campaea margaritaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Campaea margaritaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Camptogramma bilineatum* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Chesias legatella* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Chesias legatella* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Chloroclysta siterata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Chloroclysta siterata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Chloroclystis v-ata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Colostygia pectinataria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Colotois pennaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Crocallis elinguaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Crocallis elinguaria* | Geometridae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Dysstroma truncata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ecliptopera silaceata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ecliptopera silaceata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ectropis crepuscularia* | Geometridae | Lepidoptera | Insecta |  |  | pacbio |
| *Electrophaes corylata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Electrophaes corylata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ennomos erosarius* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ennomos fuscantarius* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ennomos fuscantarius* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ennomos quercinarius* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ennomos quercinarius* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Epirrhoe alternata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Erannis defoliaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Erannis defoliaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eulithis prunata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eulithis prunata* | Geometridae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Eulithis testata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eulithis testata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eupithecia abbreviata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eupithecia abbreviata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eupithecia centaureata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eupithecia centaureata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eupithecia dodoneata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eupithecia dodoneata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eupithecia exiguata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eupithecia exiguata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eupithecia insigniata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eupithecia insigniata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eupithecia tripunctaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eupithecia vulgata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eupithecia vulgata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Gandaritis pyraliata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Gandaritis pyraliata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Gymnoscelis rufifasciata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Gymnoscelis rufifasciata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hemistola chrysoprasaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hemithea aestivaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hemithea aestivaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Horisme vitalbata* | Geometridae | Lepidoptera | Insecta | AACCT | ATCCC | pacbio |
| *Hydriomena furcata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hydriomena furcata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hylaea fasciaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hylaea fasciaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hypomecis punctinalis* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Idaea aversata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Idaea aversata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Idaea dimidiata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lampropteryx suffumata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ligdia adustata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ligdia adustata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lobophora halterata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lobophora halterata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lomaspilis marginata* | Geometridae | Lepidoptera | Insecta | AACGTGAT | AATAGAT | pacbio |
| *Lomographa bimaculata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lycia hirtaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lycia hirtaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Macaria notata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Macaria notata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Odontopera bidentata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Operophtera brumata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Operophtera brumata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Operophtera fagata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Opisthograptis luteolata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Opisthograptis luteolata* | Geometridae | Lepidoptera | Insecta | AACCT | AAATAG | pacbio |
| *Parectropis similaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Peribatodes rhomboidaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Peribatodes rhomboidaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Perizoma alchemillatum* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Perizoma flavofasciatum* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Philereme vetulata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Philereme vetulata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Plemyria rubiginata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Scopula imitaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Scotopteryx chenopodiata* | Geometridae | Lepidoptera | Insecta | ACTCTG | AACCT | pacbio |
| *Selenia dentaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Selenia dentaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Selenia tetralunaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thera britannica* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Thera britannica* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thera juniperata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thera obeliscata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Thera obeliscata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Theria primaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xanthorhoe fluctuata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xanthorhoe quadrifasciata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xanthorhoe spadicearia* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Xanthorhoe spadicearia* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Euspilapteryx auroguttella* | Gracillariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Parectopa ononidis* | Gracillariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Parornix anglicella* | Gracillariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Phyllonorycter quercifoliella* | Gracillariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hepialus humuli* | Hepialidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Korscheltellus lupulinus* | Hepialidae | Lepidoptera | Insecta | AACCT | AACCG | pacbio |
| *Triodia sylvina* | Hepialidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Carterocephalus palaemon* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Carterocephalus palaemon* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Erynnis tages* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Erynnis tages* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hesperia comma* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hesperia comma* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ochlodes sylvanus* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ochlodes sylvanus* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pyrgus malvae* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pyrgus malvae* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thymelicus acteon* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thymelicus lineola* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thymelicus sylvestris* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Thymelicus sylvestris* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Incurvaria masculella* | Incurvariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Incurvaria masculella* | Incurvariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Poecilocampa populi* | Lasiocampidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apoda limacodes* | Limacodidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Apoda limacodes* | Limacodidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Aricia agestis* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Aricia agestis* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Aricia artaxerxes* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Aricia artaxerxes* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Callophrys rubi* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Celastrina argiolus* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Celastrina argiolus* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cupido minimus* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cyaniris semiargus* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Cyaniris semiargus* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Glaucopsyche alexis* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Glaucopsyche alexis* | Lycaenidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Lycaena phlaeas* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lycaena phlaeas* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lysandra bellargus* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lysandra bellargus* | Lycaenidae | Lepidoptera | Insecta | ACATC | AACCT | pacbio |
| *Lysandra coridon* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lysandra coridon* | Lycaenidae | Lepidoptera | Insecta | AACCT | ACATC | pacbio |
| *Plebejus argus* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Plebejus argus* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Polyommatus icarus* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Polyommatus icarus* | Lycaenidae | Lepidoptera | Insecta | AACTCG | AACCT | pacbio |
| *Satyrium w-album* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thecla betulae* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Micropterix aruncella* | Micropterigidae | Lepidoptera | Insecta | AAGACGGTAAGTGTGTATGTATGT | AACCT | assembly |
| *Micropterix aruncella* | Micropterigidae | Lepidoptera | Insecta | AAGACGGTAAGTGTGTATGTATGT | AACCT | pacbio |
| *Mompha ochraceella* | Momphidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Abrostola tripartita* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Abrostola tripartita* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Abrostola triplasia* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Abrostola triplasia* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acronicta aceris* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Acronicta aceris* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acronicta alni* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acronicta leporina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Acronicta leporina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acronicta psi* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Acronicta psi* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acronicta rumicis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agrochola circellaris* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agrochola circellaris* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Agrochola litura* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agrochola lota* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agrochola lota* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agrochola macilenta* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agrochola macilenta* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agrotis puta* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agrotis puta* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Allophyes oxyacanthae* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Allophyes oxyacanthae* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Amphipoea lucens* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Amphipoea lucens* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Amphipoea oculea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Amphipoea oculea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Amphipyra berbera* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Amphipyra berbera* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Amphipyra tragopoginis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Amphipyra tragopoginis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Anaplectoides prasina* | Noctuidae | Lepidoptera | Insecta | AACCT | AAAAGTC | pacbio |
| *Anorthoa munda* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Anorthoa munda* | Noctuidae | Lepidoptera | Insecta | AACCT | ACCCTACCT | pacbio |
| *Antitype chi* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Antitype chi* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apamea anceps* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apamea crenata* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apamea epomidion* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Apamea epomidion* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apamea monoglypha* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Apamea monoglypha* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Apamea scolopacina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apamea sordens* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Apamea sordens* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Aporophyla lueneburgensis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Aporophyla lueneburgensis* | Noctuidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Aporophyla nigra* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Aporophyla nigra* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Arenostola phragmitidis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Asteroscopus sphinx* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Atethmia centrago* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Atethmia centrago* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Autographa gamma* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Autographa gamma* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Autographa pulchrina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Autographa pulchrina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Axylia putris* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Brachylomia viminalis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Brachylomia viminalis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Caradrina clavipalpis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Caradrina clavipalpis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Caradrina kadenii* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Caradrina kadenii* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Charanyca ferruginea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Charanyca ferruginea* | Noctuidae | Lepidoptera | Insecta | AACCT | ACACCTACCCT | pacbio |
| *Charanyca trigrammica* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Colocasia coryli* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Conistra vaccinii* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cosmia pyralina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Cosmia pyralina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cosmia trapezina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Cosmia trapezina* | Noctuidae | Lepidoptera | Insecta |  |  | pacbio |
| *Craniophora ligustri* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Craniophora ligustri* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Diachrysia chrysitis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Diachrysia chrysitis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Diarsia dahlii* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Diarsia mendica* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Diarsia rubi* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Diarsia rubi* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Dicycla oo* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Diloba caeruleocephala* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Diloba caeruleocephala* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Dryobota labecula* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Dryobotodes eremita* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Dryobotodes eremita* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eremobia ochroleuca* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eugnorisma glareosa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eugnorisma glareosa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Euplexia lucipara* | Noctuidae | Lepidoptera | Insecta | AACCT | AAATG | assembly |
| *Euplexia lucipara* | Noctuidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Eupsilia transversa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eupsilia transversa* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Fissipunctia ypsillon* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Fissipunctia ypsillon* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Globia sparganii* | Noctuidae | Lepidoptera | Insecta |  |  | pacbio |
| *Griposia aprilina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Griposia aprilina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hecatera dysodea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hecatera dysodea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hoplodrina blanda* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hoplodrina octogenaria* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hydraecia micacea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hydraecia micacea* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Lacanobia wlatinum* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lacanobia wlatinum* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lithophane ornitopus* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lithophane semibrunnea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lithophane semibrunnea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lithophane socia* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lithophane socia* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Luperina testacea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Luperina testacea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mamestra brassicae* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mamestra brassicae* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Melanchra persicariae* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Melanchra persicariae* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mesoligia furuncula* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mesoligia furuncula* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mythimna albipuncta* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mythimna albipuncta* | Noctuidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Mythimna ferrago* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mythimna ferrago* | Noctuidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Mythimna impura* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mythimna impura* | Noctuidae | Lepidoptera | Insecta | AACCT | ACCTACCT | pacbio |
| *Mythimna lalbum* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mythimna vitellina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Noctua comes* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Noctua fimbriata* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Noctua fimbriata* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Noctua janthe* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Noctua janthe* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Noctua pronuba* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Noctua pronuba* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Ochropleura plecta* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ochropleura plecta* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Oligia latruncula* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Oligia strigilis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Omphaloscelis lunosa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Omphaloscelis lunosa* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Orthosia cerasi* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Orthosia gothica* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Orthosia gracilis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Orthosia gracilis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Orthosia incerta* | Noctuidae | Lepidoptera | Insecta | ACACCTACCCT | AACCT | pacbio |
| *Phlogophora meticulosa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Phlogophora meticulosa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Photedes minima* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Polymixis flavicincta* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Polymixis lichenea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Protodeltote pygarga* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Protodeltote pygarga* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Shargacucullia verbasci* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Shargacucullia verbasci* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Subacronicta megacephala* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thalpophila matura* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Tholera decimalis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Tholera decimalis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Tiliacea aurago* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Tiliacea aurago* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Trisateles emortualis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Trisateles emortualis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xanthia icteritia* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xestia agathina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xestia c-nigrum* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Xestia c-nigrum* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Xestia sexstrigata* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Xestia sexstrigata* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xestia triangulum* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xestia xanthographa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Xestia xanthographa* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Xylocampa areola* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Xylocampa areola* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Bena bicolorana* | Nolidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Meganola albula* | Nolidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Meganola albula* | Nolidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Nola cucullatella* | Nolidae | Lepidoptera | Insecta | AACCT | ACACAC | pacbio |
| *Nycteola revayana* | Nolidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Nycteola revayana* | Nolidae | Lepidoptera | Insecta | AAACCACCCT | AAACCACCCTAAACCACCCT | pacbio |
| *Pseudoips prasinana* | Nolidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Clostera curtula* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Clostera curtula* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Drymonia ruficornis* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Drymonia ruficornis* | Notodontidae | Lepidoptera | Insecta | ACAGAG | AACCT | pacbio |
| *Furcula furcula* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Furcula furcula* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Notodonta dromedarius* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Notodonta dromedarius* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Notodonta ziczac* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Notodonta ziczac* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Phalera bucephala* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Phalera bucephala* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pheosia gnoma* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pheosia gnoma* | Notodontidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Pheosia tremula* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pheosia tremula* | Notodontidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Ptilodon capucinus* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ptilodon capucinus* | Notodontidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Apatura iris* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Argynnis aglaja* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Bicyclus anynana* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Boloria selene* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Boloria selene* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Coenonympha tullia* | Nymphalidae | Lepidoptera | Insecta | AACCT | ACTCAG | pacbio |
| *Erebia aethiops* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Erebia aethiops* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Erebia epiphron* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Erebia ligea* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACTACCT | assembly |
| *Erebia ligea* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Euphydryas aurinia* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Fabriciana adippe* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Fabriciana adippe* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hipparchia semele* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hipparchia semele* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lasiommata megera* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lasiommata megera* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Limenitis camilla* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Limenitis camilla* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Maniola jurtina* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Maniola jurtina* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Melanargia galathea* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Melanargia galathea* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Melitaea cinxia* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Melitaea cinxia* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mellicta athalia* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mellicta athalia* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Nymphalis c-album* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Nymphalis polychloros* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Nymphalis polychloros* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Nymphalis urticae* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Nymphalis urticae* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pararge aegeria* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pararge aegeria* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Vanessa atalanta* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Vanessa atalanta* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Vanessa cardui* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Vanessa cardui* | Nymphalidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Crassa unitella* | Oecophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Esperia sulphurella* | Oecophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Esperia sulphurella* | Oecophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hofmannophila pseudospretella* | Oecophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hofmannophila pseudospretella* | Oecophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Papilio machaon* | Papilionidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Anthocharis cardamines* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Anthocharis cardamines* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Aporia crataegi* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Aporia crataegi* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Colias croceus* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Colias croceus* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Leptidea sinapis* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Leptidea sinapis* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pieris brassicae* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pieris brassicae* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pieris napi* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pieris napi* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pieris rapae* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pieris rapae* | Pieridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Plutella xylostella* | Plutellidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Prays ruficeps* | Praydidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Emmelina monodactyla* | Pterophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Emmelina monodactyla* | Pterophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Marasmarcha lunaedactyla* | Pterophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Marasmarcha lunaedactyla* | Pterophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Stenoptilia bipunctidactyla* | Pterophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Stenoptilia bipunctidactyla* | Pterophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acrobasis advenella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acrobasis consociella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acrobasis repandana* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acrobasis suavella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Acrobasis suavella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Aglossa pinguinalis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apomyelois bistriatella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Apomyelois bistriatella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Elegia similella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Elegia similella* | Pyralidae | Lepidoptera | Insecta |  |  | pacbio |
| *Endotricha flammealis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Endotricha flammealis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Euzophera pinguis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Euzophera pinguis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hypsopygia costalis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hypsopygia costalis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hypsopygia glaucinalis* | Pyralidae | Lepidoptera | Insecta | AACCT | AAATG | pacbio |
| *Myelois circumvoluta* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Phycita roborella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Plodia interpunctella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pyralis farinalis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pyralis farinalis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Sciota angustella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hamearis lucina* | Riodinidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Saturnia pavonia* | Saturniidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Saturnia pavonia* | Saturniidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Bembecia ichneumoniformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Bembecia ichneumoniformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Sesia apiformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Sesia apiformis* | Sesiidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Sesia bembeciformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Sesia bembeciformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Synanthedon andrenaeformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Synanthedon andrenaeformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Synanthedon formicaeformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Synanthedon formicaeformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Synanthedon myopaeformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Synanthedon myopaeformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Synanthedon tipuliformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Synanthedon vespiformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Synanthedon vespiformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Deilephila elpenor* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Deilephila porcellus* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Deilephila porcellus* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hemaris fuciformis* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hemaris fuciformis* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Laothoe populi* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Laothoe populi* | Sphingidae | Lepidoptera | Insecta | ACAGACAG | AACCT | pacbio |
| *Mimas tiliae* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mimas tiliae* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Sphinx ligustri* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Sphinx pinastri* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Sphinx pinastri* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Monopis laevigella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Monopis laevigella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Morophaga choragella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Tinea pellionella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Tinea semifulvella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Tinea semifulvella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Tinea trinotella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Tinea trinotella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris cristana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris emargana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Acleris emargana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris ferrugana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris holmiana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris kochiella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris literana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Acleris literana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris rhombana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris sparsana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Acleris sparsana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apotomis betuletana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Apotomis betuletana* | Tortricidae | Lepidoptera | Insecta | AACCT | ACAGGC | pacbio |
| *Apotomis capreana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apotomis turbidana* | Tortricidae | Lepidoptera | Insecta | AACCT | ACTGATAGAT | assembly |
| *Apotomis turbidana* | Tortricidae | Lepidoptera | Insecta | AACCT | AGATAGAT | pacbio |
| *Archips crataeganus* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Archips crataeganus* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Archips podanus* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Archips xylosteana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Archips xylosteana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Clepsis spectrana* | Tortricidae | Lepidoptera | Insecta |  |  | pacbio |
| *Cochylimorpha straminea* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cydia amplana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cydia fagiglandana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cydia splendana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Cydia splendana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cydia strobilella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Cydia strobilella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ditula angustiorana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Enarmonia formosana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Epagoge grotiana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Epinotia bilunana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Epinotia bilunana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Epinotia brunnichana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Epinotia demarniana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Epinotia demarniana* | Tortricidae | Lepidoptera | Insecta |  |  | pacbio |
| *Epinotia nisella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Epinotia nisella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Epinotia ramella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Epinotia ramella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eucosma campoliliana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eucosma cana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eudemis profundana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eudemis profundana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hedya salicella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hedya salicella* | Tortricidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Lozotaeniodes formosana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Neocochylis molliculana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Notocelia uddmanniana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Notocelia uddmanniana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pammene aurita* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pammene aurita* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pammene fasciana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pammene fasciana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pammene regiana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pandemis cinnamomeana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pandemis cinnamomeana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pandemis corylana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ptycholomoides aeriferana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Rhopobota naevana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Tortricodes alternella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Tortricodes alternella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Zeiraphera isertana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Paraswammerdamia nebulella* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Yponomeuta cagnagella* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Yponomeuta cagnagella* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Yponomeuta padella* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Yponomeuta padella* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Yponomeuta plumbellus* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Yponomeuta plumbellus* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Yponomeuta rorrellus* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Yponomeuta rorrellus* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Yponomeuta sedellus* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Yponomeuta sedellus* | Yponomeutidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Zelleria hepariella* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ypsolopha alpella* | Ypsolophidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ypsolopha parenthesella* | Ypsolophidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ypsolopha scabrella* | Ypsolophidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ypsolopha scabrella* | Ypsolophidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ypsolopha sequella* | Ypsolophidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ypsolopha sequella* | Ypsolophidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Zygaena filipendulae* | Zygaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Zygaena filipendulae* | Zygaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Boreus hyemalis* | Boreidae | Mecoptera | Insecta | AAAGGT | ACAGACAG | pacbio |
| *Panorpa germanica* | Panorpidae | Mecoptera | Insecta | AAGAATAT | AAGAATATAAGAATAT | pacbio |
| *Sialis lutaria* | Sialidae | Megaloptera | Insecta | AACCT |  | pacbio |
| *Chrysoperla carnea* | Chrysopidae | Neuroptera | Insecta | AACCC | AACCCAACCC | assembly |
| *Chrysoperla carnea* | Chrysopidae | Neuroptera | Insecta | AACCC |  | pacbio |
| *Chrysoperla lucasina* | Chrysopidae | Neuroptera | Insecta | AACCC | AACCCAACCC | pacbio |
| *Drepanepteryx phalaenoides* | Hemerobiidae | Neuroptera | Insecta | AACCTAACCT | AACCT | pacbio |
| *Sisyra nigra* | Sisyridae | Neuroptera | Insecta |  |  | pacbio |
| *Aeshna juncea* | Aeshnidae | Odonata | Insecta | AACCC | AACTGACT | pacbio |
| *Aeshna mixta* | Aeshnidae | Odonata | Insecta | ATATAT | ATATATAT | pacbio |
| *Coenagrion puella* | Coenagrionidae | Odonata | Insecta | AGCCATCGCCAT | AGCCATCGCCATAGCCATCGCCAT | pacbio |
| *Enallagma cyathigerum* | Coenagrionidae | Odonata | Insecta | ACACAC | ACACACAC | pacbio |
| *Ischnura elegans* | Coenagrionidae | Odonata | Insecta | AGATC |  | assembly |
| *Ischnura elegans* | Coenagrionidae | Odonata | Insecta | AACCC |  | pacbio |
| *Somatochlora arctica* | Corduliidae | Odonata | Insecta | AACTCACAACTCAG | AACCC | pacbio |
| *Somatochlora metallica* | Corduliidae | Odonata | Insecta | AAAATAACAC | AACTGTCTCACC | pacbio |
| *Chalcolestes viridis* | Lestidae | Odonata | Insecta | AACCC | ACACAC | pacbio |
| *Libellula quadrimaculata* | Libellulidae | Odonata | Insecta | ACACAC | AACAG | pacbio |
| *Orthetrum cancellatum* | Libellulidae | Odonata | Insecta | AACCT | AACCTAACCT | pacbio |
| *Sympetrum sanguineum* | Libellulidae | Odonata | Insecta | AACCC | AACCCAACCC | pacbio |
| *Sympetrum striolatum* | Libellulidae | Odonata | Insecta | AACCC | AAAATTTG | assembly |
| *Sympetrum striolatum* | Libellulidae | Odonata | Insecta | ACACAC | ACTCACTC | pacbio |
| *Platycnemis pennipes* | Platycnemididae | Odonata | Insecta | AACCC | AACCCAACCC | assembly |
| *Platycnemis pennipes* | Platycnemididae | Odonata | Insecta |  |  | pacbio |
| *Chorthippus albomarginatus* | Acrididae | Orthoptera | Insecta | AACCT | AACTTG | pacbio |
| *Chorthippus brunneus* | Acrididae | Orthoptera | Insecta | AACCT | ACACAG | pacbio |
| *Chorthippus parallelus* | Acrididae | Orthoptera | Insecta | AACCT |  | pacbio |
| *Gomphocerippus rufus* | Acrididae | Orthoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Stenobothrus lineatus* | Acrididae | Orthoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Teleogryllus oceanicus* | Gryllidae | Orthoptera | Insecta | AACCT | ACTACT | pacbio |
| *Tetrix subulata* | Tetrigidae | Orthoptera | Insecta | AACCT | ACTCTGC | pacbio |
| *Leptophyes punctatissima* | Tettigoniidae | Orthoptera | Insecta | AAGTAAGT | AAGTAAGTAAGT | pacbio |
| *Meconema thalassinum* | Tettigoniidae | Orthoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Meconema thalassinum* | Tettigoniidae | Orthoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Chloroperla tripunctata* | Chloroperlidae | Plecoptera | Insecta | ACTACT | AGATAGAT | pacbio |
| *Leuctra nigra* | Leuctridae | Plecoptera | Insecta | AAGCGAGCG | AACAATT | assembly |
| *Leuctra nigra* | Leuctridae | Plecoptera | Insecta | AACCT |  | pacbio |
| *Nemoura dubitans* | Nemouridae | Plecoptera | Insecta | ATCATC | ATCATCATC | assembly |
| *Nemoura dubitans* | Nemouridae | Plecoptera | Insecta | AACCT | AGAGC | pacbio |
| *Nemurella pictetii* | Nemouridae | Plecoptera | Insecta | AGCAGC | AACCT | assembly |
| *Nemurella pictetii* | Nemouridae | Plecoptera | Insecta | AACCT | AAGTAG | pacbio |
| *Protonemura montana* | Nemouridae | Plecoptera | Insecta | ACATGGGGCAGG | AACCT | assembly |
| *Protonemura montana* | Nemouridae | Plecoptera | Insecta | ACTAGC | AACCT | pacbio |
| *Perla bipunctata* | Perlidae | Plecoptera | Insecta | AAGTCG | ACTGCT | pacbio |
| *Isoperla grammatica* | Perlodidae | Plecoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Isoperla grammatica* | Perlodidae | Plecoptera | Insecta | AAATAAAT | AACCT | pacbio |
| *Brachyptera putata* | Taeniopterygidae | Plecoptera | Insecta | ATATAT | ATATATATAT | assembly |
| *Brachyptera risi* | Taeniopterygidae | Plecoptera | Insecta | ATATAT | ATATATAT | pacbio |
| *Mesopsocus fuscifrons* | Mesopsocidae | Psocoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xanthostigma xanthostigma* | Raphidiidae | Raphidioptera | Insecta | AAGACAGT | AAGACAGTAAGACAGT | pacbio |
| *Stylops melittae* | Stylopidae | Strepsiptera | Insecta | ACCAGTG | AACCT | pacbio |
| *Agapetus fuscipes* | Glossosomatidae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Silo pallipes* | Goeridae | Trichoptera | Insecta | ATATAT | ATATATAT | pacbio |
| *Hydropsyche siltalai* | Hydropsychidae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Athripsodes cinereus* | Leptoceridae | Trichoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Athripsodes cinereus* | Leptoceridae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mystacides azureus* | Leptoceridae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Anabolia nervosa* | Limnephilidae | Trichoptera | Insecta | AATGACAGCG | ACTACT | pacbio |
| *Chaetopteryx villosa* | Limnephilidae | Trichoptera | Insecta |  |  | pacbio |
| *Glyphotaelius pellucidus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Glyphotaelius pellucidus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACTT | pacbio |
| *Limnephilus lunatus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Limnephilus lunatus* | Limnephilidae | Trichoptera | Insecta | AACCT |  | pacbio |
| *Limnephilus marmoratus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Limnephilus marmoratus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Limnephilus rhombicus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Limnephilus rhombicus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Stenophylax permistus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Odontocerum albicorne* | Odontoceridae | Trichoptera | Insecta | ATATAT | ATATATAT | pacbio |
| *Polycentropus irroratus* | Polycentropodidae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Sericostoma personatum* | Sericostomatidae | Trichoptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Chelura terebrans* | Cheluridae | Amphipoda | Malacostraca |  |  | pacbio |
| *Crangonyx pseudogracilis* | Crangonyctidae | Amphipoda | Malacostraca |  |  | pacbio |
| *Atelecyclus rotundatus* | Atelecyclidae | Decapoda | Malacostraca | AACCT | AACCTAACCT | pacbio |
| *Cancer pagurus* | Cancridae | Decapoda | Malacostraca | AACCT | ACAGACAG | pacbio |
| *Pagurus bernhardus* | Paguridae | Decapoda | Malacostraca | AACCT | AACCTAACCT | pacbio |
| *Pagurus pubescens* | Paguridae | Decapoda | Malacostraca | AACCT | AACCTAACCT | pacbio |
| *Liocarcinus pusillus* | Polybiidae | Decapoda | Malacostraca | AACCT | AACCTAACCT | pacbio |
| *Pisidia longicornis* | Porcellanidae | Decapoda | Malacostraca | AACCT | AACCTAACCT | pacbio |
| *Porcellana platycheles* | Porcellanidae | Decapoda | Malacostraca | AACCT | AAAGTTCCTCG | pacbio |
| *Xantho hydrophilus* | Xanthidae | Decapoda | Malacostraca | AACCT | ACACAC | pacbio |
| *Astacilla damnoniensis* | Arcturidae | Isopoda | Malacostraca | AGATAGAT | AACCCT | pacbio |
| *Asellus aquaticus* | Asellidae | Isopoda | Malacostraca |  |  | pacbio |
| *Idotea granulosa* | Idoteidae | Isopoda | Malacostraca | ATATAT | AGATAGATAT | pacbio |
| *Synisoma lancifer* | Idoteidae | Isopoda | Malacostraca | AGATAGAT | ACAGACAG | pacbio |
| *Oniscus asellus* | Oniscidae | Isopoda | Malacostraca | ATATAT | ATATATAT | pacbio |
| *Philoscia muscorum* | Philosciidae | Isopoda | Malacostraca |  |  | pacbio |
| *Platyarthrus hoffmannseggii* | Platyarthridae | Isopoda | Malacostraca |  |  | pacbio |
| *Porcellio spinicornis* | Porcellionidae | Isopoda | Malacostraca | AGGATG | ACTCTG | pacbio |
| *Clistosaccus paguri* | Clistosaccidae |  | Thecostraca | ACACAC | ACACACAC | pacbio |
| *Sacculina carcini* | Sacculinidae |  | Thecostraca | AACCT | AACCTAACCT | assembly |
| *Sacculina carcini* | Sacculinidae |  | Thecostraca | AAAATAAAG | ACACAC | pacbio |
| *Scalpellum scalpellum* | Scalpellidae |  | Thecostraca | AAGTCT | AAATACACATAACT | pacbio |
| *Perforatus perforatus* | Balanidae | Balanomorpha | Thecostraca | AACCT | AACCTAACCT | pacbio |
| *Semibalanus balanoides* | Balanidae | Balanomorpha | Thecostraca | AACCT | ACACAC | pacbio |
| *Epicoccum nigrum* | Didymellaceae | Pleosporales | Dothideomycetes |  |  | pacbio |
| *Paradendryphiella salina* | Pleosporaceae | Pleosporales | Dothideomycetes |  |  | pacbio |
| *Arachnomyces peruvianus* | Arachnomycetaceae | Onygenales | Eurotiomycetes | AACCCT |  | pacbio |
| *Cladonia squamosa* | Cladoniaceae | Lecanorales | Lecanoromycetes |  |  | pacbio |
| *Platismatia glauca* | Parmeliaceae | Lecanorales | Lecanoromycetes |  |  | pacbio |
| *Flavoplaca marina* | Teloschistaceae | Teloschistales | Lecanoromycetes |  |  | pacbio |
| *Metschnikowia zobellii* | Metschnikowiaceae | Saccharomycetales | Saccharomycetes |  |  | assembly |
| *Metschnikowia zobellii* | Metschnikowiaceae | Saccharomycetales | Saccharomycetes |  |  | pacbio |
| *Trichoderma pseudokoningii* | Hypocreaceae | Hypocreales | Sordariomycetes |  |  | assembly |
| *Trichoderma pseudokoningii* | Hypocreaceae | Hypocreales | Sordariomycetes | CCCCC | CCCCCC | pacbio |
| *Chaetoceros curvisetus* | Chaetocerotaceae | Chaetocerotales | Coscinodiscophyceae | ACCCT | ACCCTACCCT | pacbio |
| *Agaricus bisporus* | Agaricaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Agaricus bisporus* | Agaricaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Agaricus bisporus* | Agaricaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Agaricus bisporus* | Agaricaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Agaricus bisporus* | Agaricaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Clavaria fumosa* | Clavariaceae | Agaricales | Agaricomycetes | AACCCT | AACCCTAACCCT | pacbio |
| *Entoloma incanum* | Entolomataceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Inocybe grammopodia* | Inocybaceae | Agaricales | Agaricomycetes | AAGCATC | AACCCT | pacbio |
| *Inocybe tigrina* | Inocybaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Pseudosperma umbrinellum* | Inocybaceae | Agaricales | Agaricomycetes | AGAGAGAT | AACGAC | pacbio |
| *Leucocybe candicans* | Lyophyllaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Lyophyllum leucophaeatum* | Lyophyllaceae | Agaricales | Agaricomycetes | ACAGACAG | ACAGACAGACAG | pacbio |
| *Armillaria gallica* | Physalacriaceae | Agaricales | Agaricomycetes | AAACCCT | AACCCTG | pacbio |
| *Flammulina velutipes* | Physalacriaceae | Agaricales | Agaricomycetes | CCCCC |  | pacbio |
| *Flammulina velutipes* | Physalacriaceae | Agaricales | Agaricomycetes | CCCCC |  | pacbio |
| *Flammulina velutipes* | Physalacriaceae | Agaricales | Agaricomycetes | CCCCC |  | pacbio |
| *Pleurotus eryngii* | Pleurotaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Pleurotus eryngii* | Pleurotaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Pleurotus eryngii* | Pleurotaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Pleurotus eryngii* | Pleurotaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Pleurotus ostreatus* | Pleurotaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Pleurotus ostreatus* | Pleurotaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Pleurotus ostreatus* | Pleurotaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Volvariella surrecta* | Pluteaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Volvopluteus gloiocephalus* | Pluteaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Coprinellus micaceus* | Psathyrellaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Tricholoma cingulatum* | Tricholomataceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Tricholoma hemisulphureum* | Tricholomataceae | Agaricales | Agaricomycetes | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Guepinia helvelloides* |  | Auriculariales | Agaricomycetes | AGATAGAT | AACCCT | pacbio |
| *Laetiporus sulphureus* | Laetiporaceae | Polyporales | Agaricomycetes | CCCCC | CCCCCCC | pacbio |
| *Laetiporus sulphureus* | Laetiporaceae | Polyporales | Agaricomycetes | CCCCC | CCCCCCC | pacbio |
| *Hericium coralloides* | Hericiaceae | Russulales | Agaricomycetes |  |  | pacbio |
| *Peniophora laeta* | Peniophoraceae | Russulales | Agaricomycetes |  |  | pacbio |
| *Lactarius evosmus* | Russulaceae | Russulales | Agaricomycetes |  |  | pacbio |
| *Lactarius tabidus* | Russulaceae | Russulales | Agaricomycetes | AACTCGGAACTCGG | AAGCCT | pacbio |
| *Russula farinipes* | Russulaceae | Russulales | Agaricomycetes |  |  | pacbio |
| *Stereum gausapatum* | Stereaceae | Russulales | Agaricomycetes |  |  | pacbio |
| *Bugulina stolonifera* | Bugulidae | Cheilostomatida | Gymnolaemata | AAACCCC | AAACCCCAAACCCC | assembly |
| *Bugulina stolonifera* | Bugulidae | Cheilostomatida | Gymnolaemata | ACAGT | AAACCCC | pacbio |
| *Cryptosula pallasiana* | Cryptosulidae | Cheilostomatida | Gymnolaemata | ATCATCG | ACATACAT | assembly |
| *Cryptosula pallasiana* | Cryptosulidae | Cheilostomatida | Gymnolaemata | ACTACT | ATCATC | pacbio |
| *Membranipora membranacea* | Membraniporidae | Cheilostomatida | Gymnolaemata | AAACCCC | AACCCCG | assembly |
| *Membranipora membranacea* | Membraniporidae | Cheilostomatida | Gymnolaemata | AAATAAAT | ACCACC | pacbio |
| *Watersipora subatra* | Watersiporidae | Cheilostomatida | Gymnolaemata | AAGTCT | AAGTCTAAGTCT | pacbio |
| *Pycnococcus provasolii* | Pycnococcaceae |  |  | AACCCT |  | assembly |
| *Pycnococcus provasolii* | Pycnococcaceae |  |  |  |  | pacbio |
| *Tetraselmis chuii* | Chlorodendraceae | Chlorodendrales | Chlorodendrophyceae |  |  | pacbio |
| *Brachiomonas submarina* | Chlamydomonadaceae | Chlamydomonadales | Chlorophyceae | AAGGATGGAC | ACAGACAG | pacbio |
| *Dunaliella primolecta* | Dunaliellaceae | Chlamydomonadales | Chlorophyceae | AACCCT | AACCCTAACCCT | assembly |
| *Dunaliella primolecta* | Dunaliellaceae | Chlamydomonadales | Chlorophyceae | ACACACAC | ACACAC | pacbio |
| *Hydrodictyon reticulatum* | Hydrodictyaceae | Sphaeropleales | Chlorophyceae | ACACAC | ACAGACAG | pacbio |
| *Coelastrum microporum* | Scenedesmaceae | Sphaeropleales | Chlorophyceae |  |  | pacbio |
| *Chloroidium saccharophilum* |  | Watanabeales | Trebouxiophyceae |  |  | pacbio |
| *Conger conger* | Congridae | Anguilliformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Telmatherina bonti* | Telmatherinidae | Atheriniformes | Actinopteri | ACCAG | AACCCT | pacbio |
| *Lipophrys pholis* | Blenniidae | Blenniiformes | Actinopteri | AGATAGAT | AACCCT | pacbio |
| *Trachurus trachurus* | Carangidae | Carangiformes | Actinopteri | AAAAA | AACCCT | assembly |
| *Trachurus trachurus* | Carangidae | Carangiformes | Actinopteri |  |  | pacbio |
| *Barbus barbus* | Cyprinidae | Cypriniformes | Actinopteri | AACCCT | AACCCTAACCCT | assembly |
| *Barbus barbus* | Cyprinidae | Cypriniformes | Actinopteri | AACCCT | ACACAC | pacbio |
| *Carassius carassius* | Cyprinidae | Cypriniformes | Actinopteri | AGATAGAT | AACCCT | pacbio |
| *Danio rerio* | Danionidae | Cypriniformes | Actinopteri | AACCCT | AGATAGAT | pacbio |
| *Gobio gobio* | Gobionidae | Cypriniformes | Actinopteri | AACCCT | AGATAGAT | pacbio |
| *Phoxinus phoxinus* | Leuciscidae | Cypriniformes | Actinopteri | AACCCT | AATGC | pacbio |
| *Rutilus rutilus* | Leuciscidae | Cypriniformes | Actinopteri | AACCCT | AGATAGAT | pacbio |
| *Squalius cephalus* | Leuciscidae | Cypriniformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Barbatula barbatula* | Nemacheilidae | Cypriniformes | Actinopteri | AACCCT | AACCCTAACCCT | assembly |
| *Barbatula barbatula* | Nemacheilidae | Cypriniformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Ciliata mustela* | Lotidae | Gadiformes | Actinopteri | AGATAGATAGAT | AACCCT | pacbio |
| *Symphodus melops* | Labridae | Labriformes | Actinopteri | AACCCT | AACCCTAACCCT | assembly |
| *Symphodus melops* | Labridae | Labriformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Taurulus bubalis* | Cottidae | Perciformes | Actinopteri | AACCCT | AACCCTAACCCT | assembly |
| *Taurulus bubalis* | Cottidae | Perciformes | Actinopteri | AACCCT | ACACAC | pacbio |
| *Gasterosteus aculeatus* | Gasterosteidae | Perciformes | Actinopteri | AGATAGAT | AACCCT | pacbio |
| *Pholis gunnellus* | Pholidae | Perciformes | Actinopteri | AACCCT | AACCCTAACCCT | assembly |
| *Pholis gunnellus* | Pholidae | Perciformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Pleuronectes platessa* | Pleuronectidae | Pleuronectiformes | Actinopteri | AACCCT | AACCCTAACCCT | assembly |
| *Pleuronectes platessa* | Pleuronectidae | Pleuronectiformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Microchirus variegatus* | Soleidae | Pleuronectiformes | Actinopteri | AGATAGAT | ACTAT | pacbio |
| *Coregonus lavaretus* | Salmonidae | Salmoniformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Salmo trutta* | Salmonidae | Salmoniformes | Actinopteri | ACACAC | AACCCT | assembly |
| *Salmo trutta* | Salmonidae | Salmoniformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Thunnus albacares* | Scombridae | Scombriformes | Actinopteri | AACCCT | ACACAC | pacbio |
| *Nerophis lumbriciformis* | Syngnathidae | Syngnathiformes | Actinopteri | AGATAGAT | AACCCT | pacbio |
| *Syngnathus acus* | Syngnathidae | Syngnathiformes | Actinopteri | AACCCT | AACCCTAACCCT | assembly |
| *Syngnathus acus* | Syngnathidae | Syngnathiformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Hyperoplus immaculatus* | Ammodytidae | Uranoscopiformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Bufo bufo* | Bufonidae | Anura | Amphibia | AACCCT | AACCCTAACCCT | assembly |
| *Rana temporaria* | Ranidae | Anura | Amphibia |  |  | assembly |
| *Lissotriton helveticus* | Salamandridae | Caudata | Amphibia | AGATAGAT | ACTACTC | pacbio |
| *Lissotriton vulgaris* | Salamandridae | Caudata | Amphibia | AGATAGAT | AGATAGATAGAT | pacbio |
| *Clavelina lepadiformis* | Clavelinidae | Aplousobranchia | Ascidiacea | AACCCT | AACCCTAACCCT | pacbio |
| *Aplidium turbinatum* | Polyclinidae | Aplousobranchia | Ascidiacea | AACCCT | AACCCTAACCCT | assembly |
| *Aplidium turbinatum* | Polyclinidae | Aplousobranchia | Ascidiacea | AACCCT | AACCCTAACCCT | pacbio |
| *Ascidia mentula* | Ascidiidae | Phlebobranchia | Ascidiacea | AACCCT | AACCCTAACCCT | assembly |
| *Ascidia mentula* | Ascidiidae | Phlebobranchia | Ascidiacea | AACCCT | AACCCTAACCCT | pacbio |
| *Corella eumyota* | Corellidae | Phlebobranchia | Ascidiacea | AACCCT | ACCCTG | pacbio |
| *Styela clava* | Styelidae | Stolidobranchia | Ascidiacea | AACCCT | AACCCTAACCCT | pacbio |
| *Accipiter gentilis* | Accipitridae | Accipitriformes | Aves | AACCCT | AACCCTAACCCT | assembly |
| *Accipiter gentilis* | Accipitridae | Accipitriformes | Aves | AACCCT | AACCCTAACCCT | pacbio |
| *Caprimulgus europaeus* | Caprimulgidae | Caprimulgiformes | Aves | AACCCT | AACCCTAACCCT | assembly |
| *Streptopelia turtur* | Columbidae | Columbiformes | Aves |  |  | assembly |
| *Tetrao urogallus* | Phasianidae | Galliformes | Aves | AACCCT | AACCCTAACCCT | pacbio |
| *Cinclus cinclus* | Cinclidae | Passeriformes | Aves | AACCCT | AAGGG | pacbio |
| *Fringilla coelebs* | Fringillidae | Passeriformes | Aves |  |  | pacbio |
| *Erithacus rubecula* | Turdidae | Passeriformes | Aves | AAGGAAGG | AGAGG | assembly |
| *Phaethon aethereus* | Phaethontidae | Pelecaniformes | Aves | AACCCT | AACCCTAACCCT | pacbio |
| *Calonectris borealis* | Procellariidae | Procellariiformes | Aves | AACCCT | CCCCC | pacbio |
| *Scyliorhinus canicula* | Scyliorhinidae | Carcharhiniformes | Chondrichthyes | AACCCT | AGATAGAT | assembly |
| *Cervus elaphus* | Cervidae | Artiodactyla | Mammalia | AAAAA | AAAAAA | assembly |
| *Cervus elaphus* | Cervidae | Artiodactyla | Mammalia | AAAAA | AAAAAA | pacbio |
| *Orcinus orca* | Delphinidae | Artiodactyla | Mammalia | AACCCT |  | pacbio |
| *Hyperoodon ampullatus* | Ziphiidae | Artiodactyla | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Canis lupus* | Canidae | Carnivora | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Canis lupus* | Canidae | Carnivora | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Lutra lutra* | Mustelidae | Carnivora | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Meles meles* | Mustelidae | Carnivora | Mammalia |  |  | assembly |
| *Meles meles* | Mustelidae | Carnivora | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Eptesicus nilssonii* | Vespertilionidae | Chiroptera | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Myotis daubentonii* | Vespertilionidae | Chiroptera | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Pipistrellus pipistrellus* | Vespertilionidae | Chiroptera | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Pipistrellus pygmaeus* | Vespertilionidae | Chiroptera | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Sorex araneus* | Soricidae | Eulipotyphla | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Homo sapiens* | Hominidae | Primates | Mammalia | AATGG | AACCCT | pacbio |
| *Arvicola amphibius* | Cricetidae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Myodes glareolus* | Cricetidae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Apodemus flavicollis* | Muridae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Apodemus sylvaticus* | Muridae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Mus musculus* | Muridae | Rodentia | Mammalia | AACCCTAACCCT | AACCCT | pacbio |
| *Rattus norvegicus* | Muridae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Rattus norvegicus* | Muridae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Sciurus carolinensis* | Sciuridae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Sciurus vulgaris* | Sciuridae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Myxine glutinosa* | Myxinidae | Myxiniformes | Myxini | AACCCT | AACCCTAACCCT | pacbio |
| *Actinia fragacea* | Actiniidae | Actiniaria | Anthozoa | AACCCT | ATCATC | pacbio |
| *Diadumene lineata* | Diadumenidae | Actiniaria | Anthozoa | AACCCT | AACCCTAACCCT | assembly |
| *Diadumene lineata* | Diadumenidae | Actiniaria | Anthozoa | AACCCT | AAGAGTGT | pacbio |
| *Nematostella vectensis* | Edwardsiidae | Actiniaria | Anthozoa | AACCCT | ACCATC | pacbio |
| *Metridium senile* | Metridiidae | Actiniaria | Anthozoa | AACCCT | AAGAC | pacbio |
| *Cordylophora caspia* | Cordylophoridae | Anthoathecata | Hydrozoa | AACCCT | AACCCTAACCCT | pacbio |
| *Haliclystus octoradiatus* | Haliclystidae | Stauromedusae | Staurozoa | AATAAT | AATAATAAT | assembly |
| *Haliclystus octoradiatus* | Haliclystidae | Stauromedusae | Staurozoa | AATAAT | ACTAT | pacbio |
| *Asterias rubens* | Asteriidae | Forcipulatida | Asteroidea | AACCCT | AACCCTAACCCT | assembly |
| *Marthasterias glacialis* | Asteriidae | Forcipulatida | Asteroidea | AACCCT | AACCCTAACCCT | assembly |
| *Marthasterias glacialis* | Asteriidae | Forcipulatida | Asteroidea | AACCCT | AAAGGAC | pacbio |
| *Antedon bifida* | Antedonidae | Comatulida | Crinoidea | AACCCT | AACAAC | pacbio |
| *Echinus esculentus* | Echinidae | Camarodonta | Echinoidea | AACCCT | AACCCTAACCCT | pacbio |
| *Psammechinus miliaris* | Parechinidae | Camarodonta | Echinoidea | AACCCT | AACCCTAACCCT | pacbio |
| *Ophiopholis aculeata* | Ophiactidae | Amphilepidida | Ophiuroidea | AACCCT | AACCCTAACCCT | pacbio |
| *Ophiocomina nigra* | Ophiocomidae | Amphilepidida | Ophiuroidea | AACCCT | AACCCTAACCCT | pacbio |
| *Ophiura albida* | Ophiuridae | Amphilepidida | Ophiuroidea | AACCCT | AACCCTAACCCT | pacbio |
| *Euglenaria anabaena* | Euglenaceae | Euglenales | Euglenida | AACCCT | AACCCTAACCCT | pacbio |
| *Chrysotila carterae* | Isochrysidaceae | Isochrysidales |  | AACCCT |  | pacbio |
| *Diacronema lutheri* | Pavlovaceae | Pavlovales |  | ACACAC | ACACACAC | pacbio |
| *Tetramitus jugosus* | Vahlkampfiidae |  |  | AAACCC | AAACCCAAACCC | assembly |
| *Tetramitus jugosus* | Vahlkampfiidae |  |  | AAACCC | CCCCC | pacbio |
| *Phaxas pellucidus* | Pharidae | Adapedonta | Bivalvia | AACAT | AAGTGC | pacbio |
| *Cerastoderma edule* | Cardiidae | Cardiida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Gari fervensis* | Psammobiidae | Cardiida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Gari tellinella* | Psammobiidae | Cardiida | Bivalvia | AACCCT | AACCCTAACCCT | assembly |
| *Gari tellinella* | Psammobiidae | Cardiida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Azorinus chamasolen* | Solecurtidae | Cardiida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Fabulina fabula* | Tellinidae | Cardiida | Bivalvia | AGATAGAT | AACCCT | pacbio |
| *Macomangulus tenuis* | Tellinidae | Cardiida | Bivalvia | AACCCT | AACATGGT | pacbio |
| *Nucula nucleus* | Nuculidae | Nuculida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Magallana gigas* | Ostreidae | Ostreida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Ostrea edulis* | Ostreidae | Ostreida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Pododesmus patelliformis* | Anomiidae | Pectinida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Mimachlamys varia* | Pectinidae | Pectinida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Pecten maximus* | Pectinidae | Pectinida | Bivalvia | CCCCC | AACCCT | assembly |
| *Spisula solida* | Mactridae | Venerida | Bivalvia | AACCCT | AACCCTAACCCT | assembly |
| *Spisula solida* | Mactridae | Venerida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Spisula subtruncata* | Mactridae | Venerida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Pisidium nitidum* | Sphaeriidae | Venerida | Bivalvia | ACTACT | ACTACTACT | pacbio |
| *Pisidium subtruncatum* | Sphaeriidae | Venerida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Mysia undata* | Veneridae | Venerida | Bivalvia |  |  | pacbio |
| *Polititapes rhomboides* | Veneridae | Venerida | Bivalvia |  |  | pacbio |
| *Venerupis corrugata* | Veneridae | Venerida | Bivalvia | AACCCT | AATGAATG | pacbio |
| *Eledone cirrhosa* | Octopodidae | Octopoda | Cephalopoda | AAGCT | AACTT | pacbio |
| *Sepia officinalis* | Sepiidae | Sepiida | Cephalopoda | AACCCT | AACCCTAACCCT | pacbio |
| *Sepiola tridens* | Sepiolidae | Sepiida | Cephalopoda | AACCCT | AGATAGAT | pacbio |
| *Ancylus fluviatilis* | Ancylidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Testudinalia testudinalis* | Lottiidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Stagnicola fuscus* | Lymnaeidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Patella depressa* | Patellidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Patella pellucida* | Patellidae |  | Gastropoda | AACCCT | AACCCTAACCCT | assembly |
| *Patella pellucida* | Patellidae |  | Gastropoda | AACTCTCTACT | AACTCTACT | pacbio |
| *Patella ulyssiponensis* | Patellidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Patella vulgata* | Patellidae |  | Gastropoda | AACCCT | AACCCTAACCCT | assembly |
| *Patella vulgata* | Patellidae |  | Gastropoda |  |  | pacbio |
| *Physa fontinalis* | Physidae |  | Gastropoda | AACCCT | AGATAGAT | pacbio |
| *Physella acuta* | Physidae |  | Gastropoda | ATCATC | AGATAGAT | pacbio |
| *Anisus vortex* | Planorbidae |  | Gastropoda | AAGTAAGT | AAGTAAGTAAGT | pacbio |
| *Biomphalaria glabrata* | Planorbidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Planorbis planorbis* | Planorbidae |  | Gastropoda | AGATGGAT | AGATATAT | pacbio |
| *Valvata piscinalis* | Valvatidae |  | Gastropoda | AATACTAC | AATACTACAATACTAC | pacbio |
| *Aplysia punctata* | Aplysiidae | Aplysiida | Gastropoda | AACCCT | ACATACAT | pacbio |
| *Theodoxus fluviatilis* | Neritidae | Cycloneritida | Gastropoda | ACACAC | AGATAGAT | pacbio |
| *Otina ovata* | Otinidae | Ellobiida | Gastropoda | AACCCT | AATAC | pacbio |
| *Bithynia leachii* | Bithyniidae | Littorinimorpha | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Littorina arcana* | Littorinidae | Littorinimorpha | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Littorina compressa* | Littorinidae | Littorinimorpha | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Littorina obtusata* | Littorinidae | Littorinimorpha | Gastropoda | AACCCT | ACACAC | pacbio |
| *Trivia monacha* | Triviidae | Littorinimorpha | Gastropoda | ACACAC | ACACACAC | pacbio |
| *Colus gracilis* | Colidae | Neogastropoda | Gastropoda |  |  | pacbio |
| *Nucella lapillus* | Muricidae | Neogastropoda | Gastropoda | ACACAC | ACTACT | pacbio |
| *Tritia reticulata* | Nassariidae | Neogastropoda | Gastropoda | ACTACT | AACCCT | pacbio |
| *Crimora papillata* |  | Nudibranchia | Gastropoda | ACTACT | ACTACTACT | pacbio |
| *Doris pseudoargus* | Dorididae | Nudibranchia | Gastropoda | AAACAC | AACCCT | pacbio |
| *Facelina auriculata* | Facelinidae | Nudibranchia | Gastropoda | ACAGTAGC | AACCCT | pacbio |
| *Clausilia bidentata* | Clausiliidae | Stylommatophora | Gastropoda | AACCCT | AGATAGAT | pacbio |
| *Discus rotundatus* | Endodontidae | Stylommatophora | Gastropoda | AACTAACT | AACTAACTAACT | pacbio |
| *Helicella itala* | Geomitridae | Stylommatophora | Gastropoda | ACTACT | ACTACTACT | pacbio |
| *Xeroplexa intersecta* | Geomitridae | Stylommatophora | Gastropoda | AACTAACT | AACTAACTAACT | pacbio |
| *Cepaea hortensis* | Helicidae | Stylommatophora | Gastropoda | ACTACT | AACCCT | pacbio |
| *Cepaea nemoralis* | Helicidae | Stylommatophora | Gastropoda | ACACAC | ACTACT | pacbio |
| *Cornu aspersum* | Helicidae | Stylommatophora | Gastropoda | ACTACT | AGATAGAT | pacbio |
| *Trochulus hispidus* | Hygromiidae | Stylommatophora | Gastropoda | AGATAGAT | AGATAGATAGAT | pacbio |
| *Daudebardia rufa* | Oxychilidae | Stylommatophora | Gastropoda | AACTAACT | AACTAACTAACT | pacbio |
| *Calliostoma zizyphinum* | Calliostomatidae | Trochida | Gastropoda | AACCCT | AAACCCT | pacbio |
| *Gibbula magus* | Trochidae | Trochida | Gastropoda | AACCCT | AACCCTAACCCT | assembly |
| *Gibbula magus* | Trochidae | Trochida | Gastropoda | AACATG | AACCCT | pacbio |
| *Phorcus lineatus* | Trochidae | Trochida | Gastropoda | AACCCT | AAACAC | assembly |
| *Phorcus lineatus* | Trochidae | Trochida | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Steromphala cineraria* | Trochidae | Trochida | Gastropoda | AACCCT | AACCCTAACCCT | assembly |
| *Steromphala cineraria* | Trochidae | Trochida | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Steromphala umbilicalis* | Trochidae | Trochida | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Acanthochitona crinita* | Acanthochitonidae | Chitonida | Polyplacophora | AACCCT | AACAT | pacbio |
| *Mucor piriformis* | Mucoraceae | Mucorales | Mucoromycetes | AACCCTCGCAGGCCGTAGGCCGTGGGTGCT |  | assembly |
| *Mucor piriformis* | Mucoraceae | Mucorales | Mucoromycetes | AAAAA | CCCCC | pacbio |
| *Caenorhabditis monodelphis* | Rhabditidae | Rhabditida | Chromadorea | AAGCCT | AAGCCTAAGCCT | pacbio |
| *Dioctophyme renale* | Dioctophymatidae | Dioctophymatida | Enoplea | ACGATG | ATCATC | pacbio |
| *Lineus longissimus* | Lineidae | Heteronemertea | Pilidiophora | AACCCT | AACCCTAACCCT | assembly |
| *Lineus longissimus* | Lineidae | Heteronemertea | Pilidiophora | AACCCT | ATCATC | pacbio |
| *Ceramium secundatum* | Ceramiaceae | Ceramiales | Florideophyceae | AACAAC | AACAACAAC | pacbio |
| *Ceramium virgatum* | Ceramiaceae | Ceramiales | Florideophyceae | AAAAT | AAAATAAAT | pacbio |
| *Heterosiphonia plumosa* | Dasyaceae | Ceramiales | Florideophyceae | AACCT | AACCAC | pacbio |
| *Vertebrata lanosa* | Rhodomelaceae | Ceramiales | Florideophyceae | AACCCT | AACACAC | pacbio |
| *Calliblepharis jubata* | Cystocloniaceae | Gigartinales | Florideophyceae | ATATAT | ATATATAT | pacbio |
| *Metacallophyllis laciniata* | Kallymeniaceae | Gigartinales | Florideophyceae | ACAGGCGTGCCC | AAGCGAGATGCAAGCGATGC | pacbio |
| *Palmaria palmata* | Palmariaceae | Palmariales | Florideophyceae | ACACTGAGT | ACAGGCGTGCCC | pacbio |
| *Anomodon viticulosus* | Anomodontaceae | Hypnales | Bryopsida | AATGAT | ACTCACTC | pacbio |
| *Pseudoscleropodium purum* | Brachytheciaceae | Hypnales | Bryopsida | ACATACAT | ACATACATACATACAT | pacbio |
| *Climacium dendroides* | Climaciaceae | Hypnales | Bryopsida | AAACCCT | AATGG | pacbio |
| *Hylocomiadelphus triquetrus* | Hylocomiaceae | Hypnales | Bryopsida | AACAG |  | pacbio |
| *Rhytidiadelphus loreus* | Hylocomiaceae | Hypnales | Bryopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Rhytidiadelphus loreus* | Hylocomiaceae | Hypnales | Bryopsida |  |  | pacbio |
| *Isothecium myosuroides* | Lembophyllaceae | Hypnales | Bryopsida | AAACCCT | AACCCT | pacbio |
| *Exsertotheca crispa* | Neckeraceae | Hypnales | Bryopsida | AAACCCT | AACCCT | pacbio |
| *Neckera pumila* | Neckeraceae | Hypnales | Bryopsida | AAACCCT | ACACAC | pacbio |
| *Thamnobryum alopecurum* | Neckeraceae | Hypnales | Bryopsida |  |  | pacbio |
| *Thuidium delicatulum* | Thuidiaceae | Hypnales | Bryopsida |  |  | pacbio |
| *Thuidium tamariscinum* | Thuidiaceae | Hypnales | Bryopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Thuidium tamariscinum* | Thuidiaceae | Hypnales | Bryopsida |  |  | pacbio |
| *Huperzia selago* | Lycopodiaceae | Lycopodiales | Lycopodiopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Selaginella selaginoides* | Selaginellaceae | Selaginellales | Lycopodiopsida | AAACCCT | AACCT | pacbio |
| *Alisma plantago-aquatica* | Alismataceae | Alismatales | Magnoliopsida | ATCATC | AAACCCT | pacbio |
| *Aponogeton distachyos* | Aponogetonaceae | Alismatales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Arum italicum* | Araceae | Alismatales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Arum maculatum* | Araceae | Alismatales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lemna minuta* | Araceae | Alismatales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lemna trisulca* | Araceae | Alismatales | Magnoliopsida | AAACCCT | AACAT | pacbio |
| *Butomus umbellatus* | Butomaceae | Alismatales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Ruppia maritima* | Cymodoceaceae | Alismatales | Magnoliopsida | AAACCCT | ACATACAT | pacbio |
| *Stratiotes aloides* | Hydrocharitaceae | Alismatales | Magnoliopsida | AACCGAGCCCAT | AACCGAGCCCATAACCGAGCCCAT | pacbio |
| *Triglochin maritima* | Juncaginaceae | Alismatales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Triglochin palustris* | Juncaginaceae | Alismatales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Potamogeton natans* | Potamogetonaceae | Alismatales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Angelica archangelica* | Apiaceae | Apiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Angelica sylvestris* | Apiaceae | Apiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Anthriscus sylvestris* | Apiaceae | Apiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Conopodium majus* | Apiaceae | Apiales | Magnoliopsida | AAACCCT | AACCCTG | pacbio |
| *Daucus carota* | Apiaceae | Apiales | Magnoliopsida |  |  | pacbio |
| *Helosciadium nodiflorum* | Apiaceae | Apiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Heracleum sphondylium* | Apiaceae | Apiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Ligusticum scoticum* | Apiaceae | Apiales | Magnoliopsida |  |  | pacbio |
| *Smyrnium perfoliatum* | Apiaceae | Apiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Hedera helix* | Araliaceae | Apiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Hedera helix* | Araliaceae | Apiales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Ilex aquifolium* | Aquifoliaceae | Aquifoliales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Allium ampeloprasum* | Amaryllidaceae | Asparagales | Magnoliopsida |  |  | pacbio |
| *Allium triquetrum* | Amaryllidaceae | Asparagales | Magnoliopsida | AACCGAGCCCAT | AACCGAGCCCATAACCGAGCCCAT | pacbio |
| *Allium vineale* | Amaryllidaceae | Asparagales | Magnoliopsida | AACCGAGCCCAT |  | pacbio |
| *Narcissus pseudonarcissus* | Amaryllidaceae | Asparagales | Magnoliopsida | AACCCT | AACCCTAACCCT | pacbio |
| *Hyacinthoides non-scripta* | Hyacinthaceae | Asparagales | Magnoliopsida |  |  | pacbio |
| *Scilla verna* | Hyacinthaceae | Asparagales | Magnoliopsida | AAACCCT | AACCCT | pacbio |
| *Iris foetidissima* | Iridaceae | Asparagales | Magnoliopsida | AACCCT | AACCCTAACCCT | pacbio |
| *Iris pseudacorus* | Iridaceae | Asparagales | Magnoliopsida | AACCCT | AACCCTAACCCT | pacbio |
| *Cephalanthera longifolia* | Orchidaceae | Asparagales | Magnoliopsida |  |  | pacbio |
| *Dactylorhiza maculata* | Orchidaceae | Asparagales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Epipactis palustris* | Orchidaceae | Asparagales | Magnoliopsida | AAACCCT |  | pacbio |
| *Epipactis purpurata* | Orchidaceae | Asparagales | Magnoliopsida |  |  | pacbio |
| *Ophrys apifera* | Orchidaceae | Asparagales | Magnoliopsida | ACCAGT | ACGCACGC | pacbio |
| *Achillea millefolium* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AGATAGAT | pacbio |
| *Achillea ptarmica* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Arctium minus* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Artemisia maritima* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Artemisia vulgaris* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Bellis perennis* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AGATAGAT | pacbio |
| *Centaurea nigra* | Asteraceae | Asterales | Magnoliopsida |  |  | pacbio |
| *Chamaemelum nobile* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | ATATAT | pacbio |
| *Cicerbita muralis* | Asteraceae | Asterales | Magnoliopsida | ACATACAT | AAACCCT | pacbio |
| *Filago vulgaris* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Helminthotheca echioides* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Hypochaeris maculata* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Hypochaeris radicata* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Inula conyza* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Leontodon hispidus* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Petasites fragrans* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Petasites japonicus* | Asteraceae | Asterales | Magnoliopsida | AATGATG | AATGATGAATGATG | pacbio |
| *Pulicaria dysenterica* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Pulicaria dysenterica* | Asteraceae | Asterales | Magnoliopsida | AACAAC | AAACCCT | pacbio |
| *Scorzoneroides autumnalis* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Senecio squalidus* | Asteraceae | Asterales | Magnoliopsida | AAACCCT |  | assembly |
| *Senecio vulgaris* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Sonchus arvensis* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Sonchus asper* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Tanacetum vulgare* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | ATATAT | pacbio |
| *Tripleurospermum maritimum* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Tripolium pannonicum* | Asteraceae | Asterales | Magnoliopsida | AGATAGAT | AACGAT | pacbio |
| *Tussilago farfara* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Campanula glomerata* | Campanulaceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Jasione montana* | Campanulaceae | Asterales | Magnoliopsida | AACCCTG | AACCCCTG | pacbio |
| *Phyteuma orbiculare* | Campanulaceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Nymphoides peltata* | Menyanthaceae | Asterales | Magnoliopsida | AAACCCT |  | pacbio |
| *Borago officinalis* | Boraginaceae | Boraginales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Echium vulgare* | Boraginaceae | Boraginales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Myosotis scorpioides* | Boraginaceae | Boraginales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Pentaglottis sempervirens* | Boraginaceae | Boraginales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Symphytum officinale* | Boraginaceae | Boraginales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Arabidopsis thaliana* | Brassicaceae | Brassicales | Magnoliopsida | AAACCCT | AACCT | pacbio |
| *Brassica oleracea* | Brassicaceae | Brassicales | Magnoliopsida |  |  | pacbio |
| *Cakile maritima* | Brassicaceae | Brassicales | Magnoliopsida | AAACCCT | ACAGACT | pacbio |
| *Cochlearia danica* | Brassicaceae | Brassicales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lepidium draba* | Brassicaceae | Brassicales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Raphanus raphanistrum* | Brassicaceae | Brassicales | Magnoliopsida |  |  | pacbio |
| *Sisymbrium officinale* | Brassicaceae | Brassicales | Magnoliopsida | AAACCCT | AACCCT | pacbio |
| *Buxus sempervirens* | Buxaceae | Buxales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Buxus sempervirens* | Buxaceae | Buxales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Agrostemma githago* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AATAAT | AAACCCT | pacbio |
| *Cerastium fontanum* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Cerastium glomeratum* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Dianthus deltoides* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Herniaria ciliolata* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Honckenya peploides* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Sagina procumbens* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AACCT | pacbio |
| *Saponaria officinalis* | Caryophyllaceae | Caryophyllales | Magnoliopsida | ACAGACAGATAG | ACAGACAGATAGACAGACAGATAG | pacbio |
| *Silene acaulis* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AACAAC | AATAAT | pacbio |
| *Silene dioica* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Silene latifolia* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AATGCT | pacbio |
| *Spergularia bocconei* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Spergularia marina* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Stellaria media* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Atriplex glabriuscula* | Chenopodiaceae | Caryophyllales | Magnoliopsida | AAATAAT | AAATAATAAATAAT | pacbio |
| *Chenopodium album* | Chenopodiaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Suaeda vera* | Chenopodiaceae | Caryophyllales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Phytolacca acinosa* | Phytolaccaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Fallopia sachalinensis* | Polygonaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Persicaria maculosa* | Polygonaceae | Caryophyllales | Magnoliopsida |  |  | pacbio |
| *Polygonum aviculare* | Polygonaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Polygonum aviculare* | Polygonaceae | Caryophyllales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Reynoutria japonica* | Polygonaceae | Caryophyllales | Magnoliopsida | AAACCCT | AACAAC | pacbio |
| *Rumex acetosa* | Polygonaceae | Caryophyllales | Magnoliopsida | AACAAC | AACAACAAC | pacbio |
| *Rumex hydrolapathum* | Polygonaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Rumex sanguineus* | Polygonaceae | Caryophyllales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Tamarix gallica* | Tamaricaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Euonymus europaeus* | Celastraceae | Celastrales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Ceratophyllum demersum* | Ceratophyllaceae | Ceratophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Cornus suecica* | Cornaceae | Cornales | Magnoliopsida |  |  | pacbio |
| *Bryonia dioica* | Cucurbitaceae | Cucurbitales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Narthecium ossifragum* | Nartheciaceae | Dioscoreales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Adoxa moschatellina* | Adoxaceae | Dipsacales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Sambucus nigra* | Adoxaceae | Dipsacales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Viburnum lantana* | Adoxaceae | Dipsacales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Knautia arvensis* | Caprifoliaceae | Dipsacales | Magnoliopsida | AGATAGAT | AATAAT | pacbio |
| *Linnaea borealis* | Caprifoliaceae | Dipsacales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Succisa pratensis* | Caprifoliaceae | Dipsacales | Magnoliopsida | AAACCCT |  | pacbio |
| *Impatiens glandulifera* | Balsaminaceae | Ericales | Magnoliopsida | AAGCATT | AAGCATC | assembly |
| *Impatiens glandulifera* | Balsaminaceae | Ericales | Magnoliopsida | AAGCATC | AAGCATCAAGCATC | pacbio |
| *Impatiens noli-tangere* | Balsaminaceae | Ericales | Magnoliopsida |  |  | pacbio |
| *Diapensia lapponica* | Diapensiaceae | Ericales | Magnoliopsida | AACCCT |  | pacbio |
| *Arctostaphylos uva-ursi* | Ericaceae | Ericales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Monotropa hypopitys* | Ericaceae | Ericales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lysimachia vulgaris* | Primulaceae | Ericales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Samolus valerandi* | Primulaceae | Ericales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Anthyllis vulneraria* | Fabaceae | Fabales | Magnoliopsida | AACCT | AACCTAACCT | pacbio |
| *Galega officinalis* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AGATAGAT | pacbio |
| *Genista pilosa* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lathyrus aphaca* | Fabaceae | Fabales | Magnoliopsida | AGATAGAT |  | pacbio |
| *Lathyrus linifolius* | Fabaceae | Fabales | Magnoliopsida |  |  | pacbio |
| *Lotus corniculatus* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AGATAGAT | pacbio |
| *Medicago arabica* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Medicago arabica* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAGAGATAC | pacbio |
| *Medicago lupulina* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Medicago sativa* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Onobrychis viciifolia* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Trifolium dubium* | Fabaceae | Fabales | Magnoliopsida | AAGAGATAC | AAACCCT | pacbio |
| *Trifolium fragiferum* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AACCCTG | pacbio |
| *Trifolium pratense* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Trifolium subterraneum* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | ACCCTAG | pacbio |
| *Ulex europaeus* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Vicia cracca* | Fabaceae | Fabales | Magnoliopsida | AATAAT | AATAATAAT | pacbio |
| *Vicia sativa* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Vicia sepium* | Fabaceae | Fabales | Magnoliopsida | AGATAGAT | AAACCCT | pacbio |
| *Alnus glutinosa* | Betulaceae | Fagales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Betula pubescens* | Betulaceae | Fagales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Carpinus betulus* | Betulaceae | Fagales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Castanea sativa* | Fagaceae | Fagales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Quercus cerris* | Fagaceae | Fagales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Quercus robur* | Fagaceae | Fagales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Quercus robur* | Fagaceae | Fagales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Myrica gale* | Myricaceae | Fagales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Vinca minor* | Apocynaceae | Gentianales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Centaurium erythraea* | Gentianaceae | Gentianales | Magnoliopsida | AAACCCT |  | pacbio |
| *Cruciata laevipes* | Rubiaceae | Gentianales | Magnoliopsida | AAACCCT |  | pacbio |
| *Galium aparine* | Rubiaceae | Gentianales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Galium odoratum* | Rubiaceae | Gentianales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Galium verum* | Rubiaceae | Gentianales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Sherardia arvensis* | Rubiaceae | Gentianales | Magnoliopsida | CCCCC |  | pacbio |
| *Erodium maritimum* | Geraniaceae | Geraniales | Magnoliopsida | CCCCC | CCCCCC | pacbio |
| *Erodium moschatum* | Geraniaceae | Geraniales | Magnoliopsida | ACTACT | AAACCCT | pacbio |
| *Geranium dissectum* | Geraniaceae | Geraniales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Geranium lucidum* | Geraniaceae | Geraniales | Magnoliopsida | AACCCT | AACCCTAACCCT | pacbio |
| *Geranium robertianum* | Geraniaceae | Geraniales | Magnoliopsida | AACCCT |  | pacbio |
| *Geranium sanguineum* | Geraniaceae | Geraniales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Geranium sylvaticum* | Geraniaceae | Geraniales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Gunnera manicata* | Gunneraceae | Gunnerales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Gunnera tinctoria* | Gunneraceae | Gunnerales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Ballota nigra* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Ballota nigra* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Lamium album* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lamium purpureum* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lycopus europaeus* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Salvia verbenaca* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Scutellaria galericulata* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Scutellaria galericulata* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Scutellaria minor* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Stachys palustris* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AACCT | pacbio |
| *Stachys sylvatica* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Teucrium scorodonia* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Thymus serpyllum* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Ligustrum vulgare* | Oleaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Euphrasia confusa* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Euphrasia foulaensis* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lathraea clandestina* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lathraea squamaria* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Melampyrum pratense* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Melampyrum sylvaticum* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Orobanche hederae* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Erythranthe lutea* | Phrymaceae | Lamiales | Magnoliopsida |  |  | pacbio |
| *Callitriche obtusangula* | Plantaginaceae | Lamiales | Magnoliopsida | AAGTAAGT | AAGTAAGTAAGT | pacbio |
| *Chaenorhinum minus* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Cymbalaria muralis* | Plantaginaceae | Lamiales | Magnoliopsida |  |  | pacbio |
| *Hippuris vulgaris* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AATCT | pacbio |
| *Linaria vulgaris* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Littorella uniflora* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Misopates orontium* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Misopates orontium* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | ATATAT | pacbio |
| *Plantago coronopus* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Plantago lanceolata* | Plantaginaceae | Lamiales | Magnoliopsida | AACCCTAAT | AACCCTAATAACCCTAAT | pacbio |
| *Plantago maritima* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Veronica arvensis* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT |  | pacbio |
| *Veronica chamaedrys* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Veronica hederifolia* | Plantaginaceae | Lamiales | Magnoliopsida | AAGAAG | AAGAAGAAG | pacbio |
| *Veronica officinalis* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Veronica serpyllifolia* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Veronica spicata* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Buddleja davidii* | Scrophulariaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Limosella aquatica* | Scrophulariaceae | Lamiales | Magnoliopsida | AAACCCT |  | pacbio |
| *Scrophularia auriculata* | Scrophulariaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Scrophularia nodosa* | Scrophulariaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Verbena officinalis* | Verbenaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Colchicum autumnale* | Colchicaceae | Liliales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Tulipa sylvestris* | Liliaceae | Liliales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Paris quadrifolia* | Melanthiaceae | Liliales | Magnoliopsida |  |  | pacbio |
| *Euphorbia amygdaloides* | Euphorbiaceae | Malpighiales | Magnoliopsida | AACCCT | AACCCTAACCCT | pacbio |
| *Euphorbia lathyris* | Euphorbiaceae | Malpighiales | Magnoliopsida | AAACCCT | ACATACATAT | pacbio |
| *Euphorbia peplus* | Euphorbiaceae | Malpighiales | Magnoliopsida | AACCCT | CCCCC | pacbio |
| *Mercurialis annua* | Euphorbiaceae | Malpighiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Mercurialis annua* | Euphorbiaceae | Malpighiales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Mercurialis perennis* | Euphorbiaceae | Malpighiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Hypericum perforatum* | Hypericaceae | Malpighiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Populus tremula* | Salicaceae | Malpighiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Salix lapponum* | Salicaceae | Malpighiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Salix myrsinifolia* | Salicaceae | Malpighiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Salix phylicifolia* | Salicaceae | Malpighiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Viola riviniana* | Violaceae | Malpighiales | Magnoliopsida | AAACCCT | AACCCT | pacbio |
| *Helianthemum apenninum* | Cistaceae | Malvales | Magnoliopsida |  |  | pacbio |
| *Daphne mezereum* | Thymelaeaceae | Malvales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lythrum salicaria* | Lythraceae | Myrtales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Chamaenerion angustifolium* | Onagraceae | Myrtales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Chamaenerion angustifolium* | Onagraceae | Myrtales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Circaea lutetiana* | Onagraceae | Myrtales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Nymphaea alba* | Nymphaeaceae | Nymphaeales | Magnoliopsida | AAACCCT | ACACT | pacbio |
| *Aristolochia clematitis* | Aristolochiaceae | Piperales | Magnoliopsida | AACCCTG | AGAGGGCG | pacbio |
| *Carex arenaria* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Carex depauperata* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AACCCTG | pacbio |
| *Carex divulsa* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Carex nigra* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Carex pendula* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Carex rostrata* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Schoenoplectus lacustris* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Eriocaulon aquaticum* | Eriocaulaceae | Poales | Magnoliopsida | AAAAAACCCT | AACCT | pacbio |
| *Juncus effusus* | Juncaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Juncus effusus* | Juncaceae | Poales | Magnoliopsida | AAACCCT | ATATAT | pacbio |
| *Juncus inflexus* | Juncaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Luzula campestris* | Juncaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Luzula sylvatica* | Juncaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Luzula sylvatica* | Juncaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Oreojuncus trifidus* | Juncaceae | Poales | Magnoliopsida | AATAAT | AATAATAAT | pacbio |
| *Agrostis stolonifera* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Alopecurus pratensis* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Anthoxanthum odoratum* | Poaceae | Poales | Magnoliopsida | AACCCT | AAACCCT | pacbio |
| *Arrhenatherum elatius* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Briza media* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Bromus hordeaceus* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Bromus interruptus* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Bromus ramosus* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Bromus sterilis* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Danthonia decumbens* | Poaceae | Poales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Deschampsia cespitosa* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Glyceria maxima* | Poaceae | Poales | Magnoliopsida | AAACCCT | ACCCTAG | pacbio |
| *Hierochloe odorata* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Holcus mollis* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Leymus arenarius* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lolium perenne* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Nardus stricta* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Phalaris arundinacea* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Phragmites australis* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Poa infirma* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Polypogon viridis* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Puccinellia maritima* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Typha latifolia* | Typhaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Berberis aquifolium* | Berberidaceae | Ranunculales | Magnoliopsida |  |  | pacbio |
| *Berberis vulgaris* | Berberidaceae | Ranunculales | Magnoliopsida |  |  | pacbio |
| *Chelidonium majus* | Papaveraceae | Ranunculales | Magnoliopsida | AAACCCT | AACCCT | pacbio |
| *Fumaria muralis* | Papaveraceae | Ranunculales | Magnoliopsida | AAACCG | AAACCGAAACCG | pacbio |
| *Fumaria officinalis* | Papaveraceae | Ranunculales | Magnoliopsida | AAACCG | AAACCGAAACCG | pacbio |
| *Glaucium flavum* | Papaveraceae | Ranunculales | Magnoliopsida | AAAACCCTACCCG | AAAACCCTACCCGAAAACCCTACCCG | pacbio |
| *Papaver dubium* | Papaveraceae | Ranunculales | Magnoliopsida | AACCCTG | AACCCTGAACCCTG | pacbio |
| *Papaver rhoeas* | Papaveraceae | Ranunculales | Magnoliopsida | AACCCTG | AACCCTGAACCCTG | pacbio |
| *Pseudofumaria lutea* | Papaveraceae | Ranunculales | Magnoliopsida | AAACCG |  | pacbio |
| *Adonis annua* | Ranunculaceae | Ranunculales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Anemone nemorosa* | Ranunculaceae | Ranunculales | Magnoliopsida | AAACCCT | AAACAC | pacbio |
| *Caltha palustris* | Ranunculaceae | Ranunculales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Clematis vitalba* | Ranunculaceae | Ranunculales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Ranunculus acris* | Ranunculaceae | Ranunculales | Magnoliopsida |  |  | pacbio |
| *Ranunculus bulbosus* | Ranunculaceae | Ranunculales | Magnoliopsida | AACCCCG | AACCCCGAACCCCG | pacbio |
| *Ranunculus sardous* | Ranunculaceae | Ranunculales | Magnoliopsida | ACTCACTC | AATCAATC | pacbio |
| *Trollius europaeus* | Ranunculaceae | Ranunculales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Humulus lupulus* | Cannabaceae | Rosales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Hippophae rhamnoides* | Elaeagnaceae | Rosales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Rhamnus cathartica* | Rhamnaceae | Rosales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Agrimonia eupatoria* | Rosaceae | Rosales | Magnoliopsida |  |  | pacbio |
| *Alchemilla alpina* | Rosaceae | Rosales | Magnoliopsida | AAACCCT |  | pacbio |
| *Alchemilla arvensis* | Rosaceae | Rosales | Magnoliopsida | AAACCCT |  | pacbio |
| *Alchemilla micans* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Comarum palustre* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AATGG | pacbio |
| *Crataegus laevigata* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Crataegus monogyna* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Dasiphora fruticosa* | Rosaceae | Rosales | Magnoliopsida | AAACCCT |  | pacbio |
| *Filipendula ulmaria* | Rosaceae | Rosales | Magnoliopsida | AAAAA | CCCCC | pacbio |
| *Geum rivale* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AACCCTAAT | pacbio |
| *Geum urbanum* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Geum urbanum* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Malus domestica* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AACCT | pacbio |
| *Malus sylvestris* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Malus sylvestris* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Potentilla anserina* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Potentilla anserina* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AACCT | pacbio |
| *Potentilla reptans* | Rosaceae | Rosales | Magnoliopsida | AACCT | AACCTAACCT | pacbio |
| *Potentilla sterilis* | Rosaceae | Rosales | Magnoliopsida | AAACCCT |  | pacbio |
| *Pyrus communis* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Rosa agrestis* | Rosaceae | Rosales | Magnoliopsida | AAACCCT |  | pacbio |
| *Rosa rubiginosa* | Rosaceae | Rosales | Magnoliopsida | AAACCCT |  | pacbio |
| *Parietaria judaica* | Urticaceae | Rosales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Urtica dioica* | Urticaceae | Rosales | Magnoliopsida | AAACCCT | ACAGTC | pacbio |
| *Urtica urens* | Urticaceae | Rosales | Magnoliopsida | AAACCCT | AAGAGATAC | pacbio |
| *Viscum album* | Viscaceae | Santalales | Magnoliopsida | CCCCC | CCCCCC | pacbio |
| *Acer campestre* | Sapindaceae | Sapindales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Acer pseudoplatanus* | Sapindaceae | Sapindales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Umbilicus rupestris* | Crassulaceae | Saxifragales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Calystegia sepium* | Convolvulaceae | Solanales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Convolvulus arvensis* | Convolvulaceae | Solanales | Magnoliopsida | AAACCCT | ACTACT | pacbio |
| *Cuscuta epithymum* | Convolvulaceae | Solanales | Magnoliopsida | AAACCCT | AACCCTG | pacbio |
| *Atropa belladonna* | Solanaceae | Solanales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Solanum dulcamara* | Solanaceae | Solanales | Magnoliopsida | AACCCTG | AACCCTGAACCCTG | assembly |
| *Solanum dulcamara* | Solanaceae | Solanales | Magnoliopsida | AACCCTG | AATAAT | pacbio |
| *Lunularia cruciata* | Lunulariaceae | Lunulariales | Marchantiopsida | AAACCCT | CCCCC | pacbio |
| *Equisetum arvense* | Equisetaceae | Equisetales | Polypodiopsida | AAACCCT | AGATAGAT | pacbio |
| *Equisetum hyemale* | Equisetaceae | Equisetales | Polypodiopsida | AGATAGAT | AGATAGATAGAT | pacbio |
| *Equisetum palustre* | Equisetaceae | Equisetales | Polypodiopsida | AGAGAG | AGATAGAT | pacbio |
| *Equisetum telmateia* | Equisetaceae | Equisetales | Polypodiopsida | AGATAGAT | AGATAGATAGAT | pacbio |
| *Equisetum variegatum* | Equisetaceae | Equisetales | Polypodiopsida | AGATAGAT | AGATAGATAGAT | pacbio |
| *Ophioglossum vulgatum* | Ophioglossaceae | Ophioglossales | Polypodiopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Asplenium scolopendrium* | Aspleniaceae | Polypodiales | Polypodiopsida | ATATAT | ATATATAT | pacbio |
| *Polystichum setiferum* | Dryopteridaceae | Polypodiales | Polypodiopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Polypodium vulgare* | Polypodiaceae | Polypodiales | Polypodiopsida | ATATAT | AAACCCT | pacbio |
| *Cryptogramma crispa* | Pteridaceae | Polypodiales | Polypodiopsida | AAACCCT | AAGTAAGT | pacbio |
| *Phegopteris connectilis* | Thelypteridaceae | Polypodiales | Polypodiopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Polytrichum commune* | Polytrichaceae | Polytrichales | Polytrichopsida | AACCT | AGATAGAT | pacbio |
| *Sphagnum inundatum* | Sphagnaceae | Sphagnales | Sphagnopsida | AAACCT | AAACCCT | pacbio |
| *Sphagnum medium* | Sphagnaceae | Sphagnales | Sphagnopsida | AAACCCT | AAACCT | pacbio |
