---
layout: default
---

##  FT_PREPROC_DETREND

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_preproc_detrend".

`<html>``<pre>`
    `<a href=/reference/ft_preproc_detrend>``<font color=green>`FT_PREPROC_DETREND`</font>``</a>` removes mean and linear trend from the
    data using using a General Linear Modeling approach.
 
    Use as
    [dat] = ft_preproc_detrend(dat, begin, end)
    where
    dat        = data matrix (Nchans X Ntime)
    begsample  = index of the begin sample for the trend estimate
    endsample  = index of the end sample for the trend estimate
 
    If no begin and end sample are specified for the trend estimate, it
    will be estimated on the complete data.
 
    See also `<a href=/reference/ft_preproc_baselinecorrect>``<font color=green>`FT_PREPROC_BASELINECORRECT`</font>``</a>`, `<a href=/reference/ft_preproc_polyremoval>``<font color=green>`FT_PREPROC_POLYREMOVAL`</font>``</a>`
`</pre>``</html>`

