---
layout: default
---

##  FT_REALTIME_DICOMPROXY

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_realtime_dicomproxy".

`<html>``<pre>`
    `<a href=/reference/ft_realtime_dicomproxy>``<font color=green>`FT_REALTIME_DICOMPROXY`</font>``</a>` simulates an fMRI acquisition system by reading a series of
    DICOM files from disk, and streaming them to a FieldTrip buffer.
 
    Use as
    ft_realtime_dicomproxy(cfg)
 
    The target to write the data to is configured as
    cfg.target.datafile      = string, target destination for the data (default = 'buffer://localhost:1972')
    cfg.input                = string or cell array of strings (see below)
    cfg.speedup              = optional speedup parameter
 
    The input files can be specified as a cell array of filenames, or as a single
    string with a wildcard, e.g., '/myhome/scan*.ima'
 
    This function requires functions from SPM, so make sure you have set up your path correctly.
 
    See also `<a href=/reference/ft_realtime_signalproxy>``<font color=green>`FT_REALTIME_SIGNALPROXY`</font>``</a>`, `<a href=/reference/ft_realtime_signalviewer>``<font color=green>`FT_REALTIME_SIGNALVIEWER`</font>``</a>`
`</pre>``</html>`

