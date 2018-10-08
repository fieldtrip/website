---
layout: default
---

##  FT_ARTIFACT_CLIP

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_artifact_clip".

`<html>``<pre>`
    `<a href=/reference/ft_artifact_clip>``<font color=green>`FT_ARTIFACT_CLIP`</font>``</a>` scans the data segments of interest for channels that
    clip. A clipping artifact is detected by the signal being completely
    flat for some time.
 
    Use as
    [cfg, artifact] = ft_artifact_clip(cfg)
    with the configuration options
    cfg.dataset     = string with the filename
    or
    cfg.headerfile  = string with the filename
    cfg.datafile    = string with the filename
 
    Alternatively you can use it as
    [cfg, artifact] = ft_artifact_clip(cfg, data)
    where the input data is a structure as obtained from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    In both cases the configuration should also contain
    cfg.artfctdef.clip.channel       = Nx1 cell-array with selection of channels, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.artfctdef.clip.pretim        = 0.000;  pre-artifact rejection-interval in seconds
    cfg.artfctdef.clip.psttim        = 0.000;  post-artifact rejection-interval in seconds
    cfg.artfctdef.clip.timethreshold = number, minimum duration in seconds of a datasegment with consecutive identical samples to be considered as 'clipped'
    cfg.artfctdef.clip.amplthreshold = number, minimum amplitude difference in consecutive samples to be considered as 'clipped' (default = 0)
                                       string, percent of the amplitude range considered as 'clipped' (i.e. '1%')
    cfg.continuous                   = 'yes' or 'no' whether the file contains continuous data
 
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

