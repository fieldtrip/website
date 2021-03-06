---
title: ft_preproc_dftfilter
---
```plaintext
 FT_PREPROC_DFTFILTER reduces power line noise (50 or 60Hz) using a 
 discrete Fourier transform (DFT) filter, or spectrum interpolation.

 Use as
   [filt] = ft_preproc_dftfilter(dat, Fsample)
 or 
   [filt] = ft_preproc_dftfilter(dat, Fsample, Fline)
 or
   [filt] = ft_preproc_dftfilter(dat, Fsample, Fline, 'dftreplace', 'zero')
 or
   [filt] = ft_preproc_dftfilter(dat, Fsample, Fline, 'dftreplace', 'neighbour')
 where
   dat        data matrix (Nchans X Ntime)
   Fsample    sampling frequency in Hz
   Fline      frequency of the power line interference (if omitted from the input
              the default European value of 50 Hz is assumed)
 
 Additional optional arguments are to be provided as key-value pairs:
   dftreplace = 'zero' (default) or 'dftreplace'.
 
 If dftreplace = 'zero', the powerline component's amplitude is estimated by
 fitting a sine and cosine at the specified frequency, and subsequently
 this fitted signal is subtracted from the data. The longer the sharper
 the spectral notch will be that is removed from the data.
 Preferably the data should have a length that is an integer multiple of the
 oscillation period of the line noise (i.e. 20ms for 50Hz noise). If the
 data is of different length, then only the first N complete periods are
 used to estimate the line noise. The estimate is subtracted from the
 complete data.

 If dftreplace = 'neighbour' the powerline component is reduced via spectrum 
 interpolation (Leske & Dalal, 2019, NeuroImage 189,
  doi: 10.1016/j.neuroimage.2019.01.026)
 The signal is:
 I)   transformed into the frequency domain via a discrete Fourier
       transform (DFT),
 II)  the line noise component (e.g. 50Hz, Flwidth = 1 (±1Hz): 49-51Hz) is
       interpolated in the amplitude spectrum by replacing the amplitude
       of this frequency bin by the mean of the adjacent frequency bins
       ('neighbours', e.g. 49Hz and 51Hz).
       Neighwidth defines frequencies considered for the mean (e.g.
       Neighwidth = 2 (±2Hz) implies 47-49 Hz and 51-53 Hz).
       The original phase information of the noise frequency bin is
       retained.
 III) the signal is transformed back into the time domain via inverse DFT
       (iDFT).
 If Fline is a vector (e.g. [50 100 150]), harmonics are also considered.
 Preferably the data should be continuous or consist of long data segments
 (several seconds) to avoid edge effects. If the sampling rate and the
 data length are such, that a full cycle of the line noise and the harmonics
 fit in the data and if the line noise is stationary (e.g. no variations
 in amplitude or frequency), then spectrum interpolation can also be
 applied to short trials. But it should be used with caution and checked
 for edge effects.

 When using spectral interpolation, additional arguments are:

   dftwidth          bandwidth of line noise frequencies, applies to spectrum interpolation, in Hz
   dftneighbourwidth width of frequencies neighbouring line noise frequencies, applies to spectrum interpolation (dftreplace = 'neighbour'), in Hz

 If the data contains NaNs, the output of the affected channel(s) will be
 all(NaN).

 See also PREPROC
```
