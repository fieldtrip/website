---
title: ft_spikedetection
---
```
 FT_SPIKEDETECTION reads continuous data from disk and detects spikes. The
 function writes the unsorted spike waveforms to disk in another file.

 Use as
   cfg = ft_spikedetection(cfg)

 The configuration options can contain
   cfg.dataset             = string with the input dataset
   cfg.output              = string with the output dataset (default is determined automatic)
   cfg.dataformat          = string with the output dataset format, see FT_WRITE_FCDC_SPIKE
   cfg.method              = string with the method to use, can be 'all', 'zthresh', 'ztrig', 'flank'
   cfg.interactive         = 'yes' or 'no'
   cfg.timestampdefinition = 'orig' or 'sample'

 The default is to process the full dataset. You can select a latency range with
   cfg.latency          = [begin end], default is [0 inf]
 or you can specify multiple latency segments with
   cfg.latency          = [b1 e1; b2 e2; ...]

 Specific settings for the zthresh spike detection method are
   cfg.zthresh.neg      = negative threshold, e.g. -3
   cfg.zthresh.pos      = positive threshold, e.g.  3
   cfg.zthresh.offset   = number of samples before peak (default = 16)
   cfg.zthresh.mindist  = mininum distance in samples between  detected peaks

 Specific settings for the flank spike detection method are
   cfg.flank.value      = positive or negative threshold
   cfg.flank.offset     = number of samples before peak
   cfg.flank.ztransform = 'yes' or 'no'
   cfg.flank.mindist    = mininum distance in samples between  detected peaks

 Furthermore, the configuration can contain options for preprocessing
   cfg.preproc.lpfilter      = 'no' or 'yes'  lowpass filter
   cfg.preproc.hpfilter      = 'no' or 'yes'  highpass filter
   cfg.preproc.bpfilter      = 'no' or 'yes'  bandpass filter
   cfg.preproc.lnfilter      = 'no' or 'yes'  line noise removal using notch filter
   cfg.preproc.dftfilter     = 'no' or 'yes'  line noise removal using discrete fourier transform
   cfg.preproc.medianfilter  = 'no' or 'yes'  jump preserving median filter
   cfg.preproc.lpfreq        = lowpass  frequency in Hz
   cfg.preproc.hpfreq        = highpass frequency in Hz
   cfg.preproc.bpfreq        = bandpass frequency range, specified as [low high] in Hz
   cfg.preproc.lnfreq        = line noise frequency in Hz, default 50Hz
   cfg.preproc.lpfiltord     = lowpass  filter order
   cfg.preproc.hpfiltord     = highpass filter order
   cfg.preproc.bpfiltord     = bandpass filter order
   cfg.preproc.lnfiltord     = line noise notch filter order
   cfg.preproc.medianfiltord = length of median filter
   cfg.preproc.lpfilttype    = digital filter type, 'but' (default) or 'fir'
   cfg.preproc.hpfilttype    = digital filter type, 'but' (default) or 'fir'
   cfg.preproc.bpfilttype    = digital filter type, 'but' (default) or 'fir'
   cfg.preproc.lpfiltdir     = filter direction, 'twopass' (default) or 'onepass'
   cfg.preproc.hpfiltdir     = filter direction, 'twopass' (default) or 'onepass'
   cfg.preproc.bpfiltdir     = filter direction, 'twopass' (default) or 'onepass'
   cfg.preproc.detrend       = 'no' or 'yes'
   cfg.preproc.demean        = 'no' or 'yes'
   cfg.preproc.baselinewindow = [begin end] in seconds, the default is the complete trial
   cfg.preproc.hilbert       = 'no' or 'yes'
   cfg.preproc.rectify       = 'no' or 'yes'
```
