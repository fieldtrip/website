---
layout: default
---

##  FT_HEADMODEL_FNS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_headmodel_fns".

`<html>``<pre>`
    `<a href=/reference/ft_headmodel_fns>``<font color=green>`FT_HEADMODEL_FNS`</font>``</a>` creates the volume conduction structure to be used
    in the FNS forward solver.
 
    Use as
    headmodel = ft_headmodel_fns(seg, ...)
 
    Optional input arguments should be specified in key-value pairs and
    can include
    tissuecond       = matrix C [9XN tissue types]; where N is the number of
                       tissues and a 3x3 tensor conductivity matrix is stored
                       in each column.
    tissue           = see fns_contable_write
    tissueval        = match tissues of segmentation input
    transform        = 4x4 transformation matrix (default eye(4))
    sens             = sensor information (for which ft_datatype(sens,'sens')==1)
    deepelec         = used in the case of deep voxel solution
    tolerance        = scalar (default 1e-8)
 
    Standard default values for conductivity matrix C are derived from
    Saleheen HI, Ng KT. New finite difference formulations for general
    inhomogeneous anisotropic bioelectric problems. IEEE Trans Biomed Eng.
    1997
 
    Additional documentation available a
    http://hunghienvn.nmsu.edu/wiki/index.php/FNS
 
    See also `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

