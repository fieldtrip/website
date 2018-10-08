---
layout: default
---

##  FT_HEADMODEL_SINGLESPHERE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_headmodel_singlesphere".

`<html>``<pre>`
    `<a href=/reference/ft_headmodel_singlesphere>``<font color=green>`FT_HEADMODEL_SINGLESPHERE`</font>``</a>` creates a volume conduction model of the
    head by fitting a spherical model to a set of points that describe
    the head surface.
 
    For MEG this implements Cuffin BN, Cohen D.  "Magnetic fields of
    a dipole in special volume conductor shapes" IEEE Trans Biomed Eng.
    1977 Jul;24(4):372-81.
 
    Use as
    headmodel = ft_headmodel_singlesphere(mesh, ...)
 
    Optional arguments should be specified in key-value pairs and can include
    conductivity     = number, conductivity of the sphere
 
    See also `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

