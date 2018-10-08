---
layout: default
---

##  FT_READ_VOL

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_read_vol".

`<html>``<pre>`
    `<a href=/reference/ft_read_vol>``<font color=green>`FT_READ_VOL`</font>``</a>` reads a volume conduction model from various manufacturer
    specific files. Currently supported are ASA, CTF, Neuromag, MBFYS
    and Matlab.
 
    Use as
    headmodel = ft_read_vol(filename, ...)
 
    Additional options should be specified in key-value pairs and can be
    'fileformat'   string
 
    The volume conduction model is represented as a structure with fields
    that depend on the type of model.
 
    See also `<a href=/reference/ft_transform_vol>``<font color=green>`FT_TRANSFORM_VOL`</font>``</a>`, `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_compute_leadfield>``<font color=green>`FT_COMPUTE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

