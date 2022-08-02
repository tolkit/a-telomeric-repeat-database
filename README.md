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
| *Aporrectodea caliginosa* | Lumbricidae | Crassiclitellata | Clitellata |  |  | pacbio |
| *Eisenia fetida* | Lumbricidae | Crassiclitellata | Clitellata | ATCATC | AACCCT | pacbio |
| *Lumbricus castaneus* | Lumbricidae | Crassiclitellata | Clitellata | ATCATC | AACCCT | pacbio |
| *Lumbricus rubellus* | Lumbricidae | Crassiclitellata | Clitellata | AAGGAC | AACCCT | pacbio |
| *Lumbricus terrestris* | Lumbricidae | Crassiclitellata | Clitellata | AACTC | AACCCT | pacbio |
| *Octolasion cyaneum* | Lumbricidae | Crassiclitellata | Clitellata | AACCCT | ACCATC | pacbio |
| *Piscicola geometra* | Piscicolidae | Hirudinida | Clitellata | AACACGAGATG | AACCCT | pacbio |
| *Glossiphonia complanata* | Glossiphoniidae | Rhynchobdellida | Clitellata | AATGAATG | AAGTAAGT | pacbio |
| *Helobdella stagnalis* | Glossiphoniidae | Rhynchobdellida | Clitellata | ACATACAT | AAATGAAT | pacbio |
| *Euclymene oerstedii* | Maldanidae |  | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Goniada maculata* | Goniadidae | Phyllodocida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Alitta virens* | Nereididae | Phyllodocida | Polychaeta | AACCCT | ACTACT | pacbio |
| *Harmothoe impar* | Polynoidae | Phyllodocida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Lepidonotus clava* | Polynoidae | Phyllodocida | Polychaeta | AACCCT |  | pacbio |
| *Sthenelais limicola* | Sigalionidae | Phyllodocida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Spirobranchus lamarcki* | Serpulidae | Sabellida | Polychaeta | AACCCT | AACCCTAACCCT | pacbio |
| *Terebella lapidaria* | Terebellidae | Terebellida | Polychaeta | ACTGACTG | ACACAC | pacbio |
| *Eimeria maxima* | Eimeriidae | Eucoccidiorida | Conoidasida | AAGGAGGAGACAAT | ACACAT | pacbio |
| *Eimeria tenella* | Eimeriidae | Eucoccidiorida | Conoidasida | AAACCCT |  | assembly |
| *Eratigena atrica* | Agelenidae | Araneae | Arachnida | ACACAC | ATATAT | pacbio |
| *Amaurobius ferox* | Amaurobiidae | Araneae | Arachnida | ATATAT | ATATATAT | pacbio |
| *Amaurobius similis* | Amaurobiidae | Araneae | Arachnida | ACACAC | ACACACAC | pacbio |
| *Araneus angulatus* | Araneidae | Araneae | Arachnida | ACAGACAG | AACCAACC | pacbio |
| *Araneus diadematus* | Araneidae | Araneae | Arachnida | AATAT |  | pacbio |
| *Argiope bruennichi* | Araneidae | Araneae | Arachnida | ACACAC | AGATAGAT | pacbio |
| *Gibbaranea gibbosa* | Araneidae | Araneae | Arachnida | ACACAC | ACAGACAG | pacbio |
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
| *Scytodes thoracica* | Scytodidae | Araneae | Arachnida | ACATG | AAATTGTCTAATAAT | pacbio |
| *Segestria senoculata* | Segestriidae | Araneae | Arachnida | ACTCACTC | ACTCACTCACTC | pacbio |
| *Meta bourneti* | Tetragnathidae | Araneae | Arachnida | ACCTACCT | ACATACAT | pacbio |
| *Metellina segmentata* | Tetragnathidae | Araneae | Arachnida | AACTTGT | ACTATGG | pacbio |
| *Enoplognatha latimana* | Theridiidae | Araneae | Arachnida | AAAGC | ACACAC | pacbio |
| *Enoplognatha ovata* | Theridiidae | Araneae | Arachnida | ACACAC | ACACACAC | pacbio |
| *Steatoda bipunctata* | Theridiidae | Araneae | Arachnida |  |  | pacbio |
| *Misumena vatia* | Thomisidae | Araneae | Arachnida | ACACAC | ACATACAT | pacbio |
| *Xysticus cristatus* | Thomisidae | Araneae | Arachnida | ACACAC | ACACACAC | pacbio |
| *Uloborus plumipes* | Uloboridae | Araneae | Arachnida | ACACAC | ATATAT | pacbio |
| *Zoropsis spinimana* | Zoropsidae | Araneae | Arachnida | ATATAT | ATATATAT | pacbio |
| *Odiellus spinosus* | Phalangiidae | Opiliones | Arachnida | ACGAG | AACCT | pacbio |
| *Euscorpius flavicaudis* | Euscorpiidae | Scorpiones | Arachnida | AACCT | AACCTAACCT | pacbio |
| *Stigmatogaster subterranea* | Himantariidae | Geophilomorpha | Chilopoda | AACCT | AACCTAACCT | pacbio |
| *Lithobius forficatus* | Lithobiidae | Lithobiomorpha | Chilopoda | AAAGTCG | AAAGTCGAAAGTCG | pacbio |
| *Lithobius melanops* | Lithobiidae | Lithobiomorpha | Chilopoda | AACCT | AACCTAACCT | pacbio |
| *Lithobius muticus* | Lithobiidae | Lithobiomorpha | Chilopoda | AACCT | AAATC | pacbio |
| *Lithobius piceus* | Lithobiidae | Lithobiomorpha | Chilopoda | AACCT | AACCTAACCT | pacbio |
| *Lithobius variegatus* | Lithobiidae | Lithobiomorpha | Chilopoda | AACCT | AACCTAACCT | pacbio |
| *Allacma fusca* | Sminthuridae | Symphypleona | Collembola | AAACTTGGAATT | AAACTTGGAATTAAACTTGGAATT | pacbio |
| *Glomeris marginata* | Glomeridae | Glomerida | Diplopoda | AACCT | AAGTGTCCG | pacbio |
| *Apoderus coryli* | Attelabidae | Coleoptera | Insecta | AACCC | AACCCAACCC | assembly |
| *Apoderus coryli* | Attelabidae | Coleoptera | Insecta | AAATAATT |  | pacbio |
| *Attelabus nitens* | Attelabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cantharis rufa* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cantharis rustica* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Cantharis rustica* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Podabrus alpinus* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Rhagonycha fulva* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Rhagonycha fulva* | Cantharidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agonum fuliginosum* | Carabidae | Coleoptera | Insecta | ACACAC | ACACAT | pacbio |
| *Demetrias atricapillus* | Carabidae | Coleoptera | Insecta | ACATACAT | ACATACATACAT | pacbio |
| *Dromius quadrimaculatus* | Carabidae | Coleoptera | Insecta |  |  | pacbio |
| *Harpalus rufipes* | Carabidae | Coleoptera | Insecta | ACATACAT | ACACAC | pacbio |
| *Leistus spinibarbis* | Carabidae | Coleoptera | Insecta |  |  | pacbio |
| *Nebria brevicollis* | Carabidae | Coleoptera | Insecta | AAATAACT | AAACATAC | pacbio |
| *Nebria salina* | Carabidae | Coleoptera | Insecta | AAATAACT | AAACTAACT | pacbio |
| *Notiophilus biguttatus* | Carabidae | Coleoptera | Insecta | AGATATAT | AGATATATAGATATAT | pacbio |
| *Ophonus ardosiacus* | Carabidae | Coleoptera | Insecta | ACATACAT | ACATACATACAT | pacbio |
| *Pterostichus madidus* | Carabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pterostichus madidus* | Carabidae | Coleoptera | Insecta | AATAAT | ATCCATCC | pacbio |
| *Pterostichus strenuus* | Carabidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Clytus arietis* | Cerambycidae | Coleoptera | Insecta | AATAAT | AATAATAAT | pacbio |
| *Rutpela maculata* | Cerambycidae | Coleoptera | Insecta | AATAAT | ACACAC | pacbio |
| *Chrysolina oricalcia* | Chrysomelidae | Coleoptera | Insecta | ATCCATCC | ATCCATCCATCC | pacbio |
| *Cryptocephalus moraei* | Chrysomelidae | Coleoptera | Insecta |  |  | pacbio |
| *Gastrophysa viridula* | Chrysomelidae | Coleoptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Lilioceris lilii* | Chrysomelidae | Coleoptera | Insecta | ACACAC | AAACG | pacbio |
| *Oulema melanopus* | Chrysomelidae | Coleoptera | Insecta | ACAGACTG | ACAGACAGACTG | pacbio |
| *Adalia bipunctata* | Coccinellidae | Coleoptera | Insecta | AAAAATTC | AACCT | assembly |
| *Adalia bipunctata* | Coccinellidae | Coleoptera | Insecta | AACCT |  | pacbio |
| *Adalia decempunctata* | Coccinellidae | Coleoptera | Insecta | AAGTC | ACATC | pacbio |
| *Anatis ocellata* | Coccinellidae | Coleoptera | Insecta | AACCT | ACACTG | pacbio |
| *Calvia quattuordecimguttata* | Coccinellidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Chilocorus renipustulatus* | Coccinellidae | Coleoptera | Insecta | ACTCTG | AAATATT | pacbio |
| *Coccinella septempunctata* | Coccinellidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Coccinella septempunctata* | Coccinellidae | Coleoptera | Insecta | AAGTCG | AACCT | pacbio |
| *Halyzia sedecimguttata* | Coccinellidae | Coleoptera | Insecta | AACTCC | AACTCCAACTCC | pacbio |
| *Harmonia axyridis* | Coccinellidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Harmonia axyridis* | Coccinellidae | Coleoptera | Insecta | AACCT |  | pacbio |
| *Hippodamia variegata* | Coccinellidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Propylea quattuordecimpunctata* | Coccinellidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Subcoccinella vigintiquattuorpunctata* | Coccinellidae | Coleoptera | Insecta | AACAT | AACATAACAT | pacbio |
| *Curculio glandium* | Curculionidae | Coleoptera | Insecta | AACCC | AGATAGAT | pacbio |
| *Limnobaris t-album* | Curculionidae | Coleoptera | Insecta | ATATAT | ACACAC | pacbio |
| *Otiorhynchus atroapterus* | Curculionidae | Coleoptera | Insecta | AGATAGAT | AGATAGATAGAT | pacbio |
| *Otiorhynchus sulcatus* | Curculionidae | Coleoptera | Insecta | AAATAAAT | AAATAAATAAAT | pacbio |
| *Philopedon plagiatum* | Curculionidae | Coleoptera | Insecta | AGGATG | AGGATGAGGATG | pacbio |
| *Polydrusus cervinus* | Curculionidae | Coleoptera | Insecta | AACAGACCCG | AAATGC | pacbio |
| *Rhinocyllus conicus* | Curculionidae | Coleoptera | Insecta | AGATAGAT | AGATAGATAGAT | pacbio |
| *Agriotes lineatus* | Elateridae | Coleoptera | Insecta | AAAGGTCACC | AAGCC | pacbio |
| *Agrypnus murinus* | Elateridae | Coleoptera | Insecta | AACCT | AAACTAT | pacbio |
| *Denticollis linearis* | Elateridae | Coleoptera | Insecta | AAAGGAC | AACCT | pacbio |
| *Peltodytes caesus* | Haliplidae | Coleoptera | Insecta | AAAAATAC |  | pacbio |
| *Hydrobius fuscipes* | Hydrophilidae | Coleoptera | Insecta |  |  | pacbio |
| *Sinodendron cylindricum* | Lucanidae | Coleoptera | Insecta | AATAAT | ACTACT | pacbio |
| *Platycis minutus* | Lycidae | Coleoptera | Insecta | AACCT | AGATAGAT | pacbio |
| *Malachius bipustulatus* | Melyridae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | assembly |
| *Malachius bipustulatus* | Melyridae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Oedemera lurida* | Oedemeridae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Oedemera nobilis* | Oedemeridae | Coleoptera | Insecta | ACTATG | ACTATGACTATG | pacbio |
| *Oedemera virescens* | Oedemeridae | Coleoptera | Insecta | AACCCAGACCT | AACCCAGACCTAACCCAGACCT | pacbio |
| *Pyrochroa serraticornis* | Pyrochroidae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | assembly |
| *Pyrochroa serraticornis* | Pyrochroidae | Coleoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Melolontha melolontha* | Scarabaeidae | Coleoptera | Insecta | AAGTAATC | AAAGAT | pacbio |
| *Phosphuga atrata* | Silphidae | Coleoptera | Insecta | AAGACAGAC | ACAGACTAG | pacbio |
| *Anotylus rugosus* | Staphylinidae | Coleoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ocypus olens* | Staphylinidae | Coleoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ocypus olens* | Staphylinidae | Coleoptera | Insecta | AACCT |  | pacbio |
| *Philonthus cognatus* | Staphylinidae | Coleoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Lagria hirta* | Tenebrionidae | Coleoptera | Insecta | ATCATC | ACAGACAG | pacbio |
| *Forficula auricularia* | Forficulidae | Dermaptera | Insecta | AAAAA | AAAAAA | pacbio |
| *Acrocera orbiculus* | Acroceridae | Diptera | Insecta |  |  | pacbio |
| *Anthomyia liturata* | Anthomyiidae | Diptera | Insecta | AAGATAGAT | AGATAGAT | pacbio |
| *Anthomyia pluvialis* | Anthomyiidae | Diptera | Insecta | ACATACAT | AGATAGAT | pacbio |
| *Delia platura* | Anthomyiidae | Diptera | Insecta | ACAGACAG | AAGTGTATGGC | pacbio |
| *Hylemya vagans* | Anthomyiidae | Diptera | Insecta | AAAATAT | AAATTAT | pacbio |
| *Hylemya variata* | Anthomyiidae | Diptera | Insecta | ACTAT | ACTATACTAT | pacbio |
| *Leucophora obtusa* | Anthomyiidae | Diptera | Insecta | AAATAAAT | AAATAAATAAAT | pacbio |
| *Leucophora personata* | Anthomyiidae | Diptera | Insecta | AAATAAAT | ACAGACAG | pacbio |
| *Choerades marginata* | Asilidae | Diptera | Insecta |  |  | pacbio |
| *Dioctria rufipes* | Asilidae | Diptera | Insecta | AAAGGCG | AAAGGCGAAAGGCG | pacbio |
| *Dysmachus trigonus* | Asilidae | Diptera | Insecta |  |  | pacbio |
| *Machimus atricapillus* | Asilidae | Diptera | Insecta | ACAGACAG | AATAC | pacbio |
| *Bibio marci* | Bibionidae | Diptera | Insecta |  |  | assembly |
| *Bibio marci* | Bibionidae | Diptera | Insecta |  |  | pacbio |
| *Bombylius discolor* | Bombyliidae | Diptera | Insecta |  |  | pacbio |
| *Bombylius major* | Bombyliidae | Diptera | Insecta | ACTACT | AATAAT | pacbio |
| *Villa modesta* | Bombyliidae | Diptera | Insecta | AATAAT | CCCCC | pacbio |
| *Bellardia pandia* | Calliphoridae | Diptera | Insecta | AATAAT | AATAATAAT | assembly |
| *Bellardia pandia* | Calliphoridae | Diptera | Insecta | ACATAT | AAATT | pacbio |
| *Calliphora vicina* | Calliphoridae | Diptera | Insecta | AACAGAACTAG | AACTAGAACTG | pacbio |
| *Calliphora vomitoria* | Calliphoridae | Diptera | Insecta | AACAGAACTAG | AGATAGAT | pacbio |
| *Lucilia richardsi* | Calliphoridae | Diptera | Insecta | AGATAGAT | ACATACAT | pacbio |
| *Melinda gentilis* | Calliphoridae | Diptera | Insecta | ATCATC | ATCATCATC | pacbio |
| *Melinda viridicyanea* | Calliphoridae | Diptera | Insecta | AATGTATGT | AATGTATGTAATGTATGT | pacbio |
| *Protocalliphora azurea* | Calliphoridae | Diptera | Insecta | AGATAT | ACATAT | pacbio |
| *Clusia tigrina* | Clusiidae | Diptera | Insecta | ATATAT | ATATATATATATAT | assembly |
| *Clusia tigrina* | Clusiidae | Diptera | Insecta |  |  | pacbio |
| *Conops quadrifasciatus* | Conopidae | Diptera | Insecta | AAAAT | AAATT | pacbio |
| *Myopa tessellatipennis* | Conopidae | Diptera | Insecta | ACGCATG | ACTCT | pacbio |
| *Physocephala rufipes* | Conopidae | Diptera | Insecta | ACAGACAG | AAAGACAAGAC | pacbio |
| *Sicus ferrugineus* | Conopidae | Diptera | Insecta | AAGTC | AAGTCAAGTC | assembly |
| *Sicus ferrugineus* | Conopidae | Diptera | Insecta | AAGTC | AAGTCAAGTC | pacbio |
| *Thecophora atra* | Conopidae | Diptera | Insecta | AACCAGCACACG |  | pacbio |
| *Empis livida* | Empididae | Diptera | Insecta |  |  | pacbio |
| *Fannia serena* | Fanniidae | Diptera | Insecta |  |  | pacbio |
| *Sapromyzosoma quadripunctata* | Lauxaniidae | Diptera | Insecta | AAAAAC | AAAAACAAAAAC | pacbio |
| *Tricholauxania praeusta* | Lauxaniidae | Diptera | Insecta | AACTCACTC | AATAAT | pacbio |
| *Coenosia intermedia* | Muscidae | Diptera | Insecta | ACATATC | AACAAC | pacbio |
| *Hebecnema nigricolor* | Muscidae | Diptera | Insecta | ACATAT | ACATATACATAT | pacbio |
| *Helina depuncta* | Muscidae | Diptera | Insecta | AAATAAAT | AAAGTT | pacbio |
| *Helina evecta* | Muscidae | Diptera | Insecta | AAAGTT | AACATT | pacbio |
| *Helina quadrum* | Muscidae | Diptera | Insecta | AGATGAT | AATAG | pacbio |
| *Hydrotaea cyrtoneurina* | Muscidae | Diptera | Insecta | AATACT | AAATTAAT | pacbio |
| *Lophosceles cinereiventris* | Muscidae | Diptera | Insecta | AAATG | AAATCTGAAATG | pacbio |
| *Mesembrina meridiana* | Muscidae | Diptera | Insecta | AAATAACT | ACAGACTG | pacbio |
| *Morellia simplex* | Muscidae | Diptera | Insecta | AATAAT | AAATAT | pacbio |
| *Musca autumnalis* | Muscidae | Diptera | Insecta | AAAATAT | AAAAT | pacbio |
| *Myospila meditabunda* | Muscidae | Diptera | Insecta | AATTAC | AATTACAATTAC | pacbio |
| *Phaonia pallida* | Muscidae | Diptera | Insecta | AATTC | AATTCAATTC | pacbio |
| *Phaonia rufiventris* | Muscidae | Diptera | Insecta | AAGTC | AAGTCAAGTC | pacbio |
| *Phaonia tuguriorum* | Muscidae | Diptera | Insecta | AAATAAAT | AAATAAATAAAT | pacbio |
| *Polietes meridionalis* | Muscidae | Diptera | Insecta | AAATGAAT | AAATGAATAAATGAAT | pacbio |
| *Thricops semicinereus* | Muscidae | Diptera | Insecta | ACAGACGG | ACAGACGGACAGACGG | pacbio |
| *Callomyia amoena* | Platypezidae | Diptera | Insecta | AAATG | AACAAC | pacbio |
| *Pollenia amentaria* | Polleniidae | Diptera | Insecta | AATGAT | AATGATAATGAT | pacbio |
| *Pollenia angustigena* | Polleniidae | Diptera | Insecta | ACATACAT | ACATACATACAT | pacbio |
| *Psila merdaria* | Psilidae | Diptera | Insecta | AATAG | AATACC | pacbio |
| *Rhagio annulatus* | Rhagionidae | Diptera | Insecta | AATAAT | AAATAAAT | pacbio |
| *Rhagio tringarius* | Rhagionidae | Diptera | Insecta | AAAATAAAT | AAATAAAT | pacbio |
| *Stomorhina lunata* | Rhiniidae | Diptera | Insecta | AACTAGAACTG | AACAGAACTAG | pacbio |
| *Phyto melanocephala* | Rhinophoridae | Diptera | Insecta | AAATT | AACAT | pacbio |
| *Rhinophora lepida* | Rhinophoridae | Diptera | Insecta | ACATACAT | ACATAT | pacbio |
| *Blaesoxipha plumicornis* | Sarcophagidae | Diptera | Insecta | AAAAC | AAAACAAAAC | pacbio |
| *Sarcophaga caerulescens* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | assembly |
| *Sarcophaga caerulescens* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga carnaria* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga crassimargo* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga haemorrhoa* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga rosellei* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga subvicina* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Sarcophaga variegata* | Sarcophagidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Scathophaga stercoraria* | Scathophagidae | Diptera | Insecta | AAGAAT | AAATC | pacbio |
| *Coremacera marginata* | Sciomyzidae | Diptera | Insecta | AAAAT | AAAATAAAAT | assembly |
| *Coremacera marginata* | Sciomyzidae | Diptera | Insecta | AAATT | AAGAAT | pacbio |
| *Dichetophora obliterata* | Sciomyzidae | Diptera | Insecta |  |  | pacbio |
| *Euthycera fumigata* | Sciomyzidae | Diptera | Insecta | AGATAT | AATATG | pacbio |
| *Hydromya dorsalis* | Sciomyzidae | Diptera | Insecta | AAATT | AAAATT | pacbio |
| *Pherbellia cinerella* | Sciomyzidae | Diptera | Insecta |  |  | pacbio |
| *Pherbina coryleti* | Sciomyzidae | Diptera | Insecta | AACATC | AGAGAT | pacbio |
| *Chloromyia formosa* | Stratiomyidae | Diptera | Insecta | ACAGACAG | ACAGACAGACAG | pacbio |
| *Nemotelus nigrinus* | Stratiomyidae | Diptera | Insecta | AGATAGAT | AGATAGATAGAT | pacbio |
| *Oplodontha viridula* | Stratiomyidae | Diptera | Insecta | ATATAT | ATATATAT | pacbio |
| *Oxycera rara* | Stratiomyidae | Diptera | Insecta | AACCCT | CCCCC | pacbio |
| *Pachygaster atra* | Stratiomyidae | Diptera | Insecta | ACAGACGG | AACGAATG | pacbio |
| *Stratiomys potamida* | Stratiomyidae | Diptera | Insecta | AATACAG | AAAGTAAGTCTCTGT | pacbio |
| *Stratiomys singularior* | Stratiomyidae | Diptera | Insecta | AATCATC | AATCATCAATCATC | pacbio |
| *Baccha elongata* | Syrphidae | Diptera | Insecta | AACAAC | ACATGTC | pacbio |
| *Brachypalpus laphriformis* | Syrphidae | Diptera | Insecta | ACTACT | AAATAAAT | pacbio |
| *Cheilosia illustrata* | Syrphidae | Diptera | Insecta | AACAAC | AACAACAAC | pacbio |
| *Cheilosia pagana* | Syrphidae | Diptera | Insecta |  |  | pacbio |
| *Cheilosia soror* | Syrphidae | Diptera | Insecta |  |  | pacbio |
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
| *Dasysyrphus albostriatus* | Syrphidae | Diptera | Insecta | AACAAC | AACAACAAC | pacbio |
| *Dasysyrphus tricinctus* | Syrphidae | Diptera | Insecta | AACATGC | AACATGCAACATGC | pacbio |
| *Epistrophe grossulariae* | Syrphidae | Diptera | Insecta | ACAGTG | AAATT | pacbio |
| *Epistrophella euchroma* | Syrphidae | Diptera | Insecta | AAAAT | AAAGT | pacbio |
| *Episyrphus balteatus* | Syrphidae | Diptera | Insecta | AATAG | AAATT | pacbio |
| *Eristalinus sepulchralis* | Syrphidae | Diptera | Insecta | AATAAT | AAATAAT | pacbio |
| *Eristalis arbustorum* | Syrphidae | Diptera | Insecta | AGCTATG | ATATAT | assembly |
| *Eristalis arbustorum* | Syrphidae | Diptera | Insecta | AATAAT | AAATAAAT | pacbio |
| *Eristalis horticola* | Syrphidae | Diptera | Insecta | AACATGC | AAGCATC | pacbio |
| *Eristalis pertinax* | Syrphidae | Diptera | Insecta | AACTG | AAACAAAT | assembly |
| *Eristalis pertinax* | Syrphidae | Diptera | Insecta | AAATAC | AAGAAT | pacbio |
| *Eristalis tenax* | Syrphidae | Diptera | Insecta | AAGAAT | AAGAATAAGAAT | assembly |
| *Eristalis tenax* | Syrphidae | Diptera | Insecta | AAGAAT | ACCATCC | pacbio |
| *Eumerus sabulonum* | Syrphidae | Diptera | Insecta |  |  | pacbio |
| *Eupeodes corollae* | Syrphidae | Diptera | Insecta | ACTATC | AATGAT | pacbio |
| *Eupeodes latifasciatus* | Syrphidae | Diptera | Insecta | ACCATG | ATCATC | assembly |
| *Eupeodes latifasciatus* | Syrphidae | Diptera | Insecta | ACCATG | AATAG | pacbio |
| *Eupeodes luniger* | Syrphidae | Diptera | Insecta | ACCATC | AATGAT | pacbio |
| *Ferdinandea cuprea* | Syrphidae | Diptera | Insecta | AACAAC | AACAACAAC | pacbio |
| *Helophilus pendulus* | Syrphidae | Diptera | Insecta | AATAAT | AACAAT | pacbio |
| *Leucozona laternaria* | Syrphidae | Diptera | Insecta | AATAG | AACAAC | pacbio |
| *Melangyna umbellatarum* | Syrphidae | Diptera | Insecta | AAATT | AAGAGTGT | pacbio |
| *Melanostoma mellinum* | Syrphidae | Diptera | Insecta | AACAAC | AACAACAAC | assembly |
| *Melanostoma mellinum* | Syrphidae | Diptera | Insecta | AACAAC | AACAACAAC | pacbio |
| *Melanostoma scalare* | Syrphidae | Diptera | Insecta | AATAAT | AACAAC | pacbio |
| *Myathropa florea* | Syrphidae | Diptera | Insecta | AGCCAGCC | AAATACAT | pacbio |
| *Paragus haemorrhous* | Syrphidae | Diptera | Insecta | AATAAT | ATCATC | pacbio |
| *Platycheirus albimanus* | Syrphidae | Diptera | Insecta | ACGTAG | ACACAC | assembly |
| *Platycheirus albimanus* | Syrphidae | Diptera | Insecta | ACGTAG | ACACAC | pacbio |
| *Platycheirus scutatus* | Syrphidae | Diptera | Insecta |  |  | pacbio |
| *Rhingia campestris* | Syrphidae | Diptera | Insecta | ACCATCT | AAATATAG | pacbio |
| *Scaeva pyrastri* | Syrphidae | Diptera | Insecta |  |  | assembly |
| *Scaeva pyrastri* | Syrphidae | Diptera | Insecta | AACTT | AATAG | pacbio |
| *Sphaerophoria scripta* | Syrphidae | Diptera | Insecta | AACTT | AATAAT | pacbio |
| *Sphaerophoria taeniata* | Syrphidae | Diptera | Insecta | ATCATC | AAAAA | pacbio |
| *Syritta pipiens* | Syrphidae | Diptera | Insecta | ACACAT |  | assembly |
| *Syritta pipiens* | Syrphidae | Diptera | Insecta | ATCATC | ACACAT | pacbio |
| *Syrphus ribesii* | Syrphidae | Diptera | Insecta | AACAAC | ATGCCC | pacbio |
| *Volucella inanis* | Syrphidae | Diptera | Insecta | ACAGGTG | AAATAAC | assembly |
| *Volucella inanis* | Syrphidae | Diptera | Insecta | AAATAAC | AAATAAT | pacbio |
| *Volucella inflata* | Syrphidae | Diptera | Insecta | AATAAT |  | assembly |
| *Volucella inflata* | Syrphidae | Diptera | Insecta | AATAAT |  | pacbio |
| *Volucella pellucens* | Syrphidae | Diptera | Insecta | AATAAT | AATAATAAT | pacbio |
| *Xanthogramma pedissequum* | Syrphidae | Diptera | Insecta | ACAGACTG | AATAG | assembly |
| *Xanthogramma pedissequum* | Syrphidae | Diptera | Insecta | ACAGACTG | ATCATC | pacbio |
| *Xylota sylvarum* | Syrphidae | Diptera | Insecta | AGGATG | AGGATGAGGATG | assembly |
| *Xylota sylvarum* | Syrphidae | Diptera | Insecta | ACTGACTG | AGGATG | pacbio |
| *Tabanus autumnalis* | Tabanidae | Diptera | Insecta | ATCATC | ACACAC | pacbio |
| *Tabanus bromius* | Tabanidae | Diptera | Insecta | AAAACAT | ATCATC | pacbio |
| *Actia lamia* | Tachinidae | Diptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Cistogaster globosa* | Tachinidae | Diptera | Insecta | AATAT | AATAAT | pacbio |
| *Epicampocera succincta* | Tachinidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Eriothrix rufomaculata* | Tachinidae | Diptera | Insecta | ACATAT | ACATATACATAT | pacbio |
| *Gymnocheta viridis* | Tachinidae | Diptera | Insecta | ATCATC | ATCATCATC | pacbio |
| *Gymnosoma rotundatum* | Tachinidae | Diptera | Insecta | AAAAAAAATT | AATAAT | assembly |
| *Gymnosoma rotundatum* | Tachinidae | Diptera | Insecta | AATAAT | ACTAT | pacbio |
| *Linnaemya tessellans* | Tachinidae | Diptera | Insecta | AAAAA | AAAAAA | pacbio |
| *Lypha dubia* | Tachinidae | Diptera | Insecta | AATAG | AATAAT | pacbio |
| *Nowickia ferox* | Tachinidae | Diptera | Insecta | AATGAT | ACATAT | pacbio |
| *Phasia hemiptera* | Tachinidae | Diptera | Insecta | AATAGT | AATAGTAATAGT | pacbio |
| *Phasia obesa* | Tachinidae | Diptera | Insecta | ACATAT | AAATT | pacbio |
| *Tachina fera* | Tachinidae | Diptera | Insecta | ACTAT | ACTATACTAT | assembly |
| *Tachina fera* | Tachinidae | Diptera | Insecta | AATAG | AATAGAATAG | pacbio |
| *Tachina grossa* | Tachinidae | Diptera | Insecta | ACATAT | AATAG | pacbio |
| *Tachina lurida* | Tachinidae | Diptera | Insecta | ACATAT | AATAG | pacbio |
| *Thecocarcelia acutangulata* | Tachinidae | Diptera | Insecta | AATCAT | AATGAT | assembly |
| *Thecocarcelia acutangulata* | Tachinidae | Diptera | Insecta | AATCAT | AATCATAATCAT | pacbio |
| *Anomoia purmunda* | Tephritidae | Diptera | Insecta | AATGAT | AATAAT | pacbio |
| *Merzomyia westermanni* | Tephritidae | Diptera | Insecta | AAAAG | AAAGT | pacbio |
| *Tephritis neesii* | Tephritidae | Diptera | Insecta | AAAAT | AAGACC | pacbio |
| *Terellia serratulae* | Tephritidae | Diptera | Insecta | AATAAT | AAAAAT | pacbio |
| *Nephrotoma appendiculata* | Tipulidae | Diptera | Insecta | AAAATATG | ACACAC | pacbio |
| *Nephrotoma flavescens* | Tipulidae | Diptera | Insecta | AAAATATG | AAGTAAT | pacbio |
| *Nephrotoma flavipalpis* | Tipulidae | Diptera | Insecta | AGATAT | AAATAAATT | pacbio |
| *Tipula paludosa* | Tipulidae | Diptera | Insecta | AGATATAT | AGATAT | pacbio |
| *Tipula vernalis* | Tipulidae | Diptera | Insecta | AAAATGT | ACCATC | pacbio |
| *Herina lugubris* | Ulidiidae | Diptera | Insecta | AAATT | AATAAT | pacbio |
| *Cloeon dipterum* | Baetidae | Ephemeroptera | Insecta |  |  | pacbio |
| *Ecdyonurus torrentis* | Heptageniidae | Ephemeroptera | Insecta |  |  | pacbio |
| *Rhithrogena germanica* | Heptageniidae | Ephemeroptera | Insecta |  |  | pacbio |
| *Rhithrogena semicolorata* | Heptageniidae | Ephemeroptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Acanthosoma haemorrhoidale* | Acanthosomatidae | Hemiptera | Insecta | AAACCACCCT |  | pacbio |
| *Elasmostethus interstinctus* | Acanthosomatidae | Hemiptera | Insecta | AAACCACCCT | AGATAGAT | pacbio |
| *Elasmucha grisea* | Acanthosomatidae | Hemiptera | Insecta |  |  | pacbio |
| *Aphelocheirus aestivalis* | Aphelocheiridae | Hemiptera | Insecta | ACAGAGAGGC | AATAT | pacbio |
| *Cercopis vulnerata* | Cercopidae | Hemiptera | Insecta | ACACAC | AACCT | pacbio |
| *Anoscopus histrionicus* | Cicadellidae | Hemiptera | Insecta | AATATAG | AATGG | pacbio |
| *Aphrodes makarovi* | Cicadellidae | Hemiptera | Insecta | AAGAAT | AAGAATAAGAAT | pacbio |
| *Ledra aurita* | Cicadellidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mocydia crocea* | Cicadellidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Opsius stactogalus* | Cicadellidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cixius nervosus* | Cixiidae | Hemiptera | Insecta | AAAATTGTTGATGGAGATCATAC | AACCT | pacbio |
| *Tachycixius pilosus* | Cixiidae | Hemiptera | Insecta | AACCT | AAAAAA | pacbio |
| *Coreus marginatus* | Coreidae | Hemiptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Gonocerus acuteangulatus* | Coreidae | Hemiptera | Insecta |  |  | pacbio |
| *Leptoglossus occidentalis* | Coreidae | Hemiptera | Insecta | ACACAC | AACCACCCCT | pacbio |
| *Canthophorus impressus* | Cydnidae | Hemiptera | Insecta | AAAAA | AAAAAA | pacbio |
| *Legnotus limbosus* | Cydnidae | Hemiptera | Insecta | AAATAACT | AAATAACTAAATAACT | pacbio |
| *Tritomegas bicolor* | Cydnidae | Hemiptera | Insecta | ACACAC | ACACACACAC | pacbio |
| *Stenocranus minutus* | Delphacidae | Hemiptera | Insecta | AACCT | ATCATC | pacbio |
| *Issus coleoptratus* | Issidae | Hemiptera | Insecta | AACCT | ACACAC | pacbio |
| *Kleidocerys resedae* | Lygaeidae | Hemiptera | Insecta | AATAC | ACTCTGAG | pacbio |
| *Centrotus cornutus* | Membracidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Closterotomus trivialis* | Miridae | Hemiptera | Insecta | ACCGAG | AACCATCCCT | pacbio |
| *Grypocoris stysi* | Miridae | Hemiptera | Insecta | AACCATCCCT | AACCATCCCTAACCATCCCT | pacbio |
| *Lygus pratensis* | Miridae | Hemiptera | Insecta | AACACTCCCT |  | pacbio |
| *Pantilius tunicatus* | Miridae | Hemiptera | Insecta |  |  | pacbio |
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
| *Pentatoma rufipes* | Pentatomidae | Hemiptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Plea minutissima* | Pleidae | Hemiptera | Insecta | AAGAATATAGAAT | AAGAATATAGAATAAGAATATAGAAT | pacbio |
| *Planococcus citri* | Pseudococcidae | Hemiptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Corizus hyoscyami* | Rhopalidae | Hemiptera | Insecta | AACCATCCCT | ACAGACAG | pacbio |
| *Rhopalus parumpunctatus* | Rhopalidae | Hemiptera | Insecta | ACACAC | AAGCAT | pacbio |
| *Rhopalus subrufus* | Rhopalidae | Hemiptera | Insecta | ACTCACTC | ACTCACTCACTCACTC | pacbio |
| *Drymus ryeii* | Rhyparochromidae | Hemiptera | Insecta | AACCTACCT | AACCATCCCT | pacbio |
| *Rhyparochromus vulgaris* | Rhyparochromidae | Hemiptera | Insecta | AACCATCCCT | AATAAT | pacbio |
| *Andrena bucephala* | Andrenidae | Hymenoptera | Insecta | ACCAGTG | AAAATAATTG | pacbio |
| *Andrena dorsata* | Andrenidae | Hymenoptera | Insecta |  |  | pacbio |
| *Andrena fulva* | Andrenidae | Hymenoptera | Insecta | AAACG | AATGGT | pacbio |
| *Andrena haemorrhoa* | Andrenidae | Hymenoptera | Insecta | AAACGAGTC | AACGAGTCG | assembly |
| *Andrena haemorrhoa* | Andrenidae | Hymenoptera | Insecta | AACGAGTCG | AAACGAGTC | pacbio |
| *Andrena hattorfiana* | Andrenidae | Hymenoptera | Insecta | AAAAAC | ACGACG | pacbio |
| *Andrena helvola* | Andrenidae | Hymenoptera | Insecta | AACGAC | AAGGGTGAAGGGTGT | pacbio |
| *Andrena minutula* | Andrenidae | Hymenoptera | Insecta |  |  | pacbio |
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
| *Bombus pascuorum* | Apidae | Hymenoptera | Insecta | AAAAAC | AAAAACGAAAAC | assembly |
| *Bombus pascuorum* | Apidae | Hymenoptera | Insecta | AAAACG | AACCCCAACCT | pacbio |
| *Bombus pratorum* | Apidae | Hymenoptera | Insecta | AACGAACG | AACCCCAACCT | pacbio |
| *Bombus rupestris* | Apidae | Hymenoptera | Insecta | AACCCCAACCT | AACTG | pacbio |
| *Bombus sylvestris* | Apidae | Hymenoptera | Insecta | AACCCGAACCT | AACGTAT | assembly |
| *Bombus sylvestris* | Apidae | Hymenoptera | Insecta | AACCCGAACCT |  | pacbio |
| *Bombus terrestris* | Apidae | Hymenoptera | Insecta | AACGTAT | AACCCCAACCT | assembly |
| *Bombus terrestris* | Apidae | Hymenoptera | Insecta | AACCCCAACCT | AACCT | pacbio |
| *Nomada fabriciana* | Apidae | Hymenoptera | Insecta | AACCT |  | assembly |
| *Nomada fabriciana* | Apidae | Hymenoptera | Insecta |  |  | pacbio |
| *Nomada ferruginata* | Apidae | Hymenoptera | Insecta | AGCCG | AAGTAAGT | pacbio |
| *Nomada flava* | Apidae | Hymenoptera | Insecta | ATCATC | ATCATCATC | pacbio |
| *Nomada lathburiana* | Apidae | Hymenoptera | Insecta | AAACCTAACCC | AAACCTAACCCAAACCTAACCC | pacbio |
| *Nomada ruficornis* | Apidae | Hymenoptera | Insecta | AAACCTAACC | AAACCTAACCAAACCTAACC | pacbio |
| *Chalcis sispes* | Chalcididae | Hymenoptera | Insecta | ACGATG | ATCATC | pacbio |
| *Hylaeus communis* | Colletidae | Hymenoptera | Insecta |  |  | pacbio |
| *Cerceris rybyensis* | Crabronidae | Hymenoptera | Insecta | AACCCAGACCT | AAAAT | assembly |
| *Cerceris rybyensis* | Crabronidae | Hymenoptera | Insecta | AACCCAGACCT | ACCACT | pacbio |
| *Crossocerus megacephalus* | Crabronidae | Hymenoptera | Insecta | ACTGACTG | ACTGACTGACTG | pacbio |
| *Ectemnius continuus* | Crabronidae | Hymenoptera | Insecta |  |  | assembly |
| *Ectemnius continuus* | Crabronidae | Hymenoptera | Insecta |  |  | pacbio |
| *Ectemnius lituratus* | Crabronidae | Hymenoptera | Insecta | AACCCAGACCT |  | assembly |
| *Ectemnius lituratus* | Crabronidae | Hymenoptera | Insecta | ACTCACTC |  | pacbio |
| *Mimumesa dahlbomi* | Crabronidae | Hymenoptera | Insecta | ACCTG | ACCTGACCTG | assembly |
| *Mimumesa dahlbomi* | Crabronidae | Hymenoptera | Insecta |  |  | pacbio |
| *Nysson spinosus* | Crabronidae | Hymenoptera | Insecta | AACCCAGACCT | AACAT | assembly |
| *Nysson spinosus* | Crabronidae | Hymenoptera | Insecta | AACCCAGACCT |  | pacbio |
| *Pemphredon lugubris* | Crabronidae | Hymenoptera | Insecta |  |  | pacbio |
| *Trypoxylon clavicerum* | Crabronidae | Hymenoptera | Insecta |  |  | pacbio |
| *Lasius niger* | Formicidae | Hymenoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Myrmica ruginodis* | Formicidae | Hymenoptera | Insecta | AACCT | AGCAGC | pacbio |
| *Lasioglossum calceatum* | Halictidae | Hymenoptera | Insecta | AACGTAT | AACGTAC | pacbio |
| *Lasioglossum lativentre* | Halictidae | Hymenoptera | Insecta | AATAT | AACCCAGACCT | assembly |
| *Lasioglossum lativentre* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | ACAGACAG | pacbio |
| *Lasioglossum leucozonium* | Halictidae | Hymenoptera | Insecta |  |  | pacbio |
| *Lasioglossum malachurum* | Halictidae | Hymenoptera | Insecta | ACATCGT | AATGAATG | pacbio |
| *Lasioglossum morio* | Halictidae | Hymenoptera | Insecta | AACGTAT | AACGCAT | assembly |
| *Lasioglossum morio* | Halictidae | Hymenoptera | Insecta | AACGTAT | AACGCAT | pacbio |
| *Lasioglossum pauxillum* | Halictidae | Hymenoptera | Insecta | AGCAGC | AACCT | pacbio |
| *Seladonia tumulorum* | Halictidae | Hymenoptera | Insecta | AACCCT | AACCCTAACCCT | assembly |
| *Seladonia tumulorum* | Halictidae | Hymenoptera | Insecta |  |  | pacbio |
| *Sphecodes crassus* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | AACCCAGACCTAACCCAGACCT | pacbio |
| *Sphecodes ephippius* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | AGAGATATG | pacbio |
| *Sphecodes hyalinatus* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | AGATATG | pacbio |
| *Sphecodes monilicornis* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | AATATACTAG | assembly |
| *Sphecodes monilicornis* | Halictidae | Hymenoptera | Insecta | AACCCAGACCT | AGATAT | pacbio |
| *Alloplasta piceator* | Ichneumonidae | Hymenoptera | Insecta | ACGACG | ATCATC | pacbio |
| *Amblyjoppa proteus* | Ichneumonidae | Hymenoptera | Insecta | ACACGC | ACGAGG | pacbio |
| *Amblyteles armatorius* | Ichneumonidae | Hymenoptera | Insecta | ACGACG | ATCATC | pacbio |
| *Buathra laborator* | Ichneumonidae | Hymenoptera | Insecta |  |  | pacbio |
| *Ichneumon xanthorius* | Ichneumonidae | Hymenoptera | Insecta | ACGATG | AACGAC | assembly |
| *Ichneumon xanthorius* | Ichneumonidae | Hymenoptera | Insecta | AACGAC | ACGATG | pacbio |
| *Netelia dilatata* | Ichneumonidae | Hymenoptera | Insecta | AAAAT | AAAATAAAT | pacbio |
| *Ophion luteus* | Ichneumonidae | Hymenoptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Polysphincta tuberosa* | Ichneumonidae | Hymenoptera | Insecta | AAACAC | ACACAG | pacbio |
| *Scambus nigricans* | Ichneumonidae | Hymenoptera | Insecta | ACACAC | ACACAG | pacbio |
| *Megachile ligniseca* | Megachilidae | Hymenoptera | Insecta | ACAGAG | AACCT | pacbio |
| *Megachile willughbiella* | Megachilidae | Hymenoptera | Insecta | ACAGAG | AACCT | pacbio |
| *Stelis phaeoptera* | Megachilidae | Hymenoptera | Insecta | AAAGGC | AACCCT | pacbio |
| *Macropis europaea* | Melittidae | Hymenoptera | Insecta | AACCC |  | assembly |
| *Macropis europaea* | Melittidae | Hymenoptera | Insecta |  |  | pacbio |
| *Melitta haemorrhoidalis* | Melittidae | Hymenoptera | Insecta | AACCCAGACCT | AACCCAGACCTAACCCAGACCT | pacbio |
| *Anoplius nigerrimus* | Pompilidae | Hymenoptera | Insecta | AACCCAGACCT | AAAAA | assembly |
| *Anoplius nigerrimus* | Pompilidae | Hymenoptera | Insecta |  |  | pacbio |
| *Evagetes crassicornis* | Pompilidae | Hymenoptera | Insecta | AACCCAGACCT |  | pacbio |
| *Ammophila pubescens* | Sphecidae | Hymenoptera | Insecta | AACTCACT | ACAGAG | pacbio |
| *Athalia circularis* | Tenthredinidae | Hymenoptera | Insecta | ACGACG | ACGACGACG | pacbio |
| *Athalia cordata* | Tenthredinidae | Hymenoptera | Insecta |  |  | pacbio |
| *Athalia rosae* | Tenthredinidae | Hymenoptera | Insecta | AAAAA | AAAAAA | pacbio |
| *Macrophya alboannulata* | Tenthredinidae | Hymenoptera | Insecta | ACCTG | ACCTGACCTG | pacbio |
| *Phymatocera aterrima* | Tenthredinidae | Hymenoptera | Insecta | AACCT | AAGGG | pacbio |
| *Rhogogaster chlorosoma* | Tenthredinidae | Hymenoptera | Insecta | AACCT | AACGAC | pacbio |
| *Tenthredo distinguenda* | Tenthredinidae | Hymenoptera | Insecta | ACTCTG | ACTCTGACTCTG | pacbio |
| *Tenthredo livida* | Tenthredinidae | Hymenoptera | Insecta | AACCT |  | pacbio |
| *Tenthredo mesomela* | Tenthredinidae | Hymenoptera | Insecta | AGGGATATC | AATGCAG | pacbio |
| *Tenthredo notha* | Tenthredinidae | Hymenoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Tenthredo notha* | Tenthredinidae | Hymenoptera | Insecta |  |  | pacbio |
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
| *Nematopogon swammerdamellus* | Adelidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Argyresthia goedartella* | Argyresthiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Batrachedra praeangusta* | Batrachedridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Blastobasis adustella* | Blastobasidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Blastobasis adustella* | Blastobasidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Blastobasis lacticolella* | Blastobasidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Blastobasis lacticolella* | Blastobasidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Zeuzera pyrina* | Cossidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Zeuzera pyrina* | Cossidae | Lepidoptera | Insecta | AACCT | AACAAC | pacbio |
| *Acentria ephemerella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agriphila geniculea* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agriphila geniculea* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agriphila straminella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agriphila tristella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agriphila tristella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Calamotropha paludella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Calamotropha paludella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Catoptria pinella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Chrysoteuchia culmella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Chrysoteuchia culmella* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cydalima perspectalis* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Elophila nymphaeata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eudonia lacustrata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Evergestis limbata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Nymphula nitidulata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ostrinia nubilalis* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Parapoynx stratiotata* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Parapoynx stratiotata* | Crambidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Patania ruralis* | Crambidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Udea prunalis* | Crambidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Agonopterix arenella* | Depressariidae | Lepidoptera | Insecta | AACCT | AGGAT | pacbio |
| *Agonopterix heracliana* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agonopterix ocellana* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agonopterix subpropinquella* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agonopterix subpropinquella* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Carcina quercana* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Carcina quercana* | Depressariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Drepana falcataria* | Drepanidae | Lepidoptera | Insecta |  |  | pacbio |
| *Habrosyne pyritoides* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Habrosyne pyritoides* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thyatira batis* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Thyatira batis* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Watsonalla binaria* | Drepanidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Watsonalla cultraria* | Drepanidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Atolmis rubricollis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Catocala fraxini* | Erebidae | Lepidoptera | Insecta |  |  | pacbio |
| *Cybosia mesomella* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eilema depressum* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eilema depressum* | Erebidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Eilema griseolum* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Euclidia mi* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Euproctis similis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Euproctis similis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Herminia grisealis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Herminia tarsipennalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hypena proboscidalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hypena proboscidalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Laspeyria flexula* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Laspeyria flexula* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lygephila pastinum* | Erebidae | Lepidoptera | Insecta | AACCATCCCT | AACCATCCCTAACCATCCCT | pacbio |
| *Lymantria monacha* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Lymantria monacha* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Macrochilo cribrumalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Miltochrista miniata* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Orgyia antiqua* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Orgyia antiqua* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Phragmatobia fuliginosa* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Schrankia costaestrigalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Schrankia costaestrigalis* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Scoliopteryx libatrix* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Spilarctia lutea* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Spilarctia lutea* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Spilosoma lubricipeda* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Spilosoma lubricipeda* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thumatha senex* | Erebidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Athrips mouffetella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AAATG | pacbio |
| *Psoricoptera gibbosella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Recurvaria leucatella* | Gelechiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acasis viretata* | Geometridae | Lepidoptera | Insecta | ACACCT | AACCT | pacbio |
| *Agriopis aurantiaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agriopis aurantiaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agriopis marginaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Alsophila aescularia* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apeira syringaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Aplocera efformata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Aplocera efformata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Biston betularia* | Geometridae | Lepidoptera | Insecta | AACCT | ACCTACCT | assembly |
| *Biston betularia* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Campaea margaritaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Campaea margaritaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Camptogramma bilineatum* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Chloroclysta siterata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Chloroclystis v-ata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Colostygia pectinataria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Colotois pennaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Crocallis elinguaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Crocallis elinguaria* | Geometridae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Dysstroma truncata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ecliptopera silaceata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ectropis crepuscularia* | Geometridae | Lepidoptera | Insecta |  |  | pacbio |
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
| *Eupithecia abbreviata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eupithecia centaureata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eupithecia dodoneata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eupithecia tripunctaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eupithecia vulgata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Gymnoscelis rufifasciata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hydriomena furcata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hydriomena furcata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hylaea fasciaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hylaea fasciaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Idaea aversata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Idaea aversata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ligdia adustata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lobophora halterata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Lomaspilis marginata* | Geometridae | Lepidoptera | Insecta | AACGTGAT | AATAGAT | pacbio |
| *Macaria notata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Macaria notata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Operophtera brumata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Operophtera fagata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Opisthograptis luteolata* | Geometridae | Lepidoptera | Insecta | AACCT | AAATAG | pacbio |
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
| *Thera britannica* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Theria primaria* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xanthorhoe fluctuata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xanthorhoe quadrifasciata* | Geometridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hepialus humuli* | Hepialidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Korscheltellus lupulinus* | Hepialidae | Lepidoptera | Insecta | AACCT | AACCG | pacbio |
| *Triodia sylvina* | Hepialidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Carterocephalus palaemon* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Erynnis tages* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Erynnis tages* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hesperia comma* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hesperia comma* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ochlodes sylvanus* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ochlodes sylvanus* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pyrgus malvae* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pyrgus malvae* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thymelicus lineola* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thymelicus sylvestris* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Thymelicus sylvestris* | Hesperiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Incurvaria masculella* | Incurvariidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Poecilocampa populi* | Lasiocampidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apoda limacodes* | Limacodidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Aricia agestis* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Aricia agestis* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
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
| *Polyommatus icarus* | Lycaenidae | Lepidoptera | Insecta | AACTCG | AACCT | pacbio |
| *Satyrium w-album* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Thecla betulae* | Lycaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Micropterix aruncella* | Micropterigidae | Lepidoptera | Insecta | AAGACGGTAAGTGTGTATGTATGT | AACCT | pacbio |
| *Mompha ochraceella* | Momphidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Abrostola tripartita* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Abrostola tripartita* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Abrostola triplasia* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acronicta aceris* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Acronicta aceris* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acronicta psi* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acronicta rumicis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agrochola circellaris* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agrochola circellaris* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Agrochola macilenta* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Agrochola macilenta* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Agrotis puta* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Allophyes oxyacanthae* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Amphipoea oculea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Amphipyra berbera* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Amphipyra berbera* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Amphipyra tragopoginis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Amphipyra tragopoginis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Anaplectoides prasina* | Noctuidae | Lepidoptera | Insecta | AACCT | AAAAGTC | pacbio |
| *Anorthoa munda* | Noctuidae | Lepidoptera | Insecta | AACCT | ACCCTACCT | pacbio |
| *Apamea monoglypha* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Apamea monoglypha* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Apamea scolopacina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apamea sordens* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Aporophyla lueneburgensis* | Noctuidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Arenostola phragmitidis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Atethmia centrago* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Atethmia centrago* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Autographa gamma* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Autographa gamma* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Autographa pulchrina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Autographa pulchrina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Axylia putris* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Brachylomia viminalis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Caradrina clavipalpis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Caradrina kadenii* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Charanyca ferruginea* | Noctuidae | Lepidoptera | Insecta | AACCT | ACACCTACCCT | pacbio |
| *Charanyca trigrammica* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Colocasia coryli* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cosmia pyralina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cosmia trapezina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Cosmia trapezina* | Noctuidae | Lepidoptera | Insecta |  |  | pacbio |
| *Craniophora ligustri* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Craniophora ligustri* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Diachrysia chrysitis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Diarsia rubi* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Dryobotodes eremita* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Dryobotodes eremita* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Euplexia lucipara* | Noctuidae | Lepidoptera | Insecta | AACCT | AAATG | assembly |
| *Euplexia lucipara* | Noctuidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Eupsilia transversa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Eupsilia transversa* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Fissipunctia ypsillon* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Globia sparganii* | Noctuidae | Lepidoptera | Insecta |  |  | pacbio |
| *Griposia aprilina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Griposia aprilina* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hecatera dysodea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hecatera dysodea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hoplodrina octogenaria* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hydraecia micacea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hydraecia micacea* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Lacanobia wlatinum* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Luperina testacea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Luperina testacea* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mamestra brassicae* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mamestra brassicae* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mesoligia furuncula* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mesoligia furuncula* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Mythimna albipuncta* | Noctuidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Mythimna ferrago* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mythimna ferrago* | Noctuidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Mythimna impura* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mythimna impura* | Noctuidae | Lepidoptera | Insecta | AACCT | ACCTACCT | pacbio |
| *Noctua comes* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Noctua fimbriata* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Noctua fimbriata* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Noctua janthe* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Noctua janthe* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Noctua pronuba* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Noctua pronuba* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Ochropleura plecta* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ochropleura plecta* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Omphaloscelis lunosa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Omphaloscelis lunosa* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Orthosia cerasi* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Orthosia gothica* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Phlogophora meticulosa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Phlogophora meticulosa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Photedes minima* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Protodeltote pygarga* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Shargacucullia verbasci* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Tholera decimalis* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xestia c-nigrum* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Xestia c-nigrum* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Xestia sexstrigata* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xestia triangulum* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Xestia xanthographa* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Xestia xanthographa* | Noctuidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Xylocampa areola* | Noctuidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Bena bicolorana* | Nolidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Meganola albula* | Nolidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Nola cucullatella* | Nolidae | Lepidoptera | Insecta | AACCT | ACACAC | pacbio |
| *Nycteola revayana* | Nolidae | Lepidoptera | Insecta | AAACCACCCT | AAACCACCCTAAACCACCCT | pacbio |
| *Pseudoips prasinana* | Nolidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Clostera curtula* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Clostera curtula* | Notodontidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
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
| *Emmelina monodactyla* | Pterophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Emmelina monodactyla* | Pterophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Marasmarcha lunaedactyla* | Pterophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Marasmarcha lunaedactyla* | Pterophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Stenoptilia bipunctidactyla* | Pterophoridae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acrobasis consociella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acrobasis repandana* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acrobasis suavella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Elegia similella* | Pyralidae | Lepidoptera | Insecta |  |  | pacbio |
| *Endotricha flammealis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Endotricha flammealis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hypsopygia costalis* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hypsopygia glaucinalis* | Pyralidae | Lepidoptera | Insecta | AACCT | AAATG | pacbio |
| *Myelois circumvoluta* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Phycita roborella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Plodia interpunctella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Sciota angustella* | Pyralidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hamearis lucina* | Riodinidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Bembecia ichneumoniformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Bembecia ichneumoniformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Sesia apiformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Sesia apiformis* | Sesiidae | Lepidoptera | Insecta | AACCT |  | pacbio |
| *Sesia bembeciformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Synanthedon andrenaeformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Synanthedon formicaeformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Synanthedon myopaeformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Synanthedon vespiformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Synanthedon vespiformis* | Sesiidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Deilephila porcellus* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Deilephila porcellus* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hemaris fuciformis* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hemaris fuciformis* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Laothoe populi* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Laothoe populi* | Sphingidae | Lepidoptera | Insecta | ACAGACAG | AACCT | pacbio |
| *Mimas tiliae* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Mimas tiliae* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Sphinx pinastri* | Sphingidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Morophaga choragella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Tinea semifulvella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Tinea semifulvella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Tinea trinotella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Tinea trinotella* | Tineidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris cristana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris emargana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Acleris emargana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris kochiella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris literana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris rhombana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Acleris sparsana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Acleris sparsana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Apotomis betuletana* | Tortricidae | Lepidoptera | Insecta | AACCT | ACAGGC | pacbio |
| *Apotomis turbidana* | Tortricidae | Lepidoptera | Insecta | AACCT | ACTGATAGAT | assembly |
| *Apotomis turbidana* | Tortricidae | Lepidoptera | Insecta | AACCT | AGATAGAT | pacbio |
| *Archips podanus* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Archips xylosteana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Clepsis spectrana* | Tortricidae | Lepidoptera | Insecta |  |  | pacbio |
| *Cochylimorpha straminea* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cydia fagiglandana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Cydia splendana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Cydia splendana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ditula angustiorana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Epagoge grotiana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Epinotia brunnichana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Epinotia demarniana* | Tortricidae | Lepidoptera | Insecta |  |  | pacbio |
| *Epinotia nisella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Epinotia ramella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eucosma campoliliana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eucosma cana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Eudemis profundana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Hedya salicella* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Hedya salicella* | Tortricidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Lozotaeniodes formosana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Neocochylis molliculana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Notocelia uddmanniana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Notocelia uddmanniana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pammene aurita* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pammene fasciana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Pammene fasciana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pammene regiana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pandemis cinnamomeana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Pandemis corylana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ptycholomoides aeriferana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Rhopobota naevana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Zeiraphera isertana* | Tortricidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Yponomeuta cagnagella* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Yponomeuta plumbellus* | Yponomeutidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Yponomeuta sedellus* | Yponomeutidae | Lepidoptera | Insecta | AACCT | ACAGACAG | pacbio |
| *Ypsolopha alpella* | Ypsolophidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ypsolopha parenthesella* | Ypsolophidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ypsolopha scabrella* | Ypsolophidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Ypsolopha scabrella* | Ypsolophidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Ypsolopha sequella* | Ypsolophidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Zygaena filipendulae* | Zygaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Zygaena filipendulae* | Zygaenidae | Lepidoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Sialis lutaria* | Sialidae | Megaloptera | Insecta | AACCT |  | pacbio |
| *Chrysoperla carnea* | Chrysopidae | Neuroptera | Insecta | AACCC | AACCCAACCC | assembly |
| *Chrysoperla carnea* | Chrysopidae | Neuroptera | Insecta | AACCC |  | pacbio |
| *Drepanepteryx phalaenoides* | Hemerobiidae | Neuroptera | Insecta | AACCTAACCT | AACCT | pacbio |
| *Aeshna mixta* | Aeshnidae | Odonata | Insecta | ATATAT | ATATATAT | pacbio |
| *Coenagrion puella* | Coenagrionidae | Odonata | Insecta | AGCCATCGCCAT | AGCCATCGCCATAGCCATCGCCAT | pacbio |
| *Enallagma cyathigerum* | Coenagrionidae | Odonata | Insecta | ACACAC | ACACACAC | pacbio |
| *Ischnura elegans* | Coenagrionidae | Odonata | Insecta | AGATC |  | assembly |
| *Ischnura elegans* | Coenagrionidae | Odonata | Insecta | AACCC |  | pacbio |
| *Chalcolestes viridis* | Lestidae | Odonata | Insecta | AACCC | ACACAC | pacbio |
| *Libellula quadrimaculata* | Libellulidae | Odonata | Insecta | ACACAC | AACAG | pacbio |
| *Sympetrum striolatum* | Libellulidae | Odonata | Insecta | ACACAC | ACTCACTC | pacbio |
| *Platycnemis pennipes* | Platycnemididae | Odonata | Insecta |  |  | pacbio |
| *Chorthippus albomarginatus* | Acrididae | Orthoptera | Insecta | AACCT | AACTTG | pacbio |
| *Chorthippus brunneus* | Acrididae | Orthoptera | Insecta | AACCT | ACACAG | pacbio |
| *Chorthippus parallelus* | Acrididae | Orthoptera | Insecta | AACCT |  | pacbio |
| *Gomphocerippus rufus* | Acrididae | Orthoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Teleogryllus oceanicus* | Gryllidae | Orthoptera | Insecta | AACCT | ACTACT | pacbio |
| *Meconema thalassinum* | Tettigoniidae | Orthoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Chloroperla tripunctata* | Chloroperlidae | Plecoptera | Insecta | ACTACT | AGATAGAT | pacbio |
| *Leuctra nigra* | Leuctridae | Plecoptera | Insecta | AACCT |  | pacbio |
| *Nemoura dubitans* | Nemouridae | Plecoptera | Insecta | ATCATC | ATCATCATC | assembly |
| *Nemoura dubitans* | Nemouridae | Plecoptera | Insecta | AACCT | AGAGC | pacbio |
| *Nemurella pictetii* | Nemouridae | Plecoptera | Insecta | AGCAGC | AACCT | assembly |
| *Nemurella pictetii* | Nemouridae | Plecoptera | Insecta | AACCT | AAGTAG | pacbio |
| *Isoperla grammatica* | Perlodidae | Plecoptera | Insecta | AAATAAAT | AACCT | pacbio |
| *Brachyptera putata* | Taeniopterygidae | Plecoptera | Insecta | ATATAT | ATATATATAT | assembly |
| *Brachyptera risi* | Taeniopterygidae | Plecoptera | Insecta | ATATAT | ATATATAT | pacbio |
| *Xanthostigma xanthostigma* | Raphidiidae | Raphidioptera | Insecta | AAGACAGT | AAGACAGTAAGACAGT | pacbio |
| *Silo pallipes* | Goeridae | Trichoptera | Insecta | ATATAT | ATATATAT | pacbio |
| *Hydropsyche siltalai* | Hydropsychidae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Anabolia nervosa* | Limnephilidae | Trichoptera | Insecta | AATGACAGCG | ACTACT | pacbio |
| *Chaetopteryx villosa* | Limnephilidae | Trichoptera | Insecta |  |  | pacbio |
| *Glyphotaelius pellucidus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACTT | pacbio |
| *Limnephilus lunatus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Limnephilus lunatus* | Limnephilidae | Trichoptera | Insecta | AACCT |  | pacbio |
| *Limnephilus marmoratus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACCTAACCT | assembly |
| *Limnephilus marmoratus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Limnephilus rhombicus* | Limnephilidae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Odontocerum albicorne* | Odontoceridae | Trichoptera | Insecta | ATATAT | ATATATAT | pacbio |
| *Polycentropus irroratus* | Polycentropodidae | Trichoptera | Insecta | AACCT | AACCTAACCT | pacbio |
| *Sericostoma personatum* | Sericostomatidae | Trichoptera | Insecta | ACACAC | ACACACAC | pacbio |
| *Chelura terebrans* | Cheluridae | Amphipoda | Malacostraca |  |  | pacbio |
| *Crangonyx pseudogracilis* | Crangonyctidae | Amphipoda | Malacostraca |  |  | pacbio |
| *Cancer pagurus* | Cancridae | Decapoda | Malacostraca | AACCT | ACAGACAG | pacbio |
| *Pagurus bernhardus* | Paguridae | Decapoda | Malacostraca | AACCT | AACCTAACCT | pacbio |
| *Pisidia longicornis* | Porcellanidae | Decapoda | Malacostraca | AACCT | AACCTAACCT | pacbio |
| *Porcellana platycheles* | Porcellanidae | Decapoda | Malacostraca | AACCT | AAAGTTCCTCG | pacbio |
| *Xantho hydrophilus* | Xanthidae | Decapoda | Malacostraca | AACCT | ACACAC | pacbio |
| *Asellus aquaticus* | Asellidae | Isopoda | Malacostraca |  |  | pacbio |
| *Idotea granulosa* | Idoteidae | Isopoda | Malacostraca | ATATAT | AGATAGATAT | pacbio |
| *Oniscus asellus* | Oniscidae | Isopoda | Malacostraca | ATATAT | ATATATAT | pacbio |
| *Philoscia muscorum* | Philosciidae | Isopoda | Malacostraca |  |  | pacbio |
| *Porcellio spinicornis* | Porcellionidae | Isopoda | Malacostraca | AGGATG | ACTCTG | pacbio |
| *Clistosaccus paguri* | Clistosaccidae |  | Thecostraca | ACACAC | ACACACAC | pacbio |
| *Sacculina carcini* | Sacculinidae |  | Thecostraca | AACCT | AACCTAACCT | assembly |
| *Sacculina carcini* | Sacculinidae |  | Thecostraca | AAAATAAAG | ACACAC | pacbio |
| *Scalpellum scalpellum* | Scalpellidae |  | Thecostraca | AAGTCT | AAATACACATAACT | pacbio |
| *Perforatus perforatus* | Balanidae | Balanomorpha | Thecostraca | AACCT | AACCTAACCT | pacbio |
| *Semibalanus balanoides* | Balanidae | Balanomorpha | Thecostraca | AACCT | ACACAC | pacbio |
| *Epicoccum nigrum* | Didymellaceae | Pleosporales | Dothideomycetes |  |  | pacbio |
| *Cladonia squamosa* | Cladoniaceae | Lecanorales | Lecanoromycetes |  |  | pacbio |
| *Platismatia glauca* | Parmeliaceae | Lecanorales | Lecanoromycetes |  |  | pacbio |
| *Metschnikowia zobellii* | Metschnikowiaceae | Saccharomycetales | Saccharomycetes |  |  | pacbio |
| *Trichoderma pseudokoningii* | Hypocreaceae | Hypocreales | Sordariomycetes | CCCCC | CCCCCC | pacbio |
| *Chaetoceros curvisetus* | Chaetocerotaceae | Chaetocerotales | Coscinodiscophyceae | ACCCT | ACCCTACCCT | pacbio |
| *Agaricus bisporus* | Agaricaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Agaricus bisporus* | Agaricaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Agaricus bisporus* | Agaricaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Agaricus bisporus* | Agaricaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Agaricus bisporus* | Agaricaceae | Agaricales | Agaricomycetes |  |  | pacbio |
| *Leucocybe candicans* | Lyophyllaceae | Agaricales | Agaricomycetes |  |  | pacbio |
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
| *Laetiporus sulphureus* | Laetiporaceae | Polyporales | Agaricomycetes | CCCCC | CCCCCCC | pacbio |
| *Laetiporus sulphureus* | Laetiporaceae | Polyporales | Agaricomycetes | CCCCC | CCCCCCC | pacbio |
| *Hericium coralloides* | Hericiaceae | Russulales | Agaricomycetes |  |  | pacbio |
| *Bugulina stolonifera* | Bugulidae | Cheilostomatida | Gymnolaemata | ACAGT | AAACCCC | pacbio |
| *Cryptosula pallasiana* | Cryptosulidae | Cheilostomatida | Gymnolaemata | ACTACT | ATCATC | pacbio |
| *Membranipora membranacea* | Membraniporidae | Cheilostomatida | Gymnolaemata | AAACCCC | AACCCCG | assembly |
| *Membranipora membranacea* | Membraniporidae | Cheilostomatida | Gymnolaemata | AAATAAAT | ACCACC | pacbio |
| *Watersipora subatra* | Watersiporidae | Cheilostomatida | Gymnolaemata | AAGTCT | AAGTCTAAGTCT | pacbio |
| *Pycnococcus provasolii* | Pycnococcaceae |  |  |  |  | pacbio |
| *Tetraselmis chuii* | Chlorodendraceae | Chlorodendrales | Chlorodendrophyceae |  |  | pacbio |
| *Brachiomonas submarina* | Chlamydomonadaceae | Chlamydomonadales | Chlorophyceae | AAGGATGGAC | ACAGACAG | pacbio |
| *Dunaliella primolecta* | Dunaliellaceae | Chlamydomonadales | Chlorophyceae | AACCCT | AACCCTAACCCT | assembly |
| *Dunaliella primolecta* | Dunaliellaceae | Chlamydomonadales | Chlorophyceae | ACACACAC | ACACAC | pacbio |
| *Hydrodictyon reticulatum* | Hydrodictyaceae | Sphaeropleales | Chlorophyceae | ACACAC | ACAGACAG | pacbio |
| *Coelastrum microporum* | Scenedesmaceae | Sphaeropleales | Chlorophyceae |  |  | pacbio |
| *Chloroidium saccharophilum* |  |  | Trebouxiophyceae |  |  | pacbio |
| *Telmatherina bonti* | Telmatherinidae | Atheriniformes | Actinopteri | ACCAG | AACCCT | pacbio |
| *Lipophrys pholis* | Blenniidae | Blenniiformes | Actinopteri | AGATAGAT | AACCCT | pacbio |
| *Trachurus trachurus* | Carangidae | Carangiformes | Actinopteri | AAAAA | AACCCT | assembly |
| *Trachurus trachurus* | Carangidae | Carangiformes | Actinopteri |  |  | pacbio |
| *Barbus barbus* | Cyprinidae | Cypriniformes | Actinopteri | AACCCT | ACACAC | pacbio |
| *Danio rerio* | Danionidae | Cypriniformes | Actinopteri | AACCCT | AGATAGAT | pacbio |
| *Taurulus bubalis* | Cottidae | Perciformes | Actinopteri | AACCCT | AACCCTAACCCT | assembly |
| *Taurulus bubalis* | Cottidae | Perciformes | Actinopteri | AACCCT | ACACAC | pacbio |
| *Pholis gunnellus* | Pholidae | Perciformes | Actinopteri | AACCCT | AACCCTAACCCT | assembly |
| *Pholis gunnellus* | Pholidae | Perciformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Salmo trutta* | Salmonidae | Salmoniformes | Actinopteri | ACACAC | AACCCT | assembly |
| *Salmo trutta* | Salmonidae | Salmoniformes | Actinopteri | AACCCT | AACCCTAACCCT | pacbio |
| *Thunnus albacares* | Scombridae | Scombriformes | Actinopteri | AACCCT | ACACAC | pacbio |
| *Bufo bufo* | Bufonidae | Anura | Amphibia | AACCCT | AACCCTAACCCT | assembly |
| *Rana temporaria* | Ranidae | Anura | Amphibia |  |  | assembly |
| *Aplidium turbinatum* | Polyclinidae | Aplousobranchia | Ascidiacea | AACCCT | AACCCTAACCCT | assembly |
| *Aplidium turbinatum* | Polyclinidae | Aplousobranchia | Ascidiacea | AACCCT | AACCCTAACCCT | pacbio |
| *Ascidia mentula* | Ascidiidae | Phlebobranchia | Ascidiacea | AACCCT | AACCCTAACCCT | pacbio |
| *Styela clava* | Styelidae | Stolidobranchia | Ascidiacea | AACCCT | AACCCTAACCCT | pacbio |
| *Accipiter gentilis* | Accipitridae | Accipitriformes | Aves | AACCCT | AACCCTAACCCT | pacbio |
| *Caprimulgus europaeus* | Caprimulgidae | Caprimulgiformes | Aves | AACCCT | AACCCTAACCCT | assembly |
| *Streptopelia turtur* | Columbidae | Columbiformes | Aves |  |  | assembly |
| *Erithacus rubecula* | Turdidae | Passeriformes | Aves | AAGGAAGG | AGAGG | assembly |
| *Phaethon aethereus* | Phaethontidae | Pelecaniformes | Aves | AACCCT | AACCCTAACCCT | pacbio |
| *Calonectris borealis* | Procellariidae | Procellariiformes | Aves | AACCCT | CCCCC | pacbio |
| *Scyliorhinus canicula* | Scyliorhinidae | Carcharhiniformes | Chondrichthyes | AACCCT | AGATAGAT | assembly |
| *Cervus elaphus* | Cervidae | Artiodactyla | Mammalia | AAAAA | AAAAAA | assembly |
| *Cervus elaphus* | Cervidae | Artiodactyla | Mammalia | AAAAA | AAAAAA | pacbio |
| *Orcinus orca* | Delphinidae | Artiodactyla | Mammalia | AACCCT |  | pacbio |
| *Canis lupus* | Canidae | Carnivora | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Canis lupus* | Canidae | Carnivora | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Lutra lutra* | Mustelidae | Carnivora | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Meles meles* | Mustelidae | Carnivora | Mammalia |  |  | assembly |
| *Meles meles* | Mustelidae | Carnivora | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Pipistrellus pipistrellus* | Vespertilionidae | Chiroptera | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Sorex araneus* | Soricidae | Eulipotyphla | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Homo sapiens* | Hominidae | Primates | Mammalia | AATGG | AACCCT | pacbio |
| *Arvicola amphibius* | Cricetidae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Myodes glareolus* | Cricetidae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Apodemus flavicollis* | Muridae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Apodemus sylvaticus* | Muridae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Mus musculus* | Muridae | Rodentia | Mammalia | AACCCTAACCCT | AACCCT | pacbio |
| *Rattus norvegicus* | Muridae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Rattus norvegicus* | Muridae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | pacbio |
| *Sciurus vulgaris* | Sciuridae | Rodentia | Mammalia | AACCCT | AACCCTAACCCT | assembly |
| *Actinia fragacea* | Actiniidae | Actiniaria | Anthozoa | AACCCT | ATCATC | pacbio |
| *Diadumene lineata* | Diadumenidae | Actiniaria | Anthozoa | AACCCT | AACCCTAACCCT | assembly |
| *Diadumene lineata* | Diadumenidae | Actiniaria | Anthozoa | AACCCT | AAGAGTGT | pacbio |
| *Nematostella vectensis* | Edwardsiidae | Actiniaria | Anthozoa | AACCCT | ACCATC | pacbio |
| *Haliclystus octoradiatus* | Haliclystidae | Stauromedusae | Staurozoa | AATAAT | AATAATAAT | assembly |
| *Haliclystus octoradiatus* | Haliclystidae | Stauromedusae | Staurozoa | AATAAT | ACTAT | pacbio |
| *Asterias rubens* | Asteriidae | Forcipulatida | Asteroidea | AACCCT | AACCCTAACCCT | assembly |
| *Marthasterias glacialis* | Asteriidae | Forcipulatida | Asteroidea | AACCCT | AACCCTAACCCT | assembly |
| *Marthasterias glacialis* | Asteriidae | Forcipulatida | Asteroidea | AACCCT | AAAGGAC | pacbio |
| *Antedon bifida* | Antedonidae | Comatulida | Crinoidea | AACCCT | AACAAC | pacbio |
| *Echinus esculentus* | Echinidae | Camarodonta | Echinoidea | AACCCT | AACCCTAACCCT | pacbio |
| *Ophiopholis aculeata* | Ophiactidae | Amphilepidida | Ophiuroidea | AACCCT | AACCCTAACCCT | pacbio |
| *Ophiocomina nigra* | Ophiocomidae | Amphilepidida | Ophiuroidea | AACCCT | AACCCTAACCCT | pacbio |
| *Ophiura albida* | Ophiuridae | Amphilepidida | Ophiuroidea | AACCCT | AACCCTAACCCT | pacbio |
| *Euglenaria anabaena* | Euglenaceae | Euglenales | Euglenida | AACCCT | AACCCTAACCCT | pacbio |
| *Chrysotila carterae* | Isochrysidaceae | Isochrysidales |  | AACCCT |  | pacbio |
| *Diacronema lutheri* | Pavlovaceae | Pavlovales |  | ACACAC | ACACACAC | pacbio |
| *Tetramitus jugosus* | Vahlkampfiidae |  |  | AAACCC | CCCCC | pacbio |
| *Cerastoderma edule* | Cardiidae | Cardiida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Gari tellinella* | Psammobiidae | Cardiida | Bivalvia | AACCCT | AACCCTAACCCT | assembly |
| *Gari tellinella* | Psammobiidae | Cardiida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Macomangulus tenuis* | Tellinidae | Cardiida | Bivalvia | AACCCT | AACATGGT | pacbio |
| *Magallana gigas* | Ostreidae | Ostreida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Mimachlamys varia* | Pectinidae | Pectinida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Pecten maximus* | Pectinidae | Pectinida | Bivalvia | CCCCC | AACCCT | assembly |
| *Spisula solida* | Mactridae | Venerida | Bivalvia | AACCCT | AACCCTAACCCT | pacbio |
| *Pisidium nitidum* | Sphaeriidae | Venerida | Bivalvia | ACTACT | ACTACTACT | pacbio |
| *Mysia undata* | Veneridae | Venerida | Bivalvia |  |  | pacbio |
| *Venerupis corrugata* | Veneridae | Venerida | Bivalvia | AACCCT | AATGAATG | pacbio |
| *Ancylus fluviatilis* | Ancylidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Testudinalia testudinalis* | Lottiidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Stagnicola fuscus* | Lymnaeidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Patella depressa* | Patellidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Patella pellucida* | Patellidae |  | Gastropoda | AACCCT | AACCCTAACCCT | assembly |
| *Patella pellucida* | Patellidae |  | Gastropoda | AACTCTCTACT | AACTCTACT | pacbio |
| *Patella ulyssiponensis* | Patellidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Patella vulgata* | Patellidae |  | Gastropoda |  |  | pacbio |
| *Physa fontinalis* | Physidae |  | Gastropoda | AACCCT | AGATAGAT | pacbio |
| *Physella acuta* | Physidae |  | Gastropoda | ATCATC | AGATAGAT | pacbio |
| *Anisus vortex* | Planorbidae |  | Gastropoda | AAGTAAGT | AAGTAAGTAAGT | pacbio |
| *Biomphalaria glabrata* | Planorbidae |  | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Planorbis planorbis* | Planorbidae |  | Gastropoda | AGATGGAT | AGATATAT | pacbio |
| *Valvata piscinalis* | Valvatidae |  | Gastropoda | AATACTAC | AATACTACAATACTAC | pacbio |
| *Theodoxus fluviatilis* | Neritidae | Cycloneritida | Gastropoda | ACACAC | AGATAGAT | pacbio |
| *Bithynia leachii* | Bithyniidae | Littorinimorpha | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Littorina obtusata* | Littorinidae | Littorinimorpha | Gastropoda | AACCCT | ACACAC | pacbio |
| *Trivia monacha* | Triviidae | Littorinimorpha | Gastropoda | ACACAC | ACACACAC | pacbio |
| *Nucella lapillus* | Muricidae | Neogastropoda | Gastropoda | ACACAC | ACTACT | pacbio |
| *Tritia reticulata* | Nassariidae | Neogastropoda | Gastropoda | ACTACT | AACCCT | pacbio |
| *Crimora papillata* |  | Nudibranchia | Gastropoda | ACTACT | ACTACTACT | pacbio |
| *Doris pseudoargus* | Dorididae | Nudibranchia | Gastropoda | AAACAC | AACCCT | pacbio |
| *Helicella itala* | Geomitridae | Stylommatophora | Gastropoda | ACTACT | ACTACTACT | pacbio |
| *Xeroplexa intersecta* | Geomitridae | Stylommatophora | Gastropoda | AACTAACT | AACTAACTAACT | pacbio |
| *Cepaea hortensis* | Helicidae | Stylommatophora | Gastropoda | ACTACT | AACCCT | pacbio |
| *Cepaea nemoralis* | Helicidae | Stylommatophora | Gastropoda | ACACAC | ACTACT | pacbio |
| *Cornu aspersum* | Helicidae | Stylommatophora | Gastropoda | ACTACT | AGATAGAT | pacbio |
| *Calliostoma zizyphinum* | Calliostomatidae | Trochida | Gastropoda | AACCCT | AAACCCT | pacbio |
| *Gibbula magus* | Trochidae | Trochida | Gastropoda | AACATG | AACCCT | pacbio |
| *Phorcus lineatus* | Trochidae | Trochida | Gastropoda | AACCCT | AAACAC | assembly |
| *Phorcus lineatus* | Trochidae | Trochida | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Steromphala cineraria* | Trochidae | Trochida | Gastropoda | AACCCT | AACCCTAACCCT | assembly |
| *Steromphala cineraria* | Trochidae | Trochida | Gastropoda | AACCCT | AACCCTAACCCT | pacbio |
| *Acanthochitona crinita* | Acanthochitonidae | Chitonida | Polyplacophora | AACCCT | AACAT | pacbio |
| *Mucor piriformis* | Mucoraceae | Mucorales | Mucoromycetes | AAAAA | CCCCC | pacbio |
| *Caenorhabditis monodelphis* | Rhabditidae | Rhabditida | Chromadorea | AAGCCT | AAGCCTAAGCCT | pacbio |
| *Dioctophyme renale* | Dioctophymatidae | Dioctophymatida | Enoplea | ACGATG | ATCATC | pacbio |
| *Lineus longissimus* | Lineidae | Heteronemertea | Pilidiophora | AACCCT | AACCCTAACCCT | assembly |
| *Lineus longissimus* | Lineidae | Heteronemertea | Pilidiophora | AACCCT | ATCATC | pacbio |
| *Ceramium secundatum* | Ceramiaceae | Ceramiales | Florideophyceae | AACAAC | AACAACAAC | pacbio |
| *Calliblepharis jubata* | Cystocloniaceae | Gigartinales | Florideophyceae | ATATAT | ATATATAT | pacbio |
| *Metacallophyllis laciniata* | Kallymeniaceae | Gigartinales | Florideophyceae | ACAGGCGTGCCC | AAGCGAGATGCAAGCGATGC | pacbio |
| *Palmaria palmata* | Palmariaceae | Palmariales | Florideophyceae | ACACTGAGT | ACAGGCGTGCCC | pacbio |
| *Hylocomiadelphus triquetrus* | Hylocomiaceae | Hypnales | Bryopsida | AACAG |  | pacbio |
| *Rhytidiadelphus loreus* | Hylocomiaceae | Hypnales | Bryopsida |  |  | pacbio |
| *Isothecium myosuroides* | Lembophyllaceae | Hypnales | Bryopsida | AAACCCT | AACCCT | pacbio |
| *Neckera pumila* | Neckeraceae | Hypnales | Bryopsida | AAACCCT | ACACAC | pacbio |
| *Thamnobryum alopecurum* | Neckeraceae | Hypnales | Bryopsida |  |  | pacbio |
| *Thuidium delicatulum* | Thuidiaceae | Hypnales | Bryopsida |  |  | pacbio |
| *Thuidium tamariscinum* | Thuidiaceae | Hypnales | Bryopsida |  |  | pacbio |
| *Huperzia selago* | Lycopodiaceae | Lycopodiales | Lycopodiopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Alisma plantago-aquatica* | Alismataceae | Alismatales | Magnoliopsida | ATCATC | AAACCCT | pacbio |
| *Aponogeton distachyos* | Aponogetonaceae | Alismatales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Arum maculatum* | Araceae | Alismatales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Butomus umbellatus* | Butomaceae | Alismatales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Angelica archangelica* | Apiaceae | Apiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Anthriscus sylvestris* | Apiaceae | Apiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Ligusticum scoticum* | Apiaceae | Apiales | Magnoliopsida |  |  | pacbio |
| *Smyrnium perfoliatum* | Apiaceae | Apiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Hedera helix* | Araliaceae | Apiales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Ilex aquifolium* | Aquifoliaceae | Aquifoliales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Allium ampeloprasum* | Amaryllidaceae | Asparagales | Magnoliopsida |  |  | pacbio |
| *Allium triquetrum* | Amaryllidaceae | Asparagales | Magnoliopsida | AACCGAGCCCAT | AACCGAGCCCATAACCGAGCCCAT | pacbio |
| *Narcissus pseudonarcissus* | Amaryllidaceae | Asparagales | Magnoliopsida | AACCCT | AACCCTAACCCT | pacbio |
| *Iris pseudacorus* | Iridaceae | Asparagales | Magnoliopsida | AACCCT | AACCCTAACCCT | pacbio |
| *Arctium minus* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Bellis perennis* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AGATAGAT | pacbio |
| *Chamaemelum nobile* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | ATATAT | pacbio |
| *Cicerbita muralis* | Asteraceae | Asterales | Magnoliopsida | ACATACAT | AAACCCT | pacbio |
| *Hypochaeris radicata* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Pulicaria dysenterica* | Asteraceae | Asterales | Magnoliopsida | AACAAC | AAACCCT | pacbio |
| *Senecio vulgaris* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Tanacetum vulgare* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | ATATAT | pacbio |
| *Tussilago farfara* | Asteraceae | Asterales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Jasione montana* | Campanulaceae | Asterales | Magnoliopsida | AACCCTG | AACCCCTG | pacbio |
| *Nymphoides peltata* | Menyanthaceae | Asterales | Magnoliopsida | AAACCCT |  | pacbio |
| *Borago officinalis* | Boraginaceae | Boraginales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Pentaglottis sempervirens* | Boraginaceae | Boraginales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Arabidopsis thaliana* | Brassicaceae | Brassicales | Magnoliopsida | AAACCCT | AACCT | pacbio |
| *Brassica oleracea* | Brassicaceae | Brassicales | Magnoliopsida |  |  | pacbio |
| *Cakile maritima* | Brassicaceae | Brassicales | Magnoliopsida | AAACCCT | ACAGACT | pacbio |
| *Lepidium draba* | Brassicaceae | Brassicales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Buxus sempervirens* | Buxaceae | Buxales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Agrostemma githago* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AATAAT | AAACCCT | pacbio |
| *Cerastium fontanum* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Cerastium glomeratum* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Dianthus deltoides* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Honckenya peploides* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Silene acaulis* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AACAAC | AATAAT | pacbio |
| *Silene dioica* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Silene latifolia* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AATGCT | pacbio |
| *Stellaria media* | Caryophyllaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Chenopodium album* | Chenopodiaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Suaeda vera* | Chenopodiaceae | Caryophyllales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Persicaria maculosa* | Polygonaceae | Caryophyllales | Magnoliopsida |  |  | pacbio |
| *Polygonum aviculare* | Polygonaceae | Caryophyllales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Reynoutria japonica* | Polygonaceae | Caryophyllales | Magnoliopsida | AAACCCT | AACAAC | pacbio |
| *Rumex acetosa* | Polygonaceae | Caryophyllales | Magnoliopsida | AACAAC | AACAACAAC | pacbio |
| *Rumex hydrolapathum* | Polygonaceae | Caryophyllales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Rumex sanguineus* | Polygonaceae | Caryophyllales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Euonymus europaeus* | Celastraceae | Celastrales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Cornus suecica* | Cornaceae | Cornales | Magnoliopsida |  |  | pacbio |
| *Bryonia dioica* | Cucurbitaceae | Cucurbitales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Adoxa moschatellina* | Adoxaceae | Dipsacales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Sambucus nigra* | Adoxaceae | Dipsacales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Viburnum lantana* | Adoxaceae | Dipsacales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Knautia arvensis* | Caprifoliaceae | Dipsacales | Magnoliopsida | AGATAGAT | AATAAT | pacbio |
| *Linnaea borealis* | Caprifoliaceae | Dipsacales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Impatiens glandulifera* | Balsaminaceae | Ericales | Magnoliopsida | AAGCATT | AAGCATC | assembly |
| *Impatiens glandulifera* | Balsaminaceae | Ericales | Magnoliopsida | AAGCATC | AAGCATCAAGCATC | pacbio |
| *Impatiens noli-tangere* | Balsaminaceae | Ericales | Magnoliopsida |  |  | pacbio |
| *Arctostaphylos uva-ursi* | Ericaceae | Ericales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lysimachia vulgaris* | Primulaceae | Ericales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Anthyllis vulneraria* | Fabaceae | Fabales | Magnoliopsida | AACCT | AACCTAACCT | pacbio |
| *Lathyrus linifolius* | Fabaceae | Fabales | Magnoliopsida |  |  | pacbio |
| *Lotus corniculatus* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AGATAGAT | pacbio |
| *Medicago arabica* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAGAGATAC | pacbio |
| *Onobrychis viciifolia* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Trifolium fragiferum* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AACCCTG | pacbio |
| *Trifolium pratense* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Ulex europaeus* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Vicia cracca* | Fabaceae | Fabales | Magnoliopsida | AATAAT | AATAATAAT | pacbio |
| *Vicia sativa* | Fabaceae | Fabales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Alnus glutinosa* | Betulaceae | Fagales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Betula pubescens* | Betulaceae | Fagales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Carpinus betulus* | Betulaceae | Fagales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Quercus robur* | Fagaceae | Fagales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Myrica gale* | Myricaceae | Fagales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Cruciata laevipes* | Rubiaceae | Gentianales | Magnoliopsida | AAACCCT |  | pacbio |
| *Galium aparine* | Rubiaceae | Gentianales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Sherardia arvensis* | Rubiaceae | Gentianales | Magnoliopsida | CCCCC |  | pacbio |
| *Erodium maritimum* | Geraniaceae | Geraniales | Magnoliopsida | CCCCC | CCCCCC | pacbio |
| *Erodium moschatum* | Geraniaceae | Geraniales | Magnoliopsida | ACTACT | AAACCCT | pacbio |
| *Geranium dissectum* | Geraniaceae | Geraniales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Geranium lucidum* | Geraniaceae | Geraniales | Magnoliopsida | AACCCT | AACCCTAACCCT | pacbio |
| *Geranium robertianum* | Geraniaceae | Geraniales | Magnoliopsida | AACCCT |  | pacbio |
| *Geranium sylvaticum* | Geraniaceae | Geraniales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Ballota nigra* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Lamium album* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lamium purpureum* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lycopus europaeus* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Salvia verbenaca* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Scutellaria galericulata* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Scutellaria minor* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Stachys palustris* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AACCT | pacbio |
| *Thymus serpyllum* | Lamiaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Ligustrum vulgare* | Oleaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Euphrasia foulaensis* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lathraea clandestina* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lathraea squamaria* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Melampyrum pratense* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Orobanche hederae* | Orobanchaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Chaenorhinum minus* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Hippuris vulgaris* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AATCT | pacbio |
| *Linaria vulgaris* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Misopates orontium* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | ATATAT | pacbio |
| *Plantago coronopus* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Plantago lanceolata* | Plantaginaceae | Lamiales | Magnoliopsida | AACCCTAAT | AACCCTAATAACCCTAAT | pacbio |
| *Veronica chamaedrys* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Veronica hederifolia* | Plantaginaceae | Lamiales | Magnoliopsida | AAGAAG | AAGAAGAAG | pacbio |
| *Veronica spicata* | Plantaginaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Buddleja davidii* | Scrophulariaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Scrophularia auriculata* | Scrophulariaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Scrophularia nodosa* | Scrophulariaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Verbena officinalis* | Verbenaceae | Lamiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Colchicum autumnale* | Colchicaceae | Liliales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Euphorbia amygdaloides* | Euphorbiaceae | Malpighiales | Magnoliopsida | AACCCT | AACCCTAACCCT | pacbio |
| *Euphorbia lathyris* | Euphorbiaceae | Malpighiales | Magnoliopsida | AAACCCT | ACATACATAT | pacbio |
| *Euphorbia peplus* | Euphorbiaceae | Malpighiales | Magnoliopsida | AACCCT | CCCCC | pacbio |
| *Mercurialis annua* | Euphorbiaceae | Malpighiales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Mercurialis perennis* | Euphorbiaceae | Malpighiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Hypericum perforatum* | Hypericaceae | Malpighiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Populus tremula* | Salicaceae | Malpighiales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Daphne mezereum* | Thymelaeaceae | Malvales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Lythrum salicaria* | Lythraceae | Myrtales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Chamaenerion angustifolium* | Onagraceae | Myrtales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Carex depauperata* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AACCCTG | pacbio |
| *Carex nigra* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Carex pendula* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Carex rostrata* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Schoenoplectus lacustris* | Cyperaceae | Poales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Juncus effusus* | Juncaceae | Poales | Magnoliopsida | AAACCCT | ATATAT | pacbio |
| *Luzula sylvatica* | Juncaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Oreojuncus trifidus* | Juncaceae | Poales | Magnoliopsida | AATAAT | AATAATAAT | pacbio |
| *Briza media* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Bromus sterilis* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Danthonia decumbens* | Poaceae | Poales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Hierochloe odorata* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Holcus mollis* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Leymus arenarius* | Poaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Typha latifolia* | Typhaceae | Poales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Berberis aquifolium* | Berberidaceae | Ranunculales | Magnoliopsida |  |  | pacbio |
| *Chelidonium majus* | Papaveraceae | Ranunculales | Magnoliopsida | AAACCCT | AACCCT | pacbio |
| *Fumaria muralis* | Papaveraceae | Ranunculales | Magnoliopsida | AAACCG | AAACCGAAACCG | pacbio |
| *Fumaria officinalis* | Papaveraceae | Ranunculales | Magnoliopsida | AAACCG | AAACCGAAACCG | pacbio |
| *Glaucium flavum* | Papaveraceae | Ranunculales | Magnoliopsida | AAAACCCTACCCG | AAAACCCTACCCGAAAACCCTACCCG | pacbio |
| *Papaver dubium* | Papaveraceae | Ranunculales | Magnoliopsida | AACCCTG | AACCCTGAACCCTG | pacbio |
| *Adonis annua* | Ranunculaceae | Ranunculales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Anemone pulsatilla* | Ranunculaceae | Ranunculales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Clematis vitalba* | Ranunculaceae | Ranunculales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Ranunculus acris* | Ranunculaceae | Ranunculales | Magnoliopsida |  |  | pacbio |
| *Ranunculus bulbosus* | Ranunculaceae | Ranunculales | Magnoliopsida | AACCCCG | AACCCCGAACCCCG | pacbio |
| *Trollius europaeus* | Ranunculaceae | Ranunculales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Humulus lupulus* | Cannabaceae | Rosales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Hippophae rhamnoides* | Elaeagnaceae | Rosales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Rhamnus cathartica* | Rhamnaceae | Rosales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Alchemilla alpina* | Rosaceae | Rosales | Magnoliopsida | AAACCCT |  | pacbio |
| *Alchemilla arvensis* | Rosaceae | Rosales | Magnoliopsida | AAACCCT |  | pacbio |
| *Alchemilla micans* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Crataegus laevigata* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Crataegus monogyna* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AATAAT | pacbio |
| *Dasiphora fruticosa* | Rosaceae | Rosales | Magnoliopsida | AAACCCT |  | pacbio |
| *Filipendula ulmaria* | Rosaceae | Rosales | Magnoliopsida | AAAAA | CCCCC | pacbio |
| *Geum rivale* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AACCCTAAT | pacbio |
| *Geum urbanum* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Malus domestica* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AACCT | pacbio |
| *Malus sylvestris* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | assembly |
| *Malus sylvestris* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | CCCCC | pacbio |
| *Potentilla anserina* | Rosaceae | Rosales | Magnoliopsida | AAACCCT | AACCT | pacbio |
| *Parietaria judaica* | Urticaceae | Rosales | Magnoliopsida | AAACCCT | AAAAA | pacbio |
| *Urtica dioica* | Urticaceae | Rosales | Magnoliopsida | AAACCCT | ACAGTC | pacbio |
| *Urtica urens* | Urticaceae | Rosales | Magnoliopsida | AAACCCT | AAGAGATAC | pacbio |
| *Viscum album* | Viscaceae | Santalales | Magnoliopsida | CCCCC | CCCCCC | pacbio |
| *Acer campestre* | Sapindaceae | Sapindales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Convolvulus arvensis* | Convolvulaceae | Solanales | Magnoliopsida | AAACCCT | ACTACT | pacbio |
| *Atropa belladonna* | Solanaceae | Solanales | Magnoliopsida | AAACCCT | AAACCCTAAACCCT | pacbio |
| *Solanum dulcamara* | Solanaceae | Solanales | Magnoliopsida | AACCCTG | AATAAT | pacbio |
| *Lunularia cruciata* | Lunulariaceae | Lunulariales | Marchantiopsida | AAACCCT | CCCCC | pacbio |
| *Equisetum hyemale* | Equisetaceae | Equisetales | Polypodiopsida | AGATAGAT | AGATAGATAGAT | pacbio |
| *Equisetum palustre* | Equisetaceae | Equisetales | Polypodiopsida | AGAGAG | AGATAGAT | pacbio |
| *Equisetum telmateia* | Equisetaceae | Equisetales | Polypodiopsida | AGATAGAT | AGATAGATAGAT | pacbio |
| *Asplenium scolopendrium* | Aspleniaceae | Polypodiales | Polypodiopsida | ATATAT | ATATATAT | pacbio |
| *Polypodium vulgare* | Polypodiaceae | Polypodiales | Polypodiopsida | ATATAT | AAACCCT | pacbio |
| *Polytrichum commune* | Polytrichaceae | Polytrichales | Polytrichopsida | AACCT | AGATAGAT | pacbio |
| *Sphagnum inundatum* | Sphagnaceae | Sphagnales | Sphagnopsida | AAACCT | AAACCCT | pacbio |
