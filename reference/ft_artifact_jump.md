---
layout: default
---

##  FT_ARTIFACT_JUMP

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_artifact_jump".

`<html>``<pre>`
    `<a href=/reference/ft_artifact_jump>``<font color=green>`FT_ARTIFACT_JUMP`</font>``</a>` reads the data segments of interest from file and identifies
    SQUID jump artifacts.
 
    Use as
    [cfg, artifact] = ft_artifact_jump(cfg)
    with the configuration options
    cfg.dataset     = string with the filename
    or
    cfg.headerfile  = string with the filename
    cfg.datafile    = string with the filename
    and optionally
    cfg.headerformat
    cfg.dataformat
 
    Alternatively you can use it as
    [cfg, artifact] = ft_artifact_jump(cfg, data)
    where the input data is a structure as obtained from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    In both cases the configuration should also contain
    cfg.trl        = structure that defines the data segments of interest. See `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>`
    cfg.continuous = 'yes' or 'no' whether the file contains continuous data
 
    The data is preprocessed (again) with the following configuration parameters,
    which are optimal for identifying jump artifacts.
    cfg.artfctdef.jump.medianfilter  = 'yes'
    cfg.artfctdef.jump.medianfiltord = 9
    cfg.artfctdef.jump.absdiff       = 'yes'
 
    Artifacts are identified by means of thresholding the z-transformed value
    of the preprocessed data.
    cfg.artfctdef.jump.channel       = Nx1 cell-array with selection of channels, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.artfctdef.jump.cutoff        = z-value at which to threshold (default = 20)
    cfg.artfctdef.jump.trlpadding    = automatically determined based on the filter padding (cfg.padding)
    cfg.artfctdef.jump.artpadding    = automatically determined based on the filter padding (cfg.padding)
 
    The output argument "artifact" is a Nx2 matrix comparable to the
    "trl" matrix of `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>`. The first column of which specifying the
    beginsamples of an artifact period, the second column contains the
    endsamples of the artifactperiods.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    If you specify this option the input data will be read from a *.mat
    file on disk. This mat files should contain only a single variable named 'data',
    corresponding to the input structure.
 
    See also `<a href=/reference/ft_rejectartifact>``<font color=green>`FT_REJECTARTIFACT`</font>``</a>`, `<a href=/reference/ft_artifact_clip>``<font color=green>`FT_ARTIFACT_CLIP`</font>``</a>`, `<a href=/reference/ft_artifact_ecg>``<font color=green>`FT_ARTIFACT_ECG`</font>``</a>`, `<a href=/reference/ft_artifact_eog>``<font color=green>`FT_ARTIFACT_EOG`</font>``</a>`,
    `<a href=/reference/ft_artifact_jump>``<font color=green>`FT_ARTIFACT_JUMP`</font>``</a>`, `<a href=/reference/ft_artifact_muscle>``<font color=green>`FT_ARTIFACT_MUSCLE`</font>``</a>`, `<a href=/reference/ft_artifact_threshold>``<font color=green>`FT_ARTIFACT_THRESHOLD`</font>``</a>`, `<a href=/reference/ft_artifact_zvalue>``<font color=green>`FT_ARTIFACT_ZVALUE`</font>``</a>`
`</pre>``</html>`

