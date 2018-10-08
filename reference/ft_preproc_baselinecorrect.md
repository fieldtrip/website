---
layout: default
---

##  FT_PREPROC_BASELINECORRECT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_preproc_baselinecorrect".

`<html>``<pre>`
    `<a href=/reference/ft_preproc_baselinecorrect>``<font color=green>`FT_PREPROC_BASELINECORRECT`</font>``</a>` performs a baseline correction, e.g. using the
    prestimulus interval of the data or using the complete data
 
    Use as
    [dat] = ft_preproc_baselinecorrect(dat, begin, end)
    where
    dat        data matrix (Nchans X Ntime)
    begsample  index of the begin sample for the baseline estimate
    endsample  index of the end sample for the baseline estimate
 
    If no begin and end sample are specified for the baseline estimate, it
    will be estimated on the complete data.
 
    See also `<a href=/reference/ft_preproc_detrend>``<font color=green>`FT_PREPROC_DETREND`</font>``</a>`, `<a href=/reference/ft_preproc_polyremoval>``<font color=green>`FT_PREPROC_POLYREMOVAL`</font>``</a>`
`</pre>``</html>`

