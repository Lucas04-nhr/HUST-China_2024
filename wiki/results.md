---
title: Results
permalink: /results/
feature_text: |
  ## Results
  This page contains the results of our project.
feature_image: "https://static.igem.wiki/teams/5175/resources/bg-result.jpg"
excerpt: "This page contains the results of our project."
---

## Introduction 

Our project aims to enable *Escherichia coli* BL21 to efficiently degrade polyethylene terephthalate (PET) into terephthalic acid (TPA) and ethylene glycol (EG) while utilizing the EG for energy. Additionally, we seek to confer the ability to utilize TPA and produce rhamnolipid on *Pseudomonas putida* KT2440. To achieve these objectives, we primarily constructed four plasmids: pPeteg-P and pPeteg-M for *E. coli* BL21, and pTerephthalate and pRhamnolipid for *P. putida* KT2440. In addition to these four main plasmids, we also developed five additional plasmids to facilitate more convenient testing of gene functions.

We transferred these plasmids into *E. coli* BL21 and *P. putida* KT2440 to express the desired proteins. Concurrently, we conducted comprehensive investigations to validate the efficiency of PET degradation and the production efficiency of rhamnolipid.

## **Plasmid Amplification and Reconstruction** 

Initially, we transformed the company-synthesized plasmids containing designed sequences into *E. coli* DH5α for amplification, allowing us to obtain a sufficient quantity of plasmid DNA for subsequent experiments. Following this, colony PCR was performed to confirm successful transformation, and the required plasmids were subsequently extracted for further experimentation.

Subsequently, we employed PCR to obtain the target fragments, which were then integrated into the requisite plasmids for our study.

###  Plasmids of *E. coli* BL21

We constructed two plasmids, pPeteg-P and pPeteg-M, for *E. coli* BL21 to assess the activity of different dual enzyme systems in engineered *E. coli*. We verified the size of the plasmids as well as all the fragments involved in constructing the plasmids . In addition to pPeteg-P and pPeteg-M, we also developed FAST-PETase-MHETase (pPM), MHETase-FAST-PETase (pMP), and T7-fucO-aldA (pEG) to independently validate their function.

The pPeteg-P/pPeteg-M plasmids contain the constructs pelB-PETase-G4S-MHETase and pelB-MHETase-G4S-FAST-PETase (using pelB-PETase-G4S-MHETase as an example), along with aldA and fucO. The pelB-PETase-G4S-MHETase enables *E. coli* BL21 to secrete FAST-PETase-G4S-MHETase, degrading PET into TPA and EG, while the aldA-fucO converts EG into GA to enhance the absorption and utilization of EG.

| Plasmids | Expected size(bp) | Fragments                                                    | Expected size(bp) |
| -------- | ----------------- | ------------------------------------------------------------ | ----------------- |
| pPeteg-P | 10712             | T7 promoter-lac operator-pelB-FAST-PETase-G4S-MHETase-T7 terminator | 2682              |
|          |                   | T7 promoter-fucO-aldA-T7 terminator                          | 2862              |
| pPeteg-M | 10736             | T7 promoter-lac operator-pelB -G4S-MHETase-FAST-PETase -T7 terminator | 2682              |
|          |                   | T7 promoter-fucO-aldA-T7 terminator                          | 2862              |
| pPM      | 7892              | T7 promoter-lac operator-pelB-FAST-PETase-G4S-MHETase-T7 terminator | 2682              |
| pMP      | 7915              | T7 promoter-lac operator-pelB -G4S-MHETase-FAST-PETase -T7 terminator | 2682              |
| pEG      | 5360              | T7 promoter-fucO-aldA-T7 terminator                          | 2862              |



Fig 1.The bands of pPeteg-P (upper band) and pPeteg-M (lower band)（~3000 bp）from PCR

The bands of pPeteg-P (upper band) and pPeteg-M (lower band)（~3000 bp）from PCR are identical to the theoretical lengths of 2862 bp estimated by the designed primer locations (homologous recombination fragments), which could demonstrate that these plasmids had successfully been obtained.



Fig 2.The bands of pPM（2500+ bp）from PCR

The bands of pPM（2500+ bp）from PCR are identical to the theoretical lengths of 2682bp estimated by the designed primer locations (promoter to terminator), which could demonstrate that these plasmids had successfully been obtained.

 

Fig 3.The bands of pEG（~3000 bp）from PCR

The bands of pEG（~3000 bp）from PCR are identical to the theoretical lengths of 2862bp estimated by the designed primer locations (promoter to terminator), which could demonstrate that these plasmids had successfully been obtained.

All the results above showed us a success of the construction of pPeteg-P, pPeteg-M, pPM, pMP, pEG.

###  Plasmids of *P. putida* KT2440

We constructed three plasmids for *P. putida* KT2440: pTerephthalate-A, pTerephthalate-B, and pRhamnolipid. We verified the size of each plasmid as well as all the fragments involved in constructing the plasmids . In addition to pTerephthalate and pRhamnolipid, we also constructed plasmids to ensure the function of rhlA-rhlB and phaZ.

The pRhamnolipid plasmid is composed of rhlA-rhlB and phaZ, which collaboratively function to ensure the efficient secretion of rhamnolipid. To reduce the transcriptional burden imposed by the T7 promoter, we designed pTerephthalate-B to assess its impact on TPA utilization and growth.

| Plasmids                                      | Expected size(bp) | Fragments                                                    | Expected size(bp) |
| --------------------------------------------- | ----------------- | ------------------------------------------------------------ | ----------------- |
| pTerephthalate-A                              | 10622             | T7 promoter- tphA2-tphA3 -tphA1-T7 terminator- T7 promoter - tphB-tpaK-T7  terminator | 10622             |
| T7 promoter- tphA2-tphA3 -tphA1-T7 terminator | 2959              |                                                              |                   |
| T7 promoter - tphB-tpaK-T7 terminator         | 2449              |                                                              |                   |
| pTerephthalate-B                              | 10832             | T7 promoter - tphA2-tphA3-tphB -tphA1-T7 terminator- T7 promoter -  tpaK-T7 terminator | 10832             |
|                                               |                   | T7 promoter - tphA2-tphA3-tphB -tphA1-T7 terminator          | 4111              |
|                                               |                   | T7 promoter - tpaK-T7 terminator                             | 1634              |
| pRhlmnolipid                                  | 13277             | T7 promoter-lac operator-rhlA-rhlB-T7 terminator- T7 promoter -phaZ-T7 terminator | 13277             |
|                                               |                   | T7 promoter -lac operator -rhlA-rhlB-T7 terminator           | 2452              |
|                                               |                   | T7 promoter -phaZ-T7 terminator                              | 1075              |
| rhlA-rhlB                                     | 12202             | T7 promoter -lac operator-rhlA-rhlB-T7 terminator            | 2452              |
| phaZ                                          | 10837             | T7 promoter -lac operator-phaZ-T7 terminator                 | 1075              |



Fig 4.The bands of pTerephthalate-A and pTerephthalate-B from PCR

The bands of pTerephthalate-A（~3000bp）from PCR are identical to the theoretical lengths of 2959 bp, 2449 bp estimated by the designed primer locations (promoter to terminator), which could demonstrate that these plasmids had successfully been obtained.

The bands of pTerephthalate-B（~4000 bp、~2000 bp）from PCR are identical to the theoretical lengths of 4111 bp，2000 bp estimated by the designed primer locations (promoter to terminator), which could demonstrate that these plasmids had successfully been obtained.



Fig 5.The bands of T7-tphA2-tphA3 -tphA1-T7（~3000 bp）from PCR

The bands of T7-tphA2-tphA3 -tphA1-T7（~3000 bp）from PCR are identical to the theoretical lengths of 2959 bp estimated by the designed primer locations (promoter to terminator), which could demonstrate that these plasmids had successfully been obtained.



Fig 6.The bands of T7-tphB-tpaK（~2000+ bp）from PCR

The bands of T7-tphB-tpaK（~2000+ bp）from PCR are identical to the theoretical lengths of 2576 bp estimated by the designed primer locations (promoter to terminator), which could demonstrate that these plasmids had successfully been obtained.



Fig 7.The bands of tphA2-tphA3-tphB -tphA1（~3000 bp）from PCR

The bands of tphA2-tphA3-tphB -tphA1（~3000 bp）from PCR are identical to the theoretical lengths of 2971 bp estimated by the designed primer locations (promoter to terminator), which could demonstrate that these plasmids had successfully been obtained.



Fig 8.The bands of tpaK（~1500 bp）from PCR

The bands of tpaK（~1500 bp）from PCR are identical to the theoretical lengths of 2971 bp estimated by the designed primer locations (promoter to terminator), which could demonstrate that these plasmids had successfully been obtained.

All the results above showed us a success of the construction of pTerephthalate-A, pTerephthalate-B.



Fig 9.The schematic diagram of pRhlmnolipid

Unfortunately, due to time constraints, we were unable to successfully construct the complete plasmids. Consequently, we opted to construct T7-rhlA-rhlB-T7 and T7-phaZ-T7 as alternative plasmids for individual validation of their functionalities.



Fig 10.The bands of rhlA-rhlB（2000+ bp）from PCR

The bands of rhlA-rhlB（2000+ bp）from PCR are identical to the theoretical lengths of 2452bp estimated by the designed primer locations (promoter to terminator), which could demonstrate that these plasmids had successfully been obtained.



Fig 11.The bands of phaZ（~2000 bp）from PCR

The bands of phaZ（~2000 bp）from PCR are identical to the theoretical lengths of 2452bp estimated by the designed primer locations (colony PCR flanking primers), which could demonstrate that these plasmids had successfully been obtained.

All the results above showed us a success of the construction of pVLT33-rhlA-rhlB-phaZ.

The results above could demonstrate that these plasmids are correctly constructed, so we can transform pPeteg-P， pPeteg-M into *E. coli* BL21, while pTerephthalate-A, pTerephthalate-B, rhlA-rhlB, phaZ into *P. putida* KT2440 for verification.

## Strain construction

We have successfully constructed all the target plasmids needed in the three loops, and this step really facilitates our subsequent experiments. At the same time, in order to facilitate the measurement of the function of some elements, we separately constructed plasmids (phaZ，rhlA-rhlB，pPM，pMP，pEG) for some essential elements.

