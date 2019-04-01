---
title: ft_spiketriggeredspectrum_fft
---
```
 FT_SPIKETRIGGEREDSPECTRUM_FFT computes the Fourier spectrum (amplitude and phase)
 of the LFP around the % spikes.  A phase of zero corresponds to the spike being on
 the peak of the LFP oscillation. A phase of 180 degree corresponds to the spike being
 in the through of the oscillation. A phase of 45 degrees corresponds to the spike
 being just after the peak in the LFP.

 If the triggered spike leads a spike in another channel, then the angle of the Fourier
 spectrum of that other channel will be negative. Earlier phases are in clockwise
 direction. 

 Use as
   [sts] = ft_spiketriggeredspectrum_convol(cfg,data,spike)
 or 
   [sts] = ft_spiketriggeredspectrum_convol(cfg,data)
 where the spike data can either be contained in the DATA input or in the SPIKE input.

 The input DATA should be organised as the raw datatype, obtained from FT_PREPROCESSING
 or FT_APPENDSPIKE. 

 The (optional) input SPIKE should be organised as the spike or the raw datatype,
 obtained from FT_SPIKE_MAKETRIALS or FT_PREPROCESSING (in that case, conversion is done
 within the function)

 Important is that data.time and spike.trialtime should be referenced relative to the
 same trial trigger times.

 The configuration should be according to
   cfg.timwin       = [begin end], time around each spike (default = [-0.1 0.1])
   cfg.foilim       = [begin end], frequency band of interest (default = [0 150])
   cfg.taper        = 'dpss', 'hanning' or many others, see WINDOW (default = 'hanning')
   cfg.tapsmofrq    = number, the amount of spectral smoothing through
                      multi-tapering. Note that 4 Hz smoothing means plus-minus 4 Hz,
                      i.e. a 8 Hz smoothing box. Note: multitapering rotates phases (no
                      problem for consistency)
   cfg.spikechannel = string, name of spike channels to trigger on cfg.channel = Nx1
                      cell-array with selection of channels (default = 'all'),
                      see FT_CHANNELSELECTION for details
   cfg.feedback     = 'no', 'text', 'textbar', 'gui' (default = 'no')

 The output STS data structure can be input to FT_SPIKETRIGGEREDSPECTRUM_STAT

 This function uses a NaN-aware spectral estimation technique, which will default to the
 standard Matlab FFT routine if no NaNs are present. The fft_along_rows subfunction below
 demonstrates the expected function behavior.

 See FT_SPIKETRIGGEREDINTERPOLATION to remove segments of LFP around spikes.
 See FT_SPIKETRIGGEREDSPECTRUM_CONVOL for an alternative implementation based
 on convolution
```
