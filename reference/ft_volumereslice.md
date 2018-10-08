---
layout: default
---

##  FT_VOLUMERESLICE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_volumereslice".

`<html>``<pre>`
    `<a href=/reference/ft_volumereslice>``<font color=green>`FT_VOLUMERESLICE`</font>``</a>` flips, permutes, interpolates and reslices a volume along the
    principal axes of the coordinate system according to a specified resolution.
 
    Use as
    mri = ft_volumereslice(cfg, mri)
    where the input MRI should be a single anatomical or functional MRI volume that
    results from `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>` or `<a href=/reference/ft_volumerealign>``<font color=green>`FT_VOLUMEREALIGN`</font>``</a>`. You can visualize the the input and
    output using `<a href=/reference/ft_sourceplot>``<font color=green>`FT_SOURCEPLOT`</font>``</a>`.
 
    The configuration structure can contain
    cfg.method     = string, 'flip', 'nearest', 'linear', 'cubic' or 'spline' (default = 'linear')
    cfg.downsample = integer number (default = 1, i.e. no downsampling)
 
    If you specify the method as 'flip', it will only permute and flip the volume, but
    not perform any interpolation. For the other methods the input volumetric data will
    also be interpolated on a regular voxel grid.
 
    For the interpolation methods you should specify
    cfg.resolution = number, in physical units
    cfg.xrange     = [min max], in physical units
    cfg.yrange     = [min max], in physical units
    cfg.zrange     = [min max], in physical units
    or alternatively with
    cfg.dim        = [nx ny nz], size of the volume in each direction
 
    If the input MRI has a coordsys-field and you don't specify explicit the
    xrange/yrange/zrange, the centre of the volume will be shifted (with respect to the
    origin of the coordinate system), for the brain to fit nicely in the box.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_volumerealign>``<font color=green>`FT_VOLUMEREALIGN`</font>``</a>`, `<a href=/reference/ft_volumedownsample>``<font color=green>`FT_VOLUMEDOWNSAMPLE`</font>``</a>`, `<a href=/reference/ft_sourceinterpolate>``<font color=green>`FT_SOURCEINTERPOLATE`</font>``</a>`, `<a href=/reference/ft_sourceplot>``<font color=green>`FT_SOURCEPLOT`</font>``</a>`
`</pre>``</html>`

