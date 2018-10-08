---
layout: default
---

##  FT_REMOVETEMPLATEARTIFACT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_removetemplateartifact".

`<html>``<pre>`
    `<a href=/reference/ft_removetemplateartifact>``<font color=green>`FT_REMOVETEMPLATEARTIFACT`</font>``</a>` removes an artifact from preprocessed data by template
    subtraction. The template can for example be formed by averaging an ECG-triggered
    MEG timecourse.
 
    Use as
    dataclean = ft_removetemplateartifact(cfg, data, template)
    where data is raw data as obtained from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>` and template is a averaged
    timelock structure as obtained from `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`. The configuration should
    be according to
 
    cfg.channel  = Nx1 cell-array with selection of channels (default = 'all'), see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.artifact = Mx2 matrix with sample numbers of the artifact segments, e.g. obtained from `<a href=/reference/ft_artifact_eog>``<font color=green>`FT_ARTIFACT_EOG`</font>``</a>`
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_artifact_ecg>``<font color=green>`FT_ARTIFACT_ECG`</font>``</a>`, `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`, `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`, `<a href=/reference/ft_rejectcomponent>``<font color=green>`FT_REJECTCOMPONENT`</font>``</a>`
`</pre>``</html>`

