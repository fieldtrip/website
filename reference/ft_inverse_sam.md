---
title: ft_inverse_sam
---
```plaintext
 FT_INVERSE_SAM scans on pre-defined dipole locations with a single dipole and
 returns the Synthetic Aperture Magnetometry (SAM) beamformer estimates.

 Use as
   [estimate] = ft_inverse_sam(sourcemodel, sens, headmodel, dat, cov, ...)
 where
   sourcemodel is the input source model, see FT_PREPARE_SOURCEMODEL
   sens        is the gradiometer or electrode definition, see FT_DATATYPE_SENS
   headmodel   is the volume conductor definition, see FT_PREPARE_HEADMODEL
   dat         is the data matrix with the ERP or ERF
   cov         is the data covariance or cross-spectral density matrix
 and
   estimate    contains the estimated source parameters

 Additional input arguments should be specified as key-value pairs and can include
   'meansphereorigin'
   'feedback'
   'fixedori'
   'noisecov'
   'toi'

 These options influence the forward computation of the leadfield
   'reducerank'      = 'no' or number  (default = 3 for EEG, 2 for MEG)
   'backproject'     = 'yes' or 'no', in the case of a rank reduction this parameter determines whether the result will be backprojected onto the original subspace (default = 'yes')
   'normalize'       = 'no', 'yes' or 'column' (default = 'no')
   'normalizeparam'  = parameter for depth normalization (default = 0.5)
   'weight'          = number or Nx1 vector, weight for each dipole position to compensate for the size of the corresponding patch (default = 1)

 See also FT_SOURCEANALYSIS, FT_PREPARE_HEADMODEL, FT_PREPARE_SOURCEMODEL
```
