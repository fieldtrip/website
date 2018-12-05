---
title: ft_prepare_layout
tags: 
---
```
 FT_PREPARE_LAYOUT loads or creates a 2-D layout of the channel locations. This
 layout is required for plotting the topographical distribution of the potential or
 field distribution, or for plotting timecourses in a topographical arrangement.

 Use as
   layout = ft_prepare_layout(cfg, data)

 There are several ways in which a 2-D layout can be made: 1) it can be read
 directly from a layout file, 2) it can be created on basis of an image or photo, 3)
 it can be created based on 3-D sensor positions in the configuration, in the data,
 or in an electrode or gradiometer file.

 Layout files are MATLAB files with a single variable representing the layout (see
 below). The layout file can also be an ASCII *.lay file, but this type of layout is
 no longer recommended, since the outline of the head and the mask within which the
 interpolation is done is less refined for an ASCII layout. A large number of
 template layout files is provided in the fieldtrip/template/layout directory. See
 also http://fieldtriptoolbox.org/template/layout

 You can specify any one of the following configuration options
   cfg.layout      = filename containg the input layout (*.mat or *.lay file), this can also be a layout
                     structure, which is simply returned as-is (see below for details)
   cfg.output      = filename (ending in .mat or .lay) to which the layout will be written (default = [])
   cfg.elec        = structure with electrode definition, or
   cfg.elecfile    = filename containing electrode definition
   cfg.grad        = structure with gradiometer definition, or
   cfg.gradfile    = filename containing gradiometer definition
   cfg.opto        = structure with optode structure definition, or
   cfg.optofile    = filename containing optode structure definition
   cfg.rotate      = number, rotation around the z-axis in degrees (default = [], which means automatic)
   cfg.projection  = string, 2D projection method can be 'stereographic', 'orthographic', 'polar' or 'gnomic' (default = 'polar')
                     When 'orthographic', cfg.viewpoint can be used to indicate to specificy projection (keep empty for legacy projection)
   cfg.viewpoint   = string indicating the view point that is used for orthographic projection of 3-D sensor
                     positions to the 2-D plane. The possible viewpoints are
                     'left'      - left  sagittal view,    L=anterior, R=posterior, top=top, bottom=bottom
                     'right'     - right sagittal view,    L=posterior, R=anterior, top=top, bottom=bottom
                     'inferior'  - inferior axial view,    L=R, R=L, top=anterior, bottom=posterior
                     'superior'  - superior axial view,    L=L, R=R, top=anterior, bottom=posterior
                     'anterior'  - anterior  coronal view, L=R, R=L, top=top, bottom=bottom
                     'posterior' - posterior coronal view, L=L, R=R, top=top, bottom=bottom
                     'auto'      - automatic guess of the most optimal of the above
                      tip: use cfg.viewpoint = 'auto' per iEEG electrode grid/strip/depth for more accurate results
                      tip: to obtain an overview of all iEEG electrodes, choose superior/inferior, use cfg.headshape/mri, and plot using FT_LAYOUTPLOT with cfg.box/mask = 'no'
   cfg.outline     = string, how to create the outline, can be 'circle', 'convex', 'headshape', 'mri' or 'no' (default is automatic)
   cfg.mask        = string, how to create the mask, can be 'circle', 'convex', 'headshape', 'mri' or 'no' (default is automatic)
   cfg.headshape   = surface mesh (e.g. pial, head, etc) to be used for generating an outline, see FT_READ_HEADSHAPE for details
   cfg.mri         = segmented anatomical MRI to be used for generating an outline, see FT_READ_MRI and FT_VOLUMESEGMENT for details
   cfg.montage     = 'no' or a montage structure (default = 'no')
   cfg.image       = filename, use an image to construct a layout (e.g. useful for ECoG grids)
   cfg.bw          = 'yes' or 'no', if an image is used and this option is true, the image is transformed in black and white (default = 'no', i.e. do not transform)
   cfg.overlap     = string, how to deal with overlapping channels when the layout is constructed from a sensor configuration structure. This can be
                     'shift'  - shift the positions in 2D space to remove the overlap (default)
                     'keep'   - do not shift, retain the overlap
                     'no'     - throw an error when overlap is present
   cfg.channel     = 'all', or Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details
   cfg.boxchannel  = 'all', or Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details
                      specificies channels to use for determining channel box size (default = 'all', recommended for MEG/EEG, a selection is recommended for iEEG)
   cfg.skipscale   = 'yes' or 'no', whether the scale should be included in the layout or not (default = 'no')
   cfg.skipcomnt   = 'yes' or 'no', whether the comment should be included in the layout or not (default = 'no')

 If you use cfg.headshape or cfg.mri to create a headshape outline, the input
 geometry should be expressed in the same units and coordinate system as the input
 sensors.

 Alternatively the layout can be constructed from either one of these in the input data structure:
   data.elec     = structure with electrode positions
   data.grad     = structure with gradiometer definition
   data.opto     = structure with optode structure definition

 Alternatively you can specify the following systematic layouts which will be
 generated for all channels present in the data. Note that these layouts are only
 suitable for multiplotting, not for topoplotting.
   cfg.layout = 'ordered'    will give you a NxN ordered layout
   cfg.layout = 'vertical'   will give you a Nx1 ordered layout
   cfg.layout = 'horizontal' will give you a 1xN ordered layout
   cfg.layout = 'butterfly'  will give you a layout with all channels on top of each other
   cfg.layout = 'circular'   will distribute the channels on a circle

 The output layout structure will contain the following fields
   layout.label   = Nx1 cell-array with channel labels
   layout.pos     = Nx2 matrix with channel positions
   layout.width   = Nx1 vector with the width of each box for multiplotting
   layout.height  = Nx1 matrix with the height of each box for multiplotting
   layout.mask    = optional cell-array with line segments that determine the area for topographic interpolation
   layout.outline = optional cell-array with line segments that represent the head, nose, ears, sulci or other anatomical features

 See also FT_TOPOPLOTER, FT_TOPOPLOTTFR, FT_MULTIPLOTER, FT_MULTIPLOTTFR, FT_PLOT_LAY
```
