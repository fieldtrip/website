---
title: Extended analysis of sensor- and source-level connectivity
tags: [tutorial, freq, connectivity, coherence, granger, dtf, pdc, meg-visuomotor151]
---

# Extended analysis of sensor- and source-level connectivity

## Introduction

{% include /shared/tutorial/connectivity_simulation_intro.md %}

## Background

{% include /shared/tutorial/connectivity_simulation_background.md %}

## Procedure

This tutorial consists of three part

- Simulated data with directed connections. In this part we are going to simulate some data and use these data to compute various connectivity metrics. As a generative model of the data we will use a multivariate autoregressive model and we will use **[ft_connectivitysimulation](/reference/ft_connectivitysimulation)** for this. Subsequently, we will estimate the multivariate autoregressive model and the spectral transfer function, and the cross-spectral density matrix using the functions **[ft_mvaranalysis](/reference/ft_mvaranalysis)** and **[ft_freqanalysis](/reference/ft_freqanalysis)**. In the next step we will compute and inspect various measures of connectivity with **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)** and **[ft_connectivityplot](/reference/ft_connectivityplot)**.
- Simulated data with common pick-up and different noise levels. In this part we are going to simulate some data consisting of an instantaneous mixture of 3 'sources', creating a situation of common pick up. We will explore the effect of this common pick up on the consequent estimates of connectivity, and we will investigate the effect of different mixings on these estimates.
- Connectivity between MEG virtual channels and EMG. In this part we are going to reconstruct MEG virtual channel data and estimate connectivity between these virtual channels and EMG. The data used for this part are the same as in the [extended beamforming](/tutorial/beamformingextended) tutorial.

## Simulated data with directed connections

{% include /shared/tutorial/connectivity_simulation_simulations.md %}

## Source-level cortico-cortical connectivity in MEG data

{% include /shared/tutorial/virtual_sensors.md %}

### Project along the strongest dipole direction

The virtual channel data just computed has three channels per location. These correspond to the three orientations of the dipole in a single voxel. The interpretation of connectivity is facilitated if we can compute it between plain channels rather than between triplets of channels. Therefore we will project the time series along the dipole direction that explains most variance. This projection is equivalent to determining the largest (temporal) eigenvector and can be computationally performed using the singular value decomposition (svd).

    visualTimeseries = cat(2, gam_pow_data.trial{:});
    motorTimeseries = cat(2, coh_lft_data.trial{:});
    [u1, s1, v1] = svd(visualTimeseries, 'econ');
    [u2, s2, v2] = svd(motorTimeseries, 'econ');

Matrices u1 and u2 contain the spatial decomposition, matrices v1 and v2 the temporal and on the diagonal of matrices s1 and s2 you can find the eigenvalues. See "help svd" for more details.

We now recompute the virtual channel time series, but now only for the dipole direction that has the most power.

    virtualchanneldata = [];
    virtualchanneldata.label = {'visual', 'motor'};
    virtualchanneldata.time = data_cmb.time;

    for k = 1:length(data_cmb.trial)
      virtualchanneldata.trial{k}(1,:) = u1(:,1)' * beamformer_gam_pow * data_cmb.trial{k}(chansel,:);
      virtualchanneldata.trial{k}(2,:) = u2(:,1)' * beamformer_lft_coh * data_cmb.trial{k}(chansel,:);
    end

### Combine the virtual channel with the EMG

The raw data structure containing one (virtual) channel can be combined with the two EMG channels from the original preprocessed data.

    % select the two EMG channels
    cfg = [];
    cfg.channel = 'EMG';
    emgdata = ft_selectdata(cfg, data_cmb);

    % combine the virtual channel with the two EMG channels
    cfg = [];
    combineddata = ft_appenddata(cfg, virtualchanneldata, emgdata);

### Compute the connectivity

The resulting combined data structure now has four channels: the activity from the visual cortex, the activity from the right motor cortex, the left EMG and the right EMG. We can now treat this data structure as any other, and perform connectivity analysis 'as if' we were working on a channel-level data set!

    %% compute the spectral decomposition
    cfg            = [];
    cfg.output     = 'fourier';
    cfg.method     = 'mtmfft';
    cfg.foilim     = [5 100];
    cfg.tapsmofrq  = 5;
    cfg.keeptrials = 'yes';
    cfg.channel    = {'visual' 'motor' 'EMGlft' 'EMGrgt'};
    freq = ft_freqanalysis(cfg, combineddata);

    cfg = [];
    cfg.method = 'coh';
    coherence = ft_connectivityanalysis(cfg, freq);

This computes the spectral decomposition and the coherence spectrum between all channel pairs, which can be plotted with

    cfg = [];
    cfg.zlim = [0 0.25];
    figure
    ft_connectivityplot(cfg, coherence);

{% include image src="/assets/img/tutorial/connectivityextended/figure1.png" width="500" %}

The spectrum reveals a strong coherence peak around 20 Hz between the right motor cortex and the left EMG, as expected, and as we found in the beamforming tutorial as well, where we beamed the sensor-level coherence directly. Additionally, we also see a corticomuscular coherence peak in the gamma frequency range.

{% include markup/skyblue %}
Rather than looking at undirected coherence, the virtual channel level data can now also easily be submitted to directed connectivity measures. Compute the spectrally resolved granger connectivity and try to assess whether the directionality is from cortex to EMG or vice versa.
{% include markup/end %}

{% include markup/skyblue %}
Now that you have the virtual channel data, you can also use it to look at, for instance, power correlations across trials between visual gamma and motor beta. Do this! (Hint: this involves computing trial-specific estimates of power using ft_freqanalysis, extracting those estimates from the resulting freq structure, and using matlab's own corr function.)
{% include markup/end %}
