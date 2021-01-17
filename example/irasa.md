---
title: Irregular Resampling Auto-Spectral Analysis (IRASA)
tags: [example, irasa]
---

# Irregular Resampling Auto-Spectral Analysis (IRASA)

IRASA allows distinguishing rhythmic activity from concurrent power-spectral 1/f modulations. The technique virtually compresses and expands the time-domain data with a set of non-integer resampling factors prior to Fourier-based spectral decomposition. As a result, rhythmic components in the power-spectrum are redistributed while the arrhythmic 1/f distribution is left intact. Taking the median of the resulting auto-spectral distributions extracts the power-spectral 1/f component, and the subsequent removal of the 1/f component from the original power-spectrum offers a power-spectral estimate of rhythmic content in the recorded signal. Together, this procedure allows defining spectral distributions on a participant-by-partipant basis (e.g., participant-specific alpha frequency bands), avoiding reliance on canonical frequency bands that may not accurately capture the neural phenomena of interest in each individual.

Below we demonstrate the use of the [IRASA technique](https://link.springer.com/article/10.1007/s10548-015-0448-0) for extracting rhythmic spectral features on simulated data. Please cite the paper when you use the procedure described here.

## Extracting rhythmic spectral features from simulated data

    % simulate data
    F = 1; % weight of (F)ractal components of the simulated data
    O = 1; % weight of (O)scillatory components of the simulated data
    t = (1:60000)/1000; % time axis
    for rpt = 1:1
        try
          % generate pink noise
            dspobj = dsp.ColoredNoise('Color', 'pink', 'SamplesPerFrame', length(t));
            fn = dspobj()';
        catch
            % use another method to make pink noise when dsp.ColoredNoise returns licence error
            fn = cumsum(randn(1,length(t))); 
        end

        % add a 10Hz and 60 Hz oscillation
        data.trial{1,rpt} = F * fn + O * cos(2*pi*10*t) + O * cos(2*pi*60*t);
        data.time{1,rpt}  = t;
        data.label{1}     = 'chan';
        data.trialinfo(rpt,1) = rpt;
    end

    % chunk 2-second segments (gives 1Hz frequency resolution) for long/continous trials
    cfg           = [];
    cfg.length    = 2; % freqency resolution = fsample/2^floor(log2(cfg.length*fsample*0.9))
    cfg.overlap   = 0.5;
    data          = ft_redefinetrial(cfg, data);

    % compute the fractal and original spectra
    cfg               = [];
    cfg.foilim        = [1 200];
    cfg.pad           = 'nextpow2';
    cfg.method        = 'irasa';
    cfg.output        = 'fractal';
    fractal = ft_freqanalysis(cfg, data);
    cfg.output        = 'original';
    original = ft_freqanalysis(cfg, data);

    % subtract the fractal component from the power spectrum
    cfg               = [];
    cfg.parameter     = 'powspctrm';
    cfg.operation     = 'x2-x1';
    oscillatory = ft_math(cfg, fractal, original);

    % display the spectra in log-log scale
    figure();
    hold on;
    plot(log(original.freq), log(original.powspctrm),'k');
    plot(log(fractal.freq), log(fractal.powspctrm));
    plot(log(fractal.freq), log(oscillatory.powspctrm));
    xlabel('log-freq'); ylabel('log-power');
    legend({'original','fractal','oscillatory'},'location','southwest');
    if F~=0 && O==0
        title('pure fractal signal');
    elseif F==0 && O~=0
        title('pure oscillatory signal');
    elseif F~=0 && O~=0
        title('mixed signal');
    end

{% include image src="/assets/img/example/irasa/example.png" %}

## Updates to the IRASA implementation

{% include markup/warning %}
Starting from version 20210114 the **[ft_specest_irasa](https://github.com/fieldtrip/fieldtrip/blob/master/specest/ft_specest_irasa.m)** function has been updated with some non-backward-compatible changes. If you have used the previous implementation of IRASA, you must adapt your analysis scripts accordingly.

  - The current implementation implements the correct computational order of geometric and arithmetic means, which were swapped in the previous implementation (see [issue 1546](https://github.com/fieldtrip/fieldtrip/pull/1602)). 

  - The current implementation enables IRASA and FFT for estimating both the fractal (arrhythmic) and original power-spectra, respectively. You do not have to use cfg.method='mtmfft' any more for computing the original power-spectrum. We recommend to compute both of them with cfg.method='irasa' to ensure a consistent frequency resolution and tapering of the fractal and original power-spectra. For that you should call **[ft_freqanalysis](https://github.com/fieldtrip/fieldtrip/blob/master/ft_freqanalysis.m)** twice, once with cfg.output='fractal', and once with cfg.output='original'.

- The current implementation partition the trials as 90% long as the original ones automatically. Users do not have to call **[ft_redefinetrial](https://github.com/fieldtrip/fieldtrip/blob/master/ft_redefinetrial.m)**. However, if you are analyzing a continuous trial or trials with unequal lengthes, it is recommended to segment the data following [the Welch's method](https://en.wikipedia.org/wiki/Welch%27s_method) before spectrum estimation, as illustrated in the example script above. The frequency resolution of the output will be `fs/2^floor(log2(L*fs*0.9))` where L is the length of the segments in seconds and fs refers to the sampling rate.
{% include markup/end %}


{% include markup/danger %}
Note that the upper limit of cfg.foilim has to be specified 1.9 (the maximal resampling factor) times as large as your intent, due to the resampling procedure of IRASA. For instance, you are interested in 100 Hz, the upper limit shall be set as 1.9 * 100 = 190 Hz. The same logic holds when you apply IRASA onto a band-pass or low-pass filtered dataset. Keep in mind, the filters might done with your own analysis piplines and/or with the acquisition system itself. For example, MEG data aquired at the DCCN with standard acquisition settings at 1200 Hz will have been subjected to a 300 Hz low-pass filter.
{% include markup/end %}


{% include image src="/assets/img/example/irasa/order.png" %}

{% include image src="/assets/img/example/irasa/fract.png" %}

{% include image src="/assets/img/example/irasa/mixed.png" %}

