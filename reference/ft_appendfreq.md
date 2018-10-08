---
layout: default
---

##  FT_APPENDFREQ

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_appendfreq".

`<html>``<pre>`
    `<a href=/reference/ft_appendfreq>``<font color=green>`FT_APPENDFREQ`</font>``</a>` concatenates multiple frequency or time-frequency data structures
    that have been processed separately. If the input data structures contain different
    channels, it will be concatenated along the channel direction. If the channels are
    identical in the input data structures, the data will be concatenated along the
    repetition dimension.
 
    Use as
   combined = ft_appendfreq(cfg, freq1, freq2, ...)
 
    The configuration should contain
    cfg.parameter  = string, the name of the field to concatenate
 
    The configuration can optionally contain
    cfg.appenddim  = string, the dimension to concatenate over (default is automatic)
    cfg.tolerance  = scalar, tolerance to determine how different the frequency and/or
                     time axes are allowed to still be considered compatible (default = 1e-5)
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a

* .mat file on disk and/or the output data will be written to a *.mat file.
    These mat files should contain only a single variable, corresponding with
    the input/output structure.
 
    See also `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`, `<a href=/reference/ft_datatype_freq>``<font color=green>`FT_DATATYPE_FREQ`</font>``</a>`, `<a href=/reference/ft_appenddata>``<font color=green>`FT_APPENDDATA`</font>``</a>`, `<a href=/reference/ft_appendtimelock>``<font color=green>`FT_APPENDTIMELOCK`</font>``</a>`,
    `<a href=/reference/ft_appendsens>``<font color=green>`FT_APPENDSENS`</font>``</a>`
`</pre>``</html>`

