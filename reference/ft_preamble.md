---
title: ft_preamble
---
```
 FT_PREAMBLE is a helper function that is included in many of the FieldTrip
 functions and which takes care of some general settings and operations at the
 begin of the function.

 This ft_preamble m-file is a function, but internally it executes a
 number of private scripts in the callers workspace. This allows the
 private script to access the variables in the callers workspace and
 behave as if the script were included as a header file in C-code.

 See also FT_POSTAMBLE
```
