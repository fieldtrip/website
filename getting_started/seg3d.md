---
title: How can I use Seg3D to check and modify segmentation results?
tags: [segmentation, seg3d, volume]
---

# How can I use Seg3D to check and modify segmentation results?

[Seg3D](https://www.sci.utah.edu/cibc-software/seg3d.html) Seg3D is a free volume segmentation and processing tool developed by the NIH Center for Integrative Biomedical Computing at the University of Utah Scientific Computing and Imaging (SCI) Institute. Seg3D combines a flexible manual segmentation interface with powerful higher-dimensional image processing and segmentation algorithms from the Insight Toolkit. Users can explore and label image volumes using volume rendering and orthogonal slice view windows. It is implemented in C++ and available for Windows, OSX, and Linux. 

In Seg3D is easy to (manually) modify a segmentation, for example, with **[ft_volumesegment](https://www.fieldtriptoolbox.org/reference/ft_volumesegment/)**. In Seg3D, a binary 3D matrix representing one segmented compartment is called mask.

{% include markup/warning %}
Seg3D can import and export masks, i.e., binary 3D matrices representing singular segmented compartments, as .mat files.
{% include markup/end %}

You can export data that has been processing in FieldTrip to a format that Seg3D understands, i.e., logical 3D matrices in .mat format representing one segmentation compartment, visualize and modify the masks in Seg3D, and import the modified masks back into MATLAB.

    %% segment a resliced mri
    cfg           = [];
    cfg.output    = {'scalp','skull','csf','gray','white'};
    segm_5c_ft = ft_volumesegment(cfg, mri_resliced); %SPM12

    %% visualize segmentation in ft
    seg_i = ft_datatype_segmentation(segm_5c_ft,'segmentationstyle','indexed');
 
    cfg              = [];
    cfg.funparameter = 'seg';
    cfg.funcolormap  = gray(6); % distinct color per tissue + background
    cfg.location     = 'center';
    cfg.atlas        = seg_i;
    ft_sourceplot(cfg, seg_i);

    %%
    save segm_5c_ft segm_5c_ft
    
    %% save masks separately 
    white_ft = segm_5c_ft.white;
    gray_ft  = segm_5c_ft.gray;
    csf_ft   = segm_5c_ft.csf;
    skull_ft = segm_5c_ft.skull;
    scalp_ft = segm_5c_ft.scalp;

    save white_ft white_ft
    save gray_ft gray_ft
    save csf_ft csf_ft
    save skull_ft skull_ft
    save scalp_ft scalp_ft

After writing the masks to disk, you open Seg3D,  read the masks and visualize/modify them. Various operations are possible in Seg3D, such as manual modification of the mask with a paint brush tool (like in Microsoft Paint).

{% include image src="/assets/img/getting_started/seg3d/fivemasks.png" width="600" %}

_Figure 1: Five masks visualized in Seg3D and the paint brush tool._

In Seg3D it is also possible to create/visualize and export isosurfaces.

{% include image src="/assets/img/getting_started/seg3d/isosurf.png" width="600" %}

_Figure 2: Visualization of gray matter isosurface created in Seg3D._

You can subsequently export the modified masks as a .mat file and load it again in MATLAB.


    %% load the new mask(s) in ft 
    load('scalp_s3d.mat')
    scalp_s3d = logical(scirunnrrd.data);

    segm_5c_s3d = segm_5c_ft;
    segm_5c_s3d.scalp = scalp_s3d;

    %% visualize segmentation in ft
    seg_i = ft_datatype_segmentation(segm_5c_s3d,'segmentationstyle','indexed');
 
    cfg              = [];
    cfg.funparameter = 'seg';
    cfg.funcolormap  = gray(6); % distinct color per tissue + background
    cfg.location     = 'center';
    cfg.atlas        = seg_i;
    ft_sourceplot(cfg, seg_i);
    
{% include markup/danger %}
Some operations in Seg3D work best if the volume has isotropic voxel spacing, i.e., the space between any two adjacent voxels is the same along each axis x, y, z. A volume can be made isotropic, for example, with **[ft_volumereslice](https://www.fieldtriptoolbox.org/reference/ft_volumereslice/)**
{% include markup/end %}
    
    
Seg3D is an Open Source software project that is principally funded through the SCI Institute's NIH/NIGMS CIBC Center (National Institute of General Medical Sciences of the National Institutes of Health under grant numbers P41 GM103545 and R24 GM136986).

