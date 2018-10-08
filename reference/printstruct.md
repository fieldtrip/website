---
layout: default
---

##  PRINTSTRUCT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help printstruct".

`<html>``<pre>`
    `<a href=/reference/printstruct>``<font color=green>`PRINTSTRUCT`</font>``</a>` converts a MATLAB structure into a multi-line string that can be
    interpreted by MATLAB, resulting in the original structure.
 
    Use as
    str = printstruct(val)
    or
    str = printstruct(name, val)
    where "val" is any MATLAB variable, e.g. a scalar, vector, matrix, structure, or
    cell-array. If you pass the name of the variable, the output is a piece of MATLAB code
    that you can execute, i.e. an ASCII serialized representation of the variable.
 
    Example
    a.field1 = 1;
    a.field2 = 2;
    s = printstruct(a)
 
    b = rand(3);
    s = printstruct(b)
 
    s = printstruct('c', randn(10)&gt;0.5)
 
    See also DISP
`</pre>``</html>`

