---
layout: default
---

##  FT_OMRI_SLICE_TIME_APPLY

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_omri_slice_time_apply".

`<html>``<pre>`
    function [STM, Xs] = ft_omri_slice_time_apply(STM, X)
 
    Put new scan X through slice time correction, by linear interpolation
    with last scan. The return value Xs is the signal sampled at deltaT = 0
    relative to the most recent scan.
`</pre>``</html>`

