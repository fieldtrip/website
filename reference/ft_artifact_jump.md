---
title: ft_artifact_jump
---
```
 FT_ARTIFACT_JUMP reads the data segments of interest from file and identifies
 SQUID jump artifacts.

 Use as
   [cfg, artifact] = ft_artifact_jump(cfg)
 with the configuration options
   cfg.dataset     = string with the filename
 or
   cfg.headerfile  = string with the filename
   cfg.datafile    = string with the filename
 and optionally
   cfg.headerformat
   cfg.dataformat

 Alternatively you can use it as
   [cfg, artifact] = ft_artifact_jump(cfg, data)
 where the input data is a structure as obtained from FT_PREPROCESSING.

 In both cases the configuration should also contain
   cfg.trl        = structure that defines the data segments of interest. See FT_DEFINETRIAL
   cfg.continuous = 'yes' or 'no' whether the file contains continuous data

 The data is preprocessed (again) with the following configuration parameters,
 which are optimal for identifying jump artifacts.
   cfg.artfctdef.jump.medianfilter  = 'yes'
   cfg.artfctdef.jump.medianfiltord = 9
   cfg.artfctdef.jump.absdiff       = 'yes'

 Artifacts are identified by means of thresholding the z-transformed value
 of the preprocessed data.
   cfg.artfctdef.jump.channel       = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details
   cfg.artfctdef.jump.cutoff        = z-value at which to threshold (default = 20)
   cfg.artfctdef.jump.trlpadding    = automatically determined based on the filter padding (cfg.padding)
   cfg.artfctdef.jump.artpadding    = automatically determined based on the filter padding (cfg.padding)

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
