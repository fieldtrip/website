---
title: beamformer_dics
---
```
 BEAMFORMER_DICS scans on pre-defined dipole locations with a single dipole
 and returns the beamformer spatial filter output for a dipole on every
 location. Dipole locations that are outside the head will return a
 NaN value.

 Use as
   [dipout] = beamformer_dics(dipin, grad, headmodel, dat, cov, varargin)
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
  'Pr'               = power of the external reference channel
  'Cr'               = cross spectral density between all data channels and the external reference channel
  'refdip'           = location of dipole with which coherence is computed
  'lambda'           = regularisation parameter
  'kappa'            = parameter for covariance matrix inversion
  'tol'              = parameter for covariance matrix inversion
  'powmethod'        = can be 'trace' or 'lambda1'
  'feedback'         = give ft_progress indication, can be 'text', 'gui' or 'none'
  'fixedori'         = use fixed or free orientation,                 can be 'yes' or 'no'
  'projectnoise'     = project noise estimate through filter,         can be 'yes' or 'no'
  'realfilter'       = construct a real-valued filter,                can be 'yes' or 'no'
  'keepfilter'       = remember the beamformer filter,                can be 'yes' or 'no'
  'keepleadfield'    = remember the forward computation,              can be 'yes' or 'no'
  'keepcsd'          = remember the estimated cross-spectral density, can be 'yes' or 'no'

 These options influence the forward computation of the leadfield
  'reducerank'       = reduce the leadfield rank, can be 'no' or a number (e.g. 2)
  'normalize'        = normalize the leadfield
  'normalizeparam'   = parameter for depth normalization (default = 0.5)

 If the dipole definition only specifies the dipole location, a rotating
 dipole (regional source) is assumed on each location. If a dipole moment
 is specified, its orientation will be used and only the strength will
 be fitted to the data.
```
