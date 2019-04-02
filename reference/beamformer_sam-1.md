---
title: beamformer_sam
---
```
 BEAMFORMER_SAM scans on pre-defined dipole locations with a single
 dipole and returns the CTF Synthetic Aperture Magnetometry (SAM)
 beamformer estimates. location. Dipole locations that are outside
 the head will return a NaN value.

 Use as
   [dipout] = beamformer_sam(dipin, sens, headmodel, dat, cov, varargin)
 where
   dipin       is the input dipole model
   sens        is the gradiometer definition
   headmodel   is the volume conductor definition
   dat         is the data matrix with the ERP or ERF
   cov         is the data covariance or cross-spectral density matrix
 and
   dipout      is the resulting dipole model with all details

 The input dipole model consists of
   dipin.pos   positions for dipole, e.g. regular grid
   dipin.mom   dipole orientation (optional)

 Additional options should be specified in key-value pairs and can be
   ...

 These options influence the forward computation of the leadfield
   'reducerank'      = reduce the leadfield rank, can be 'no' or a number (e.g. 2)
   'normalize'       = normalize the leadfield
   'normalizeparam'  = parameter for depth normalization (default = 0.5)
```
