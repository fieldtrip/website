---
title: ft_connectivity_psi
---
```
 FT_CONNECTIVITY_PSI computes the phase slope index from a data-matrix
 containing the cross-spectral density. It implements the method described
 in: Nolte et al., Robustly estimating the flow direction of information
 in complex physical systems. Physical Review Letters, 2008; 100; 234101.

 Use as
   [c, v, n] = ft_connectivity_psi(input, ...)

 The input data input should be organized as
   Repetitions x Channel x Channel (x Frequency) (x Time)
 or
   Repetitions x Channelcombination (x Frequency) (x Time)

 The first dimension should be singleton if the input already contains an
 average.

 Additional optional input arguments come as key-value pairs:
   nbin			=	scalar, half-bandwidth parameter: the number of frequency bins
								across which to integrate
   hasjack		= 0 or 1, specifying whether the repetitions represent
               leave-one-out samples (allowing for a variance estimate)
   feedback	= 'none', 'text', 'textbar' type of feedback showing progress of
               computation
   dimord		= string, specifying how the input matrix should be interpreted
   powindx   =
   normalize =

 The output p contains the phase slope index, v is a variance estimate
 which only can be computed if the data contains leave-one-out samples,
 and n is the number of repetitions in the input data. If the phase slope
 index is positive, then the first chan (1st dim) becomes more lagged (or
 less leading) with higher frequency, indicating that it is causally
 driven by the second channel (2nd dim)

 See also FT_CONNECTIVITYANALYSIS
```
