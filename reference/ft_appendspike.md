---
layout: default
---

##  FT_APPENDSPIKE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_appendspike".

`<html>``<pre>`
    `<a href=/reference/ft_appendspike>``<font color=green>`FT_APPENDSPIKE`</font>``</a>` combines continuous data (i.e. LFP) with point-process data
    (i.e. spikes) into a single large dataset. For each spike channel an
    additional continuos channel is inserted in the data that contains
    zeros most of the time, and an occasional one at the samples at which a
    spike occurred. The continuous and spike data are linked together using
    the timestamps.
 
    Use as
    [spike] = ft_appendspike(cfg, spike1, spike2, spike3, ...)
    where the input structures come from `<a href=/reference/ft_read_spike>``<font color=green>`FT_READ_SPIKE`</font>``</a>`, or as
    [data]  = ft_appendspike(cfg, data, spike1, spike2, ...)
    where the first data structure is the result of `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`
    and the subsequent ones come from `<a href=/reference/ft_read_spike>``<font color=green>`FT_READ_SPIKE`</font>``</a>`.
 
    See also `<a href=/reference/ft_appenddata>``<font color=green>`FT_APPENDDATA`</font>``</a>`, `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`
`</pre>``</html>`

