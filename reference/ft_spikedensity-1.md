---
title: ft_spikedensity
---
```
 FT_SPIKEDENSITY computes the spike density function of the spike trains by
 convolving the data with a window.

 Use as
   [sdf]          = ft_spike_density(cfg, data)
   [sdf, sdfdata] = ft_spike_density(cfg, data)
 
 If you specify one output argument, only the average and variance of spike density
 function across trials will be computed and individual trials are not kept. See
 cfg.winfunc below for more information on the smoothing kernel to use.

 Inputs:
   DATA should be organised in a RAW structure with binary spike
   representations obtained from FT_APPENDSPIKE or FT_CHECKDATA, or
   a SPIKE structure.

 Configurations:
   cfg.timwin         = [begin end], time of the smoothing kernel (default = [-0.05 0.05])
                        If cfg.winfunc = @alphawin, cfg.timwin(1) will be
                        set to 0. Hence, it is possible to use asymmetric
                        kernels. 
   cfg.outputunit     = 'rate' (default) or 'spikecount'. This determines the physical unit
                        of our spikedensityfunction, either in firing rate or in spikecount.
   cfg.winfunc        = (a) string or function handle, type of window to convolve with (def = 'gauss').
                        - 'gauss' (default)
                        - 'alphawin', given by win = x*exp(-x/timeconstant)
                        - For standard window functions in the signal processing toolbox see
                          WINDOW.
                        (b) vector of length nSamples, used directly as window
   cfg.winfuncopt     = options that go with cfg.winfunc
                        For cfg.winfunc = 'alpha': the timeconstant in seconds (default = 0.005s)
                        For cfg.winfunc = 'gauss': the standard deviation in seconds (default =
                                         1/4 of window duration in seconds)
                        For cfg.winfunc = 'wname' with 'wname' any standard window function
                                          see window opts in that function and add as cell-array
                        If cfg.winfunctopt = [], default opts are taken.
   cfg.latency        = [begin end] in seconds, 'maxperiod' (default), 'minperiod',
                        'prestim'(t>=0), or 'poststim' (t>=0).
   cfg.vartriallen    = 'yes' (default) or 'no'.
                        'yes' - accept variable trial lengths and use all available trials
                         and the samples in every trial. Missing values will be ignored in
                         the computation of the average and the variance.
                        'no'  - only select those trials that fully cover the window as
                         specified by cfg.latency.
   cfg.spikechannel   = cell-array ,see FT_CHANNELSELECTION for details
   cfg.trials         =  numeric or logical selection of trials (default = 'all')
   cfg.keeptrials     = 'yes' or 'no' (default). If 'yes', we store the trials in a matrix
                         in the output SDF as well
   cfg.fsample        = additional user input that can be used when input
                        is a SPIKE structure, in that case a continuous
                        representation is created using cfg.fsample
                        (default = 1000)

 The SDF output is a data structure similar to the TIMELOCK structure from FT_TIMELOCKANALYSIS.
 For subsequent processing you can use for example
   FT_TIMELOCKSTATISTICS                Compute statistics on SDF
   FT_SPIKE_PLOT_RASTER                 Plot together with the raster plots
   FT_SINGLEPLOTER and FT_MULTIPLOTER   Plot spike-density alone

 The SDFDATA output is a data structure similar to DATA type structure from FT_PREPROCESSING.
 For subsequent processing you can use for example
   FT_TIMELOCKANALYSIS                  Compute time-locked average and variance
   FT_FREQANALYSIS                      Compute frequency and time-ferquency spectrum.
```
