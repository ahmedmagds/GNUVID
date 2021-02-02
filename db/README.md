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

**The table below shows summary information of the 406 Clonal Complexes (CCs).**

The "Most common 5 countries" and "Most common Region" columns show the five countries and the region, respectively, with the most sequences from each Clonal Complex. Starting from the DB update (01/06/2021), the GISAID clades are reported for each CC for easier correlation between the two systems.

**GNUVID now assigns the three new variants:**
- Brazilian P.1 lineage (a.k.a. 20J/501Y.V3).
- South African B.1.351 lineage (a.k.a. 20H/501Y.V2).
- UK B.1.1.7 lineage (a.k.a. 20I/501Y.V1 Variant of Concern (VOC) 202012/01).


| Clonal Complex | Number of STs | Number of isolates | Most common 5 countries | Most common Region | Date range | Status | Variant of Concern (%isolates) | GISAID Clade |
|----------------|---------------|--------------------|-------------------------|--------------------|------------|--------|--------------------------------|--------------|
| 4 | 155 | 505 | USA (35%), China (25%), Lithuania (11%), Singapore (6%), United Arab Emirates (4%) | Asia (47%) | 2019-12-30 to 2020-08-12 | Inactive | Not_VOC (0) | L |
| 16 | 37 | 47 | China (55%), France (15%), Japan (6%), USA (6%), United Arab Emirates (4%) | Asia (74%) | 2020-01-10 to 2020-05-17 | Inactive | Not_VOC (0) | S |
| 67 | 201 | 277 | USA (15%), Australia (14%), United Arab Emirates (13%), Kazakhstan (10%), India (8%) | Asia (51%) | 2020-01-19 to 2020-09-13 | Inactive | Not_VOC (0) | Not Applicaple |
| **255** | 3238 | 5568 | USA (21%), United Kingdom (17%), India (8%), France (6%), Netherlands (5%) | Europe (57%) | 2020-01-24 to 2020-12-26 | **Active** | Not_VOC (0) | G |
| 256 | 952 | 2088 | USA (73%), Canada (8%), China (6%), Australia (3%), Japan (3%) | North America (81%) | 2020-01-05 to 2020-10-13 | Inactive | Not_VOC (0) | S |
| **258** | 6737 | 12935 | USA (66%), Denmark (5%), United Kingdom (5%), Netherlands (4%), France (3%) | North America (69%) | 2020-02-16 to 2020-12-28 | **Active** | Not_VOC (0.007730963) | GH |
| 266 | 72 | 110 | Spain (45%), United Kingdom (17%), Portugal (8%), Peru (5%), USA (5%) | Europe (72%) | 2020-02-23 to 2020-06-22 | Inactive | Not_VOC (0) | S |
| 291 | 163 | 271 | France (22%), USA (21%), Saudi Arabia (15%), United Kingdom (11%), Sweden (6%) | Europe (52%) | 2020-02-26 to 2020-12-04 | Inactive | Not_VOC (0) | GH |
| 297 | 403 | 612 | USA (28%), United Kingdom (17%), Belgium (16%), Russia (6%), Denmark (4%) | Europe (63%) | 2020-02-26 to 2020-12-20 | Quiet | Not_VOC (0) | GR |
| **300** | 10460 | 17836 | United Kingdom (38%), USA (16%), Russia (4%), Denmark (4%), India (3%) | Europe (64%) | 2020-01-24 to 2020-12-28 | **Active** | Not_VOC (0) | GR |
| 301 | 217 | 577 | Spain (32%), United Kingdom (16%), USA (7%), Chile (4%), Portugal (3%) | Europe (69%) | 2020-02-26 to 2020-12-04 | Inactive | Not_VOC (0) | G |
| 305 | 71 | 156 | United Kingdom (65%), USA (17%), Australia (8%), Chile (3%), Poland (3%) | Europe (71%) | 2020-02-22 to 2020-06-23 | Inactive | Not_VOC (0) | G |
| 317 | 257 | 556 | USA (29%), Japan (23%), United Kingdom (15%), France (4%), Spain (3%) | Europe (36%) | 2020-02-26 to 2020-12-03 | Inactive | Not_VOC (0) | GR |
| **333** | 158 | 396 | USA (53%), Canada (11%), France (7%), Slovenia (7%), United Kingdom (6%) | North America (63%) | 2020-02-29 to 2020-12-23 | **Active** | Not_VOC (0) | GH |
| 336 | 30 | 38 | Australia (97%), United Arab Emirates (3%) | Oceania (97%) | 2020-02-25 to 2020-04-04 | Inactive | Not_VOC (0) | Not Applicaple |
| **338** | 210 | 487 | USA (69%), Denmark (6%), Canada (5%), United Kingdom (4%), Colombia (2%) | North America (74%) | 2020-02-29 to 2020-12-24 | **Active** | Not_VOC (0) | GH |
| 348 | 237 | 465 | Netherlands (12%), United Kingdom (11%), Peru (8%), Italy (8%), South Africa (6%) | Europe (67%) | 2020-02-22 to 2020-11-30 | Inactive | Not_VOC (0) | G |
| 355 | 126 | 269 | Spain (59%), Kazakhstan (7%), Portugal (4%), Netherlands (4%), United Kingdom (4%) | Europe (77%) | 2020-02-25 to 2020-07-13 | Inactive | Not_VOC (0) | S |
| 358 | 79 | 221 | Portugal (72%), United Kingdom (9%), New Zealand (5%), Netherlands (4%), USA (3%) | Europe (89%) | 2020-02-21 to 2020-11-30 | Inactive | Not_VOC (0) | G |
| 369 | 226 | 511 | United Kingdom (23%), Netherlands (22%), Sweden (10%), Iceland (9%), Austria (5%) | Europe (89%) | 2020-02-26 to 2020-06-19 | Inactive | Not_VOC (0) | GR |
| **399** | 856 | 1521 | United Kingdom (48%), Peru (10%), Denmark (7%), Belgium (5%), Canada (4%) | Europe (73%) | 2020-03-02 to 2020-12-29 | **Active** | Not_VOC (0) | GR |
| 439 | 88 | 138 | USA (85%), China (6%), South Korea (4%), Vietnam (2%), Hong Kong (1%) | North America (86%) | 2020-01-15 to 2020-05-15 | Inactive | Not_VOC (0) | S |
| 454 | 273 | 639 | France (23%), Switzerland (21%), Belgium (17%), United Kingdom (7%), Suriname (6%) | Europe (81%) | 2020-03-03 to 2020-12-14 | Quiet | Not_VOC (0) | G |
| **498** | 305 | 586 | USA (46%), United Kingdom (31%), Denmark (5%), Mexico (4%), South Africa (2%) | North America (51%) | 2020-03-05 to 2020-12-26 | **Active** | Not_VOC (0) | G |
| 550 | 915 | 1456 | United Kingdom (37%), USA (13%), South Korea (9%), Australia (6%), Iceland (5%) | Europe (61%) | 2020-01-22 to 2020-07-15 | Inactive | Not_VOC (0) | V |
| 551 | 50 | 141 | United Kingdom (35%), USA (19%), Netherlands (9%), Australia (7%), Belgium (5%) | Europe (63%) | 2020-02-26 to 2020-05-18 | Inactive | Not_VOC (0) | V |
| 559 | 53 | 120 | France (82%), Germany (5%), USA (2%), Luxembourg (2%), Portugal (2%) | Europe (92%) | 2020-03-06 to 2020-07-01 | Inactive | Not_VOC (0) | GH |
| 623 | 110 | 266 | USA (67%), Australia (20%), Iceland (6%), Canada (3%), Taiwan (1%) | North America (71%) | 2020-03-05 to 2020-07-22 | Inactive | Not_VOC (0) | S |
| 645 | 91 | 178 | USA (74%), Australia (17%), United Kingdom (4%), New Zealand (1%), Canada (1%) | North America (76%) | 2020-03-05 to 2020-04-15 | Inactive | Not_VOC (0) | S |
| 681 | 168 | 305 | Netherlands (76%), South Africa (5%), USA (3%), Austria (3%), Iceland (2%) | Europe (89%) | 2020-03-08 to 2020-11-07 | Inactive | Not_VOC (0) | G |
| 750 | 59 | 88 | China (52%), Singapore (8%), USA (8%), Indonesia (6%), India (5%) | Asia (80%) | 2019-12-30 to 2020-12-03 | Inactive | Not_VOC (0) | L |
| 768 | 1011 | 1785 | USA (97%), Canada (2%), Australia (1%), Nigeria (0%), New Zealand (0%) | North America (99%) | 2020-03-09 to 2020-12-17 | Quiet | Not_VOC (0) | GH |
| 780 | 196 | 408 | United Kingdom (96%), Canada (1%), United Arab Emirates (1%), Uganda (1%), Iceland (0%) | Europe (97%) | 2020-03-02 to 2020-08-19 | Inactive | Not_VOC (0) | GR |
| **800** | 473 | 743 | Saudi Arabia (38%), United Kingdom (21%), India (17%), Norway (5%), Indonesia (5%) | Asia (64%) | 2020-02-03 to 2020-12-28 | **Active** | Not_VOC (0) | GH |
| 834 | 48 | 90 | United Kingdom (64%), USA (10%), Australia (9%), Jordan (4%), Canada (3%) | Europe (71%) | 2020-03-09 to 2020-07-31 | Inactive | Not_VOC (0) | V |
| 844 | 121 | 270 | USA (67%), Israel (14%), United Kingdom (8%), Canada (3%), Argentina (3%) | North America (71%) | 2020-03-09 to 2020-12-22 | Quiet | Not_VOC (0) | GH |
| 927 | 51 | 135 | India (35%), Malaysia (13%), USA (11%), Australia (7%), Singapore (7%) | Asia (69%) | 2020-03-07 to 2020-08-31 | Inactive | Not_VOC (0) | Not Applicaple |
| 985 | 277 | 514 | United Kingdom (81%), USA (9%), Australia (2%), Singapore (1%), Peru (1%) | Europe (84%) | 2020-03-06 to 2020-09-20 | Inactive | Not_VOC (0) | G |
| 1043 | 83 | 224 | USA (98%), New Zealand (1%), Australia (1%) | North America (98%) | 2020-03-12 to 2020-10-14 | Inactive | Not_VOC (0) | GH |
| 1063 | 312 | 543 | Sweden (32%), Finland (28%), Denmark (17%), United Kingdom (15%), USA (3%) | Europe (95%) | 2020-03-08 to 2020-10-08 | Inactive | Not_VOC (0) | GH |
| 1085 | 72 | 167 | Denmark (97%), Singapore (2%), New Zealand (1%), United Kingdom (1%) | Europe (98%) | 2020-03-09 to 2020-06-15 | Inactive | Not_VOC (0) | GH |
| 1094 | 28 | 56 | USA (98%), Australia (2%) | North America (98%) | 2020-03-10 to 2020-06-29 | Inactive | Not_VOC (0) | GH |
| 1102 | 434 | 593 | Brazil (58%), Chile (23%), USA (5%), Uruguay (4%), Australia (2%) | South America (87%) | 2020-02-27 to 2020-12-06 | Quiet | Not_VOC (0) | GR |
| 1142 | 32 | 67 | United Kingdom (52%), Austria (19%), Denmark (10%), Finland (6%), India (6%) | Europe (93%) | 2020-03-13 to 2020-07-06 | Inactive | Not_VOC (0) | GH |
| 1148 | 52 | 98 | United Kingdom (90%), Canada (4%), USA (4%), China (1%), Germany (1%) | Europe (91%) | 2020-01-23 to 2020-06-23 | Inactive | Not_VOC (0) | L |
| 1179 | 431 | 606 | Singapore (61%), India (17%), Malaysia (9%), Australia (6%), USA (2%) | Asia (90%) | 2020-03-04 to 2020-10-06 | Inactive | Not_VOC (0) | Not Applicaple |
| 1189 | 185 | 334 | USA (95%), Romania (5%), United Kingdom (0%) | North America (95%) | 2020-03-13 to 2020-12-15 | Quiet | Not_VOC (0) | GH |
| 1208 | 68 | 99 | United Kingdom (69%), Russia (7%), South Africa (6%), USA (4%), Iceland (3%) | Europe (84%) | 2020-03-14 to 2020-11-14 | Inactive | Not_VOC (0) | GR |
| 1222 | 21 | 42 | USA (83%), Canada (7%), Australia (5%), Sweden (2%), Belize (2%) | North America (93%) | 2020-03-13 to 2020-05-22 | Inactive | Not_VOC (0) | GH |
| 1240 | 48 | 70 | USA (79%), Belgium (4%), Netherlands (4%), Denmark (3%), Portugal (3%) | North America (80%) | 2020-03-14 to 2020-12-21 | Quiet | Not_VOC (0) | GH |
| 1328 | 217 | 262 | Brazil (83%), United Kingdom (6%), Portugal (3%), Australia (3%), China (1%) | South America (84%) | 2020-03-15 to 2020-12-17 | Quiet | Not_VOC (0) | GR |
| **1455** | 181 | 283 | United Kingdom (70%), Denmark (11%), France (6%), Ireland (5%), Italy (3%) | Europe (100%) | 2020-03-16 to 2020-12-23 | **Active** | Not_VOC (0) | G |
| 1507 | 933 | 1468 | United Kingdom (27%), USA (15%), Netherlands (12%), Japan (10%), China (9%) | Europe (52%) | 2019-12-24 to 2020-12-04 | Inactive | Not_VOC (0) | L |
| 1508 | 57 | 106 | USA (94%), Taiwan (2%), South Korea (2%), United Kingdom (1%), Canada (1%) | North America (95%) | 2020-03-12 to 2020-06-26 | Inactive | Not_VOC (0) | S |
| 1540 | 56 | 87 | United Kingdom (69%), USA (9%), Netherlands (3%), France (2%), Vietnam (2%) | Europe (83%) | 2020-03-17 to 2020-11-23 | Inactive | Not_VOC (0) | GR |
| 1582 | 49 | 96 | USA (98%), Taiwan (1%), United Arab Emirates (1%) | North America (98%) | 2020-03-11 to 2020-05-31 | Inactive | Not_VOC (0) | S |
| 1726 | 33 | 47 | United Kingdom (34%), New Zealand (28%), Australia (19%), USA (4%), Taiwan (2%) | Oceania (47%) | 2020-03-03 to 2020-04-22 | Inactive | Not_VOC (0) | V |
| 1824 | 75 | 91 | USA (89%), South Africa (4%), France (1%), Hong Kong (1%), Vietnam (1%) | North America (90%) | 2020-03-13 to 2020-12-02 | Inactive | Not_VOC (0) | GR |
| **1852** | 146 | 231 | United Kingdom (47%), USA (17%), Czech Republic (4%), Denmark (4%), Portugal (4%) | Europe (70%) | 2020-03-13 to 2020-12-24 | **Active** | Not_VOC (0) | GR |
| 2165 | 63 | 133 | Denmark (71%), United Kingdom (17%), Japan (2%), Norway (2%), Hungary (2%) | Europe (97%) | 2020-03-18 to 2020-12-18 | Quiet | Not_VOC (0) | GR |
| 2175 | 74 | 236 | Australia (89%), United Kingdom (6%), USA (1%), Israel (1%), Peru (1%) | Oceania (90%) | 2020-03-09 to 2020-04-27 | Inactive | Not_VOC (0) | S |
| 2445 | 74 | 157 | Canada (49%), United Kingdom (25%), France (14%), Belgium (10%), Switzerland (1%) | Europe (50%) | 2020-03-04 to 2020-06-10 | Inactive | Not_VOC (0) | G |
| 2490 | 151 | 377 | United Kingdom (94%), Lithuania (3%), Australia (1%), USA (1%), Oman (0%) | Europe (98%) | 2020-03-18 to 2020-11-13 | Inactive | Not_VOC (0) | GR |
| 2532 | 93 | 117 | India (37%), Saudi Arabia (26%), Nigeria (8%), Bangladesh (4%), Belgium (3%) | Asia (68%) | 2020-03-06 to 2020-12-14 | Quiet | Not_VOC (0) | S |
| 2574 | 168 | 414 | United Kingdom (92%), Ireland (3%), France (2%), Switzerland (2%), Iceland (1%) | Europe (100%) | 2020-03-07 to 2020-06-23 | Inactive | Not_VOC (0) | G |
| 2774 | 25 | 42 | USA (100%) | North America (100%) | 2020-03-09 to 2020-05-01 | Inactive | Not_VOC (0) | V |
| 3186 | 53 | 86 | USA (100%) | North America (100%) | 2020-03-13 to 2020-08-17 | Inactive | Not_VOC (0) | GH |
| 3297 | 30 | 46 | USA (85%), Australia (4%), New Zealand (4%), Canada (2%), Israel (2%) | North America (87%) | 2020-03-12 to 2020-08-12 | Inactive | Not_VOC (0) | GH |
| 3530 | 368 | 583 | USA (85%), New Zealand (7%), Canada (6%), India (1%), Australia (1%) | North America (91%) | 2020-03-12 to 2020-12-22 | Quiet | Not_VOC (0) | GH |
| 3859 | 118 | 306 | United Kingdom (96%), Norway (3%), Denmark (0%), Sweden (0%), Russia (0%) | Europe (100%) | 2020-04-13 to 2020-11-09 | Inactive | Not_VOC (0) | GR |
| 4313 | 40 | 59 | Australia (39%), United Kingdom (36%), Spain (5%), Slovenia (5%), USA (3%) | Europe (51%) | 2020-02-28 to 2020-06-14 | Inactive | Not_VOC (0) | V |
| **4326** | 96 | 137 | Serbia (22%), Denmark (21%), Hungary (13%), North Macedonia (10%), United Kingdom (10%) | Europe (96%) | 2020-03-24 to 2020-12-28 | **Active** | Not_VOC (0) | GR |
| 4669 | 165 | 265 | USA (62%), United Kingdom (9%), Austria (6%), Russia (5%), Mexico (3%) | North America (66%) | 2020-03-13 to 2020-12-15 | Quiet | Not_VOC (0) | G |
| 4713 | 98 | 171 | Singapore (100%) | Asia (100%) | 2020-04-03 to 2020-08-29 | Inactive | Not_VOC (0) | Not Applicaple |
| 4971 | 79 | 141 | USA (99%), Australia (1%) | North America (99%) | 2020-04-06 to 2020-11-09 | Inactive | Not_VOC (0) | GH |
| 5473 | 59 | 98 | USA (99%), United Kingdom (1%) | North America (99%) | 2020-04-01 to 2020-11-04 | Inactive | Not_VOC (0) | GH |
| 6298 | 32 | 36 | Germany (89%), USA (6%), Bosnia and Herzegovina (3%), Denmark (3%) | Europe (94%) | 2020-03-16 to 2020-05-20 | Inactive | Not_VOC (0) | G |
| 6331 | 67 | 131 | United Kingdom (85%), Australia (5%), Russia (2%), USA (2%), Portugal (2%) | Europe (92%) | 2020-03-13 to 2020-11-09 | Inactive | Not_VOC (0) | GR |
| 6360 | 242 | 386 | United Arab Emirates (56%), Denmark (17%), Uganda (10%), United Kingdom (9%), South Korea (2%) | Asia (59%) | 2020-03-17 to 2020-12-21 | Quiet | Not_VOC (0) | S |
| **6410** | 66 | 80 | USA (79%), India (6%), Sweden (5%), Israel (4%), United Kingdom (1%) | North America (80%) | 2020-03-24 to 2020-12-26 | **Active** | Not_VOC (0) | GH |
| 7363 | 27 | 41 | United Kingdom (98%), Australia (2%) | Europe (98%) | 2020-03-24 to 2020-07-16 | Inactive | Not_VOC (0) | GR |
| 7374 | 156 | 221 | India (88%), United Kingdom (4%), South Africa (2%), Russia (2%), Bahrain (2%) | Asia (91%) | 2020-04-05 to 2020-12-12 | Quiet | Not_VOC (0) | GR |
| 8410 | 57 | 83 | United Arab Emirates (90%), USA (5%), United Kingdom (2%), Sweden (1%), Portugal (1%) | Asia (90%) | 2020-03-25 to 2020-09-16 | Inactive | Not_VOC (0) | GR |
| 8626 | 36 | 58 | India (76%), United Kingdom (17%), Singapore (2%), USA (2%), Australia (2%) | Asia (79%) | 2020-04-20 to 2020-12-06 | Quiet | Not_VOC (0) | GR |
| 8902 | 33 | 92 | USA (98%), United Kingdom (1%), South Africa (1%) | North America (98%) | 2020-04-15 to 2020-08-07 | Inactive | Not_VOC (0) | GR |
| 9238 | 47 | 67 | India (66%), United Kingdom (21%), USA (6%), Denmark (6%), Sweden (1%) | Asia (66%) | 2020-04-19 to 2020-10-07 | Inactive | Not_VOC (0) | GR |
| 9478 | 40 | 56 | South Africa (62%), United Kingdom (34%), Brazil (2%), USA (2%) | Africa (62%) | 2020-04-07 to 2020-11-19 | Inactive | Not_VOC (0) | GR |
| 9505 | 42 | 108 | United Kingdom (94%), Portugal (2%), South Africa (2%), Netherlands (1%), Denmark (1%) | Europe (98%) | 2020-03-13 to 2020-11-15 | Inactive | Not_VOC (0) | GR |
| 9581 | 83 | 121 | USA (98%), United Kingdom (1%), France (1%) | North America (98%) | 2020-03-23 to 2020-11-12 | Inactive | Not_VOC (0) | GH |
| 9734 | 125 | 215 | USA (29%), Japan (28%), United Arab Emirates (13%), India (5%), Australia (4%) | Asia (52%) | 2020-01-23 to 2020-12-18 | Quiet | Not_VOC (0) | S |
| 9999 | 137 | 258 | Netherlands (31%), France (21%), United Kingdom (10%), Belgium (8%), Spain (8%) | Europe (86%) | 2020-02-29 to 2020-11-29 | Inactive | Not_VOC (0) | GH |
| **10221** | 371 | 578 | USA (96%), Mexico (4%), Norway (0%), South Korea (0%) | North America (100%) | 2020-03-23 to 2020-12-28 | **Active** | Not_VOC (0) | G |
| 10505 | 33 | 45 | Japan (53%), USA (11%), Russia (9%), South Africa (4%), Denmark (4%) | Asia (58%) | 2020-04-01 to 2020-12-13 | Quiet | Not_VOC (0) | GR |
| 12210 | 38 | 91 | USA (100%) | North America (100%) | 2020-04-30 to 2020-06-09 | Inactive | Not_VOC (0) | GH |
| 12995 | 1067 | 4150 | Australia (100%) | Oceania (100%) | 2020-03-19 to 2020-10-17 | Inactive | Not_VOC (0) | GR |
| 13059 | 26 | 33 | Japan (64%), USA (24%), United Kingdom (3%), South Korea (3%), Australia (3%) | Asia (70%) | 2020-05-27 to 2020-10-26 | Inactive | Not_VOC (0) | GR |
| 13180 | 42 | 126 | United Kingdom (100%) | Europe (100%) | 2020-04-21 to 2020-08-27 | Inactive | Not_VOC (0) | GR |
| 13208 | 69 | 110 | India (68%), Norway (31%), United Kingdom (1%) | Asia (68%) | 2020-04-26 to 2020-12-02 | Inactive | Not_VOC (0) | GH |
| 13245 | 47 | 96 | United Kingdom (92%), India (2%), Bangladesh (1%), South Africa (1%), USA (1%) | Europe (94%) | 2020-03-27 to 2020-10-26 | Inactive | Not_VOC (0) | GR |
| 13264 | 78 | 132 | USA (81%), Norway (14%), Sweden (2%), Serbia (2%), Ireland (1%) | North America (81%) | 2020-04-13 to 2020-12-07 | Quiet | Not_VOC (0) | GR |
| 13301 | 135 | 256 | USA (98%), Denmark (2%), Australia (0%), Germany (0%) | North America (98%) | 2020-04-09 to 2020-12-08 | Quiet | Not_VOC (0) | G |
| 13389 | 51 | 173 | United Kingdom (100%) | Europe (100%) | 2020-06-02 to 2020-11-13 | Inactive | Not_VOC (0) | GR |
| 13413 | 195 | 244 | South Africa (98%), Singapore (0%), Serbia (0%), United Kingdom (0%), Denmark (0%) | Africa (98%) | 2020-06-14 to 2020-12-07 | Quiet | Not_VOC (0) | GR |
| 13561 | 64 | 113 | United Kingdom (51%), Denmark (14%), Serbia (13%), Luxembourg (9%), Switzerland (3%) | Europe (98%) | 2020-03-10 to 2020-11-30 | Inactive | Not_VOC (0) | GR |
| 14963 | 24 | 28 | Saudi Arabia (100%) | Asia (100%) | 2020-04-06 to 2020-07-18 | Inactive | Not_VOC (0) | Not Applicaple |
| 15279 | 162 | 507 | South Korea (99%), USA (0%), Belgium (0%), France (0%) | Asia (99%) | 2020-03-14 to 2020-10-08 | Inactive | Not_VOC (0) | GH |
| **15298** | 79 | 111 | USA (31%), India (21%), United Kingdom (20%), Australia (15%), Denmark (4%) | North America (34%) | 2020-05-06 to 2021-01-03 | **Active** | Not_VOC (0) | GR |
| 16681 | 39 | 44 | Costa Rica (98%), Australia (2%) | North America (98%) | 2020-06-18 to 2020-11-26 | Inactive | Not_VOC (0) | GR |
| 16808 | 55 | 105 | United Kingdom (90%), India (9%), United Arab Emirates (1%) | Europe (90%) | 2020-06-07 to 2020-12-20 | Quiet | Not_VOC (0) | GR |
| 16909 | 71 | 82 | South Africa (94%), United Kingdom (4%), Russia (2%) | Africa (94%) | 2020-06-19 to 2020-11-18 | Inactive | Not_VOC (0) | GR |
| 16987 | 256 | 394 | USA (97%), Australia (1%), Canada (1%), Denmark (1%) | North America (98%) | 2020-06-16 to 2020-12-21 | Quiet | Not_VOC (0) | GH |
| 17002 | 34 | 51 | USA (94%), Japan (2%), Canada (2%), United Kingdom (2%) | North America (96%) | 2020-03-19 to 2020-08-19 | Inactive | Not_VOC (0) | GR |
| 17027 | 265 | 386 | USA (90%), United Kingdom (7%), Aruba (1%), Curacao (1%), Canada (0%) | North America (90%) | 2020-06-02 to 2020-12-16 | Quiet | Not_VOC (0) | G |
| 17444 | 147 | 285 | USA (99%), Gambia (0%), South Korea (0%), Australia (0%), Netherlands (0%) | North America (99%) | 2020-03-11 to 2020-12-21 | Quiet | Not_VOC (0) | GH |
| 17466 | 127 | 165 | South Africa (98%), USA (2%) | Africa (98%) | 2020-05-21 to 2020-11-25 | Inactive | Not_VOC (0) | GR |
| 17516 | 57 | 219 | Australia (100%) | Oceania (100%) | 2020-07-13 to 2020-11-02 | Inactive | Not_VOC (0) | Not Applicaple |
| 17607 | 37 | 168 | Australia (100%) | Oceania (100%) | 2020-07-03 to 2020-09-12 | Inactive | Not_VOC (0) | GR |
| 18372 | 111 | 153 | United Kingdom (44%), USA (22%), Denmark (11%), South Africa (7%), Russia (4%) | Europe (65%) | 2020-03-22 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| 18398 | 36 | 58 | United Kingdom (76%), Canada (10%), USA (9%), Gambia (3%), United Arab Emirates (2%) | Europe (76%) | 2020-03-23 to 2020-12-03 | Inactive | Not_VOC (0) | GR |
| 19653 | 80 | 215 | United Kingdom (89%), USA (8%), Russia (3%), Portugal (0%) | Europe (92%) | 2020-04-11 to 2020-11-14 | Inactive | Not_VOC (0) | GR |
| **20133** | 140 | 196 | United Arab Emirates (98%), Hong Kong (1%), United Kingdom (1%) | Asia (99%) | 2020-04-24 to 2020-12-23 | **Active** | Not_VOC (0) | GR |
| 21098 | 48 | 61 | USA (100%) | North America (100%) | 2020-05-18 to 2020-10-19 | Inactive | Not_VOC (0) | GH |
| **21210** | 1077 | 1609 | USA (96%), United Kingdom (1%), Denmark (1%), Australia (1%), Canada (0%) | North America (97%) | 2020-04-11 to 2020-12-28 | **Active** | Not_VOC (0) | GH |
| 22075 | 56 | 174 | United Kingdom (99%), USA (1%), Australia (1%) | Europe (99%) | 2020-04-14 to 2020-09-30 | Inactive | Not_VOC (0) | GR |
| 22279 | 62 | 115 | United Kingdom (99%), USA (1%) | Europe (99%) | 2020-06-09 to 2020-12-16 | Quiet | Not_VOC (0) | GR |
| 22280 | 58 | 95 | USA (97%), Denmark (2%), Canada (1%) | North America (98%) | 2020-05-23 to 2020-11-03 | Inactive | Not_VOC (0) | GH |
| 22318 | 142 | 517 | Australia (100%) | Oceania (100%) | 2020-06-09 to 2020-09-14 | Inactive | Not_VOC (0) | GR |
| 22896 | 49 | 57 | USA (32%), Russia (28%), United Kingdom (16%), India (5%), Norway (4%) | Europe (56%) | 2020-03-26 to 2020-12-09 | Quiet | Not_VOC (0) | GR |
| 23032 | 121 | 160 | USA (100%) | North America (100%) | 2020-03-28 to 2020-11-30 | Inactive | Not_VOC (0) | GH |
| 23107 | 66 | 150 | United Kingdom (99%), United Arab Emirates (1%) | Europe (99%) | 2020-05-17 to 2020-11-27 | Inactive | Not_VOC (0) | GR |
| 23939 | 61 | 184 | USA (98%), Luxembourg (1%), Germany (1%), Russia (1%) | North America (98%) | 2020-03-23 to 2020-09-02 | Inactive | Not_VOC (0) | GH |
| 24039 | 25 | 163 | Australia (100%) | Oceania (100%) | 2020-06-24 to 2020-08-14 | Inactive | Not_VOC (0) | GR |
| 24502 | 84 | 148 | USA (100%) | North America (100%) | 2020-06-28 to 2020-12-21 | Quiet | Not_VOC (0) | GH |
| 24788 | 28 | 102 | Australia (100%) | Oceania (100%) | 2020-06-30 to 2020-08-29 | Inactive | Not_VOC (0) | GR |
| 25251 | 45 | 53 | South Africa (100%) | Africa (100%) | 2020-07-01 to 2020-11-03 | Inactive | Not_VOC (0) | GR |
| 25297 | 91 | 335 | Australia (93%), Denmark (5%), Ukraine (1%), Belgium (1%), Bangladesh (1%) | Oceania (93%) | 2020-07-06 to 2020-12-02 | Inactive | Not_VOC (0) | GR |
| 25300 | 98 | 161 | Denmark (48%), United Kingdom (26%), Russia (18%), Latvia (2%), South Korea (2%) | Europe (98%) | 2020-03-31 to 2020-12-22 | Quiet | Not_VOC (0) | GR |
| **25468** | 90 | 178 | Australia (53%), USA (46%), Canada (1%) | Oceania (53%) | 2020-05-21 to 2021-01-02 | **Active** | Not_VOC (0) | Not Applicaple |
| 25470 | 31 | 114 | Australia (95%), United Kingdom (3%), USA (2%), Denmark (1%) | Oceania (95%) | 2020-06-30 to 2020-09-28 | Inactive | Not_VOC (0) | GR |
| **25545** | 440 | 875 | United Kingdom (29%), Denmark (29%), Belgium (19%), Luxembourg (9%), Netherlands (4%) | Europe (99%) | 2020-07-02 to 2020-12-26 | **Active** | Not_VOC (0) | G |
| 25734 | 29 | 119 | United Kingdom (100%) | Europe (100%) | 2020-07-12 to 2020-09-29 | Inactive | Not_VOC (0) | GR |
| 25780 | 35 | 81 | United Kingdom (95%), New Zealand (2%), USA (1%), Denmark (1%) | Europe (96%) | 2020-04-06 to 2020-12-12 | Quiet | Not_VOC (0) | GR |
| 25988 | 55 | 135 | United Kingdom (100%) | Europe (100%) | 2020-05-05 to 2020-11-23 | Inactive | Not_VOC (0) | GR |
| 26188 | 68 | 108 | Belgium (46%), Luxembourg (33%), Netherlands (13%), Germany (3%), Denmark (2%) | Europe (100%) | 2020-07-16 to 2020-11-29 | Inactive | Not_VOC (0) | GR |
| 26286 | 43 | 142 | United Kingdom (96%), Ireland (3%), Bangladesh (1%) | Europe (99%) | 2020-07-14 to 2020-10-13 | Inactive | Not_VOC (0) | GR |
| 26321 | 29 | 50 | Japan (76%), Luxembourg (10%), Russia (8%), Australia (4%), Thailand (2%) | Asia (78%) | 2020-05-30 to 2020-10-28 | Inactive | Not_VOC (0) | GR |
| **26377** | 1529 | 2975 | United Kingdom (57%), Denmark (32%), Spain (3%), Netherlands (2%), Luxembourg (2%) | Europe (100%) | 2020-07-18 to 2020-12-29 | **Active** | Not_VOC (0) | GV |
| **26477** | 1482 | 2384 | United Kingdom (57%), India (12%), Denmark (6%), Saudi Arabia (5%), Canada (4%) | Europe (69%) | 2020-02-16 to 2020-12-28 | **Active** | Not_VOC (0) | GH |
| 26711 | 572 | 1275 | United Kingdom (92%), Denmark (8%), Portugal (0%), Netherlands (0%), Australia (0%) | Europe (100%) | 2020-07-21 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| **26754** | 962 | 1660 | United Kingdom (63%), Denmark (11%), Netherlands (5%), Spain (4%), Norway (4%) | Europe (100%) | 2020-06-20 to 2020-12-28 | **Active** | Not_VOC (0) | GV |
| 26806 | 102 | 202 | United Kingdom (36%), Denmark (25%), France (20%), Netherlands (9%), Norway (5%) | Europe (100%) | 2020-07-22 to 2020-12-16 | Quiet | Not_VOC (0) | GH |
| 26989 | 89 | 170 | United Kingdom (95%), Montenegro (1%), France (1%), South Africa (1%), Italy (1%) | Europe (99%) | 2020-04-09 to 2020-11-12 | Inactive | Not_VOC (0) | GR |
| **27324** | 86 | 148 | USA (57%), Denmark (32%), United Kingdom (8%), Netherlands (1%), Switzerland (1%) | North America (57%) | 2020-06-28 to 2020-12-23 | **Active** | Not_VOC (0) | G |
| 27413 | 36 | 140 | United Kingdom (100%) | Europe (100%) | 2020-07-28 to 2020-11-16 | Inactive | Not_VOC (0) | GR |
| 27449 | 127 | 273 | United Kingdom (94%), Luxembourg (2%), Belgium (2%), Germany (1%), Netherlands (0%) | Europe (100%) | 2020-07-21 to 2020-12-17 | Quiet | Not_VOC (0) | GV |
| **27456** | 1333 | 2817 | Denmark (42%), France (15%), United Kingdom (15%), Luxembourg (15%), Netherlands (4%) | Europe (99%) | 2020-07-09 to 2020-12-29 | **Active** | Not_VOC (0) | GH |
| **27465** | 93 | 152 | Sweden (44%), Denmark (41%), Norway (7%), United Kingdom (4%), Latvia (4%) | Europe (100%) | 2020-07-06 to 2020-12-23 | **Active** | Not_VOC (0) | GR |
| 27578 | 92 | 186 | United Kingdom (100%) | Europe (100%) | 2020-04-13 to 2020-12-13 | Quiet | Not_VOC (0) | GR |
| 27581 | 96 | 159 | Finland (33%), United Kingdom (26%), France (23%), Denmark (7%), Belgium (6%) | Europe (99%) | 2020-07-30 to 2020-12-18 | Quiet | Not_VOC (0) | GR |
| 27666 | 100 | 157 | United Kingdom (46%), Denmark (24%), France (9%), Belgium (8%), Portugal (5%) | Europe (100%) | 2020-06-01 to 2020-11-30 | Inactive | Not_VOC (0) | GR |
| **27693** | 1608 | 3705 | United Kingdom (98%), Denmark (1%), Ireland (0%), Spain (0%), Germany (0%) | Europe (100%) | 2020-03-21 to 2020-12-27 | **Active** | Not_VOC (0) | GV |
| 27698 | 36 | 43 | United Kingdom (100%) | Europe (100%) | 2020-07-15 to 2020-09-28 | Inactive | Not_VOC (0) | GH |
| 27736 | 90 | 157 | Netherlands (85%), United Kingdom (6%), Denmark (4%), St Eustatius (3%), Belgium (1%) | Europe (97%) | 2020-06-07 to 2020-12-07 | Quiet | Not_VOC (0) | GH |
| 27774 | 144 | 295 | United Kingdom (100%), Denmark (0%) | Europe (100%) | 2020-08-02 to 2020-12-22 | Quiet | Not_VOC (0) | GR |
| 27950 | 431 | 776 | United Kingdom (70%), Denmark (10%), Netherlands (9%), Sweden (4%), Luxembourg (2%) | Europe (99%) | 2020-08-04 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 28012 | 290 | 616 | United Kingdom (99%), South Korea (0%), Belgium (0%), Ireland (0%), Norway (0%) | Europe (100%) | 2020-04-04 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 28019 | 255 | 554 | United Kingdom (80%), Denmark (12%), Ireland (1%), Norway (1%), Germany (1%) | Europe (100%) | 2020-08-02 to 2020-12-20 | Quiet | Not_VOC (0) | GH |
| 28127 | 85 | 132 | United Kingdom (38%), France (22%), Denmark (12%), Luxembourg (10%), Tunisia (5%) | Europe (95%) | 2020-03-16 to 2020-12-17 | Quiet | Not_VOC (0) | GV |
| **28179** | 64 | 197 | United Kingdom (100%) | Europe (100%) | 2020-06-11 to 2020-12-23 | **Active** | Not_VOC (0) | GR |
| 28274 | 38 | 61 | United Kingdom (97%), Norway (3%) | Europe (100%) | 2020-08-06 to 2020-12-10 | Quiet | Not_VOC (0) | GR |
| 28445 | 241 | 549 | United Kingdom (64%), Hungary (13%), Denmark (11%), Norway (8%), Netherlands (2%) | Europe (99%) | 2020-08-03 to 2020-12-21 | Quiet | Not_VOC (0) | GH |
| 28513 | 227 | 413 | United Kingdom (82%), Denmark (17%), Australia (0%), United Arab Emirates (0%), Italy (0%) | Europe (100%) | 2020-03-24 to 2020-12-20 | Quiet | Not_VOC (0) | GR |
| 28606 | 41 | 70 | United Kingdom (49%), Denmark (19%), Hungary (11%), Italy (9%), Czech Republic (6%) | Europe (100%) | 2020-04-11 to 2020-12-13 | Quiet | Not_VOC (0) | GR |
| 28714 | 82 | 186 | United Kingdom (100%) | Europe (100%) | 2020-08-11 to 2020-12-10 | Quiet | Not_VOC (0) | GR |
| 28743 | 27 | 117 | United Kingdom (93%), Netherlands (3%), Denmark (2%), Luxembourg (2%), Portugal (1%) | Europe (100%) | 2020-08-11 to 2020-11-20 | Inactive | Not_VOC (0) | GR |
| 28786 | 129 | 228 | United Kingdom (84%), Denmark (7%), Czech Republic (2%), Netherlands (2%), France (1%) | Europe (100%) | 2020-04-06 to 2020-12-16 | Quiet | Not_VOC (0) | G |
| 28825 | 72 | 138 | United Kingdom (100%) | Europe (100%) | 2020-08-12 to 2020-12-18 | Quiet | Not_VOC (0) | GV |
| 28885 | 143 | 376 | United Kingdom (99%), Hong Kong (1%), Denmark (0%), Luxembourg (0%) | Europe (99%) | 2020-08-12 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 28987 | 101 | 216 | United Kingdom (77%), Denmark (11%), Netherlands (2%), Germany (2%), France (1%) | Europe (99%) | 2020-06-01 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| 29144 | 69 | 133 | United Kingdom (100%) | Europe (100%) | 2020-07-06 to 2020-11-08 | Inactive | Not_VOC (0) | G |
| **29259** | 403 | 736 | United Kingdom (54%), Denmark (12%), Netherlands (12%), Luxembourg (7%), Italy (4%) | Europe (100%) | 2020-08-05 to 2020-12-28 | **Active** | Not_VOC (0) | GV |
| **29310** | 181 | 400 | United Kingdom (95%), Ireland (5%), Sweden (0%) | Europe (100%) | 2020-08-17 to 2020-12-25 | **Active** | Not_VOC (0) | GV |
| 29320 | 86 | 258 | United Kingdom (94%), Spain (3%), Denmark (2%), France (0%) | Europe (100%) | 2020-08-17 to 2020-12-17 | Quiet | Not_VOC (0) | GV |
| 29367 | 60 | 179 | United Kingdom (96%), Ireland (3%), Netherlands (1%), Spain (1%) | Europe (100%) | 2020-08-18 to 2020-12-14 | Quiet | Not_VOC (0) | GV |
| **29368** | 63 | 81 | Portugal (68%), United Kingdom (20%), Netherlands (4%), Luxembourg (4%), Ireland (2%) | Europe (100%) | 2020-08-18 to 2020-12-28 | **Active** | Not_VOC (0) | GV |
| **29374** | 246 | 397 | USA (96%), Australia (3%), Denmark (1%), United Kingdom (1%) | North America (96%) | 2020-08-10 to 2020-12-28 | **Active** | Not_VOC (0) | GH |
| 29376 | 102 | 406 | United Kingdom (99%), Finland (0%), Sweden (0%), Norway (0%) | Europe (100%) | 2020-08-18 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| **29432** | 210 | 407 | Netherlands (40%), United Kingdom (35%), Denmark (9%), Germany (6%), Belgium (4%) | Europe (100%) | 2020-08-18 to 2020-12-27 | **Active** | Not_VOC (0) | GV |
| 29496 | 64 | 109 | Denmark (41%), Lithuania (34%), Norway (17%), United Kingdom (3%), Latvia (3%) | Europe (100%) | 2020-08-19 to 2020-12-22 | Quiet | Not_VOC (0) | GV |
| 29516 | 94 | 222 | United Kingdom (96%), Netherlands (3%), Norway (0%), Belgium (0%) | Europe (100%) | 2020-08-19 to 2020-12-15 | Quiet | Not_VOC (0) | GR |
| 29670 | 46 | 107 | United Kingdom (100%) | Europe (100%) | 2020-08-20 to 2020-12-14 | Quiet | Not_VOC (0) | GR |
| **29691** | 34 | 46 | USA (100%) | North America (100%) | 2020-08-21 to 2020-12-27 | **Active** | Not_VOC (0) | GH |
| 29839 | 139 | 316 | Denmark (48%), Norway (22%), United Kingdom (21%), Czech Republic (2%), Germany (2%) | Europe (98%) | 2020-06-20 to 2020-11-30 | Inactive | Not_VOC (0) | GR |
| 29873 | 40 | 59 | Italy (59%), France (19%), United Kingdom (14%), Luxembourg (5%), Ireland (2%) | Europe (100%) | 2020-08-24 to 2020-12-13 | Quiet | Not_VOC (0) | GH |
| 29952 | 100 | 206 | United Kingdom (100%) | Europe (100%) | 2020-06-08 to 2020-11-25 | Inactive | Not_VOC (0) | G |
| 29967 | 34 | 64 | United Kingdom (100%) | Europe (100%) | 2020-08-25 to 2020-12-11 | Quiet | Not_VOC (0) | GV |
| 29978 | 95 | 179 | United Kingdom (91%), Denmark (4%), Netherlands (2%), France (1%), Croatia (1%) | Europe (99%) | 2020-08-25 to 2020-12-20 | Quiet | Not_VOC (0) | G |
| 29993 | 71 | 126 | United Kingdom (38%), France (18%), USA (11%), Switzerland (11%), Czech Republic (6%) | Europe (87%) | 2020-04-17 to 2020-12-21 | Quiet | Not_VOC (0) | G |
| **30018** | 565 | 1365 | Denmark (69%), United Kingdom (16%), Czech Republic (5%), Netherlands (3%), Sweden (2%) | Europe (100%) | 2020-05-19 to 2020-12-26 | **Active** | Not_VOC (0) | G |
| **30071** | 72 | 120 | Luxembourg (35%), France (17%), Denmark (13%), Belgium (11%), United Kingdom (8%) | Europe (99%) | 2020-08-25 to 2020-12-27 | **Active** | Not_VOC (0) | GH |
| 30095 | 601 | 1141 | United Kingdom (99%), Denmark (1%), Ireland (0%), Norway (0%) | Europe (100%) | 2020-05-13 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| 30163 | 243 | 497 | United Kingdom (98%), Denmark (1%), Australia (0%), France (0%), Germany (0%) | Europe (100%) | 2020-08-26 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 30173 | 40 | 158 | United Kingdom (99%), Denmark (1%) | Europe (100%) | 2020-08-26 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 30174 | 141 | 261 | United Kingdom (89%), Russia (10%), Bangladesh (1%), Denmark (0%), Hungary (0%) | Europe (99%) | 2020-04-01 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| **30180** | 424 | 703 | Netherlands (53%), Denmark (29%), Luxembourg (7%), United Kingdom (5%), Belgium (2%) | Europe (99%) | 2020-06-11 to 2020-12-23 | **Active** | Not_VOC (0) | G |
| 30199 | 129 | 260 | United Kingdom (82%), Hungary (10%), Denmark (4%), Netherlands (2%), Germany (1%) | Europe (100%) | 2020-08-01 to 2020-12-15 | Quiet | Not_VOC (0) | GH |
| 30210 | 53 | 100 | United Kingdom (92%), Netherlands (6%), Luxembourg (2%) | Europe (100%) | 2020-08-26 to 2020-12-19 | Quiet | Not_VOC (0) | GV |
| 30333 | 29 | 54 | United Kingdom (100%) | Europe (100%) | 2020-08-27 to 2020-12-11 | Quiet | Not_VOC (0) | GV |
| 30362 | 166 | 411 | United Kingdom (100%) | Europe (100%) | 2020-08-27 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 30431 | 90 | 187 | United Kingdom (100%) | Europe (100%) | 2020-08-28 to 2020-12-02 | Inactive | Not_VOC (0) | GR |
| 30498 | 109 | 263 | United Kingdom (100%), South Korea (0%) | Europe (100%) | 2020-08-28 to 2020-12-20 | Quiet | Not_VOC (0) | GR |
| 30499 | 93 | 177 | United Kingdom (100%) | Europe (100%) | 2020-07-17 to 2020-11-18 | Inactive | Not_VOC (0) | GR |
| 30500 | 52 | 87 | United Kingdom (93%), France (3%), Denmark (1%), Luxembourg (1%), USA (1%) | Europe (99%) | 2020-08-03 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 30933 | 55 | 114 | United Kingdom (99%), Italy (1%) | Europe (100%) | 2020-08-29 to 2020-12-20 | Quiet | Not_VOC (0) | G |
| 30945 | 193 | 368 | United Kingdom (99%), Germany (1%) | Europe (100%) | 2020-09-01 to 2020-12-19 | Quiet | Not_VOC (0) | GV |
| 30950 | 46 | 111 | United Kingdom (100%) | Europe (100%) | 2020-09-01 to 2020-12-13 | Quiet | Not_VOC (0) | GV |
| 31067 | 132 | 240 | United Kingdom (100%), Sweden (0%) | Europe (100%) | 2020-08-14 to 2020-12-22 | Quiet | Not_VOC (0) | GV |
| 31169 | 31 | 69 | United Kingdom (100%) | Europe (100%) | 2020-09-03 to 2020-12-06 | Quiet | Not_VOC (0) | GR |
| **31179** | 3073 | 6050 | United Kingdom (95%), Denmark (3%), Netherlands (1%), Portugal (0%), Spain (0%) | Europe (100%) | 2020-08-09 to 2020-12-23 | **Active** | Not_VOC (0) | GV |
| 31217 | 42 | 88 | United Kingdom (100%) | Europe (100%) | 2020-09-03 to 2020-12-20 | Quiet | Not_VOC (0) | GR |
| 31272 | 68 | 163 | United Kingdom (100%) | Europe (100%) | 2020-09-03 to 2020-12-17 | Quiet | Not_VOC (0) | GV |
| 31352 | 37 | 71 | United Kingdom (99%), Denmark (1%) | Europe (100%) | 2020-09-03 to 2020-11-30 | Inactive | Not_VOC (0) | GR |
| 31384 | 46 | 81 | United Kingdom (100%) | Europe (100%) | 2020-08-27 to 2020-12-11 | Quiet | Not_VOC (0) | GV |
| 31421 | 637 | 1294 | United Kingdom (99%), Latvia (1%), Ireland (0%), Luxembourg (0%) | Europe (100%) | 2020-06-02 to 2020-12-22 | Quiet | Not_VOC (0) | GR |
| 31434 | 263 | 510 | United Kingdom (85%), Ireland (15%), USA (0%), Portugal (0%) | Europe (100%) | 2020-09-06 to 2020-12-22 | Quiet | Not_VOC (0) | GV |
| 31473 | 108 | 223 | United Kingdom (100%), Taiwan (0%) | Europe (100%) | 2020-09-07 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| 31480 | 60 | 158 | United Kingdom (100%) | Europe (100%) | 2020-09-07 to 2020-11-20 | Inactive | Not_VOC (0) | GV |
| 31631 | 80 | 118 | United Kingdom (100%) | Europe (100%) | 2020-08-31 to 2020-12-05 | Inactive | Not_VOC (0) | GV |
| **31641** | 275 | 477 | United Kingdom (69%), Denmark (20%), Germany (4%), Norway (3%), Luxembourg (1%) | Europe (99%) | 2020-09-08 to 2020-12-23 | **Active** | Not_VOC (0) | G |
| 31725 | 50 | 87 | United Kingdom (100%) | Europe (100%) | 2020-09-09 to 2020-12-19 | Quiet | Not_VOC (0) | G |
| **31744** | 868 | 2114 | United Kingdom (99%), Denmark (1%), Ireland (0%), USA (0%) | Europe (100%) | 2020-09-08 to 2020-12-24 | **Active** | Not_VOC (0) | GV |
| 31775 | 86 | 248 | United Kingdom (94%), Russia (2%), Sweden (1%), Senegal (1%), Denmark (1%) | Europe (98%) | 2020-03-19 to 2020-12-14 | Quiet | Not_VOC (0) | GR |
| 31803 | 249 | 791 | United Kingdom (100%), Italy (0%) | Europe (100%) | 2020-09-09 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 31873 | 52 | 86 | USA (100%) | North America (100%) | 2020-06-22 to 2020-12-22 | Quiet | Not_VOC (0) | GH |
| 31890 | 69 | 122 | United Kingdom (100%) | Europe (100%) | 2020-09-09 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 31942 | 778 | 1611 | United Kingdom (100%), South Korea (0%), Denmark (0%), New Zealand (0%), Portugal (0%) | Europe (100%) | 2020-09-02 to 2020-12-22 | Quiet | Not_VOC (0) | GV |
| 31973 | 29 | 54 | United Kingdom (98%), Denmark (2%) | Europe (100%) | 2020-09-02 to 2020-11-18 | Inactive | Not_VOC (0) | G |
| 32010 | 67 | 150 | United Kingdom (99%), Ireland (1%), Australia (1%) | Europe (99%) | 2020-06-13 to 2020-12-10 | Quiet | Not_VOC (0) | GR |
| 32100 | 111 | 222 | United Kingdom (100%) | Europe (100%) | 2020-09-10 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| **32234** | 109 | 145 | USA (51%), United Kingdom (48%), Canada (1%) | North America (52%) | 2020-07-13 to 2020-12-27 | **Active** | Not_VOC (0) | GR |
| **32357** | 37 | 80 | United Kingdom (54%), Luxembourg (29%), Portugal (10%), Belgium (5%), Denmark (2%) | Europe (100%) | 2020-08-24 to 2020-12-29 | **Active** | Not_VOC (0) | G |
| 32400 | 210 | 427 | United Kingdom (100%) | Europe (100%) | 2020-09-14 to 2020-12-19 | Quiet | Not_VOC (0) | GV |
| 32406 | 94 | 273 | United Kingdom (100%), Denmark (0%) | Europe (100%) | 2020-09-14 to 2020-12-10 | Quiet | Not_VOC (0) | GV |
| 32467 | 104 | 247 | United Kingdom (100%) | Europe (100%) | 2020-08-29 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 32544 | 68 | 244 | United Kingdom (100%) | Europe (100%) | 2020-09-16 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 32618 | 46 | 128 | United Kingdom (100%) | Europe (100%) | 2020-09-16 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 32923 | 66 | 116 | United Kingdom (97%), Ireland (2%), Denmark (1%) | Europe (100%) | 2020-09-03 to 2020-12-05 | Inactive | Not_VOC (0) | GV |
| 32941 | 68 | 134 | United Kingdom (100%) | Europe (100%) | 2020-09-18 to 2020-12-17 | Quiet | Not_VOC (0) | GV |
| 32971 | 35 | 71 | United Kingdom (85%), Latvia (14%), Denmark (1%) | Europe (100%) | 2020-09-09 to 2020-12-18 | Quiet | Not_VOC (0) | GR |
| 33002 | 64 | 142 | United Kingdom (100%) | Europe (100%) | 2020-09-08 to 2020-12-17 | Quiet | Not_VOC (0) | GV |
| 33003 | 47 | 68 | United Kingdom (60%), Italy (35%), Sweden (1%), Australia (1%), Luxembourg (1%) | Europe (99%) | 2020-09-19 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 33194 | 49 | 77 | United Kingdom (100%) | Europe (100%) | 2020-09-21 to 2020-12-17 | Quiet | Not_VOC (0) | GH |
| 33330 | 38 | 82 | United Kingdom (100%) | Europe (100%) | 2020-09-21 to 2020-12-22 | Quiet | Not_VOC (0) | GV |
| **33331** | 50 | 105 | United Kingdom (99%), Netherlands (1%) | Europe (100%) | 2020-09-21 to 2020-12-25 | **Active** | Not_VOC (0) | GV |
| 33350 | 102 | 224 | United Kingdom (76%), Ireland (24%), Denmark (0%) | Europe (100%) | 2020-08-28 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 33363 | 63 | 118 | United Kingdom (100%) | Europe (100%) | 2020-09-22 to 2020-12-14 | Quiet | Not_VOC (0) | GV |
| 33381 | 101 | 294 | United Kingdom (94%), Portugal (3%), Luxembourg (1%), Belgium (1%), Ireland (1%) | Europe (100%) | 2020-08-30 to 2020-12-17 | Quiet | Not_VOC (0) | G |
| 33460 | 48 | 94 | United Kingdom (100%) | Europe (100%) | 2020-09-23 to 2020-12-22 | Quiet | Not_VOC (0) | GV |
| 33569 | 182 | 340 | United Kingdom (100%) | Europe (100%) | 2020-09-24 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 33592 | 38 | 84 | United Kingdom (100%) | Europe (100%) | 2020-09-21 to 2020-12-16 | Quiet | Not_VOC (0) | GV |
| 33603 | 101 | 233 | United Kingdom (100%) | Europe (100%) | 2020-09-24 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| **33612** | 88 | 180 | United Kingdom (100%) | Europe (100%) | 2020-09-24 to 2020-12-23 | **Active** | Not_VOC (0) | GV |
| 33689 | 63 | 116 | United Kingdom (98%), Denmark (2%) | Europe (100%) | 2020-09-24 to 2020-12-22 | Quiet | Not_VOC (0) | GV |
| 33695 | 92 | 194 | United Kingdom (99%), India (1%) | Europe (99%) | 2020-05-19 to 2020-12-17 | Quiet | Not_VOC (0) | GR |
| 33703 | 67 | 138 | United Kingdom (100%) | Europe (100%) | 2020-09-24 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 33763 | 171 | 297 | United Kingdom (100%), Portugal (0%) | Europe (100%) | 2020-09-21 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 33773 | 45 | 120 | Denmark (95%), United Kingdom (5%) | Europe (100%) | 2020-09-21 to 2020-12-14 | Quiet | Not_VOC (0) | GR |
| 33932 | 39 | 68 | United Kingdom (100%) | Europe (100%) | 2020-09-18 to 2020-12-17 | Quiet | Not_VOC (0) | GV |
| 33964 | 27 | 58 | United Kingdom (100%) | Europe (100%) | 2020-09-24 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 33979 | 73 | 169 | United Kingdom (99%), Belgium (1%) | Europe (100%) | 2020-09-18 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 34142 | 90 | 266 | United Kingdom (100%), Denmark (0%) | Europe (100%) | 2020-09-26 to 2020-12-18 | Quiet | Not_VOC (0) | GR |
| 34268 | 61 | 151 | United Kingdom (99%), Luxembourg (1%) | Europe (100%) | 2020-08-13 to 2020-12-22 | Quiet | Not_VOC (0) | GR |
| 34310 | 30 | 51 | United Kingdom (100%) | Europe (100%) | 2020-09-29 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 34410 | 51 | 131 | United Kingdom (100%) | Europe (100%) | 2020-09-24 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| **34423** | 78 | 149 | United Kingdom (100%) | Europe (100%) | 2020-09-29 to 2020-12-24 | **Active** | Not_VOC (0) | GV |
| 34437 | 90 | 156 | United Kingdom (100%) | Europe (100%) | 2020-09-29 to 2020-12-22 | Quiet | Not_VOC (0) | GV |
| 34485 | 60 | 113 | United Kingdom (99%), New Zealand (1%) | Europe (99%) | 2020-09-21 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 34499 | 36 | 83 | United Kingdom (100%) | Europe (100%) | 2020-10-01 to 2020-12-16 | Quiet | Not_VOC (0) | GV |
| 34505 | 43 | 75 | United Kingdom (100%) | Europe (100%) | 2020-08-01 to 2020-12-13 | Quiet | Not_VOC (0) | GR |
| 34620 | 44 | 111 | United Kingdom (100%) | Europe (100%) | 2020-09-29 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 34632 | 85 | 266 | United Kingdom (100%) | Europe (100%) | 2020-09-04 to 2020-12-19 | Quiet | Not_VOC (0) | GR |
| 34680 | 77 | 137 | United Kingdom (86%), Saudi Arabia (6%), Denmark (6%), New Zealand (1%), Australia (1%) | Europe (92%) | 2020-04-01 to 2020-12-22 | Quiet | Not_VOC (0) | GH |
| 34871 | 28 | 52 | United Kingdom (100%) | Europe (100%) | 2020-09-18 to 2020-12-17 | Quiet | Not_VOC (0) | GV |
| 34910 | 207 | 502 | United Kingdom (100%), Sweden (0%) | Europe (100%) | 2020-09-01 to 2020-12-18 | Quiet | Not_VOC (0) | GV |
| 34923 | 77 | 100 | Israel (31%), United Kingdom (30%), Palestine (30%), Denmark (6%), Belgium (3%) | Asia (61%) | 2020-06-14 to 2020-12-16 | Quiet | Not_VOC (0) | GR |
| **34933** | 210 | 400 | United Kingdom (100%), Denmark (0%), Sweden (0%) | Europe (100%) | 2020-09-10 to 2020-12-24 | **Active** | Not_VOC (0) | GV |
| 34959 | 60 | 108 | United Kingdom (100%) | Europe (100%) | 2020-10-05 to 2020-12-19 | Quiet | Not_VOC (0) | GV |
| 34961 | 26 | 52 | United Kingdom (100%) | Europe (100%) | 2020-09-25 to 2020-12-10 | Quiet | Not_VOC (0) | GV |
| 34975 | 103 | 205 | United Kingdom (98%), Ireland (2%) | Europe (100%) | 2020-10-03 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 34998 | 107 | 309 | United Kingdom (100%) | Europe (100%) | 2020-09-21 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| **35123** | 1161 | 1796 | USA (55%), United Kingdom (28%), South Africa (4%), Mexico (3%), Denmark (2%) | North America (58%) | 2020-03-10 to 2020-12-27 | **Active** | Not_VOC (0) | G |
| 35307 | 144 | 179 | India (63%), USA (23%), United Kingdom (10%), Mexico (1%), Thailand (1%) | Asia (64%) | 2020-03-15 to 2020-12-05 | Inactive | Not_VOC (0) | GR |
| 36126 | 108 | 321 | USA (99%), Australia (1%), South Africa (0%) | North America (99%) | 2020-03-29 to 2020-12-17 | Quiet | Not_VOC (0) | G |
| 36269 | 123 | 227 | USA (100%), Canada (0%) | North America (100%) | 2020-03-13 to 2020-08-21 | Inactive | Not_VOC (0) | GH |
| **36691** | 42 | 61 | United Kingdom (34%), Russia (16%), Latvia (10%), Denmark (8%), Oman (7%) | Europe (79%) | 2020-04-10 to 2020-12-25 | **Active** | Not_VOC (0) | GR |
| 37868 | 71 | 106 | United Arab Emirates (85%), United Kingdom (7%), Croatia (4%), Norway (2%), USA (1%) | Asia (85%) | 2020-04-16 to 2020-10-31 | Inactive | Not_VOC (0) | GR |
| 40860 | 56 | 182 | Denmark (98%), France (1%), Turkey (1%) | Europe (100%) | 2020-07-20 to 2020-10-19 | Inactive | Not_VOC (0) | GR |
| **40969** | 223 | 432 | USA (100%), United Kingdom (0%) | North America (100%) | 2020-07-23 to 2020-12-29 | **Active** | Not_VOC (0) | G |
| 40982 | 59 | 106 | USA (97%), Mexico (1%), United Kingdom (1%), Taiwan (1%) | North America (98%) | 2020-07-23 to 2020-12-18 | Quiet | Not_VOC (0) | G |
| 41128 | 71 | 217 | Denmark (99%), United Kingdom (1%) | Europe (100%) | 2020-07-27 to 2020-11-16 | Inactive | Not_VOC (0) | GR |
| 41458 | 56 | 76 | United Kingdom (50%), Denmark (17%), Spain (12%), Germany (8%), New Zealand (4%) | Europe (93%) | 2020-08-02 to 2020-12-15 | Quiet | Not_VOC (0) | G |
| 41476 | 39 | 171 | Denmark (100%) | Europe (100%) | 2020-07-27 to 2020-10-19 | Inactive | Not_VOC (0) | GR |
| 41766 | 42 | 108 | Finland (99%), Denmark (1%) | Europe (100%) | 2020-08-08 to 2020-10-25 | Inactive | Not_VOC (0) | GH |
| 41784 | 111 | 276 | Finland (99%), India (0%), Latvia (0%), Norway (0%) | Europe (100%) | 2020-06-17 to 2020-12-03 | Inactive | Not_VOC (0) | GH |
| 42398 | 37 | 147 | Denmark (97%), United Kingdom (1%), USA (1%), Russia (1%) | Europe (99%) | 2020-04-03 to 2020-10-01 | Inactive | Not_VOC (0) | GR |
| 42817 | 77 | 337 | Denmark (98%), United Kingdom (1%), Spain (1%) | Europe (100%) | 2020-08-17 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 42893 | 56 | 259 | Denmark (99%), Netherlands (0%), United Kingdom (0%) | Europe (100%) | 2020-08-24 to 2020-12-14 | Quiet | Not_VOC (0) | GV |
| 42920 | 53 | 216 | Denmark (81%), United Kingdom (10%), France (5%), Portugal (1%), Luxembourg (1%) | Europe (100%) | 2020-08-24 to 2020-12-17 | Quiet | Not_VOC (0) | GH |
| 43189 | 31 | 69 | USA (100%) | North America (100%) | 2020-08-27 to 2020-10-08 | Inactive | Not_VOC (0) | G |
| 43211 | 32 | 116 | Denmark (99%), United Kingdom (1%) | Europe (100%) | 2020-08-31 to 2020-11-16 | Inactive | Not_VOC (0) | GR |
| 43232 | 154 | 283 | Denmark (100%) | Europe (100%) | 2020-08-10 to 2020-12-14 | Quiet | Not_VOC (0) | GR |
| **43400** | 48 | 98 | Malaysia (96%), Singapore (2%), Australia (2%) | Asia (98%) | 2020-09-01 to 2020-12-30 | **Active** | Not_VOC (0) | G |
| **43531** | 90 | 180 | Luxembourg (67%), Belgium (13%), France (11%), United Kingdom (3%), Italy (2%) | Europe (100%) | 2020-09-02 to 2020-12-29 | **Active** | Not_VOC (0) | GH |
| 43662 | 78 | 135 | South Korea (100%) | Asia (100%) | 2020-09-01 to 2020-11-26 | Inactive | Not_VOC (0) | GH |
| **44057** | 109 | 250 | Luxembourg (73%), Belgium (24%), Netherlands (1%), United Kingdom (1%), Portugal (0%) | Europe (100%) | 2020-09-09 to 2020-12-26 | **Active** | Not_VOC (0) | G |
| 44321 | 83 | 256 | Denmark (100%), Netherlands (0%) | Europe (100%) | 2020-09-14 to 2020-12-21 | Quiet | Not_VOC (0) | G |
| 44323 | 29 | 36 | Czech Republic (50%), United Kingdom (39%), Luxembourg (6%), Denmark (6%) | Europe (100%) | 2020-09-14 to 2020-11-15 | Inactive | Not_VOC (0) | G |
| 44573 | 41 | 122 | Denmark (97%), United Kingdom (2%), Norway (1%) | Europe (100%) | 2020-09-14 to 2020-12-19 | Quiet | Not_VOC (0) | G |
| **44837** | 82 | 139 | Luxembourg (51%), Belgium (37%), Netherlands (7%), United Kingdom (2%), Malaysia (1%) | Europe (99%) | 2020-08-01 to 2020-12-29 | **Active** | Not_VOC (0) | GV |
| **45062** | 197 | 518 | United Kingdom (98%), Portugal (1%), France (0%), Finland (0%), Italy (0%) | Europe (100%) | 2020-09-20 to 2020-12-29 | **Active** | B.1.1.7 (100) | GR |
| 45072 | 140 | 300 | United Kingdom (99%), Singapore (0%), Luxembourg (0%), Ireland (0%) | Europe (100%) | 2020-09-20 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 45440 | 63 | 142 | United Kingdom (70%), Denmark (14%), Italy (13%), Luxembourg (3%), Australia (1%) | Europe (99%) | 2020-03-21 to 2020-12-22 | Quiet | Not_VOC (0) | GV |
| 45452 | 69 | 124 | United Kingdom (81%), Ireland (10%), Netherlands (8%), Lithuania (1%) | Europe (100%) | 2020-09-09 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| **45545** | 38 | 74 | Belgium (31%), Luxembourg (30%), Netherlands (22%), United Kingdom (5%), Portugal (5%) | Europe (100%) | 2020-09-18 to 2020-12-27 | **Active** | Not_VOC (0) | GH |
| 46070 | 91 | 145 | United Kingdom (28%), Denmark (23%), Switzerland (21%), Norway (10%), Belgium (4%) | Europe (99%) | 2020-07-06 to 2020-12-14 | Quiet | Not_VOC (0) | GR |
| 46169 | 95 | 228 | United Kingdom (100%) | Europe (100%) | 2020-09-17 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 46434 | 39 | 55 | Denmark (100%) | Europe (100%) | 2020-09-28 to 2020-11-30 | Inactive | Not_VOC (0) | Not Applicaple |
| **46649** | 1647 | 3429 | United Kingdom (96%), Denmark (2%), Portugal (0%), Italy (0%), Finland (0%) | Europe (100%) | 2020-09-30 to 2020-12-29 | **Active** | B.1.1.7 (100) | GR |
| 46669 | 220 | 340 | Jordan (99%), Malaysia (0%), New Zealand (0%) | Asia (100%) | 2020-08-13 to 2020-11-27 | Inactive | Not_VOC (0) | GR |
| 46855 | 40 | 77 | United Kingdom (100%) | Europe (100%) | 2020-09-20 to 2020-12-19 | Quiet | Not_VOC (0) | GV |
| 46880 | 28 | 45 | United Kingdom (100%) | Europe (100%) | 2020-10-01 to 2020-12-09 | Quiet | Not_VOC (0) | GV |
| 47078 | 51 | 93 | United Kingdom (91%), Belgium (4%), Portugal (4%) | Europe (100%) | 2020-08-27 to 2020-12-18 | Quiet | Not_VOC (0) | GR |
| 47364 | 85 | 212 | United Kingdom (99%), Denmark (1%), Italy (0%) | Europe (100%) | 2020-10-03 to 2020-12-20 | Quiet | Not_VOC (0) | GH |
| 47408 | 48 | 63 | Jordan (100%) | Asia (100%) | 2020-08-18 to 2020-11-04 | Inactive | Not_VOC (0) | GR |
| 47512 | 52 | 102 | United Kingdom (97%), Denmark (3%) | Europe (100%) | 2020-09-07 to 2020-12-07 | Quiet | Not_VOC (0) | Not Applicaple |
| 47951 | 25 | 185 | Denmark (100%) | Europe (100%) | 2020-10-05 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 48047 | 53 | 109 | Denmark (80%), United Kingdom (12%), Belgium (5%), Norway (3%), Switzerland (1%) | Europe (100%) | 2020-10-05 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| 48251 | 69 | 129 | Denmark (100%) | Europe (100%) | 2020-10-06 to 2020-12-14 | Quiet | Not_VOC (0) | GR |
| 48625 | 51 | 91 | United Kingdom (23%), Denmark (22%), South Korea (20%), Germany (9%), Poland (4%) | Europe (75%) | 2020-03-17 to 2020-12-07 | Quiet | Not_VOC (0) | GR |
| 48734 | 52 | 100 | United Kingdom (100%) | Europe (100%) | 2020-10-05 to 2020-12-19 | Quiet | Not_VOC (0) | GV |
| 49321 | 57 | 121 | United Kingdom (100%) | Europe (100%) | 2020-10-05 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 49395 | 38 | 78 | United Kingdom (100%) | Europe (100%) | 2020-10-09 to 2020-12-20 | Quiet | Not_VOC (0) | GR |
| 49629 | 82 | 239 | Denmark (79%), United Kingdom (15%), Sweden (6%), Luxembourg (0%) | Europe (100%) | 2020-07-27 to 2020-12-22 | Quiet | Not_VOC (0) | GH |
| **49676** | 123 | 351 | United Kingdom (99%), Netherlands (1%), Pakistan (0%) | Europe (100%) | 2020-10-11 to 2020-12-25 | **Active** | B.1.1.7 (100) | GR |
| 49777 | 27 | 53 | Netherlands (26%), Switzerland (23%), Italy (19%), United Kingdom (15%), Germany (9%) | Europe (98%) | 2020-10-12 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 49798 | 60 | 207 | Denmark (100%) | Europe (100%) | 2020-10-05 to 2020-12-21 | Quiet | Not_VOC (0) | GH |
| 49908 | 150 | 437 | Denmark (100%) | Europe (100%) | 2020-10-12 to 2020-12-21 | Quiet | Not_VOC (0) | G |
| 49936 | 51 | 141 | Denmark (100%) | Europe (100%) | 2020-10-12 to 2020-12-21 | Quiet | Not_VOC (0) | G |
| 49982 | 51 | 114 | United Kingdom (100%) | Europe (100%) | 2020-10-12 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 50111 | 28 | 44 | Denmark (100%) | Europe (100%) | 2020-08-31 to 2020-12-07 | Quiet | Not_VOC (0) | GR |
| 51132 | 73 | 154 | United Kingdom (100%) | Europe (100%) | 2020-09-30 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 51410 | 55 | 90 | United Kingdom (100%) | Europe (100%) | 2020-10-15 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 51660 | 38 | 55 | United Kingdom (100%) | Europe (100%) | 2020-10-09 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 52046 | 34 | 66 | South Korea (100%) | Asia (100%) | 2020-10-16 to 2020-11-23 | Inactive | Not_VOC (0) | GH |
| 52395 | 44 | 95 | United Kingdom (100%) | Europe (100%) | 2020-10-17 to 2020-12-19 | Quiet | Not_VOC (0) | GV |
| 52752 | 32 | 62 | United Kingdom (97%), Denmark (3%) | Europe (100%) | 2020-09-21 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 52925 | 66 | 196 | Denmark (99%), United Kingdom (1%), Netherlands (1%) | Europe (100%) | 2020-04-09 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| **53107** | 23 | 83 | Luxembourg (100%) | Europe (100%) | 2020-10-19 to 2020-12-27 | **Active** | Not_VOC (0) | G |
| **54452** | 57 | 102 | United Kingdom (99%), Sweden (1%) | Europe (100%) | 2020-10-21 to 2020-12-28 | **Active** | B.1.1.7 (100) | GR |
| 54556 | 33 | 51 | United Kingdom (100%) | Europe (100%) | 2020-10-01 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 54897 | 54 | 99 | United Kingdom (79%), Spain (7%), Italy (5%), France (4%), Switzerland (2%) | Europe (100%) | 2020-08-05 to 2020-12-20 | Quiet | Not_VOC (0) | GV |
| 54949 | 36 | 92 | United Kingdom (92%), Netherlands (8%) | Europe (100%) | 2020-10-22 to 2020-12-22 | Quiet | B.1.1.7 (100) | GR |
| **55253** | 53 | 103 | Luxembourg (97%), South Korea (3%) | Europe (97%) | 2020-09-30 to 2020-12-29 | **Active** | Not_VOC (0) | GV |
| 55421 | 43 | 88 | United Kingdom (100%) | Europe (100%) | 2020-10-19 to 2020-12-15 | Quiet | Not_VOC (0) | GV |
| 55540 | 26 | 39 | Denmark (51%), United Kingdom (41%), Norway (5%), Sweden (3%) | Europe (100%) | 2020-09-30 to 2020-12-14 | Quiet | Not_VOC (0) | GR |
| 56094 | 36 | 62 | United Kingdom (98%), Portugal (2%) | Europe (100%) | 2020-09-10 to 2020-11-27 | Inactive | Not_VOC (0) | GV |
| 56104 | 67 | 187 | Denmark (99%), Netherlands (1%) | Europe (100%) | 2020-09-14 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 56115 | 33 | 71 | Denmark (85%), United Kingdom (13%), Poland (1%), Russia (1%) | Europe (100%) | 2020-08-31 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| 56216 | 98 | 303 | Denmark (100%), United Kingdom (0%) | Europe (100%) | 2020-10-26 to 2020-12-21 | Quiet | Not_VOC (0) | G |
| 56816 | 43 | 122 | Denmark (98%), Australia (1%), United Kingdom (1%) | Europe (99%) | 2020-10-26 to 2020-12-21 | Quiet | Not_VOC (0) | GH |
| 57107 | 32 | 96 | United Kingdom (100%) | Europe (100%) | 2020-10-27 to 2020-12-19 | Quiet | Not_VOC (0) | GV |
| 57402 | 22 | 31 | USA (97%), Mexico (3%) | North America (100%) | 2020-06-24 to 2020-11-24 | Inactive | Not_VOC (0) | G |
| 57578 | 25 | 50 | United Kingdom (88%), Luxembourg (6%), Denmark (4%), Portugal (2%) | Europe (100%) | 2020-09-19 to 2020-12-19 | Quiet | Not_VOC (0) | GV |
| **57630** | 222 | 484 | United Kingdom (97%), France (1%), Australia (0%), Israel (0%), Portugal (0%) | Europe (99%) | 2020-10-29 to 2020-12-28 | **Active** | B.1.1.7 (100) | GR |
| 58222 | 50 | 63 | USA (98%), Australia (2%) | North America (98%) | 2020-08-17 to 2020-12-21 | Quiet | Not_VOC (0) | GH |
| **58534** | 231 | 438 | United Kingdom (97%), France (1%), Portugal (1%), Denmark (0%), Israel (0%) | Europe (99%) | 2020-10-29 to 2020-12-28 | **Active** | B.1.1.7 (100) | GR |
| 58550 | 78 | 138 | United Kingdom (53%), Denmark (33%), Australia (9%), Sweden (1%), New Zealand (1%) | Europe (89%) | 2020-06-17 to 2020-12-21 | Quiet | Not_VOC (0) | GH |
| 59475 | 27 | 32 | USA (94%), United Kingdom (6%) | North America (94%) | 2020-10-16 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| 62415 | 30 | 71 | United Kingdom (96%), USA (4%) | Europe (96%) | 2020-11-06 to 2020-12-21 | Quiet | B.1.1.7 (100) | GR |
| 62730 | 78 | 162 | United Kingdom (100%) | Europe (100%) | 2020-10-06 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 63880 | 21 | 77 | Denmark (100%) | Europe (100%) | 2020-11-09 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 63884 | 111 | 354 | Denmark (85%), United Kingdom (15%) | Europe (100%) | 2020-11-02 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 64153 | 28 | 78 | Denmark (100%) | Europe (100%) | 2020-09-14 to 2020-12-21 | Quiet | Not_VOC (0) | GH |
| 64300 | 49 | 227 | Denmark (86%), United Kingdom (14%) | Europe (100%) | 2020-10-08 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 64726 | 42 | 52 | Portugal (85%), Luxembourg (8%), Netherlands (6%), France (2%) | Europe (100%) | 2020-10-20 to 2020-12-11 | Quiet | Not_VOC (0) | GV |
| 65578 | 33 | 42 | Portugal (62%), Luxembourg (31%), United Kingdom (5%), Denmark (2%) | Europe (100%) | 2020-09-21 to 2020-12-02 | Inactive | Not_VOC (0) | GV |
| **66559** | 42 | 94 | United Kingdom (98%), France (1%), Italy (1%) | Europe (100%) | 2020-11-08 to 2020-12-27 | **Active** | B.1.1.7 (100) | GR |
| 67441 | 48 | 85 | United Kingdom (99%), Netherlands (1%) | Europe (100%) | 2020-11-08 to 2020-12-22 | Quiet | B.1.1.7 (100) | GR |
| 67728 | 22 | 160 | Denmark (98%), Netherlands (2%), United Kingdom (1%) | Europe (100%) | 2020-10-21 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 67741 | 101 | 250 | Denmark (96%), Finland (2%), Israel (2%) | Europe (98%) | 2020-11-09 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 67774 | 41 | 131 | Denmark (100%) | Europe (100%) | 2020-10-19 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 67797 | 24 | 88 | Denmark (95%), United Kingdom (2%), Portugal (1%), Netherlands (1%) | Europe (100%) | 2020-10-19 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 67846 | 62 | 161 | Denmark (99%), North Macedonia (1%), United Kingdom (1%) | Europe (100%) | 2020-07-29 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| 70137 | 81 | 169 | Denmark (82%), United Kingdom (15%), Italy (1%), Netherlands (1%), South Korea (1%) | Europe (99%) | 2020-03-11 to 2020-12-21 | Quiet | Not_VOC (0) | G |
| 70227 | 38 | 106 | Denmark (100%) | Europe (100%) | 2020-11-16 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 70268 | 108 | 366 | Denmark (92%), Germany (3%), United Kingdom (3%), Sweden (1%), Switzerland (0%) | Europe (100%) | 2020-09-21 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 70352 | 24 | 72 | Denmark (100%) | Europe (100%) | 2020-11-23 to 2020-12-21 | Quiet | Not_VOC (0) | G |
| 70458 | 282 | 783 | Denmark (100%) | Europe (100%) | 2020-11-09 to 2020-12-21 | Quiet | Not_VOC (0) | GV |
| 70516 | 45 | 131 | Denmark (95%), United Kingdom (3%), Croatia (2%) | Europe (100%) | 2020-08-10 to 2020-12-21 | Quiet | Not_VOC (0) | GR |
| 70949 | 69 | 92 | Brazil (86%), USA (5%), United Kingdom (5%), Canada (3%) | South America (86%) | 2020-10-26 to 2020-12-20 | Quiet | Not_VOC (0) | GR |
| **71014** | 35 | 35 | South Africa (89%), France (3%), United Kingdom (3%), Sweden (3%), South Korea (3%) | Africa (89%) | 2020-10-22 to 2020-12-26 | **Active** | B.1.351 (100) | GH |
| 71629 | 39 | 61 | USA (100%) | North America (100%) | 2020-07-28 to 2020-12-15 | Quiet | Not_VOC (0) | GH |
| **72860** | 71 | 87 | USA (97%), Australia (2%), New Zealand (1%) | North America (97%) | 2020-09-28 to 2020-12-27 | **Active** | Not_VOC (0) | GH |
| 74258 | 23 | 29 | France (34%), United Kingdom (28%), Denmark (21%), Luxembourg (7%), Switzerland (7%) | Europe (100%) | 2020-09-26 to 2020-12-09 | Quiet | Not_VOC (0) | GH |
| 74866 | 21 | 97 | Belgium (98%), United Kingdom (2%) | Europe (100%) | 2020-10-22 to 2020-12-14 | Quiet | Not_VOC (0) | GR |
| **81085** | 15 | 22 | Brazil (77%), Japan (18%), USA (5%) | South America (77%) | 2020-12-04 to 2021-01-18 | **Active** | P.1 (100) | GR |
