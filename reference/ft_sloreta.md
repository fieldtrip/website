---
title: ft_sloreta
---
```
 ft_sloreta scans on pre-defined dipole locations with a single dipole
 and returns the sLORETA spatial filter output for a dipole on every
 location. Dipole locations that are outside the head will return a
 NaN value. Adapted from beamformer_lcmv.m

 Use as
   [dipout] = beamformer_lcmv(dipin, grad, headmodel, dat, cov, varargin)
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

 Additional options should be specified in key-value pairs and can be
  'lambda'           = regularisation parameter
  'powmethod'        = can be 'trace' or 'lambda1'
  'feedback'         = give ft_progress indication, can be 'text', 'gui' or 'none' (default)
  'fixedori'         = use fixed or free orientation,                   can be 'yes' or 'no'
  'projectnoise'     = project noise estimate through filter,           can be 'yes' or 'no'
  'projectmom'       = project the dipole moment timecourse on the direction of maximal power, can be 'yes' or 'no'
  'keepfilter'       = remember the beamformer filter,                  can be 'yes' or 'no'
  'keepleadfield'    = remember the forward computation,                can be 'yes' or 'no'
  'keepmom'          = remember the estimated dipole moment timeseries, can be 'yes' or 'no'
  'keepcov'          = remember the estimated dipole covariance,        can be 'yes' or 'no'
  'kurtosis'         = compute the kurtosis of the dipole timeseries,   can be 'yes' or 'no'

 These options influence the forward computation of the leadfield
  'reducerank'       = reduce the leadfield rank, can be 'no' or a number (e.g. 2)
  'normalize'        = normalize the leadfield
  'normalizeparam'   = parameter for depth normalization (default = 0.5)

 If the dipole definition only specifies the dipole location, a rotating
 dipole (regional source) is assumed on each location. If a dipole moment
 is specified, its orientation will be used and only the strength will
 be fitted to the data.
```
