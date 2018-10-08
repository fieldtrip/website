---
layout: default
---

##  FT_ARTIFACT_ECG

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_artifact_ecg".

`<html>``<pre>`
    `<a href=/reference/ft_artifact_ecg>``<font color=green>`FT_ARTIFACT_ECG`</font>``</a>` performs a peak-detection on the ECG-channel and identifies the windows
    around the QRS peak as artifacts. Using `<a href=/reference/ft_rejectartifact>``<font color=green>`FT_REJECTARTIFACT`</font>``</a>` you can remove these windows from
    your data, or using `<a href=/reference/ft_removetemplateartifact>``<font color=green>`FT_REMOVETEMPLATEARTIFACT`</font>``</a>` you can subtract an averaged template artifact
    from your data.
 
    Use as
    [cfg, artifact] = ft_artifact_ecg(cfg)
    with the configuration options
    cfg.dataset     = string with the filename
    or
    cfg.headerfile  = string with the filename
    cfg.datafile    = string with the filename
    and optionally
    cfg.headerformat
    cfg.dataformat
 
    Alternatively you can use it as
    [cfg, artifact] = ft_artifact_ecg(cfg, data)
    where the input data is a structure as obtained from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    In both cases the configuration should also contain
    cfg.trl        = structure that defines the data segments of interest. See `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>`
    cfg.continuous = 'yes' or 'no' whether the file contains continuous data
    and
    cfg.artfctdef.ecg.channel = Nx1 cell-array with selection of channels, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.artfctdef.ecg.pretim  = 0.05; pre-artifact rejection-interval in seconds
    cfg.artfctdef.ecg.psttim  = 0.3;  post-artifact rejection-interval in seconds
    cfg.artfctdef.ecg.method  = 'zvalue'; peak-detection method
    cfg.artfctdef.ecg.cutoff  = 3; peak-threshold
    cfg.artfctdef.ecg.inspect = Nx1 list of channels which will be shown in a QRS-locked average
 
    The output argument "artifact" is a Nx2 matrix comparable to the
    "trl" matrix of `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>`. The first column of which specifying the
    beginsamples of an artifact period, the second column contains the
    endsamples of the artifactperiods.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    If you specify this option the input data will be read from a *.mat
    file on disk. This mat files should contain only a single variable named 'data',
    corresponding to the input structure.
 
    See also `<a href=/reference/ft_rejectartifact>``<font color=green>`FT_REJECTARTIFACT`</font>``</a>`, `<a href=/reference/ft_removetemplateartifact>``<font color=green>`FT_REMOVETEMPLATEARTIFACT`</font>``</a>`, `<a href=/reference/ft_artifact_clip>``<font color=green>`FT_ARTIFACT_CLIP`</font>``</a>`, `<a href=/reference/ft_artifact_ecg>``<font color=green>`FT_ARTIFACT_ECG`</font>``</a>`,
    `<a href=/reference/ft_artifact_eog>``<font color=green>`FT_ARTIFACT_EOG`</font>``</a>`, `<a href=/reference/ft_artifact_jump>``<font color=green>`FT_ARTIFACT_JUMP`</font>``</a>`, `<a href=/reference/ft_artifact_muscle>``<font color=green>`FT_ARTIFACT_MUSCLE`</font>``</a>`, `<a href=/reference/ft_artifact_threshold>``<font color=green>`FT_ARTIFACT_THRESHOLD`</font>``</a>`,
    `<a href=/reference/ft_artifact_zvalue>``<font color=green>`FT_ARTIFACT_ZVALUE`</font>``</a>`
`</pre>``</html>`

