---
title: printstruct
---
```
 PRINTSTRUCT converts a MATLAB structure into a multiple-line string that, when
 evaluated by MATLAB, results in the original structure. It also works for most
 other standard MATLAB classes, such as numbers, vectors, matrices, and cell-arrays.

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

   s = printstruct('c', randn(10)>0.5)

 See also DISP
```
