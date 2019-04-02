---
title: beamformer_pcc
---
```
 BEAMFORMER_PCC implements an experimental beamformer based on partial
 canonical correlations or coherences. Dipole locations that are outside
 the head will return a NaN value.

 Use as
   [dipout] = beamformer_pcc(dipin, grad, headmodel, dat, cov, ...)
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
 and can additionally contain things like a precomputed filter.

 Additional options should be specified in key-value pairs and can be
   refchan
   refdip
   supchan
   supdip
   reducerank
   normalize
   normalizeparam
   feedback
   keepcsd
   keepfilter
   keepleadfield
   keepmom
   lambda
   projectnoise
   realfilter
   fixedori
```
