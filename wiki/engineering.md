---
title: Engineering
permalink: /engineering/
feature_text: |
  ## Engineering
  This page contains information about the engineering of our project.
feature_image: "https://static.igem.wiki/teams/5175/resources/background/bg-engineering.jpg"
excerpt: "This page contains information about the engineering of HUST-China 2024."
---

## Introduction

We want to alleviate the microplastic pollution problem by degrading PET in irrigation water and produce rhamnolipid which is beneficial to the soil fertility and improve the soil environment. To this end, we designed three system paths and chose two kinds of chassis bacteria, *E. coli* BL21 and *P. putida* KT2440. We hope to realize our goal by co-cultivating genetically modified *E. coli* BL21 and *P. putida* KT2440.  In the construction stage, we used homologous recombination and double enzyme digestion to construct the pathway. Although we encountered some problems, we finally achieved certain results through continuous attempts and summaries, which also provided some experience for the subsequent teams.

## Cycle 1

**Construct by the homologous recombination and double enzyme digestion.**

### Design

To construct a well-functioning systemic pathway, we hope that the three plasmids can enable *E. coli* BL21 to degrade PET and enhance its own metabolic capacity, while providing *P. putida* KT2440 the ability to degrade the PET-breakdown-product "terephthalate" and secret rhamnolipid. Based on existing parts with independent functions, we achieved our goal by connecting multiple components to complete plasmids to form a fully functional system pathway.

#### *E. coli*

In order to realize the ideal function of *E. coli* BL21 which is to degrade PET and enhance its own metabolic capacity, we wanted to use homologous recombination to build our fully functional plasmids. We first obtained fragments and vectors with homologous arms by PCR, and then used homologous recombination to connect the corresponding homologous vector and fragments together.

In the first step, we inserted homologous arms at both ends of the target gene fragment as well as the linearized vector fragment. In the PETase-MHETase-fucO-aldA pathway, we begin by incorporating the first homologous arm downstream of the sPETase-MHETase vector fragment and upstream of fucO-aldA. Following that, a second homologous arm is introduced downstream of fucO-aldA and upstream of the PETase-MHETase vector fragment.

The second step. We used the homologous recombinase to directly link the linearized vector PETase-MHETase with the fucO-aldA fragment to construct a complete plasmid.

#### *P. putida*

To achieve the ideal function of *P. putida* KT2440 in degrading the PET breakdown product "terephthalate" and produce rhamnolipids, we decided to use double enzyme digestion to construct our plasmids. We first perform double enzyme digestion to obtain multiple fragments and vectors with the same sticky ends, and then ligate the vectors and fragments containing the same sticky ends together through ligation.

In the first step, we use the double enzyme digestion method to obtain the target gene fragments and the vector fragment with sticky ends. We first culture the basal plasmid-containing strain and extract the plasmid, then we obtain the target gene fragment and the vector fragment with the same sticky end by double enzyme digestion.

In the second step, we use enzyme ligation to link the target gene fragment and its corresponding vector fragment with the same sticky end together, and finally construct a complete plasmid.

### Build

#### *E. coli* BL21

Based on the principle of seamless cloning, we tried to use homologous recombinase to attach multiple fragments directly into the vector to form a complete plasmid.

In the pathway PETase-MHETase-fucO-aldA: First, the linearized vector fragment PETase-MHETase and the gene fragment fucO-aldA were obtained, respectively, by reverse PCR and PCR. They were then etracted and purified by gel extraction. Finally, homologous recombinase was used to connect PETase-MHETase with fucO-aldA to construct a complete system pathway. Next, we transferred the constructed plasmid into E. coli DH5αand inoculated it onto an LB plate containing kanamycin. Then, the solid medium was placed in a 37℃ incubator for overnight incubation at a constant temperature. Subsequently, we picked bacterial plaque for PCR verification. After observing the correct bands, we mixed 800 μL of bacterial solution with 800 μL of 1:1 mixture of glycerol and double distilled water, and we stored the seeds at -20°C.

#### *P. putida* KT2440

Our basic process of constructing a complete plasmid is: extract the plasmid, perform PCR to obtain the fragment containing the target gene, obtain the fragment of the target gene with sticky ends through double enzyme digestion, and use the ligation to link the target gene to the vector.

Take the tphA2A3BA1-tpak system pathway as an example.Initially, we separately cultured *E. coli* DH5$\alpha$(tphA2A3BA1-pUC57) , *E. coli* DH5$\alpha$ (tpaK-pUC57)  and *E. coli* DH5$\alpha$ (pBBR1-CS2)  and extracted the plasmids. After that, We use double enzyme digestion on the plasmids tphA2A3BA1-pUC57 and pBBR1-CS2 with restriction endonucleases *Xho* I and *EcoR* I for 30 minutes. Then we used double enzyme digestion on plasmids the tpaK-pUC57 and pBBR1-CS2 with restriction endonucleases *Spe* I and *EcoR* I for 30 minutes. Next we verified and purified them through agarose gel extraction to obtain the target gene fragment and vector fragment with the identical sticky ends. We have constructed the plasmids tphA2A3BA1-pBBR1-CS2 and tpaK-pBBR1-CS2 through ligation. Next, we transferred the constructed plasmid into *E. coli* DH5$\alpha$ and inoculated it onto an LB plate containing kanamycin. Then, the solid medium was placed in a 37°C incubator for overnight incubation at a constant temperature. Subsequently, we picked bacterial plaque for PCR verification. After observing the correct bands, we mixed 800 μL of bacterial solution with 800 μL of 1:1 mixture of glycerol and double distilled water, and we stored the seeds at -20°C.

After that, We use double enzyme digestion on the plasmids tphA2A3BA1-pUC57 and tpaK-pBBR1CS-2 with restriction endonucleases *Xho* I and *EcoR* I for 30 minutes. And we use double enzyme digestion on the plasmids tpaK-pUC57 and the tphA2A3BA1-pBBR1-CS2 with restriction endonucleases *Spe* I and *EcoR* I for 30 minutes. We then verified them through agarose gel extraction. Unfortunately, we did not find the target band.

### Result

We successfully constructed plasmids PETase-MHETase-fucO-aldA, phaZ-pVLT33, tphA2A3BA1-pBBR1-CS2 and tpak- pBBR1-CS2.

{% include figure.html image="https://static.igem.wiki/teams/5175/resources/engineering/engineering-01.png" alt="The results of PCR identification for PETase-MHETase-aldA-fucO and phaZ-pVLT33" caption="Fig 1. The results of PCR identification for PETase-MHETase-aldA-fucO (left) and phaZ-pVLT33 (right)" %}

In Fig.1, the left sub-figure is the result of PCR identification of PETase-MHETase-aldA-fucO plasmid, it shows that there is a bright band at about 2900 bp, and the length of the fragment we obtained by PCR using the primers we designed should be 2862 bp, which proves that we have successfully constructed the plasmid of PETase-MHETase -aldA-fucO system pathway.

The right sub-figure of Fig.1 is the result of PCR identification of phaZ-pVLT33 plasmid. It shows that there is a bright band at about 800 bp, and the length of the fragment we obtained by PCR using the primers we designed should be 867 bp, which proves that we have successfully constructed the plasmid of phaZ-pVLT33 system pathway.








