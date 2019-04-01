---
title: minimumnormestimate
---
```
 MINIMUMNORMESTIMATE computes a linear estimate of the current in a
 distributed source model.

 Use as
   [dipout] = minimumnormestimate(dip, grad, headmodel, dat, ...)

 Optional input arguments should come in key-value pairs and can include
   'noisecov'         = Nchan x Nchan matrix with noise covariance
   'noiselambda'      = scalar value, regularisation parameter for the noise covariance matrix (default = 0)
   'sourcecov'        = Nsource x Nsource matrix with source covariance (can be empty, the default will then be identity)
   'lambda'           = scalar, regularisation parameter (can be empty, it will then be estimated from snr)
   'snr'              = scalar, signal to noise ratio
   'reducerank'       = reduce the leadfield rank, can be 'no' or a number (e.g. 2)
   'normalize'        = normalize the leadfield
   'normalizeparam'   = parameter for depth normalization (default = 0.5)
   'keepfilter'       = 'no' or 'yes', keep the spatial filter in the output
   'prewhiten'        = 'no' or 'yes', prewhiten the leadfield matrix with the noise covariance matrix C
   'scalesourcecov'   = 'no' or 'yes', scale the source covariance matrix R such that trace(leadfield*R*leadfield')/trace(C)=1

 Note that leadfield normalization (depth regularisation) should be done
 by scaling the leadfields outside this function, e.g. in
 prepare_leadfield. Note also that with precomputed leadfields the
 normalization parameters will not have an effect.

 This implements
 * Dale AM, Liu AK, Fischl B, Buckner RL, Belliveau JW, Lewine JD,
   Halgren E (2000): Dynamic statistical parametric mapping: combining
   fMRI and MEG to produce high-resolution spatiotemporal maps of
   cortical activity. Neuron 26:55-67.
 * Arthur K. Liu, Anders M. Dale, and John W. Belliveau  (2002): Monte
   Carlo Simulation Studies of EEG and MEG Localization Accuracy.
   Human Brain Mapping 16:47-62.
 * Fa-Hsuan Lin, Thomas Witzel, Matti S. Hamalainen, Anders M. Dale,
   John W. Belliveau, and Steven M. Stufflebeam (2004): Spectral
   spatiotemporal imaging of cortical oscillations and interactions
   in the human brain.  NeuroImage 23:582-595.
```
