---
title: ft_connectivity_plm
---
```plaintext
 FT_CONNECTIVITY_PLM computes the phase linearity measurement from a cell
 array of time-domain data, where each cell is an epoch. This function implements
 the metric described in Baselice et al. "Phase Linearity Measurement:
 a novel index for brain functional connectivity", IEEE Transactions
 on Medical Imaging, 2018. Please reference the paper in case of use.

 Use as
   [p] = ft_connectivity_plm(input, ...)

 The input data input should be organized as a cell-array, one element for each epoch.
 Each cell element should be a matrix of of nchan x nsamples values.

 Additional optional input arguments come as key-value pairs:
   bandwidth	=	scalar, half-bandwidth parameter: the frequency range
			across which to integrate
   fsample     =       sampling frequency, needed to convert bandwidth to number of bins

 The output p contains the phase linearity measurement in the [0, 1] interval.
 The output p is organized as a 3D matrix of nepoch x nchan x  nchan dimensions.

 See also FT_CONNECTIVITYANALYSIS
```
