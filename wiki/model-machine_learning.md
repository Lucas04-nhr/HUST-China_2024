---
title: Machine Learning
permalink: /model/machine-learning/
feature_text: |
  ## Model
  The model is a means of assisting the overall completion and implementation of a project through computational methods.
  <br>
  We attempt to delve into various components of the project from design to implementation for model construction and computation.
feature_image: "https://static.igem.wiki/teams/5175/resources/background/bg-model.jpg"
excerpt: "The model is a means of assisting the overall completion and implementation of a project through computational methods."
---

## Machine Learning

微塑料污染已然成为全球环境问题，广泛存在于海洋、湖泊和土壤中，对生态系统和人类健康造成潜在威胁，亟需加强监测和治理。一项研究发现，在中国的农田土壤中，微塑料的浓度可达到每千克土壤20-30颗（ Zhang, Y., et al. (2020).）。微塑料对生态和人类健康构成威胁，可能通过食物链影响生物，导致毒素积累。如果不适当控制微塑料污染扩散，微塑料将摧毁当地的生态系统和许多人赖以生存的土地。为了进一步了解当前和未来的微塑料土壤污染区域，我们整合已有的微塑料丰度数据和相关的辅助环境变量，通过构建线性或非线性模型将田间采样与机器学习相结合，模拟和预测区域土壤中微塑料污染的分布，在比较6种机器学习模型后，选取SVR-RBF预测并绘制研究区土壤MPs模拟污染空间图，以辅助硬件的微塑料降解菌液发酵罐的选址，以及未来可能制成的降解菌剂的定点定量喷洒，为微塑料污染的治理提供更精准的指导。

### Model data selection and processing

{% include figure.html image="https://static.igem.wiki/teams/5175/resources/model/model-machine-learning-01.png" alt="Sampling data of microplastics abundance in Wuhan" caption="Figure 1. Sampling data of microplastics abundance in Wuhan"}

参考已有文献中采用多元回归决策树（MRT）方法分离出影响MPs空间丰度和组成的源汇相关因子，我们选择5个源汇因子和7个汇因子（TXT S1），其中的土壤属性数据 [^1] 来自<a href="https://www.fao.org/soils-portal/data-hub/en/" target="_blank">世界土壤数据库（HWSD）</a>，空间分辨率为1km，地理坐标系为WGS_1984_Albers，人口密度数据来自<a href="https://www.geodata.cn" target="_blank">National Earth System Science Data Center</a>，耕地、路网、建筑物数据来自<a href="https://www.openstreetmap.org/" target="_blank">OpenStreetMap</a>，POI数据选取8类不同POI，基于<a href="https://github.com/Civitasv/AMapPoi" target="_blank">AMapPOI</a>使用百度地图API SDK服务抓取了POI数据，通过ArcGIS 10.7（ESRI，USA）进行数据处理。

利用以往在武汉市采样的MPs丰度实测数据 [^2]（图1），将数据按3：1的比例分为训练集和预测集用于训练模型。由于影响土壤MPs发生的源汇因子在维度和数量级上存在差异，因此采用min-max方法对输入数据进行归一化，以避免潜在问题。

### Model selection and evaluation

我们选择了6种常用的机器学习模型进行测试对比，从模型的数量和性质来看，可以分为单个模型和集成模型。

单一模型包含BP-GAO、LSTM、RBF三种神经网络和SVR-RBF模型。集成模型则包含XGBoost、RF，将多个单一模型组合成一个强大的模型，利用所有单个模型来实现更优越的性能。它们各有优势：BP-GAO通过遗传算法优化神经网络的初始参数，然后利用反向传播算法进一步调整网络权重，提高了学习效率和性能；RBF隐藏层神经元使用径向基函数作为激活函数，通常以欧氏距离作为输入，输出层则是隐藏层输出的线性组合，具有局部逼近特性;LSTM引入了门控机制解决了传统RNN中的梯度消失问题，具备长期依赖信息的保持能力；SVR-RBF通过最小化正则化误差来预测连续的数值输出，同时保持模型的泛化能力;XGBoost通过优化目标函数的一阶和二阶导数来提高模型性能，具有处理大规模数据集和自动特征选择的能力;RF在处理高维数据时表现出色，并且能够自然地处理分类和回归问题。

我们基于拟合优度 （R<sup>2</sup>）、均方根误差（RMSE）和平均绝对误差（MAE）三个标准考虑不同机器学习模型的模拟和预测精度。

<center>
  $R^2=1-\frac{\sum{_{i=1}^{N}\left( p_i-a_i \right)}^2}{\sum{_{i=1}^{N}\left( a_i-\bar{a} \right)}^2}$
  <br>
  $RMSE=\sqrt{\frac{1}{N}\sum{_{i=1}^{N}\left( p_i-a_i \right) ^2}}$
  <br>
  $MAE=\frac{1}{N}\sum{_{i=1}^{N}|p_i-a_i|}$
</center>


<center>{% include button.html link="../" text="Go back to Model Introduction" %}</center>

---

## References

[^1]: FAO & IIASA. 2023. Harmonized World Soil Database version 2.0. Rome and Laxenburg. doi: 10.4060/cc3823en
[^2]: Zhou, Y., Wang, T., Zou, M., et.al. (2023). Trends in the occurrence and accumulation of microplastics in urban soil of Nanjing and their policy implications. Science of The Total Environment, 903, 166144.

