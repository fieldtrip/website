---
layout: default
---

##  FT_APPENDSENS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_appendsens".

`<html>``<pre>`
    `<a href=/reference/ft_appendsens>``<font color=green>`FT_APPENDSENS`</font>``</a>` concatenates multiple sensor definitions that have been processed
    separately.
 
    Use as
    combined = ft_appendsens(cfg, sens1, sens2, ...)
 
    A call to `<a href=/reference/ft_appendsens>``<font color=green>`FT_APPENDSENS`</font>``</a>` results in the label, pos and ori fields to be
    concatenated, and the tra matrix to be merged. Any duplicates will be removed.
    The labelold and chanposold fields are kept under the condition that they
    are identical across the inputs.
 
    See also `<a href=/reference/ft_electrodeplacement>``<font color=green>`FT_ELECTRODEPLACEMENT`</font>``</a>`, `<a href=/reference/ft_electroderealign>``<font color=green>`FT_ELECTRODEREALIGN`</font>``</a>`, FT_DATAYPE_SENS,
    `<a href=/reference/ft_appenddata>``<font color=green>`FT_APPENDDATA`</font>``</a>`, `<a href=/reference/ft_appendtimelock>``<font color=green>`FT_APPENDTIMELOCK`</font>``</a>`, `<a href=/reference/ft_appendfreq>``<font color=green>`FT_APPENDFREQ`</font>``</a>`, `<a href=/reference/ft_appendsource>``<font color=green>`FT_APPENDSOURCE`</font>``</a>`
`</pre>``</html>`

