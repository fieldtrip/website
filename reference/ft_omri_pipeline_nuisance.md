---
title: ft_omri_pipeline_nuisance
---
```
 FT_OMRI_PIPELINE_NUISANCE implements an online fMRI pre-processing pipeline, including
 motion correction, slice time correction, smoothing, and regressing out nuisance
 regressors (constant, linear trend, motion estimates).
 
 Use as
   ft_omri_pipeline_nuisance(cfg)
 where cfg is a structure with configuration settings.

 Configuration options are
   cfg.input            = FieldTrip buffer containing raw scans (default 'buffer://localhost:1972')
   cfg.output           = where to write processed scans to     (default 'buffer://localhost:1973')
   cfg.numDummy         = how many scans to ignore initially    (default 4)
   cfg.smoothFWHM       = kernel width in mm (Full Width Half Maximum) for smoothing (default = 8)
   cfg.whichEcho        = which echo to process for multi-echo sequences (default = 1)
   cfg.correctMotion 	 = flag indicating whether to correct motion artifacts (default = 1 = yes)
   cfg.correctSliceTime = flag indicating whether to correct slice timing (default = 1 = yes)
   cfg.numRegr          = number of nuisance regressors (1=constant term, 2=const+linear,5=const,linear+translation)
```
