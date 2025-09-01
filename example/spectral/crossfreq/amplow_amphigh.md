---
title: Amplow_amphigh
---

## Help ft_freqsimulation

    % method 'amplow_amphigh
    %   signal is build up of 5 components; s1, s2, s3, s4 and noise.
    %     s1: first frequency
    %     s2: second frequency
    %     s3: DC shift of s1 and s2, should have frequency of 0
    %     s4: amplitude modulation (AM), frequency of this signal should be lower than s1 and s2
    % and the output consists of the following channel
    %     1st channel: mixed signal = (s4 + s3)*s1 + (s4 + s3)*s2 + noise,
    %     2nd channel: s1
    %     3rd channel: s2
    %     4th channel: s3
    %     5th channel: noise
    %     6th channel: s4
    %     7th channel: mixed part 1: (s4 + s3)*s1
    %     8th channel: mixed part 2: (s4 + s3)*s2

## Simulating the data

    cfg = [];
    cfg.method   = 'amplow_amphigh';
    cfg.fsample  = 1000;
    cfg.trllen   = 10;
    cfg.numtrl   = 10;
    cfg.output   = 'all';
    % first frequency
    cfg.s1.freq  = 6;
    cfg.s1.phase = 0;
    cfg.s1.ampl  = 1;
    % second frequency
    cfg.s2.freq  = 20;
    cfg.s2.phase = 0;
    cfg.s2.ampl  = 1;
    % DC shift of s1 and s2
    cfg.s3.freq  = 0;
    cfg.s3.phase = 0;
    cfg.s3.ampl  = 1; %determines amount of modulation, should be at least s4.ampl
    % amplitude modulation (AM)
    cfg.s4.freq  = 1; %frequency of this signal should be lower than s1 and s2
    cfg.s4.phase = -1*pi;
    cfg.s4.ampl  = 1;
    % noise
    cfg.noise    = 0.1;

    data = ft_freqsimulation(cfg);

## What does the signal look like?

    figure;
    sel = 1:2000;
    subplot(3,3,1); plot(data.trial{1}(1,sel)); title(data.label{1})
    subplot(3,3,2); plot(data.trial{1}(2,sel)); title(data.label{2})
    subplot(3,3,3); plot(data.trial{1}(3,sel)); title(data.label{3})
    subplot(3,3,4); plot(data.trial{1}(4,sel)); title(data.label{4})
    subplot(3,3,5); plot(data.trial{1}(5,sel)); title(data.label{5})
    subplot(3,3,6); plot(data.trial{1}(6,sel)); title(data.label{6})
    subplot(3,3,7); plot(data.trial{1}(7,sel)); title(data.label{7})
    subplot(3,3,8); plot(data.trial{1}(8,sel)); title(data.label{8})
    print -dpng amplow_amphigh_fig1.png

    % show powerspectrum simulated data
    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.channel   = 'mix';
    cfg.output    = 'pow';
    cfg.taper     = 'hanning';
    cfg.foilim    = [2 60];

    fft_data = ft_freqanalysis(cfg,data);
    figure; ft_singleplotER([],fft_data);
    print -dpng amplow_amphigh_fig2.png

{% include image src="/assets/img/example/crossfreq/amplow_amphigh/amplow_amphigh_fig1.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/amplow_amphigh/amplow_amphigh_fig2b.png" width="400" %}

## Analysis Methods

### Calculate correlation between power of power

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
    figure;
    imagesc(freq1.time, freq1.freq, squeeze(freq1.powspctrm(1,1,:,:))); axis xy
    print -dpng amplow_amphigh_fig3.png

    figure; plot(freq1.time,squeeze(freq1.powspctrm(1,1,3,:)))   % at 6 Hz
    hold on
    plot(freq1.time,squeeze(freq1.powspctrm(1,1,10,:)),'r')      % at 20 Hz
    hold on
    plot(data.time{1}(3001:7000),data.trial{1}(6,3001:7000),'g') % lowest -> original amplitude modulation
    legend('power at 6 Hz','power at 20 Hz','s4 (AM)','location','Best')
    print -dpng amplow_amphigh_fig4.png

{% include image src="/assets/img/example/crossfreq/amplow_amphigh/amplow_amphigh_fig3.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/amplow_amphigh/amplow_amphigh_fig4.png" width="400" %}

    % calculate covariance with ft_timelockanalysis
    cfg = [];
    cfg.covariance         = 'yes';
    cfg.keeptrials         = 'no';
    cfg.removemean         = 'yes';
    timelock = ft_timelockanalysis(cfg,freq1);
    freqlabel = [2:2:60];
    figure; imagesc(freqlabel,freqlabel,timelock.cov)
    title('covariance')
    colorbar
    axis xy
    print -dpng amplow_amphigh_fig5.png

    % calculate correlation
    cov = timelock.cov; % all trials
    d = sqrt(diag(cov)); % SD, diagonal is variance per channel
    r = cov ./ (d*d');
    figure; imagesc(freqlabel,freqlabel,r)
    title('correlation')
    colorbar
    axis xy
    print -dpng amplow_amphigh_fig6.png

{% include image src="/assets/img/example/crossfreq/amplow_amphigh/amplow_amphigh_fig5b.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/amplow_amphigh/amplow_amphigh_fig6.png" width="400" %}

### Coherence between amplitude envelopes (by Hilbert transform)

    cfg = [];
    cfg.hilbert = 'abs';
    cfg.channel = 'mix';
    cfg.bpfilter = 'yes';
    cfg.bpfreq   = [4 8]; %do not bandpass to tight, then amplitude modulation is lost
    data_bp6 = ft_preprocessing(cfg, data);
    data_bp6.label = {'mix@6Hz'};

    cfg.bpfreq   = [18 22];
    data_bp20 = ft_preprocessing(cfg, data);
    data_bp20.label = {'mix@20Hz'};

    data_bp = ft_appenddata([], data_bp6, data_bp20);
    figure
    plot(data_bp.time{1}, data_bp.trial{1}); legend(data_bp.label)
    print -dpng amplow_amphigh_fig7.png

{% include image src="/assets/img/example/crossfreq/amplow_amphigh/amplow_amphigh_fig7.png" width="400" %}

    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'powandcsd';
    cfg.taper     = 'hanning';
    cfg.foilim    = [0 60];
    cfg.keeptrials = 'no';
    cfg.channelcmb = {'all', 'all'};

    freq3 = ft_freqanalysis(cfg, data_bp);
    freq3_coh = ft_freqdescriptives([], freq3);

    figure
    plot(freq3_coh.freq, freq3_coh.cohspctrm);
    title('coherence between amplitude envelopes at 6 and 20 Hz');
    xlabel('frequency');
    ylabel('coherence');
    print -dpng amplow_amphigh_fig8.png

    % zoom in
    xlim([0 10]);
    print -dpng amplow_amphigh_fig9.png

{% include image src="/assets/img/example/crossfreq/amplow_amphigh/amplow_amphigh_fig8.png" width="400" %}
{% include image src="/assets/img/example/crossfreq/amplow_amphigh/amplow_amphigh_fig9.png" width="400" %}
