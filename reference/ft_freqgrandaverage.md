---
layout: default
---

##  FT_FREQGRANDAVERAGE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_freqgrandaverage".

`<html>``<pre>`
    `<a href=/reference/ft_freqgrandaverage>``<font color=green>`FT_FREQGRANDAVERAGE`</font>``</a>` computes the average powerspectrum or time-frequency spectrum
    over multiple subjects
 
    Use as
    [grandavg] = ft_freqgrandaverage(cfg, freq1, freq2, freq3...)
 
    The input data freq1..N are obtained from either `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>` with
    keeptrials=no or from `<a href=/reference/ft_freqdescriptives>``<font color=green>`FT_FREQDESCRIPTIVES`</font>``</a>`. The configuration structure
    can contain
    cfg.keepindividual = 'yes' or 'no' (default = 'no')
    cfg.foilim         = [fmin fmax] or 'all', to specify a subset of frequencies (default = 'all')
    cfg.toilim         = [tmin tmax] or 'all', to specify a subset of latencies (default = 'all')
    cfg.channel        = Nx1 cell-array with selection of channels (default = 'all'),
                         see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.parameter      = string or cell-array of strings indicating which
                         parameter(s) to average. default is set to
                         'powspctrm', if it is present in the data.
 
    To facilitate data-handling and distributed computing you can use
    cfg.inputfile   =  ...
    cfg.outputfile  =  ...
    If you specify one of these (or both) the input data will be read from a *.mat
    file on disk and/or the output data will be written to a *.mat file. These mat
    files should contain only a single variable, corresponding with the
    input/output structure. For this particular function, the input should be
    specified as a cell array.
 
    See also `<a href=/reference/ft_timelockgrandaverage>``<font color=green>`FT_TIMELOCKGRANDAVERAGE`</font>``</a>`, `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`, `<a href=/reference/ft_freqdescriptives>``<font color=green>`FT_FREQDESCRIPTIVES`</font>``</a>`,
    `<a href=/reference/ft_freqbaseline>``<font color=green>`FT_FREQBASELINE`</font>``</a>`
`</pre>``</html>`

