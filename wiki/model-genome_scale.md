---
title: Genome-scale Metabolic Modeling
permalink: /model/genome-scale/
feature_text: |
  ## Model
  The model is a means of assisting the overall completion and implementation of a project through computational methods.
  <br>
  We attempt to delve into various components of the project from design to implementation for model construction and computation.
feature_image: "https://static.igem.wiki/teams/5175/resources/background/bg-model.jpg"
excerpt: "The model is a means of assisting the overall completion and implementation of a project through computational methods."
images01:
  - src: https://static.igem.wiki/teams/5175/resources/model/model-gssm-02.png
    alt: A Figure of dFBA Simulation Results
    caption: 图1<br>生物质浓度以克干重 （gDW） 为单位，底物浓度以 mmol 为单位。<br>模拟开始时，菌株的初始生物量为 0.1 gDW，鼠李糖脂由于生成量过少难以辨别，补充见图2
  - src: https://static.igem.wiki/teams/5175/resources/model/model-gssm-03.png
    alt: A Figure of dFBA Simulation Results
    caption: 图2.在图1模拟条件下鼠李糖脂生成的补充图像

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

#### 模型性能评估

我们利用 Memote v0.14.0 [^4]软件中给出的指标来评估我们的GSMM的水平。Memote 提供了符合 GSMM 理想构建共识的质量控制和保证指标，分为四类：注释、基本测试、生物质反应和化学计量。注释测试确保 SBML 格式模型中的交叉引用完整且符合 MIRIAM 标准，这对于 GSMM 的扩展和使用至关重要 (Lieven at al. 2020)。基本测试确保模型的形式正确性，生物质测试评估不同介质中的一致生长，化学计量测试确保从模型中消除质量和能量的不一致。

#### dFBA 实现（时间分辨模拟）

对于 dFBA 模拟，初始培养基成分设置为 200 mmol TPA作为碳源，令葡萄糖含量为0，以评估在富TPA环境下的生长状态。其他必要的非碳代谢物（例如氧气、二氧化碳、水等）设置为 1000 mmol，以确保生长模拟不受它们的限制。动态调整 TPA 的最大摄取速率，通过计算通量并乘以一个小的时间间隔常数，可以给出介质组成在时间框架上的近似变化。0.1小时的时间步长提供了良好的分辨率和适度的计算时间。将这一变化从初始介质组成中减去，得到一个新的初始介质组成。[^5] 重复该过程，直到dFBA求解函数到达计算极限。在每个时间步长，存储介质浓度向量用于绘图和分析。

You can <a href="https://static.igem.wiki/teams/5175/resources/model/model-gssm-attachment-01.csv" target="_blank">click here</a> to download the original ingredient of the culture medium.

### Results

#### 模型性能评估

Norsigian等人评估了在Bigg中发布的模型的Memote得分，发现JSON格式的模型的平均得分为58％，SBML格式的模型的平均得率为73％。[^5] 我们的模型为SBML格式，得分达76%，超过已发表模型的平均水平，有理由相信我们的模型能在一定程度上良好地反映实际情况。

{% include figure.html image="https://static.igem.wiki/teams/5175/resources/model/model-gssm-01.png" alt="Our Memote Score" caption="Figure 1. Our Memote Score" %}

#### 动态磁通平衡分析 （dFBA）模拟

通过使用 dFBA 对工程恶臭假单胞菌在富TPA的培养环境下的代谢活动进行建模，分别定性评价工程菌的TPA处理能力和鼠李糖脂生产能力。
模拟如预期的那样预测了工程菌的演变，在 TPA 作为主要碳源的环境中，恶臭假单胞菌能成功生长，表明该菌株具备有效的 TPA 代谢能力。TPA含量持续下降并在生物质积累到一定量后开始有少量鼠李糖脂生成。在初期，细胞可能集中资源用于生长，而一旦达到一定生物量，代谢途径逐渐转向次级代谢物的合成，如鼠李糖脂。通过 dFBA 预测其鼠李糖脂开始生成的时间和产量变化，将为优化生产条件提供思路。

{% include figure2.html images=page.images01 %}

## Discussion

我们完成了时间分辨的工程恶臭假单胞菌基因组规模代谢模型modified_iJN1463。memote证明了我们的模型的完整可靠。我们希望未来的团队可以通过进一步的生长和代谢组学数据来提高其准确性和验证性。
使用时间依赖型 dFBA 生成的生长曲线显示了预期的总体趋势。然而，无法通过实验确定潜在的估计塑料降解率。对塑料解聚速率本身进行建模具有挑战性，因为该模型无法预测酶的表达强度，而酶的表达强度与降解速率直接相关。
由于我们的模型未经进一步验证，就无法从该模型得出大型生物反应器中的生长行为，因为放大很可能不像将通量乘以特定因子那么简单。有必要在实验室中使用不同尺寸的生物反应器进行更多的生长实验，以微调模型并可能预测每个参数的函数。然后，可以将额外的数据集成到 dFBA 模型中，以优化参数以最好地描述代谢组学数据。
通过允许代谢通量成为底物浓度依赖性，可以进一步改进 dFBA 模拟。Michaelis-Menten 动力学可用于解决此问题，但是，基因组规模代谢模型所需的 vmax 和 Km 值不存在。质量作用动力学可能是近似生长率的宝贵替代方法。包括底物浓度依赖性通量将允许更准确地预测从指数到稳定相的过渡。
尽管存在这些限制，我们仍然相信代谢模型将对项目未来进展继续做出贡献，通过与 Wet Lab 团队的持续合作，我们可以改进模型，同时优化 Wet Lab 实验。



<center>{% include button.html link="../" text="Go back to Model Introduction" %}</center>

---

## References

[^1]: Heirendt L, Arreckx S, Pfau T, et. al. Creation and analysis of biochemical constraint-based models using the COBRA Toolbox v.3.0. Nat Protoc. 2019 Mar;14(3):639-702. doi: 10.1038/s41596-018-0098-2. PMID: 30787451; PMCID: PMC6635304. 
[^2]: Ebrahim A, Lerman JA, Palsson BO, Hyduke DR. COBRApy: COnstraints-Based Reconstruction and Analysis for Python. BMC Syst Biol. 2013 Aug 8;7:74. doi: 10.1186/1752-0509-7-74. PMID: 23927696; PMCID: PMC3751080. 
[^3]: Nogales J, Mueller J, Gudmundsson S, et, al. High-quality genome-scale metabolic modelling of Pseudomonas putida highlights its broad metabolic capabilities. Environ Microbiol. 2020 Jan;22(1):255-269. doi: 10.1111/1462-2920.14843. Epub 2019 Nov 11. PMID: 31657101; PMCID: PMC7078882. 
[^4]: Lieven C, Beber ME, Olivier BG, et. al. MEMOTE for standardized genome-scale metabolic model testing. Nat Biotechnol. 2020 Mar;38(3):272-276. doi: 10.1038/s41587-020-0446-y. Erratum in: Nat Biotechnol. 2020 Apr;38(4):504. doi: 10.1038/s41587-020-0477-4. PMID: 32123384; PMCID: PMC7082222. 
[^5]: Norsigian CJ, Pusarla N, McConn JL, Yurkovich JT, Dräger A, Palsson BO, King Z. BiGG Models 2020: multi-strain genome-scale models and expansion across the phylogenetic tree. Nucleic Acids Res. 2020 Jan 8;48(D1):D402-D406. doi: 10.1093/nar/gkz1054. PMID: 31696234; PMCID: PMC7145653. 
