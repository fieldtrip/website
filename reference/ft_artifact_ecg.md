---
title: ft_artifact_ecg
---
```
 FT_ARTIFACT_ECG performs a peak-detection on the ECG-channel and identifies the
 windows around the QRS peak as artifacts. Using FT_REJECTARTIFACT you can remove
 these windows from your data, or using FT_REMOVETEMPLATEARTIFACT you can subtract
 an averaged template artifact from your data.

 Use as
   [cfg, artifact] = ft_artifact_ecg(cfg)
 with the configuration options
   cfg.dataset     = string with the filename
 or
   cfg.headerfile  = string with the filename
   cfg.datafile    = string with the filename
 and optionally
   cfg.headerformat
   cfg.dataformat

 Alternatively you can use it as
   [cfg, artifact] = ft_artifact_ecg(cfg, data)
 where the input data is a structure as obtained from FT_PREPROCESSING.

 In both cases the configuration should also contain
   cfg.trl        = structure that defines the data segments of interest. See FT_DEFINETRIAL
   cfg.continuous = 'yes' or 'no' whether the file contains continuous data
 and
   cfg.artfctdef.ecg.channel = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details
   cfg.artfctdef.ecg.pretim  = 0.05; pre-artifact rejection-interval in seconds
   cfg.artfctdef.ecg.psttim  = 0.3;  post-artifact rejection-interval in seconds
   cfg.artfctdef.ecg.method  = 'zvalue'; peak-detection method
   cfg.artfctdef.ecg.cutoff  = 3; peak-threshold
   cfg.artfctdef.ecg.inspect = Nx1 list of channels which will be shown in a QRS-locked average

 The output argument "artifact" is a Nx2 matrix comparable to the
 "trl" matrix of FT_DEFINETRIAL. The first column of which specifying the
 beginsamples of an artifact period, the second column contains the
 endsamples of the artifactperiods.

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
 If you specify this option the input data will be read from a *.mat
 file on disk. This mat files should contain only a single variable named 'data',
 corresponding to the input structure.

 See also FT_REJECTARTIFACT, FT_REMOVETEMPLATEARTIFACT, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG,
 FT_ARTIFACT_EOG, FT_ARTIFACT_JUMP, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_THRESHOLD,
 FT_ARTIFACT_ZVALUE
```
