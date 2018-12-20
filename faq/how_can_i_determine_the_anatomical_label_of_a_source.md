---
title: How can I determine the anatomical label of a source?
tags: [faq, source]
---

# How can I determine the anatomical label of a source?

FieldTrip supports the use of an anatomical atlas to look up the anatomical label of a source that you have localized. Vice versa you can also first look up the location of an anatomical region and subsequently use that in source analysis, e.g. as region of interest for beamforming or as starting point for dipole fitting.

The function **[ft_load_atlas](/reference/ft_load_atlas)** reads in a specified atlas with coordinates and anatomical labels. It either uses the [AFNI brik file](http://afni.nimh.nih.gov/afni/doc/misc/afni_ttatlas/), or it uses one of the [WFU atlases](http://fmri.wfubmc.edu). The following example code shows a simple demonstration:

    atlas = ft_read_atlas('ROI_MNI_V4.nii');

    cfg              = [];
    cfg.method       = 'ortho';
    cfg.funparameter = 'brick0';
    cfg.funcolormap  = 'jet';
    ft_sourceplot(cfg, atlas)

Atlases can be used in several FieldTrip functions. For instance in the **[ft_sourceplot](/reference/ft_sourceplot)** function if you specify cfg.atlas and cfg.atlascoordinates you can click on a voxel in the interactive mode (cfg.method = ‘ortho’) and the label of that voxel according to the specified atlas is given.

The most important function for using an atlas is **[ft_volumelookup](/reference/ft_volumelookup)**. It can be used in two approaches.

 1.  Given the anatomical or functional label, it looks up the locations and creates a mask (as a binary volume) based on the label, or creates a sphere or box around a point of interest.
 2.  Given a binary volume that indicates a region of interest, it looks up the corresponding anatomical or functional labels from a given atlas.
