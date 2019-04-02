---
title: ft_preproc_bandpassfilter
---
```
 FT_PREPROC_BANDPASSFILTER applies a band-pass filter to the data and thereby
 removes the spectral components in the data except for the ones in the
 specified frequency band.

 Use as
   [filt] = ft_preproc_bandpassfilter(dat, Fsample, Fbp, N, type, dir, instabilityfix)
 where
   dat        data matrix (Nchans X Ntime)
   Fsample    sampling frequency in Hz
   Fbp        frequency band, specified as [Fhp Flp]
   N          optional filter order, default is 4 (but) or dependent upon
              frequency band and data length (fir/firls)
   type       optional filter type, can be
                'but' Butterworth IIR filter (default)
                'firws' windowed sinc FIR filter
                'fir' FIR filter using MATLAB fir1 function
                'firls' FIR filter using MATLAB firls function (requires MATLAB Signal Processing Toolbox)
                'brickwall' Frequency-domain filter using MATLAB FFT and iFFT function
   dir        optional filter direction, can be
                'onepass'         forward filter only
                'onepass-reverse' reverse filter only, i.e. backward in time
                'twopass'         zero-phase forward and reverse filter (default except for firws)
                'twopass-reverse' zero-phase reverse and forward filter
                'twopass-average' average of the twopass and the twopass-reverse
                'onepass-zerophase' zero-phase forward filter with delay compensation (default for firws, linear-phase symmetric FIR only)
                'onepass-reverse-zerophase' zero-phase reverse filter with delay compensation
                'onepass-minphase' minimum-phase converted forward filter (non-linear!, firws only)
   instabilityfix optional method to deal with filter instabilities
                'no'       only detect and give error (default)
                'reduce'   reduce the filter order
                'split'    split the filter in two lower-order filters, apply sequentially
   df         optional transition width (firws)
   wintype    optional window type (firws), can be
                'hann'                 (max passband deviation 0.0063 [0.63%], stopband attenuation -44dB)
                'hamming' (default)    (max passband deviation 0.0022 [0.22%], stopband attenuation -53dB)
                'blackman'             (max passband deviation 0.0002 [0.02%], stopband attenuation -74dB)
                'kaiser'
   dev        optional max passband deviation/stopband attenuation (firws with kaiser window, default = 0.001 [0.1%, -60 dB])
   plotfiltresp optional, 'yes' or 'no', plot filter responses (firws, default = 'no')
   usefftfilt optional, 'yes' or 'no', use fftfilt instead of filter (firws, default = 'no')

 Note that a one- or two-pass filter has consequences for the
 strength of the filter, i.e. a two-pass filter with the same filter
 order will attenuate the signal twice as strong.

 Further note that the filter type 'brickwall' filters in the frequency domain,
 but may have severe issues. For instance, it has the implication that the time
 domain signal is periodic. Another issue pertains to that frequencies are
 not well defined over short time intervals; particularly for low frequencies.

 See also PREPROC
```
