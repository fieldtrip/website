---
title: Getting started with Seg3D
parent: Other software
grand_parent: Getting started
category: getting_started
tags: [segmentation, volume, headmodel, seg3d]
redirect_from:
    - /getting_started/seg3d/
---

# Getting started with Seg3D

[Seg3D](https://www.sci.utah.edu/cibc-software/seg3d.html) is a free volume segmentation and processing tool that can be used to check and modify segmentation results. It is developed by the NIH Center for Integrative Biomedical Computing at the University of Utah Scientific Computing and Imaging (SCI) Institute and combines a flexible manual segmentation interface with powerful higher-dimensional image processing and segmentation algorithms from the [Insight Toolkit](https://itk.org). You can explore and interact with volumetric imaging data using volume rendering and orthogonal slice view windows and label voxels as a certain tissue class. Seg3D is implemented in C++ and hence very fast, and is available for Windows, macOS, and Linux.

In Seg3D is easy to manually modify a segmentation that was for example created with **[ft_volumesegment](/reference/ft_volumesegment)** and the underlying SPM algorithms.

{% include markup/green %}
Seg3D calls a binary 3D array that represents a single type of tissue a "mask". Seg3D can import and export these masks as .mat files; these should each contain a single binary 3D array. The 4x4 `transform` matrix that is used in FieldTrip to determine the size of the voxels and the origin of the coordinate system is not exported to Seg3D.
{% include markup/end %}

## Example use

You can export data that has been processing in FieldTrip to a format that Seg3D understands, visualize and modify the masks in Seg3D, and import the modified masks back into MATLAB.

    % segment a resliced mri
    cfg           = [];
    cfg.output    = {'gray', 'white', 'csf', 'skull', 'scalp'};
    segmentedmri  = ft_volumesegment(cfg, mri);

    % convert from probabilistic/binary into indexed representation
    segmentedmri_indexed = ft_datatype_segmentation(segmentedmri, 'segmentationstyle', 'indexed');
 
    % visualize the segmentation, different color per tissue type
    cfg              = [];
    cfg.funparameter = 'tissue';
    cfg.funcolormap  = lines(6);                % distinct color per tissue + background
    cfg.atlas        = segmentedmri_indexed;    % this is just like an anatomical atlas, see https://www.fieldtriptoolbox.org/template/atlas/
    cfg.location     = 'center';
    ft_sourceplot(cfg, segmentedmri_indexed);

    % you could also add the anatomy to the segmentation and plot them together in FT_SOURCEPLOT
    % segmentedmri_indexed.anatomy = mri.anatomy

    % make a copy of the anatomy and save it to a file
    anatomy = mri.anatomy
    save anatomy anatomy -v6

    % save the binary masks separately
    gray  = segmentedmri.gray;
    white = segmentedmri.white;
    csf   = segmentedmri.csf;
    skull = segmentedmri.skull;
    scalp = segmentedmri.scalp;

    save gray  gray  -v6
    save white white -v6
    save csf   csf   -v6
    save skull skull -v6
    save scalp scalp -v6
    
    % or save them all together in a single file
    tissue = int8(segmentedmri_indexed.tissue);
    save tissue tissue -v6

After writing the masks to disk, you open Seg3D, read the masks, visualize and modify/correct them where needed. Various operations are possible in Seg3D, for example, editing the segmentation using a paint brush tool like in Microsoft Paint.

{% include image src="/assets/img/getting_started/seg3d/fivemasks.png" width="600" %}

_Figure 1: Five masks visualized in Seg3D and the paint brush tool._

In Seg3D it is also possible to create/visualize and export isosurfaces.

{% include image src="/assets/img/getting_started/seg3d/isosurf.png" width="600" %}

_Figure 2: Visualization of gray matter isosurface created in Seg3D._

You can subsequently export the modified masks as a .mat file and load them again into MATLAB.

    % load the updated mask from Seg3D into FieldTrip/MATLAB
    load('scalp_s3d.mat')
    scalp_edit = logical(scirunnrrd.data);

    % make a copy of the original FieldTrip structure and replace the scalp
    segmentedmri_edit = segmentedmri;
    segmentedmri_edit.scalp = scalp_edit;

    % convert from probabilistic/binary into indexed representation
    segmentedmri_edit_indexed = ft_datatype_segmentation(segmentedmri_edit, 'segmentationstyle', 'indexed');
 
    % visualize the segmentation, different color per tissue type
    cfg              = [];
    cfg.funparameter = 'tissue';
    cfg.funcolormap  = lines(6); % distinct color per tissue + background
    cfg.location     = 'center';
    cfg.atlas        = segmentedmri_edit_indexed;
    ft_sourceplot(cfg, segmentedmri_edit_indexed);
    
{% include markup/red %}
Some operations in Seg3D work the best if the volume consists of isotropic voxels, i.e., the space between the center of any two adjacent voxels is the same along each axis x, y, z. You can make a volume isotropic with **[ft_volumereslice](/reference/ft_volumereslice)**
{% include markup/end %}

## Acknowledgements

Seg3D is an Open Source software project that is principally funded through the SCI Institute's NIH/NIGMS CIBC Center. Please use the following acknowledgment in publications, presentations, or studies that make use of NIH/NIGMS CIBC software or data sets.

"This study was supported by the National Institute of General Medical Sciences of the National Institutes of Health under grant numbers P41 GM103545 and R24 GM136986.”
