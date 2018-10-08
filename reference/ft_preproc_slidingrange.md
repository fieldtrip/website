---
layout: default
---

##  FT_PREPROC_SLIDINGRANGE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_preproc_slidingrange".

`<html>``<pre>`
    `<a href=/reference/ft_preproc_slidingrange>``<font color=green>`FT_PREPROC_SLIDINGRANGE`</font>``</a>` computes the range of the data in a sliding time
    window of the width specified. Width should be an odd number (since the
    window needs to be centered on an individual sample).
 
    Use as
    y = ft_preproc_slidingrange(dat, width, ...)
 
    Optional key-value pair arguments ar
    'normalize', whether to normalize the range of the data with the square
                 root of the window size
`</pre>``</html>`

