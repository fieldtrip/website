---
layout: default
---

##  FT_SOURCEDEPTH

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_sourcedepth".

`<html>``<pre>`
    `<a href=/reference/ft_sourcedepth>``<font color=green>`FT_SOURCEDEPTH`</font>``</a>` computes the distance from the source to the surface of
    the source compartment (usually the brain) in the volume conduction model.
 
    Use as
    depth = ft_sourcedepth(dippos, headmodel);
    where
    dippos    =  Nx3 matrix with the position of N sources
    headmodel =  structure describing volume condition model
 
    A negative depth indicates that the source is inside the source
    compartment, positive indicates outside.
 
    See also FIND_INSIDE_VOL
`</pre>``</html>`

