---
layout: default
---

##  FT_READ_ATLAS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_read_atlas".

`<html>``<pre>`
    `<a href=/reference/ft_read_atlas>``<font color=green>`FT_READ_ATLAS`</font>``</a>` reads an template/individual segmentation or parcellation from disk.
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
    `<a href=/reference/ft_datatype_segmentation>``<font color=green>`FT_DATATYPE_SEGMENTATION`</font>``</a>` or `<a href=/reference/ft_datatype_parcellation>``<font color=green>`FT_DATATYPE_PARCELLATION`</font>``</a>`.
 
    The "lines" and the "colorcube" colormaps are useful for plotting the different
    patches, for example using `<a href=/reference/ft_plot_mesh>``<font color=green>`FT_PLOT_MESH`</font>``</a>`.
 
    See also `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>`, `<a href=/reference/ft_read_headshape>``<font color=green>`FT_READ_HEADSHAPE`</font>``</a>`, `<a href=/reference/ft_prepare_sourcemodel>``<font color=green>`FT_PREPARE_SOURCEMODEL`</font>``</a>`, `<a href=/reference/ft_sourceparcellate>``<font color=green>`FT_SOURCEPARCELLATE`</font>``</a>`, `<a href=/reference/ft_plot_mesh>``<font color=green>`FT_PLOT_MESH`</font>``</a>`
`</pre>``</html>`

