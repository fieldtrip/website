---
layout: default
---

##  EDF2FIELDTRIP

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help edf2fieldtrip".

`<html>``<pre>`
    `<a href=/reference/edf2fieldtrip>``<font color=green>`EDF2FIELDTRIP`</font>``</a>` reads data from a EDF file with channels that have a different
    sampling rates. It upsamples all data to the highest sampling rate and
    concatenates all channels into a raw data structure that is compatible with the
    output of `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    Use as
    data = edf2fieldtrip(filename);
 
    For reading EDF files in which all channels have the same sampling rate, you can
    use the standard procedure with `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>` and `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
 
    See also `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`, `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>`, `<a href=/reference/ft_redefinetrial>``<font color=green>`FT_REDEFINETRIAL`</font>``</a>`
`</pre>``</html>`

