---
layout: default
---

##  FT_REALTIME_SELECTIVEAVERAGE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_realtime_selectiveaverage".

`<html>``<pre>`
    `<a href=/reference/ft_realtime_selectiveaverage>``<font color=green>`FT_REALTIME_SELECTIVEAVERAGE`</font>``</a>` is an example realtime application for online
    averaging of the data. It should work both for EEG and MEG.
 
    Use as
    ft_realtime_selectiveaverage(cfg)
    with the following configuration options
    cfg.channel    = cell-array, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` (default = 'all')
    cfg.trialfun   = string with the trial function
 
    The source of the data is configured as
    cfg.dataset       = string
    or alternatively to obtain more low-level control as
    cfg.datafile      = string
    cfg.headerfile    = string
    cfg.eventfile     = string
    cfg.dataformat    = string, default is determined automatic
    cfg.headerformat  = string, default is determined automatic
    cfg.eventformat   = string, default is determined automatic
 
    To stop the realtime function, you have to press Ctrl-C
`</pre>``</html>`

