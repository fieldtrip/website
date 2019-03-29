---
title: ft_preproc_dftfilter
---
```
 FT_PREPROC_DFTFILTER reduces power line noise (50 or 60Hz) via two 
 alternative methods:
 A) DFT filter (Flreplace = 'zero') or
 B) Spectrum Interpolation (Flreplace = 'neighbour').

 A) The DFT filter applies a notch filter to the data to remove the 50Hz
 or 60Hz line noise components ('zeroing'). This is done by fitting a sine 
 and cosine at the specified frequency to the data and subsequently 
 subtracting the estimated components. The longer the data is, the sharper 
 the spectral notch will be that is removed from the data.
 Preferably the data should have a length that is a multiple of the
 oscillation period of the line noise (i.e. 20ms for 50Hz noise). If the
 data is of different lenght, then only the first N complete periods are
 used to estimate the line noise. The estimate is subtracted from the
 complete data.

 B) Alternatively line noise is reduced via spectrum interpolation
 (Leske & Dalal, 2019, NeuroImage 189,
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

 Use as
   [filt] = ft_preproc_dftfilter(dat, Fsample, Fline, varargin)
 where
   dat             data matrix (Nchans X Ntime)
   Fsample         sampling frequency in Hz
   Fline           line noise frequency (and harmonics)

 Additional input arguments come as key-value pairs:

   Flreplace       'zero' or 'neighbour', method used to reduce line noise, 'zero' implies DFT filter, 'neighbour' implies spectrum interpolation  
   Flwidth         bandwidth of line noise frequencies, applies to spectrum interpolation, in Hz
   Neighwidth      width of frequencies neighbouring line noise frequencies, applies to spectrum interpolation (Flreplace = 'neighbour'), in Hz 

 The line frequency should be specified as a single number for the DFT filter.
 If omitted, a European default of 50Hz will be assumed

 See also PREPROC
```
