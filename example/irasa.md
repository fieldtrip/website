---
title: Irregular Resampling Auto-Spectral Analysis (IRASA)
tags: [example, irasa]
---

# Irregular Resampling Auto-Spectral Analysis (IRASA)

IRASA allows distinguishing rhythmic activity from concurrent power-spectral 1/f modulations. The technique virtually compresses and expands the time-domain data with a set of non-integer resampling factors prior to Fourier-based spectral decomposition. As a result, rhythmic components in the power-spectrum are redistributed while the arrhythmic 1/f distribution is left intact. Taking the median of the resulting auto-spectral distributions extracts the power-spectral 1/f component, and the subsequent removal of the 1/f component from the original power-spectrum offers a power-spectral estimate of rhythmic content in the recorded signal. Below we demonstrate the [IRASA](https://link.springer.com/article/10.1007/s10548-015-0448-0) technique on simulated data containing both rhythmic and arrhythmic content.

Further below, we demonstrate the [extraction of spectral features](https://elifesciences.org/articles/48065) based on IRASA. This adaptive approach allows defining rhythm frequency bands on a participant-by-participant basis (e.g., alpha and beta frequency bands), avoiding having to rely on canonical frequency bands that may not accurately capture the neural phenomena of interest in each individual.

## Separating fractal and oscillatory components in the power-spectrum of simulated data

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
            % use another method to make pink noise when dsp.ColoredNoise returns license error
            fn = cumsum(randn(1,length(t))); 
        end

        % add a 10 Hz and 60 Hz oscillation
        data.trial{1,rpt} = F * fn + O * cos(2*pi*10*t) + O * cos(2*pi*60*t);
        data.time{1,rpt}  = t;
        data.label{1}     = 'chan';
        data.trialinfo(rpt,1) = rpt;
    end

    % chunk into 2-second segments
    cfg               = [];
    cfg.length        = 2;
    cfg.overlap       = 0.5;
    data              = ft_redefinetrial(cfg, data);

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

## Extracting spectral features from human ECoG data

To run this example, download S5_raw_segmented.mat from the [OSF repository](https://osf.io/z4hfm/). Additionally, download S5_lh.pial used to localize rhythmic activity in the sensorimotor cortex in a next step.

    % load the raw raw data
    load('S5_raw_segmented.mat')

    % filter and re-reference the raw data
    cfg               = [];
    cfg.hpfilter      = 'yes';
    cfg.hpfiltord     = 3;
    cfg.hpfreq        = 1;
    cfg.lpfilter      = 'yes';
    cfg.lpfiltord     = 3;
    cfg.lpfreq        = 249;
    cfg.bsfilter      = 'yes';
    cfg.bsfiltord     = 3;
    cfg.bsfreq        = [49 51; 99 101; 149 151; 199 201]; % EU line noise
    cfg.reref         = 'yes';
    cfg.refchannel    = 'all';
    data_filt = ft_preprocessing(cfg, data);
    
    % select electrodes placed over the sensorimotor cortex
    cfg               = [];
    cfg.channel       = {'chan007','chan008','chan015','chan016','chan024', ...
      'chan092','chan093','chan094','chan095', ...
      'chan113','chan115','chan117','chan118','chan119'};
    data_sel = ft_selectdata(cfg, data_filt);

    % segment the data into one-second overlapping chunks
    cfg               = [];
    cfg.length        = 1;
    cfg.overlap       = .95; % 95 percent overlap (sliding 50 ms)
    data_redef = ft_redefinetrial(cfg, data_sel);
    
    % compute the fractal and original spectra
    cfg               = [];
    cfg.foilim        = [1 50];
    cfg.pad           = 'nextpow2';
    cfg.method        = 'irasa';
    cfg.output        = 'fractal';
    fractal = ft_freqanalysis(cfg, data_redef);
    cfg.output        = 'original';
    original = ft_freqanalysis(cfg, data_redef);
    
    % subtract the fractal component from the power spectrum
    cfg               = [];
    cfg.parameter     = 'powspctrm';
    cfg.operation     = 'x2-x1';
    oscillatory = ft_math(cfg, fractal, original);

    % extract alpha and beta frequency bands
    figure; plot(oscillatory.freq, mean(oscillatory.powspctrm), ...
      'linewidth', 3, 'color', [.3 .3 .3])
    f = fit(oscillatory.freq', mean(oscillatory.powspctrm)', 'gauss3');
    alpha_band = [f.b1-2 f.b1+2];
    beta_band  = [f.b3-3 f.b3+3];
    yl = get(gca, 'YLim');
    p1 = patch([alpha_band flip(alpha_band)], [yl(1) yl(1) yl(2) yl(2)], [.9 .9 .9]);
    p2 = patch([beta_band flip(beta_band)], [yl(1) yl(1) yl(2) yl(2)], [.8 .8 .8]);
    uistack(p2, 'bottom'); uistack(p1, 'bottom');
    legend('alpha band', 'beta band', 'oscillatory component');
    xlabel('Frequency'); ylabel('Power');
    set(gca, 'YLim', yl);

{% include image src="/assets/img/example/irasa/IRASA_S5.png" %}

## Localizing spectral features in the sensorimotor cortex 

    % read in the cortical surface
    cortex = ft_read_headshape('S5_lh.pial');

    % plot the spatial distribution of alpha rhythmic activity
    cfg               = [];
    cfg.frequency     = alpha_band;
    cfg.avgoverfreq   = 'yes';
    alpha = ft_selectdata(cfg, oscillatory);
    
    cfg               = [];
    cfg.funparameter  = 'powspctrm';
    cfg.funcolorlim   = 'zeromax';
    cfg.method        = 'surface';
    cfg.interpmethod  = 'sphere_weighteddistance';
    cfg.sphereradius  = 10;
    cfg.camlight      = 'no';
    cfg.funcolormap   = 'parula';
    cfg.colorbar      = 'no';
    ft_sourceplot(cfg, alpha, cortex);
    view([-90 20]);
    material dull; lighting gouraud; camlight
    
    ft_plot_sens(alpha.elec, 'elecshape', 'disc', 'facecolor', [0 0 0])

{% include image src="/assets/img/example/irasa/IRASA_S5_alpha.png" %}

    % plot the spatial distribution of beta rhythmic activity
    cfg               = [];
    cfg.frequency     = beta_band;
    cfg.avgoverfreq   = 'yes';
    beta = ft_selectdata(cfg, oscillatory);
    
    cfg               = [];
    cfg.funparameter  = 'powspctrm';
    cfg.funcolorlim   = 'zeromax';
    cfg.method        = 'surface';
    cfg.interpmethod  = 'sphere_weighteddistance';
    cfg.sphereradius  = 10;
    cfg.camlight      = 'no';
    cfg.funcolormap   = 'parula';
    cfg.colorbar      = 'no';
    ft_sourceplot(cfg, beta, cortex);
    view([-90 20]);
    material dull; lighting gouraud; camlight
    
    ft_plot_sens(beta.elec, 'elecshape', 'disc', 'facecolor', [0 0 0])

{% include image src="/assets/img/example/irasa/IRASA_S5_beta.png" %}

Consistent with the findings of the [original study](https://elifesciences.org/articles/48065), alpha rhythmic activity is maximal at electrodes on the postcentral gyrus, and beta rhythmic activity is strongest at electrodes placed over the central sulcus. 


{% include markup/warning %}
Update: Starting from version 20210114 the implementation of **[ft_specest_irasa](https://github.com/fieldtrip/fieldtrip/blob/master/specest/ft_specest_irasa.m)** has changed. In short, the current implementation incorporates sub-segmentation of the data and, hence, the sub-segmentation and recombination steps no longer have to be performed outside IRASA. More details regarding this update can be found in [PR 1546](https://github.com/fieldtrip/fieldtrip/pull/1602).
{% include markup/end %}
