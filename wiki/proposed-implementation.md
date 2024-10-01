---
title: Proposed Implementation
permalink: /proposed-implementation/
feature_text: |
  ## Proposed Implementation
  This page contains the proposed implementation of the project.
feature_image: "https://static.igem.wiki/teams/5175/resources/background/bg-protocol.jpg"
excerpt: "This page contains the proposed implementation of the project."
---

## Background

According to the Food and Agriculture Organization of the United Nations (FAO), the agricultural industry chain consumes 12.5 million tons of plastic products and 37.3 million tons of food packaging annually. Experts predict that due to the increasing demand for greenhouses, plastic films, and silage films, the use of plastics in the agricultural sector will grow by 50% or even higher in the coming years.Approximately 300 million acres of land in Asia need to be covered with 1.45 million tons of plastic film each year, accounting for 75% of the global film usage[^1]. 

The large-scale use of plastics has brought about great harm in the dark - microplastic pollution. Microplastics(MP) refer to plastic fragments and particles with a diameter of less than 5 millimeters, which are a diverse and non-uniform mixture of plastic particles that are difficult to distinguish by the naked eye. A large amount of agricultural plastic residue can lead to the accumulation of high concentrations of microplastics in farmland soil. Research has shown that microplastics can alter soil properties, affecting environmental conditions such as soil aggregate structure and porosity by altering soil bulk density and water holding capacity[^2]. Changes in soil porosity and water holding capacity may affect oxygen content, thereby altering the diversity and distribution of both aerobic and anaerobic microorganisms, and disrupting crop growth. Microplastics can significantly alter soil carbon storage in farmland, affecting nitrogen and phosphorus cycling as well as microbial activity[^3].

The presence of microplastics in soil can also affect plant growth, interfere with plant metabolic processes, such as causing oxidative stress, increasing the bioavailability and toxicity of heavy metals in plants, reducing soil bulk density, and thus reducing yield and crop quality. And plastic in the form of nanoparticles (<100 nm) can be absorbed by roots and transferred to aboveground plant parts, becoming an important source of microplastic in food[^4].

At present, the treatment methods for microplastics are mainly divided into three categories: physical separation, chemical degradation, and biodegradation. Physical separation mainly separates microplastics from other substances through screening, filtration, and other methods. The operation is simple, but the removal efficiency is low, making it difficult to remove nanoscale microplastics. Chemical degradation uses chemical reagents to further decompose microplastics into small molecules under specific conditions, but the cost of using the chemicals is high, and improper use may also cause secondary pollution to the environment. Biodegradation is the use of microorganisms or enzymes to degrade microplastics into gases, water, and harmless substances for living organisms. Biodegradation has a relatively small impact on the environment and is widely used in the treatment of microplastics in soil and water bodies. It has the potential to develop efficient, low-cost, and low side effect methods for removing environmental microplastics.

## Target users

We expect our users to consist of three main groups: government, plastic degradation research teams, and other iGEM teams.

**1.Government**
In China, 200000 to 300000 tons of residual plastic film are left in farmland every year, resulting in high concentrations of microplastics in agricultural soil. Microplastics have led to a significant decrease in agricultural production. Microplastics entering the human body through the food chain may lead to malignant diseases such as tumors, which are harmful to residents' health. The Chinese government attaches great importance to agricultural issues, pays attention to the yield of agricultural products and the lives of farmers, and adheres to the principle of people-oriented, focusing on food safety and residents' health. So solving the problem of soil microplastic pollution can be a new work achievement for the government. Correspondingly, the improvement of agricultural soil pollution areas with severe microplastic pollution is precisely the problem that this project aims to solve.

Firstly, to solve the pollution of polyethylene terephthalate (PET) in soil microplastics, we introduced the PETase-MHETase dual-enzyme system for efficient PET degradation in *E. coli* BL21, which decomposes PET into terephthalic acid (TPA) and ethylene glycol (EG). In order to further utilize degradation products, we overexpressed the ethylene glycol (EG) utilization pathway (fucO ,aldA) in *E.coli* BL21 to improve its survival rate.

In order to further utilize the degradation products of PET and synthesize useful products, the tph gene cluster (tphA2-tphA3-tphA1, tpaK tphB) was introduced into the *Pseudomonas putida* KT2440 to fully uptake and utilize terephthalic acid (TPA), followed by the introduction of rhlA, rhlB to endow it with the ability to produce rhamnolipids. In order to increase the production of rhamnolipids by *P.putida*, overexpression of the polyhydroxyalkanoate (PHA) degradation pathway (phaZ) in  *P.putida*  increases the carbon flux to rhamnolipids. Through the metabolic coupling system of *E.coli* BL21 and  *P.putida*, we have achieved efficient degradation of PET and upgraded the utilization of metabolic waste to synthesize fertilizers, innovatively solving the most threatening PET part in soil microplastics. We have also used rhamnolipids to alleviate the yield threat of microplastics to crops.

**2.Research center**

In addition to deploying our project designed products in polluted areas that require treatment with government funding, we have decided to collaborate with relevant research institutions to further develop our products.

The plasmids and strains we have constructed, as well as our design plan, will be awarded to research teams or institutions. Then, researchers can improve the efficiency of our target genes or vectors, or endow them with additional functions. Alternatively, they can use our pre-constructed strains to explore novel forms of carbon source supply and carbon flow pathways for the  *P.putida* KT2440, in order to enhance metabolite synthesis. Furthermore, our tracking teams shall be dispatched to monitor the progress of these strains and provide guidance and communication on cultivation environments, hardware facilities, and other conditions.

**3.Other iGEM teams**

Not limited to the initial project design, we designed a dual-enzyme system consisting of FAST-PETase and MHETase linked by a linker for efficient degradation of PET, and optimized the optimal combination using bioinformatics methods. If other teams are eager to improve the degradation efficiency of PET, they can refer to our carefully designed project design.

In addition, we supplemented the genome scale metabolic model of the *P.putida* KT2440. If other teams also need to simulate and estimate the production capacity and metabolic pathway integrity of specific products using the *P.putida*  KT2440, they can draw inspiration from our metabolic model modifications.

Finally, we developed a compact fermentation tank that allows us to simulate the supplementation of culture materials while precisely controlling temperature, pH, and oxygen concentration under laboratory conditions. From now on, if other iGEM teams also seek to simulate industrial planting needs, they can gain insights from our innovative hardware design.

## Safety

Firstly, *E. coli* would have been included in the iGEM's whitelist of strains; and *P. Putida* is a soil-dwelling bacterium to be certified as a safety strain by the Recombinant DNA Advisory Committee and has been highlighted as an optimal chassis for implantation of synthetic genetic circuits[^5]. Moreover, the general principles of microbiological and biomedical laboratory biosafety specify that BSL 1 is appropriate for microorganisms known to have no pathogenic effects on healthy adults. According to ATCC, the chassis organisms we have selected, such as *E. coli* BL21 and *P. putida* KT2440, can be used in a BSL 1 laboratory. Additionally, we plan to use nutrient-deficient strains in the later stages of the project to further ensure safety. Furthermore, our hardware is designed to ensure that all entrances and exits are equipped with bacteria filtration membranes and UV disinfection devices are installed to prevent any possible release of bacteria into the surrounding environment, thus ensuring the safety of the project.

In terms of regulations and policies, according to Article 5(1) of the Agreement on the Application of Sanitary and Phytosanitary Measures (SPS) by the World Trade Organization (WTO), it states that Members shall ensure that their sanitary or phytosanitary measures are based on an assessment, as appropriate to the circumstances, of the risks to human, animal or plant life or health, taking into account risk assessment techniques developed by the relevant international organizations[^6]. When conducting cross-regional exchanges and collaborations in this project, it is necessary to re-evaluate the safety of bacterial strains based on local quarantine and hygiene requirements. At the same time, efforts should be made to prevent any leakage of bacteria in the local area, thereby reducing the risk of cross-regional contamination. According to Article 13 of the "Regulations on the Safety Management of Agricultural Genetically Modified Organisms" issued by the State Council of the People's Republic of China, before conducting productive experiments and industrialization plans for our project, it is necessary to conduct preliminary small-scale "intermediate trials" and medium-scale "environmental release experiments" in different pilot areas[^7]. This means that during the process from laboratory experimentation to industrialization, we need to select different trial sites in various environmental regions for experiments in order to ensure that this genetically modified product will not contaminate the environment and is truly effective.

## Future design

## Challenges

Our project faces the following challenges：

1. More efficient and convenient production of ascending products (e.g., rhamnolipids, etc.), as the current production efficiency is slightly lower than expected; 
2. Fermentation methods suitable for different environments, such as integrated fermentation tanks that can be used for water, and targeted placement of bacteriophages for heavily contaminated areas of soil; 
3. Lower costs, such as the use of a more efficient culture solution as well as low-cost materials, which is convenient for popularization; 
4. A more precise and larger model, which can be achieved through the enriched detection of more samples, which helps our model to be more accurate in order to determine the high microplastic contamination area in the region.

## References

[^1]:Assessment of agricultural plastics and their sustainability: A call for action[J].
[^2]:WAN Y, WU C, XUE Q, 等. Effects of plastic contamination on water evaporation and desiccation cracking in soil[J/OL]. Science of The Total Environment, 2019, 654: 576-582[2024-10-02]. 
[^3]:吕一涵, 周杰, 杨亚东, 等. 微塑料对农田生态系统的影响:研究现状与展望[J/OL]. 中国生态农业学报, 2022, 30(1): 1-14. 
[^4]:李连祯, 周倩, 尹娜, 等. 食用蔬菜能吸收和积累微塑料[J/OL]. 科学通报, 2019, 64(9): 928-934. 
[^5]:Nikel, P. I., Martínez-García, E., & de Lorenzo, V. (2014). Biotechnological domestication of pseudomonads using synthetic biology. Nature Reviews Microbiology, 12(5), 368-379. 
[^6]:Sanitary and Phytosanitary Measures (SPS) by the World Trade Organization (WTO)
[^7]:"Regulations on the Safety Management of Agricultural Genetically Modified Organisms" -State Council of the People's Republic of China

