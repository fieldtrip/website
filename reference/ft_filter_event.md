---
layout: default
---

##  FT_FILTER_EVENT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_filter_event".

`<html>``<pre>`
    `<a href=/reference/ft_filter_event>``<font color=green>`FT_FILTER_EVENT`</font>``</a>` does what its name implies
 
    Use as
    event = ft_filter_event(event, ...)
 
    The optional arguments should come in key-value pairs and determine the
    filter characteristic
    type         = cell-array with strings
    value        = numeric array
    sample       = numeric array
    timestamp    = numeric array
    offset       = numeric array
    duration     = numeric array
    minsample    = value
    maxsample    = value
    minduration  = value
    maxduration  = value
    mintimestamp = value
    maxtimestamp = value
    minnumber    = value, applies only if event.number is present
    maxnmumber   = value, applies only if event.number is present
 
    See also `<a href=/reference/ft_read_event>``<font color=green>`FT_READ_EVENT`</font>``</a>`, `<a href=/reference/ft_write_event>``<font color=green>`FT_WRITE_EVENT`</font>``</a>`
`</pre>``</html>`

