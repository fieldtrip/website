---
layout: default
---

##  FT_STATFUN_MEAN

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_statfun_mean".

`<html>``<pre>`
    `<a href=/reference/ft_statfun_mean>``<font color=green>`FT_STATFUN_MEAN`</font>``</a>` computes the mean over all replications for each of the
    observations (i.e. channel-time-frequency points or voxels).
 
    This function does not depend on the experimental design and cannot be used for any
    statistical testing. However, it serves as example how you can use the statistical
    framework in FieldTrip to perform a simple (or more complex) task, without having
    to worry about the representation of the data. The output of `<a href=/reference/ft_timelockstatistics>``<font color=green>`FT_TIMELOCKSTATISTICS`</font>``</a>`,
    `<a href=/reference/ft_freqstatistics>``<font color=green>`FT_FREQSTATISTICS`</font>``</a>` or `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>` will be an appropriate structure, that
    contains the result of the computation inside this function in the stat field.
 
    See also `<a href=/reference/ft_statfun_diff>``<font color=green>`FT_STATFUN_DIFF`</font>``</a>` for another example statfun
`</pre>``</html>`

