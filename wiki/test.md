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
  - src: https://static.igem.wiki/teams/5175/test-resources/test-pic-left.jpeg
    alt: Yunli
    caption: Yunli
  - src: https://static.igem.wiki/teams/5175/test-resources/test-pic-middle.jpeg
    alt: High-Cloud Quintet
    caption: High-Cloud Quintet
  - src: https://static.igem.wiki/teams/5175/test-resources/test-pic-right.jpeg
    alt: March 7th
    caption: March 7th

images02:
  - src: https://static.igem.wiki/teams/5175/test-resources/test-pic-left.jpeg
    alt: Yunli
    caption: Yunli
  - src: https://static.igem.wiki/teams/5175/test-resources/test-pic-right.jpeg
    alt: March 7th
    caption: March 7th
---

> **Warning:** This is a test page. Please ignore it.

## Pictures embedded in the page

### Single

{% include figure.html image="https://static.igem.wiki/teams/5175/test-resources/test-pic-center.jpeg" alt="March 7th" caption="March 7th" %}

{% include figure.html image="https://static.igem.wiki/teams/5175/test-resources/test-pic-center.jpeg" alt="March 7th" caption="March 7th" %}

### Multiple

#### Left, Middle, Right

{% include figure3.html images=page.images01 %}

#### Left, Right

{% include figure2.html images=page.images02 %}

## Buttons

{% include button.html link="../" text="Go back to Home Page" %}

{% include button.html link="../resources/" text="Go to Resources Page" %}

## MathJax

### Inline Math

The formula $E=mc^2$ is well-known.

### Pseudo-Block Math

<center>$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$</center>

## Table

<div class="table-container">

<figcaption class="caption">Test table</figcaption>

<table>
    <thead>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
            <th>Header 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Cell 1</td>
            <td>Cell 2</td>
            <td>Cell 3</td>
        </tr>
        <tr>
            <td>Cell 4</td>
            <td>Cell 5</td>
            <td>Cell 6</td>
        </tr>
    </tbody>
</table>

</div>
