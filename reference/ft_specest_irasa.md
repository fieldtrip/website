---
title: ft_specest_irasa
---
```plaintext
 FT_SPECEST_IRASA separates fractal components from the orginal
 power spectrum using Irregular-Resampling Auto-Spectral Analysis (IRASA)

 Use as
   [spectrum,ntaper,freqoi] = ft_specest_irasa(dat,time...)
 where
   dat        = matrix of chan*sample
   time       = vector, containing time in seconds for each sample
   spectrum   = matrix of taper*chan*freqoi of fourier coefficients
   ntaper     = vector containing number of tapers per element of freqoi
   freqoi     = vector of frequencies in spectrum

 Optional arguments should be specified in key-value pairs and can include
   output     = string, indicating type of output('fractal' or 'orignal', default 'fractal')
   pad        = number, total length of data after zero padding (in seconds)
   padtype    = string, indicating type of padding to be used (see ft_preproc_padding, default: zero)
   freqoi     = vector, containing frequencies of interest
   polyorder  = number, the order of the polynomial to fitted to and removed from the data prior to the Fourier transform (default = 0, which removes the DC-component)
   verbose    = boolean, output progress to console (0 or 1, default 1)

 This implements: Wen.H. & Liu.Z.(2016), Separating fractal and oscillatory components in the power 
 spectrum of neurophysiological signal. Brain Topogr. 29(1):13-26. The source code accompanying the 
 original paper is avaible from https://purr.purdue.edu/publications/1987/1
 
 For more information about the difference between the current and previous version and how to use this 
 function, please see https://www.fieldtriptoolbox.org/example/irasa/
 
 See also FT_FREQANALYSIS, FT_SPECEST_MTMFFT, FT_SPECEST_MTMCONVOL, FT_SPECEST_TFR, FT_SPECEST_HILBERT, FT_SPECEST_WAVELET

 Copyright (C) 2019-2020, Rui Liu, Arjen Stolk

 This file is part of FieldTrip, see http://www.fieldtriptoolbox.org
 for the documentation and details.

    FieldTrip is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    FieldTrip is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with FieldTrip. If not, see <http://www.gnu.org/licenses/>.

 $Id$
```
