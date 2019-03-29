---
title: ft_write_sens
---
```
 FT_WRITE_SENS writes electrode information to an external file for further processing in external software.

 Use as
  ft_write_sens(filename, sens, ...)

 The specified filename can already contain the filename extention,
 but that is not required since it will be added automatically.

 Additional options should be specified in key-value pairs and can be
   'format'     string, see below

 The supported file formats are
   bioimage_mgrid

 See also FT_READ_SENS, FT_DATATYPE_SENS
```
