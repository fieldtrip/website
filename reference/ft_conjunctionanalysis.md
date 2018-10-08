---
layout: default
---

##  FT_CONJUNCTIONANALYSIS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_conjunctionanalysis".

`<html>``<pre>`
    `<a href=/reference/ft_conjunctionanalysis>``<font color=green>`FT_CONJUNCTIONANALYSIS`</font>``</a>` finds the minimum statistic common across two or
    more contrasts, i.e. data following ft_xxxstatistics. Furthermore, it
    finds the overlap of sensors/voxels that show statistically significant
    results (a logical AND on the mask fields).
 
    Alternatively, it finds minimalistic mean power values in the
    input datasets. Here, a type 'relative change' baselinecorrection
    prior to conjunction is advised.
 
    Use as
    [stat] = ft_conjunctionanalysis(cfg, stat1, stat2, .., statN)
 
    where the input data is the result from either `<a href=/reference/ft_timelockstatistics>``<font color=green>`FT_TIMELOCKSTATISTICS`</font>``</a>`,
    `<a href=/reference/ft_freqstatistics>``<font color=green>`FT_FREQSTATISTICS`</font>``</a>`, or `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>`
 
    No configuration options are yet implemented.
 
    See also `<a href=/reference/ft_timelockstatistics>``<font color=green>`FT_TIMELOCKSTATISTICS`</font>``</a>`, `<a href=/reference/ft_freqstatistics>``<font color=green>`FT_FREQSTATISTICS`</font>``</a>`, `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>`
`</pre>``</html>`

