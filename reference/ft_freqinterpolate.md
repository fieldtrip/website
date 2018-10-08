---
layout: default
---

##  FT_FREQINTERPOLATE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_freqinterpolate".

`<html>``<pre>`
    `<a href=/reference/ft_freqinterpolate>``<font color=green>`FT_FREQINTERPOLATE`</font>``</a>` interpolates frequencies by looking at neighbouring
    values or simply replaces a piece in the spectrum by NaN.
 
    Use as
    freq = ft_freqinterpolate(cfg, freq)
    where freq is the output of `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>` or `<a href=/reference/ft_freqdescriptives>``<font color=green>`FT_FREQDESCRIPTIVES`</font>``</a>` and the
    configuration may contain
    cfg.method   = 'nan', 'linear' (default = 'nan')
    cfg.foilim   = Nx2 matrix with begin and end of each interval to be
                   interpolated (default = [49 51; 99 101; 149 151])
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure.
 
    See also `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`, `<a href=/reference/ft_freqdescriptives>``<font color=green>`FT_FREQDESCRIPTIVES`</font>``</a>`, `<a href=/reference/ft_freqsimulation>``<font color=green>`FT_FREQSIMULATION`</font>``</a>`
`</pre>``</html>`

