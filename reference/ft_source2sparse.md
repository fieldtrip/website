---
layout: default
---

##  FT_SOURCE2SPARSE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_source2sparse".

`<html>``<pre>`
    `<a href=/reference/ft_source2sparse>``<font color=green>`FT_SOURCE2SPARSE`</font>``</a>` removes the grid locations outside the brain from the source 
    reconstruction, thereby saving memory.
 
    This invalidates the fields that describe the grid, and also makes it
    more difficult to make a plot of each of the slices of the source volume.
    The original source structure can be recreated using `<a href=/reference/ft_source2full>``<font color=green>`FT_SOURCE2FULL`</font>``</a>`.
 
    Use as
    [source] = ft_source2sparse(source)
 
    See also `<a href=/reference/ft_source2full>``<font color=green>`FT_SOURCE2FULL`</font>``</a>`
`</pre>``</html>`

