---
layout: default
---

##  FT_SPIKETRIGGEREDSPECTRUM

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_spiketriggeredspectrum".

`<html>``<pre>`
    `<a href=/reference/ft_spiketriggeredspectrum>``<font color=green>`FT_SPIKETRIGGEREDSPECTRUM`</font>``</a>` computes the Fourier spectrup (amplitude and phase) of
    the LFP around the spikes. A phase of zero corresponds to the spike being on the
    peak of the LFP oscillation. A phase of 180 degree corresponds to the spike being in
    the through of the oscillation. A phase of 45 degrees corresponds to the spike being
    just after the peak in the LFP.
 
    Use as
    [sts] = ft_spiketriggeredspectrum(cfg, data)
    or
    [sts] = ft_spiketriggeredspectrum(cfg, data, spike) 
 
    Configuration
     cfg.method = 'mtmfft' or 'mtmconvol' (see below)
 
    If you specify the method 'mtmconvol', `<a href=/reference/ft_spiketriggeredspectrum_convol>``<font color=green>`FT_SPIKETRIGGEREDSPECTRUM_CONVOL`</font>``</a>` is used. If
    you specify 'mtmfft', `<a href=/reference/ft_spiketriggeredspectrum_fft>``<font color=green>`FT_SPIKETRIGGEREDSPECTRUM_FFT`</font>``</a>` is used (which corresponds to the
    old `<a href=/reference/ft_spiketriggeredspectrum>``<font color=green>`FT_SPIKETRIGGEREDSPECTRUM`</font>``</a>`).
 
 %%%%%%%%%%%%%%
 
    `<a href=/reference/ft_spiketriggeredspectrum_fft>``<font color=green>`FT_SPIKETRIGGEREDSPECTRUM_FFT`</font>``</a>` determines the spike phases by taking the
    FFT locally around every spike, for one unit. This is an efficient
    algorithm when we have few neurons recorded simultaneously with low
    firing rates. All frequencies are computed using the same time-window.
 
    The function must then be called as
    [sts] = ft_spiketriggeredspectrum(cfg, data)
    where some channels of DATA are spike channels, and data is in the raw
    format.
 
    For configuration options see `<a href=/reference/ft_spiketriggeredspectrum_fft>``<font color=green>`FT_SPIKETRIGGEREDSPECTRUM_FFT`</font>``</a>`.
 
 %%%%%%%%%%%%%%
 
    `<a href=/reference/ft_spiketriggeredspectrum_convol>``<font color=green>`FT_SPIKETRIGGEREDSPECTRUM_CONVOL`</font>``</a>` computes the Fourier spectrum of the LFP
    around the spikes using convolution of the complete LFP traces. 
    This is a very efficient algorithm if we many spikes per trial. The
    function allows to compute phases for multiple neurons at the same time.
    An additional feature is that every frequency is processed separately (as
    its done through convolution), such that different time-windows can be
    used per frequency.
    Finally, the function can be called by adding a third input (SPIKE) which
    has the same trial definitions as DATA.
 
    The function must then be called as
    [sts] = ft_spiketriggeredspectrum(cfg, data)
    or
    [sts] = ft_spiketriggeredspectrum(cfg, data, spike)
    where the spiking information can either be represented  in the first data
    input or in the second spike input structure.
 
    For configurations options see `<a href=/reference/ft_spiketriggeredspectrum_convol>``<font color=green>`FT_SPIKETRIGGEREDSPECTRUM_CONVOL`</font>``</a>`
 
 %%%%%%%%%%%%%%
 
    The output STS data structure can be further analyzed using `<a href=/reference/ft_spiketriggeredspectrum_stat>``<font color=green>`FT_SPIKETRIGGEREDSPECTRUM_STAT`</font>``</a>`
`</pre>``</html>`

