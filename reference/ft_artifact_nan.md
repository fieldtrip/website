---
title: ft_artifact_nan
---
```
 FT_ARTIFACT_NAN identifies artifacts that are indicated in the data as nan (not a
 number) values.

 Use as
   [cfg, artifact] = ft_artifact_nan(cfg, data)
 where the input data is a structure as obtained from FT_REJECTARTIFACT with
 the option cfg.artfctdef.reject='nan'.

 The configuration can contain
   cfg.artfctdef.nan.channel = Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details

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
