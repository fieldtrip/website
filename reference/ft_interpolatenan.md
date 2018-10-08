---
layout: default
---

##  FT_INTERPOLATENAN

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_interpolatenan".

`<html>``<pre>`
    `<a href=/reference/ft_interpolatenan>``<font color=green>`FT_INTERPOLATENAN`</font>``</a>` interpolates time series that contains segments of nans obtained
    by replacing artifactual data with nans using, for example, `<a href=/reference/ft_rejectartifact>``<font color=green>`FT_REJECTARTIFACT`</font>``</a>`, or
    by redefining trials with `<a href=/reference/ft_redefinetrial>``<font color=green>`FT_REDEFINETRIAL`</font>``</a>` resulting in trials with gaps.
 
    Use as
    outdata = ft_interpolatenan(cfg, indata)
    where cfg is a configuration structure and the input data is obtained from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    The configuration should contain
    cfg.method      = string, interpolation method, see HELP INTERP1 (default = 'linear')
    cfg.prewindow   = value, length of data prior to interpolation window, in seconds (default = 1)
    cfg.postwindow  = value, length of data after interpolation window, in seconds (default = 1)
    cfg.feedback    = string, 'no', 'text', 'textbar', 'gui' (default = 'text')
 
    This function only interpolates over time, not over space. If you want to
    interpolate using spatial information, e.g. using neighbouring channels, you should
    use `<a href=/reference/ft_channelrepair>``<font color=green>`FT_CHANNELREPAIR`</font>``</a>`.
 
    To facilitate data-handling and distributed computing with the peer-to-peer
    module, this function has the following option
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_rejectartifact>``<font color=green>`FT_REJECTARTIFACT`</font>``</a>`, `<a href=/reference/ft_redefinetrial>``<font color=green>`FT_REDEFINETRIAL`</font>``</a>`, `<a href=/reference/ft_channelrepair>``<font color=green>`FT_CHANNELREPAIR`</font>``</a>`
`</pre>``</html>`

