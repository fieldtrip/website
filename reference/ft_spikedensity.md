---
layout: default
---

##  FT_SPIKEDENSITY

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_spikedensity".

`<html>``<pre>`
    `<a href=/reference/ft_spikedensity>``<font color=green>`FT_SPIKEDENSITY`</font>``</a>` computes the spike density function of the spike trains by
    convolving the data with a window.
 
    Use as
    [sdf]          = ft_spike_density(cfg, data)
    [sdf, sdfdata] = ft_spike_density(cfg, data)
    
    If you specify one output argument, only the average and variance of spike density
    function across trials will be computed and individual trials are not kept. See
    cfg.winfunc below for more information on the smoothing kernel to use.
 
    Input
    DATA should be organised in a RAW structure with binary spike
    representations obtained from `<a href=/reference/ft_appendspike>``<font color=green>`FT_APPENDSPIKE`</font>``</a>` or `<a href=/reference/ft_checkdata>``<font color=green>`FT_CHECKDATA`</font>``</a>`, or
    a SPIKE structure.
 
    Configuration
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
                                           see window opts in that function and add as cell array
                         If cfg.winfunctopt = [], default opts are taken.
    cfg.latency        = [begin end] in seconds, 'maxperiod' (default), 'minperiod',
                         'prestim'(t&gt;=0), or 'poststim' (t&gt;=0).
    cfg.vartriallen    = 'yes' (default) or 'no'.
                         'yes' - accept variable trial lengths and use all available trials
                          and the samples in every trial. Missing values will be ignored in
                          the computation of the average and the variance.
                         'no'  - only select those trials that fully cover the window as
                          specified by cfg.latency.
    cfg.spikechannel   = cell-array ,see `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>` for details
    cfg.trials         =  numeric or logical selection of trials (default = 'all')
    cfg.keeptrials     = 'yes' or 'no' (default). If 'yes', we store the trials in a matrix
                          in the output SDF as well
    cfg.fsample        = additional user input that can be used when input
                         is a SPIKE structure, in that case a continuous
                         representation is created using cfg.fsample
                         (default = 1000)
 
    The SDF output is a data structure similar to the TIMELOCK structure from `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`.
    For subsequent processing you can use for example
    `<a href=/reference/ft_timelockstatistics>``<font color=green>`FT_TIMELOCKSTATISTICS`</font>``</a>`                Compute statistics on SDF
    `<a href=/reference/ft_spike_plot_raster>``<font color=green>`FT_SPIKE_PLOT_RASTER`</font>``</a>`                 Plot together with the raster plots
    `<a href=/reference/ft_singleplotER>``<font color=green>`FT_SINGLEPLOTER`</font>``</a>` and `<a href=/reference/ft_multiplotER>``<font color=green>`FT_MULTIPLOTER`</font>``</a>`   Plot spike-density alone
 
    The SDFDATA output is a data structure similar to DATA type structure from `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`.
    For subsequent processing you can use for example
    `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`                  Compute time-locked average and variance
    `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`                      Compute frequency and time-ferquency spectrum.
`</pre>``</html>`

