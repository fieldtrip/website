---
title: Why is there a rim around the brain for which the source reconstruction is not computed?
layout: default
tags: [faq, source]
---

##  Why is there a rim around the brain for which the source reconstruction is not computed? 

The sourceanalysis function starts by determining a regular 3-D grid, and for each gridpoint it determines whether it falls within the brain compartment of the volume conduction model or not. Grid points that are inside the brain are marked as "inside", points outside the brain are marked as "outside". The subsequent source reconstruction is only computed on the grid points that are inside the brain.

Depending on the resolution of your 3-D grid, there will be points in the grid that *just* ly outside the brain, i.e. close to those points there will be no points inside the brain that are included in the source reconstruction (see figure below). This results in a rim around the brain in which the source reconstruction is not performed, and hence no functional source data will be displayed in that rim after interpolating the source data onto the anatomical MRI.

![image](/media/faq/grid_resolution_high.png)

If you have a low grid resolution, the rim will apear to be wider (see figure below). 

![image](/media/faq/grid_resolution_low.png)

In the figures, the brain is indicated with the circle, the "inside" points are indicated with red dots and the yellow region indicates that part of the brain volume on which the functional data will be interpolated.

`<note>`
In **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)** you can give a **negative** value for cfg.inwardshift to compensate for this rim. 

Note that this is only valid if you are working with MEG data and if you are using a singlesphere, localspheres or singleshell volume conduction model. You should **not** do this when you are working with EEG data, nor if you are using a BEM or FEM volume conduction models.
</div>

