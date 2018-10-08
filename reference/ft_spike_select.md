---
layout: default
---

##  FT_SPIKE_SELECT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_spike_select".

`<html>``<pre>`
    `<a href=/reference/ft_spike_select>``<font color=green>`FT_SPIKE_SELECT`</font>``</a>` selects subsets of spikes, channels and trials from a
    spike structure.
 
    Use as
    [spike] = ft_spike_select(cfg, spike)
 
    The input SPIKE should be organised as the spike datatype (see
    `<a href=/reference/ft_datatype_spike>``<font color=green>`FT_DATATYPE_SPIKE`</font>``</a>`) 
 
    Configuration
    cfg.spikechannel     = See `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details.
    cfg.trials           = vector of indices (e.g., 1:2:10)
                           logical selection of trials (e.g., [1010101010])
                           'all' (default), selects all trials
    cfg.latency          = [begin end] in seconds
                           'maxperiod' (default), i.e., maximum period available
                           'minperiod', i.e., the minimal period all trials share
                           'prestim' (all t&lt;=0)
                           'poststim' (all t&gt;=0).
    Output
    Spike structure with selections
`</pre>``</html>`

