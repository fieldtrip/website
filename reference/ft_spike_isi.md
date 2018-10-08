---
layout: default
---

##  FT_SPIKE_ISI

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_spike_isi".

`<html>``<pre>`
    `<a href=/reference/ft_spike_isi>``<font color=green>`FT_SPIKE_ISI`</font>``</a>` computes the interspike interval histogram
 
    The input SPIKE should be organised as 
    a) the spike datatype, obtained from `<a href=/reference/ft_spike_maketrials>``<font color=green>`FT_SPIKE_MAKETRIALS`</font>``</a>` 
    b) the raw datatype, containing binary spike trains, obtained from
    `<a href=/reference/ft_appendspike>``<font color=green>`FT_APPENDSPIKE`</font>``</a>` or `<a href=/reference/ft_checkdata>``<font color=green>`FT_CHECKDATA`</font>``</a>`. In this case the raw datatype is
    converted to the spike datatype.
 
    Use as
    [isih] = ft_spike_isi(cfg, spike)
 
    Configuration
    cfg.outputunit       = 'spikecount' (default) or 'proportion' (sum of all bins = 1).
    cfg.spikechannel     = string or index of spike channels to
                           trigger on (default = 'all')
                           See `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details.
    cfg.trials           = numeric selection of trials (default = 'all')
    cfg.bins             = ascending vector of isi bin edges.
    cfg.latency          = [begin end] in seconds, 'max' (default), 'min', 'prestim'(t&lt;=0), or
                           'poststim' (t&gt;=0).
                           If 'max', we use all available latencies.
                           If 'min', we use only the time window contained by all trials.
                           If 'prestim' or 'poststim', we use time to or
                           from 0, respectively.
 `  cfg.keeptrials       = 'yes' or 'no'. If 'yes', we keep the individual
                            isis between spikes and output as isih.isi
    cfg.param            = string, one of
       'gamfit'      : returns [shape scale] for gamma distribution fit
       'coeffvar'    : coefficient of variation (sd / mean)
       'lv'          : Shinomoto's Local Variation measure (2009)
 
    Output
    isih.avg             = nUnits-by-nBins interspike interval histogram
    isih.time            = 1 x nBins bincenters corresponding to isih.avg
    isih.isi             = 1-by-nUnits cell with interval to previous spike per spike.
                           For example isih.isi{1}(2) = 0.1 means that the
                           second spike fired was 0.1 s later than the
                           first. Note that jumps within trials or first
                           spikes within trials are given NaNs.
    isih.label           = 1-by-nUnits cell array with labels
`</pre>``</html>`

