---
title: Cluster-based permutation tests on time-frequency data
tags: [tutorial, statistics, eeg, meg, raw, freq, meg-language, neighbours]
---

# Cluster-based permutation tests on time-frequency data

## Introduction

The objective of this tutorial is to give an introduction to the statistical analysis of EEG and MEG data (denoted as M/EEG data in the following) by means of cluster-based permutation tests.

The tutorial starts with a long background section that sketches the background of permutation tests. The next sections are more tutorial-like. They deal with the analysis of an actual MEG [dataset](/tutorial/meg_language). In a step-by-step fashion, it will be shown how to statistically compare the data observed in two experimental conditions in a between-trials, in a within-trials and in a within-subjects design. For this, we will use planar TFR's.

In this tutorial we will continue working on the [dataset](/tutorial/meg_language) described in the preprocessing tutorials. Below we will repeat code to select the trials and preprocess the data as described in the earlier tutorials. We assume that the preprocessing (see the [Preprocessing - Segmenting and reading trial-based EEG and MEG data](/tutorial/preprocessing) tutorial), calculation of the planar gradient (see the [Event-related averaging and MEG planar gradient](/tutorial/eventrelatedaveraging) tutorial) and the time-frequency analysis (see the [Time-frequency analysis using Hanning window, multitapers and wavelets](/tutorial/timefrequencyanalysis) tutorial) are already clear for the reader.

This tutorial is not covering statistical test on event-related fields. If you are interested in that, you can read the [Cluster-based permutation tests on event-related fields](/tutorial/cluster_permutation_timelock) tutorial. If you are interested how parametric statistical tests can be used, you can read the [Parametric and non-parametric statistics on event-related fields](/tutorial/eventrelatedstatistics) tutorial.

{% include markup/skyblue %}
This tutorial contains hands-on material that we use for the [MEG/EEG toolkit course](/workshop/toolkit2015) and it is complemented by this lecture.

{% include youtube id="x0hR-VsHZj8" %}
{% include markup/end %}

## Background

{% include /shared/tutorial/cluster_permutation_background.md %}

## Procedure

In this tutorial we will consider a **between-trials** experiment, in which we analyze the data of a single subject. For the statistical analysis for this experiment we calculate the planar TFRs. The steps we perform are as follow

- Preprocessing with the **[ft_definetrial](/reference/ft_definetrial)** and with the **[ft_preprocessing](/reference/ft_preprocessing)** functions
- Calculation of the planar gradient and time-frequency analysis with the **[ft_megplanar](/reference/ft_megplanar)**, with the **[ft_freqanalysis](/reference/ft_freqanalysis)** and **[ft_combineplanar](/reference/ft_combineplanar)** functions
- Permutation test with the **[ft_freqstatistics](/reference/ft_freqstatistics)** function
- Plotting the result using the **[ft_freqdescriptives](/reference/ft_freqdescriptives)** and the **[ft_clusterplot](/reference/ft_clusterplot)** functions

{% include image src="/assets/img/tutorial/cluster_permutation_freq/figure1.png" %}

_Figure 1. Pipeline of statistical analysis of planar TFR's in a between trials design_

Subsequently we will consider a **within-trials** experiment, in which we compare the pre-stimulus baseline to the post-stimulus activity time window. The steps we perform are as follows

- Preprocessing with **[ft_definetrial](/reference/ft_definetrial)** and with **[ft_preprocessing](/reference/ft_preprocessing)** and selecting the appropriate time windows with the **[ft_redefinetrial](/reference/ft_redefinetrial)** function
- Calculation of the planar gradient and time-frequency analysis with the **[ft_megplanar](/reference/ft_megplanar)**, with the **[ft_freqanalysis](/reference/ft_freqanalysis)** and **[ft_combineplanar](/reference/ft_combineplanar)** functions
- Permutation test with the **[ft_freqstatistics](/reference/ft_freqstatistics)** function
- Plotting the result using **[ft_clusterplot](/reference/ft_clusterplot)**

{% include image src="/assets/img/tutorial/cluster_permutation_freq/figure2.png" %}

_Figure 2. Pipeline of statistical analysis of planar TFR's in a within-trials design_

Finally we will consider a **within-subjects** experiment with the following step

- Preprocessing with **[ft_definetrial](/reference/ft_definetrial)** and with **[ft_preprocessing](/reference/ft_preprocessing)**
- Calculation of the planar gradient and time-frequency analysis with the **[ft_megplanar](/reference/ft_megplanar)**, with the **[ft_freqanalysis](/reference/ft_freqanalysis)** and **[ft_combineplanar](/reference/ft_combineplanar)** functions
- Calculation of the grandaverage with the **[ft_freqgrandaverage](/reference/ft_freqgrandaverage)** function
- Permutation test with **[ft_freqstatistics](/reference/ft_freqstatistics)**
- Plotting the result using **[ft_clusterplot](/reference/ft_clusterplot)**

{% include image src="/assets/img/tutorial/cluster_permutation_freq/figure3.png" %}

_Figure 3. Pipeline of statistical analysis of planar TFR's in a within-subjects design_

## Between-trial experiments

In a between-trials experiment, we analyze the data of a single subject. By means of a statistical test, we want to answer the question whether there is a systematic difference in the MEG recorded on trials with a fully congruent and trials with a fully incongruent sentence ending.

### Preprocessing

### Reading in the data

We will now read and preprocess the data. If you would like to continue directly with the already preprocessed data, you can download [dataFIC.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/dataFIC.mat) and [dataFC.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/dataFC.mat). Load the data into MATLAB with the command `load` and skip to [Calculation of the planar gradient and time-frequency analysis](#calculation-of-the-planar-gradient-and-time-frequency-analysis).

Otherwise run the following code:

{% include /shared/tutorial/definetrial_all.md %}

### Cleaning

{% include /shared/tutorial/preprocessing_nofilter.md %}

For subsequent analysis we extract the trials of the fully incongruent condition and the fully congruent condition to separate data structures.

    cfg = [];
    cfg.trials = data_all.trialinfo == 3;
    dataFIC = ft_redefinetrial(cfg, data_all);

    cfg = [];
    cfg.trials = data_all.trialinfo == 9;
    dataFC = ft_redefinetrial(cfg, data_all);

Subsequently you can save the data to disk.

    save dataFIC dataFIC
    save dataFC dataFC

### Calculation of the planar gradient and time-frequency analysis

Before calculating the TFRs we calculate the planar gradient with **[ft_megplanar](/reference/ft_megplanar)**. This requires preprocessed data (see above or download [dataFIC.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/dataFIC.mat) and [dataFC.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/dataFC.mat)).

    load dataFIC
    load dataFC

    cfg = [];
    cfg.planarmethod = 'sincos';
    % prepare_neighbours determines with what sensors the planar gradient is computed
    cfg_neighb.method = 'distance';
    cfg.neighbours    = ft_prepare_neighbours(cfg_neighb, dataFC);

    dataFIC_planar = ft_megplanar(cfg, dataFIC);
    dataFC_planar  = ft_megplanar(cfg, dataFC);

Without a prior hypothesis (i.e., an hypothesis that is independent of the present data), we must test the difference between the FIC and the FC condition for all frequency bands that may be of interest. However, such an analysis is not suited as a first step in a tutorial. Therefore, we assume that we have a prior hypothesis about the frequency band in which the FIC and FC condition may differ. This frequency band is centered at 20 Hz. We will now investigate if there is a difference between the FIC and the FC condition at this frequency. To calculate the TFRs, we use **[ft_freqanalysis](/reference/ft_freqanalysis)** with the configuration below. See the [tutorial Time-frequency analysis using Hanning window, multitapers and wavelets](/tutorial/timefrequencyanalysis) for an explanation of the settings. Note that cfg.keeptrials = 'yes', which is necessary for the subsequent statistical analysis.

    cfg = [];
    cfg.output     = 'pow';
    cfg.channel    = 'MEG';
    cfg.method     = 'mtmconvol';
    cfg.taper      = 'hanning';
    cfg.foi        = 20;
    cfg.toi        = [-1:0.05:2.0];
    cfg.t_ftimwin  = 7./cfg.foi; %7 cycles
    cfg.keeptrials = 'yes';

Calculate the TFRs for the two experimental conditions (FIC and FC).

    freqFIC_planar = ft_freqanalysis(cfg, dataFIC_planar);
    freqFC_planar  = ft_freqanalysis(cfg, dataFC_planar);

Finally, we calculate the combined planar gradient and copy the gradiometer structure in the new datasets.

    cfg = [];
    freqFIC_planar_cmb = ft_combineplanar(cfg, freqFIC_planar);
    freqFC_planar_cmb = ft_combineplanar(cfg, freqFC_planar);

    freqFIC_planar_cmb.grad = dataFIC.grad
    freqFC_planar_cmb.grad = dataFC.grad

To save:

    save freqFIC_planar_cmb freqFIC_planar_cmb
    save freqFC_planar_cmb  freqFC_planar_cmb

### Permutation test

Now, run **[ft_freqstatistics](/reference/ft_freqstatistics)** to compare freqFIC_planar_cmb and freqFC_planar_cmb. Except for the field cfg.latency, the following configuration is identical to the configuration that was used for comparing event-related averages in the [Cluster-based permutation tests on event-related fields tutorial](/tutorial/cluster_permutation_timelock). Also see [this tutorial](/tutorial/cluster_permutation_timelock) for a detailed explanation of all the configuration settings. You can read more about the **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)** function in the [FAQs](/faq/how_does_ft_prepare_neighbours_work).

To load the planar gradient TFRs (also available from [freqFIC_planar_cmb.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/freqFIC_planar_cmb.mat) and [freqFC_planar_cmb.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/freqFC_planar_cmb.mat) on our download server), us

    load freqFIC_planar_cmb
    load freqFC_planar_cmb

    cfg = [];
    cfg.channel          = {'MEG', '-MLP31', '-MLO12'};
    cfg.latency          = 'all';
    cfg.frequency        = 20;
    cfg.method           = 'montecarlo';
    cfg.statistic        = 'ft_statfun_indepsamplesT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = 0;
    cfg.alpha            = 0.025;
    cfg.numrandomization = 500;
    % prepare_neighbours determines what sensors may form clusters
    cfg_neighb.method    = 'distance';
    cfg.neighbours       = ft_prepare_neighbours(cfg_neighb, dataFC);

    design = zeros(1,size(freqFIC_planar_cmb.powspctrm,1) + size(freqFC_planar_cmb.powspctrm,1));
    design(1,1:size(freqFIC_planar_cmb.powspctrm,1)) = 1;
    design(1,(size(freqFIC_planar_cmb.powspctrm,1)+1):(size(freqFIC_planar_cmb.powspctrm,1)+...
    size(freqFC_planar_cmb.powspctrm,1))) = 2;

    cfg.design           = design;
    cfg.ivar             = 1;

    [stat] = ft_freqstatistics(cfg, freqFIC_planar_cmb, freqFC_planar_cmb);

Save the output:

    save stat_freq_planar_FICvsFC stat

### Plotting the results

The output can also be obtained from [stat_freq_planar_FICvsFC.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/stat_freq_planar_FICvsFC.mat). If you need to reload the statistics output, us

    load stat_freq_planar_FICvsFC

By inspecting stat.posclusters and stat.negclusters, you will see that there is one large cluster that shows a negative effect and no large clusters showing a positive effect.

To show the topography of the negative cluster, we make use of **[ft_clusterplot](/reference/ft_clusterplot)**. This is a function that displays the channels that contribute to large clusters, based on which the null-hypothesis can be rejected. First we use **[ft_freqdescriptives](/reference/ft_freqdescriptives)** to average over the trials.

    cfg = [];
    freqFIC_planar_cmb = ft_freqdescriptives(cfg, freqFIC_planar_cmb);
    freqFC_planar_cmb  = ft_freqdescriptives(cfg, freqFC_planar_cmb);

Subsequently we add the raw effect (FIC-FC) to the obtained stat structure and plot the largest cluster overlayed on the raw effect.

    stat.raweffect = freqFIC_planar_cmb.powspctrm - freqFC_planar_cmb.powspctrm;

    cfg = [];
    cfg.alpha  = 0.025;
    cfg.parameter = 'raweffect';
    cfg.zlim   = [-1e-27 1e-27];
    cfg.layout = 'CTF151_helmet.mat';
    ft_clusterplot(cfg, stat);

{% include image src="/assets/img/tutorial/cluster_permutation_freq/figure4.png" %}

_Figure 1: Raw effect (FIC-FC) and channel-time cluster of planar gradient TFRs of subject 1._

## Within trial experiments

We will now show how to statistically test the difference between the TFRs in the post-stimulus (activation) and the pre-stimulus (baseline) period of the fully incongruent sentence endings. To perform this comparison by means of a permutation test, we have to select equal-length non-overlapping time intervals in the activation and the baseline period. For the activation period we choose [0.6 1.6], which is the time interval from 0.6 to 1.6 seconds after stimulus onset. and for the baseline period we choose [-1 0], which is the time interval from 1 to 0 seconds before stimulus onset.

It must be stressed that the time windows we choose to compare are **nonoverlapping** and of **equal length**. This constraint follows from the null hypothesis that is tested with a permutation test. This null hypothesis involves that the data (spatiotemporal matrices) observed in the two experimental conditions are drawn from the same probability distribution. This null hypothesis only makes sense if the dimensions of the data matrices in the two experimental conditions are equal. In other words, the number of channels and the number of time points of these spatiotemporal data matrices must be equal. This also applies to a within trials experiment in which an activation and a baseline condition are compared: the number of channels and time points of the two data matrices must be equal.

### Preprocessing and freqanalysis on planar data

We first select equal-length non-overlapping time intervals in the activation and the baseline period. For the activation period we choose [0.6 1.6], the time interval from 0.6 to 1.6 seconds after stimulus onset. We will again focus on the power in the beta band (around 20 Hz). And for the baseline period we choose [-1 0], the time interval from 1 to 0 seconds before stimulus onset.

We now calculate the TFRs for the activation and the baseline period. We use again the preprocessed dataFIC (see above or download [dataFIC.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/dataFIC.mat)).

    load dataFIC

To calculate the TFRs with the planar gradient, we first cut out the time intervals of interest with the function **[ft_redefinetrial](/reference/ft_redefinetrial)**.

    cfg = [];
    cfg.toilim = [0.6 1.6];
    dataFIC_activation = ft_redefinetrial(cfg, dataFIC);

    cfg = [];
    cfg.toilim = [-1.0 0];
    dataFIC_baseline = ft_redefinetrial(cfg, dataFIC);

**[ft_freqstatistics](/reference/ft_freqstatistics)** will always compare data at the same time point, and therefore you get an error if you try to statistically test differences between data structures with non-overlapping time axes. This implies that, in order to statistically test the differences between activation and baseline period data, we have to trick the function by making the time axis the same. We do this by copying the time axis of dataFIC_activation onto dataFIC_baseline.

    dataFIC_baseline.time = dataFIC_activation.time;

To calculate the TFRs for the synthetic planar gradient data, we must run the following code:

    cfg = [];
    cfg.planarmethod = 'sincos';
    % prepare_neighbours determines with what sensors the planar gradient is computed
    cfg_neighb.method    = 'distance';
    cfg.neighbours       = ft_prepare_neighbours(cfg_neighb, dataFIC_activation);
    dataFIC_activation_planar = ft_megplanar(cfg, dataFIC_activation);
    dataFIC_baseline_planar   = ft_megplanar(cfg, dataFIC_baseline);

    cfg = [];
    cfg.output = 'pow';
    cfg.channel = 'MEG';
    cfg.method = 'mtmconvol';
    cfg.taper = 'hanning';
    cfg.foi = 20;
    cfg.toi = [0.6:0.05:1.6];
    cfg.t_ftimwin = 7./cfg.foi; %7 cycles
    cfg.keeptrials = 'yes';

    freqFIC_activation_planar = ft_freqanalysis(cfg, dataFIC_activation_planar);
    freqFIC_baseline_planar   = ft_freqanalysis(cfg, dataFIC_baseline_planar);

Finally, we combine the two planar gradients at each sensor and add the gradiometer definition

    cfg = [];
    freqFIC_baseline_planar_cmb   = ft_combineplanar(cfg,freqFIC_baseline_planar);
    freqFIC_activation_planar_cmb = ft_combineplanar(cfg,freqFIC_activation_planar);

    freqFIC_baseline_planar_cmb.grad   = dataFIC.grad;
    freqFIC_activation_planar_cmb.grad = dataFIC.grad;

To save:

    save freqFIC_baseline_planar_cmb freqFIC_baseline_planar_cmb;
    save freqFIC_activation_planar_cmb freqFIC_activation_planar_cmb;

### Permutation test

You can download the planar gradient TFRs from [freqFIC_activation_planar_cmb.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/freqFIC_activation_planar_cmb.mat)) and [freqFIC_baseline_planar_cmb.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/freqFIC_baseline_planar_cmb.mat). To load them, use:

    load freqFIC_activation_planar_cmb
    load freqFIC_baseline_planar_cmb

To compare `freqFIC_activation_planar_cmb` and `freqFIC_baseline_planar_cmb` by means of **[ft_freqstatistics](/reference/ft_freqstatistics)**, we use the following configuration:

    cfg = [];
    cfg.channel          = {'MEG', '-MLP31', '-MLO12'};
    cfg.latency          = [0.8 1.4];
    cfg.method           = 'montecarlo';
    cfg.frequency        = 20;
    cfg.statistic        = 'ft_statfun_actvsblT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = 0;
    cfg.alpha            = 0.025;
    cfg.numrandomization = 500;
    % prepare_neighbours determines what sensors may form clusters
    cfg_neighb.method    = 'distance';
    cfg.neighbours       = ft_prepare_neighbours(cfg_neighb, freqFIC_activation_planar_cmb);

    ntrials = size(freqFIC_activation_planar_cmb.powspctrm,1);
    design  = zeros(2,2*ntrials);
    design(1,1:ntrials) = 1;
    design(1,ntrials+1:2*ntrials) = 2;
    design(2,1:ntrials) = [1:ntrials];
    design(2,ntrials+1:2*ntrials) = [1:ntrials];

    cfg.design   = design;
    cfg.ivar     = 1;
    cfg.uvar     = 2;

This configuration for a within-trials experiment is very similar to the configuration for the [within-subjects experiment in the "Cluster-based permutation tests on event-related fields" tutorial](/tutorial/cluster_permutation_timelock#within-subjects_experiments) in which we compared the evoked responses to fully incongruent and fully congruent sentence endings. The main difference is the measure that we use to evaluate the effect at the sample level (cfg.statistic = 'ft_statfun_actvsblT' instead of cfg.statistic = 'ft_statfun_depsamplesT'). With cfg.statistic = 'ft_statfun_actvsblT', we choose the so-called _activation-versus-baseline T-statistic_. This statistic compares the power in every sample (i.e., a (channel,frequency,time)-triplet) in the activation period with the corresponding time-averaged power (i.e., the average over the temporal dimension) in the baseline period. The comparison of the activation and the time-averaged baseline power is performed by means of a dependent samples T-statistic.

You can read more about the **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)** function in the [FAQs](/faq/how_does_ft_prepare_neighbours_work).

We can now run **[ft_freqstatistics](/reference/ft_freqstatistics)**

    [stat] = ft_freqstatistics(cfg, freqFIC_activation_planar_cmb, freqFIC_baseline_planar_cmb);

Save the output:

    save stat_freqFIC_ACTvsBL stat

The output can also be obtained from [stat_freqFIC_ACTvsBL.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/stat_freqFIC_ACTvsBL.mat). If you need to reload the statistics output, use:

    load stat_freqFIC_ACTvsBL

By inspecting stat.posclusters and stat.negclusters, you will see that there is one substantially large cluster showing a positive effect and no large clusters showing a negative effect.

### Plotting the results

This time we will plot the largest cluster on top of the statistics, which are present in the .stat field.

    cfg = [];
    cfg.alpha     = 0.025;
    cfg.parameter = 'stat';
    cfg.zlim      = [-4 4];
    cfg.layout    = 'CTF151_helmet.mat';
    ft_clusterplot(cfg, stat);

{% include image src="/assets/img/tutorial/cluster_permutation_freq/figure5.png" %}

_Figure 2: Largest cluster that shows a difference between activation and baseline, plotted on top of the T-statistic of the difference.._

## Within subjects experiments

In this paragraph we describe permutation testing for TFRs obtained in experiments involving multiple subjects that are each observed in multiple experimental conditions. Every subject is observed in a large number of trials, each one belonging to one experimental condition. For every subject, averages are computed over all trials belonging to each of the experimental conditions. Thus, for every subject, the data are summarized in an array of condition-specific averages. The permutation test that will be described in the following informs us about the following null hypothesis: the probability distribution of the condition-specific averages is identical for all experimental conditions.

### Preprocessing, planar gradient and grand average

To test the difference between the average TFRs for fully incongruent (FIC) and fully congruent (FC) sentence endings we use planar gradient data. To load the data structures containing time frequency grand averages of all ten subjects (available [here](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/GA_TFR_orig.mat)), use:

    load GA_TFR_orig;

The averages of the TFRs for the fully incongruent and the fully congruent sentence endings are stored in GA_TFRFIC and GA_TFRFC. These averages were calculated using **[ft_freqgrandaverage](/reference/ft_freqgrandaverage)** .

### Permutation test

We now perform the permutation test using **[ft_freqstatistics](/reference/ft_freqstatistics)**. The configuration setting for this analysis are almost identical to the settings for the [within-subjects experiment in the "Cluster-based permutation tests on event-related fields" tutorial](/tutorial/cluster_permutation_timelock#within-subjects_experiments). The only difference is a small change in the latency window (cfg.latency). You can read more about the **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)** function in the [FAQs](/faq/how_does_ft_prepare_neighbours_work).

    cfg = [];
    cfg.channel          = {'MEG'};
    cfg.latency          = [0 1.8];
    cfg.frequency        = 20;
    cfg.method           = 'montecarlo';
    cfg.statistic        = 'ft_statfun_depsamplesT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = 0;
    cfg.alpha            = 0.025;
    cfg.numrandomization = 500;
    % specifies with which sensors other sensors can form clusters
    cfg_neighb.method    = 'distance';
    cfg.neighbours       = ft_prepare_neighbours(cfg_neighb, GA_TFRFC);

    subj = 10;
    design = zeros(2,2*subj);
    for i = 1:subj
      design(1,i) = i;
    end
    for i = 1:subj
      design(1,subj+i) = i;
    end
    design(2,1:subj)        = 1;
    design(2,subj+1:2*subj) = 2;

    cfg.design   = design;
    cfg.uvar     = 1;
    cfg.ivar     = 2;

    [stat] = ft_freqstatistics(cfg, GA_TFRFIC, GA_TFRFC)

Save the output:

    save stat_freq_planar_FICvsFC_GA stat

The output can also be obtained from [stat_freq_planar_FICvsFC_GA.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_freq/stat_freq_planar_FICvsFC_GA.mat). If you need to reload the statistics output, us

    load stat_freq_planar_FICvsFC_GA

From inspection of stat.posclusters and stat.negclusters, we observe that there is one significant negative cluster.

### Plotting the results

Plot again with **[ft_clusterplot](/reference/ft_clusterplot)**:

    cfg = [];
    cfg.alpha  = 0.025;
    cfg.parameter = 'stat';
    cfg.zlim   = [-4 4];
    cfg.layout = 'CTF151_helmet.mat';
    ft_clusterplot(cfg, stat);

{% include image src="/assets/img/tutorial/cluster_permutation_freq/figure6.png" width="600" %}

_Figure 3: T-statistic of the difference (FIC-FC) (of the combined planar gradient TFRs) and largest channel-time clusters._

#### Exercise

{% include markup/skyblue %}
Try calling clusterplot with cfg.alpha = 0.05;
{% include markup/end %}

## Summary and suggested further readings

In this tutorial, we showed how to do non-parametric statistical test, cluster-based permutation test on planar TFR's with between-trials, with within-trials and with within-subjects experimental designs. It was also shown how to plot the results.

If you are interested in parametric tests, you can read the [Parametric and non-parametric statistics on event-related fields](/tutorial/eventrelatedstatistics) tutorial. If you are interested in how to do the same statistics on event-related fields, you can read the [Cluster-based permutation tests on event-related fields](/tutorial/cluster_permutation_timelock) tutorial.

If you would like to read more about statistical analysis, you can look at the following FAQs:

{% include seealso tag1="faq" tag2="statistics" %}
{% include seealso tag1="faq" tag2="cluster"    %}
{% include seealso tag1="faq" tag2="neighbour"  %}

and example scripts:

{% include seealso tag1="example" tag2="statistics" %}
{% include seealso tag1="example" tag2="cluster"    %}
{% include seealso tag1="example" tag2="neighbour"  %}
