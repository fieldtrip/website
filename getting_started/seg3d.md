---
title: How can I use Seg3D to check and modify segmentation results?
tags: [segmentation, volume, headmodel, eeg, seg3d]
---

# How can I use Seg3D to check and modify segmentation results?

[Seg3D](https://www.sci.utah.edu/cibc-software/seg3d.html) is a free volume segmentation and processing tool developed by the NIH Center for Integrative Biomedical Computing at the University of Utah Scientific Computing and Imaging (SCI) Institute. It combines a flexible manual segmentation interface with powerful higher-dimensional image processing and segmentation algorithms from the [Insight Toolkit](https://itk.org). You can explore and interact with volumetric imaging data using volume rendering and orthogonal slice view windows and label voxels as a certain tissue class. Seg3D is implemented in C++ and hence very fast, and is available for Windows, macOS, and Linux. 

In Seg3D is easy to manually modify a segmentation that was for example created with **[ft_volumesegment](/reference/ft_volumesegment)** and the underlying SPM algorithms. 

{% include markup/success %}
Seg3D calls a binary 3D array that represents a single type of tissue a "mask". Seg3D can import and export these masks as .mat files; these should each contain a single binary 3D array. The 4x4 `transform` matrix that is used in FieldTrip to determine the size of the voxels and the origin of the coordinate system is not exported to Seg3D.
{% include markup/end %}

You can export data that has been processing in FieldTrip to a format that Seg3D understands, visualize and modify the masks in Seg3D, and import the modified masks back into MATLAB.

    %% segment a resliced mri
    cfg           = [];
    cfg.output    = {'scalp','skull','csf','gray','white'};
    segm_5c_ft = ft_volumesegment(cfg, mri_resliced); %SPM12

    %% visualize segmentation in ft
    seg_i = ft_datatype_segmentation(segm_5c_ft, 'segmentationstyle', 'indexed');
 
    cfg              = [];
    cfg.funparameter = 'seg';
    cfg.funcolormap  = gray(6); % distinct color per tissue + background
    cfg.location     = 'center';
    cfg.atlas        = seg_i;
    ft_sourceplot(cfg, seg_i);

    %% save the masks separately 
    white_ft = segm_5c_ft.white;
    gray_ft  = segm_5c_ft.gray;
    csf_ft   = segm_5c_ft.csf;
    skull_ft = segm_5c_ft.skull;
    scalp_ft = segm_5c_ft.scalp;

    save white_ft white_ft
    save gray_ft  gray_ft
    save csf_ft   csf_ft
    save skull_ft skull_ft
    save scalp_ft scalp_ft

After writing the masks to disk, you open Seg3D, read the masks and visualize/modify them. Various operations are possible in Seg3D, such as manual modification of the mask with a paint brush tool (like in Microsoft Paint).

{% include image src="/assets/img/getting_started/seg3d/fivemasks.png" width="600" %}

_Figure 1: Five masks visualized in Seg3D and the paint brush tool._

In Seg3D it is also possible to create/visualize and export isosurfaces.

{% include image src="/assets/img/getting_started/seg3d/isosurf.png" width="600" %}

_Figure 2: Visualization of gray matter isosurface created in Seg3D._

You can subsequently export the modified masks as a .mat file and load them again into MATLAB.

    %% load the updated mask into FieldTrip
    load('scalp_s3d.mat')
    scalp_s3d = logical(scirunnrrd.data);

    % make a copy of the original FT structure and replace the scalp
    segm_5c_s3d = segm_5c_ft;
    segm_5c_s3d.scalp = scalp_s3d;

    %% visualize segmentation in ft
    seg_i = ft_datatype_segmentation(segm_5c_s3d, 'segmentationstyle', 'indexed');
 
    cfg              = [];
    cfg.funparameter = 'seg';
    cfg.funcolormap  = gray(6); % distinct color per tissue + background
    cfg.location     = 'center';
    cfg.atlas        = seg_i;
    ft_sourceplot(cfg, seg_i);
    
{% include markup/danger %}
Some operations in Seg3D work the best if the volume consists of isotropic voxels, i.e., the space between the center of any two adjacent voxels is the same along each axis x, y, z. You can make a volume isotropic with **[ft_volumereslice](/reference/ft_volumereslice)**
{% include markup/end %}

## Acknowledgements

Seg3D is an Open Source software project that is principally funded through the SCI Institute's NIH/NIGMS CIBC Center. Please use the following acknowledgment in publications, presentations, or studies that make use of NIH/NIGMS CIBC software or data sets.

"This study was supported by the National Institute of General Medical Sciences of the National Institutes of Health under grant numbers P41 GM103545 and R24 GM136986.”
