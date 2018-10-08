---
layout: default
---

##  FT_TIMELOCKBASELINE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_timelockbaseline".

`<html>``<pre>`
    `<a href=/reference/ft_timelockbaseline>``<font color=green>`FT_TIMELOCKBASELINE`</font>``</a>` performs baseline correction for ERF and ERP data
 
    Use as
     [timelock] = ft_timelockbaseline(cfg, timelock)
    where the timelock data comes from `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>` and the
    configuration should contain
    cfg.baseline     = [begin end] (default = 'no')
    cfg.channel      = cell-array, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>`
    cfg.parameter    = field for which to apply baseline normalization, or
                       cell array of strings to specify multiple fields to normalize
                       (default = 'avg')
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`, `<a href=/reference/ft_freqbaseline>``<font color=green>`FT_FREQBASELINE`</font>``</a>`, `<a href=/reference/ft_timelockgrandaverage>``<font color=green>`FT_TIMELOCKGRANDAVERAGE`</font>``</a>`
`</pre>``</html>`

