---
title: ft_omri_pipeline
---
```
 FT_OMRI_PIPELINE implements an online fMRI pre-processing pipeline

 Use as
   ft_omri_pipeline(cfg)
 where cfg is a structure with configuration settings.

 Configuration options are
   cfg.input            = FieldTrip buffer containing raw scans (default 'buffer://localhost:1972')
   cfg.output           = where to write processed scans to     (default 'buffer://localhost:1973')
   cfg.numDummy         = how many scans to ignore initially    (default 0)
   cfg.smoothFWHM       = kernel width in mm (Full Width Half Maximum) for smoothing (default = 0 => no smoothing)
   cfg.correctMotion 	 = flag indicating whether to correct motion artifacts (default = 1 = yes)
   cfg.correctSliceTime = flag indicating whether to correct slice timing (default = 1 = yes)
```
