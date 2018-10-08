---
layout: default
---

##  FT_REALTIME_BRAINAMPPROXY

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_realtime_brainampproxy".

`<html>``<pre>`
    `<a href=/reference/ft_realtime_brainampproxy>``<font color=green>`FT_REALTIME_BRAINAMPPROXY`</font>``</a>` reads continuous data from a BrainAmp EEG acquisition
    system through the RDA network interface and writes it to a FieldTrip buffer.
 
    The FieldTrip buffer is a network transparent server that allows the acquisition
    client to stream data to it. An analysis client can connect to read the data upon
    request. Multiple clients can connect simultaneously, each analyzing a specific
    aspect of the data concurrently.
 
    Use as
    ft_realtime_brainampproxy(cfg)
 
    The configuration should contain
    cfg.host                 = string, name of computer running the recorder software (default = 'eeg002')
    cfg.port                 = number, TCP port to connect to (default = 51244)
    cfg.channel              = cell-array, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` (default = 'all')
    cfg.feedback             = 'yes' or 'no' (default = 'no')
 
    The target to write the data to is configured as
    cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
    cfg.target.dataformat    = string, default is determined automatic
    cfg.target.eventfile     = string, target destination for the events (default = 'buffer://localhost:1972')
    cfg.target.eventformat   = string, default is determined automatic
 
    To stop this realtime function, you have to press Ctrl-C
 
    See also `<a href=/reference/ft_realtime_signalproxy>``<font color=green>`FT_REALTIME_SIGNALPROXY`</font>``</a>`, `<a href=/reference/ft_realtime_signalviewer>``<font color=green>`FT_REALTIME_SIGNALVIEWER`</font>``</a>`
`</pre>``</html>`

