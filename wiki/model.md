---
title: Model
permalink: /model/
feature_text: |
  ## Model
  The model is a means of assisting the overall completion and implementation of a project through computational methods.
  <br>
  We attempt to delve into various components of the project from design to implementation for model construction and computation.
feature_image: "https://static.igem.wiki/teams/5175/resources/background/bg-model.jpg"
excerpt: "The model is a means of assisting the overall completion and implementation of a project through computational methods."
---

## Introduction

The model is a means of assisting the overall completion and implementation of a project through computational methods.
We attempt to delve into various components of the project from design to implementation for model construction and computation.

{% include figure.html image="https://static.igem.wiki/teams/5175/resources/model/model-01.jpg" alt="Introduction of Modeling" caption="Introduction of Modeling" %}

### Optimization of Dual-Enzyme System

In project design, we aim to optimize the dual enzyme system of PETase-MHETase. We consider the impact of the types and lengths of linkers, with the order of PETase and MHETase in the peptide chain. With molecular docking, we use docking simulations and scoring function to obtain the optimal dual enzyme system.

### Genome-Scale Metabolic Modeling

To support the results from Wet Lab, we have developed a genome-scale metabolic model for the engineered Pseudomonas putida KT2440. This model predicts its growth behavior, TPA absorption rate, and rhamnolipid product yield. We estimate that the engineered strain can efficiently absorb and degrade TPA while producing rhamnolipids in the process.

### Spatial Prediction Model for Microplastics

Understanding the spatial distribution characteristics of microplastics is an important prerequisite for controlling soil pollution, which can assist the location selection of the fermentation tank for hardware. We plan to use machine learning to predict the spatial distribution with existing microplastic abundance data and environmental source-sink data.

---

## Molecular Docking

分子对接（molecular docking）是指通过计算模拟小分子与靶标分子之间的相互作用，以预测它们的结合模式和结合位点的过程。在实验设计中，我们预期找到降解PET效率最高的PETase-MHETase双酶体系，预估双酶体系中Linker的种类以及长度，PETase与MHETase在肽段上的先后会对降解效率产生影响，因而采用分子对接来探究各因素对于PET与双酶体系中PETase的结合亲和力的影响，最终得到最高效的双酶体系搭配组合PETase-ggggs(15)-MHETase用于后续的实验设计和湿实验部分。

### Materials

从PDB获取FAST -PETase与MHETase的序列信息。常用linker分为柔性linker与刚性linker，柔性linker能够提供更大的灵活性，允许连接的酶自由旋转和运动，使其能够适应动态的相互作用，而刚性linker可以防止两个酶之间的过度接近或旋转，保持适当的空间分离，减少相互干扰。选取了广泛使用的柔性linker（GGGGS，GSGSG与GGGGG）与刚性linker （EAAAK与 PAPAP）并采取不同的linker长度（分别为10,15,20,25,30,35个氨基酸）来构建PETase-Linker-MHETase双酶体系。
双酶体系的立体结构通过AlphaFold Server[^1]获得，并使用AutoDockTools进行加极性氢处理，作为对接的受体。配体通过Avogadro来进行构建。Avogadro是an advanced semantic chemical editor, visualization, and analysis platform[^2], 我们用其构建并最小化4PET作为分子对接的配体。


---

## References

[^1]: Abramson, J., Adler, J., Dunger, J. et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 493–500 (2024).
[^2]: Hanwell, M.D., Curtis, D.E., Lonie, D.C. et al. Avogadro: an advanced semantic chemical editor, visualization, and analysis platform. J Cheminform 4, 17 (2012). 


