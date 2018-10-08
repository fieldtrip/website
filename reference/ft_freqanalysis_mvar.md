---
layout: default
---

##  FT_FREQANALYSIS_MVAR

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_freqanalysis_mvar".

`<html>``<pre>`
    `<a href=/reference/ft_freqanalysis_mvar>``<font color=green>`FT_FREQANALYSIS_MVAR`</font>``</a>` performs frequency analysis on
    mvar data, by fourier transformation of the coefficients. The output
    contains cross-spectral density, spectral transfer matrix, and the
    covariance of the innovation noise. The dimord = 'chan_chan(_freq)(_time)
 
    The function is stand-alone, but is typically called through
    `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`, specifying cfg.method = 'mvar'.
 
    Use as
    [freq] = ft_freqanalysis(cfg, data), with cfg.method = 'mvar'
 
    or
 
    [freq] = ft_freqanalysis_mvar(cfg, data)
 
    The input data structure should be a data structure created by
    `<a href=/reference/ft_mvaranalysis>``<font color=green>`FT_MVARANALYSIS`</font>``</a>`, i.e. a data-structure of type 'mvar'.
 
    The configuration can contai
    cfg.foi = vector with the frequencies at which the spectral quantities
                are estimated (in Hz). Default: 0:1:Nyquist
    cfg.feedback = 'none', or any of the methods supported by `<a href=/reference/ft_progress>``<font color=green>`FT_PROGRESS`</font>``</a>`,
                     for providing feedback to the user in the command
                     window.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_mvaranalysis>``<font color=green>`FT_MVARANALYSIS`</font>``</a>`, `<a href=/reference/ft_datatype_mvar>``<font color=green>`FT_DATATYPE_MVAR`</font>``</a>`, `<a href=/reference/ft_progress>``<font color=green>`FT_PROGRESS`</font>``</a>`
`</pre>``</html>`

