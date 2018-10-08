---
layout: default
---

##  FT_STRUCT2SINGLE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_struct2single".

`<html>``<pre>`
    `<a href=/reference/ft_struct2single>``<font color=green>`FT_STRUCT2SINGLE`</font>``</a>` converts all double precision numeric data in a structure
    into single precision, which takes up half the amount of memory compared
    to double precision. It will also convert plain matrices and cell-arrays.
 
    Use as
    x = ft_struct2single(x)
 
    Starting from MATLAB 7.0, you can use single precision data in your
    computations, i.e. you do not have to convert back to double precision.
 
    MATLAB version 6.5 and older only support single precision for storing
    data in memory or on disk, but do not allow computations on single
    precision data. After reading a single precision structure from file, you
    can convert it back with `<a href=/reference/ft_struct2double>``<font color=green>`FT_STRUCT2DOUBLE`</font>``</a>`.
 
    See also `<a href=/reference/ft_struct2double>``<font color=green>`FT_STRUCT2DOUBLE`</font>``</a>`
`</pre>``</html>`

