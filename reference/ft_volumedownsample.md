---
layout: default
---

##  FT_VOLUMEDOWNSAMPLE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_volumedownsample".

`<html>``<pre>`
    `<a href=/reference/ft_volumedownsample>``<font color=green>`FT_VOLUMEDOWNSAMPLE`</font>``</a>` downsamples an anatomical MRI or source reconstruction
    and optionally normalizes its coordinate axes, keeping the homogenous
    transformation matrix correct.
 
    Use as
    [volume] = ft_volumedownsample(cfg, mri)
    where the input mri should be a single anatomical volume that was
    for example read with `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>` or should be a volumetric source
    reconstruction resulting from `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>` or `<a href=/reference/ft_sourceinterpolate>``<font color=green>`FT_SOURCEINTERPOLATE`</font>``</a>`.
 
    The configuration can contain
    cfg.downsample = integer number (default = 1, i.e. no downsampling)
    cfg.parameter  = string, data field to downsample (default = 'all')
    cfg.smooth     = 'no' or the FWHM of the gaussian kernel in voxels (default = 'no')
    cfg.keepinside = 'yes' or 'no', keep the inside/outside labeling (default = 'yes')
    cfg.spmversion = string, 'spm2', 'spm8', 'spm12' (default = 'spm8')
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_sourceinterpolate>``<font color=green>`FT_SOURCEINTERPOLATE`</font>``</a>`, `<a href=/reference/ft_volumewrite>``<font color=green>`FT_VOLUMEWRITE`</font>``</a>` and `<a href=/reference/ft_volumenormalise>``<font color=green>`FT_VOLUMENORMALISE`</font>``</a>`
`</pre>``</html>`

