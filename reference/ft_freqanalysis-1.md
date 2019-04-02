---
title: ft_freqanalysis
---
```
 FT_FREQANALYSIS performs frequency and time-frequency analysis
 on time series data over multiple trials

 Use as
   [freq] = ft_freqanalysis(cfg, data)

 The input data should be organised in a structure as obtained from
 the FT_PREPROCESSING or the FT_MVARANALYSIS function. The configuration
 depends on the type of computation that you want to perform.

 The configuration should contain:
   cfg.method      = different methods of calculating the spectra
                     'mtmfft', analyses an entire spectrum for the entire data
                       length, implements multitaper frequency transformation
                     'mtmconvol', implements multitaper time-frequency
                       transformation based on multiplication in the
                       frequency domain.
                     'wavelet', implements wavelet time frequency
                       transformation (using Morlet wavelets) based on
                       multiplication in the frequency domain.
                     'tfr', implements wavelet time frequency
                       transformation (using Morlet wavelets) based on
                       convolution in the time domain.
                     'mvar', does a fourier transform on the coefficients
                       of an estimated multivariate autoregressive model,
                       obtained with FT_MVARANALYSIS. In this case, the
                       output will contain a spectral transfer matrix,
                       the cross-spectral density matrix, and the
                       covariance matrix of the innovatio noise.
   cfg.output      = 'pow'       return the power-spectra
                     'powandcsd' return the power and the cross-spectra
                     'fourier'   return the complex Fourier-spectra
   cfg.channel     = Nx1 cell-array with selection of channels (default = 'all'),
                       see FT_CHANNELSELECTION for details
   cfg.channelcmb  = Mx2 cell-array with selection of channel pairs (default = {'all' 'all'}),
                       see FT_CHANNELCOMBINATION for details
   cfg.trials      = 'all' or a selection given as a 1xN vector (default = 'all')
   cfg.keeptrials  = 'yes' or 'no', return individual trials or average (default = 'no')
   cfg.keeptapers  = 'yes' or 'no', return individual tapers or average (default = 'no')
   cfg.pad         = number, 'nextpow2', or 'maxperlen' (default), length
                      in seconds to which the data can be padded out. The
                      padding will determine your spectral resolution. If you
                      want to compare spectra from data pieces of different
                      lengths, you should use the same cfg.pad for both, in
                      order to spectrally interpolate them to the same
                      spectral resolution.  The new option 'nextpow2' rounds
                      the maximum trial length up to the next power of 2.  By
                      using that amount of padding, the FFT can be computed
                      more efficiently in case 'maxperlen' has a large prime
                      factor sum.
   cfg.padtype     = string, type of padding (default 'zero', see
                      ft_preproc_padding)
   cfg.polyremoval = number (default = 0), specifying the order of the
                      polynome which is fitted and subtracted from the time
                      domain data prior to the spectral analysis. For
                      example, a value of 1 corresponds to a linear trend.
                      The default is a mean subtraction, thus a value of 0.
                      If no removal is requested, specify -1.
                      see FT_PREPROC_POLYREMOVAL for details


 METHOD SPECIFIC OPTIONS AND DESCRIPTIONS

 MTMFFT performs frequency analysis on any time series trial data using a
 conventional single taper (e.g. Hanning) or using the multiple tapers based on
 discrete prolate spheroidal sequences (DPSS), also known as the Slepian
 sequence.
   cfg.taper      = 'dpss', 'hanning' or many others, see WINDOW (default = 'dpss')
                     For cfg.output='powandcsd', you should specify the channel combinations
                     between which to compute the cross-spectra as cfg.channelcmb. Otherwise
                     you should specify only the channels in cfg.channel.
   cfg.foilim     = [begin end], frequency band of interest
       OR
   cfg.foi        = vector 1 x numfoi, frequencies of interest
   cfg.tapsmofrq  = number, the amount of spectral smoothing through
                    multi-tapering. Note that 4 Hz smoothing means
                    plus-minus 4 Hz, i.e. a 8 Hz smoothing box.

 MTMCONVOL performs time-frequency analysis on any time series trial data using
 the 'multitaper method' (MTM) based on Slepian sequences as tapers.
 Alternatively, you can use conventional tapers (e.g. Hanning).
   cfg.tapsmofrq  = vector 1 x numfoi, the amount of spectral smoothing
                     through multi-tapering. Note that 4 Hz smoothing means
                     plus-minus 4 Hz, i.e. a 8 Hz smoothing box.
    cfg.foi        = vector 1 x numfoi, frequencies of interest
    cfg.taper      = 'dpss', 'hanning' or many others, see WINDOW (default = 'dpss')
                      For cfg.output='powandcsd', you should specify the channel combinations
                      between which to compute the cross-spectra as cfg.channelcmb. Otherwise
                      you should specify only the channels in cfg.channel.
    cfg.t_ftimwin  = vector 1 x numfoi, length of time window (in seconds)
    cfg.toi        = vector 1 x numtoi, the times on which the analysis
                     windows should be centered (in seconds), or a string
                     such as '50%' or 'all' (default).  Both string options
                     use all timepoints available in the data, but 'all'
                     centers a spectral estimate on each sample, whereas
                     the percentage specifies the degree of overlap between
                     the shortest time windows from cfg.t_ftimwin.

 WAVELET performs time-frequency analysis on any time series trial data using the
 'wavelet method' based on Morlet wavelets. Using mulitplication in the frequency
 domain instead of convolution in the time domain.
   cfg.foi        = vector 1 x numfoi, frequencies of interest
       OR
   cfg.foilim     = [begin end], frequency band of interest
   cfg.toi        = vector 1 x numtoi, the times on which the analysis
                    windows should be centered (in seconds)
   cfg.width      = 'width', or number of cycles, of the wavelet (default = 7)
   cfg.gwidth     = determines the length of the used wavelets in standard
                    deviations of the implicit Gaussian kernel and should
                    be choosen >= 3; (default = 3)

 The standard deviation in the frequency domain (sf) at frequency f0 is
 defined as: sf = f0/width
 The standard deviation in the temporal domain (st) at frequency f0 is
 defined as: st = 1/(2*pi*sf)


 TFR performs time-frequency analysis on any time series trial data using the
 'wavelet method' based on Morlet wavelets. Using convolution in the time domain
 instead of multiplication in the frequency domain.
   cfg.foi        = vector 1 x numfoi, frequencies of interest
       OR
   cfg.foilim     = [begin end], frequency band of interest
   cfg.width      = 'width', or number of cycles, of the wavelet (default = 7)
   cfg.gwidth     = determines the length of the used wavelets in standard
                    deviations of the implicit Gaussian kernel and should
                    be choosen >= 3; (default = 3)


 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a
 *.mat file on disk and/or the output data will be written to a *.mat
 file. These mat files should contain only a single variable,
 corresponding with the input/output structure.

 See also FT_FREQSTATISTICS, FT_FREQDESCRIPTIVES, FT_CONNECTIVITYANALYSIS
```
