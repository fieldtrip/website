---
title: MEG whole-brain connectivity
tags: [chieti, hcp-motort]
---

# MEG whole-brain connectivity

## Introduction

{% include markup/info %}
This tutorial contains hands-on material that we used for the [MEG connectivity workshop in Chieti](/workshop/chieti2015).
{% include markup/end %}

In this tutorial we will analyze a single-subject MEG dataset from the [Human Connectome Project](http://www.humanconnectome.org).

{% include /shared/tutorial/hcp_motort.md %}

This tutorial follows on the [MEG virtual channels and seed-based connectivity](/workshop/chieti2015/virtualchannel) tutorial and continues with the data that has already partially been computed there.

## Procedure

We start by setting up the path to the FieldTrip toolbox, to the HCP megconnectome toolbox and to the HCP data.

    restoredefaultpath;
    clear;
    clc;

    addpath('/Volumes/SEAGATE 2TB/workshop/fieldtrip-20150909');
    ft_defaults;
    addpath(genpath('/Volumes/SEAGATE 2TB/workshop/fieldtrip-20150909/template'));
    addpath(genpath('/Volumes/SEAGATE 2TB/workshop/megconnectome-2.2'));
    addpath(genpath('/Volumes/SEAGATE 2TB/workshop/177746'));

Most data has already been prepared in the previous tutorial, here we just load the relevant .mat files.

    load data_rh
    load headmodel
    load leadfield
    load freq
    load lh_seed_pos
    load rh_seed_pos
    load ml_seed_pos
    load individual_mri

### Whole brain connectivity, starting at a seed location

Previously we computed the time-frequency representation over the full time and frequency range, and we computed with "mtmfft" the multi-tapered spectral representation at a single time-frequency point. We can also use wavelets to obtain the spectral estimate at a single time-frequency point.

    cfg = [];
    cfg.channel = 'meg';
    cfg.method = 'wavelet';
    cfg.output = 'fourier';
    cfg.keeptrials = 'yes';
    cfg.foi = 20;
    cfg.toi = 0.100; % just following movement onset
    freq = ft_freqanalysis(cfg, data_rh);

The have pre-computed the lead field for a full 3-D grid with source locations. We can project the spectral estimate from the channel-level into the source-level using the "pcc" method. This is a modification of the [original DICS method](http://www.ncbi.nlm.nih.gov/pubmed/?term=dics+gross+2001) that allows post-hoc computation of various connectivity measures.

    cfg = [];
    cfg.headmodel = headmodel;
    cfg.grid = leadfield;
    cfg.method = 'pcc';
    cfg.pcc.fixedori = 'yes';

    source = ft_sourceanalysis(cfg, freq);

The source level data now contains the complex-values spectral estimate at each grid location.

    figure
    plot(squeeze(freq.fourierspctrm(:,1,1,1)), '.')
    xlabel('real');
    ylabel('imag');

    figure
    plot(source.avg.mom{find(source.inside, 1, 'first')}, '.')
    xlabel('real');
    ylabel('imag');

Using these spectral estimates, we can compute connectivity measures such as (imaginary) coherence.

In the previous tutorial we have determined some regions of interest. These are not exactly in the source grid, but we can find the grid location that is the closest to the seed points.

    pos = lh_seed_pos;
    % pos = rh_seed_pos;
    % pos = ml_seed_pos;

    % compute the nearest grid location
    dif = leadfield.pos;
    dif(:, 1) = dif(:, 1)-pos(1);
    dif(:, 2) = dif(:, 2)-pos(2);
    dif(:, 3) = dif(:, 3)-pos(3);
    dif = sqrt(sum(dif.^2, 2));
    [distance, refindx] = min(dif);

Given the seed location, we can now compute the imaginary coherence with all other locations in the brain.

    cfg = [];
    cfg.method = 'coh';
    cfg.complex = 'absimag';
    cfg.refindx = refindx;
    source_coh = ft_connectivityanalysis(cfg, source);

    % the output contains both the actual source position, as well as the position of the reference
    % this is ugly and will probably change in future FieldTrip versions
    orgpos = source_coh.pos(:, 1:3);
    refpos = source_coh.pos(:, 4:6);
    source_coh.pos = orgpos;

Subsequently we can visualize the distribution of the seed-based connectivity.

    cfg = [];
    cfg.funparameter = 'cohspctrm';
    ft_sourceplot(cfg, source_coh);

It will look nicer if we interpolate the connectivity map on the subject's individual MRI.

    cfg = [];
    cfg.parameter = 'cohspctrm';
    source_coh_int = ft_sourceinterpolate(cfg, source_coh, individual_mri);

    cfg = [];
    cfg.funparameter = 'cohspctrm';
    ft_sourceplot(cfg, source_coh_int);

{% include markup/info %}
Compute a full brain connectivity distribution with another connectivity metric.
{% include markup/end %}

{% include markup/info %}
Compute the connectivity distribution in the left-hand movement data using the right hemisphere seed location.

Subsequently, you can make a contrast between left-hand and right-hand connectivity results.
{% include markup/end %}

### All-to-all connectivity

In principle it is also possible to compute all-to-all source connectivity. However, that requires more memory than is available in the workshop computers. The source model consists of 24024 locations, which means that the connectivity will consist of a 24024x24024 matrix. Each element is 8 bytes, which means that the whole matrix requires about ~4.5 GB of RAM.
