---
layout: default
---

##  FT_REALTIME_JAGA16PROXY

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_realtime_jaga16proxy".

`<html>``<pre>`
    `<a href=/reference/ft_realtime_jaga16proxy>``<font color=green>`FT_REALTIME_JAGA16PROXY`</font>``</a>` reads continuous EEG data from a Jinga-Hi JAGA16 system
    through the UDP network interface and writes it to a FieldTrip buffer.
 
    The FieldTrip buffer is a network transparent server that allows the acquisition
    client to stream data to it. An analysis client can connect to read the data upon
    request. Multiple clients can connect simultaneously, each analyzing a specific
    aspect of the data concurrently.
 
    Use as
    ft_realtime_jaga16proxy(cfg)
 
    The configuration should contain
    cfg.port                 = number, UDP port to listen on (default = 55000)
    cfg.channel              = cell-array with channel names, see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>`
    cfg.blocksize            = number, in seconds (default = 0.5)
    cfg.decimate             = integer number (default = 1)
    cfg.calibration          = number, in uV per bit (default = 1)
    cfg.feedback             = 'yes' or 'no' (default = 'no')
 
    The target to write the data to is configured as
    cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
    cfg.target.dataformat    = string, default is determined automatic
 
    To stop this realtime function, you have to press Ctrl-C
 
    See also `<a href=/reference/ft_realtime_signalproxy>``<font color=green>`FT_REALTIME_SIGNALPROXY`</font>``</a>`, `<a href=/reference/ft_realtime_signalviewer>``<font color=green>`FT_REALTIME_SIGNALVIEWER`</font>``</a>`
`</pre>``</html>`

