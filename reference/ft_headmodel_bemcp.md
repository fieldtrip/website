---
layout: default
---

##  FT_HEADMODEL_BEMCP

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_headmodel_bemcp".

`<html>``<pre>`
    `<a href=/reference/ft_headmodel_bemcp>``<font color=green>`FT_HEADMODEL_BEMCP`</font>``</a>` creates a volume conduction model of the head
    using the boundary element method (BEM) for EEG. This function
    takes as input the triangulated surfaces that describe the boundaries
    and returns as output a volume conduction model which can be used
    to compute leadfields.
 
    The implementation of this function is based on Christophe Phillips'
    MATLAB code, hence the name "bemcp".
 
    Use as
    headmodel = ft_headmodel_bemcp(mesh, ...)
 
    See also `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

