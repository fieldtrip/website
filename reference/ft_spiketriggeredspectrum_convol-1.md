---
title: ft_spiketriggeredspectrum_convol
---
```
 FT_SPIKETRIGGEREDSPECTRUM_CONVOL computes the Fourier spectrum (amplitude and
 phase) of the LFP around the spikes using convolution of the complete LFP traces. A
 phase of zero corresponds to the spike being on the peak of the LFP oscillation. A
 phase of 180 degree corresponds to the spike being in the through of the oscillation.
 A phase of 45 degrees corresponds to the spike being just after the peak in the LFP.

 The difference to FT_SPIKETRIGGEREDSPECTRUM_FFT is that this function allows for
 multiple frequencies to be processed with different time-windows per frequency, and
 that FT_SPIKETRIGGEREDSPECTRUM_FFT is based on taking the FFT of a limited LFP
 segment around each spike.

 Use as
   [sts] = ft_spiketriggeredspectrum_convol(cfg,data,spike)
 or 
   [sts] = ft_spiketriggeredspectrum_convol(cfg,data)
 The spike data can either be contained in the data input or in the spike
 input.

 The input DATA should be organised as the raw datatype, obtained from
 FT_PREPROCESSING or FT_APPENDSPIKE.

 The input SPIKE should be organised as the spike or the raw datatype, obtained from
 FT_SPIKE_MAKETRIALS or FT_PREPROCESSING, in which case the conversion is done
 within this function.

 Important is that data.time and spike.trialtime should be referenced
 relative to the same trial trigger times!

 Configurations (following largely FT_FREQNALYSIS with method mtmconvol)
     cfg.tapsmofrq       = vector 1 x numfoi, the amount of spectral smoothing through
                           multi-tapering. Note that 4 Hz smoothing means
                           plus-minus 4 Hz, i.e. a 8 Hz smoothing box.
     cfg.foi             = vector 1 x numfoi, frequencies of interest
     cfg.taper           = 'dpss', 'hanning' or many others, see WINDOW (default = 'hanning')
     cfg.t_ftimwin       = vector 1 x numfoi, length of time window (in
     seconds)
     cfg.taperopt        =  parameter that goes in WINDOW function (only
                           applies to windows like KAISER).
     cfg.spikechannel    = cell-array with selection of channels (default = 'all')
                           see FT_CHANNELSELECTION for details
     cfg.channel         = Nx1 cell-array with selection of channels (default = 'all'),
                           see FT_CHANNELSELECTION for details
     cfg.borderspikes    = 'yes' (default) or 'no'. If 'yes', we process the spikes
                           falling at the border using an LFP that is not centered
                           on the spike. If 'no', we output NaNs for spikes
                           around which we could not center an LFP segment.
     cfg.rejectsaturation= 'yes' (default) or 'no'. If 'yes', we set
                           EEG segments where the maximum or minimum
                           voltage range is reached
                           with zero derivative (i.e., saturated signal) to
                           NaN, effectively setting all spikes phases that
                           use these parts of the EEG to NaN. An EEG that
                           saturates always returns the same phase at all
                           frequencies and should be ignored.

 Note: some adjustment of the frequencies can occur as the chosen time-window may not 
 be appropriate for the chosen frequency.
 For example, suppose that cfg.foi = 80, data.fsample = 1000, and
 cfg.t_ftimwin = 0.0625. The DFT frequencies in that case are 
 linspace(0,1000,63) such that cfg.foi --> 80.645. In practice, this error
 can only become large if the number of cycles per frequency is very
 small and the frequency is high. For example, suppose that cfg.foi = 80
 and cfg.t_ftimwin = 0.0125. In that case cfg.foi-->83.33.
 The error is smaller as data.fsample is larger.

 Outputs:
   sts is a spike structure, containing new fields:
   sts.fourierspctrm = 1 x nUnits cell-array with dimord spike_lfplabel_freq
   sts.lfplabel      = 1 x nChan cell-array with EEG labels
   sts.freq          = 1 x nFreq frequencies. Note that per default, not
                       all frequencies can be used as we compute the DFT
                       around the spike based on an uneven number of
                       samples. This introduces a slight adjustment of the
                       selected frequencies.

   Note: sts.fourierspctrm can contain NaNs, for example if
   cfg.borderspikes = 'no', or if cfg.rejectsaturation = 'yes', or if the
   trial length was too short for the window desired.

 WHen using multitapering, the phase distortion is corrected for.

 The output STS data structure can be input to FT_SPIKETRIGGEREDSPECTRUM_STAT
```
