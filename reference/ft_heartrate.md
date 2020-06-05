---
title: ft_heartrate
---
```plaintext
 FT_HEARTRATE estimates the heart rate from a continuous PPG or ECG channel. It
 returns a new data structure with a continuous representation of the heartrate in
 beats per minute.

 Use as
   dataout = ft_heartrate(cfg, data)
 where the input data is a structure as obtained from FT_PREPROCESSING.

 The configuration structure has the following general options
   cfg.channel          = selected channel for processing, see FT_CHANNELSELECTION
   cfg.feedback         = 'yes' or 'no'
   cfg.method           = string representing the method for heart beat detection
                          'findpeaks'  filtering and normalization, followed by FINDPEAKS (default)
                          'pantompkin' implementation of the Pan-Tompkin algorithm for ECG beat detection

 For the 'findpeaks' method the following additional options can be specified
   cfg.envelopewindow   = scalar, time in seconds (default = 10)
   cfg.peakseparation   = scalar, time in seconds
   cfg.threshold        = scalar, usually between 0 and 1 (default = 0.4)
   cfg.flipsignal       = 'yes' or 'no', whether to flip the polarity of the signal (default is automatic)
 and the data can be preprocessed on the fly using
   cfg.preproc.bpfilter = 'yes' or 'no'
   cfg.preproc.bpfreq   = [low high], filter frequency in Hz
 This implementation performs some filtering and amplitude normalization, followed
 by the FINDPEAKS function. It works both for ECG as for PPG signals.

 For the 'pantompkin` method there are no additional options. This implements
 - J Pan, W J Tompkins, "A Real-Time QRS Detection Algorithm", IEEE Trans Biomed Eng, 1985. https://doi.org/10.1109/tbme.1985.325532
 - H Sedghamiz, "Matlab Implementation of Pan Tompkins ECG QRS detector". https://doi.org/10.13140/RG.2.2.14202.59841

 See also FT_ELECTRODERMALACTIVITY, FT_HEADMOVEMENT, FT_REGRESSCONFOUND
```
