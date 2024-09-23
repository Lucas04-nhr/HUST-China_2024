---
title: Molecular Docking
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

使用AutoDock vina[^3] [^4]将配体受体对接，box参数通过参考PETase上的催化三联体（Ser133 Asp179 His210）以及氧阴离子空穴（Tyr60 Met134）[^5]位置来配置。对接采用半柔性对接，配体4PET被设为柔性分子，受体均被设为刚性分子。对接结束后，选取具有最低结合能的构象作为判断配体与受体亲和力的依据。

AutoDock Vina的构象相关部分使用如下评分函数：

<center>$c = \sum f _ { t _ { i } t _ { j } } ( r _ { i j } )$</center>

其中求和范围是所有可以相对运动的原子对，每个原子$i$被分配一个类型$t_i$，并定义了与原子间的距离有关的相互作用函数$f$。

值$c$可以看作是分子间和分子内贡献的总和，即：

<center>$c = c _ { \mathrm{inter} } + c _ { \mathrm{intra} }$</center>

### Results

通过改变linker种类，linker长度以及PETase与MHETase的前后顺序，探究这些因素对PET与PETase的亲和力影响。使用了5种linker、 6种不同的linker长度、2种顺序共计比较了60种组合，得到亲和力数据（见附件[^6]，图1）。

{% include figure.html 
  image="https://static.igem.wiki/teams/5175/resources/model/molecular-docking-01.png" 
  alt="Molecular Docking" 
  caption="图1.分子对接的部分结果，显示出对接完成后PET的构象以及形成的氢键，红色部分为4PET，蓝色部分为与PET形成氢键的氨基酸残基。蛋白名称中f代表FAST-PETase, eaaak等代表linker种类，括号中为linker的长度（氨基酸个数），m代表MHETase" 
%}

从对接结果中可以看出，部分使用刚性linker的双酶体系中PETase对PET的亲和力较好，但考虑到柔性linker可以提供更大的灵活性，允许连接的酶自由旋转和运动，使其能够适应动态的相互作用，故倾向于选择柔性linker。柔性linker中PETase-gsgsg(35)-MHETase虽具有最大的亲和力，但通过对接结果可以看出其PET与两个酶同时发生了作用，故综合考虑下，采用了亲和力较好且对接结果中氢键较合理的PETase-ggggs(15)-MHETase（见图2）。

{% include figure.html 
  image="https://static.igem.wiki/teams/5175/resources/model/molecular-docking-02.png" 
  alt="Molecular Docking" 
  caption="图2.PETase-ggggs(15)-MHETase的对接结果图。其中红色部分为4PET，绿色部分为PETase，粉色部分是长为15个氨基酸，种类为ggggs的linker，黄色部分为MHETase"
%}

### Limitation

分子对接探究了不同双酶体系中PETase对PET亲和力的影响，从亲和力的角度给与了选择不同双酶体系的依据。但4PET与单体FAST-PETase对接的结合能为-9.8 kcal/mol，这意味着双酶体系降解PET效率的提高并不能从亲和力的角度去解释，未来的团队可更多去考虑PETase反应产物的扩散带来的影响。
  
对接的过程中采用的是半柔性对接，将受体设置为了刚体，与实际情况有所差异，后续可以考虑将PETase的催化位点设置为柔性，以此可以得到更为准确的结合能。
  
计算方法本身具有局限性，AutoVock Vina采用的是迭代局部搜索全局优化，这意味着存在没找到最优构象的可能性，可以通过适当增加重复计算的次数以减少这一概率。



<center>{% include button.html link="../" text="Go back to Model Introduction" %}</center>

---

## References

[^1]: Abramson, J., Adler, J., Dunger, J. et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 493–500 (2024). doi: 10.1038/s41586-024-07487-w
[^2]: Hanwell, M.D., Curtis, D.E., Lonie, D.C. et al. Avogadro: an advanced semantic chemical editor, visualization, and analysis platform. J Cheminform 4, 17 (2012). doi: 10.1186/1758-2946-4-17
[^3]: Trott O, Olson AJ. AutoDock Vina: improving the speed and accuracy of docking with a new scoring function, efficient optimization, and multithreading. J Comput Chem. 2010 Jan 30;31(2):455-61. doi: 10.1002/jcc.21334. PMID: 19499576; PMCID: PMC3041641.
[^4]: Eberhardt J, Santos-Martins D, Tillack AF, Forli S. AutoDock Vina 1.2.0: New Docking Methods, Expanded Force Field, and Python Bindings. J Chem Inf Model. 2021 Aug 23;61(8):3891-3898. doi: 10.1021/acs.jcim.1c00203. Epub 2021 Jul 19. PMID: 34278794; PMCID: PMC10683950.
[^5]: García-Meseguer R, Ortí E, Tuñón I, Ruiz-Pernía JJ, Aragó J. Insights into the Enhancement of the Poly(ethylene terephthalate) Degradation by FAST-PETase from Computational Modeling. J Am Chem Soc. 2023 Sep 6;145(35):19243-19255. doi: 10.1021/jacs.3c04427. Epub 2023 Aug 16. PMID: 37585687; PMCID: PMC10851425.
[^6]: <a href="https://static.igem.wiki/teams/5175/resources/model/molecular-docking-result.csv" target="_blank">Press here</a> to download the result CSV file.


