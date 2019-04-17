---
title: getsubfield
---
```
 GETSUBFIELD returns a field from a structure just like the standard
 GETFIELD function, except that you can also specify nested fields
 using a '.' in the fieldname. The nesting can be arbitrary deep.

 Use as
   f = getsubfield(s, 'fieldname')
 or as
   f = getsubfield(s, 'fieldname.subfieldname')

 See also GETFIELD, ISSUBFIELD, SETSUBFIELD
```
