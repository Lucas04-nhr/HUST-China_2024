---
title: Hardware
permalink: /hardware/
feature_text: |
  ## Hardware
  Welcome to iGEM HUST-China 2024 wiki! It's still under construction. Please stay tuned for more information.
feature_image: "https://static.igem.wiki/teams/5175/resources/background/bg-hardware.jpg"
excerpt: "Welcome to iGEM HUST-China 2024 wiki! It's still under construction. Please stay tuned for more information."
# Multiple Figures
images01:
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-01.png
    alt: 
    caption: 
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-02.png
    alt: 
    caption: 

images02:
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-03.png
    alt: 
    caption: 
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-04.png
    alt: 
    caption: 

images03:
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-05.png
    alt: 
    caption: 
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-06.png
    alt: 
    caption: 
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-07.png
    alt: 
    caption: 

images04:
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-08.png
    alt: 
    caption: 

images05:
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-09.png
    alt: 
    caption: 
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-10.png
    alt: 
    caption: 
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-11.png
    alt: 
    caption: 

images06:
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-13.png
    alt: 
    caption: 
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-14.png
    alt: 
    caption:

images07:
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-15.png
    alt: 
    caption: 
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-16.png
    alt: 
    caption: 

images08:
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-17.png
    alt: 
    caption: 
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-18.png
    alt: 
    caption: 

images09:
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-19.png
    alt: 
    caption: 
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-20.png
    alt: 
    caption: 

images10:
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-23.png
    alt: 
    caption: 
  - src: https://static.igem.wiki/teams/5175/resources/hardware/hardware-24.png
    alt: 
    caption:
---

## Background

微塑料虽然已经在环境中广泛存在，但目前处理微塑料分子的难点之一就是在于，塑料产品在环境中物理分解后，形成小粒径的颗粒，难以被回收再利用。因此硬件方面的第一项工作就是要首先完成对环境样本中的微塑料进行富集，提高后续系统降解的效率。我们首先决定在土壤中富集微塑料颗粒，但是（），最后决定把目标转向富含微塑料的水体。
鼠李糖脂作为一种生物活性物质，有利于农作物生长。为了使该体系更具适用性，我们硬件部分设计了微塑料富集装置、大肠杆菌和恶臭甲单胞菌共培养发酵罐以及产物灌溉装置。

土壤到水体，菌剂到硬件（hp还没给）

## 富集

## 发酵罐

### Overview

为了实现恶臭假单胞菌KT2440和大肠杆菌BL21的共培养并完成反应，我们设计了如上图所示的发酵罐结构。我们通过设计互相啮合的螺纹，来保证其结构的完整性。从外观上看，发酵罐呈现上下对称的结构，如同一个沙漏，具有几何的美感。我们在罐体的所有液体交换开口处均有滤菌膜防护，以保证菌体不会逸散到外界环境中。

### Structure

发酵罐整体为一套双向流动系统，包括由上到下的温度差异型培养系统和由左到右的待处理样品流动系统，可分为上罐、中层、下罐和搅拌棒四个部分。

#### 上罐部分

{% include figure2.html images=page.images01 %}

{% include figure2.html images=page.images02 %}

上罐为大肠杆菌发酵场所，由顶盖和罐体组成。整体漏斗形的设计既增大了培养空间，也便于实现对流量与温度的控制。考虑到前期培养基的添加量较大，因此设计了完全分离的顶盖，并且顶盖分为上半盖沿和下半嵌合部分，下半嵌合部分可以与罐体完全密合，既方便前期添加培养液，也利于后期封闭空见发酵培养，保障了安全性与恒定发酵环境。上半部分直径216mm，厚6.38mm，下半部分吻合罐体的倾角，厚8mm。中间通孔为搅拌棒控制孔，通过另一零件的螺旋上升或下降，控制搅拌棒所在高度，从而控制上罐内挡板，影响上罐向下流动的通量，与培养液隔离可以避免搅拌的机械结构影响培养环境，也可以避免大肠杆菌进入中层，直径20mm，设计有螺距6mm的螺纹用于啮合。

上罐罐体总高185mm，圆台部分单高125mm，上径216mm，下径116mm，厚度8mm。a、b、c、d四个管道外径30mm，内径20mm。左右两侧分别为培养基更新口c、出水口a、位置位于中层的富集后样本进出口d和b；中间孔板处可固定滤菌膜，以防止大肠杆菌进入中间部分但允许生成的PET酶通过；罐体中间预留通道用于放置搅拌棒。中层即用于锚定滤菌膜以及连接上下罐。

#### 下罐部分

{% include figure3.html images=page.images03 %}

下罐部分与上罐部分呈对称结构。倒漏斗形的设计可以使整个系统保持稳定，确保垂直方向液体流动正常进行，也可以中间通孔设计螺纹用于啮合上罐管道。下发酵罐由罐体与底板两部分组成，底板利用卡扣式的结构与罐体契合，确保培养液不会溢出，也便于整体培养液的更新与罐体的更换检查。a管道为培养基更新口；为了释放含有鼠李糖脂的溶液，b管道设计有螺距6mm的螺纹用于连接后续灌溉装置。

#### 搅拌棒部分

{% include figure3.html images=page.images05 %}

整体采用上下罐联动搅拌系统，由于上罐培养基更新口持续有培养液通入，我们在入口处设计了一款可单项旋转的搅拌装，下方有挂钩，可直接衔接下罐搅拌板；为防止在小流量时无法完成自驱动，我们额外加入了类似榫卯的结构，保证搅拌板可沿顺时针自由旋转的同时，也可以通过上方连杆逆时针手动转动。

{% include figure.html image="https://static.igem.wiki/teams/5175/resources/hardware/hardware-08.png" alt="" caption="" %}

理想情况下，上罐内培养液经中层待处理样液降温后即适于恶臭假单胞菌培养，对此需要对垂直方向上的液体流量有所控制，我们利用隔板的螺旋上升或下降来控制流量，隔板又受到上方连杆和转轴控制，间接受到温度控制；

{% include figure.html image="https://static.igem.wiki/teams/5175/resources/hardware/hardware-12.png" alt="" caption="" %}

### 设计过程

此部分用以记录我们设计过程中遇到的问题以及改进方法。

#### 发酵罐1.0

{% include figure2.html images=page.images06 %}

首先，我们试图以最直接的想法实现两种菌的共培养。设计了一种内部分为两个部分的罐体，中间以滤菌膜隔开。左侧培养大肠杆菌BL21，其产生的产物透过滤菌膜到右侧，提供给恶臭假单胞菌KT2440生产鼠李糖脂。左侧通道进料，右侧通道出料。装置上侧的两个孔用于温度和pH值的控制。然而，这个设想在现实中遇到了三个问题：1.无法实现菌培养液的搅拌。2.无法给两种菌提供最适的温度条件。3.无法控制反应的速度。

针对这三个问题，我们做出了后续调整。

#### 发酵罐2.0

{% include figure2.html images=page.images07 %}

我们将罐体一分为二，在每个罐中内置了搅拌棒。中间连接管道的部分加入了流量控制器以控制反应速度。大体解决了上述三个问题。但是，需要两个外力驱动搅拌棒转动无疑会造成巨大的能量损耗。由于整个装置是单连通的，想要控制温度必然会造成发酵效率降低。所以，我们做出了如下调整

#### 发酵罐3.0

{% include figure2.html images=page.images08 %}

我们将原来分隔为左右两部分的罐体分隔为了上下两部分，发酵罐3.0已经初具雏形。具备双向流动功能，使得对于发酵液的温度控制更加方便了。但是由于上下罐滤菌膜的隔离，搅拌棒只能控制上罐的搅拌效果，下罐依然没有搅拌功能。

#### Results

{% include figure2.html images=page.images09 %}

我们设计了上罐与下罐连接部分的孔洞，以使得搅拌棒能上下贯通。解决了以上诸多问题，实现了具备温度、pH、流量监测控制，搅拌发酵液实现快速反应等功能的最终硬件产品。

## 模块化

发酵罐采用“积木式”发酵罐的模式，通过模块化的设计提高发酵系统的便携性与环境适应性，可以更具不同的场景与发酵要求使用不同的模块，确保系统适用不同的场景以达到最大环境效益与最高效率。我们设计了一些替换模块，包括：发酵罐模块、搅拌模块、流速控制模块，温度控制模块。模块化的设计也降低了成本，可以随意的更换零件，确保系统可以持续工作与降低建设成本。

### 搅拌模块

### 发酵罐模块

### 控速模块

### 控温模块

### 灌溉模块

恶臭假单胞菌在下罐合成鼠李糖脂后，我们需要将其释放到环境当中以达到我们的增强肥力的效果。因此我们根据不同的应用场景与要求，设计了如下几种灌溉喷头以便使用。

{% include figure.html image="https://static.igem.wiki/teams/5175/resources/hardware/hardware-21.png" alt="" caption="" %}

#### 花洒式

我们从洗澡的花洒获得灵感，设计一个类似于花洒的喷头。利用喷头可以实现更大氛围的浇灌与覆盖，更好的实现我们的增强肥力的效果。我们可以通过控制底部细孔的数量与大小来满足不同的灌溉速度与灌溉范围。

{% include figure.html image="https://static.igem.wiki/teams/5175/resources/hardware/hardware-22.png" alt="" caption="" %}

#### 滴灌式

采用一端封闭，一段内部有螺纹用于与下罐管道啮合，整体为一根长直管道，管道上钻有许多小孔来排除液体。采用滴灌的方式既符合我们的绿色农业的发展需求，也扩大了系统的应有场景。滴灌式喷头制作较为简单，且通过控制整体管道的长度可以实现大范围的滴灌，

{% include figure2.html images=page.images10 %}

以低成本实现了大范围的灌溉。

#### 喷灌式

形状上类似于一个蘑菇，内部有从中心向四周扩散的通道，通道直径从中心到四周从大到小，实现液体的加速，以便扩大灌溉范围。该喷头适用于高水压的情况。













