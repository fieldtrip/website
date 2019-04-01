---
title: ft_spike_jpsth
---
```
 FT_SPIKE_JPSTH computes the joint peristimulus histograms for spiketrains
 and a shift predictor (for example see Aertsen et al. 1989).

 The shift predictor is computed in consecutive trials in a symmetric way.
 For example, we compute the jpsth for chan 1 in trial 1 versus chan 2 in
 trial 2, but also for chan 1 in trial 2 versus chan 2 in trial 1. This
 gives (nTrials-1)*2 jpsth matrices for individual trials. Picking
 consecutive trials and computing the shift predictor in a symmetric way
 ensures that slow changes in the temporal structure do not affect the
 shift predictor (as opposed to shuffling the order of all trials for one
 of the two channels).

 Use as
   [jpsth] = ft_spike_jpsth(cfg,psth)

 The input PSTH should be organised as the input from FT_SPIKE_PSTH,
 FT_SPIKE_DENSITY or FT_TIMELOCKANALYSIS containing a field PSTH.trial and
 PSTH.time. In any case, one is expected to use cfg.keeptrials = 'yes' in
 these functions.

 Configurations:
   cfg.method           = 'jpsth' or 'shiftpredictor'. If 'jpsth', we
                           output the normal stat. If 'shiftpredictor',
                           we compute the jpsth after shuffling subsequent
                           trials.
   cfg.normalization    = 'no' (default), or 'yes'. If requested, the joint psth is normalized as in van Aertsen et al. (1989).
   cfg.channelcmb       =  Mx2 cell-array with selection of channel pairs (default = {'all' 'all'}), see FT_CHANNELCOMBINATION for details
   cfg.trials           = 'all' (default) or numerical or logical array of to be selected trials.
   cfg.latency          = [begin end] in seconds, 'maxperiod' (default), 'prestim'(t<=0), or 'poststim' (t>=0)
   cfg.keeptrials       = 'yes' or 'no' (default)

 See also FT_SPIKE_PSTH
```
