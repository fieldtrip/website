---
title: What are the different Neuromag/Elekta/Megin and Yokogawa layouts good for?
tags: [layout, plotting]
category: faq
redirect_from:
    - /faq/what_are_the_different_neuromag_and_yokogawa_layouts_good_for/
    - /faq/layout_magandgrad/
---

The Neuromag/Elekta/Megin and some Yokogawa MEG systems use a combination of two different kind of sensors within one system: (planar) gradiometers and magnetometers. Gradiometer consists of two coils, and the data recorded of such a pair reflects the gradient of the magnetic field, measured in Tesla per distance unit. In contrast, magnetometers measure the magnetic field using one coil only, resulting in a measure in Tesla. Since the two type of sensors measure in different units, data obtained from these two types of sensor cannot be easily compared directly. Therefore FieldTrip features layouts for gradiometer and magnetometer sensor positions separately, so that the user can visualize either the magnetometer data or the gradiometer data.

For more information, please consult the manual of the MEG system of your choice or see [Hämäläinen, Hari, Ilmoniemi, Knuutila, Lounasmaa (1993) Magnetoencephalography—theory, instrumentation, and applications to noninvasive studies of the working human brain. Rev. Mod. Phys. 65 (2), 413-497](http://rmp.aps.org/abstract/RMP/v65/i2/p413_1)
