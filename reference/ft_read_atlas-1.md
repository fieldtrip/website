---
title: ft_read_atlas
---
```
 FT_READ_ATLAS reads an template/individual segmentation or parcellation from disk.
 The volumetric segmentation or the surface-based parcellation can either represent
 a template atlas (eg. AAL or the Talairach Daemon), it can represent an
 individualized atlas (e.g. obtained from FreeSurfer) or it can represent an
 unlabeled parcellation obtained from the individual's DTi or resting state fMRI.

 Use as
   atlas = ft_read_atlas(filename, ...)
 or
   atlas = ft_read_atlas({filenamelabels, filenamemesh}, ...)

 Additional options should be specified in key-value pairs and can include
   'format'      = string, see below
   'unit'        = string, e.g. 'mm' (default is to keep it in the native units of the file)

 For individual surface-based atlases from FreeSurfer you should specify two
 filenames as a cell-array: the first points to the file that contains information
 with respect to the parcels' labels, the second points to the file that defines the
 mesh on which the parcellation is defined.

 The output atlas will be represented as structure according to
 FT_DATATYPE_SEGMENTATION or FT_DATATYPE_PARCELLATION.

 The "lines" and the "colorcube" colormaps are useful for plotting the different
 patches, for example using FT_PLOT_MESH.

 See also FT_READ_MRI, FT_READ_HEADSHAPE, FT_PREPARE_SOURCEMODEL, FT_SOURCEPARCELLATE, FT_PLOT_MESH
```
