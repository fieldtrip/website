---
layout: default
---

##  FT_PREPROC_MEDIANFILTER

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_preproc_medianfilter".

`<html>``<pre>`
    `<a href=/reference/ft_preproc_medianfilter>``<font color=green>`FT_PREPROC_MEDIANFILTER`</font>``</a>` applies a median filter, which smooths the data with a
    boxcar-like kernel, except that it keeps steps in the data. This function requires
    the MATLAB Signal Processing toolbox.
 
    Use as
    [dat] = ft_preproc_medianfilter(dat, order)
    where
    dat        data matrix (Nchans X Ntime)
    order      number, the length of the median filter kernel (default = 25)
 
    See also PREPROC
`</pre>``</html>`

