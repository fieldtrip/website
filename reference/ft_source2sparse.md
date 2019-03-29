---
title: ft_source2sparse
---
```
 FT_SOURCE2SPARSE removes the grid locations outside the brain from the source 
 reconstruction, thereby saving memory.

 This invalidates the fields that describe the grid, and also makes it
 more difficult to make a plot of each of the slices of the source volume.
 The original source structure can be recreated using FT_SOURCE2FULL.

 Use as
   [source] = ft_source2sparse(source)

 See also FT_SOURCE2FULL
```
