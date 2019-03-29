---
title: music
---
```
 MUSIC source localization using MUltiple SIgnal Classification

 This is a signal subspace method, which covers the techniques for
 multiple source localization by using the eigen structure of the
 measured data matrix.

 Use as
   [dipout] = music(dip, grad, headmodel, dat, ...)

 Optional input arguments should be specified as key-value pairs and can be
   'cov'              = data covariance matrix
   'numcomponent'     = integer number
   'feedback'         = 'none', 'gui', 'dial', 'textbar', 'text', 'textcr', 'textnl'
   'reducerank'       = reduce the leadfield rank, can be 'no' or a number (e.g. 2)
   'normalize'        = normalize the leadfield
   'normalizeparam'   = parameter for depth normalization (default = 0.5)

 The original reference is
   J.C. Mosher, P.S. Lewis and R.M. Leahy, "Multiple dipole modeling and
   localization from spatiotemporal MEG data", IEEE Trans. Biomed.
   Eng., pp 541-557, June, 1992.
```
