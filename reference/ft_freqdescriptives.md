---
layout: default
---

##  FT_FREQDESCRIPTIVES

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_freqdescriptives".

`<html>``<pre>`
    `<a href=/reference/ft_freqdescriptives>``<font color=green>`FT_FREQDESCRIPTIVES`</font>``</a>` computes descriptive univariate statistics of
    the frequency or time-frequency decomposition of the EEG/MEG signal,
    thus the powerspectrum and its standard error.
 
    Use as
    [freq] = ft_freqdescriptives(cfg, freq)
    [freq] = ft_freqdescriptives(cfg, freqmvar)
 
    The data in freq should be organised in a structure as obtained from
    from the `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>` or `<a href=/reference/ft_mvaranalysis>``<font color=green>`FT_MVARANALYSIS`</font>``</a>` function. The output structure is comparable
    to the input structure and can be used in most functions that require
    a freq input.
 
    The configuration options are
    cfg.variance      = 'yes' or 'no', estimate standard error in the standard way (default = 'no')
    cfg.jackknife     = 'yes' or 'no', estimate standard error by means of the jack-knife (default = 'no')
    cfg.keeptrials    = 'yes' or 'no', estimate single trial power (useful for fourier data) (default = 'no')
    cfg.channel       = Nx1 cell-array with selection of channels (default = 'all'),
                        see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.trials        = 'all' or a selection given as a 1xN vector (default = 'all')
    cfg.frequency     = [fmin fmax] or 'all', to specify a subset of frequencies (default = 'all')
    cfg.latency       = [tmin tmax] or 'all', to specify a subset of latencies (default = 'all')
 
    A variance estimate can only be computed if results from trials and/or
    tapers have been kept.
 
    Descriptive statistics of bivariate metrics is not computed by this function anymore. To this end you
    should use `<a href=/reference/ft_connectivityanalysis>``<font color=green>`FT_CONNECTIVITYANALYSIS`</font>``</a>`.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`, `<a href=/reference/ft_freqstatistics>``<font color=green>`FT_FREQSTATISTICS`</font>``</a>`, `<a href=/reference/ft_freqbaseline>``<font color=green>`FT_FREQBASELINE`</font>``</a>`, `<a href=/reference/ft_connectivityanalysis>``<font color=green>`FT_CONNECTIVITYANALYSIS`</font>``</a>`
`</pre>``</html>`

