---
layout: default
---

##  FT_APPENDSOURCE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_appendsource".

`<html>``<pre>`
    `<a href=/reference/ft_appendsource>``<font color=green>`FT_APPENDSOURCE`</font>``</a>` concatenates multiple volumetric source reconstruction data
    structures that have been processed seperately.
 
    If the source reconstructions were computed for different ROIs or different slabs
    of a regular 3D grid (as indicated by the source positions), the data will be
    concatenated along the spatial dimension.
 
    If the source reconstructions were computed on the same source positions, but for
    different frequencies and/or latencies, e.g. for time-frequency spectrally
    decomposed data, the data will be concatenared along the frequency and/or time
    dimension.
 
    Use as
    combined = ft_appendsource(cfg, source1, source2, ...)
 
    See also `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, `<a href=/reference/ft_datatype_source>``<font color=green>`FT_DATATYPE_SOURCE`</font>``</a>`, `<a href=/reference/ft_appenddata>``<font color=green>`FT_APPENDDATA`</font>``</a>`, T_APPENDTIMELOCK,
    `<a href=/reference/ft_appendfreq>``<font color=green>`FT_APPENDFREQ`</font>``</a>`
`</pre>``</html>`

