---
layout: default
---

##  FT_GETOPT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_getopt".

`<html>``<pre>`
    `<a href=/reference/ft_getopt>``<font color=green>`FT_GETOPT`</font>``</a>` gets the value of a specified option from a configuration structure
    or from a cell-array with key-value pairs.
 
    Use as
    val = ft_getopt(s, key, default, emptymeaningful)
    where the input values are
    s               = structure or cell-array
    key             = string
    default         = any valid MATLAB data type (optional, default = [])
    emptymeaningful = boolean value (optional, default = 0)
 
    If the key is present as field in the structure, or as key-value pair in the
    cell-array, the corresponding value will be returned.
 
    If the key is not present, ft_getopt will return the default, or an empty array
    when no default was specified.
 
    If the key is present but has an empty value, then the emptymeaningful flag
    specifies whether the empty value or the default value should be returned.
    If emptymeaningful==true, then the empty array will be returned.
    If emptymeaningful==false, then the specified default will be returned.
 
    See also `<a href=/reference/ft_setopt>``<font color=green>`FT_SETOPT`</font>``</a>`, `<a href=/reference/ft_checkopt>``<font color=green>`FT_CHECKOPT`</font>``</a>`
`</pre>``</html>`

