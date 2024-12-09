---
title: Preprocessing of EEG/MEG time series data
tags: [development, preproc]
redirect_from:
  - /development/preproc/
---

# Preprocessing of EEG/MEG time series data

FieldTrip has a consistent set of low-level functions for reprocessing of EEG and MEG data, such as filtering, baseline
correction and re-referencing. This allows other projects to re-use the implemented methods separate from FieldTrip (e.g., for realtime analysis of EEG and MEG data) and perhaps also to contribute to FieldTrip.

The low-level functions are combined in the **preproc** toolbox, which is available for download [here](https://download.fieldtriptoolbox.org/modules/).

## Interface to the preprocessing functions

Note that the FieldTrip toolbox comes with a user-friendly **[ft_preprocessing](/reference/ft_preprocessing)** function, which reads data from disk and applies preprocessing to that data. Regular users mainly interested in analyzing their data should be using that function. The functions described here are for people that are developing their own code and/or contributing to the development of FieldTrip.

All of the low-level preprocessing functions require data to be represented as a 2D matrix (Nchans X Nsamples). The following functions are implemented in the preproc module:

- **[ft_preproc_bandpassfilter](/reference/preproc/ft_preproc_bandpassfilter)** applies a band-pass filter to the data
- **[ft_preproc_bandstopfilter](/reference/preproc/ft_preproc_bandstopfilter)** applies a band-stop filter to the data
- **[ft_preproc_highpassfilter](/reference/preproc/ft_preproc_highpassfilter)** applies a high-pass filter to the data
- **[ft_preproc_lowpassfilter](/reference/preproc/ft_preproc_lowpassfilter)** applies a low-pass filter to the data
- **[ft_preproc_medianfilter](/reference/preproc/ft_preproc_medianfilter)** applies a median filter, i.e. a jump-preserving smoothing kernel
- **[ft_preproc_dftfilter](/reference/preproc/ft_preproc_dftfilter)** applies a narrow-band notch filter to the data to remove the 50Hz noise
- **[ft_preproc_baselinecorrect](/reference/preproc/ft_preproc_baselinecorrect)** performs a baseline correction
- **[ft_preproc_detrend](/reference/preproc/ft_preproc_detrend)** removes linear or higher order polynomial trends
- **[ft_preproc_polyremoval](/reference/preproc/ft_preproc_polyremoval)** removes polynomial trends
- **[ft_preproc_denoise](/reference/preproc/ft_preproc_denoise)** regresses out noise with a known time course
- **[ft_preproc_derivative](/reference/preproc/ft_preproc_derivative)** computes the temporal Nth order derivative
- **[ft_preproc_hilbert](/reference/preproc/ft_preproc_hilbert)** computes the Hilbert transpose of the data
- **[ft_preproc_rectify](/reference/preproc/ft_preproc_rectify)** rectifies the data, useful for EMG
- **[ft_preproc_rereference](/reference/preproc/ft_preproc_rereference)** rereferences EEG data using the average over all channels or selected channels
- **[ft_preproc_resample](/reference/preproc/ft_preproc_resample)** resamples the data
- **[ft_preproc_slidingrange](/reference/preproc/ft_preproc_slidingrange)** computes the range of the data in a sliding time window
- **[ft_preproc_standardize](/reference/preproc/ft_preproc_standardize)** performs a z-transformation of the data

## Benchmarking

For real-time use of the functions in this module it is relevant to know how much time each function takes. The execution time depends on the number of channels and on the number of samples in the data block. Assuming that multiple functions are called as part of a larger processing pipeline, the time of the functions that are called has to be summed up.

The benchmarking results presented in the table below were determined with fieldtrip-20101227 and MATLAB R2010a running on a Macbook Pro with a 2.53 GHz Intel Core 2 Duo processor. Execution time was determined for three representative data block sizes and for various parameters for each function.

The full code for the benchmarking (one script per preproc function and some helper functions) is included in the release version of FieldTrip. You can repeat it on your own workstation and for your own data characteristics.

| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| ---------------------------------------------------------------------------------------------------- | ------------ | ------------ | ------------- |
| preproc_bandpassfilter; Fsample = 1000; Fbp = [ 10 100 ]; order = 2; type = 'but'; dir = 'onepass';  | 0.84 ms      | 1.03 ms      | 1.95 ms       |
| preproc_bandpassfilter; Fsample = 1000; Fbp = [ 10 100 ]; order = 4; type = 'but'; dir = 'onepass';  | 1.04 ms      | 1.38 ms      | 2.87 ms       |
| preproc_bandpassfilter; Fsample = 1000; Fbp = [ 10 100 ]; order = 6; type = 'but'; dir = 'onepass';  | 1.19 ms      | 1.24 ms      | 3.79 ms       |
| preproc_bandpassfilter; Fsample = 1000; Fbp = [ 10 100 ]; order = 16; type = 'fir'; dir = 'onepass'; | 1.37 ms      | 1.38 ms      | 2.60 ms       |
| preproc_bandpassfilter; Fsample = 1000; Fbp = [ 10 100 ]; order = 32; type = 'fir'; dir = 'onepass'; | 1.67 ms      | 1.51 ms      | 2.84 ms       |
| preproc_bandpassfilter; Fsample = 1000; Fbp = [ 10 100 ]; order = 64; type = 'fir'; dir = 'onepass'; | 1.62 ms      | 1.39 ms      | 3.08 ms       |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_bandstopfilter; Fsample = 1000; Fbp = [ 45 55 ]; order = 2; type = 'but'; dir = 'onepass';   | 1.09 ms      | 1.01 ms      | 2.63 ms       |
| preproc_bandstopfilter; Fsample = 1000; Fbp = [ 45 55 ]; order = 4; type = 'but'; dir = 'onepass';   | 1.20 ms      | 1.39 ms      | 3.57 ms       |
| preproc_bandstopfilter; Fsample = 1000; Fbp = [ 45 55 ]; order = 6; type = 'but'; dir = 'onepass';   | 1.49 ms      | 1.39 ms      | 4.47 ms       |
| preproc_bandstopfilter; Fsample = 1000; Fbp = [ 45 55 ]; order = 16; type = 'fir'; dir = 'onepass';  | 1.65 ms      | 1.33 ms      | 3.09 ms       |
| preproc_bandstopfilter; Fsample = 1000; Fbp = [ 45 55 ]; order = 32; type = 'fir'; dir = 'onepass';  | 1.57 ms      | 1.40 ms      | 3.03 ms       |
| preproc_bandstopfilter; Fsample = 1000; Fbp = [ 45 55 ]; order = 64; type = 'fir'; dir = 'onepass';  | 1.60 ms      | 1.40 ms      | 3.29 ms       |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_baselinecorrect; begsample = []; endsample = [];                                             | 0.14 ms      | 0.17 ms      | 0.49 ms       |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_derivative; order = 1; padding = 'end';                                                      | 0.08 ms      | 0.10 ms      | 0.46 ms       |
| preproc_derivative; order = 1; padding = 2;                                                          | 0.08 ms      | 0.10 ms      | 0.30 ms       |
| preproc_derivative; order = 1; padding = 3;                                                          | 0.08 ms      | 0.09 ms      | 0.17 ms       |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_detrend; begsample = []; endsample = []; order = 1;                                          | 0.14 ms      | 0.22 ms      | 0.54 ms       |
| preproc_detrend; begsample = []; endsample = []; order = 2;                                          | 0.13 ms      | 0.24 ms      | 0.76 ms       |
| preproc_detrend; begsample = []; endsample = []; order = 3;                                          | 0.15 ms      | 0.32 ms      | 0.77 ms       |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_dftfilter; Fsample = 1000; Fline = 50;                                                       | 0.19 ms      | 0.37 ms      | 1.87 ms       |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_highpassfilter; Fsample = 1000; Fh = 1; order = 2; type = 'but'; dir = 'onepass';            | 0.77 ms      | 0.94 ms      | 1.73 ms       |
| preproc_highpassfilter; Fsample = 1000; Fh = 1; order = 4; type = 'but'; dir = 'onepass';            | 0.81 ms      | 1.19 ms      | 1.97 ms       |
| preproc_highpassfilter; Fsample = 1000; Fh = 1; order = 6; type = 'but'; dir = 'onepass';            | 0.90 ms      | 0.99 ms      | 2.21 ms       |
| preproc_highpassfilter; Fsample = 1000; Fh = 1; order = 16; type = 'fir'; dir = 'onepass';           | 1.14 ms      | 1.55 ms      | 2.59 ms       |
| preproc_highpassfilter; Fsample = 1000; Fh = 1; order = 32; type = 'fir'; dir = 'onepass';           | 1.50 ms      | 1.24 ms      | 2.72 ms       |
| preproc_highpassfilter; Fsample = 1000; Fh = 1; order = 64; type = 'fir'; dir = 'onepass';           | 1.50 ms      | 1.26 ms      | 2.85 ms       |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_hilbert; option = 'complex';                                                                 | 0.26 ms      | 0.45 ms      | 2.24 ms       |
| preproc_hilbert; option = 'abs';                                                                     | 0.24 ms      | 0.59 ms      | 4.48 ms       |
| preproc_hilbert; option = 'angle';                                                                   | 0.34 ms      | 0.93 ms      | 6.50 ms       |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_lowpassfilter; Fsample = 1000; Fl = 30; order = 2; type = 'but'; dir = 'onepass';            | 0.73 ms      | 0.79 ms      | 1.49 ms       |
| preproc_lowpassfilter; Fsample = 1000; Fl = 30; order = 4; type = 'but'; dir = 'onepass';            | 0.61 ms      | 0.79 ms      | 3.28 ms       |
| preproc_lowpassfilter; Fsample = 1000; Fl = 30; order = 8; type = 'but'; dir = 'onepass';            | 0.98 ms      | 0.93 ms      | 2.52 ms       |
| preproc_lowpassfilter; Fsample = 1000; Fl = 30; order = 16; type = 'fir'; dir = 'onepass';           | 1.34 ms      | 1.15 ms      | 2.33 ms       |
| preproc_lowpassfilter; Fsample = 1000; Fl = 30; order = 32; type = 'fir'; dir = 'onepass';           | 1.41 ms      | 1.18 ms      | 2.36 ms       |
| preproc_lowpassfilter; Fsample = 1000; Fl = 30; order = 64; type = 'fir'; dir = 'onepass';           | 1.40 ms      | 1.25 ms      | 2.87 ms       |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_medianfilter; order = 10;                                                                    | 1.43 ms      | 2.68 ms      | 20.63 ms      |
| preproc_medianfilter; order = 20;                                                                    | 1.92 ms      | 4.28 ms      | 32.26 ms      |
| preproc_medianfilter; order = 40;                                                                    | 2.51 ms      | 9.53 ms      | 75.12 ms      |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_rectify;                                                                                     | 0.06 ms      | 0.06 ms      | 0.14 ms       |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_rereference; refchan = 1;                                                                    | 0.10 ms      | 0.15 ms      | 0.40 ms       |
| preproc_rereference; refchan = 'all';                                                                | 0.13 ms      | 0.17 ms      | 0.71 ms       |
| function name and algorithm details                                                                  | 8ch x 100smp | 8ch x 500smp | 64ch x 500smp |
| preproc_standardize; begsample = []; endsample = [];                                                 | 0.20 ms      | 0.29 ms      | 1.48 ms       |
