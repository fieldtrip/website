---
title: dipole_fit
---
```plaintext
 DIPOLE_FIT performs an equivalent current dipole fit with a single
 or a small number of dipoles to explain an EEG or MEG scalp topography.

 Use as
   [dipout] = dipole_fit(dip, sens, headmodel, dat, ...)

 Additional input arguments should be specified as key-value pairs and can include
   'display'     = Level of display [ off | iter | notify | final ]
   'optimfun'    = Function to use [fminsearch | fminunc ]
   'maxiter'     = Maximum number of function evaluations allowed [ positive integer ]
   'constr'      = Structure with constraints
   'metric'      = Error measure to be minimised [ rv | var | abs ]
   'checkinside' = Boolean flag to check whether dipole is inside source compartment [ 0 | 1 ]
   'mleweight'   = weight matrix for maximum likelihood estimation, e.g. inverse noise covariance

 The following optional input arguments are for the computation of leadfields
   'reducerank'      = 'no' or number
   'normalize'       = 'no', 'yes' or 'column'
   'normalizeparam'  = parameter for depth normalization (default = 0.5)
   'weight'          = number or 1xN vector, weight for each dipole position to compensate for the size of the corresponding patch (default = 1)
   'backproject'     = 'yes' (default) or 'no', in the case of a rank reduction this parameter determines whether the result will be backprojected onto the original subspace

 The constraints on the source model are specified in a structure
   constr.symmetry   = boolean, dipole positions are symmetrically coupled to each other
   constr.fixedori   = boolean, keep dipole orientation fixed over whole data window
   constr.rigidbody  = boolean, keep relative position of multiple dipoles fixed
   constr.mirror     = vector, used for symmetric dipole models
   constr.reduce     = vector, used for symmetric dipole models
   constr.expand     = vector, used for symmetric dipole models
   constr.sequential = boolean, fit different dipoles to sequential slices of the data

 The maximum likelihood estimation implements
   Lutkenhoner B. "Dipole source localization by means of maximum
   likelihood estimation I. Theory and simulations" Electroencephalogr Clin
   Neurophysiol. 1998 Apr;106(4):314-21.
```
