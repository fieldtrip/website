---
title: Phalow_amphigh
---

## Help ft_freqsimulation

    % In the method 'phalow_amphigh' the signal is build up of 4 components; s1, s2, s3 and nois
    %     s1: amplitude modulation (AM), frequency of this signal should be lower than s2
    %     s2: second frequency, frequncy that becomes amplitude modulated
    %     s3: DC shift of s1, should have frequency of 0
    % and the output consists of the following channel
    %     1st channel: mixed signal = (s1 + s3)*s2 + noise,
    %     2nd channel: s1
    %     3rd channel: s2
    %     4th channel: s3
    %     5th channel: noise

## Simulating the data

    clear all; close all;

    cfg = [];
    cfg.method     = 'phalow_amphigh';
    cfg.fsample    = 1000;
    cfg.trllen     = 10;
    cfg.numtrl     = 10;
    cfg.output     = 'all';
    % amplitude modulation
    cfg.s1.freq    = 6;
    cfg.s1.phase   = 'random'; %phase differs over trials
    cfg.s1.ampl    = 1;
    % frequency that becomes modulated
    cfg.s2.freq    = 40;
    cfg.s2.phase   = 'random'; %phase differs over trials
    cfg.s2.ampl    = 1;
    % DC shift of S1
    cfg.s3.freq    = 0;
    cfg.s3.phase   = 0;
    cfg.s3.ampl    = 1; %determines amount of modulation, should be at least s1.ampl
    % noise
    cfg.noise.ampl = 0.5;

## What does the signal look like?

    data = ft_freqsimulation(cfg);
    figure;
    sel = 1:1000;
    subplot(3,3,1); plot(data.trial{1}(1,sel)); title(data.label{1})
    subplot(3,3,2); plot(data.trial{1}(2,sel)); title(data.label{2})
    subplot(3,3,3); plot(data.trial{1}(3,sel)); title(data.label{3})
    subplot(3,3,4); plot(data.trial{1}(4,sel)); title(data.label{4})
    subplot(3,3,5); plot(data.trial{1}(5,sel)); title(data.label{5})
    print -dpng phalow_amphigh_fig1.png

    % show power spectrum simulated data
    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.channel   = 'mix';
    cfg.output    = 'pow';
    cfg.taper     = 'hanning';
    cfg.foilim    = [2 60];

    fft_data = ft_freqanalysis(cfg,data);
    figure; ft_singleplotER([],fft_data);
    print -dpng phalow_amphigh_fig2.png

{% include image src="/assets/img/example/crossfreq/phalow_amphigh/phalow_amphigh_fig1.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/phalow_amphigh/phalow_amphigh_fig2.png" width="400" %}

## Analysis Methods

### Calculate power of power

    % mtmconvol
    cfg = [];
    cfg.method    = 'mtmconvol';
    cfg.channel   = 'mix';
    cfg.output    = 'pow';
    cfg.taper     = 'hanning';
    cfg.foi       = 2:2:60;
    cfg.toi       = data.time{1}(3001:7000); %power is calculated at every sample
    cfg.t_ftimwin = 4./cfg.foi; %timewindow used to calculated power is 4 cycles long and therefore differs over frequencies
    cfg.keeptrials = 'yes';

    freq1 = ft_freqanalysis(cfg,data);

    figure; imagesc(freq1.time, freq1.freq, squeeze(freq1.powspctrm(1,1,:,:)))
    axis xy
    print -dpng phalow_amphigh_fig3.png

    % mtmfft output power
    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'pow';
    cfg.taper     = 'hanning';
    cfg.foilim    = [2 60];
    cfg.keeptrials = 'no';

    freq2 = ft_freqanalysis(cfg,freq1); %FieldTrip automatically converts the freq1 data to raw data.
                                   %Every frequency in the power spectrum is converted to a a channel labeled mix@xxHz

    freq2.freq2 = [2:2:60];
    figure; imagesc(freq2.freq, freq2.freq2, freq2.powspctrm)
    axis xy
    print -dpng phalow_amphigh_fig4.png

{% include image src="/assets/img/example/crossfreq/phalow_amphigh/phalow_amphigh_fig3.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/phalow_amphigh/phalow_amphigh_fig4.png" width="400" %}

### Calculate coherence between power and raw

    % mtmconvol
    cfg = [];
    cfg.method    = 'mtmconvol';
    cfg.channel   = 'mix';
    cfg.output    = 'pow';
    cfg.taper     = 'hanning';
    cfg.foi       = 2:2:60;
    cfg.toi       = data.time{1}(3001:7000); %power is calculated at every sample
    cfg.t_ftimwin = 4./cfg.foi; %timewindow used to calculated power is 4 cycles long and therefore differs over frequencies
    cfg.keeptrials = 'yes';

    freq1 = ft_freqanalysis(cfg,data);

    % Make data same length as freq1
    data_cut = data;
    for iTr = 1:length(data.trial)
    data_cut.trial{iTr} = data.trial{iTr}(:,3001:7000);
    data_cut.time{iTr}  = data.time{iTr}(3001:7000);
    end

    data_app = ft_appenddata([],data_cut, freq1); %contains original channel and channels with power
                                             %FieldTrip automatically converts the freq1 data to raw data.

    % mtmfft output cross-spectral-density between mix(raw) and freq1
    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'powandcsd';
    cfg.taper     = 'hanning';
    cfg.foilim    = [2 60];
    cfg.keeptrials = 'no';
    cfg.pad = 4;
    cfg.channelcmb = {'mix' 'mix@2Hz'; 'mix' 'mix@4Hz'; 'mix' 'mix@6Hz'; 'mix' 'mix@8Hz'; 'mix' 'mix@10Hz'; 'mix' 'mix@12Hz'; 'mix' 'mix@14Hz'; 'mix' 'mix@16Hz'; 'mix' 'mix@18Hz'; 'mix' 'mix@20Hz'; 'mix' 'mix@22Hz'; 'mix' 'mix@24Hz'; 'mix' 'mix@26Hz'; 'mix' 'mix@28Hz'; 'mix' 'mix@30Hz'; 'mix' 'mix@32Hz'; 'mix' 'mix@34Hz'; 'mix' 'mix@36Hz'; 'mix' 'mix@38Hz'; 'mix' 'mix@40Hz'; 'mix' 'mix@42Hz'; 'mix' 'mix@44Hz'; 'mix' 'mix@46Hz'; 'mix' 'mix@48Hz'; 'mix' 'mix@50Hz'; 'mix' 'mix@52Hz'; 'mix' 'mix@54Hz'; 'mix' 'mix@56Hz'; 'mix' 'mix@58Hz'; 'mix' 'mix@60Hz';};

    freq2 = ft_freqanalysis(cfg,data_app);

    % calculate coherence
    coh = ft_freqdescriptives([],freq2);

    coh.freq2 = [2:2:60];
    figure; imagesc(coh.freq, coh.freq2, coh.powspctrm)
    axis xy
    print -dpng phalow_amphigh_fig5.png

{% include image src="/assets/img/example/crossfreq/phalow_amphigh/phalow_amphigh_fig5.png" width="400" %}

    % mtmfft output cross-spectral-density between s1 (AM)(raw) and freq1
    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'powandcsd';
    cfg.taper     = 'hanning';
    cfg.foilim    = [2 60];
    cfg.keeptrials = 'no';
    cfg.pad = 4;
    cfg.channelcmb = {'s1 (AM)' 'mix@2Hz'; 's1 (AM)' 'mix@4Hz'; 's1 (AM)' 'mix@6Hz'; 's1 (AM)' 'mix@8Hz'; 's1 (AM)' 'mix@10Hz'; 's1 (AM)' 'mix@12Hz'; 's1 (AM)' 'mix@14Hz'; 's1 (AM)' 'mix@16Hz'; 's1 (AM)' 'mix@18Hz'; 's1 (AM)' 'mix@20Hz'; 's1 (AM)' 'mix@22Hz'; 's1 (AM)' 'mix@24Hz'; 's1 (AM)' 'mix@26Hz'; 's1 (AM)' 'mix@28Hz'; 's1 (AM)' 'mix@30Hz'; 's1 (AM)' 'mix@32Hz'; 's1 (AM)' 'mix@34Hz'; 's1 (AM)' 'mix@36Hz'; 's1 (AM)' 'mix@38Hz'; 's1 (AM)' 'mix@40Hz'; 's1 (AM)' 'mix@42Hz'; 's1 (AM)' 'mix@44Hz'; 's1 (AM)' 'mix@46Hz'; 's1 (AM)' 'mix@48Hz'; 's1 (AM)' 'mix@50Hz'; 's1 (AM)' 'mix@52Hz'; 's1 (AM)' 'mix@54Hz'; 's1 (AM)' 'mix@56Hz'; 's1 (AM)' 'mix@58Hz'; 's1 (AM)' 'mix@60Hz';};
    freq2 = ft_freqanalysis(cfg,data_app);

    %calculate coherence
    coh = ft_freqdescriptives([],freq2);

    coh.freq2 = [2:2:60];
    figure; imagesc(coh.freq, coh.freq2, coh.powspctrm)
    axis xy
    print -dpng phalow_amphigh_fig6.png

{% include image src="/assets/img/example/crossfreq/phalow_amphigh/phalow_amphigh_fig6.png" width="400" %}

### Power spectrum of amplitude envelope (by Hilbert transform)

    % bandpass and hilbert (is automaticly abs of hilbert in ft_preprocessing)
    cfg = [];
    cfg.channel    = 'mix';
    cfg.bpfilter   = 'yes';
    cfg.bpfreq     = [30 50];
    cfg.hilbert    = 'yes';
    cfg.keeptrials = 'yes';
    data_hilbert = ft_preprocessing(cfg,data);

    figure
    plot(data.time{1}(sel),data.trial{1}(1,sel))
    hold on
    plot(data_hilbert.time{1}(sel),data_hilbert.trial{1}(sel),'r', 'linewidth', 2)
    print -dpng phalow_amphigh_fig7.png

    % calculate power spectrum of hilbert data
    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.channel   = 'mix';
    cfg.output    = 'pow';
    cfg.taper     = 'hanning';
    cfg.foilim    = [2 60];

    fft_hilbert = ft_freqanalysis(cfg,data_hilbert);

    % plot power spectrum
    cfg = []
    cfg.xlim = [1 20];
    figure; ft_singleplotER(cfg,fft_hilbert);
    print -dpng phalow_amphigh_fig8.png

{% include image src="/assets/img/example/crossfreq/phalow_amphigh/phalow_amphigh_fig7.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/phalow_amphigh/phalow_amphigh_fig8.png" width="400" %}
