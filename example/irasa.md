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
    cfg.length    = 2; % freqency resolution = 1/2^floor(log2(cfg.length*0.9))
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

## Updates and usage of ft_specest_irasa

{% include markup/warning %}
  The current implementation ([2020](https://github.com/fieldtrip/fieldtrip/blob/master/specest/ft_specest_irasa.m)) of IRASA contains the following features comparing to the previous version (2019). Owing to these new features, users may want to adapt their analysis pipelines accordingly, if the pipelines were developed based on the example script for the previous implementation of IRASA.
  - The current implementation partition the trials as 90% long as the original ones automatically. Users do not have to call ft_redefinetrial. However, if you are analyzing a continuous trial or trials with unequal lengthes, it is recommended to segment the data following [the Welch's method](https://en.wikipedia.org/wiki/Welch%27s_method) before spectrum estimation, as illurstrated in the example script above. The frequency resolution of the output will be 1/2^floor(log2(L*0.9)) (L is the length of the segments in samples instead of seconds).
  - The current implementation enables IRASA and FFT for estimating the fractal(arrhythmic) and original power-spectra, respectively. Users do not have to apply cfg.method = 'mtmfft' for computing the original power-spectrum. Instead, it is recommended to compute both of them with ft_specest_irasa to ensure a consistent frequency resolution of the fractal and original power-spectra. To do so, users need to specify the output option as cfg.output = 'fractal' (default) or cfg.output = 'original'. The previous output option cfg.output = 'pow' is no longer compatible with cfg.method = 'irasa'.
  - The current implementation was made for correcting the computational order of geometric and arithmetic means of the previous implementation. 
{% include markup/end %}

{% include image src="/assets/img/example/irasa/order.png" %}

{% include image src="/assets/img/example/irasa/fract.png" %}

{% include image src="/assets/img/example/irasa/mixed.png" %}

