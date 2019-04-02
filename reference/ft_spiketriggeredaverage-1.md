---
title: ft_spiketriggeredaverage
---
```
 FT_SPIKETRIGGEREDAVERAGE computes the avererage of the LFP around the
 spikes.

 Use as
   [timelock] = ft_spiketriggeredaverage(cfg, data)

 The input data should be organised in a structure as obtained from
 the FT_PREPROCESSING function. The configuration should be according to

   cfg.timwin       = [begin end], time around each spike (default = [-0.1 0.1])
   cfg.spikechannel = string, name of single spike channel to trigger on
   cfg.channel      = Nx1 cell-array with selection of channels (default = 'all'),
                      see FT_CHANNELSELECTION for details
   cfg.latency 
   cfg.keeptrials   = 'yes' or 'no', return individual trials or average (default = 'no')
   cfg.feedback     = 'no', 'text', 'textbar', 'gui' (default = 'no')
```
