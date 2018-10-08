---
layout: default
---

##  FT_REALTIME_FMRIVIEWER

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_realtime_fmriviewer".

`<html>``<pre>`
    `<a href=/reference/ft_realtime_fmriviewer>``<font color=green>`FT_REALTIME_FMRIVIEWER`</font>``</a>` allows for realtime visualization of the fMRI data stream
 
    Use as
    ft_realtime_fmriviewer(cfg)
    with the following configuration options
    cfg.bufferdata = whether to start on the 'first or 'last' data that is available (default = 'last')
 
    The source of the data is configured as
    cfg.dataset       = string
    or alternatively to obtain more low-level control as
    cfg.datafile      = string
    cfg.headerfile    = string
    cfg.eventfile     = string
    cfg.dataformat    = string, default is determined automatic
    cfg.headerformat  = string, default is determined automatic
    cfg.eventformat   = string, default is determined automatic
`</pre>``</html>`

