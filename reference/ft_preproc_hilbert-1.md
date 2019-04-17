---
title: ft_preproc_hilbert
---
```
 FT_PREPROC_HILBERT computes the Hilbert transpose of the data and optionally
 performs post-processing on the complex representation, e.g. the absolute
 value of the Hilbert transform of a band-pass filtered signal corresponds
 with the amplitude envelope.

 Use as
   [dat] = ft_preproc_hilbert(dat, option)
 where
   dat        data matrix (Nchans X Ntime)
   option     string that determines whether and how the Hilbert transform
              should be post-processed, can be
                'abs'
                'complex'
                'real'
                'imag'
                'absreal'
                'absimag'
                'angle'

 The default is to return the absolute value of the Hilbert transform.

 See also PREPROC
```
