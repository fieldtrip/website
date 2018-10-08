---
layout: default
---

##  FT_INSIDE_VOL

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_inside_vol".

`<html>``<pre>`
    `<a href=/reference/ft_inside_vol>``<font color=green>`FT_INSIDE_VOL`</font>``</a>` locates dipole locations inside/outside the source
    compartment of a volume conductor model.
 
    Use as
    [inside] = ft_inside_vol(dippos, headmodel, ...)
 
    The input should be
    dippos      = Nx3 matrix with dipole positions
    headmodel   = structure with volume conductor model
    and the output is
    inside      = boolean vector indicating for each dipole wether it is inside the source compartment
 
    Additional optional input arguments should be given in key value pairs and can include
    inwardshift = number
    grad        = structure with gradiometer information, used for localspheres
    headshape   = structure with headshape, used for old CTF localspheres strategy
`</pre>``</html>`

