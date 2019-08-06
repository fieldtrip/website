---
title: Irregular Resampling Auto-Spectral Analysis (IRASA)
tags: [example, irasa]
---

# Irregular Resampling Auto-Spectral Analysis (IRASA)

IRASA allows distinguishing rhythmic activity from concurrent power-spectral 1/f modulations. The technique virtually compresses and expands the time-domain data with a set of non-integer resampling factors prior to Fourier-based spectral decomposition. As a result, rhythmic components in the power-spectrum are redistributed while the arrhythmic 1/f distribution is left intact. Taking the median of the resulting auto-spectral distributions extracts the power-spectral 1/f component, and the subsequent removal of the 1/f component from the original power-spectrum offers a power-spectral estimate of rhythmic content in the recorded signal.

The below MATLAB script demonstrates the use of the [IRASA technique](https://link.springer.com/article/10.1007/s10548-015-0448-0) (on simulated data) for the purpose of [extracting rhythmic spectral features](https://www.biorxiv.org/content/10.1101/636241v2) from the electrophysiological signal.


    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % MATLAB script for the extraction of rhythmic spectral features 
    % from the electrophysiological signal based on Irregular Resampling
    % Auto-Spectral Analysis (IRASA, Wen & Liu, Brain Topogr. 2016)
    %
    % Ensure FieldTrip is correcty added to the MATLAB path:
    %   addpath <path to fieldtrip home directory>
    %   ft_defaults
    %
    % From Stolk et al., Electrocorticographic dissociation of alpha and 
    % beta rhythmic activity in the human sensorimotor system
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    % generate trials with a 15 Hz oscillation embedded in pink noise
    t = (1:1000)/1000; % time axis
    for rpt = 1:100
      % generate pink noise
      dspobj = dsp.ColoredNoise('Color', 'pink', ...
        'SamplesPerFrame', length(t));
      fn = dspobj()';
      
      % add a 15 Hz oscillation
      data.trial{1,rpt} = fn + cos(2*pi*15*t); 
      data.time{1,rpt}  = t;
      data.label{1}     = 'chan';
      data.trialinfo(rpt,1) = rpt;
    end
    
    % partition the data into ten overlapping sub-segments
    w = data.time{1}(end)-data.time{1}(1); % window length
    cfg               = [];
    cfg.length        = w*.9;
    cfg.overlap       = 1-((w-cfg.length)/(10-1));
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
    for rpt = unique(frac_r.trialinfo)'
      cfg               = [];
      cfg.trials        = find(frac_r.trialinfo==rpt);
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
    mean = f.b1;
    std  = f.c1/sqrt(2)*2.3548;
    fwhm = [mean-std/2 mean+std/2];
    yl   = get(gca, 'YLim');
    p = patch([fwhm flip(fwhm)], [yl(1) yl(1) yl(2) yl(2)], [1 1 1]);
    uistack(p, 'bottom');
    legend('FWHM oscillation', 'Fractal component', 'Power spectrum');
    xlabel('Frequency'); ylabel('Power');
    set(gca, 'YLim', yl);

