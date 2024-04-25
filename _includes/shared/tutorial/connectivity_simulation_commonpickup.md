When working with electrophysiological data (EEG/MEG/LFP) the signals that are picked up by the individual channels invariably consist of instantaneous mixtures of the underlying source signals. This mixing can severely affect the outcome of connectivity analysis, and thus affects the interpretation. We will demonstrate this by simulating data in two channels, where each of the channels consists of a weighted combination of temporal white noise unique to each of the channels, and a common input of a band-limited signal (filtered between 15 and 25 Hz). We will compute connectivity between these channels, and show that the common input can give rise to spurious estimates of connectivity.

    % create some instantaneously mixed data

    % define some variables locally
    nTrials  = 100;
    nSamples = 1000;
    fsample  = 1000;

    % mixing matrix
    mixing   = [0.8 0.2 0;
                  0 0.2 0.8];

    data       = [];
    data.trial = cell(1,nTrials);
    data.time  = cell(1,nTrials);
    for k = 1:nTrials
      dat = randn(3, nSamples);
      dat(2,:) = ft_preproc_bandpassfilter(dat(2,:), 1000, [15 25]);
      dat = 0.2.*(dat-repmat(mean(dat,2),[1 nSamples]))./repmat(std(dat,[],2),[1 nSamples]);
      data.trial{k} = mixing * dat;
      data.time{k}  = (0:nSamples-1)./fsample;
    end
    data.label = {'chan1' 'chan2'}';

    figure;plot(dat'+repmat([0 1 2],[nSamples 1]));
    title('original ''sources''');

    figure;plot((mixing*dat)'+repmat([0 1],[nSamples 1]));
    axis([0 1000 -1 2]);
    set(findobj(gcf,'color',[0 0.5 0]), 'color', [1 0 0]);
    title('mixed ''sources''');

{% include image src="/assets/img/shared/tutorial/connectivity_simulation_commonpickup/figure1.png" width="300" %}

{% include image src="/assets/img/shared/tutorial/connectivity_simulation_commonpickup/figure2.png" width="300" %}

    % do spectral analysis
    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'fourier';
    cfg.foilim    = [0 200];
    cfg.tapsmofrq = 5;
    freq          = ft_freqanalysis(cfg, data);
    fd            = ft_freqdescriptives(cfg, freq);

    figure;plot(fd.freq, fd.powspctrm);
    set(findobj(gcf,'color',[0 0.5 0]), 'color', [1 0 0]);
    title('power spectrum');

{% include image src="/assets/img/shared/tutorial/connectivity_simulation_commonpickup/figure3.png" width="300" %}

    % compute connectivity
    cfg = [];
    cfg.method = 'granger';
    g = ft_connectivityanalysis(cfg, freq);
    cfg.method = 'coh';
    c = ft_connectivityanalysis(cfg, freq);


    % visualize the results
    cfg = [];
    cfg.parameter = 'grangerspctrm';
    figure; ft_connectivityplot(cfg, g);
    cfg.parameter = 'cohspctrm';
    figure; ft_connectivityplot(cfg, c);

{% include image src="/assets/img/shared/tutorial/connectivity_simulation_commonpickup/figure4.png" width="400" %} {% include image src="/assets/img/shared/tutorial/connectivity_simulation_commonpickup/mixingcoherence.png" width="400" %}

#### Exercise 5

{% include markup/skyblue %}
Simulate new data using the following mixing matrix:

    [0.9 0.1 0;0 0.2 0.8]

and recompute the connectivity measures. Discuss what you see.
{% include markup/end %}

#### Exercise 6

{% include markup/skyblue %}
Play a bit with the parameters in the mixing matrix and see what is the effect on the estimated connectivity.
{% include markup/end %}

#### Exercise 7

{% include markup/skyblue %}
Simulate new data where the 2 mixed signals are created from 4 underlying sources, and where two of these sources are common input to both signals, and where these two sources are temporally shifted copies of one another.

Hint: the mixing matrix could look like this:

    [a b c 0; 0 d e f];

and the trials could be created like this:

    for k = 1:nTrials
      dat = randn(4, nSamples+10);
      dat(2,:) = ft_preproc_bandpassfilter(dat(2,:), 1000, [15 25]);
      dat(3,1:(nSamples)) = dat(2,11:(nSamples+10));
      dat = dat(:,1:1000);
      dat = 0.2.*(dat-repmat(mean(dat,2),[1 nSamples]))./repmat(std(dat,[],2),[1 nSamples]);
      data.trial{k} = mixing * dat;
      data.time{k}  = (0:nSamples-1)./fsample;
    end

Compute connectivity between the signals and discuss what you observe. In particular, also compute measures of directed interaction.
{% include markup/end %}
