---
layout: default
---

##  FT_PREPROC_SMOOTH

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_preproc_smooth".

`<html>``<pre>`
    `<a href=/reference/ft_preproc_smooth>``<font color=green>`FT_PREPROC_SMOOTH`</font>``</a>` performs boxcar smoothing with specified length.
    Edge behavior is improved by implicit padding with the mean over
    half the boxcar length at the edges of the data segment.
 
    Use as
    datsmooth = ft_preproc_smooth(dat, n)
 
    Where dat is an Nchan x Ntimepoints data matrix, and n the length
    of the boxcar smoothing kernel
`</pre>``</html>`

