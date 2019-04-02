---
title: ft_defacemesh
---
```
 FT_DEFACEMESH allows you to de-identify a scalp surface mesh by erasing specific
 regions, such as the face and ears. The graphical user interface allows you to
 position a box over the anatomical data inside which all vertices will be removed.
 You might have to call this function multiple times when both face and ears need to
 be removed. Following defacing, you should check the result with FT_PLOT_MESH.

 Use as
   mesh = ft_defacevolume(cfg, mesh)

 The configuration can contain the following options
   cfg.translate  = initial position of the center of the box (default = [0 0 0])
   cfg.scale      = initial size of the box along each dimension (default is automatic)
   cfg.translate  = initial rotation of the box (default = [0 0 0])
   cfg.selection  = which voxels to keep, can be 'inside' or 'outside' (default = 'outside')

 See also FT_ANONYMIZEDATA, FT_DEFACEVCOLUME, FT_ANALYSISPIPELINE, FT_PLOT_MESH
```
