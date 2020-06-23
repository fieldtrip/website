---
title: beamformer_pcc
---
```plaintext
 BEAMFORMER_PCC implements a linearly-constrained miminum variance  beamformer
 that allows for post-hoc computation of canonical or partial coherence or
 correlation. Moreover, if cortico-cortical interactions are computed, the
 spatial filters are computed with a paired dipole as sourcemodel, thus
 suppressing the distortive effect of correlated activity from the seed region.
 Dipole locations that are outside the head will return a NaN value.

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
