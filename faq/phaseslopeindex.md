---
title: How to interpret the sign of the phase slope index?
parent: Spectral analysis
category: faq
tags: [coherence]
redirect_from:
    - /faq/how_to_interpret_the_sign_of_the_phase_slope_index/
---

# How to interpret the sign of the phase slope index?

The phase slope index is a bivariate measure that quantifies the consistency of the phase lag (or lead) as a function of frequency, between two signals. A value that is deviating substantially from zero, for a wider frequency range, suggests that one of the signals is consistently leading the other one, which in itself is suggestive of a 'causal' (at least a time-delayed) interaction between the two signals. What does the sign of the phase slope index mean, i.e. which signal is leading which?

The answer to this question is that a positive value of the phase slope index indicates that the first signal is leading the second signal. First and second signal are defined based on the order of the channels in the labelcmb field (if the data has this field). Alternatively, if the data are defined as an NxN(xNfrequency) matrix, the channel in the row is leading the channel in the column (in this case the channel names are defined in the label field of the variable.

Alternative to the answer above, if you're unsure what's going on, you can always simulate some data for which you know the time-lag, and see what happens with the phase slope index. If in doubt, simulate!

The following chunk of code provides data that would allow you to answer the above question yourself:

    clear all;
    
    % simulate some data
    fsample = 1000;
    nsample = fsample*30;
     
    dat = randn(1,nsample+100);
     
    data.trial{1}(1,:) = dat(1,1:nsample) + 0.1.*randn(1,nsample);
    data.trial{1}(2,:) = dat(1,100+(1:nsample)) + 0.1.*randn(1,nsample);
    data.time{1} = (1:nsample)./fsample;
    data.label   = {'a';'b'}; % channel 2 is leading channel 1
     
    figure;plot(data.time{1},data.trial{1}); xlim([0 1]);
     
    % cut into 2 second snippets
    cfg = [];
    cfg.length = 2;
    data = ft_redefinetrial(cfg, data);
     
    % spectral decomposition
    cfg = [];
    cfg.method = 'mtmfft';
    cfg.output = 'fourier';
    cfg.tapsmofrq = 2;
    cfg.foilim = [0 100];
    freq = ft_freqanalysis(cfg, data);
     
    % connectivity estimation
    cfg = [];
    cfg.method = 'psi';
    cfg.bandwidth = 5;
    psi = ft_connectivityanalysis(cfg, freq);
     
    % visualization
    cfg = [];
    cfg.parameter = 'psispctrm';
    ft_connectivityplot(cfg, psi);
