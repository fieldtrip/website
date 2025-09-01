---
title: How can I compute inter-trial coherence?
category: faq
tags: [coherence]
redirect_from:
    - /faq/itc/
---

Inter-trial coherence (ITC, also referred to as inter-trial phase-locking factor) is a measure of phase consistency over trials (typically within the range of zero to one). An ITC value close to 0 reflects high variability of phase angles across trials. It is not a connectivity measure, as it does not relate the phase in one channel to that of another channel. You can compute it following frequency decomposition of your data.
You can use cfg.method='mtmfft', 'mtmconvol' or 'wavelet, but in either case you should use cfg.output='fourier'. Here is an example:

    cfg        = [];
    cfg.numtrl = 100
    data       = ft_freqsimulation(cfg); % simulate some data

    cfg        = [];
    cfg.method = 'wavelet';
    cfg.toi    = 0:0.01:1;
    cfg.output = 'fourier';
    freq       = ft_freqanalysis(cfg, data);

    % make a new FieldTrip-style data structure containing the ITC
    % copy the descriptive fields over from the frequency decomposition

    itc           = [];
    itc.label     = freq.label;
    itc.freq      = freq.freq;
    itc.time      = freq.time;
    itc.dimord    = 'chan_freq_time';

    F = freq.fourierspctrm;   % copy the Fourier spectrum
    N = size(F,1);           % number of trials

    % compute inter-trial phase coherence (itpc)
    itc.itpc      = F./abs(F);         % divide by amplitude
    itc.itpc      = sum(itc.itpc,1);   % sum angles
    itc.itpc      = abs(itc.itpc)/N;   % take the absolute value and normalize
    itc.itpc      = squeeze(itc.itpc); % remove the first singleton dimension

    % compute inter-trial linear coherence (itlc)
    itc.itlc      = sum(F) ./ (sqrt(N*sum(abs(F).^2)));
    itc.itlc      = abs(itc.itlc);     % take the absolute value, i.e. ignore phase
    itc.itlc      = squeeze(itc.itlc); % remove the first singleton dimension

Finally we can plot it, just like a regular time-frequency representation

    figure
    subplot(2, 1, 1);
    imagesc(itc.time, itc.freq, squeeze(itc.itpc(1,:,:)));
    axis xy
    title('inter-trial phase coherence');
    subplot(2, 1, 2);
    imagesc(itc.time, itc.freq, squeeze(itc.itlc(1,:,:)));
    axis xy
    title('inter-trial linear coherence');

For interpretation of the ITC metric, we recommend the following paper for caveats: van Diepen, R. M., & Mazaheri, A. (2018). _The caveats of observing inter-trial phase-coherence in cognitive neuroscience._ Scientific reports, 8(1), 1-9. 

### Reference

Delorme A, Makeig S. _EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis._ J Neurosci Methods. 2004 Mar 15;134(1):9-21. [pdf](http://sccn.ucsd.edu/~scott/pdf/EEGLAB04.pdf)
