---
title: ft_artifact_clip
---
```
 FT_ARTIFACT_CLIP scans the data segments of interest for channels that clip. These
 artifacts are detected by the signal being completely flat for a given amount of
 time.

 Use as
   [cfg, artifact] = ft_artifact_clip(cfg)
 with the configuration options
   cfg.dataset     = string with the filename
 or
   cfg.headerfile  = string with the filename
   cfg.datafile    = string with the filename
 and optionally
   cfg.headerformat
   cfg.dataformat

 Alternatively you can use it as
   [cfg, artifact] = ft_artifact_clip(cfg, data)
 where the input data is a structure as obtained from FT_PREPROCESSING.

 In both cases the configuration should also contain
   cfg.artfctdef.clip.channel       = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details
   cfg.artfctdef.clip.pretim        = 0.000;  pre-artifact rejection-interval in seconds
   cfg.artfctdef.clip.psttim        = 0.000;  post-artifact rejection-interval in seconds
   cfg.artfctdef.clip.timethreshold = number, minimum duration in seconds of a datasegment with consecutive identical samples to be considered as 'clipped'
   cfg.artfctdef.clip.amplthreshold = number, minimum amplitude difference in consecutive samples to be considered as 'clipped' (default = 0)
                                      string, percent of the amplitude range considered as 'clipped' (i.e. '1%')
   cfg.continuous                   = 'yes' or 'no' whether the file contains continuous data

 The output argument "artifact" is a Nx2 matrix comparable to the
 "trl" matrix of FT_DEFINETRIAL. The first column of which specifying the
 beginsamples of an artifact period, the second column contains the
 endsamples of the artifactperiods.

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
 If you specify this option the input data will be read from a *.mat
 file on disk. This mat files should contain only a single variable named 'data',
 corresponding to the input structure.

 See also FT_REJECTARTIFACT, FT_ARTIFACT_CLIP, FT_ARTIFACT_ECG, FT_ARTIFACT_EOG,
 FT_ARTIFACT_JUMP, FT_ARTIFACT_MUSCLE, FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_ZVALUE
```
