---
layout: default
---

##  FT_TIMELOCKANALYSIS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_timelockanalysis".

`<html>``<pre>`
    `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>` computes the timelocked average ERP/ERF and
    computes the covariance matrix
 
    Use as
    [timelock] = ft_timelockanalysis(cfg, data)
 
    The data should be organised in a structure as obtained from the
    `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>` function. The configuration should be according to
 
    cfg.channel            = Nx1 cell-array with selection of channels (default = 'all'),
                             see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.trials             = 'all' or a selection given as a 1xN vector (default = 'all')
    cfg.covariance         = 'no' or 'yes' (default = 'no')
    cfg.covariancewindow   = 'prestim', 'poststim', 'all' or [begin end] (default = 'all')
    cfg.keeptrials         = 'yes' or 'no', return individual trials or average (default = 'no')
    cfg.removemean         = 'no' or 'yes' for covariance computation (default = 'yes')
    cfg.vartrllength       = 0, 1 or 2 (see below)
 
    Depending on cfg.vartrllength, variable length trials and trials with
    differences in their time axes (so even if they are of the same length, e.g. 1
    second snippets of data cut from a single long recording) are treated differentl
    0 - do not accept variable length trials [default]
    1 - accept variable length trials, but only take those trials in which
        data is present in both the average and the covariance window
    2 - accept variable length trials, use all available trials
        the available samples in every trial will be used for the
        average and covariance computation. Missing values are replaced
        by NaN and are not included in the computation.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_timelockgrandaverage>``<font color=green>`FT_TIMELOCKGRANDAVERAGE`</font>``</a>`, `<a href=/reference/ft_timelockstatistics>``<font color=green>`FT_TIMELOCKSTATISTICS`</font>``</a>`
`</pre>``</html>`

