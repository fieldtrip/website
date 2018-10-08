---
layout: default
---

##  FT_HEADMODEL_LOCALSPHERES

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_headmodel_localspheres".

`<html>``<pre>`
    `<a href=/reference/ft_headmodel_localspheres>``<font color=green>`FT_HEADMODEL_LOCALSPHERES`</font>``</a>` constructs a MEG volume conduction model in
    with a local sphere fitted to the head or brain surface for each separate
    channel
 
    This implements
    Huang MX, Mosher JC, Leahy RM. "A sensor-weighted overlapping-sphere
    head model and exhaustive head model comparison for MEG." Phys Med
    Biol. 1999 Feb;44(2):423-40
 
    Use as
    headmodel = ft_headmodel_localspheres(mesh, grad, ...)
 
    Optional arguments should be specified in key-value pairs and can include
    radius    = number, radius of sphere within which headshape points will
                be included for the fitting algorithm
    maxradius = number, if for a given sensor the fitted radius exceeds
                this value, the radius and origin will be replaced with the
                single sphere fit
    baseline  = number
    feedback  = boolean, true or false
 
    See also `<a href=/reference/ft_prepare_headmodel>``<font color=green>`FT_PREPARE_HEADMODEL`</font>``</a>`, `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

