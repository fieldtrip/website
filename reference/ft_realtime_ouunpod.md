---
layout: default
---

##  FT_REALTIME_OUUNPOD

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_realtime_ouunpod".

`<html>``<pre>`
    `<a href=/reference/ft_realtime_ouunpod>``<font color=green>`FT_REALTIME_OUUNPOD`</font>``</a>` is an example realtime application for online power
    estimation and visualisation. It is designed for use with the OuUnPod, an
    OpenEEG based low cost EEG system with two channels, but in principle
    should work for any EEG or MEG system.
 
    Use as
    ft_realtime_ouunpod(cfg)
    with the following configuration options
    cfg.channel    = cell-array, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` (default = 'all')
    cfg.foilim     = [Flow Fhigh] (default = [1 45])
    cfg.blocksize  = number, size of the blocks/chuncks that are processed (default = 1 second)
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
 
    To stop the realtime function, you have to press Ctrl-C
 
    See also http://ouunpod.blogspot.com
`</pre>``</html>`

