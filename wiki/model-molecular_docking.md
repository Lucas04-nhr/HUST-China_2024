---
title: Model
permalink: /model/molecular-docking/
feature_text: |
  ## Model
  The model is a means of assisting the overall completion and implementation of a project through computational methods.
  <br>
  We attempt to delve into various components of the project from design to implementation for model construction and computation.
feature_image: "https://static.igem.wiki/teams/5175/resources/background/bg-model.jpg"
excerpt: "The model is a means of assisting the overall completion and implementation of a project through computational methods."
---

## Molecular Docking

分子对接（molecular docking）是指通过计算模拟小分子与靶标分子之间的相互作用，以预测它们的结合模式和结合位点的过程。在实验设计中，我们预期找到降解PET效率最高的PETase-MHETase双酶体系，预估双酶体系中Linker的种类以及长度，PETase与MHETase在肽段上的先后会对降解效率产生影响，因而采用分子对接来探究各因素对于PET与双酶体系中PETase的结合亲和力的影响，最终得到最高效的双酶体系搭配组合PETase-ggggs(15)-MHETase用于后续的实验设计和湿实验部分。

### Materials

从PDB获取FAST -PETase与MHETase的序列信息。常用linker分为柔性linker与刚性linker，柔性linker能够提供更大的灵活性，允许连接的酶自由旋转和运动，使其能够适应动态的相互作用，而刚性linker可以防止两个酶之间的过度接近或旋转，保持适当的空间分离，减少相互干扰。选取了广泛使用的柔性linker（GGGGS，GSGSG与GGGGG）与刚性linker （EAAAK与 PAPAP）并采取不同的linker长度（分别为10,15,20,25,30,35个氨基酸）来构建PETase-Linker-MHETase双酶体系。
双酶体系的立体结构通过AlphaFold Server[^1]获得，并使用AutoDockTools进行加极性氢处理，作为对接的受体。配体通过Avogadro来进行构建。Avogadro是an advanced semantic chemical editor, visualization, and analysis platform[^2], 我们用其构建并最小化4PET作为分子对接的配体。

### Methods

使用AutoDock vina[^3][^4]将配体受体对接，box参数通过参考PETase上的催化三联体（Ser133 Asp179 His210）以及氧阴离子空穴（Tyr60 Met134）位置来配置。对接采用半柔性对接，配体4PET被设为柔性分子，受体均被设为刚性分子。对接结束后，选取具有最低结合能的构象作为判断配体与受体亲和力的依据。



<center>{% include button.html link="../" text="Go back to Model Introduction" %}</center>

---

## References

[^1]: Abramson, J., Adler, J., Dunger, J. et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 493–500 (2024). doi: 10.1038/s41586-024-07487-w
[^2]: Hanwell, M.D., Curtis, D.E., Lonie, D.C. et al. Avogadro: an advanced semantic chemical editor, visualization, and analysis platform. J Cheminform 4, 17 (2012). doi: 10.1186/1758-2946-4-17
[^3]: Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient optimization, and multithreading. J Comput Chem. 2010 Jan 30;31(2):455-61. doi: 10.1002/jcc.21334. PMID: 19499576; PMCID: PMC3041641.
[^4]: Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: New Docking Methods, Expanded Force Field, and Python Bindings. J Chem Inf Model. 2021 Aug 23;61(8):3891-3898. doi: 10.1021/acs.jcim.1c00203. Epub 2021 Jul 19. PMID: 34278794; PMCID: PMC10683950.


