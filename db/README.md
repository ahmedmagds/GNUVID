# Compressed Databases
Authors: **Ahmed M Moustafa and Paul J Planet**

## Rules

Each Compressed Database Release has more genomes analyzed from GISAID, new STs and CCs may be assigned and older CCs may be renamed.


GISAID Sequences inclusion criteria in this analysis.
  - Complete, high coverage genomes (excluding low coverage ) were downloaded from GISAID.
  - Genomes had at least 29,000 bp in length and had less than 1% Ns.
  - Any genome that had any ambiguity (any letter other than A,T,G and C) in the 10 open reading frames (ORF) was excluded.

The STs identified by GNUVID were grouped into larger taxonomic units, clonal complexes (CCs), defined as clusters of >20 STs that were single or double allele variants (SLV or DLV) away from a “founder” as defined in a a minimum spanning tree (MST) using the goeBURST algorithm.

## Limitations

- Because a change in any allele creates a new ST our method may accumulate and count “unnecessary” STs that have been seen only once or may be due to a sequencing error. This is partially ameliorated by the use of the CC definition that allows some variability amongst the members of a group. A large number of STs also may allow more granular approaches to tracking new lineages.

- The status of the CCs (active, silent and inactive) may be a sampling issue.

- Certain regions (US and Europe) clearly sequenced more genomes compared to other regions.

**The table below shows summary information of the 154 Clonal Complexes (CCs).**

The "Most common 5 countries" and "Most common Region" columns show the five countries and the region, respectively, with the most sequences from each Clonal Complex. Starting from the DB update (10/20/2020), the ten defining SNPs (C241,C3037,A23403,C8782,G11083,G25563,G26144,T28144,G28882,C22227) for the seven GISAID clades are reported for each CC for easier correlation between the two systems.


| Clonal Complex | Number of STs | Number of isolates | Most common 5 countries | Most common Region | Date range | Status | Defining SNPs | GISAID Clade |
|----------------|---------------|--------------------|-------------------------|--------------------|------------|--------|---------------|--------------|
| 4 | 684 | 1287 | USA (21%), United Kingdom (19%), China (16%), Japan (10%), Netherlands (9%) | Asia (37%) | 2019-12-24 to 2020-08-12 | Inactive | CCACGGGTGC | L |
| 16 | 23 | 31 | China (65%), Japan (10%), Thailand (6%), USA (6%), Australia (3%) | Asia (87%) | 2020-01-10 to 2020-04-15 | Inactive | CCATGGGCGC | S |
| 67 | 68 | 113 | Kazakhstan (23%), Australia (17%), USA (10%), China (8%), Canada (7%) | Asia (50%) | 2020-01-19 to 2020-04-26 | Inactive | CCACTGGTGC | Not Applicaple |
| 255 | 1883 | 3541 | United Kingdom (20%), USA (19%), India (6%), Netherlands (6%), Canada (5%) | Europe (59%) | 2020-01-24 to 2020-09-25 | Quiet | TTGCGGGTGC | G |
| 256 | 648 | 1561 | USA (74%), Canada (9%), China (4%), Japan (4%), Australia (3%) | North America (83%) | 2020-01-17 to 2020-06-19 | Inactive | CCATGGGCGC | S |
| 258 | 3964 | 8256 | USA (68%), United Kingdom (4%), France (4%), Canada (3%), Denmark (3%) | North America (72%) | 2020-02-16 to 2020-09-18 | Inactive | TTGCGTGTGC | GH |
| 266 | 58 | 91 | Spain (47%), United Kingdom (18%), Portugal (10%), Peru (7%), Australia (4%) | Europe (77%) | 2020-02-23 to 2020-06-22 | Inactive | CCATGGGCGC | S |
| 291 | 63 | 139 | USA (25%), France (23%), Saudi Arabia (15%), United Kingdom (11%), Belgium (6%) | Europe (49%) | 2020-02-26 to 2020-06-19 | Inactive | TTGCGTGTGC | GH |
| 297 | 76 | 176 | Belgium (18%), USA (11%), United Kingdom (10%), Switzerland (7%), Turkey (6%) | Europe (70%) | 2020-02-26 to 2020-09-28 | Quiet | TTGCGGGTAC | GR |
| **300** | 4577 | 9266 | United Kingdom (47%), USA (15%), Portugal (5%), Australia (4%), Russia (3%) | Europe (67%) | 2020-01-24 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 301 | 102 | 413 | Spain (33%), United Kingdom (18%), USA (7%), Portugal (4%), Russia (4%) | Europe (73%) | 2020-02-26 to 2020-08-03 | Inactive | TTGCGGGTGC | G |
| 305 | 52 | 125 | United Kingdom (66%), USA (19%), Australia (5%), Chile (3%), Greece (2%) | Europe (70%) | 2020-02-22 to 2020-06-23 | Inactive | TTGCGGGTGC | G |
| **317** | 144 | 393 | Japan (34%), USA (23%), United Kingdom (16%), Spain (4%), Switzerland (4%) | Asia (41%) | 2020-02-26 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 333 | 74 | 231 | USA (59%), Canada (12%), Australia (6%), France (5%), United Kingdom (5%) | North America (71%) | 2020-02-29 to 2020-06-30 | Inactive | TTGCGTGTGC | GH |
| 336 | 22 | 29 | Australia (97%), United Arab Emirates (3%) | Oceania (97%) | 2020-02-25 to 2020-04-04 | Inactive | CCACTGGTGC | Not Applicaple |
| 338 | 74 | 254 | USA (73%), Canada (8%), Saudi Arabia (2%), Colombia (2%), Peru (2%) | North America (81%) | 2020-02-29 to 2020-08-22 | Inactive | TTGCGTGTGC | GH |
| 348 | 128 | 291 | United Kingdom (16%), Netherlands (12%), Belgium (7%), Italy (6%), Portugal (6%) | Europe (74%) | 2020-02-22 to 2020-08-20 | Inactive | TTGCGGGTGC | G |
| 355 | 98 | 232 | Spain (63%), Kazakhstan (8%), Netherlands (5%), Portugal (4%), Peru (3%) | Europe (79%) | 2020-02-25 to 2020-07-13 | Inactive | CCATGGGCGC | S |
| 358 | 53 | 187 | Portugal (75%), United Kingdom (11%), New Zealand (5%), Netherlands (5%), Iceland (2%) | Europe (94%) | 2020-02-21 to 2020-05-18 | Inactive | TTGCGGGTGC | G |
| 369 | 162 | 400 | Netherlands (26%), United Kingdom (20%), Sweden (13%), Iceland (7%), Belgium (6%) | Europe (90%) | 2020-03-01 to 2020-06-13 | Inactive | TTGCGGGTAC | GR |
| **399** | 275 | 630 | United Kingdom (59%), Peru (11%), Canada (6%), Belgium (4%), Italy (3%) | Europe (74%) | 2020-03-02 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 454 | 130 | 426 | Switzerland (30%), Belgium (17%), France (14%), Canada (12%), United Kingdom (6%) | Europe (77%) | 2020-03-04 to 2020-07-17 | Inactive | TTGCGGGTGC | G |
| **498** | 343 | 707 | United Kingdom (45%), USA (42%), Switzerland (3%), Canada (2%), Spain (1%) | Europe (53%) | 2020-03-05 to 2020-10-06 | **Active** | TTGCGGGTGC | G |
| 550 | 676 | 1125 | United Kingdom (41%), USA (11%), South Korea (10%), Australia (6%), Iceland (6%) | Europe (63%) | 2020-01-22 to 2020-06-27 | Inactive | CCACTGTTGC | V |
| 551 | 27 | 100 | United Kingdom (42%), USA (14%), Netherlands (12%), Belgium (5%), Australia (4%) | Europe (70%) | 2020-03-01 to 2020-05-13 | Inactive | CCACTGTTGC | V |
| 623 | 72 | 184 | USA (54%), Australia (27%), Iceland (8%), Canada (4%), Taiwan (2%) | North America (60%) | 2020-03-05 to 2020-07-22 | Inactive | CCATGGGCGC | S |
| 645 | 47 | 96 | USA (57%), Australia (29%), United Kingdom (8%), New Zealand (2%), Singapore (2%) | North America (58%) | 2020-03-07 to 2020-04-10 | Inactive | CCATGGGCGC | S |
| 681 | 75 | 149 | Netherlands (68%), South Africa (9%), USA (5%), Austria (3%), Iceland (3%) | Europe (82%) | 2020-03-08 to 2020-06-24 | Inactive | TTGCGGGTGC | G |
| 750 | 40 | 65 | China (63%), Singapore (11%), USA (6%), Indonesia (5%), Australia (3%) | Asia (85%) | 2019-12-30 to 2020-05-26 | Inactive | CCACGGGTGC | L |
| 768 | 497 | 982 | USA (96%), Canada (3%), Australia (0%), New Zealand (0%), Singapore (0%) | North America (99%) | 2020-03-09 to 2020-10-02 | Quiet | TTGCGTGTGC | GH |
| 780 | 108 | 275 | United Kingdom (96%), Canada (1%), Iceland (1%), Uganda (1%), United Arab Emirates (1%) | Europe (96%) | 2020-03-09 to 2020-08-19 | Inactive | TTGCGGGTAC | GR |
| 800 | 213 | 360 | Saudi Arabia (64%), India (22%), Indonesia (3%), United Kingdom (2%), Japan (2%) | Asia (92%) | 2020-02-03 to 2020-09-02 | Inactive | TTGCGTGTGC | GH |
| 834 | 37 | 73 | United Kingdom (63%), USA (11%), Australia (8%), Jordan (5%), Canada (4%) | Europe (68%) | 2020-03-09 to 2020-07-31 | Inactive | CCACTGTTGC | V |
| 844 | 58 | 182 | USA (79%), Israel (12%), Canada (3%), Argentina (2%), France (2%) | North America (82%) | 2020-03-03 to 2020-07-18 | Inactive | TTGCGTGTGC | GH |
| 985 | 174 | 366 | United Kingdom (80%), USA (9%), Australia (2%), Singapore (1%), Peru (1%) | Europe (83%) | 2020-03-06 to 2020-07-16 | Inactive | TTGCGGGTGC | G |
| 1043 | 32 | 136 | USA (96%), New Zealand (2%), Australia (1%) | North America (96%) | 2020-03-12 to 2020-06-19 | Inactive | TTGCGTGTGC | GH |
| 1063 | 199 | 346 | Finland (40%), Sweden (30%), United Kingdom (20%), USA (3%), Netherlands (1%) | Europe (95%) | 2020-03-08 to 2020-07-13 | Inactive | TTGCGTGTGC | GH |
| 1085 | 23 | 45 | Denmark (91%), Singapore (7%), New Zealand (2%) | Europe (91%) | 2020-03-13 to 2020-04-28 | Inactive | TTGCGTGTGC | GH |
| 1102 | 135 | 224 | Brazil (78%), USA (11%), Australia (3%), Canada (2%), Chile (2%) | South America (82%) | 2020-03-07 to 2020-08-15 | Inactive | TTGCGGGTAC | GR |
| 1142 | 20 | 44 | United Kingdom (48%), Austria (30%), Finland (9%), India (5%), Australia (2%) | Europe (93%) | 2020-03-13 to 2020-06-15 | Inactive | TTGCGTGTGC | GH |
| 1148 | 45 | 89 | United Kingdom (89%), Canada (4%), USA (4%), China (1%), Germany (1%) | Europe (90%) | 2020-01-23 to 2020-06-23 | Inactive | CCACGGGTGC | L |
| 1179 | 245 | 406 | Singapore (43%), India (25%), Malaysia (10%), Australia (9%), USA (3%) | Asia (83%) | 2020-03-04 to 2020-09-03 | Inactive | CCACTGGTGC | Not Applicaple |
| 1189 | 50 | 126 | USA (100%) | North America (100%) | 2020-03-13 to 2020-08-03 | Inactive | TTGCGTGTGC | GH |
| 1208 | 41 | 66 | United Kingdom (79%), Iceland (5%), South Africa (5%), Canada (2%), Belgium (2%) | Europe (86%) | 2020-03-14 to 2020-09-26 | Quiet | TTGCGGGTAC | GR |
| 1328 | 62 | 94 | Brazil (94%), China (2%), United Kingdom (1%), Australia (1%), Portugal (1%) | South America (94%) | 2020-03-15 to 2020-08-10 | Inactive | TTGCGGGTAC | GR |
| 1455 | 23 | 46 | United Kingdom (96%), Romania (2%), Ireland (2%) | Europe (100%) | 2020-03-16 to 2020-09-25 | Quiet | TTGCGGGTGC | G |
| 1508 | 45 | 75 | USA (92%), Taiwan (3%), South Korea (3%), United Kingdom (1%), Canada (1%) | North America (93%) | 2020-01-23 to 2020-05-27 | Inactive | CCATGGGCGC | S |
| 1540 | 34 | 56 | United Kingdom (82%), Vietnam (4%), USA (2%), Sweden (2%), Canada (2%) | Europe (88%) | 2020-03-17 to 2020-08-14 | Inactive | TTGCGGGTAC | GR |
| 1582 | 36 | 77 | USA (97%), Taiwan (1%), United Arab Emirates (1%) | North America (97%) | 2020-03-16 to 2020-05-28 | Inactive | CCATGGGCGC | S |
| 1698 | 70 | 96 | India (60%), United Kingdom (34%), USA (2%), Gambia (1%), Australia (1%) | Asia (61%) | 2020-03-17 to 2020-08-19 | Inactive | TTGCGGGTAC | GR |
| 1726 | 22 | 33 | New Zealand (36%), Australia (27%), United Kingdom (27%), Finland (3%), South Korea (3%) | Oceania (64%) | 2020-03-14 to 2020-04-22 | Inactive | CCACTGTTGC | V |
| 1852 | 41 | 74 | United Kingdom (46%), USA (20%), Portugal (11%), Canada (7%), South Africa (4%) | Europe (61%) | 2020-03-13 to 2020-09-09 | Inactive | TTGCGGGTAC | GR |
| 2175 | 47 | 173 | Australia (97%), Canada (1%), USA (1%), Portugal (1%), New Zealand (1%) | Oceania (97%) | 2020-03-16 to 2020-04-27 | Inactive | CCATGGGCGC | S |
| 2445 | 36 | 66 | United Kingdom (55%), Canada (35%), Belgium (5%), France (3%), Democratic Republic of the Congo (2%) | Europe (64%) | 2020-03-04 to 2020-06-09 | Inactive | TTGCGGGTGC | G |
| 2490 | 73 | 200 | United Kingdom (96%), Lithuania (2%), Australia (0%), Oman (0%), USA (0%) | Europe (98%) | 2020-03-18 to 2020-09-07 | Inactive | TTGCGGGTAC | GR |
| 2532 | 59 | 78 | India (36%), Saudi Arabia (27%), Nigeria (6%), Bangladesh (5%), Australia (4%) | Asia (68%) | 2020-03-06 to 2020-08-04 | Inactive | CCATGGGCGC | S |
| 2566 | 87 | 171 | USA (99%), Canada (1%) | North America (100%) | 2020-03-13 to 2020-08-04 | Inactive | TTGCGTGTGC | GH |
| 2574 | 135 | 369 | United Kingdom (97%), Switzerland (2%), Iceland (1%), Taiwan (0%), Denmark (0%) | Europe (100%) | 2020-03-07 to 2020-06-23 | Inactive | TTGCGGGTGC | G |
| 2649 | 45 | 77 | USA (75%), China (9%), South Korea (6%), Vietnam (4%), Canada (3%) | North America (78%) | 2020-01-15 to 2020-05-15 | Inactive | CCATGGGCGC | S |
| 2774 | 22 | 37 | USA (100%) | North America (100%) | 2020-03-09 to 2020-04-27 | Inactive | CCACTGTTGC | V |
| 3186 | 27 | 50 | USA (100%) | North America (100%) | 2020-03-27 to 2020-07-06 | Inactive | TTGCGTGTGC | GH |
| 3297 | 24 | 36 | USA (83%), Australia (6%), New Zealand (6%), Canada (3%), Israel (3%) | North America (86%) | 2020-03-14 to 2020-07-20 | Inactive | TTGCGTGTGC | GH |
| 3530 | 82 | 171 | USA (73%), New Zealand (22%), India (2%), Canada (2%), Taiwan (1%) | North America (75%) | 2020-03-13 to 2020-09-01 | Inactive | TTGCGTGTGC | GH |
| **3859** | 79 | 260 | United Kingdom (98%), Norway (2%) | Europe (100%) | 2020-04-13 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 4313 | 29 | 42 | United Kingdom (38%), Australia (33%), Spain (5%), USA (5%), New Zealand (5%) | Europe (52%) | 2020-02-28 to 2020-06-14 | Inactive | CCACTGTTGC | V |
| 4669 | 70 | 102 | USA (54%), Russia (14%), United Kingdom (8%), Spain (4%), Hungary (3%) | North America (54%) | 2020-03-16 to 2020-08-06 | Inactive | TTGCGGGTGC | G |
| 4713 | 32 | 56 | Singapore (100%) | Asia (100%) | 2020-04-04 to 2020-07-22 | Inactive | CCACTGGTGC | Not Applicaple |
| 4971 | 34 | 83 | USA (100%) | North America (100%) | 2020-04-06 to 2020-06-22 | Inactive | TTGCGTGTGC | GH |
| **5447** | 343 | 609 | United Kingdom (62%), India (24%), Saudi Arabia (7%), Netherlands (1%), Ireland (1%) | Europe (66%) | 2020-02-16 to 2020-10-11 | **Active** | TTGCGTGTGC | GH |
| 6331 | 24 | 38 | United Kingdom (79%), Portugal (5%), USA (3%), New Zealand (3%), Sweden (3%) | Europe (89%) | 2020-03-13 to 2020-06-17 | Inactive | TTGCGGGTAC | GR |
| 6360 | 29 | 48 | United Arab Emirates (40%), United Kingdom (21%), Australia (8%), Sweden (6%), Democratic Republic of the Congo (6%) | Asia (46%) | 2020-03-17 to 2020-09-04 | Inactive | CCATGGGCGC | S |
| 6620 | 25 | 72 | USA (96%), Luxembourg (3%), Russia (1%) | North America (96%) | 2020-03-27 to 2020-08-24 | Inactive | TTGCGTGTGC | GH |
| 7363 | 21 | 33 | United Kingdom (100%) | Europe (100%) | 2020-03-24 to 2020-07-16 | Inactive | TTGCGGGTAC | GR |
| 8626 | 26 | 44 | India (95%), Singapore (2%), USA (2%) | Asia (98%) | 2020-04-20 to 2020-09-08 | Inactive | TTGCGGGTAC | GR |
| 8902 | 26 | 79 | USA (97%), United Kingdom (1%), South Africa (1%) | North America (97%) | 2020-04-15 to 2020-08-07 | Inactive | TTGCGGGTAC | GR |
| 9238 | 24 | 34 | India (94%), United Kingdom (3%), Sweden (3%) | Asia (94%) | 2020-05-11 to 2020-08-17 | Inactive | TTGCGGGTAC | GR |
| 9505 | 31 | 95 | United Kingdom (100%) | Europe (100%) | 2020-03-13 to 2020-05-06 | Inactive | TTGCGGGTAC | GR |
| 9581 | 30 | 42 | USA (98%), United Kingdom (2%) | North America (98%) | 2020-06-19 to 2020-09-18 | Inactive | TTGCGTGTGC | GH |
| 9734 | 57 | 109 | Japan (52%), USA (16%), Netherlands (6%), Mali (6%), India (5%) | Asia (64%) | 2020-01-23 to 2020-06-13 | Inactive | CCATGGGCGC | S |
| 9999 | 82 | 169 | Netherlands (32%), France (14%), Spain (10%), United Kingdom (9%), Belgium (8%) | Europe (84%) | 2020-02-29 to 2020-06-09 | Inactive | TTGCGTGTGC | GH |
| 10221 | 105 | 191 | USA (99%), South Korea (1%), Mexico (1%) | North America (99%) | 2020-03-23 to 2020-09-22 | Quiet | TTGCGGGTGC | G |
| 12210 | 28 | 78 | USA (100%) | North America (100%) | 2020-04-30 to 2020-06-09 | Inactive | TTGCGTGTGC | GH |
| 12995 | 727 | 3150 | Australia (100%) | Oceania (100%) | 2020-03-19 to 2020-09-18 | Inactive | TTGCGGGTAC | GR |
| 13180 | 35 | 118 | United Kingdom (100%) | Europe (100%) | 2020-04-21 to 2020-08-27 | Inactive | TTGCGGGTAC | GR |
| 13208 | 38 | 57 | India (100%) | Asia (100%) | 2020-04-26 to 2020-06-25 | Inactive | TTGCGTGTGC | GH |
| 13245 | 30 | 73 | United Kingdom (96%), Bangladesh (1%), India (1%), South Africa (1%) | Europe (96%) | 2020-03-27 to 2020-08-31 | Inactive | TTGCGGGTAC | GR |
| 13264 | 38 | 72 | USA (83%), Norway (17%) | North America (83%) | 2020-04-21 to 2020-09-14 | Inactive | TTGCGGGTAC | GR |
| 13301 | 52 | 119 | USA (100%) | North America (100%) | 2020-04-09 to 2020-09-16 | Inactive | TTGCGGGTGC | G |
| 13389 | 31 | 148 | United Kingdom (100%) | Europe (100%) | 2020-06-02 to 2020-10-02 | Quiet | TTGCGGGTAC | GR |
| 13413 | 82 | 116 | South Africa (99%), Singapore (1%) | Africa (99%) | 2020-06-14 to 2020-09-14 | Inactive | TTGCGGGTAC | GR |
| 15279 | 124 | 429 | South Korea (99%), Belgium (0%), USA (0%), France (0%) | Asia (99%) | 2020-03-14 to 2020-08-11 | Inactive | TTGCGTGTGC | GH |
| 16416 | 21 | 21 | Saudi Arabia (95%), India (5%) | Asia (100%) | 2020-04-18 to 2020-06-19 | Inactive | TTACGTGTGC | Not Applicaple |
| 16909 | 33 | 38 | South Africa (100%) | Africa (100%) | 2020-06-20 to 2020-08-24 | Inactive | TTGCGGGTAC | GR |
| 16987 | 45 | 87 | USA (100%) | North America (100%) | 2020-06-16 to 2020-09-16 | Inactive | TTGCGTGTGC | GH |
| 17002 | 25 | 38 | USA (92%), Japan (3%), Canada (3%), United Kingdom (3%) | North America (95%) | 2020-03-19 to 2020-08-19 | Inactive | TTGCGGGTAC | GR |
| 17027 | 76 | 118 | USA (94%), United Kingdom (5%), Canada (1%) | North America (95%) | 2020-06-15 to 2020-09-30 | Quiet | TTGCGGGTGC | G |
| 17444 | 61 | 151 | USA (99%), Gambia (1%) | North America (99%) | 2020-05-27 to 2020-09-29 | Quiet | TTGCGTGTGC | GH |
| 17516 | 35 | 160 | Australia (100%) | Oceania (100%) | 2020-07-13 to 2020-09-18 | Inactive | TTGCGGGTAC | GR |
| 18372 | 44 | 67 | United Kingdom (88%), USA (4%), Spain (1%), Belgium (1%), Italy (1%) | Europe (93%) | 2020-03-22 to 2020-08-20 | Inactive | TTGCGGGTAC | GR |
| 19653 | 42 | 145 | United Kingdom (99%), USA (1%) | Europe (99%) | 2020-04-11 to 2020-09-08 | Inactive | TTGCGGGTAC | GR |
| **20544** | 30 | 98 | United Kingdom (100%) | Europe (100%) | 2020-05-05 to 2020-10-05 | **Active** | TTGCGGGTAC | GR |
| 21210 | 127 | 223 | USA (99%), United Kingdom (1%) | North America (99%) | 2020-05-20 to 2020-09-30 | Quiet | TTGCGTGTGC | GH |
| **21976** | 52 | 93 | United Kingdom (58%), South Africa (32%), India (8%), USA (2%) | Europe (58%) | 2020-05-21 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 22075 | 36 | 144 | United Kingdom (99%), USA (1%) | Europe (99%) | 2020-04-14 to 2020-08-30 | Inactive | TTGCGGGTAC | GR |
| 22279 | 24 | 56 | United Kingdom (98%), USA (2%) | Europe (98%) | 2020-06-09 to 2020-09-25 | Quiet | TTGCGGGTAC | GR |
| 22280 | 25 | 53 | USA (100%) | North America (100%) | 2020-06-09 to 2020-07-20 | Inactive | TTGCGTGTGC | GH |
| 22318 | 106 | 451 | Australia (100%) | Oceania (100%) | 2020-06-09 to 2020-09-14 | Inactive | TTGCGGGTAC | GR |
| 23032 | 42 | 62 | USA (100%) | North America (100%) | 2020-03-28 to 2020-09-24 | Quiet | TTGCGTGTGC | GH |
| **23107** | 47 | 141 | United Kingdom (100%) | Europe (100%) | 2020-06-15 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 24039 | 24 | 152 | Australia (100%) | Oceania (100%) | 2020-06-24 to 2020-08-14 | Inactive | TTGCGGGTAC | GR |
| 24502 | 37 | 64 | USA (100%) | North America (100%) | 2020-06-28 to 2020-09-23 | Quiet | TTGCGTGTGC | GH |
| 25251 | 21 | 26 | South Africa (100%) | Africa (100%) | 2020-07-01 to 2020-08-16 | Inactive | TTGCGGGTAC | GR |
| 25297 | 60 | 251 | Australia (100%), Ukraine (0%) | Oceania (100%) | 2020-07-06 to 2020-09-10 | Inactive | TTGCGGGTAC | GR |
| 25470 | 24 | 82 | Australia (96%), United Kingdom (4%) | Oceania (96%) | 2020-07-08 to 2020-09-24 | Quiet | TTGCGGGTAC | GR |
| **25545** | 92 | 198 | United Kingdom (72%), Belgium (22%), Netherlands (2%), France (2%), Germany (2%) | Europe (100%) | 2020-07-09 to 2020-10-06 | **Active** | TTGCGGGTGC | G |
| **25780** | 20 | 58 | United Kingdom (95%), New Zealand (3%), USA (2%) | Europe (95%) | 2020-04-06 to 2020-10-05 | **Active** | TTGCGGGTAC | GR |
| 26286 | 34 | 128 | United Kingdom (99%), Bangladesh (1%) | Europe (99%) | 2020-07-14 to 2020-08-28 | Inactive | TTGCGGGTAC | GR |
| **26377** | 231 | 643 | United Kingdom (95%), Spain (2%), Netherlands (2%), Ireland (1%), Switzerland (0%) | Europe (100%) | 2020-07-18 to 2020-10-13 | **Active** | TTGCGGGTGT | GV |
| **26711** | 234 | 629 | United Kingdom (100%) | Europe (100%) | 2020-07-21 to 2020-10-08 | **Active** | TTGCTGGTAC | Not Applicaple |
| **26754** | 119 | 284 | United Kingdom (74%), Norway (21%), Netherlands (1%), Spain (1%), France (1%) | Europe (100%) | 2020-06-20 to 2020-10-11 | **Active** | TTGCGGGTGT | GV |
| 26806 | 45 | 99 | United Kingdom (52%), France (22%), Netherlands (17%), Norway (9%) | Europe (100%) | 2020-07-22 to 2020-10-01 | Quiet | TTGCGTGTGC | GH |
| 26989 | 45 | 102 | United Kingdom (95%), Montenegro (2%), Italy (1%), Russia (1%), South Africa (1%) | Europe (99%) | 2020-04-09 to 2020-09-26 | Quiet | TTGCGGGTAC | GR |
| **27413** | 52 | 232 | United Kingdom (100%) | Europe (100%) | 2020-07-28 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 27456 | 66 | 123 | United Kingdom (57%), France (36%), Netherlands (6%), Spain (1%), Belgium (1%) | Europe (100%) | 2020-07-29 to 2020-10-01 | Quiet | TTGCGTGTGC | GH |
| 27569 | 40 | 70 | United Kingdom (51%), Norway (27%), Czech Republic (9%), South Korea (6%), India (1%) | Europe (93%) | 2020-06-20 to 2020-09-28 | Quiet | TTGCGGGTAC | GR |
| 27578 | 22 | 70 | United Kingdom (100%) | Europe (100%) | 2020-04-13 to 2020-10-02 | Quiet | TTGCGGGTAC | GR |
| 27666 | 32 | 58 | United Kingdom (90%), France (5%), Netherlands (3%), Spain (2%) | Europe (100%) | 2020-07-31 to 2020-09-10 | Inactive | TTGCGGGTAC | GR |
| **27693** | 387 | 1102 | United Kingdom (99%), Netherlands (0%), Spain (0%), Ireland (0%), France (0%) | Europe (100%) | 2020-07-31 to 2020-10-10 | **Active** | TTGCGGGTGT | GV |
| 27698 | 30 | 37 | United Kingdom (100%) | Europe (100%) | 2020-07-15 to 2020-09-28 | Quiet | TTGCGTGTGC | GH |
| **27700** | 65 | 161 | United Kingdom (99%), Norway (1%) | Europe (100%) | 2020-07-31 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 27736 | 41 | 83 | Netherlands (99%), United Kingdom (1%) | Europe (100%) | 2020-06-11 to 2020-09-18 | Inactive | TTGCGTGTGC | GH |
| **27950** | 61 | 174 | United Kingdom (97%), Netherlands (2%), New Zealand (1%) | Europe (99%) | 2020-08-04 to 2020-10-08 | **Active** | TTGCGGGTGT | GV |
| **28012** | 67 | 202 | United Kingdom (100%) | Europe (100%) | 2020-08-04 to 2020-10-06 | **Active** | TTGCGGGTGT | GV |
| 28019 | 90 | 226 | United Kingdom (92%), Ireland (3%), France (1%), Malta (1%), Netherlands (1%) | Europe (100%) | 2020-08-04 to 2020-10-01 | Quiet | TTGCGTGTGC | GH |
| **28179** | 253 | 632 | United Kingdom (100%) | Europe (100%) | 2020-06-02 to 2020-10-10 | **Active** | TTGCGGGTAC | GR |
| **28445** | 104 | 309 | United Kingdom (89%), Norway (9%), Netherlands (1%), France (0%), Sweden (0%) | Europe (100%) | 2020-08-08 to 2020-10-08 | **Active** | TTGCGTGTGC | GH |
| **28513** | 46 | 120 | United Kingdom (99%), Australia (1%) | Europe (99%) | 2020-03-24 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **28786** | 73 | 165 | United Kingdom (100%) | Europe (100%) | 2020-08-11 to 2020-10-08 | **Active** | TTGCGGGTGC | G |
| 28825 | 40 | 89 | United Kingdom (93%), France (7%) | Europe (100%) | 2020-08-02 to 2020-09-24 | Quiet | TTGCGGGTGT | GV |
| 28987 | 47 | 148 | United Kingdom (100%) | Europe (100%) | 2020-06-01 to 2020-09-25 | Quiet | TTGCGGGTAC | GR |
| 29259 | 41 | 129 | United Kingdom (91%), Netherlands (9%) | Europe (100%) | 2020-08-05 to 2020-10-02 | Quiet | TTGCGGGTGT | GV |
| **29310** | 24 | 71 | United Kingdom (99%), Ireland (1%) | Europe (100%) | 2020-08-17 to 2020-10-07 | **Active** | TTGCGGGTGT | GV |
| 29423 | 31 | 66 | United Kingdom (98%), Switzerland (2%) | Europe (100%) | 2020-05-19 to 2020-10-02 | Quiet | TTGCGGGTGC | G |
| **29516** | 37 | 117 | United Kingdom (99%), Netherlands (1%) | Europe (100%) | 2020-08-19 to 2020-10-05 | **Active** | TTGCGGGTAC | GR |
| **29952** | 39 | 107 | United Kingdom (100%) | Europe (100%) | 2020-06-08 to 2020-10-06 | **Active** | TTGCGGGTGC | G |
| **30174** | 61 | 140 | United Kingdom (98%), Bangladesh (1%), Russia (1%) | Europe (99%) | 2020-07-10 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 30180 | 21 | 31 | Netherlands (94%), United Kingdom (6%) | Europe (100%) | 2020-08-25 to 2020-09-27 | Quiet | TTGCGGGTGC | G |
| **30362** | 29 | 116 | United Kingdom (100%) | Europe (100%) | 2020-08-27 to 2020-10-10 | **Active** | TTGCGGGTGT | GV |
| **30431** | 30 | 65 | United Kingdom (100%) | Europe (100%) | 2020-08-28 to 2020-10-06 | **Active** | TTGCGGGTAT | Not Applicaple |
| **30498** | 29 | 85 | United Kingdom (100%) | Europe (100%) | 2020-08-28 to 2020-10-06 | **Active** | TTGCTGGTAC | Not Applicaple |
| **30499** | 37 | 93 | United Kingdom (100%) | Europe (100%) | 2020-07-17 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **31179** | 216 | 606 | United Kingdom (100%), Spain (0%) | Europe (100%) | 2020-09-01 to 2020-10-09 | **Active** | TTGCGGGTGT | GV |
| **31744** | 78 | 177 | United Kingdom (100%) | Europe (100%) | 2020-09-08 to 2020-10-09 | **Active** | TTGCGGGTGT | GV |
| **31942** | 79 | 236 | United Kingdom (100%) | Europe (100%) | 2020-09-02 to 2020-10-10 | **Active** | TTGCGGGTGT | GV |
