---
title: harmony
---
```
 HARMONY computes a linear estimate of the current in a distributed source model
 using a mesh harmonic based low-pass filter.

 Use as
   [dipout] = minimumnormestimate(dip, grad, headmodel, dat, ...)

 Optional input arguments should come in key-value pairs and can include
  'noisecov'             = Nchan x Nchan matrix with noise covariance
  'noiselambda'          = scalar value, regularisation parameter for the noise covariance matrix (default=0)
  'filter_order'         = scalar, order of the mesh Butterwirth filter
  'filter_bs'            = scalar, stop-band of the mesh Butterworth filter
  'number_harmonics'     = Integer, number of mesh harmonics used (can be empty, the default will then be identity)
  'lambda'               = scalar, regularisation parameter (can be empty, it will then be estimated from snr)
  'snr'                  = scalar, signal to noise ratio
  'reducerank'           = reduce the leadfield rank, can be 'no' or a number (e.g. 2)
  'normalize'            = normalize the leadfield
  'normalizeparam'       = parameter for depth normalization (default = 0.5)
  'keepfilter'           = 'no' or 'yes', keep the spatial filter in the output
  'prewhiten'            = 'no' or 'yes', prewhiten the leadfield matrix with the noise covariance matrix C
  'scalesourcecov'       = 'no' or 'yes', scale the source covariance matrix R such that trace(leadfield*R*leadfield')/trace(C)=1
  'connected_components' = number of connected components of the source mesh (1 or 2)

 Note that leadfield normalization (depth regularisation) should be done by scaling
 the leadfields outside this function, e.g. in prepare_leadfield. Note also that
 with precomputed leadfields the normalization parameters will not have an effect.

 This implements
   Petrov Y (2012) Harmony: EEG/MEG Linear Inverse Source Reconstruction in the
   Anatomical Basis of Spherical Harmonics. PLoS ONE 7(10): e44439.
   doi:10.1371/journal.pone.0044439
```
