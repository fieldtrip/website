---
layout: default
---

##  FT_AVERAGE_SENS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_average_sens".

`<html>``<pre>`
    `<a href=/reference/ft_average_sens>``<font color=green>`FT_AVERAGE_SENS`</font>``</a>` computes average sensor array from a series of input
    arrays. Corresponding average fiducials can also be computed (optional)
 
    Use as
    [asens, afid] = ft_average_sens(sens)
    where sens is a 1xN structure array containing N sensor arrays
 
    Additional options should be specified in key-value pairs and can be
    'weights'    a vector of weights (will be normalized to sum==1)
    'fiducials'  optional structure array of headshapes
 
    See also `<a href=/reference/ft_read_sens>``<font color=green>`FT_READ_SENS`</font>``</a>`, `<a href=/reference/ft_prepare_vol_sens>``<font color=green>`FT_PREPARE_VOL_SENS`</font>``</a>`, `<a href=/reference/ft_transform_sens>``<font color=green>`FT_TRANSFORM_SENS`</font>``</a>`
`</pre>``</html>`

