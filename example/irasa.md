---
title: Irregular Resampling Auto-Spectral Analysis (IRASA)
tags: [example, irasa]
---

# Irregular Resampling Auto-Spectral Analysis (IRASA)

IRASA allows distinguishing rhythmic activity from concurrent power-spectral 1/f modulations. The technique virtually compresses and expands the time-domain data with a set of non-integer resampling factors prior to Fourier-based spectral decomposition. As a result, rhythmic components in the power-spectrum are redistributed while the arrhythmic 1/f distribution is left intact. Taking the median of the resulting auto-spectral distributions extracts the power-spectral 1/f component, and the subsequent removal of the 1/f component from the original power-spectrum offers a power-spectral estimate of rhythmic content in the recorded signal. Together, this procedure allows defining spectral distributions on a participant-by-partipant basis (e.g., participant-specific alpha frequency bands), avoiding reliance on canonical frequency bands that may not accurately capture the neural phenomena of interest in each individual.

Below we demonstrate the use of the [IRASA technique](https://link.springer.com/article/10.1007/s10548-015-0448-0) for [extracting rhythmic spectral features](https://elifesciences.org/articles/48065) on simulated data and on human ECoG data. Please cite these papers when you use the procedure described here.

## Extracting rhythmic spectral features from simulated data

    % generate trials with a 10 Hz oscillation embedded in pink noise
    t = (1:1000)/1000; % time axis
    for rpt = 1:100
      % generate pink noise
      dspobj = dsp.ColoredNoise('Color', 'pink', ...
        'SamplesPerFrame', length(t));
      fn = dspobj()';
      
      % add a 10 Hz oscillation
      data.trial{1,rpt} = fn + cos(2*pi*10*t); 
      data.time{1,rpt}  = t;
      data.label{1}     = 'chan';
      data.trialinfo(rpt,1) = rpt;
    end
    
    % partition the data into ten overlapping sub-segments
    w = data.time{1}(end)-data.time{1}(1); % window length
    cfg               = [];
    cfg.length        = w*.9;
    cfg.overlap       = 1-(((w-cfg.length)/cfg.length)/(10-1));
    data_r = ft_redefinetrial(cfg, data);
    
    % perform IRASA and regular spectral analysis
    cfg               = [];
    cfg.foilim        = [1 50];
    cfg.taper         = 'hanning';
    cfg.pad           = 'nextpow2';
    cfg.keeptrials    = 'yes';
    cfg.method        = 'irasa';
    frac_r = ft_freqanalysis(cfg, data_r);
    cfg.method        = 'mtmfft';
    orig_r = ft_freqanalysis(cfg, data_r);
    
    % average across the sub-segments
    frac_s = {}; 
    orig_s = {};
    for rpt = unique(frac_r.trialinfo(:,end))'
      cfg               = [];
      cfg.trials        = find(frac_r.trialinfo(:,end)==rpt);
      cfg.avgoverrpt    = 'yes';
      frac_s{end+1} = ft_selectdata(cfg, frac_r);
      orig_s{end+1} = ft_selectdata(cfg, orig_r);
    end
    frac_a = ft_appendfreq([], frac_s{:});
    orig_a = ft_appendfreq([], orig_s{:});
    
    % average across trials
    cfg               = [];
    cfg.trials        = 'all';
    cfg.avgoverrpt    = 'yes';
    frac = ft_selectdata(cfg, frac_a);
    orig = ft_selectdata(cfg, orig_a);
    
    % subtract the fractal component from the power spectrum
    cfg               = [];
    cfg.parameter     = 'powspctrm';
    cfg.operation     = 'x2-x1';
    osci = ft_math(cfg, frac, orig);
    
    % plot the fractal component and the power spectrum 
    figure; plot(frac.freq, frac.powspctrm, ...
      'linewidth', 3, 'color', [0 0 0])
    hold on; plot(orig.freq, orig.powspctrm, ...
      'linewidth', 3, 'color', [.6 .6 .6])
    
    % plot the full-width half-maximum of the oscillatory component
    f    = fit(osci.freq', osci.powspctrm', 'gauss1');
    avg  = f.b1;
    sd   = f.c1/sqrt(2)*2.3548;
    fwhm = [avg-sd/2 avg+sd/2];
    yl   = get(gca, 'YLim');
    p = patch([fwhm flip(fwhm)], [yl(1) yl(1) yl(2) yl(2)], [.9 .9 .9]);
    uistack(p, 'bottom');
    legend('FWHM oscillation', 'Fractal component', 'Power spectrum');
    xlabel('Frequency'); ylabel('Power');
    set(gca, 'YLim', yl);

FIXME: add figure

## Extracting rhythmic spectral features from human ECoG data

    % download human ECoG dataset from https://osf.io/z4hfm/
    load('S5_raw_segmented.mat')
    cortex = ft_read_headshape('S5_lh.pial');
    
    % filter and re-reference the raw data
    cfg               = [];
    cfg.hpfilter      = 'yes'; % high-pass in order to get rid of low-freq trends
    cfg.hpfiltord     = 3;
    cfg.hpfreq        = 1;
    cfg.lpfilter      = 'yes'; % low-pass in order to get rid of high-freq noise
    cfg.lpfiltord     = 3;
    cfg.lpfreq        = 249; % 249 when combining with a linenoise bandstop filter
    cfg.bsfilter      = 'yes'; % band-stop filter, to take out 50 Hz and its harmonics
    cfg.bsfiltord     = 3;
    cfg.bsfreq        = [49 51; 99 101; 149 151; 199 201]; % EU line noise
    cfg.reref         = 'yes';
    cfg.refchannel    = 'all';
    data_f = ft_preprocessing(cfg, data);
    
    % segment the data into one-second non-overlapping chunks
    cfg               = [];
    cfg.length        = 1;
    cfg.overlap       = 0;
    data_c = ft_redefinetrial(cfg, data_f);
    
    % partition the data into ten overlapping sub-segments
    w = data_c.time{1}(end)-data_c.time{1}(1); % window length
    cfg               = [];
    cfg.length        = w*.9;
    cfg.overlap       = 1-(((w-cfg.length)/cfg.length)/(10-1));
    data_r = ft_redefinetrial(cfg, data_c);
    
    % perform IRASA and regular spectral analysis
    cfg               = [];
    cfg.foilim        = [1 50];
    cfg.taper         = 'hanning';
    cfg.pad           = 'nextpow2';
    cfg.keeptrials    = 'yes';
    cfg.method        = 'irasa';
    frac_r = ft_freqanalysis(cfg, data_r);
    cfg.method        = 'mtmfft';
    orig_r = ft_freqanalysis(cfg, data_r);
    
    % average across the sub-segments
    frac_s = {}; 
    orig_s = {};
    for rpt = unique(frac_r.trialinfo(:,end))'
      cfg               = [];
      cfg.trials        = find(frac_r.trialinfo(:,end)==rpt);
      cfg.avgoverrpt    = 'yes';
      frac_s{end+1} = ft_selectdata(cfg, frac_r);
      orig_s{end+1} = ft_selectdata(cfg, orig_r);
    end
    frac_a = ft_appendfreq([], frac_s{:});
    orig_a = ft_appendfreq([], orig_s{:});
    
    % sensorimotor channels
    sensorimotor = {'chan007','chan008','chan015','chan016','chan024', ...
      'chan092','chan093','chan094','chan095', ...
      'chan113','chan115','chan117','chan118','chan119'};
    
    % average across trials
    cfg               = [];
    cfg.trials        = 'all';
    cfg.avgoverrpt    = 'yes';
    cfg.channel       = sensorimotor;
    frac = ft_selectdata(cfg, frac_a);
    orig = ft_selectdata(cfg, orig_a);
    
    % subtract the fractal component from the power spectrum
    cfg               = [];
    cfg.parameter     = 'powspctrm';
    cfg.operation     = 'x2-x1';
    osci = ft_math(cfg, frac, orig);
    
    % plot the fractal component and the power spectrum 
    figure; plot(frac.freq, mean(frac.powspctrm), ...
      'linewidth', 3, 'color', [0 0 0])
    hold on; plot(orig.freq, mean(orig.powspctrm), ...
      'linewidth', 3, 'color', [.6 .6 .6])
    
    % plot the full-width half-maximum of the oscillatory components
    f    = fit(osci.freq', mean(osci.powspctrm)', 'gauss3');
    avg  = f.b1;
    sd  = f.c1/sqrt(2)*2.3548;
    alpha_fwhm = [avg-sd/2 avg+sd/2];
    yl   = get(gca, 'YLim');
    p = patch([alpha_fwhm flip(alpha_fwhm)], [yl(1) yl(1) yl(2) yl(2)], [.9 .9 .9]);
    uistack(p, 'bottom');
    avg  = f.b3;
    sd  = f.c3/sqrt(2)*2.3548;
    beta_fwhm = [avg-sd/2 avg+sd/2];
    yl   = get(gca, 'YLim');
    p = patch([beta_fwhm flip(beta_fwhm)], [yl(1) yl(1) yl(2) yl(2)], [.9 .9 .9]);
    uistack(p, 'bottom');
    legend('FWHM alpha', 'FWHM beta', 'Fractal component', 'Power spectrum');
    xlabel('Frequency'); ylabel('Power');
    set(gca, 'YLim', yl);

FIXME: add figure

    % plot the spatial distribution of the alpha oscillatory component
    cfg               = [];
    cfg.frequency     = alpha_fwhm;
    cfg.avgoverfreq   = 'yes';
    alpha_osci = ft_selectdata(cfg, osci);
    
    cfg               = [];
    cfg.funparameter  = 'powspctrm';
    cfg.funcolorlim   = 'maxabs';
    cfg.method        = 'surface';
    cfg.interpmethod  = 'sphere_weighteddistance';
    cfg.sphereradius  = 10;
    cfg.camlight      = 'no';
    cfg.funcolormap   = 'parula';
    cfg.colorbar      = 'yes';
    ft_sourceplot(cfg, alpha_osci, cortex);

FIXME: add figure
        
    % plot the spatial distribution of the beta oscillatory component
    cfg               = [];
    cfg.frequency     = beta_fwhm;
    cfg.avgoverfreq   = 'yes';
    beta_osci = ft_selectdata(cfg, osci);
    
    cfg               = [];
    cfg.funparameter  = 'powspctrm';
    cfg.funcolorlim   = 'maxabs';
    cfg.method        = 'surface';
    cfg.interpmethod  = 'sphere_weighteddistance';
    cfg.sphereradius  = 10;
    cfg.camlight      = 'no';
    cfg.funcolormap   = 'parula';
    cfg.colorbar      = 'yes';
    ft_sourceplot(cfg, beta_osci, cortex);
    
FIXME: add figure
