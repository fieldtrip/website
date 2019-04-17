---
title: ft_spike_rate
---
```
 FT_SPIKE_RATE computes the firing rate of spiketrains and their variance

 Use as
   [rate] = ft_spike_rate(cfg, spike)

 The input SPIKE should be organised as the spike or the (binary) raw
 datatype, obtained from FT_SPIKE_MAKETRIALS or FT_APPENDSPIKE (in that
 case, conversion is done within the function)

 Configurations:
   cfg.outputunit       = 'rate' (default) or 'spikecount'. If 'rate', we convert
                          the output per trial to firing rates (spikes/sec).
                          If 'spikecount', we count the number spikes per trial.
   cfg.spikechannel     = see FT_CHANNELSELECTION for details
   cfg.trials           = vector of indices (e.g., 1:2:10)
                          logical selection of trials (e.g., [1010101010])
                          'all' (default), selects all trials%   cfg.trials
   cfg.vartriallen      = 'yes' (default) or 'no'.
                          If 'yes' - accept variable trial lengths and use all available trials
                          and the samples in every trial.
                          If 'no'  - only select those trials that fully cover the window as
                          specified by cfg.latency and discard those trials that do not.
   cfg.latency          = [begin end] in seconds
                          'maxperiod' (default)
                          'minperiod', i.e., the minimal period all trials share
                          'prestim' (all t<=0)
                          'poststim' (all t>=0).
   cfg.keeptrials       = 'yes' or 'no' (default).

 The outputs from spike is a TIMELOCK structure (see FT_DATATYPE_TIMELOCK)
   rate.trial:        nTrials x nUnits matrix containing the firing rate per unit and trial
   rate.avg:          nTrials array containing the average firing rate per unit
   rate.var:          nTrials array containing the variance of firing rates per unit
   rate.dof:          nTrials array containing the degree of freedom per unit
   rate.label:        nUnits cell-array containing the labels of the neuronal units%
   rate.time:         Mean latency (this field ensures it is TIMELOCK
                      struct)
```
