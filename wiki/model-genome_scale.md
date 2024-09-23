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



<center>{% include button.html link="../" text="Go back to Model Introduction" %}</center>

---

## References

[^1]: Heirendt L, Arreckx S, Pfau T, et. al. Creation and analysis of biochemical constraint-based models using the COBRA Toolbox v.3.0. Nat Protoc. 2019 Mar;14(3):639-702. doi: 10.1038/s41596-018-0098-2. PMID: 30787451; PMCID: PMC6635304. 
[^2]
