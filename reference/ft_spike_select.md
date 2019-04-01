---
title: ft_spike_select
---
```
 FT_SPIKE_SELECT selects subsets of spikes, channels and trials from a
 spike structure.

 Use as
   [spike] = ft_spike_select(cfg, spike)

 The input SPIKE should be organised as the spike datatype (see
 FT_DATATYPE_SPIKE) 

 Configurations:
   cfg.spikechannel     = See FT_CHANNELSELECTION for details.
   cfg.trials           = vector of indices (e.g., 1:2:10)
                          logical selection of trials (e.g., [1010101010])
                          'all' (default), selects all trials
   cfg.latency          = [begin end] in seconds
                          'maxperiod' (default), i.e., maximum period available
                          'minperiod', i.e., the minimal period all trials share
                          'prestim' (all t<=0)
                          'poststim' (all t>=0).
 Outputs:
   Spike structure with selections
```
