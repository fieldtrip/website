---
layout: default
---

##  FT_PREPARE_MONTAGE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_prepare_montage".

`<html>``<pre>`
    `<a href=/reference/ft_prepare_montage>``<font color=green>`FT_PREPARE_MONTAGE`</font>``</a>` creates a referencing scheme based on the input configuration
    options and the channels in the data structure. The resulting montage can be
    given as input to `<a href=/reference/ft_apply_montage>``<font color=green>`FT_APPLY_MONTAGE`</font>``</a>`, or as cfg.montage to `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    Use as
    montage = ft_prepare_montage(cfg, data)
 
    The configuration can contain the following field
    cfg.refmethod     = 'avg', 'bioloar', 'comp' (default = 'avg')
    cfg.implicitref   = string with the label of the implicit reference, or empty (default = [])
    cfg.refchannel    = cell-array with new EEG reference channel(s), this can be 'all' for a common average reference
 
    The implicitref option allows adding the implicit reference channel to the data as
    a channel with zeros.
 
    See also `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`, `<a href=/reference/ft_apply_montage>``<font color=green>`FT_APPLY_MONTAGE`</font>``</a>`
`</pre>``</html>`

