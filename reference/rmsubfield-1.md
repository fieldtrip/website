---
title: rmsubfield
---
```
 RMSUBFIELD removes the contents of the specified field from a structure
 just like the standard Matlab RMFIELD function, except that you can also
 specify nested fields using a '.' in the fieldname. The nesting can be
 arbitrary deep.

 Use as
   s = rmsubfield(s, 'fieldname')
 or as
   s = rmsubfield(s, 'fieldname.subfieldname')

 See also SETFIELD, GETSUBFIELD, ISSUBFIELD
```
