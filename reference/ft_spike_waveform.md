---
title: ft_spike_waveform
---
```
 FT_SPIKE_WAVEFORM computes descriptive parameters on
 waveform (mean and variance), and performs operations like realignment, outlier rejection,
 invertation, normalization and interpolation (see configurations).

 Use as
   [wave] = ft_spike_waveform(cfg, spike)
 Or
   [wave, spike] = ft_spike_waveform(cfg, spike)
 The input SPIKE should be organised as the SPIKE datatype (see FT_DATATYPE_SPIKE)

 Configurations:
   cfg.rejectonpeak     = 'yes' (default) or 'no': takes away waveforms with too late peak, and no
                           rising AP towards peak of other waveforms
   cfg.rejectclippedspikes = 'yes' (default) or 'no': removes spikes that
                           saturated the voltage range. 
   cfg.normalize        = 'yes' (default) or 'no': normalizes all
   waveforms
                           to have peak-to-through amp of 2
   cfg.interpolate      = double integer (default = 1). Increaes the
                          density of samples by a factor cfg.interpolate
   cfg.align            = 'yes' (def). or 'no'. If 'yes', we align all waves to
                          maximum
   cfg.fsample          = sampling frequency of waveform time-axis.
                          Obligatory field.
   cfg.spikechannel     = See FT_CHANNELSELECTION for details.

 Outputs:
   Wave.avg   = average waveform
   Wave.time  = time of waveform axis
   Wave.var   = variance of waveform
   Wave.dof   = number of spikes contributing to average

 Spike structure if two outputs are desired: waveform is replaced by interpolated and
 cleaned waveforms, removing also their associated time-stamps and data.
```
