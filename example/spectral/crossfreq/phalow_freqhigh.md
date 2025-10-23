---
title: Phalow_freqhigh
---

## Help freqsimulation

    % method 'phalow_freqhigh' creates a frequency modulated signal
    %   signal is build up of 3 components; s1, s2 and noise.
    %     s1: represents the base signal that will be modulated
    %     s2: signal that will be used for the frequency modulation
    % and the output consists of the following channel
    %     1st channel: mixed signal = s1.ampl * cos(ins_pha) + noise
    %     2nd channel: s1
    %     3rd channel: s2
    %     4th channel: noise
    %     5th channel: inst_pha_base   instantaneous phase of the high (=base) frequency signal s1
    %     6th channel: inst_pha_mod    low frequency phase modulation, this is equal to s2
    %     7th channel: inst_pha        instantaneous phase, i.e. inst_pha_base + inst_pha_mod

## Simulating the data

    cfg = [];
    cfg.fsample   = 1000;
    cfg.method    = 'phalow_freqhigh';
    cfg.trllen    = 10;
    cfg.numtrl    = 10;
    cfg.s1.freq   = 20; %base frequency
    cfg.s1.phase  = 0;
    cfg.s1.ampl   = 1;
    cfg.s2.freq   = 2;
    cfg.s2.phase  = -0.5 * pi; %then base freq at t=0
    cfg.s2.ampl   = pi; % should not be too high, then diff inst phase becomes negative or very close to zero and time stops or reverses
    cfg.noise.ampl = 0;
    cfg.output = 'all';

    data = ft_freqsimulation(cfg);

## What does the signal look like?

    figure;
    sel = 1:1000;
    subplot(3,3,1); plot(data.trial{1}(1,sel)); title(data.label{1})
    subplot(3,3,2); plot(data.trial{1}(2,sel)); title(data.label{2})
    subplot(3,3,3); plot(data.trial{1}(3,sel)); title(data.label{3})
    subplot(3,3,4); plot(data.trial{1}(4,sel)); title(data.label{4})
    subplot(3,3,5); plot(data.trial{1}(5,sel)); title(data.label{5})
    subplot(3,3,6); plot(data.trial{1}(6,sel)); title(data.label{6})
    subplot(3,3,7); plot(data.trial{1}(7,sel)); title(data.label{7})
    print -dpng phalow_freqhigh_fig1.png

    figure;plot(diff(data.trial{1}(7,:))); title('diff inst phase, should not be less than or close to zero')
    print -dpng phalow_freqhigh_fig2.png

{% include image src="/assets/img/example/crossfreq/phalow_freqhigh/phalow_freqhigh_fig1.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/phalow_freqhigh/phalow_freqhigh_fig2.png" width="400" %}

    % show power spectrum simulated data
    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.channel   = 'mix';
    cfg.output    = 'pow';
    cfg.taper     = 'hanning';
    cfg.foilim    = [2 60];

    fft_data = ft_freqanalysis(cfg,data);
    figure; ft_singleplotER([],fft_data);
    print -dpng phalow_freqhigh_fig3.png

{% include image src="/assets/img/example/crossfreq/phalow_freqhigh/phalow_freqhigh_fig3.png" width="400" %}

## Analysis Methods

### Calculate power of power

    % mtmconvol 1ex
    cfg = [];
    cfg.method    = 'mtmconvol';
    cfg.channel   = 'mix';
    cfg.output    = 'pow';
    cfg.taper     = 'hanning';
    cfg.foi       = 2:2:60;
    cfg.toi       = data.time{1}(3001:7000);
    cfg.t_ftimwin = 4./cfg.foi;
    cfg.keeptrials = 'yes';

    freq1 = ft_freqanalysis(cfg,data);
    figure; imagesc(freq1.time(1:1000), freq1.freq, squeeze(freq1.powspctrm(1,1,:,1:1000)))
    axis xy
    print -dpng phalow_freqhigh_fig4.png

    % plot power at different frequencies
    pow_10Hz = squeeze(freq1.powspctrm(1,1,5,:));
    pow_12Hz = squeeze(freq1.powspctrm(1,1,6,:));
    pow_14Hz = squeeze(freq1.powspctrm(1,1,7,:));
    pow_16Hz = squeeze(freq1.powspctrm(1,1,8,:));
    pow_18Hz = squeeze(freq1.powspctrm(1,1,9,:));
    pow_20Hz = squeeze(freq1.powspctrm(1,1,10,:));
    pow_22Hz = squeeze(freq1.powspctrm(1,1,11,:));
    pow_24Hz = squeeze(freq1.powspctrm(1,1,12,:));
    pow_26Hz = squeeze(freq1.powspctrm(1,1,13,:));
    pow_28Hz = squeeze(freq1.powspctrm(1,1,14,:));
    pow_30Hz = squeeze(freq1.powspctrm(1,1,15,:));
    figure;
    subplot(3,4,1); plot(freq1.time(1:1000),pow_10Hz(1:1000));title('pow @ 10 Hz');ylim([0 0.4])
    subplot(3,4,2); plot(freq1.time(1:1000),pow_12Hz(1:1000));title('pow @ 12 Hz');ylim([0 0.4])
    subplot(3,4,3); plot(freq1.time(1:1000),pow_14Hz(1:1000));title('pow @ 14 Hz');ylim([0 0.4])
    subplot(3,4,4); plot(freq1.time(1:1000),pow_16Hz(1:1000));title('pow @ 16 Hz');ylim([0 0.4])
    subplot(3,4,5); plot(freq1.time(1:1000),pow_18Hz(1:1000));title('pow @ 18 Hz');ylim([0 0.4])
    subplot(3,4,6); plot(freq1.time(1:1000),pow_20Hz(1:1000));title('pow @ 20 Hz');ylim([0 0.4])
    subplot(3,4,7); plot(freq1.time(1:1000),pow_22Hz(1:1000));title('pow @ 22 Hz');ylim([0 0.4])
    subplot(3,4,8); plot(freq1.time(1:1000),pow_24Hz(1:1000));title('pow @ 24 Hz');ylim([0 0.4])
    subplot(3,4,9); plot(freq1.time(1:1000),pow_26Hz(1:1000));title('pow @ 26 Hz');ylim([0 0.4])
    subplot(3,4,10); plot(freq1.time(1:1000),pow_28Hz(1:1000));title('pow @ 28 Hz');ylim([0 0.4])
    subplot(3,4,11); plot(freq1.time(1:1000),pow_30Hz(1:1000));title('pow @ 30 Hz');ylim([0 0.4])
    print -dpng phalow_freqhigh_fig5.png

{% include image src="/assets/img/example/crossfreq/phalow_freqhigh/phalow_freqhigh_fig4b.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/phalow_freqhigh/phalow_freqhigh_fig5.png" width="400" %}

    % mtmfft on freq1 with output power
    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'pow';
    cfg.taper     = 'hanning';
    cfg.foilim    = [2 60];
    cfg.keeptrials = 'no';

    freq2 = ft_freqanalysis(cfg,freq1); %FieldTrip automatically converts the freq1 data to raw data.
                                   %Every frequency in the power spectrum is converted to a a channel labeled mix@xxHz

    freq2.freq2 = [2:2:60];

    %plot
    figure; imagesc(freq2.freq, freq2.freq2, freq2.powspctrm)
    axis xy
    print -dpng phalow_freqhigh_fig6.png

    %zoom in
    figure; imagesc(freq2.freq(1:33), freq2.freq2(5:15), freq2.powspctrm(5:15,1:33))
    axis xy
    print -dpng phalow_freqhigh_fig7.png

{% include image src="/assets/img/example/crossfreq/phalow_freqhigh/phalow_freqhigh_fig6.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/phalow_freqhigh/phalow_freqhigh_fig7.png" width="400" %}

In figure 7 you can see that most frequencies are modulated at 2 Hz, which was indeed the frequency of the modulation (s2 in data). Harmonics are seen at 4 and 6 Hz. The base frequency (20 Hz, s1 in data) is the only frequency that shows the strongest correlation with the modulation frequency (s2.freq = 2Hz) \* 2 = 4Hz.

### Calculate power of derivative of estimated instanteneous phase

    % bandpass
    cfg = [];
    cfg.channel = 'mix';
    cfg.bpfilter = 'yes';
    cfg.bpfreq = [10 40];
    data_bp = ft_preprocessing(cfg,data);

    % check
    figure;
    sel = 1:1000;
    plot(data.trial{1}(1,sel))
    hold on
    plot(data_bp.trial{1}(1,sel),'r')
    legend('original data','bandpassed data','location','Best')
    print -dpng phalow_freqhigh_fig8.png

    % estimate instantaneous phase by angle Hilbert
    cfg = [];
    cfg.channel = 'mix';
    cfg.hilbert = 'angle';
    data_H = ft_preprocessing(cfg,data_bp);

    % check
    figure;
    sel = 1:1000;
    plot(data.trial{1}(7,sel));
    hold on
    plot(data_H.trial{1}(1,sel),'r')
    legend(data.label{7},'estimated ins phase','location','Best')
    print -dpng phalow_freqhigh_fig9.png

{% include image src="/assets/img/example/crossfreq/phalow_freqhigh/phalow_freqhigh_fig8.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/phalow_freqhigh/phalow_freqhigh_fig9.png" width="400" %}

    % calculate derivative of instantaneous phase
    cfg = [];
    cfg.channel = 'mix';
    cfg.absdiff = 'yes'
    data_diff = ft_preprocessing(cfg,data_H);

    % check
    figure;
    sel = 1:3000;
    plot(data_diff.trial{1}(1,sel),'r')
    print -dpng phalow_freqhigh_fig10.png

    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'pow';
    cfg.taper     = 'hanning';
    cfg.foilim    = [1 20];
    cfg.keeptrials = 'no';

    fft_data_diff = ft_freqanalysis(cfg, data_diff);
    figure; ft_singleplotER([],fft_data_diff);
    print -dpng phalow_freqhigh_fig11.png

{% include image src="/assets/img/example/crossfreq/phalow_freqhigh/phalow_freqhigh_fig10.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/phalow_freqhigh/phalow_freqhigh_fig11.png" width="400" %}
