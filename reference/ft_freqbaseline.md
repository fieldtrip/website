---
layout: default
---

##  FT_FREQBASELINE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_freqbaseline".

`<html>``<pre>`
    `<a href=/reference/ft_freqbaseline>``<font color=green>`FT_FREQBASELINE`</font>``</a>` performs baseline normalization for time-frequency data
 
    Use as
     [freq] = ft_freqbaseline(cfg, freq)
    where the freq data comes from `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>` and the configuration
    should contain
    cfg.baseline     = [begin end] (default = 'no'), alternatively an
                       Nfreq x 2 matrix can be specified, that provides
                       frequency specific baseline windows.
    cfg.baselinetype = 'absolute', 'relative', 'relchange', 'normchange' or 'db' (default = 'absolute')
    cfg.parameter    = field for which to apply baseline normalization, or
                       cell array of strings to specify multiple fields to normalize
                       (default = 'powspctrm')
 
    See also `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`, `<a href=/reference/ft_timelockbaseline>``<font color=green>`FT_TIMELOCKBASELINE`</font>``</a>`, FT_FREQCOMPARISON,
    `<a href=/reference/ft_freqgrandaverage>``<font color=green>`FT_FREQGRANDAVERAGE`</font>``</a>`
`</pre>``</html>`

