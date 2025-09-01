---
title: Can I compare EEG channels between different electrode caps?
category: faq
tags: [eeg, electrode]
redirect_from:
    - /faq/capmapping/
---

Different EEG caps use different labels and especially different electrode placements. However, sometimes you want to relate electrode positions in one layout to another layout.

Here is a schematic layout of the easycapM10 and easycapM11 electrode caps.

## easycapM10 - Equidistant 61-Channel-Arrangement

{% include image src="/assets/img/faq/capmapping/easycapm10.png" width="200" %}

## easycapM11 - 61-Channel-Arrangement ("10%-System") (used in BrainCap64)

{% include image src="/assets/img/faq/capmapping/easycapm11.png" width="200" %}

We can see that the channel **Cz** from M10 relates to the channel **1** from M11. However for the channel **FT10** there does not exist a relating channel in M11. So we can only make a few-to-few mapping with channels that mostly overlap.

Mapping between easycapM10 and easycapM11:

- 1 - Cz
- 2 - FCz
- 5 - CPz
- 8 - Fz
- 11 - C4
- 14 - Pz
- 17 - C3
- 20 - AFz
- 35 - Fpz
- 39 - T8
- 43 - Oz
- 47 - T7
- 50 - Fp1
