---
title: Model
permalink: /model/genome-scale/
feature_text: |
  ## Model
  The model is a means of assisting the overall completion and implementation of a project through computational methods.
  <br>
  We attempt to delve into various components of the project from design to implementation for model construction and computation.
feature_image: "https://static.igem.wiki/teams/5175/resources/background/bg-model.jpg"
excerpt: "The model is a means of assisting the overall completion and implementation of a project through computational methods."
---

## Genome-scale Metabolic Modeling

为了帮助湿实验代谢通路改造，并评估该项目在实际应用中的性能，我们构建了工程恶臭假单胞菌 KT2440的基因组规模代谢模型，能够动态模拟细胞代谢活动。与其他已发布GSSM相比，我们的模型得分达76%，超过已发表模型的平均水平。我们可以预测工程菌的生长行为、TPA吸收率和鼠李糖脂产品产量。我们估计工程恶臭假单胞菌可以高效吸收降解TPA，同时在此过程中生产鼠李糖脂。通过我们的GSSM，我们建立了一个基础，帮助未来的团队进一步进行恶臭假单胞菌的代谢工程，并进一步推动利用恶臭假单胞菌来降解塑料这一想法的前景。

### Methods

GSMM是一种表示、量化和比较特定生物新陈代谢的方法，将生物的代谢表示为一组包括关键基因表达、酶催化反应、运输机制和自发非催化反应的方程，主要使用磁通量平衡分析 （FBA） 或动态磁通量平衡分析 （dFBA） 进行分析[^1]。使用适用于 python 的 COBRA 包[^2]访问 MATLAB COBRA工具箱实现。

#### 代谢反应列表构建

 恶臭假单胞菌KT2440的初始代谢反应列表是从恶臭假单胞菌的最新高质量基因组规模代谢模型“iJN1463”中获得的[^3]。 以其为基础，加入TPA代谢通路和鼠李糖脂合成代谢通路，得到修改后的反应列表modified iJN1463。具体而言，TPA被代谢成乙酰辅酶 A和琥珀酰辅酶 A进入TCA 循环并与野生型的 β-酮己二酸通路联系起来，鼠李糖脂合成从脂肪酸合成通路中的底物β-hydroxyacyl-ACP起始并与dTDP-L-鼠李糖缩合。共加入7种代谢物和8个反应，并对其中phaZ调控的24个反应进行上限调整，以获得工程恶臭假单胞菌KT2440的生长行为。由于缺乏数据，假设在模拟过程中在铜绿假单胞菌代谢模型PAO1中设定的RHLA、RHLB通量上下限与工程恶臭假单胞菌相同。增加的反应列表如下（参见表 1 和 2）。

 <figcaption class="caption table_caption">表1.定义新加入的代谢物，ID后缀代表所在隔室<br>注：c:cytosol, e:extracellular space</figcaption>

 | Metabolite ID | Formula  | Name                                                       | Charge | Compartment |
| ------------- | -------- | ---------------------------------------------------------- | ------ | ----------- |
| tpa_c         | $C_8H_4O_4$   | Terephthalate                                              | -2     | c           |
| tpa_e         | $C_8H_4O_4$   | Terephthalate                                              | -2     | e           |
| dhchdc_c      | $C_8H_6O_6$   | (3S,4R)-3,4-Dihydroxycyclohexa-1,5-diene-1,4-dicarboxylate | -2     | c           |
| 3h3h_c        | $C_{20}H_{37}O_5$ | 3-hydroxydecanoyl-3-hydroxydecanoate                       | -1     | c           |
| 3h3h_e        | $C_{20}H_{37}O_5$ | 3-hydroxydecanoyl-3-hydroxydecanoate                       | -1     | e           |
| lrhh_c        | $C_{26}H_{47}O_9$ | L-rhamnosyl-3-hydroxydecanoyl-3-hydroxydecanoate           | -1     | c           |
| lrhh_e        | $C_{26}H_{47}O_9$ | L-rhamnosyl-3-hydroxydecanoyl-3-hydroxydecanoate           | -1     | e           |

<figcaption class="caption table_caption">表2.定义新加入的反应，EX_前缀代表交换反应 </figcaption>

| Reaction ID    | Name                         | Metabolites                                                  |
| -------------- | ---------------------------- | ------------------------------------------------------------ |
| EX_tpa_e       | Terephthalic acid exchange   | tpa_e: -1                                                    |
| TPA_transport  | TPA_transport                | tpa_e: -1, tpa_c: 1                                          |
| TPHA123        | TPA Dioxygenase Reaction     | tpa_c: -1, o2_c: -1, nadph_c: -1, h_c:  -1, dhchdc_c: 1, nadp_c: 1 |
| TPHB           | Diol Dehydrogenase Reaction  | dhchdc_c: -1, nadp_c: -1, dhbz_c: 1,  co2_c: 1, nadph_c: 1   |
| RHLA           | Rhamnosyltransferase chain A | hydroxydecanoyl_acp: -2, h2o_c: -1,  hydroxydecanoyl_hydroxydecanoate: 1, h_c: 1, ACP_c: 2 |
| RHLB           | Rhamnosyltransferase chain B | hydroxydecanoyl_hydroxydecanoate: -1,  dtdprmn_c: -1, dtdp_c: 1, h_c: 1, lrhh_c: 1 |
| EX_lrhh_e      | lrhh exchange                | lrhh_e: 1                                                    |
| lrhh_transport | lrhh_transport               | lrhh_c: -1, lrhh_e: 1                                        |




<center>{% include button.html link="../" text="Go back to Model Introduction" %}</center>

---

## References

[^1]: Heirendt L, Arreckx S, Pfau T, et. al. Creation and analysis of biochemical constraint-based models using the COBRA Toolbox v.3.0. Nat Protoc. 2019 Mar;14(3):639-702. doi: 10.1038/s41596-018-0098-2. PMID: 30787451; PMCID: PMC6635304. 
[^2]: Ebrahim A, Lerman JA, Palsson BO, Hyduke DR. COBRApy: COnstraints-Based Reconstruction and Analysis for Python. BMC Syst Biol. 2013 Aug 8;7:74. doi: 10.1186/1752-0509-7-74. PMID: 23927696; PMCID: PMC3751080. 
[^3]: Nogales J, Mueller J, Gudmundsson S, et, al. High-quality genome-scale metabolic modelling of Pseudomonas putida highlights its broad metabolic capabilities. Environ Microbiol. 2020 Jan;22(1):255-269. doi: 10.1111/1462-2920.14843. Epub 2019 Nov 11. PMID: 31657101; PMCID: PMC7078882. 
