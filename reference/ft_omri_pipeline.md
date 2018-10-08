---
layout: default
---

##  FT_OMRI_PIPELINE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_omri_pipeline".

`<html>``<pre>`
    `<a href=/reference/ft_omri_pipeline>``<font color=green>`FT_OMRI_PIPELINE`</font>``</a>` implements an online fMRI pre-processing pipeline
 
    Use as
    ft_omri_pipeline(cfg)
    where cfg is a structure with configuration settings.
 
    Configuration options are
    cfg.input            = FieldTrip buffer containing raw scans (default 'buffer://localhost:1972')
    cfg.output           = where to write processed scans to     (default 'buffer://localhost:1973')
    cfg.numDummy         = how many scans to ignore initially    (default 0)
    cfg.smoothFWHM       = kernel width in mm (Full Width Half Maximum) for smoothing (default = 0 =&gt; no smoothing)
    cfg.correctMotion 	 = flag indicating whether to correct motion artifacts (default = 1 = yes)
    cfg.correctSliceTime = flag indicating whether to correct slice timing (default = 1 = yes)
`</pre>``</html>`

