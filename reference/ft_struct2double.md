---
layout: default
---

##  FT_STRUCT2DOUBLE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_struct2double".

`<html>``<pre>`
    `<a href=/reference/ft_struct2double>``<font color=green>`FT_STRUCT2DOUBLE`</font>``</a>` converts all single precision numeric data in a structure
    into double precision. It will also convert plain matrices and
    cell-arrays.
 
    Use as
    x = ft_struct2double(x)
 
    Starting from MATLAB 7.0, you can use single precision data in your
    computations, i.e. you do not have to convert back to double precision.
 
    MATLAB version 6.5 and older only support single precision for storing
    data in memory or on disk, but do not allow computations on single
    precision data. Therefore you should converted your data from single to
    double precision after reading from file.
 
    See also `<a href=/reference/ft_struct2single>``<font color=green>`FT_STRUCT2SINGLE`</font>``</a>`
`</pre>``</html>`

