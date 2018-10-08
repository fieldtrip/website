---
layout: default
---

##  RMSUBFIELD

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help rmsubfield".

`<html>``<pre>`
    `<a href=/reference/rmsubfield>``<font color=green>`RMSUBFIELD`</font>``</a>` removes the contents of the specified field from a structure
    just like the standard Matlab RMFIELD function, except that you can also
    specify nested fields using a '.' in the fieldname. The nesting can be
    arbitrary deep.
 
    Use as
    s = rmsubfield(s, 'fieldname')
    or as
    s = rmsubfield(s, 'fieldname.subfieldname')
 
    See also SETFIELD, `<a href=/reference/getsubfield>``<font color=green>`GETSUBFIELD`</font>``</a>`, `<a href=/reference/issubfield>``<font color=green>`ISSUBFIELD`</font>``</a>`
`</pre>``</html>`

