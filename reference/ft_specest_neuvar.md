---
layout: default
---

##  FT_SPECEST_NEUVAR

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_specest_neuvar".

`<html>``<pre>`
    `<a href=/reference/ft_specest_neuvar>``<font color=green>`FT_SPECEST_NEUVAR`</font>``</a>` computes a time-domain estimation of overall signal 
    power, having compensated for the 1/f distribution of spectral content.
 
    Use as
    [spectrum,ntaper,freqoi] = ft_specest_neuvar(dat,time...)
    where
    dat        = matrix of chan*sample
    time       = vector, containing time in seconds for each sample
    neuvar     = matrix of chan*neuvar
 
    Optional arguments should be specified in key-value pairs and can include
    order      = number, the order of differentation for compensating for the 1/f (default: 1)
    pad        = number, total length of data after zero padding (in seconds)
    padtype    = string, indicating type of padding to be used (see ft_preproc_padding, default: 0)
    verbose    = output progress to console (0 or 1, default 1)
 
    See also `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`, `<a href=/reference/ft_specest_mtmfft>``<font color=green>`FT_SPECEST_MTMFFT`</font>``</a>`, `<a href=/reference/ft_specest_mtmconvol>``<font color=green>`FT_SPECEST_MTMCONVOL`</font>``</a>`, `<a href=/reference/ft_specest_tfr>``<font color=green>`FT_SPECEST_TFR`</font>``</a>`, `<a href=/reference/ft_specest_hilbert>``<font color=green>`FT_SPECEST_HILBERT`</font>``</a>`, `<a href=/reference/ft_specest_wavelet>``<font color=green>`FT_SPECEST_WAVELET`</font>``</a>`
`</pre>``</html>`

