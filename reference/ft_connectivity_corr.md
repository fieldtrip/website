---
title: ft_connectivity_corr
---
```
 FT_CONNECTIVITY_CORR computes correlation, coherence or a related quantity from a
 data-matrix containing a covariance or cross-spectral density. It implements the
 methods as described in the following papers:

 Coherence: Rosenberg et al, The Fourier approach to the identification of
 functional coupling between neuronal spike trains. Prog Biophys Molec
 Biol 1989; 53; 1-31

 Partial coherence: Rosenberg et al, Identification of patterns of
 neuronal connectivity - partial spectra, partial coherence, and neuronal
 interactions. J. Neurosci. Methods, 1998; 83; 57-72

 Phase locking value: Lachaux et al, Measuring phase sychrony in brain
 signals. Human Brain Mapping, 1999; 8; 194-208.

 Imaginary part of coherency: Nolte et al, Identifying true brain
 interaction from EEG data using the imaginary part of coherence. Clinical
 Neurophysiology, 2004; 115; 2292-2307

 Use as
   [c, v, n] = ft_connectivity_corr(input, ...)

 The input data should be an array organized as
   Repetitions x Channel x Channel (x Frequency) (x Time)
 or
   Repetitions x Channelcombination (x Frequency) (x Time)

 If the input already contains an average, the first dimension should be singleton.
 Furthermore, the input data can be complex-valued cross spectral densities, or
 real-valued covariance estimates. If the former is the case, the output will be
 coherence (or a derived metric), if the latter is the case, the output will be the
 correlation coefficient.

 Additional optional input arguments come as key-value pairs:
   hasjack   = 0 or 1 specifying whether the Repetitions represent
               leave-one-out samples
   complex   = 'abs', 'angle', 'real', 'imag', 'complex', 'logabs' for
               post-processing of coherency
   feedback  = 'none', 'text', 'textbar' type of feedback showing progress of
               computation
   dimord    = specifying how the input matrix should be interpreted
   powindx   = required if the input data contain linearly indexed
               channel pairs. should be an Nx2 matrix indexing on each
               row for the respective channel pair the indices of the
               corresponding auto-spectra
   pownorm   = flag that specifies whether normalisation with the
               product of the power should be performed (thus should
               be true when correlation/coherence is requested, and
               false when covariance or cross-spectral density is
               requested).

 Partialisation can be performed when the input data is (chan x chan). The
 following options need to be specified:

   pchanindx   = index-vector to the channels that need to be
                 partialised
   allchanindx = index-vector to all channels that are used
                 (including the "to-be-partialised" ones).

 The output c contains the correlation/coherence, v is a variance estimate
 which only can be computed if the data contains leave-one-out samples,
 and n is the number of repetitions in the input data.

 See also FT_CONNECTIVITYANALYSIS
```
