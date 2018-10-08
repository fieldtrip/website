---
layout: default
---

##  FT_SOURCEPARCELLATE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_sourceparcellate".

`<html>``<pre>`
    `<a href=/reference/ft_sourceparcellate>``<font color=green>`FT_SOURCEPARCELLATE`</font>``</a>` combines the source-reconstruction parameters over the parcels, for
    example by averaging all the values in the anatomically or functionally labeled parcel.
 
    Use as
     output = ft_sourceparcellate(cfg, source, parcellation)
    where the input source is a 2D surface-based or 3-D voxel-based source grid that was for
    example obtained from `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>` or `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`. The input parcellation is
    described in detail in `<a href=/reference/ft_datatype_parcellation>``<font color=green>`FT_DATATYPE_PARCELLATION`</font>``</a>` (2-D) or `<a href=/reference/ft_datatype_segmentation>``<font color=green>`FT_DATATYPE_SEGMENTATION`</font>``</a>` (3-D) and
    can be obtained from `<a href=/reference/ft_read_atlas>``<font color=green>`FT_READ_ATLAS`</font>``</a>` or from a custom parcellation/segmentation for your
    individual subject. The output is a channel-based representation with the combined (e.g.
    averaged) representation of the source parameters per parcel.
 
    The configuration "cfg" is a structure that can contain the following fields
    cfg.method       = string, method to combine the values, see below (default = 'mean')
    cfg.parcellation = string, fieldname that contains the desired parcellation
    cfg.parameter    = cell-array with strings, fields that should be parcellated (default = 'all')
 
    The values within a parcel or parcel-combination can be combined with different method
    'mean'      compute the mean
    'median'    compute the median (unsupported for fields that are represented in a cell-array)
    'eig'       compute the largest eigenvector
    'min'       take the minimal value
    'max'       take the maximal value
    'maxabs'    take the signed maxabs value
 
    See also `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, `<a href=/reference/ft_datatype_parcellation>``<font color=green>`FT_DATATYPE_PARCELLATION`</font>``</a>`, `<a href=/reference/ft_datatype_segmentation>``<font color=green>`FT_DATATYPE_SEGMENTATION`</font>``</a>`
`</pre>``</html>`

