---
title: ft_artifact_zvalue
---
```
 FT_ARTIFACT_ZVALUE reads the interesting segments of data from file and identifies
 artifacts by means of thresholding the z-transformed value of the preprocessed raw data.
 Depending on the preprocessing options, this method will be sensitive to EOG, muscle or
 jump artifacts.  This procedure only works on continuously recorded data.

 Use as
   [cfg, artifact] = ft_artifact_zvalue(cfg)
 with the configuration options
   cfg.dataset     = string with the filename
 or
   cfg.headerfile  = string with the filename
   cfg.datafile    = string with the filename
 and optionally
   cfg.headerformat
   cfg.dataformat

 Alternatively you can use it as
   [cfg, artifact] = ft_artifact_zvalue(cfg, data)
 where the input data is a structure as obtained from FT_PREPROCESSING.

 The required configuration settings are:
   cfg.trl         = structure that defines the data segments of interest. See FT_DEFINETRIAL
   cfg.continuous  = 'yes' or 'no' whether the file contains continuous data (default   = 'yes')
 and
   cfg.artfctdef.zvalue.channel
   cfg.artfctdef.zvalue.cutoff
   cfg.artfctdef.zvalue.trlpadding
   cfg.artfctdef.zvalue.fltpadding
   cfg.artfctdef.zvalue.artpadding

 If you encounter difficulties with memory usage, you can use
   cfg.memory = 'low' or 'high', whether to be memory or computationally efficient, respectively (default = 'high')

 The optional configuration settings (see below) are:
   cfg.artfctdef.zvalue.artfctpeak  = 'yes' or 'no'
   cfg.artfctdef.zvalue.interactive = 'yes' or 'no'

 If you specify cfg.artfctdef.zvalue.artfctpeak='yes', the maximum value of the
 artifact within its range will be found and saved into cfg.artfctdef.zvalue.peaks.

 If you specify cfg.artfctdef.zvalue.interactive='yes', a GUI will be started and
 you can manually accept/reject detected artifacts, and/or change the threshold. To
 control the graphical interface via keyboard, use the following keys:

     q                 : Stop

     comma             : Step to the previous artifact trial
     a                 : Specify artifact trial to display
     period            : Step to the next artifact trial

     x                 : Step 10 trials back
     leftarrow         : Step to the previous trial
     t                 : Specify trial to display
     rightarrow        : Step to the next trial
     c                 : Step 10 trials forward

     k                 : Keep trial
     space             : Mark complete trial as artifact
     r                 : Mark part of trial as artifact

     downarrow         : Shift the z-threshold down
     z                 : Specify the z-threshold
     uparrow           : Shift the z-threshold down

 Use also, e.g. as input to DSS option of ft_componentanalysis
 cfg.artfctdef.zvalue.artfctpeakrange=[-0.25 0.25], for example to indicate range
 around peak to include, saved into cfg.artfctdef.zvalue.dssartifact. The default is
 [0 0]. Range will respect trial boundaries (i.e. be shorter if peak is near
 beginning or end of trial). Samples between trials will be removed; thus this won't
 match .sampleinfo of the data structure.

 Configuration settings related to the preprocessing of the data are
   cfg.artfctdef.zvalue.lpfilter      = 'no' or 'yes'  lowpass filter
   cfg.artfctdef.zvalue.hpfilter      = 'no' or 'yes'  highpass filter
   cfg.artfctdef.zvalue.bpfilter      = 'no' or 'yes'  bandpass filter
   cfg.artfctdef.zvalue.bsfilter      = 'no' or 'yes'  bandstop filter for line noise removal
   cfg.artfctdef.zvalue.dftfilter     = 'no' or 'yes'  line noise removal using discrete fourier transform
   cfg.artfctdef.zvalue.medianfilter  = 'no' or 'yes'  jump preserving median filter
   cfg.artfctdef.zvalue.lpfreq        = lowpass  frequency in Hz
   cfg.artfctdef.zvalue.hpfreq        = highpass frequency in Hz
   cfg.artfctdef.zvalue.bpfreq        = bandpass frequency range, specified as [low high] in Hz
   cfg.artfctdef.zvalue.bsfreq        = bandstop frequency range, specified as [low high] in Hz
   cfg.artfctdef.zvalue.lpfiltord     = lowpass  filter order
   cfg.artfctdef.zvalue.hpfiltord     = highpass filter order
   cfg.artfctdef.zvalue.bpfiltord     = bandpass filter order
   cfg.artfctdef.zvalue.bsfiltord     = bandstop filter order
   cfg.artfctdef.zvalue.medianfiltord = length of median filter
   cfg.artfctdef.zvalue.lpfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'
   cfg.artfctdef.zvalue.hpfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'
   cfg.artfctdef.zvalue.bpfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'
   cfg.artfctdef.zvalue.bsfilttype    = digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'
   cfg.artfctdef.zvalue.detrend       = 'no' or 'yes'
   cfg.artfctdef.zvalue.demean        = 'no' or 'yes'
   cfg.artfctdef.zvalue.baselinewindow = [begin end] in seconds, the default is the complete trial
   cfg.artfctdef.zvalue.hilbert       = 'no' or 'yes'
   cfg.artfctdef.zvalue.rectify       = 'no' or 'yes'

 The output argument "artifact" is a Nx2 matrix comparable to the
 "trl" matrix of FT_DEFINETRIAL. The first column of which specifying the
 beginsamples of an artifact period, the second column contains the
 endsamples of the artifactperiods.

 See also FT_REJECTARTIFACT, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG, FT_ARTIFACT_EOG,
 FT_ARTIFACT_JUMP, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_ZVALUE
```
