---
layout: default
---

##  FT_REALTIME_ASAPROXY

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_realtime_asaproxy".

`<html>``<pre>`
    `<a href=/reference/ft_realtime_asaproxy>``<font color=green>`FT_REALTIME_ASAPROXY`</font>``</a>` reads continuous data from the ASA acquisition system and
    writes it to a FieldTrip buffer. This function uses the NeuroSDK software, which
    can be obtained from ANT.
 
    The FieldTrip buffer is a network transparent server that allows the acquisition
    client to stream data to it. An analysis client can connect to read the data upon
    request. Multiple clients can connect simultaneously, each analyzing a specific
    aspect of the data concurrently.
 
    Use as
    ft_realtime_asaproxy(cfg)
 
    The configuration should contain
    cfg.channel              = cell-array, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` (default = 'all')
 
    The target to write the data to is configured as
    cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
    cfg.target.dataformat    = string, default is determined automatic
 
    To stop this realtime function, you have to press Ctrl-C
 
    See also `<a href=/reference/ft_realtime_signalproxy>``<font color=green>`FT_REALTIME_SIGNALPROXY`</font>``</a>`, `<a href=/reference/ft_realtime_signalviewer>``<font color=green>`FT_REALTIME_SIGNALVIEWER`</font>``</a>`
`</pre>``</html>`

