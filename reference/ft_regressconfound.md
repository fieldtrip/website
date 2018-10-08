---
layout: default
---

##  FT_REGRESSCONFOUND

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_regressconfound".

`<html>``<pre>`
    `<a href=/reference/ft_regressconfound>``<font color=green>`FT_REGRESSCONFOUND`</font>``</a>` estimates the regression weight of a set of confounds
    using a General Linear Model (GLM) and removes the estimated contribution
    from the single-trial data.
 
    Use as
    timelock = ft_regressconfound(cfg, timelock)
    or as
    freq     = ft_regressconfound(cfg, freq)
    or as
    source   = ft_regressconfound(cfg, source)
 
    where timelock, freq, or, source come from `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`,
    `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`, or `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>` respectively, with keeptrials = 'yes'
 
    The cfg argument is a structure that should contain
    cfg.confound    = matrix, [Ntrials X Nconfounds], may not contain NaNs
 
    The following configuration options are supporte
    cfg.reject      = vector, [1 X Nconfounds], listing the confounds that
                      are to be rejected (default = 'all')
    cfg.normalize   = string, 'yes' or 'no', normalization to
                      make the confounds orthogonal (default = 'yes')
    cfg.output      = 'residual' (default), 'beta', or 'model'.
                      If 'residual' is specified, the output is a data
                      structure containing the residuals after regressing
                      out the in cfg.reject listed confounds. If 'beta' or 'model'
                      is specified, the output is a data structure containing
                      the regression weights or the model, respectively.
 
    This method is described by Stolk et al., Online and offline tools for head
    movement compensation in MEG (Neuroimage, 2013)
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_rejectcomponent>``<font color=green>`FT_REJECTCOMPONENT`</font>``</a>`, `<a href=/reference/ft_rejectartifact>``<font color=green>`FT_REJECTARTIFACT`</font>``</a>`
`</pre>``</html>`

