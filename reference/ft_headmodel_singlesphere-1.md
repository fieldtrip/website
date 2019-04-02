---
title: ft_headmodel_singlesphere
---
```
 FT_HEADMODEL_SINGLESPHERE creates a volume conduction model of the
 head by fitting a spherical model to a set of points that describe
 the head surface.

 For MEG this implements Cuffin BN, Cohen D.  "Magnetic fields of
 a dipole in special volume conductor shapes" IEEE Trans Biomed Eng.
 1977 Jul;24(4):372-81.

 Use as
   headmodel = ft_headmodel_singlesphere(mesh, ...)

 Optional arguments should be specified in key-value pairs and can include
   conductivity     = number, conductivity of the sphere

 See also FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD
```
