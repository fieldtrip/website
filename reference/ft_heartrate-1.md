---
title: ft_heartrate
---
```
 FT_HEARTRATE estimates the heart rate from a continuous PPG or ECG channel. It
 returns a new data structure with a continuous representation of the heartrate in
 beats per minute.

 Use as
   dataout = ft_heartrate(cfg, data)
 where the input data is a structure as obtained from FT_PREPROCESSING.

 The configuration structure has the following options
   cfg.channel          = selected channel for processing, see FT_CHANNELSELECTION
   cfg.envelopewindow   = scalar, time in seconds
   cfg.peakseparation   = scalar, time in seconds
   cfg.threshold        = scalar, between 0 and 1 (default = 0.4)
   cfg.feedback         = 'yes' or 'no'
 The input data can be preprocessed on the fly using
   cfg.preproc.bpfilter = 'yes' or 'no'
   cfg.preproc.bpfreq   = [low high], filter frequency in Hz

 See also FT_ELECTRODERMALACTIVITY, FT_HEADMOVEMENT, FT_REGRESSCONFOUND
```
