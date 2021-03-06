---
title: ft_preproc_derivative
---
```plaintext
 FT_PREPROC_DERIVATIVE computes the temporal Nth order derivative of the
 data

 Use as
   [dat] = ft_preproc_derivative(dat, order)
 where
   dat        data matrix (Nchans X Ntime)
   order      number representing the Nth derivative (default = 1)

 If the data contains NaNs, these are ignored for the computation, but
 retained in the output.

 See also PREPROC
```
