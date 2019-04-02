---
title: ft_spike_xcorr
---
```
 FT_SPIKE_XCORR computes the cross-correlation histogram and shift predictor.

 Use as
   [stat] = ft_spike_xcorr(cfg, data)

 The input SPIKE should be organised as the spike or the raw datatype, obtained from
 FT_SPIKE_MAKETRIALS or FT_PREPROCESSING (in that case, conversion is done
 within the function). A mex file is located in /contrib/spike/private
 which will be automatically mexed.

 Configurations options for xcorr general:
   cfg.maxlag           = number in seconds, indicating the maximum lag for the
                          cross-correlation function in sec (default = 0.1 sec).
   cfg.debias           = 'yes' (default) or 'no'. If 'yes', we scale the
                          cross-correlogram by M/(M-abs(lags)), where M = 2*N -1 with N
                          the length of the data segment.
   cfg.method           = 'xcorr' or 'shiftpredictor'. If 'shiftpredictor'
                           we do not compute the normal cross-correlation
                           but shuffle the subsequent trials.
                           If two channels are independent, then the shift
                           predictor should give the same correlogram as the raw
                           correlogram calculated from the same trials.
                           Typically, the shift predictor is subtracted from the
                           correlogram.
   cfg.outputunit       = - 'proportion' (value in each bin indicates proportion of occurence)
                          - 'center' (values are scaled to center value which is set to 1)
                          - 'raw' (default) unnormalized crosscorrelogram.
   cfg.binsize          = [binsize] in sec (default = 0.001 sec).
   cfg.channelcmb       = Mx2 cell-array with selection of channel pairs (default = {'all' 'all'}),
                          see FT_CHANNELCOMBINATION for details
   cfg.latency          = [begin end] in seconds, 'max' (default), 'min', 'prestim'(t<=0), or
                          'poststim' (t>=0).%
   cfg.vartriallen      = 'yes' (default) or 'no'.
                          If 'yes' - accept variable trial lengths and use all available trials
                          and the samples in every trial.
                          If 'no'  - only select those trials that fully cover the window as
                          specified by cfg.latency and discard those trials that do not.
                          if cfg.method = 'yes', then cfg.vartriallen
                          should be 'no' (otherwise, fewer coincidences
                          will occur because of non-overlapping windows)
   cfg.trials           = numeric selection of trials (default = 'all')
   cfg.keeptrials       = 'yes' or 'no' (default)

 A peak at a negative lag for stat.xcorr(chan1,chan2,:) means that chan1 is leading
 chan2. Thus, a negative lag represents a spike in the second dimension of
 stat.xcorr before the channel in the third dimension of stat.stat.

 Variable trial length is controlled by the option cfg.vartriallen. If it is
 specified as cfg.vartriallen='yes', all trials are selected that have a minimum
 overlap with the latency window of cfg.maxlag. However, the shift predictor
 calculation demands that following trials have the same amount of data, otherwise,
 it does not control for rate non-stationarities. If cfg.vartriallen = 'yes', all
 trials should fall in the latency window, otherwise we do not compute the shift
 predictor.

 Output:
    stat.xcorr            = nchans-by-nchans-by-(2*nlags+1) cross correlation histogram with dimord 'chan_chan_time'
   or
    stat.shiftpredictor   = nchans-by-nchans-by-(2*nlags+1) shift predictor with dimord 'chan_chan_time'
 and
    stat.lags             = (2*nlags + 1) vector with lags in seconds.
    stat.trial            = ntrials-by-nchans-by-nchans-by-(2*nlags + 1) with single trials and dimord 'rpt_chan_chan_time'
    stat.label            = corresponding labels to channels in stat.xcorr
    stat.cfg              = configurations used in this function
```
