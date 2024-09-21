---
title: Test Page
feature_text: |
  ## Test Page
  Welcome to iGEM HUST-China 2024 wiki! It's still under construction. Please stay tuned for more information.
feature_image: "https://static.igem.wiki/teams/5175/test-resources/test-image-1300x400.jpg"
excerpt: "Welcome to iGEM HUST-China 2024 wiki! It's still under construction. Please stay tuned for more information."
permalink: /test/

# Multiple Figures
images01:
  - image: https://static.igem.wiki/teams/5175/test-resources/test-pic-left.jpeg
    alt: Yunli
    caption: Yunli
  - image: https://static.igem.wiki/teams/5175/test-resources/test-pic-center.jpeg
    alt: March 7th
    caption: March 7th
  - image: https://static.igem.wiki/teams/5175/test-resources/test-pic-right.jpeg
    alt: March 7th - 2
    caption: March 7th - 2

images02:
  - image: https://static.igem.wiki/teams/5175/test-resources/test-pic-left.jpeg
    alt: Yunli
    caption: Yunli
  - image: https://static.igem.wiki/teams/5175/test-resources/test-pic-center.jpeg
    alt: March 7th
    caption: March 7th
---

> **Warning:** This is a test page. Please ignore it.

## Pictures embedded in the page

### Single

{% include figure.html image="https://static.igem.wiki/teams/5175/test-resources/test-pic-center.jpeg" alt="March 7th" caption="March 7th" width="300" height="800" %}

### Multiple

{% include figure_multiple.html images=page.images01 %}

{% include figure_multiple.html images=page.images02 %}
