---
layout: default
---

##  FT_CONNECTIVITY_CANCORR

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_connectivity_cancorr".

`<html>``<pre>`
    `<a href=/reference/ft_connectivity_cancorr>``<font color=green>`FT_CONNECTIVITY_CANCORR`</font>``</a>` computes the canonical correlation or coherence between
    multiple variables. Canonical correlation analysis (CCA) is a way of measuring the
    linear relationship between two multidimensional variables. It finds two bases, one
    for each variable, that are optimal with respect to correlations and, at the same
    time, it finds the corresponding correlations.
 
    Use as
    [px, py, wx, wy] = ft_connectivity_cancorr(C, x, y, ...)
    
    The input data C represents the Nchan*Nchan covariance or cross-spectral density
    matrix, and x and y specify the indices to the cross-spectral density making up the
    dependent and independent variable
 
    See also `<a href=/reference/ft_connectivityanalysis>``<font color=green>`FT_CONNECTIVITYANALYSIS`</font>``</a>`
`</pre>``</html>`

