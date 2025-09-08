---
title: Why is there a rim around the brain for which the source reconstruction is not computed?
tags: [source]
category: faq
redirect_from:
    - /faq/why_is_there_a_rim_around_the_brain_for_which_the_source_reconstruction_is_not_computed/
    - /faq/sourcerecon_rim/
---

The **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)** function starts by determining a regular 3-D grid, and for each grid point it determines whether it falls within the brain compartment of the volume conduction model or not. Grid points that are inside the brain are marked as "inside", points outside the brain are marked as "outside". All subsequent source estimates are only computed on the grid points that are inside the brain.

Depending on the resolution of your 3-D grid, there will be points in the grid that _just_ ly outside the brain, i.e. close to those points there will be no points inside the brain that are included in the source reconstruction (see figure below). This results in a rim around the brain in which the source reconstruction is not performed, and hence no functional source data will be displayed in that rim after interpolating the source data onto the anatomical MRI.

{% include image src="/assets/img/faq/sourcerecon_rim/grid_resolution_high.png" %}

If you have a low grid resolution, the rim will appear to be wider (see figure below).

{% include image src="/assets/img/faq/sourcerecon_rim/grid_resolution_low.png" %}

In the figures, the brain is indicated with the circle, the "inside" points are indicated with red dots and the yellow region indicates that part of the brain volume on which the functional data will be interpolated.

{% include markup/skyblue %}
When you are working with MEG data and if you are using a singlesphere, localspheres or singleshell volume conduction model, you can give a **negative** value for `cfg.inwardshift` in **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)** to compensate for this rim

You should **not** do this when you are working with EEG data, nor if you are using a BEM or FEM volume conduction models.
{% include markup/end %}
