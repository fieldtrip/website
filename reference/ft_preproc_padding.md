---
layout: default
---

##  FT_PREPROC_PADDING

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_preproc_padding".

`<html>``<pre>`
    `<a href=/reference/ft_preproc_padding>``<font color=green>`FT_PREPROC_PADDING`</font>``</a>` performs padding on the data, i.e. adds or removes samples
    to or from the data matrix.
 
    Use as
    [dat] = ft_preproc_padding(dat, padtype, padlength)
    or as
    [dat] = ft_preproc_padding(dat, padtype, prepadlength, postpadlength)
    where
    dat           data matrix (Nchan x Ntime)
    padtype       'zero', 'mean', 'localmean', 'edge', 'mirror', 'nan' or 'remove'
    padlength     scalar, number of samples that will be padded
    prepadlength  scalar, number of samples that will be padded before the data
    postpadlength scalar, number of samples that will be padded after the data
 
    If padlength is used instead of prepadlength and postpadlength, padding
    will be symmetrical (i.e. padlength = prepadlength = postpadlength)
 
    See also `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`
`</pre>``</html>`

