---
layout: default
---

##  FT_WRITE_SPIKE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_write_spike".

`<html>``<pre>`
    `<a href=/reference/ft_write_spike>``<font color=green>`FT_WRITE_SPIKE`</font>``</a>` writes animal electrophysiology spike timestamps and/or waveforms
    to file
 
    Use as
    ft_write_spike(filename, spike, ...)
 
    Additional options should be specified in key-value pairs and can be
    'dataformat'          string, see below
    'fsample'             sampling frequency of the waveforms
    'chanindx'            index of selected channels
    'TimeStampPerSample'  number of timestamps per sample
 
    The supported dataformats are
    neuralynx_nse
    neuralynx_nts
    plexon_nex
    matlab
 
    See also `<a href=/reference/ft_read_spike>``<font color=green>`FT_READ_SPIKE`</font>``</a>`
`</pre>``</html>`

