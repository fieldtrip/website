---
title: Cluster-based permutation tests on resting-state EEG power spectra
tags: [madrid2019, eeg-sedation]
---

# Cluster-based permutation tests on resting-state EEG power spectra

## Introduction

This tutorial gives an introduction to the statistical analysis of resting state
EEG power spectra by means of cluster-based permutation tests.

We will sketch the background of permutation tests and apply it to different
experimental questions. In this tutorial we will continue with the Chennu et al.
dataset. We will use data that has already been preprocessed and spectrally
analyzed, but if you are interested in the raw data from all subjects, you can
download it from our [download server](https://download.fieldtriptoolbox.org/workshop/madrid2019/extra/).
Please note that you **do not** have to download all subjects for this tutorial.

In a step-by-step fashion, this tutorial will show how to

1. Compute **within**-participant contrasts
2. Compute **between**-participant contrasts

Toward the end of the tutorial there are some more challenging exercises:

3. Compute a **multivariate ANOVA** to test the drug effect on the entire power spectrum
4. Compute a **2x2 interaction**
5. Compute a **correlation** between an external variable and the power spectrum

## Overview

EEG data in the study by **[Chennu et al., 2016](https://doi.org/10.1371/journal.pcbi.1004669.m)**
was recorded from multiple participants in multiple experimental conditions, i.e. levels of sedation. Data
is recorded in in blocks (runs) of 10 mins, in which the participants received
varying amounts of Propofol, an anesthetic drug, aimed to produce a relaxed but
still responsive behavioral state. For more details on the dataset
[click here](/workshop/madrid2019/eeg_sedation).

For every subject, average power spectra are computed over all segments of data
belonging to each of the sedative state. Thus, for every subject, the data are
summarized as condition-specific power spectra for each of the channels. The
question of interest is whether the data is _different_ between the sedative
states. The permutation test that will be described in the following informs us
about the following null hypothesis: the probability distribution of the
condition-specific power averages is _not different_ between the sedative
states.

## Preparing the dataset

To test the difference between the baseline and moderate sedative states, we use
data for all subjects that has been preprocessed and for which the power spectra
have been computed. You can download
[freq_resting.mat](https://download.fieldtriptoolbox.org/workshop/madrid2019/tutorial_stats/freq_resting.mat)
from our download server. The MATLAB file contains four data structures, one for each
sedation level.

    % load averages for each individual subject, for each condition
    load freq_resting.mat

Defining of regions of interest

    occipital_ROI = {'E50','T5','E59','E60','Pz','E65','E66','E67','O1','E71','E72','Oz','E76','E77','O2','E84','E85','E90','E91','T6','E101','E51','E97'};
    frontal_ROI   = {'E3','E4','E5','E6','E7','Fp2','E10','Fz','E12','E13','E15','E16','E18','E19','E20','Fp1','E23','F3','E27','E28','E29','E30','E105','E106','E111','E112','E117','E118','E123','F4'};

    cfg = [];
    cfg.keepindividual = 'yes';
    base_sedation = ft_freqgrandaverage(cfg, base_sedation{:});
    mild_sedation = ft_freqgrandaverage(cfg, mild_sedation{:});
    mode_sedation = ft_freqgrandaverage(cfg, mode_sedation{:});
    reco_sedation = ft_freqgrandaverage(cfg, reco_sedation{:});

Get the numerical indices of the regions of interest to compute averages

    sel_oROI = match_str(base_sedation.label, occipital_ROI);
    sel_fROI = match_str(base_sedation.label, frontal_ROI);

Also load the electrode positions

    elec = prepare_elec_chennu2016(base_sedation.label);

In the [frequency analysis tutorial](/workshop/madrid2019/tutorial_freq) we learnt
different ways to normalize the power spectra, here we can employ one of them.
We will normalize the power spectra for each of the individuals, using the mean
power over a frequency range defined in **freq_norm**.

    freq_oi   = [8 15];   % frequency range of interest
    freq_norm = [0.7 40]; % frequency range used to normalize the spectrum
    foi_norm  = nearest(base_sedation.freq, freq_norm);

    common_denominator = mean(base_sedation.powspctrm(:,:,foi_norm(1):foi_norm(2)),3);
    base_sedation.powspctrm_b = bsxfun(@rdivide, base_sedation.powspctrm, common_denominator);     mild_sedation.powspctrm_b = bsxfun(@rdivide, mild_sedation.powspctrm, common_denominator);
    mode_sedation.powspctrm_b = bsxfun(@rdivide, mode_sedation.powspctrm, common_denominator);
    reco_sedation.powspctrm_b = bsxfun(@rdivide, reco_sedation.powspctrm, common_denominator);

To simplify the results, let us collapse the data using the ROIs and frequency
ranges defined in the [original paper](https://doi.org/10.1371/journal.pcbi.1004669).

    cfg = [];
    cfg.channel     = frontal_ROI;
    cfg.avgoverchan = 'yes';
    cfg.frequency   = freq_oi;
    cfg.avgoverfreq = 'yes';
    cfg.parameter   = {'powspctrm','powspctrm_b'};
    base_sedation_fROI = ft_selectdata(cfg, base_sedation);
    mild_sedation_fROI = ft_selectdata(cfg, mild_sedation);
    mode_sedation_fROI = ft_selectdata(cfg, mode_sedation);
    reco_sedation_fROI = ft_selectdata(cfg, reco_sedation);

    cfg.channel     = occipital_ROI;
    base_sedation_oROI = ft_selectdata(cfg, base_sedation);
    mild_sedation_oROI = ft_selectdata(cfg, mild_sedation);
    mode_sedation_oROI = ft_selectdata(cfg, mode_sedation);
    reco_sedation_oROI = ft_selectdata(cfg, reco_sedation);

Collect the data to plot it using the `plotSpread` function, which is specific for this tutorial and available from the download server.

    data_raw_fROI    = {base_sedation_fROI.powspctrm...
      mild_sedation_fROI.powspctrm...
      mode_sedation_fROI.powspctrm...
      reco_sedation_fROI.powspctrm};
    data_raw_oROI    = {base_sedation_oROI.powspctrm...
      mild_sedation_oROI.powspctrm...
      mode_sedation_oROI.powspctrm...
      reco_sedation_oROI.powspctrm};

    data_between_fROI ={base_sedation_fROI.powspctrm_b...
      mild_sedation_fROI.powspctrm_b...
      mode_sedation_fROI.powspctrm_b...
      reco_sedation_fROI.powspctrm_b};
    data_between_oROI ={base_sedation_oROI.powspctrm_b...
      mild_sedation_oROI.powspctrm_b...
      mode_sedation_oROI.powspctrm_b...
      reco_sedation_oROI.powspctrm_b};

    figure

    subplot(2,2,1);
    plotSpread(data_raw_fROI,[],[],{'baseline','mild','moderate','recovery'});
    ylabel('abs. power (V^2)');
    title('raw PSD Front');

    subplot(2,2,2);
    h3 = plotSpread(data_between_fROI,[],[],{'baseline','mild','moderate','recovery'});
    ylabel('rel. power');
    title('between PSD Front');
    set(h3{1},'LineWidth',1,'Marker', '.','Color','k','MarkerFaceColor','k')

    subplot(2,2,3);
    plotSpread(data_raw_oROI,[],[],{'baseline','mild','moderate','recovery'});
    ylabel('abs. power (V^2)');
    title('raw PSD Occip');

    subplot(2,2,4);
    h6 = plotSpread(data_between_oROI,[],[],{'baseline','mild','moderate','recovery'});
    ylabel('rel. power');
    title('between PSD Occip');
    set(h6{1},'LineWidth',1,'Marker', '.','Color','k','MarkerFaceColor','k')

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig1_spreadplot.png" width="800" %}

Let us make topoplots and power spectra for each ROI in each sedative condition,
similar to Fig 5A in [original paper](https://doi.org/10.1371/journal.pcbi.1004669).

    cfg = [];
    cfg.elec             = elec;
    cfg.parameter        = 'powspctrm_b'; % you can plot either powspctrm (default) or powspctrm_b
    cfg.xlim             = [8 15]; % frequency range to make the topoplot
    cfg.highlight        = 'on';

We can use some options to improve the figure cosmetics.

    cfg.highlightchannel = {frontal_ROI occipital_ROI};
    cfg.highlightsymbol  = {'o','*'};
    cfg.highlightcolor   = [0 0 0];
    cfg.highlightsize    = 6;
    cfg.markersymbol     = '.';
    cfg.comment          = 'no';
    cfg.colormap         = 'jet';

    figure('position',[680 240 1039 420]);
    subplot(2,4,1); ft_topoplotER(cfg, base_sedation); colorbar; title('baseline');
    subplot(2,4,2); ft_topoplotER(cfg, mild_sedation); colorbar; title('mild');
    subplot(2,4,3); ft_topoplotER(cfg, mode_sedation); colorbar; title('moderate');
    subplot(2,4,4); ft_topoplotER(cfg, reco_sedation); colorbar; title('recovery');

    subplot(2,4,5);loglog(base_sedation.freq,...
      [squeeze(mean(mean(base_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(base_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    legend('Front ROI','Occip ROI','Location','southwest');
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('baseline');

    subplot(2,4,6);loglog(mild_sedation.freq,...
      [squeeze(mean(mean(mild_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(mild_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('mild');

    subplot(2,4,7);loglog(mode_sedation.freq,...
      [squeeze(mean(mean(mode_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(mode_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('moderate');

    subplot(2,4,8);loglog(reco_sedation.freq,...
      [squeeze(mean(mean(reco_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(reco_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('recovery');

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig2_topo_psd.png" width="600" %}

## 1. Compute **within**-participant contrasts

We now consider experiments involving multiple subjects that are each
observed in multiple experimental conditions. Typically, every subject is
observed in a large number of trials, each one belonging to one
experimental condition. Usually, for every subject, averages are computed
over all trials belonging to each of the experimental conditions. Thus,
for every subject, the data are summarized in an array of
condition-specific averages. The permutation test that is described in
this section informs us about the following **null hypothesis**: the
probability distribution of the condition-specific averages is
independent of the experimental conditions.

### Permutation test

Cluster-level permutation tests for power spectra are performed by the function
**[ft_freqstatistics](/reference/ft_freqstatistics)**. This
function takes as its input arguments a configuration structure (cfg) and
one or multiple data structures. These data structures must be produced by
**[ft_freqanalysis](/reference/ft_freqanalysis)** or
**[ft_freqgrandaverage](/reference/ft_freqgrandaverage)**. The argument list of
**[ft_freqstatistics](/reference/ft_freqstatistics)** contains
one data structure for every experimental condition. For
comparing the data structures base_sedation and mode_sedation, you must call
**[ft_freqstatistics](/reference/ft_freqstatistics)** as follows:

    % do NOT EXECUTE this yet, it is just to introduce the function
    [stat] = ft_freqstatistics(cfg, base_sedation, mode_sedation);

Many fields of the configuration (cfg), such as the selection of channels, are
not unique to
**[ft_freqstatistics](/reference/ft_freqstatistics)**; their role
is similar in other FieldTrip functions. We first concentrate on the
fields that are unique to
**[ft_freqstatistics](/reference/ft_freqstatistics)**.

    foi_contrast = [0.5 30];

    cfg = [];
    cfg.channel          = 'all';
    cfg.frequency        = foi_contrast;
    cfg.parameter        = 'powspctrm_b';
    cfg.method           = 'ft_statistics_montecarlo';  % use the Monte Carlo method to calculate probabilities
    cfg.statistic        = 'ft_statfun_depsamplesT';    % use the dependent samples T-statistic as a measure to evaluate the effect at each sample
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;                        % threshold for the sample-specific test, is used for thresholding
    cfg.clusterstatistic = 'maxsize';
    cfg.clusterthreshold = 'nonparametric_common';
    cfg.minnbchan        = 2;                           % minimum number of neighbouring channels that is required
    cfg.tail             = 0;                           % test the left, right or both tails of the distribution
    cfg.clustertail      = cfg.tail;
    cfg.alpha            = 0.05;                        % alpha level of the permutation test
    cfg.correcttail      = 'alpha';                     % see https://www.fieldtriptoolbox.org/faq/why_should_i_use_the_cfg.correcttail_option_when_using_statistics_montecarlo/
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 500;                         % number of random permutations
    cfg.neighbours       = cfg_neigh.neighbours;        % the neighbours for each sensor to form clusters

    nsubj                     = size(base_sedation.powspctrm,1);
    design                    = zeros(2,2*nsubj);
    design(1,1:nsubj)         = 1;
    design(1,nsubj+1:2*nsubj) = 2;
    design(2,1:nsubj)         = 1:nsubj;
    design(2,nsubj+1:2*nsubj) = 1:nsubj;

    cfg.design   = design; % design matrix
    cfg.ivar     = 1;      % the 1st row codes the independent variable (sedation level)
    cfg.uvar     = 2;      % the 2nd row codes the unit of observation (subject)

In the following section we will describe the various options one-by-one.

- With **cfg.method** = **[ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)**
  we choose the Monte Carlo method for calculating the significance probability.
  This significance probability is a Monte Carlo estimate of the p-value under the
  permutation distribution.

- With **cfg.statistic** = **[ft_statfun_depsamplesT](/reference/statfun/ft_statfun_depsamplesT)**
  we choose the dependent samples T-statistic to evaluate the effect (the
  difference between the baseline and the moderate condition) at the sample level.
  In cfg.statistic, many other test statistics can be specified. Which test
  statistic is appropriate depends on your research question and your experimental
  design. For instance, in a within-UO design (present one), one must use the
  dependent samples T-statistic
  (**[ft_statfun_depsamplesT](/reference/statfun/ft_statfun_depsamplesT)**). And if you
  want to compare more than two experimental conditions, you should choose an
  F-statistic (**[ft_statfun_indepsamplesT](/reference/statfun/ft_statfun_indepsamplesT)**
  or **[ft_statfun_depsamplesFmultivariate](/reference/statfun/ft_statfun_depsamplesFmultivariate)**;
  you can give a try in the Challenging exercise section below).

- We use **cfg.clusteralpha** to choose the critical value that will be
  used for thresholding the sample-specific T-statistics. With
  a value of 0.05, every sample-specific T-statistic is compared
  with the critical value of the univariate T-test with a critical
  alpha-level of 0.05. The value of cfg.clusteralpha does not affect the false
  alarm rate of the statistical test at the cluster-level. It is a rational
  threshold for deciding whether a sample should be considered a member of
  some large cluster of samples, which may or may not be significant at the
  cluster-level.

- We use **cfg.clusterstatistic** to choose the test statistic that will
  be evaluated under the permutation distribution. This is the actual test
  statistic and it must be distinguished from the sample-specific T-statistics
  that are used for thresholding. With 'maxsum', the actual test statistic is the
  maximum of the cluster-level statistics. A cluster-level statistic is equal to
  the sum of the sample-specific T-statistics that belong to this cluster. Taking
  the largest of these cluster-level statistics of the different clusters produces
  the actual test statistic.

- The value of **cfg.minnbchan** is a tuning parameter that determines
  the way the clusters are formed. More specifically, we use it to specify the
  minimum number of channels from the neighbours that is required for a selected
  sample (i.e., a sample who's T-statistic exceeds the threshold) to be included
  in the clustering algorithm. With the default value, it sometimes happens that
  two clusters are spatially connected via a narrow bridge. Because they are
  connected, these two clusters merge into a single cluster. If you want to
  interpret clusters as reflecting spatially distinct sources, such a combined
  cluster does not make much sense. To suppress this type of combined clusters,
  you can choose to ignore all selected samples (on the basis of their T-values)
  if they have less than some minimum number of neighbors that were also selected.
  This minimum number is assigned to cfg.minnbchan. This number must be chosen
  independently of the data.

- **cfg.neighbours** is a structure that you need to have previously
  created using **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)**.

- We use **cfg.tail** to choose between a one-sided and a two-sided
  statistical test. Choosing cfg.tail = 0 affects the calculations in three
  ways. First, the sample-specific T-values are thresholded from below as
  well as from above. This implies that both large negative and large
  positive T-statistics are selected for later clustering. Second,
  clustering is performed separately for thresholded positive and
  thresholded negative T-statistics. And third, the critical value for the
  cluster-level test statistic (determined by cfg.alpha; see further) is
  now two-sided: negative cluster-level statistics must be compared with
  the negative critical value, and positive cluster-level statistics must
  be compared with the positive critical value.

- We use **cfg.alpha** to control the false alarm rate of the
  permutation test (the probability of falsely rejecting the null
  hypothesis). The value of cfg.alpha determines the critical values with
  which we must compare the test statistic (i.e., the maximum and the
  minimum cluster-level statistic).

{% include markup/danger %}
If you want to run a two-sided test, i.e. you want to test both the left
(negative clusters) and the right (positive clusters) tail of the distribution.
you have to split the critical alpha value by setting cfg.correcttail = 'alpha';
i.e. this effectively does a Bonferroni correction and sets cfg.alpha = 0.025,
corresponding to a false alarm rate of 0.05 in a two-sided test.\*
{% include markup/end %}

- We use **cfg.numrandomization** to control the number of draws from
  the permutation distribution. Remember that
  **[ft_freqstatistics](/reference/ft_freqstatistics)** approximates the
  permutation distribution by means of a histogram with a Monte Carlo approximation of the true permutation distribution. In this tutorial,
  we use cfg.numrandomization = 500 to keep the computational time low. In general you should set this to a higher value (1000 or up). If it turns out that estimated p-value is very close to the the critical
  alpha-level (0.05 or 0.01), you should increase this number.

- We use **cfg.design** to store information about the independent variable
  (the experimental manipulation) and the units of observation (the subjects).
  Consider the hypothetical case that 12 participants has been observed in two
  different conditions. Then the design matrix looks like this:

```
cfg.design =

Columns 1 through 12
1     1     1     1     1     1     1     1     1     1     1     1...
1     2     3     4     5     6     7     8     9    10    11    12...

Columns 12 through 24
2     2     2     2     2     2     2     2     2     2     2     2...
1     2     3     4     5     6     7     8     9    10    11    12...
```

- We use **cfg.ivar** to indicate the row of the design matrix that
  contains the independent variable (i.e. condition).

You should be aware that the sensitivity of the statistical test (i.e., the
probability of detecting an effect) depends on the width of the frequency
interval that is analyzed, as specified in cfg.frequency. For instance, assume
that the difference between the two experimental conditions extends over a short
frequency interval only (e.g., between 8-12hz). If you would have good reasons
a-priori that this short frequency interval is the only interval where an effect
is likely to occur, then you should limit the analysis to this interval (i.e.,
choose cfg.frequency = [8 12]). Choosing a frequency interval on the basis of
prior information increases the sensitivity of the statistical test. If there is
no prior information, you must compare the experimental conditions over the
complete frequency interval. This is accomplished by choosing cfg.frequency =
'all'.

Now, run **[ft_freqstatistics](/reference/ft_freqstatistics)** to
compare base_sedation and mode_sedation using the configuration described
above.

    stat1 = ft_freqstatistics(cfg, base_sedation, mode_sedation);

### The format of the output

The output of **[ft_freqstatistics](/reference/ft_freqstatistics)** has
separate fields for positive and negative clusters. For the positive
clusters, the output is given in the following pair of fields:
stat1.posclusters and stat1.posclusterslabelmat. The field
**stat.posclusters** is an array that provides the following information
for every cluste

- The field `stat1.clusterstat` contains the cluster-level statistic (the
  sum of the T-values in each cluster).

- The field `stat1.prob` contains the proportion of draws from the
  permutation distribution with a maximum cluster-level statistic that is
  larger than clusterstat. The elements in the array stat.posclusters are
  sorted according to their p-value: the cluster with the smallest p-value
  comes first, followed by the cluster with the second-smallest, etc. Thus,
  if the k-th cluster has a p-value that is larger than the critical
  alpha-level (e.g., 0.025), then so does the (k+1)-th. Type
  stat.posclusters(k) on the MATLAB command line to see the information for
  the k-th cluster.

The field `stat1.posclusterslabelmat` contains indices (i.e. numbers 1, 2, 3,
...) that identify the clusters to which the (channel,frequency)-pairs (the samples)
belong. For example, all (channel,frequency)-pairs that belong to the third cluster,
are identified by the number 3. As will be shown in the following, this
information can be used to visualize the topography of the clusters.

For the negative clusters, the output is given in the following pair of
fields: `stat1.negclusters` and `stat1.negclusterslabelmat`. These fields
contain the same type of information as `stat1.posclusters` and
`stat1.posclusterslabelmat`, but now for the negative clusters.

By inspecting `stat1.posclusters` and `stat1.negclusters`, it can be seen that
only the first positive and the first negative cluster have a p-value less than
the critical alpha-level of 0.025. This critical alpha-level corresponds to a
false alarm rate of 0.05 in a two-sided test. You can inspect the details of the
first positive cluster like this

    stat1.posclusters(1)

    ans =
           prob: 0.2136
    clusterstat: 68
         stddev: 0.0183
        cirange: 0.0359

And by typing stat.negclusters(1), you should obtain the following:

    stat1.negclusters(1)

    ans =
           prob: 0.0020
    clusterstat: -3046
         stddev: 0.0020
        cirange: 0.0039

It is likely that the p-values in your specific output are a bit different. This
is because **[ft_freqstatistics](/reference/ft_freqstatistics)** calculated a
Monte Carlo approximation of the permutation p-values: the p-value for the k-th
positive cluster is calculated as the proportion of random draws from the
permutation distribution in which the maximum of the cluster-level statistics is
larger than `stat.posclusters(k).clusterstat`. The random draws will be
different every time you execute the code, hence the distribution will also be
slightly different.

### Plotting the results

Get the 1st positive and negative cluster

    sigposmask = (stat1.posclusterslabelmat==1) & stat1.mask;
    signegmask = (stat1.negclusterslabelmat==1) & stat1.mask;

    cfg = [];
    cfg.frequency  = foi_contrast;
    cfg.avgoverrpt = 'yes';
    cfg.parameter  = {'powspctrm','powspctrm_b'};
    base_sedation_avg = ft_selectdata(cfg, base_sedation);
    mild_sedation_avg = ft_selectdata(cfg, mild_sedation);
    mode_sedation_avg = ft_selectdata(cfg, mode_sedation);
    reco_sedation_avg = ft_selectdata(cfg, reco_sedation);

Choose the cluster you want to see: either positive or negative

    base_sedation_avg.mask = signegmask;
    mode_sedation_avg.mask = signegmask;

    cfg = [];
    cfg.elec          = elec;
    cfg.colorbar      = 'no';
    cfg.maskparameter = 'mask';  % use the thresholded probability to mask the data
    cfg.maskstyle     = 'box';
    cfg.parameter     = 'powspctrm_b';
    cfg.maskfacealpha = 0.5;

    figure; ft_multiplotER(cfg, base_sedation_avg, mode_sedation_avg);
    title('within-participant BASELINE vs MODERATE');

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig3_stats_with.png" width="600" %}

## 2. Compute **between**-participants contrasts

In a between-participant experimental designs, we analyze the data of multiple
participants that are observed during different experimental conditions, for
example comparing a control group to a patient group. In these cases we want to
answer in general the question whether there is a systematic difference in the
EEG recorded in the two groups. In the experiment that we are using, each level
of sedation has been applied to the same subject. But the way that subjects
responded to it differs, i.e. we can split the participants in a drowsy and a
responsive group.

First we compute the hit rate of each participant and condition knowing that the
number of correct responses in that task is 40. See [point
5](https://www.repository.cam.ac.uk/handle/1810/252736).

    hit_rate = (covariates(:,:,3)./40).*100;

Chennu et al 2016 made a more elaborate behavioral analysis to detect the drowsy
group. Here we just used to select arbitrarily 70% threshold to match
Figure 1B of the [original paper](https://doi.org/10.1371/journal.pcbi.1004669).

We now describe how to statistically evaluate the power spectra difference
between the responsive and the drowsy groups. The format for these variables,
are a prime example of how you should organize your data to be suitable for
**[ft_freqstatistics](/reference/ft_freqstatistics)**. Specifically, each
variable is a structure, with each subject's averaged stored in one cell. To
create this data structure we will make copies and we will select the subgroups
based on the behavioral performance (see below). Note that this subgroup
selection is orthogonal to the EEG contrast we will test.

    drowsy_group = find(hit_rate(:,3)<70);
    respon_group = setxor(1:size(covariates,1),drowsy_group);

    figure;
    plot(hit_rate(respon_group,:)','-^b','MarkerFaceColor','b');
    hold on;
    plot(hit_rate(drowsy_group,:)','marker','^','color',[0 0.5 0],'MarkerFaceColor',[0 0.5 0])
    hold off;
    ylabel('Perceptual hit rate (%)');
    set(gca,'XTickLabel',{'baseline','','mild','','moderate','','recovery'});

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig4_behav_performance.png" width="300" %}

copy the datasets and select the relevant subgroups

    [base_sedation_respon base_sedation_drowsy] = deal(base_sedation);
    [mild_sedation_respon mild_sedation_drowsy] = deal(mild_sedation);
    [mode_sedation_respon mode_sedation_drowsy] = deal(mode_sedation);
    [reco_sedation_respon reco_sedation_drowsy] = deal(reco_sedation);

    cfg = [];
    cfg.parameter   = {'powspctrm','powspctrm_b'};

    cfg.trials      = respon_group; % cfg.trials will select the 'subj' dimension
    base_sedation_respon = ft_selectdata(cfg, base_sedation_respon);
    mild_sedation_respon = ft_selectdata(cfg, mild_sedation_respon);
    mode_sedation_respon = ft_selectdata(cfg, mode_sedation_respon);
    reco_sedation_respon = ft_selectdata(cfg, reco_sedation_respon);

    cfg.trials      = drowsy_group; % cfg.trials will select the 'subj' dimension
    base_sedation_drowsy = ft_selectdata(cfg, base_sedation_drowsy);
    mild_sedation_drowsy = ft_selectdata(cfg, mild_sedation_drowsy);
    mode_sedation_drowsy = ft_selectdata(cfg, mode_sedation_drowsy);
    reco_sedation_drowsy = ft_selectdata(cfg, reco_sedation_drowsy);

We now perform the permutation test using
**[ft_freqstatistics](/reference/ft_freqstatistics)**. The configuration
settings for this analysis differ from the previous settings in several fields:

1.  We have to select a different statistic for the sample level effect (in cfg.statistic)
2.  The design matrix is different (i.c., it now contains only one row instead of two)
3.  The independent variable is now the group assignment

The configuration looks as follow:

    cfg                 = [];
    cfg.channel          = 'all';
    cfg.avgovergchan     = 'no';
    cfg.frequency        = foi_contrast;
    cfg.avgovergfreq     = 'yes';
    cfg.parameter        = 'powspctrm_b';
    cfg.method           = 'ft_statistics_montecarlo';
    cfg.statistic        = 'ft_statfun_indepsamplesT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.clusterthreshold = 'nonparametric_common';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = cfg.tail;
    cfg.alpha            = 0.05;
    cfg.correcttail      = 'alpha';
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 1000;
    cfg.neighbours       = cfg_neigh.neighbours;

    design = zeros(1,size(respon_group,1) + size(drowsy_group,1));
    design(1,1:size(respon_group,1)) = 1;
    design(1,(size(respon_group,1)+1):(size(respon_group,1)+size(drowsy_group,1))) = 2;

    cfg.design = design;
    cfg.ivar   = 1;

We now describe the differences between this configuration and the
configuration for a within-trials experiment.

- Instead of an dependent samples T-statistic, we use the **independent
  samples T-statistic** to evaluate the effect at the sample level
  (cfg.statistic = **[ft_statfun_indepsamplesT](/reference/statfun/ft_statfun_indepsamplesT)**). This is because we are
  dealing with a between-UO instead of a within-UO design.

- The **design matrix** in a between-UO design is different from the
  design matrix in a within-UO design. In the design matrix for a between-UO
  design, you have to specify the group to which each unit (subject) is assigned.
  For example, consider a hypothetical study with two experimental groups, the
  first group with 4 subjects and the second group with 6 subjects: the design
  matrix then looks like this: `design = [1 1 1 1 2 2 2 2 2 2]`. The data from the
  subjects will be shuffled between the two groups, but the number of subjects per
  group will remain the same (i.e. 4 versus 6).

Now, use the configuration above to perform the following statistical
analysis:

    stat2 = ft_freqstatistics(cfg, reco_sedation_respon, reco_sedation_drowsy);

### Plotting the results

    cfg = [];
    cfg.alpha     = stat2.cfg.alpha;
    cfg.parameter = 'stat';
    cfg.zlim      = [-3 3];
    cfg.elec      = elec;
    ft_clusterplot(cfg, stat2);

    cfg = [];
    cfg.elec         = elec;
    cfg.zlim         = [1.5 3];
    cfg.xlim         = [8 15];
    cfg.parameter    = 'powspctrm_b';
    cfg.markersymbol = '.';
    cfg.comment      = 'no';
    cfg.colormap     = 'jet';
    cfg.colorbar     = 'no';

    figure('position',[680 240 1039 420]);
    subplot(2,4,1); ft_topoplotER(cfg, base_sedation_respon); colorbar; title('base Responsive');
    subplot(2,4,2); ft_topoplotER(cfg, mild_sedation_respon); colorbar; title('mild Responsive');
    subplot(2,4,3); ft_topoplotER(cfg, mode_sedation_respon); colorbar; title('mode Responsive');
    subplot(2,4,4); ft_topoplotER(cfg, reco_sedation_respon); colorbar; title('reco Responsive');

    subplot(2,4,5); ft_topoplotER(cfg, base_sedation_drowsy); colorbar; title('base Drowsy');
    subplot(2,4,6); ft_topoplotER(cfg, mild_sedation_drowsy); colorbar; title('mild Drowsy');
    subplot(2,4,7); ft_topoplotER(cfg, mode_sedation_drowsy); colorbar; title('mode Drowsy');
    subplot(2,4,8); ft_topoplotER(cfg, reco_sedation_drowsy); colorbar; title('reco Drowsy');

We can also plot power spectra for each group separately, as a function of sedative state. Let us first plot them for the frontal region of interest:

    figure;

    subplot(2,4,1); loglog(base_sedation_respon.freq,...
      [squeeze(mean(mean(base_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(base_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    legend('Front ROI resp','Front ROI drow','Location','southwest');
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('baseline');

    subplot(2,4,2); loglog(mild_sedation_respon.freq,...
      [squeeze(mean(mean(mild_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(mild_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('mild');

    subplot(2,4,3); loglog(mode_sedation_respon.freq,...
      [squeeze(mean(mean(mode_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(mode_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('moderate');

    subplot(2,4,4); loglog(reco_sedation_respon.freq,...
      [squeeze(mean(mean(reco_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(reco_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('recover');

And for the occipital region of interest:

    subplot(2,4,5); loglog(base_sedation_respon.freq,...
      [squeeze(mean(mean(base_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
      squeeze(mean(mean(base_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    legend('Occip ROI resp','Occip ROI drow','Location','southwest');

    subplot(2,4,6); loglog(mild_sedation_respon.freq,...
      [squeeze(mean(mean(mild_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
      squeeze(mean(mean(mild_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);

    subplot(2,4,7); loglog(mode_sedation_respon.freq,...
      [squeeze(mean(mean(mode_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
      squeeze(mean(mean(mode_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);

    subplot(2,4,8); loglog(reco_sedation_respon.freq,...
      [squeeze(mean(mean(reco_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
      squeeze(mean(mean(reco_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);
    grid on; hold on;
    plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig5_topo.png" width="800" %}

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig5_psd.png" width="800" %}

{% include markup/warning %}
The remainder of the tutorial contains some more challenging exercises.
{% include markup/end %}

## 3. Compute a **multivariate ANOVA** to test the drug effect on the entire power spectrum

The Chennu et al. dataset is very rich and allows us to look at more complex
contrasts. Let us consider not only simple contract between two sedative states,
but all four states. The power spectrum of very subject is summarized in 4
arrays of condition-specific averages. The permutation test that is described in
this section addresses the following **null hypothesis**: the probability
distribution of the condition-specific averages is independent of the four
experimental conditions.

    cfg = [];
    cfg.channel          = 'all';
    cfg.frequency        = foi_contrast;
    cfg.avgovergfreq     = 'no';
    cfg.parameter        = 'powspctrm_b';
    cfg.method           = 'ft_statistics_montecarlo';
    cfg.statistic        = 'ft_statfun_depsamplesFmultivariate';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum'; %'maxsum', 'maxsize', 'wcm'
    cfg.clusterthreshold = 'nonparametric_common';
    cfg.minnbchan        = 2;
    cfg.tail             = 1; % For a F-statistic, it only make sense to calculate the right tail
    cfg.clustertail      = cfg.tail;
    cfg.alpha            = 0.05;
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 500;
    cfg.neighbours       = cfg_neigh.neighbours;

    nsubj = size(covariates,1);
    design = zeros(2,4*nsubj);
    design(1,1:nsubj)           = 1;
    design(1,nsubj+1:2*nsubj)   = 2;
    design(1,nsubj*2+1:3*nsubj) = 3;
    design(1,nsubj*3+1:4*nsubj) = 4;
    design(2,:) = repmat(1:nsubj,1,4);

    cfg.design = design;
    cfg.ivar   = 1; % sedation level
    cfg.uvar   = 2; % subject number

- We use the **[ft_statfun_depsamplesFmultivariate](/reference/statfun/ft_statfun_depsamplesFmultivariate)** for a repeated-measures (i.e. dependent samples) multivariate ANOVA.

- The **design matrix**, the **cfg.ivar** and the **cfg.uvar** will be
  the same as in the within-UO design

We now pass the data from all four conditions as input variables:

    stat3 = ft_freqstatistics(cfg, base_sedation, mild_sedation, mode_sedation, reco_sedation);

### Plotting the results

    cfg            = [];
    cfg.frequency  = foi_contrast;
    cfg.avgoverrpt = 'yes';
    cfg.parameter  = {'powspctrm','powspctrm_b'};
    base_sedation_avg = ft_selectdata(cfg, base_sedation);
    mild_sedation_avg = ft_selectdata(cfg, mild_sedation);
    mode_sedation_avg = ft_selectdata(cfg, mode_sedation);
    reco_sedation_avg = ft_selectdata(cfg, reco_sedation);

    % copy the mask field to each variable
    base_sedation_avg.mask = stat3.mask;
    mild_sedation_avg.mask = stat3.mask;
    mode_sedation_avg.mask = stat3.mask;
    reco_sedation_avg.mask = stat3.mask;

    cfg = [];
    cfg.zlim          = [0 90];
    cfg.elec          = elec;
    cfg.colorbar      = 'no';
    cfg.maskparameter = 'mask';  % use the thresholded probability to mask the data
    cfg.maskstyle     = 'box';
    cfg.parameter     = 'powspctrm_b';
    cfg.maskfacealpha = 0.1;
    figure; ft_multiplotER(cfg, base_sedation_avg, mild_sedation_avg, mode_sedation_avg, reco_sedation_avg);

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig6_manova.png" width="600" %}

## 4. Compute a **2x2 interaction**

The interaction effects are usually the most interesting in a multifactorial
design. In this dataset we will compute the interaction using the
within-participant factor SEDATION (baseline vs moderate) and the
between-subject factor GROUP (responsive vs drowsy) based on the strategy
outlined in this [frequently asked question](/faq/how_can_i_test_an_interaction_effect_using_cluster-based_permutation_tests).

Let us prepare the data

1. Compute the within-participant contrast for each group: baseline vs moderate
2. Compute the between-participant contrast of the differences computed in step 1

The complexity here is that we are dealing with a between-within
participants design, but the design matrix and statistical pipeline is the
one we used in between-participant contrast

    cfg = [];
    cfg.parameter = {'powspctrm','powspctrm_b'};
    cfg.operation = 'subtract';

    sedation_respon_d = ft_math(cfg, base_sedation_respon, mode_sedation_respon);
    sedation_drowsy_d = ft_math(cfg, base_sedation_drowsy, mode_sedation_drowsy);

    cfg = [];
    cfg.channel          = 'all';
    cfg.frequency        = foi_contrast;
    cfg.avgovergfreq     = 'no';
    cfg.parameter        = 'powspctrm_b';
    cfg.method           = 'ft_statistics_montecarlo';
    cfg.statistic        = 'ft_statfun_indepsamplesT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.clusterthreshold = 'nonparametric_common';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = cfg.tail;
    cfg.alpha            = 0.05;
    cfg.correcttail      = 'alpha';
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 1000;
    cfg.neighbours       = cfg_neigh.neighbours;

    design = zeros(1,size(respon_group,1) + size(drowsy_group,1));
    design(1,1:size(respon_group,1)) = 1;
    design(1,(size(respon_group,1)+1):(size(respon_group,1)+size(drowsy_group,1))) = 2;

    cfg.design = design;
    cfg.ivar   = 1;

    stat4 = ft_freqstatistics(cfg, sedation_respon_d, sedation_drowsy_d);

Now select the significant sensors and frequencies and plot the interaction.

Get the 1st positive and negative cluster

    signegmask = (stat4.negclusterslabelmat==1) & stat4.mask;

Pool all channels and frequencies that in the cluster

    chanoineg = match_str(stat4.label,stat4.label(sum(signegmask,2) > 0));
    foilimneg = stat4.freq(sum(signegmask,1) > 0);
    foilim = [min(foilimneg) max(foilimneg)];

Choose the cluster you want to see

    base_sedation_avg.mask = signegmask;
    mode_sedation_avg.mask = signegmask;

Choose the cluster you want to see: positive or negative

    base_sedation_avg.mask = signegmask;
    mode_sedation_avg.mask = signegmask;

    cfg = [];
    cfg.frequency   = foilim;
    cfg.avgoverfreq = 'yes';
    cfg.channel     = chanoineg;
    cfg.avgoverchan = 'yes';
    cfg.parameter   = {'powspctrm','powspctrm_b'};
    b_r = ft_selectdata(cfg, base_sedation_respon);
    m_r = ft_selectdata(cfg, mode_sedation_respon);
    b_d = ft_selectdata(cfg, base_sedation_drowsy);
    m_d = ft_selectdata(cfg, mode_sedation_drowsy);

Compute the confidence intervals

    parameter = 'powspctrm_b'; % make sure this is the same as the one used in ft_freqstatistics

Compute the means

    x_b_r = mean(b_r.(parameter),1);
    x_m_r = mean(m_r.(parameter),1);
    x_b_d = mean(b_d.(parameter),1);
    x_m_d = mean(m_d.(parameter),1);

    sem_b_r = sem(b_r.(parameter),1);
    sem_m_r = sem(m_r.(parameter),1);
    sem_b_d = sem(b_d.(parameter),1);
    sem_m_d = sem(m_d.(parameter),1);

    figure;

    errorbar([1 2],[x_b_r,x_m_r]',[sem_b_r,sem_m_r(1)],'-rs');
    ylabel(parameter);
    hold all
    errorbar([1 2],[x_b_d x_m_d]',[sem_b_r,sem_m_r],'-bs');
    ylabel(parameter);
    xlim([0 3]);
    ylim([-0.5 1.5]);
    title(['Interaction ' num2str(foilim(1)) '-' num2str(foilim(2)) 'Hz band'])
    set(gca,'XTickLabel',{'','','baseline','','moderate','',''});
    legend('Responsive','Drowsy','Location','northwest');

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig7_interaction.png" width="600" %}

## 5. Compute a **correlation** between an external variable and the power spectrum

Here we will test for correlations between other external quantitative variable and the EEG data.

A common perspective on statistical testing starts from the distinction between
dependent and independent variables. The EEG signals are typically considered to
be the dependent variable. The independent variable can be the experimental
conditions, as defined by task instructions, stimulus type, learning history,
etc. The label _independent variable_ suggests that it must be under the
experimenter's control. However, this is not necessarily the case, for example
in case of reaction times, response accuracy or the drug concentrations in the blood.

Because neither the behavioral accuracy, nor the neural activity are under
precise experimental control, it is arbitrary how the roles of dependent and
independent variable are assigned. In FieldTrip, we use the convention that the
variable with the smallest dimensionality is assigned the role of independent
variable. For our example, this implies that accuracy is assigned the role of
independent and the neurobiological signal the role of dependent variable. In
fact, accuracy is represented by a single number, whereas the neurobiological
signal often has a spatial (the channels) and a spectral (the frequencies)
dimension. More information can be found in this [frequently asked
question](/faq/how_can_i_test_for_correlations_between_neuronal_data_and_quantitative_stimulus_and_behavioural_variables).

### The Permutation Distribution Results From Breaking the Association Between Dependent and Independent Variable

The null hypothesis that is tested by a permutation test involves that the
probability distribution of the dependent variable is identical for all possible
values of the independent variable. Quantitative independent variables, such us
drug concentration, may have an infinite number of values, and in this case it
is more difficult to conceptualize the probability distributions within each of
these values. However, there is a null hypothesis for quantitative independent
variables: **statistical independence** between the dependent and the
independent variable. Testing for this statistical independence is possible in
the same way for categorical as for quantitative independent variables: breaking
the association between dependent and independent variable by randomly permuting
the values of the independent variable. In a between-UO design, these values are
permuted across the UOs, and in a within-UO design, they are permuted across the
conditions in which the UO has been observed.

It is important to point out that the hypothesis of statistical independence
rules out _all possible_ relations between the dependent and a quantitative
independent variable, and not only the linear relation. This contrasts with the
three test statistics for quantitative independent variables that are
implemented in FieldTrip: these are only sensitive to deviations from
statistical independence that can be captured as a **linear** relation between
the dependent and the independent variable. Of course, new test statistics can
be formulated (and implemented as statfuns) with a sensitivity profile that is
optimized for particular non-linear deviations from statistical independence.

### Statistical Testing of the Relation Between a Neurobiological and a Behavioral Variable

Now, it is time to prepare the data as follows:

1. Compute the within-participant contrast for each group: baseline vs moderate
2. Compute the between-participant contrast of the differences computed in step 1

```
    cfg = [];
    cfg.channel          = 'all';
    cfg.frequency        = [8 20]; % let us test alpha and low beta bands
    cfg.avgoverfreq      = 'no';
    cfg.avgoverchan      = 'no';
    cfg.parameter        = 'powspctrm_b';
    cfg.method           = 'ft_statistics_montecarlo';
    cfg.statistic        = 'ft_statfun_correlationT';
    cfg.type             = 'spearman'; % type of the correlation (see help corr to know other types)
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsize';
    cfg.clusterthreshold = 'nonparametric_common';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = 0;
    cfg.alpha            = 0.05;
    cfg.correcttail      = 'alpha';
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 1000;
    cfg.neighbours       = cfg_neigh.neighbours;

    subj = size(mode_sedation.powspctrm,1);
    design = zeros(1,subj);

    % The three columns of the covariates are
    %  - drug concentration
    %  - reaction time
    %  - correct responses

    design(1,:)  = covariates(:,3,1)./1000; % select the column with concentrations
    cfg.design   = design;
    cfg.ivar     = 1;

    stat5 = ft_freqstatistics(cfg, mode_sedation);

    cfg            = [];
    cfg.alpha      = stat5.cfg.alpha;
    cfg.parameter  = 'stat';
    cfg.zlim       = [-3 3];
    cfg.elec       = elec;
    ft_clusterplot(cfg, stat5);
```

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig8_corr.png" width="800" %}
