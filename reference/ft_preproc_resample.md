---
layout: default
---

##  FT_PREPROC_RESAMPLE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_preproc_resample".

`<html>``<pre>`
    `<a href=/reference/ft_preproc_resample>``<font color=green>`FT_PREPROC_RESAMPLE`</font>``</a>` resamples all channels in the data matrix
 
    Use as
    dat = ft_preproc_resample(dat, Fold, Fnew, method)
    where
    dat    = matrix with the input data (Nchans X Nsamples)
    Fold   = scalar, original sampling frequency in Hz
    Fnew   = scalar, desired sampling frequency in Hz
    method = string, can be 'resample', 'decimate', 'downsample', 'fft'
 
    The resample method applies an anti-aliasing (lowpass) FIR filter to
    the data during the resampling process, and compensates for the filter's
    delay. For the other two methods you should apply an anti-aliassing
    filter prior to calling this function.
 
    See also PREPROC, `<a href=/reference/ft_preproc_lowpassfilter>``<font color=green>`FT_PREPROC_LOWPASSFILTER`</font>``</a>`
`</pre>``</html>`

