---
layout: default
---

##  SETSUBFIELD

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help setsubfield".

`<html>``<pre>`
    `<a href=/reference/setsubfield>``<font color=green>`SETSUBFIELD`</font>``</a>` sets the contents of the specified field to a specified value
    just like the standard Matlab SETFIELD function, except that you can also
    specify nested fields using a '.' in the fieldname. The nesting can be
    arbitrary deep.
 
    Use as
    s = setsubfield(s, 'fieldname', value)
    or as
    s = setsubfield(s, 'fieldname.subfieldname', value)
 
    where nested is a logical, false denoting that setsubfield will create
    s.subfieldname instead of s.fieldname.subfieldname
 
    See also SETFIELD, `<a href=/reference/getsubfield>``<font color=green>`GETSUBFIELD`</font>``</a>`, `<a href=/reference/issubfield>``<font color=green>`ISSUBFIELD`</font>``</a>`
`</pre>``</html>`

