---
title: Analysis of sensor- and source-level connectivity
category: tutorial
tags: [freq, connectivity, coherence, granger, dtf, pdc]
---

# Analysis of sensor- and source-level connectivity

## Introduction

{% include /shared/tutorial/connectivity_simulation_intro.md %}

{% include markup/skyblue %}
This tutorial contains hands-on material that we use for the [MEG/EEG toolkit course](/workshop/toolkit2015) and it is complemented by this lecture.

{% include youtube id="ZBwh0Vm4fh4" %}
{% include markup/end %}

## Background

{% include /shared/tutorial/connectivity_simulation_background.md %}

## Procedure

This tutorial consists of three parts:

- **Simulated data with directed connections**: In this part we are going to simulate some data with the help of **[ft_connectivitysimulation](/reference/ft_connectivitysimulation)** and use these data to compute various connectivity metrics. As a generative model of the data we will use a multivariate autoregressive model. Subsequently, we will estimate the multivariate autoregressive model, the spectral transfer function, and the cross-spectral density matrix using the functions **[ft_mvaranalysis](/reference/ft_mvaranalysis)** and **[ft_freqanalysis](/reference/ft_freqanalysis)**. In the next step we will compute and inspect various measures of connectivity with **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)** and **[ft_connectivityplot](/reference/ft_connectivityplot)**.

- **Simulated data with common pick-up and different noise levels**: In this part we are going to simulate some data consisting of an instantaneous mixture of three 'sources', creating a situation of common pick up. We will explore the effect of this common pick up on the consequent estimates of connectivity, and we will investigate the effect of different mixings on these estimates.

- **Connectivity between MEG virtual channel and EMG**: In this part we are going to reconstruct MEG virtual channel data and estimate connectivity between this virtual channel and EMG. The data used for this part are the same as in the [corticomuscular coherence tutorial](/tutorial/coherence).

## Simulated data with directed connections

{% include /shared/tutorial/connectivity_simulation_simulations.md %}

## Simulated data with common pick-up and different noise levels

{% include /shared/tutorial/connectivity_simulation_commonpickup.md %}

## Connectivity between MEG virtual channel and EMG

The previous two examples were using simulated data, either with a clear directed connectivity structure, or with a trivial pick-up of a common source in two channels. We will now continue with connectivity analysis on real MEG data. The dataset is the same as the one used in the [Analysis of corticomuscular coherence tutorial](/tutorial/coherence).

In short, the dataset consists of combined MEG and EMG recordings while the subject lifted his right hand. The [coherence tutorial](/tutorial/coherence#introduction) contains a more elaborate description of the experiment and the dataset and a detailed analysis can be found in the corresponding paper ([Jan-Mathijs Schoffelen, Robert Oostenveld and Pascal Fries. Neuronal Coherence as a Mechanism of Effective Corticospinal Interaction, Science 2005, Vol. 308 no. 5718 pp. 111-113](http://www.sciencemag.org/content/308/5718/111.abstract)). Due to the long distance between the EMG and the MEG, there is no volume conduction and hence no common pick-up. Hence this dataset lends itself well for connectivity analysis. But rather than using one of the MEG channels (as in the original study) and computing connectivity between that one channel and EMG, we will extract the cortical activity using a beamformer virtual channel.

### Compute the spatial filter for the region of interest

We start with determining the motor cortex as the region of interest. At the [end of the coherence tutorial](/tutorial/coherence#appendix_1localisation_of_neuronal_sources_coherent_with_the_emg_using_beamformers) it is demonstrated how to make a 3-D reconstruction of the cortico-muscular coherence (CMC) using the DICS algorithm. That source reconstruction serves as starting point for this analysis.

You can download the (source.mat)(https://download.fieldtriptoolbox.org/tutorial/connectivity/source.mat) file with the result from the DICS reconstruction.

We will first determine the position on which the cortico-muscular coherence is the largest.

    load source

    [maxval, maxindx] = max(source.avg.coh);
    maxpos = source.pos(maxindx,:)

    maxpos =
        4 -3 12

The cortical position is expressed in individual subject [head-coordinates](/faq/coordsys) and in centimeter. Relative to the center of the head (in between the ears) the position is 4 cm towards the nose, -3 towards the left side (i.e., 3 cm towards the right!) and 12 cm towards the vertex.

The **[ft_sourceanalysis](/reference/ft_sourceanalysis)** methods are usually applied to the whole brain using a regular 3-D grid or using a triangulated cortical sheet. You can also just specify the location of a single or multiple points of interest with _cfg.sourcemodel.pos_ and the LCMV beamformer will simply be performed at the location of interest.

The LCMV beamformer spatial filter for the location of interest will pass the activity at that location with unit-gain, while optimally suppressing all other noise and other source contributions to the MEG data. The LCMV implementation in FieldTrip requires the data covariance matrix to be computed with **[ft_timelockanalysis](/reference/ft_timelockanalysis)**.

Rather than doing all the preprocessing again, you can download the preprocessed data and headmodel [data.mat](https://download.fieldtriptoolbox.org/tutorial/connectivity/data.mat) and [SubjectCMC.hdm](https://download.fieldtriptoolbox.org/tutorial/connectivity/SubjectCMC.hdm).

    load data

    %% compute the beamformer filter
    cfg                   = [];
    cfg.covariance        = 'yes';
    cfg.channel           = 'MEG';
    cfg.covariancewindow  = 'all';
    timelock              = ft_timelockanalysis(cfg, data);

    cfg                  = [];
    cfg.method           = 'lcmv';
    cfg.hdmfile          = 'SubjectCMC.hdm';
    cfg.sourcemodel.pos  = maxpos;
    cfg.sourcemodel.unit = 'cm';;
    cfg.keepfilter       = 'yes';
    source               = ft_sourceanalysis(cfg, timelock);

The source reconstruction contains the estimated power and the source-level time series of the averaged ERF, but here we are not interested in those. The _cfg.keepfilter_ option results in the spatial filter being kept in the output source structure. This filter can be used to reconstruct the single-trial time series as a virtual channel by multiplying it with the original MEG data.

{% include markup/yellow %}
In this case, the headmodel coordinates were defined in cm, this might be different for different headmodels. You can inspect the units of the headmodel with **[ft_read_headmodel](/reference/fileio/ft_read_headmodel)**

    hdm = ft_read_headmodel('SubjectCMC.hdm')

    hdm =
      orig: [1x1 struct]
     label: {1x183 cell}
         r: [183x1 double]
         o: [183x3 double]
      unit: 'cm'
      cond: 1

{% include markup/end %}

### Extract the virtual channel time series

    %% construct the 3-D virtual channel at the location of interest
    beamformer = source.avg.filter{1};

    chansel = ft_channelselection('MEG', data.label); % find the names
    chansel = match_str(data.label, chansel);         % find the indices

    sourcedata = [];
    sourcedata.label = {'x', 'y', 'z'};
    sourcedata.time = data.time;
    for i=1:length(data.trial)
      sourcedata.trial{i} = beamformer * data.trial{i}(chansel,:);
    end

{% include markup/yellow %}
The LCMV spatial filter is computed using data in the time domain. However, no time-domain spatial filters (during preprocessing e.g., low-pass or high-pass filters) have been applied before hand. Consequently, the filter will suppress all noise in the data in all frequency bands. The spatial filter derived from the broadband data allows us to compute a broadband source level time series.

If you would know that the subsequent analysis would be limited to a specific frequency range in the data (e.g., everything above 30 Hz), you could first apply a filter using **[ft_preprocessing](/reference/ft_preprocessing)** (e.g., _cfg.hpfilter=yes_ and _cfg.hpfreq=30_) prior to computing the covariance and the spatial filter.
{% include markup/end %}

The _sourcedata_ structure resembles the raw-data output of **[ft_preprocessing](/reference/ft_preprocessing)** and consequently can be used in any follow-up function. You can for example visualize the single-trial virtual channel time series using **[ft_databrowser](/reference/ft_databrowser)**:

    cfg = [];
    cfg.viewmode = 'vertical';  % you can also specify 'butterfly'
    ft_databrowser(cfg, sourcedata);

{% include image src="/assets/img/tutorial/connectivity/figure1.png" width="300" %}

Notice that the reconstruction contains three channels, for the x-, the y- and the z-component of the equivalent current dipole source at the location of interest.

### Project along the strongest dipole direction

The interpretation of connectivity is facilitated if we can compute it between two plain channels rather than between one channel and a triplet of channels. Therefore we will project the time series along the dipole direction that explains most variance. This projection is equivalent to determining the largest (temporal) eigenvector and can be computationally performed using the singular value decomposition (svd).

    %% construct a single virtual channel in the maximum power orientation
    timeseries = cat(2, sourcedata.trial{:});

    [u, s, v] = svd(timeseries, 'econ');

    whos u s v
     Name           Size              Bytes  Class     Attributes

       s              3x3                  72  double
       u              3x3                  72  double
       v         196800x3             4723200  double

Matrix u contains the spatial decomposition, matrix v the temporal and on the diagonal of matrix s you can find the eigenvalues. See *help svd* for more details.

We now recompute the virtual channel time series, but now only for the dipole direction that has the most power.

    % this is equal to the first column of matrix V, apart from the scaling with s(1,1)
    timeseriesmaxproj = u(:,1)' * timeseries;

    virtualchanneldata = [];
    virtualchanneldata.label = {'cortex'};
    virtualchanneldata.time = data.time;
    for i=1:length(data.trial)
      virtualchanneldata.trial{i} = u(:,1)' * beamformer * data.trial{i}(chansel,:);
    end

#### Exercise 8

{% include markup/skyblue %}
Rather than using a sourcemodel in the beamformer that consists of all three (x, y, z) directions, you can also have the beamformer compute the filter for only the optimal source orientation. This is implemented using the _cfg.lcmv.fixedori='yes'_ option.

Recompute the spatial filter for the optimal source orientation and using that spatial filter (a 1x151 vector) recompute the time series.

Investigate and describe the difference between the two time series. What is the difference between the two dipole orientations?

Note that one orientation is represented in the SVD matrix "u" and the other is in the source.avg.ori field.
{% include markup/end %}

### Combine the virtual channel with the EMG

The raw data structure containing one (virtual) channel can be combined with the two EMG channels from the original preprocessed data.

    %% select the two EMG channels
    cfg = [];
    cfg.channel = 'EMG';
    emgdata = ft_selectdata(cfg, data);

    %% combine the virtual channel with the two EMG channels
    cfg = [];
    combineddata = ft_appenddata(cfg, virtualchanneldata, emgdata);

    save combineddata combineddata

### Compute the connectivity

The resulting combined data structure has three channels: the activity from the cortex, the left EMG and the right EMG. We can now continue with regular channel-level connectivity analysis.

    %% compute the spectral decomposition
    cfg            = [];
    cfg.output     = 'fourier';
    cfg.method     = 'mtmfft';
    cfg.foilim     = [5 100];
    cfg.tapsmofrq  = 5;
    cfg.keeptrials = 'yes';
    cfg.channel    = {'cortex' 'EMGlft' 'EMGrgt'};
    freq    = ft_freqanalysis(cfg, combineddata);

    cfg = [];
    cfg.method = 'coh';
    coherence = ft_connectivityanalysis(cfg, freq);

This computes the spectral decomposition and the coherence spectrum between all channel pairs, which can be plotted with

    cfg = [];
    cfg.zlim = [0 0.2];
    figure
    ft_connectivityplot(cfg, coherence);
    title('coherence')

{% include image src="/assets/img/tutorial/connectivity/figure2.png" width="400" %}

To look in more detail into the numerical representation of the coherence results, you can use

    figure
    plot(coherence.freq, squeeze(coherence.cohspctrm(1,2,:)))
    title(sprintf('connectivity between %s and %s', coherence.label{1}, coherence.label{2}));
    xlabel('freq (Hz)')
    ylabel('coherence')

{% include image src="/assets/img/tutorial/connectivity/figure3.png" width="300" %}

The spectrum reveals coherence peaks at 10 and 20 Hz (remember that the initial DICS localizer was done at beta). Furthermore, there is a broader plateau of coherence in the gamma range from 40-50 Hz.

#### Exercise 9

{% include markup/skyblue %}
The spectral decomposition was performed with mutitapering and 5 Hz spectral smoothing (i.e. 5Hz in both directions). Recompute the spectral decomposition and the coherence with a hanning taper. Recompute it with mutitapering and 10 Hz smoothing. Plot the three coherence spectra and look at the differences.
{% include markup/end %}

#### Exercise 10

{% include markup/skyblue %}
Rather than looking at undirected coherence, the virtual channel level data can now also easily be submitted to directed connectivity measures. Compute the spectrally resolved granger connectivity and try to assess whether the directionality is from cortex to EMG or vice versa.
{% include markup/end %}

#### Exercise 11

{% include markup/skyblue %}
Let's say you wanted to look at cortico-cortical connectivity, e.g., interactions between visual and motor cortex in a particular frequency band. How would you approach this?
{% include markup/end %}

## Summary and further reading

This tutorial demonstrates how to compute connectivity measures between two time series. If you want to learn how to make a distributed representation of connectivity throughout the whole brain, you may want to continue with the [corticomuscular coherence tutorial](/tutorial/coherence).

### See also these frequently asked questions

{% include seealso category="faq" tag1="coherence" %}

### See also these examples

{% include seealso category="example" tag1="connectivity" %}
{% include seealso category="example" tag1="coherence" %}
