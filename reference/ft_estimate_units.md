---
layout: default
---

##  FT_ESTIMATE_UNITS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_estimate_units".

`<html>``<pre>`
    `<a href=/reference/ft_estimate_units>``<font color=green>`FT_ESTIMATE_UNITS`</font>``</a>` tries to determine the units of a geometrical object by
    looking at its size and by relating this to the approximate size of the
    human head according to the following tabl
    from  0.050 to   0.500 -&gt; meter
    from  0.500 to   5.000 -&gt; decimeter
    from  5.000 to  50.000 -&gt; centimeter
    from 50.000 to 500.000 -&gt; millimeter
 
    Use as
    unit = ft_estimate_units(size)
 
    This function will return one of the following strings
    'm'
    'dm'
    'cm'
    'mm'
 
    See also `<a href=/reference/ft_convert_units>``<font color=green>`FT_CONVERT_UNITS`</font>``</a>`
`</pre>``</html>`

