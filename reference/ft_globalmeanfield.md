---
layout: default
---

##  FT_GLOBALMEANFIELD

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_globalmeanfield".

`<html>``<pre>`
    `<a href=/reference/ft_globalmeanfield>``<font color=green>`FT_GLOBALMEANFIELD`</font>``</a>` calculates global mean field amplitude or power of input data
 
    Use as
    [gmf] = ft_globalmeanfield(cfg, data)
 
    The data should be organised in a structure as obtained from the
    `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>` function. The configuration should be according to
    `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>` function. The configuration should be according to
 
    cfg.method    = string, determines whether the amplitude or power should be calculated (see below, default is 'amplitude', can be 'power')
    cfg.channel   = Nx1 cell-array with selection of channels (default = 'all'),
                             see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
 
    This function calculates the global mean field power, or amplitude,
    as described i
    Lehmann D, Skrandies W. Reference-free identification of components of
    checkerboard-evoked multichannel potential fields. Electroencephalogr Clin
    Neurophysiol. 1980 Jun;48(6):609-21. PubMed PMID: 6155251.
 
    Please note that to calculate what is clasically referred to as Global
    Mean Field Power, cfg.method must be 'amplitude'. The naming implies a
    squared measure but this is not the case.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`
`</pre>``</html>`

