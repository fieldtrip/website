---
title: ft_warp_error
---
```
 FT_WARP_ERROR computes the mean distance after linear or non-linear warping
 and can be used as the goalfunction in a 3D warping minimalisation

 Use as
   dist = ft_warp_error(M, input, target, 'method')

 It returns the mean Euclidian distance (i.e. the residual) for an interative
 optimalization to transform the input towards the target using the
 transformation M with the specified warping method.

 See also FT_WARP_OPTIM, FT_WARP_APPLY
```
