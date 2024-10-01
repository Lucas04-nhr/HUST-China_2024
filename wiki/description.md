---
title: Description
permalink: /description/
feature_text: |
  ## Description
  A brief introduction to our project.
feature_image: "https://static.igem.wiki/teams/5175/resources/background/bg-description.jpg"
excerpt: "A brief introduction to our project."
---

## Origin

During the summer of 2023, while completing our school's "Triple Services Activity into Rural Areas" summer social practice activity, we stumbled upon piles of black and transparent plastic bags strewn along the edges of rice fields. These unsightly heaps of waste stood in stark contrast to the natural beauty of the landscape, in direct contact with the crops destined for people's tables. This disturbing sight raised an unsettling question: could plastic waste be contaminating farmland and posing a threat to agriculture? Motivated by this concern, we conducted an extensive literature review. Our findings revealed that plastic waste in farmland causes microplastic pollution, which not only directly reduces crop yields but also poses a serious risk to human health. What's even more alarming is that the dangers of farmland plastic pollution don't emerge suddenly; they slowly seep into every aspect of our lives, often going unnoticed and neglected as a critical issue.

{% include figure.html image="https://static.igem.wiki/teams/5175/resources/description/description-01.png" caption="Plastic Waste in Agricultural Fields" %}

## Background

From 1950 to 2015, human society produced approximately 8.3 billion tons of plastic, resulting in about 6.3 billion tons of plastic waste. Of this waste, 79% ended up in landfills or leaked into the environment[^1]. Once large plastic materials enter the environment, they break down into smaller particles through weathering and degradation, forming microplastics—particles ranging from 100 nm to 5 mm in diameter.

Microplastics easily penetrate soil pores and quickly migrate to deeper layers. Once in the soil, they integrate into soil aggregates, leading to a reduction in organic matter, alkaline nitrogen, available phosphorus, and available potassium levels. This disrupts soil structure, decreases the amount of air and water in the soil, and hampers their distribution. Consequently, the germination and root growth of crops are inhibited, resulting in a significant drop in agricultural yields. Additionally, microplastics in the soil can be absorbed by plant roots and enter the human body through the food chain. They may even penetrate the cellular barrier, the blood-brain barrier, and the placenta[^2], influencing gene expression and causing adverse effects such as DNA damage, oxidative stress, tissue necrosis, and potentially leading to malignant diseases like tumors[^3].

The use of plastic films in agriculture has been reported to increase crop yields by 39.5%[^4]. Similar plastic products are employed on a large scale because they provide short-term benefits in boosting crop production and economic gains. According to the United Nations Food and Agriculture Organization (FAO), the agricultural sector consumes 12.5 million tons of plastic annually, while food packaging alone consumes 37.3 million tons. Experts predict that due to rising demand for greenhouses, plastic mulch, and silage films, plastic use in agriculture will increase by 50% or more in the coming years. In Asia, 3 million hectares of land are covered with 1.45 million tons of plastic mulch annually, accounting for 75% of global usage. Plastics are difficult to degrade under natural conditions due to their highly hydrophobic and chemically stable structure, featuring covalent bonds and functional groups resistant to breakdown. As a result, they gradually accumulate in the form of microplastics in soils. Each year in China, 200,000 to 300,000 tons of residual plastic films are left behind in farmlands, leading to high concentrations of microplastics in agricultural soils.

Beyond plastic products, organic fertilizers, plastic films, and irrigation water are major sources of microplastic pollution in farmland. In particular, irrigation water—often drawn from rivers, lakes, and other surface water bodies—has become a key contributor to the problem, given the widespread presence of microplastics in these water sources. Prolonged use of microplastic-contaminated irrigation water only exacerbates the accumulation of microplastics in soils, threatening crop yields and posing serious risks to human health.

Polyethylene terephthalate (PET), a durable and thermoplastic polyester, is one of the most commonly used plastics and a significant component of microplastics in soil. To reduce PET concentrations and alleviate soil microplastic pollution, we aim to utilize synthetic biology to engineer bacteria that can degrade PET in irrigation water. Furthermore, we intend to use the degradation products to synthesize organic matter that can regulate soil pH and microbial activity, providing an efficient, economical, and environmentally friendly solution to the issue of microplastic degradation in soil.

## *Escherichia coli* BL21 and *Pseudomonas putida* KT2440

The research team sought to identify microorganisms and their metabolic pathways that could be employed to degrade PET. Following an exhaustive investigation, we ultimately selected *E. coli* BL21 with *Pseudomonas putida* KT2440 as our chassis organisms. *E. coli*, one of the most extensively studied chassis organisms, facilitates genetic modification while enabling the use of its readily available metabolic pathways to produce by-products. The objective is to engineer the *E. coli* BL21 strain to secrete efficient PET hydrolases that will degrade PET plastic into monomers, namely ethylene glycol (EG) and terephthalic acid (TPA). The EG will be utilized by *E. coli* BL21 for metabolic energy production, while TPA will be converted by *Pseudomonas putida* KT2440 into soil remediation organisms, namely rhamnolipids. *E. coli* BL21 has a natural ethanolic acid metabolic pathway, which was genetically modified to improve the efficiency of EG conversion to ethanolic acid for metabolic energy production. *Pseudomonas putida* KT2440 has natural phenolic and lipid metabolism pathways. The introduction of exogenous genes has the effect of increasing the TPA utilization pathway and modifying the original metabolic pathway to synthesize rhamnolipids. Rhamnolipid is a surfactant that can accelerate the degradation of compost organic matter in agricultural production activities, reduce soil caking, and improve soil physicochemical properties. The combined effect of these two strains will result in the transformation and upgrading of PET to soil remediation organisms, effectively alleviating the problem of soil microplastic pollution.

{% include figure.html image="https://static.igem.wiki/teams/5175/resources/description/description-02.png" caption="The Schematic diagram of the metabolic coupling system between <em>Escherichia coli</em> BL21 and <em>Pseudomonas putida</em> KT2440." %}

## Hardware

We are working to develop a controlled and closed system for our co-culture setup to efficiently capture and degrade microplastics. This system will allow for precise testing in the laboratory while also laying the groundwork for future industrial applications. We have designed a microplastic enrichment device, and building on the modular design proposed last year, we have constructed a co-culture bioreactor of *Escherichia coli* and *Pseudomonas putida*. We further refined the design of the modular bioreactor, incorporating a bidirectional flow temperature control system to ensure both the convenience and replicability of the design. This hardware development continues to advance synthetic biology by enhancing the hardware implementation. As a result, we have successfully created a fermentation system based on our co-culture setup.

{% include figure.html image="https://static.igem.wiki/teams/5175/resources/description/description-03.png" caption="Sample lab diagram of the application hardware." %}

---

## References

[^1]: LIN D, YANG G, DOU P, et al. Microplastics negatively affect soil fauna but stimulate microbial activity: Insights from a field-based microplastic addition experiment: Microplastics affect soil biota [J]. Proceedings of the Royal Society B: Biological Sciences, 2020, 287(1934).
[^2]: Plastic planet: How tiny plastic particles are polluting our soil
[^3]: SINGH S, TRUSHNA T, KALYANASUNDARAM M, et al. Microplastics in drinking water: a macro issue [J]. Water science & technology: Water supply, 2022, 22(5): 5650-74.
[^4]: Xiao L, Wei X, Wang C, Zhao R. Plastic film mulching significantly boosts crop production and water use efficiency but not evapotranspiration in China. Agric Water Manag. 2023;275:108023. doi:10.1016/j.agwat.2022.108023
 