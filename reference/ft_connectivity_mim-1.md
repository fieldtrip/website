---
title: ft_connectivity_mim
---
```
 FT_CONNECTIVITY_MIM computes the multivariate interaction measure from a
 data-matrix containing the cross-spectral density. This implements the method
 described in Ewald et al., Estimating true brain connectivity from EEG/MEG data
 invariant to linear and static trasformations in sensor space. Neuroimage, 2012;
 476:488.

 Use as
   [m] = hcp_connectivity_mim(input, ...)

 The input data should be an array organized as
   Channel x Channel x Frequency

 Additional optional input arguments come as key-value pairs:
   indices   = 1xN vector with indices of the groups to which the channels belong,
               e.g. [1 1 2 2] for a 2-by-2 connectivity between planar MEG channels.

 The output m contains the Channel*Channel connectivity measure.

 See also FT_CONNECTIVITYANALYSIS
```
