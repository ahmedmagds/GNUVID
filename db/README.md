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
| 4 | 963 | 1706 | United Kingdom (23%), USA (18%), China (15%), Netherlands (9%), Japan (8%) | Europe (45%) | 2019-12-24 to 2020-08-12 | Inactive | CCACGGGTGC | L |
| 16 | 30 | 39 | China (69%), Japan (8%), USA (8%), Thailand (5%), Australia (3%) | Asia (87%) | 2020-01-10 to 2020-04-15 | Inactive | CCATGGGCGC | S |
| 67 | 169 | 227 | Australia (16%), Kazakhstan (12%), USA (11%), India (10%), United Arab Emirates (9%) | Asia (52%) | 2020-01-19 to 2020-07-16 | Inactive | CCACTGGTGC | Not Applicaple |
| **255** | 2545 | 4408 | United Kingdom (22%), USA (21%), India (7%), Netherlands (6%), Canada (5%) | Europe (57%) | 2020-01-24 to 2020-10-06 | **Active** | TTGCGGGTGC | G |
| 256 | 874 | 1914 | USA (73%), Canada (8%), China (7%), Japan (4%), Australia (2%) | North America (81%) | 2020-01-05 to 2020-07-14 | Inactive | CCATGGGCGC | S |
| **258** | 5301 | 10172 | USA (67%), United Kingdom (6%), France (4%), Netherlands (4%), Canada (3%) | North America (71%) | 2020-02-16 to 2020-10-05 | **Active** | TTGCGTGTGC | GH |
| 266 | 66 | 99 | Spain (46%), United Kingdom (19%), Portugal (9%), Peru (6%), Australia (4%) | Europe (77%) | 2020-02-23 to 2020-06-22 | Inactive | CCATGGGCGC | S |
| 291 | 101 | 183 | USA (23%), France (21%), Saudi Arabia (17%), United Kingdom (10%), Israel (6%) | Europe (46%) | 2020-02-26 to 2020-09-03 | Inactive | TTGCGTGTGC | GH |
| **297** | 171 | 299 | Belgium (24%), United Kingdom (18%), USA (12%), Switzerland (4%), Netherlands (4%) | Europe (73%) | 2020-02-26 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **300** | 7435 | 13477 | United Kingdom (47%), USA (15%), Australia (4%), Portugal (3%), Russia (3%) | Europe (66%) | 2020-01-24 to 2020-10-09 | **Active** | TTGCGGGTAC | GR |
| 301 | 208 | 548 | Spain (29%), United Kingdom (23%), USA (7%), Portugal (3%), Russia (3%) | Europe (74%) | 2020-02-26 to 2020-09-25 | Quiet | TTGCGGGTGC | G |
| 305 | 65 | 142 | United Kingdom (69%), USA (17%), Australia (4%), Chile (3%), Greece (1%) | Europe (73%) | 2020-02-22 to 2020-06-23 | Inactive | TTGCGGGTGC | G |
| **317** | 246 | 523 | Japan (29%), USA (24%), United Kingdom (21%), Spain (3%), Switzerland (3%) | Asia (36%) | 2020-02-26 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 333 | 106 | 274 | USA (58%), Canada (11%), France (7%), Australia (5%), United Kingdom (4%) | North America (69%) | 2020-02-29 to 2020-08-12 | Inactive | TTGCGTGTGC | GH |
| 336 | 23 | 30 | Australia (97%), United Arab Emirates (3%) | Oceania (97%) | 2020-02-25 to 2020-04-04 | Inactive | CCACTGGTGC | Not Applicaple |
| 338 | 168 | 411 | USA (69%), Latvia (8%), Canada (5%), United Kingdom (2%), Colombia (2%) | North America (74%) | 2020-02-29 to 2020-09-24 | Quiet | TTGCGTGTGC | GH |
| 348 | 197 | 384 | United Kingdom (13%), Netherlands (12%), Peru (10%), South Africa (7%), Portugal (7%) | Europe (64%) | 2020-02-22 to 2020-08-28 | Inactive | TTGCGGGTGC | G |
| 355 | 129 | 275 | Spain (59%), United Kingdom (8%), Kazakhstan (7%), Portugal (4%), Netherlands (4%) | Europe (80%) | 2020-02-25 to 2020-07-13 | Inactive | CCATGGGCGC | S |
| 358 | 74 | 209 | Portugal (76%), United Kingdom (10%), New Zealand (5%), Netherlands (4%), Iceland (1%) | Europe (92%) | 2020-02-21 to 2020-06-20 | Inactive | TTGCGGGTGC | G |
| 369 | 204 | 461 | United Kingdom (24%), Netherlands (23%), Sweden (11%), Iceland (10%), Austria (6%) | Europe (91%) | 2020-03-01 to 2020-06-19 | Inactive | TTGCGGGTAC | GR |
| **399** | 550 | 1068 | United Kingdom (66%), Peru (10%), Canada (6%), Belgium (3%), Italy (2%) | Europe (76%) | 2020-03-02 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 454 | 225 | 543 | Switzerland (25%), Belgium (16%), France (15%), Canada (9%), United Kingdom (8%) | Europe (73%) | 2020-03-04 to 2020-08-25 | Inactive | TTGCGGGTGC | G |
| **498** | 589 | 1119 | United Kingdom (50%), USA (38%), Switzerland (2%), Norway (2%), Canada (1%) | Europe (58%) | 2020-03-05 to 2020-10-06 | **Active** | TTGCGGGTGC | G |
| 550 | 840 | 1334 | United Kingdom (40%), USA (12%), South Korea (10%), Australia (6%), Iceland (5%) | Europe (61%) | 2020-01-22 to 2020-07-16 | Inactive | CCACTGTTGC | V |
| 551 | 43 | 117 | United Kingdom (42%), USA (15%), Netherlands (10%), Belgium (5%), Australia (4%) | Europe (69%) | 2020-02-26 to 2020-05-13 | Inactive | CCACTGTTGC | V |
| 623 | 89 | 214 | USA (59%), Australia (24%), Iceland (7%), Canada (4%), Taiwan (1%) | North America (64%) | 2020-03-05 to 2020-07-22 | Inactive | CCATGGGCGC | S |
| 645 | 67 | 129 | USA (67%), Australia (22%), United Kingdom (6%), New Zealand (2%), Singapore (2%) | North America (69%) | 2020-03-07 to 2020-04-15 | Inactive | CCATGGGCGC | S |
| 681 | 142 | 249 | Netherlands (76%), South Africa (6%), USA (3%), Austria (3%), Iceland (3%) | Europe (88%) | 2020-03-08 to 2020-09-15 | Inactive | TTGCGGGTGC | G |
| 750 | 45 | 70 | China (63%), Singapore (10%), USA (6%), Netherlands (4%), Indonesia (4%) | Asia (83%) | 2019-12-30 to 2020-07-14 | Inactive | CCACGGGTGC | L |
| **768** | 774 | 1356 | USA (96%), Canada (2%), Australia (0%), New Zealand (0%), Nigeria (0%) | North America (99%) | 2020-03-09 to 2020-10-07 | **Active** | TTGCGTGTGC | GH |
| 780 | 188 | 396 | United Kingdom (97%), Canada (1%), Iceland (1%), Uganda (1%), United Arab Emirates (1%) | Europe (97%) | 2020-03-02 to 2020-08-19 | Inactive | TTGCGGGTAC | GR |
| **800** | 344 | 563 | Saudi Arabia (45%), India (21%), United Kingdom (18%), Norway (5%), Indonesia (3%) | Asia (71%) | 2020-02-03 to 2020-10-05 | **Active** | TTGCGTGTGC | GH |
| 834 | 40 | 76 | United Kingdom (64%), USA (11%), Australia (8%), Jordan (5%), Canada (4%) | Europe (70%) | 2020-03-09 to 2020-07-31 | Inactive | CCACTGTTGC | V |
| 844 | 119 | 255 | USA (71%), Israel (14%), United Kingdom (9%), Canada (2%), Argentina (2%) | North America (73%) | 2020-03-03 to 2020-09-13 | Inactive | TTGCGTGTGC | GH |
| 985 | 281 | 521 | United Kingdom (83%), USA (9%), Australia (2%), Singapore (1%), Peru (1%) | Europe (85%) | 2020-03-06 to 2020-09-20 | Quiet | TTGCGGGTGC | G |
| 1043 | 76 | 201 | USA (98%), New Zealand (1%), Australia (1%) | North America (98%) | 2020-03-12 to 2020-08-04 | Inactive | TTGCGTGTGC | GH |
| 1063 | 252 | 403 | Finland (36%), Sweden (33%), United Kingdom (21%), USA (3%), Netherlands (1%) | Europe (95%) | 2020-03-08 to 2020-08-27 | Inactive | TTGCGTGTGC | GH |
| 1085 | 24 | 46 | Denmark (91%), Singapore (7%), New Zealand (2%) | Europe (91%) | 2020-03-13 to 2020-04-28 | Inactive | TTGCGTGTGC | GH |
| 1102 | 169 | 261 | Brazil (75%), USA (10%), Australia (3%), United Kingdom (2%), Argentina (2%) | South America (80%) | 2020-03-07 to 2020-09-29 | Quiet | TTGCGGGTAC | GR |
| 1142 | 29 | 61 | United Kingdom (57%), Austria (21%), Finland (7%), India (7%), Australia (2%) | Europe (92%) | 2020-03-13 to 2020-07-06 | Inactive | TTGCGTGTGC | GH |
| 1148 | 53 | 99 | United Kingdom (89%), Canada (4%), USA (4%), China (2%), Germany (1%) | Europe (90%) | 2020-01-23 to 2020-06-23 | Inactive | CCACGGGTGC | L |
| 1179 | 362 | 552 | Singapore (43%), India (24%), Malaysia (12%), Australia (7%), USA (3%) | Asia (86%) | 2020-03-04 to 2020-09-12 | Inactive | CCACTGGTGC | Not Applicaple |
| 1189 | 122 | 228 | USA (100%), United Kingdom (0%) | North America (100%) | 2020-03-13 to 2020-09-28 | Quiet | TTGCGTGTGC | GH |
| 1208 | 50 | 75 | United Kingdom (77%), South Africa (7%), Iceland (4%), Netherlands (3%), Canada (1%) | Europe (85%) | 2020-03-14 to 2020-09-26 | Quiet | TTGCGGGTAC | GR |
| 1328 | 88 | 120 | Brazil (88%), United Kingdom (4%), China (2%), Australia (2%), Portugal (1%) | South America (89%) | 2020-03-15 to 2020-09-04 | Inactive | TTGCGGGTAC | GR |
| **1455** | 72 | 114 | United Kingdom (86%), Ireland (8%), Norway (4%), Italy (2%), Romania (1%) | Europe (100%) | 2020-03-16 to 2020-10-05 | **Active** | TTGCGGGTGC | G |
| 1508 | 48 | 79 | USA (92%), Taiwan (3%), South Korea (3%), United Kingdom (1%), Canada (1%) | North America (94%) | 2020-01-23 to 2020-05-27 | Inactive | CCATGGGCGC | S |
| 1540 | 52 | 81 | United Kingdom (72%), Canada (12%), USA (4%), France (2%), Vietnam (2%) | Europe (77%) | 2020-03-17 to 2020-09-10 | Inactive | TTGCGGGTAC | GR |
| 1582 | 45 | 88 | USA (98%), Taiwan (1%), United Arab Emirates (1%) | North America (98%) | 2020-03-16 to 2020-05-31 | Inactive | CCATGGGCGC | S |
| 1698 | 141 | 176 | India (69%), United Kingdom (23%), USA (6%), Singapore (1%), Gambia (1%) | Asia (70%) | 2020-03-17 to 2020-08-19 | Inactive | TTGCGGGTAC | GR |
| 1726 | 28 | 39 | New Zealand (33%), United Kingdom (31%), Australia (23%), Taiwan (3%), Finland (3%) | Oceania (56%) | 2020-03-03 to 2020-04-22 | Inactive | CCACTGTTGC | V |
| 1852 | 114 | 186 | United Kingdom (60%), USA (12%), Czech Republic (5%), Portugal (4%), Bangladesh (4%) | Europe (76%) | 2020-03-13 to 2020-09-21 | Quiet | TTGCGGGTAC | GR |
| 2175 | 53 | 180 | Australia (96%), Israel (1%), Canada (1%), USA (1%), Portugal (1%) | Oceania (96%) | 2020-03-16 to 2020-04-27 | Inactive | CCATGGGCGC | S |
| 2445 | 36 | 66 | United Kingdom (55%), Canada (35%), Belgium (5%), France (3%), Democratic Republic of the Congo (2%) | Europe (64%) | 2020-03-04 to 2020-06-09 | Inactive | TTGCGGGTGC | G |
| 2490 | 130 | 342 | United Kingdom (94%), Lithuania (4%), Australia (1%), USA (1%), Oman (0%) | Europe (98%) | 2020-03-18 to 2020-09-07 | Inactive | TTGCGGGTAC | GR |
| 2532 | 85 | 107 | India (45%), Saudi Arabia (22%), Nigeria (5%), Bangladesh (5%), Belgium (4%) | Asia (72%) | 2020-03-06 to 2020-08-04 | Inactive | CCATGGGCGC | S |
| 2566 | 111 | 200 | USA (100%), Canada (0%) | North America (100%) | 2020-03-13 to 2020-08-11 | Inactive | TTGCGTGTGC | GH |
| 2574 | 156 | 395 | United Kingdom (97%), Switzerland (2%), Iceland (1%), Taiwan (0%), Denmark (0%) | Europe (99%) | 2020-03-07 to 2020-06-23 | Inactive | TTGCGGGTGC | G |
| 2649 | 60 | 98 | USA (80%), China (8%), South Korea (5%), Vietnam (3%), Canada (2%) | North America (82%) | 2020-01-15 to 2020-05-15 | Inactive | CCATGGGCGC | S |
| 2774 | 24 | 39 | USA (100%) | North America (100%) | 2020-03-09 to 2020-05-01 | Inactive | CCACTGTTGC | V |
| 3186 | 59 | 96 | USA (100%) | North America (100%) | 2020-03-27 to 2020-07-18 | Inactive | TTGCGTGTGC | GH |
| 3297 | 28 | 41 | USA (85%), Australia (5%), New Zealand (5%), Canada (2%), Israel (2%) | North America (88%) | 2020-03-14 to 2020-07-23 | Inactive | TTGCGTGTGC | GH |
| 3530 | 190 | 320 | USA (82%), New Zealand (12%), Canada (3%), India (2%), United Kingdom (1%) | North America (85%) | 2020-03-13 to 2020-09-28 | Quiet | TTGCGTGTGC | GH |
| **3859** | 97 | 280 | United Kingdom (98%), Norway (2%), Israel (0%) | Europe (100%) | 2020-04-13 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 4313 | 34 | 48 | United Kingdom (42%), Australia (31%), Spain (6%), USA (4%), New Zealand (4%) | Europe (56%) | 2020-02-28 to 2020-06-14 | Inactive | CCACTGTTGC | V |
| 4669 | 101 | 145 | USA (62%), Russia (10%), United Kingdom (6%), Norway (5%), Spain (3%) | North America (62%) | 2020-03-16 to 2020-09-06 | Inactive | TTGCGGGTGC | G |
| 4713 | 44 | 70 | Singapore (100%) | Asia (100%) | 2020-04-04 to 2020-08-29 | Inactive | CCACTGGTGC | Not Applicaple |
| 4971 | 57 | 111 | USA (100%) | North America (100%) | 2020-04-06 to 2020-08-12 | Inactive | TTGCGTGTGC | GH |
| **5447** | 577 | 948 | United Kingdom (52%), India (25%), Saudi Arabia (5%), Canada (5%), Norway (2%) | Europe (58%) | 2020-02-16 to 2020-10-11 | **Active** | TTGCGTGTGC | GH |
| 6331 | 58 | 121 | United Kingdom (91%), Australia (3%), Portugal (2%), USA (1%), New Zealand (1%) | Europe (94%) | 2020-03-13 to 2020-08-24 | Inactive | TTGCGGGTAC | GR |
| 6360 | 43 | 64 | United Arab Emirates (36%), United Kingdom (23%), South Korea (8%), Australia (6%), Sweden (5%) | Asia (52%) | 2020-03-17 to 2020-09-07 | Inactive | CCATGGGCGC | S |
| 6620 | 38 | 107 | USA (97%), Luxembourg (2%), Russia (1%) | North America (97%) | 2020-03-27 to 2020-09-01 | Inactive | TTGCGTGTGC | GH |
| 7363 | 26 | 39 | United Kingdom (100%) | Europe (100%) | 2020-03-24 to 2020-07-16 | Inactive | TTGCGGGTAC | GR |
| 8626 | 27 | 45 | India (96%), Singapore (2%), USA (2%) | Asia (98%) | 2020-04-20 to 2020-09-08 | Inactive | TTGCGGGTAC | GR |
| 8902 | 33 | 92 | USA (98%), United Kingdom (1%), South Africa (1%) | North America (98%) | 2020-04-15 to 2020-08-07 | Inactive | TTGCGGGTAC | GR |
| 9238 | 35 | 46 | India (96%), United Kingdom (2%), Sweden (2%) | Asia (96%) | 2020-05-11 to 2020-08-19 | Inactive | TTGCGGGTAC | GR |
| 9505 | 37 | 102 | United Kingdom (99%), Portugal (1%) | Europe (100%) | 2020-03-13 to 2020-09-09 | Inactive | TTGCGGGTAC | GR |
| 9581 | 43 | 59 | USA (98%), United Kingdom (2%) | North America (98%) | 2020-06-19 to 2020-09-18 | Inactive | TTGCGTGTGC | GH |
| 9734 | 95 | 169 | Japan (34%), USA (33%), China (5%), Australia (5%), Mali (5%) | Asia (48%) | 2020-01-23 to 2020-06-15 | Inactive | CCATGGGCGC | S |
| 9999 | 110 | 216 | Netherlands (37%), France (12%), United Kingdom (12%), Spain (9%), Belgium (6%) | Europe (86%) | 2020-02-29 to 2020-06-24 | Inactive | TTGCGTGTGC | GH |
| 10221 | 185 | 292 | USA (99%), Mexico (1%), South Korea (0%) | North America (100%) | 2020-03-23 to 2020-09-22 | Quiet | TTGCGGGTGC | G |
| 12210 | 38 | 91 | USA (100%) | North America (100%) | 2020-04-30 to 2020-06-09 | Inactive | TTGCGTGTGC | GH |
| 12995 | 890 | 3409 | Australia (100%) | Oceania (100%) | 2020-03-19 to 2020-09-18 | Inactive | TTGCGGGTAC | GR |
| 13180 | 42 | 126 | United Kingdom (100%) | Europe (100%) | 2020-04-21 to 2020-08-27 | Inactive | TTGCGGGTAC | GR |
| 13208 | 51 | 70 | India (100%) | Asia (100%) | 2020-04-26 to 2020-06-25 | Inactive | TTGCGTGTGC | GH |
| 13245 | 42 | 91 | United Kingdom (97%), Bangladesh (1%), India (1%), South Africa (1%) | Europe (97%) | 2020-03-27 to 2020-08-31 | Inactive | TTGCGGGTAC | GR |
| 13264 | 52 | 89 | USA (78%), Norway (20%), Serbia (1%), Ireland (1%) | North America (78%) | 2020-04-21 to 2020-09-14 | Inactive | TTGCGGGTAC | GR |
| 13301 | 71 | 144 | USA (100%) | North America (100%) | 2020-04-09 to 2020-09-16 | Inactive | TTGCGGGTGC | G |
| 13389 | 36 | 153 | United Kingdom (100%) | Europe (100%) | 2020-06-02 to 2020-10-02 | Quiet | TTGCGGGTAC | GR |
| 13413 | 120 | 158 | South Africa (99%), Singapore (1%) | Africa (99%) | 2020-06-14 to 2020-09-14 | Inactive | TTGCGGGTAC | GR |
| 15279 | 141 | 460 | South Korea (99%), Belgium (0%), USA (0%), France (0%) | Asia (99%) | 2020-03-14 to 2020-08-11 | Inactive | TTGCGTGTGC | GH |
| 16416 | 22 | 22 | Saudi Arabia (95%), India (5%) | Asia (100%) | 2020-04-18 to 2020-06-19 | Inactive | TTACGTGTGC | Not Applicaple |
| 16909 | 49 | 54 | South Africa (100%) | Africa (100%) | 2020-06-19 to 2020-08-25 | Inactive | TTGCGGGTAC | GR |
| 16987 | 51 | 97 | USA (100%) | North America (100%) | 2020-06-16 to 2020-09-16 | Inactive | TTGCGTGTGC | GH |
| 17002 | 27 | 40 | USA (92%), Japan (2%), Canada (2%), United Kingdom (2%) | North America (95%) | 2020-03-19 to 2020-08-19 | Inactive | TTGCGGGTAC | GR |
| 17027 | 102 | 149 | USA (93%), United Kingdom (5%), Canada (1%), Netherlands (1%) | North America (94%) | 2020-06-15 to 2020-09-30 | Quiet | TTGCGGGTGC | G |
| 17444 | 68 | 160 | USA (99%), Gambia (1%) | North America (99%) | 2020-03-11 to 2020-09-29 | Quiet | TTGCGTGTGC | GH |
| **17516** | 39 | 164 | Australia (100%) | Oceania (100%) | 2020-07-13 to 2020-10-12 | **Active** | TTGCGGGTAC | GR |
| **18372** | 82 | 125 | United Kingdom (74%), USA (20%), Russia (2%), Spain (1%), Belgium (1%) | Europe (78%) | 2020-03-22 to 2020-10-05 | **Active** | TTGCGGGTAC | GR |
| 19653 | 67 | 204 | United Kingdom (99%), USA (1%) | Europe (99%) | 2020-04-11 to 2020-09-16 | Inactive | TTGCGGGTAC | GR |
| **20544** | 37 | 106 | United Kingdom (100%) | Europe (100%) | 2020-05-05 to 2020-10-05 | **Active** | TTGCGGGTAC | GR |
| 21210 | 180 | 298 | USA (99%), United Kingdom (1%) | North America (99%) | 2020-04-12 to 2020-09-30 | Quiet | TTGCGTGTGC | GH |
| **21976** | 84 | 134 | United Kingdom (48%), South Africa (45%), India (6%), USA (1%) | Europe (48%) | 2020-05-21 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 22075 | 55 | 173 | United Kingdom (99%), USA (1%), Sweden (1%) | Europe (99%) | 2020-04-14 to 2020-09-09 | Inactive | TTGCGGGTAC | GR |
| **22279** | 54 | 117 | United Kingdom (99%), USA (1%) | Europe (99%) | 2020-06-09 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 22280 | 35 | 63 | USA (100%) | North America (100%) | 2020-06-09 to 2020-08-26 | Inactive | TTGCGTGTGC | GH |
| 22318 | 123 | 473 | Australia (100%) | Oceania (100%) | 2020-06-09 to 2020-09-14 | Inactive | TTGCGGGTAC | GR |
| 23032 | 82 | 103 | USA (100%) | North America (100%) | 2020-03-28 to 2020-09-24 | Quiet | TTGCGTGTGC | GH |
| **23107** | 67 | 173 | United Kingdom (100%) | Europe (100%) | 2020-06-15 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 24039 | 24 | 152 | Australia (100%) | Oceania (100%) | 2020-06-24 to 2020-08-14 | Inactive | TTGCGGGTAC | GR |
| 24502 | 41 | 68 | USA (100%) | North America (100%) | 2020-06-28 to 2020-09-23 | Quiet | TTGCGTGTGC | GH |
| 25251 | 24 | 29 | South Africa (100%) | Africa (100%) | 2020-07-01 to 2020-08-16 | Inactive | TTGCGGGTAC | GR |
| 25297 | 66 | 257 | Australia (100%), Ukraine (0%) | Oceania (100%) | 2020-07-06 to 2020-09-10 | Inactive | TTGCGGGTAC | GR |
| 25470 | 25 | 84 | Australia (94%), United Kingdom (6%) | Oceania (94%) | 2020-07-08 to 2020-10-01 | Quiet | TTGCGGGTAC | GR |
| **25545** | 121 | 236 | United Kingdom (74%), Belgium (19%), Netherlands (3%), France (2%), Germany (1%) | Europe (100%) | 2020-07-09 to 2020-10-06 | **Active** | TTGCGGGTGC | G |
| **25780** | 22 | 60 | United Kingdom (95%), New Zealand (3%), USA (2%) | Europe (95%) | 2020-04-06 to 2020-10-05 | **Active** | TTGCGGGTAC | GR |
| 26286 | 39 | 138 | United Kingdom (99%), Bangladesh (1%) | Europe (99%) | 2020-07-14 to 2020-08-28 | Inactive | TTGCGGGTAC | GR |
| **26377** | 377 | 860 | United Kingdom (92%), Ireland (3%), Netherlands (2%), Spain (2%), Latvia (1%) | Europe (100%) | 2020-07-18 to 2020-10-13 | **Active** | TTGCGGGTGT | GV |
| **26711** | 269 | 669 | United Kingdom (100%) | Europe (100%) | 2020-07-21 to 2020-10-08 | **Active** | TTGCTGGTAC | GR |
| **26754** | 248 | 519 | United Kingdom (85%), Norway (11%), Netherlands (1%), Spain (1%), France (1%) | Europe (100%) | 2020-06-20 to 2020-10-11 | **Active** | TTGCGGGTGT | GV |
| 26806 | 55 | 115 | United Kingdom (57%), France (20%), Netherlands (15%), Norway (8%) | Europe (100%) | 2020-07-22 to 2020-10-01 | Quiet | TTGCGTGTGC | GH |
| 26989 | 77 | 149 | United Kingdom (95%), Montenegro (1%), France (1%), Italy (1%), Russia (1%) | Europe (99%) | 2020-04-09 to 2020-09-26 | Quiet | TTGCGGGTAC | GR |
| **27413** | 64 | 245 | United Kingdom (100%) | Europe (100%) | 2020-07-28 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 27456 | 80 | 139 | United Kingdom (57%), France (37%), Netherlands (5%), Spain (1%), Belgium (1%) | Europe (100%) | 2020-07-29 to 2020-10-01 | Quiet | TTGCGTGTGC | GH |
| 27569 | 66 | 104 | United Kingdom (62%), Norway (20%), Czech Republic (6%), South Korea (4%), India (2%) | Europe (94%) | 2020-06-18 to 2020-09-28 | Quiet | TTGCGGGTAC | GR |
| 27578 | 30 | 82 | United Kingdom (100%) | Europe (100%) | 2020-04-13 to 2020-10-02 | Quiet | TTGCGGGTAC | GR |
| 27666 | 41 | 68 | United Kingdom (88%), France (6%), Spain (3%), Netherlands (3%) | Europe (100%) | 2020-07-31 to 2020-09-10 | Inactive | TTGCGGGTAC | GR |
| **27693** | 487 | 1296 | United Kingdom (99%), Netherlands (0%), Spain (0%), Ireland (0%), Hong Kong (0%) | Europe (100%) | 2020-07-31 to 2020-10-10 | **Active** | TTGCGGGTGT | GV |
| 27698 | 34 | 41 | United Kingdom (100%) | Europe (100%) | 2020-07-15 to 2020-09-28 | Quiet | TTGCGTGTGC | GH |
| **27700** | 96 | 210 | United Kingdom (99%), Norway (1%) | Europe (100%) | 2020-07-31 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 27736 | 84 | 164 | Netherlands (96%), United Kingdom (4%) | Europe (100%) | 2020-04-24 to 2020-09-20 | Quiet | TTGCGTGTGC | GH |
| **27950** | 78 | 198 | United Kingdom (97%), Netherlands (2%), New Zealand (1%) | Europe (99%) | 2020-08-04 to 2020-10-08 | **Active** | TTGCGGGTGT | GV |
| **28012** | 83 | 222 | United Kingdom (100%) | Europe (100%) | 2020-08-04 to 2020-10-06 | **Active** | TTGCGGGTGT | GV |
| 28019 | 102 | 241 | United Kingdom (91%), Ireland (3%), Malta (2%), France (1%), Netherlands (1%) | Europe (100%) | 2020-08-04 to 2020-10-01 | Quiet | TTGCGTGTGC | GH |
| **28179** | 322 | 803 | United Kingdom (100%) | Europe (100%) | 2020-06-02 to 2020-10-10 | **Active** | TTGCGGGTAC | GR |
| **28445** | 129 | 338 | United Kingdom (90%), Norway (8%), Netherlands (1%), France (1%), Sweden (0%) | Europe (100%) | 2020-08-08 to 2020-10-08 | **Active** | TTGCGTGTGC | GH |
| **28513** | 47 | 121 | United Kingdom (99%), Australia (1%) | Europe (99%) | 2020-03-24 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **28786** | 83 | 176 | United Kingdom (100%) | Europe (100%) | 2020-08-11 to 2020-10-08 | **Active** | TTGCGGGTGC | G |
| 28825 | 72 | 129 | United Kingdom (94%), France (6%) | Europe (100%) | 2020-08-02 to 2020-10-02 | Quiet | TTGCGGGTGT | GV |
| 28987 | 50 | 155 | United Kingdom (100%) | Europe (100%) | 2020-06-01 to 2020-09-25 | Quiet | TTGCGGGTAC | GR |
| **29259** | 72 | 173 | United Kingdom (93%), Netherlands (7%) | Europe (100%) | 2020-08-05 to 2020-10-06 | **Active** | TTGCGGGTGT | GV |
| **29310** | 27 | 76 | United Kingdom (99%), Ireland (1%) | Europe (100%) | 2020-08-17 to 2020-10-07 | **Active** | TTGCGGGTGT | GV |
| **29423** | 71 | 138 | United Kingdom (99%), Switzerland (1%) | Europe (100%) | 2020-05-19 to 2020-10-06 | **Active** | TTGCGGGTGC | G |
| **29516** | 46 | 128 | United Kingdom (98%), Netherlands (2%) | Europe (100%) | 2020-08-19 to 2020-10-05 | **Active** | TTGCGGGTAC | GR |
| **29952** | 48 | 119 | United Kingdom (100%) | Europe (100%) | 2020-06-08 to 2020-10-06 | **Active** | TTGCGGGTGC | G |
| **30174** | 72 | 156 | United Kingdom (90%), Russia (9%), Bangladesh (1%) | Europe (99%) | 2020-06-07 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| 30180 | 25 | 35 | Netherlands (91%), United Kingdom (9%) | Europe (100%) | 2020-08-25 to 2020-10-01 | Quiet | TTGCGGGTGC | G |
| **30362** | 30 | 117 | United Kingdom (100%) | Europe (100%) | 2020-08-27 to 2020-10-10 | **Active** | TTGCGGGTGT | GV |
| **30431** | 33 | 68 | United Kingdom (100%) | Europe (100%) | 2020-08-28 to 2020-10-06 | **Active** | TTGCGGGTAT | GR |
| **30498** | 29 | 85 | United Kingdom (100%) | Europe (100%) | 2020-08-28 to 2020-10-06 | **Active** | TTGCTGGTAC | GR |
| **30499** | 44 | 106 | United Kingdom (100%) | Europe (100%) | 2020-07-17 to 2020-10-06 | **Active** | TTGCGGGTAC | GR |
| **31179** | 228 | 618 | United Kingdom (100%), Spain (0%) | Europe (100%) | 2020-09-01 to 2020-10-10 | **Active** | TTGCGGGTGT | GV |
| **31744** | 83 | 182 | United Kingdom (100%) | Europe (100%) | 2020-09-08 to 2020-10-09 | **Active** | TTGCGGGTGT | GV |
| **31942** | 88 | 245 | United Kingdom (100%) | Europe (100%) | 2020-09-02 to 2020-10-10 | **Active** | TTGCGGGTGT | GV |
