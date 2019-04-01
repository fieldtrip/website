---
title: ft_eloreta
---
```

 Use as
   [dipout] = ft_eloreta(dipin, grad, headmodel, dat, cov, varargin)
 where
   dipin       is the input dipole model
   grad        is the gradiometer definition
   headmodel   is the volume conductor definition
   dat         is the data matrix with the ERP or ERF
   cov         is the data covariance or cross-spectral density matrix
 and
   dipout      is the resulting dipole model with all details

 The input dipole model consists of
   dipin.pos   positions for dipole, e.g. regular grid, Npositions x 3
   dipin.mom   dipole orientation (optional), 3 x Npositions
   dipin.filter precomputed filter cell-array of 1 x Npositions, each cell
               containing nchannels x 3 matrix

 Additional options should be specified in key-value pairs and can be
  'keepfilter'       = remember the beamformer filter,    can be 'yes' or 'no'
  'keepleadfield'    = remember the forward computation,  can be 'yes' or 'no'
  'keepmom'          = remember the dipole moment,        can be 'yes' or 'no'
  'lambda'           = scalar, regularisation parameter (default = 0.05)
```
