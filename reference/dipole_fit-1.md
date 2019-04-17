---
title: dipole_fit
---
```
 DIPOLE_FIT performs an equivalent current dipole fit with a single
 or a small number of dipoles to explain an EEG or MEG scalp topography.

 Use as
   [dipout] = dipole_fit(dip, sens, headmodel, dat, ...)

 Additional input arguments should be specified as key-value pairs and can include
   'constr'      = Structure with constraints
   'display'     = Level of display [ off | iter | notify | final ]
   'optimfun'    = Function to use [fminsearch | fminunc ]
   'maxiter'     = Maximum number of function evaluations allowed [ positive integer ]
   'metric'      = Error measure to be minimised [ rv | var | abs ]
   'checkinside' = Boolean flag to check whether dipole is inside source compartment [ 0 | 1 ]
   'weight'      = weight matrix for maximum likelihood estimation, e.g. inverse noise covariance

 The following optional input arguments relate to the computation of the leadfields
   'reducerank'      = 'no' or number
   'normalize'       = 'no', 'yes' or 'column'
   'normalizeparam'  = parameter for depth normalization (default = 0.5)

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
