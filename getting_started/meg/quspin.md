---
title: Getting started with QuSpin OPM data
tags: [dataformat, meg, opm, quspin]
category: getting_started
redirect_from:
    - /getting_started/quspin/
---

[QuSpin](https://quspin.com) is based in Louisville, Colorado, USA, and develops miniature, optically-pumped magnetometer (OPM) sensors for functional brain imaging and other applications. The QuSpin magnetometer sensors are used in their own MEG systems, but also in the MEG systems from [Cerca Magnetics](/getting_started/meg/cerca). Here we will be discussing only the QuSpin MEG system itself.

## File formats

The QuSpin acquisition software records the raw data in the `.lvm` format, which can be converted into the `.fif` format for further processing.

## Coregistration

QuSpin uses a semi-flexible cap or helmet that consists of multiple panels. To record the position and orientation of the sensors relative to each other, and to coregister the sensors with the head of the participant, QuSpin uses the [HALO](https://doi.org/10.1162/imag_a_00535), a circular printed circuit board (PCB) containing 16 independently controllable electromagnetic coils, which is mounted above the head like an aureola.
