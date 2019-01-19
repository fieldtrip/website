---
title: Cluster-based permutation tests on resting-state Power Spectral Density
tags: [eeg-chennu, madrid2019]
---

# Cluster-based permutation tests on resting-state Power Spectral Density (PSD)

## Introduction

The objective of this tutorial is to give an introduction to the
statistical analysis of resting state EEG data by means of cluster-based
permutation tests.

The tutorial starts with a long background section that sketches the
background of permutation tests. The next sections are more
tutorial-like. They deal with the analysis of an actual EEG dataset
[(Download full dataset here)](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/madrid19/extra/).

In a step-by-step fashion, this tutorial will show:

1. Compute **within**-participant contrasts
2. Compute **between**-participant contrasts

 Toward the end of the tutorial there are some more challenging exercises:

3. Compute a **multivariate ANOVA**  to test the effect of the (drug) intervention on the entire EEG spectrum.
4. Compute a **2x2 interaction**
5. Compute a **correlation** between a variable and the EEG spectrum

## Overview

In this paragraph we describe permutation testing for PSD data obtained
in **[Chennu et al., 2016](https://doi.org/10.1371/journal.pcbi.1004669)**
involving multiple participants that are each observed in multiple
experimental conditions (sedative states). Every participant is observed
during a period of 10 mins, where they received an amount of anesthetic
drug aimed to produce a relaxed but still responsive behavioural state.
For every subject, averages are computed over all segments of data
belonging to each sedative state. (For more details on the dataset
[click here](/workshop/madrid2019/eeg_chennu)). Thus, for every subject, the data are
summarized in an array of condition-specific averages of power.
The permutation test that will be described in the following informs us about
the following null hypothesis: the probability distribution of the
condition-specific power averages is identical for all sedative states
(baseline vs moderate).

## Preparing the dataset

To test the difference between the average PSDs for baseline and moderate
sedative states. The data structures containing the frequency data
averages of all 20 participants are available [here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/madrid19/tutorial_stats.mat)

    % averages for each individual subject, for each condition
    load freq_resting.mat

Defining of regions of interest

    occipital_ROI = {'E50','T5','E59','E60','Pz','E65','E66','E67','O1','E71','E72','Oz','E76','E77','O2','E84','E85','E90','E91','T6','E101','E51','E97'};
    frontal_ROI   = {'E3','E4','E5','E6','E7','Fp2','E10','Fz','E12','E13','E15','E16','E18','E19','E20','Fp1','E23','F3','E27','E28','E29','E30','E105','E106','E111','E112','E117','E118','E123','F4'};

    cfg = [];
    cfg.keepindividual = 'yes';
    base_sedation = ft_freqgrandaverage(cfg,base_sedation{:});
    mild_sedation = ft_freqgrandaverage(cfg,mild_sedation{:});
    mode_sedation = ft_freqgrandaverage(cfg,mode_sedation{:});
    reco_sedation = ft_freqgrandaverage(cfg,reco_sedation{:});

get the numerical indices to compute averages

    sel_oROI = match_str(base_sedation.label,occipital_ROI);
    sel_fROI = match_str(base_sedation.label,frontal_ROI);

    elec = prepare_elec_chennu2016(base_sedation.label);

Now we are going to normalize the PSD using the mean taken over a frequency range defined in **freq_norm**.

In the **[resting state frequency analysis](/workshop/madrid2019/tutorial_freq)** we learnt different ways to normalize the PSD and here we can employ one of them

    freq_oi   = [8 15];   % frequency range to display averages
    freq_norm = [0.7 40]; % frequency range used to normalize the spectrum
    foi_norm = nearest(base_sedation.freq,freq_norm);

    common_denominator = mean(base_sedation.powspctrm(:,:,foi_norm(1):foi_norm(2)),3);
    base_sedation.powspctrm_b = bsxfun(@rdivide, base_sedation.powspctrm, common_denominator); %repmat(mean(base_sedation.powspctrm,3),1,1,90);
    mild_sedation.powspctrm_b = bsxfun(@rdivide, mild_sedation.powspctrm, common_denominator);
    mode_sedation.powspctrm_b = bsxfun(@rdivide, mode_sedation.powspctrm, common_denominator);
    reco_sedation.powspctrm_b = bsxfun(@rdivide, reco_sedation.powspctrm, common_denominator);

to simplify the results, let us collapse the data using the ROIs and
frequency ranges defined in the paper

    cfg = [];
    cfg.channel     = frontal_ROI;
    cfg.avgoverchan = 'yes';
    cfg.frequency   = freq_oi;
    cfg.avgoverfreq = 'yes';
    cfg.parameter   = {'powspctrm','powspctrm_b'};
    base_sedation_fROI = ft_selectdata(cfg,base_sedation);
    mild_sedation_fROI = ft_selectdata(cfg,mild_sedation);
    mode_sedation_fROI = ft_selectdata(cfg,mode_sedation);
    reco_sedation_fROI = ft_selectdata(cfg,reco_sedation);

    cfg.channel     = occipital_ROI;
    base_sedation_oROI = ft_selectdata(cfg,base_sedation);
    mild_sedation_oROI = ft_selectdata(cfg,mild_sedation);
    mode_sedation_oROI = ft_selectdata(cfg,mode_sedation);
    reco_sedation_oROI = ft_selectdata(cfg,reco_sedation);

collect the data to plot it using plotSpread

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

    figure('Position',[30 197 1281 420]);
    subplot(221);
    plotSpread(data_raw_fROI,[],[],{'baseline','mild','moderate','recovery'});ylabel('abs. power (V^2)');
    title('raw PSD Front');
    subplot(222);
    h3 = plotSpread(data_between_fROI,[],[],{'baseline','mild','moderate','recovery'});ylabel('rel. power');
    title('between PSD Front');
    set(h3{1},'LineWidth',1,'Marker', '.','Color','k','MarkerFaceColor','k')

    subplot(223);
    plotSpread(data_raw_oROI,[],[],{'baseline','mild','moderate','recovery'});ylabel('abs. power (V^2)');
    title('raw PSD Occip');
    subplot(224);
    h6 = plotSpread(data_between_oROI,[],[],{'baseline','mild','moderate','recovery'});ylabel('rel. power');
    title('between PSD Occip');
    set(h6{1},'LineWidth',1,'Marker', '.','Color','k','MarkerFaceColor','k')

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig1_spreadplot.png" width="800" %}

 Let us make topoplots and the PSD for each ROI for each sedative condition (similar to Fig 5A in Chennu et al.,)

    cfg = [];
    cfg.elec             = elec;
    cfg.parameter        = 'powspctrm_b'; % you can test any of the subfields: powspctrm, powspctrm_w, powspctrm_b
    cfg.xlim             = [8 15]; % frequency range to make the topoplot
    cfg.highlight        = 'on';

here the figure cosmetics

    cfg.highlightchannel = {frontal_ROI occipital_ROI};
    cfg.highlightsymbol  = {'o','*'};
    cfg.highlightcolor   = [0 0 0];
    cfg.highlightsize    = 6;
    cfg.markersymbol     = '.';
    cfg.comment          = 'no';
    cfg.colormap         = 'jet';

    figure('position',[680 240 1039 420]);
    subplot(241);ft_topoplotER(cfg,base_sedation);colorbar;title('baseline');
    subplot(242);ft_topoplotER(cfg,mild_sedation);colorbar;title('mild');
    subplot(243);ft_topoplotER(cfg,mode_sedation);colorbar;title('moderate');
    subplot(244);ft_topoplotER(cfg,reco_sedation);colorbar;title('recovery');

    subplot(245);loglog(base_sedation.freq,...
      [squeeze(mean(mean(base_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(base_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    legend('Front ROI','Occip ROI','Location','southwest');
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('baseline');

    subplot(246);loglog(mild_sedation.freq,...
      [squeeze(mean(mean(mild_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(mild_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('mild');

    subplot(247);loglog(mode_sedation.freq,...
      [squeeze(mean(mean(mode_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(mode_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('moderate');

    subplot(248);loglog(reco_sedation.freq,...
      [squeeze(mean(mean(reco_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(reco_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
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

Cluster-level permutation tests for PSD data are performed by the function
**[ft_freqstatistics](/reference/ft_freqstatistics)**. This
function takes as its input arguments a configuration structure (cfg) and
two or more data structures. These data structures must be produced by
**[ft_freqanalysis](/reference/ft_freqanalysis)** or
**[ft_freqgrandaverage](/reference/ft_freqgrandaverage)**, which
all operate on preprocessed data. The argument list of
**[ft_freqstatistics](/reference/ft_freqstatistics)** must
contain one data structure for every experimental condition. For
comparing the data structures base_sedation and mode_sedation, you must call
**[ft_freqstatistics](/reference/ft_freqstatistics)** as follows:
[stat] = ft_freqstatistics(cfg, base_sedation, mode_sedation);

#### The configuration settings

Some fields of the configuration (cfg), such as channel and latency, are
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
    cfg.method           = 'ft_statistics_montecarlo';% use the Monte Carlo Method to calculate the significance probability
    cfg.statistic        = 'ft_statfun_depsamplesT';% use the dependent samples T-statistic as a measure to evaluate the effect at the sample level
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;% alpha level of the sample-specific test statistic that will be used for thresholding
    cfg.clusterstatistic = 'maxsize';
    cfg.clusterthreshold = 'nonparametric_common';
    cfg.minnbchan        = 2;% minimum number of neighborhood channels that is required for a selected sample to be included in the clustering algorithm (default=0).
    cfg.tail             = 0;% -1, 1 or 0 (default = 0); one-sided or two-sided test
    cfg.clustertail      = cfg.tail;
    cfg.alpha            = 0.05; % alpha level of the permutation test
    cfg.correcttail      = 'alpha'; % http://www.fieldtriptoolbox.org/faq/why_should_i_use_the_cfg.correcttail_option_when_using_statistics_montecarlo/
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 500; % number of draws from the permutation distribution
    cfg.neighbours       = cfg_neigh.neighbours;% the neighbours specify for each sensor with which other sensors it can form clusters

    subj = size(base_sedation.powspctrm,1);
    design = zeros(2,2*subj);
    design(1,1:subj)        = 1;
    design(1,subj+1:2*subj) = 2;
    design(2,1:subj)        = 1:subj;
    design(2,subj+1:2*subj) = 1:subj;

    cfg.design = design; % design matrix
    cfg.ivar     = 1;% number or list with indices indicating the independent variable(s)
    cfg.uvar     = 2;% number or list with indices indicating the dependent variable(s)

# We now describe these options one-by-one.

-  With **cfg.method** = **[ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)** we choose the Monte Carlo method
for calculating the significance probability. This significance
probability is a Monte Carlo estimate of the p-value under the
permutation distribution.

-  With **cfg.statistic** = **[ft_statfun_depsamplesT](/reference/ft_statfun_depsamplesT)**, we choose the
dependent samples T-statistic to evaluate the effect (the difference
between the baseline and the moderate condition) at the sample level. In
cfg.statistic, many other test statistics can be specified. Which test
statistic is appropriate depends on your research question and your
experimental design. For instance, in a within-UO design (present one),
one must use the dependent samples T-statistic
(**[ft_statfun_depsamplesT](/reference/ft_statfun_depsamplesT)**). And if you want to compare more than two
experimental conditions, you should choose an F-statistic
(**[ft_statfun_indepsamplesT](/reference/ft_statfun_indepsamplesT)** or **[ft_statfun_depsamplesFmultivariate](/reference/ft_statfun_depsamplesFmultivariate)**; you
can give a try in the Challenging exercise section below).

-  We use **cfg.clusteralpha** to choose the critical value that will be
used for thresholding the sample-specific T-statistics. With
cfg.clusteralpha = 0.05, every sample-specific T-statistic is compared
with the critical value of the univariate T-test with a critical
alpha-level of 0.05. (This statistical test would have been the most
appropriate test if we had observed a single channel at a single
time-point.) The value of cfg.clusteralpha does not affect the false
alarm rate of the statistical test at the cluster-level. It is a rational
threshold for deciding whether a sample should be considered a member of
some large cluster of samples (which may or may not be significant at the
cluster-level).

-  We use **cfg.clusterstatistic** to choose the test statistic that will
be evaluated under the permutation distribution. This is the actual test
statistic and it must be distinguished from the sample-specific
T-statistics that are used for thresholding. With cfg.clusterstatistic =
'maxsum', the actual test statistic is the maximum of the cluster-level
statistics. A cluster-level statistic is equal to the sum of the
sample-specific T-statistics that belong to this cluster. Taking the
largest of these cluster-level statistics of the different clusters
produces the actual test statistic.

-  The value of **cfg.minnbchan** is a tuning parameter that determines
the way the clusters are formed. More specifically, we use cfg.minnbchan
to specify the minimum number of neighborhood channels that is required
for a selected sample (i.e., a sample who's T-value exceeds the
threshold) to be included in the clustering algorithm. With cfg.minnbchan
= 0 (the default), it sometimes happens that two clusters are spatially
connected via a narrow bridge of samples. Because they are connected,
these two clusters are considered as a single cluster. If clusters are
interpreted as reflecting spatially distinct sources, such a combined
cluster does not make much sense. To suppress this type of combined
clusters, one can choose to ignore all selected samples (on the basis of
their T-values) if they have less than some minimum number of neighbors
that were also selected. This minimum number is assigned to
cfg.minnbchan. This number must be chosen independently of the data.

-  **cfg.neighbours** is a structure that you need to have previously
created using **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)**.

-  We use **cfg.tail** to choose between a one-sided and a two-sided
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

-  We use **cfg.alpha** to control the false alarm rate of the
permutation test (the probability of falsely rejecting the null
hypothesis). The value of cfg.alpha determines the critical values with
which we must compare the test statistic (i.e., the maximum and the
minimum cluster-level statistic).

{% include markup/danger %}
*Note that if you want to run a
two-sided test, you have to split the critical alpha value by setting
cfg.correcttail = 'alpha'; i.e. this sets cfg.alpha = 0.025,
corresponding to a false alarm rate of 0.05 in a two-sided test.*
{% include markup/end %}

The field cfg.alpha is not crucial. This is because the output of
**[ft_timelockstatistics](/reference/ft_timelockstatistics)** (see
further) contains a p-value for every cluster (calculated under the
permutation distribution of the maximum/minimum cluster-level statistic).
Instead of the critical values, we can also use these p-values to
determine the significance of the clusters.

-  We use **cfg.numrandomization** to control the number of draws from
the permutation distribution. Remember that
**[ft_freqstatistics](/reference/ft_freqstatistics)** approximates the
permutation distribution by means of a histogram. This histogram is a
so-called Monte Carlo approximation of the permutation distribution. This
Monte Carlo approximation is used to calculate the p-values and the
critical values that are shown in the output of
**[ft_freqstatistics](/reference/ft_freqstatistics)**. In this tutorial,
we use cfg.numrandomization = 500. As a rule of thumb, you can double
this number if it turns out that the p-value differs from the critical
alpha-level (0.05 or 0.01) by less than 0.02.

-  We use **cfg.design** to store information about the UOs. The content
of cfg.design must be a matrix. Consider the hypothetical case that 20
participants has been observed in two different conditions. Then the
correct design matrix looks like this:

```
cfg.design =

Columns 1 through 20
1     1     1     1     1     1     1     1     1     1     1     1...
1     2     3     4     5     6     7     8     9    10    11    12...

Columns 21 through 40
2     2     2     2     2     2     2     2     2     2     2     2...
1     2     3     4     5     6     7     8     9    10    11    12...
```

-  We use **cfg.ivar** to indicate the row of the design matrix that
contains the independent variable. For a within-trials statistical
analysis the design matrix must contain more than one row, with cfg.ivar
indicating the experimental condition and the cfg.uvar indicating the participant

One should be aware of the fact that the sensitivity of
**[ft_freqstatistics](/reference/ft_freqstatistics)** (i.e., the
probability of detecting an effect) depends on the length of the
frequency interval that is analyzed, as specified in cfg.frequency. For
instance, assume that the difference between the two experimental
conditions extends over a short frequency interval only (e.g., between
8-12hz). If it is known in advance that this short frequency interval is
the only interval where an effect is likely to occur, then one should
limit the analysis to this time interval (i.e., choose cfg.frequency = [8
12]). Choosing a frequency interval on the basis of prior information
about the frequency range of the effect will increase the sensitivity of
the statistical test. If there is no prior information, then one must
compare the experimental conditions over the complete frequency interval. This
is accomplished by choosing cfg.frequency = 'all'.

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

-  The field **clusterstat** contains the cluster-level statistic (the
sum of the T-values in this cluster).

-  The field **prob** contains the proportion of draws from the
permutation distribution with a maximum cluster-level statistic that is
larger than clusterstat. The elements in the array stat.posclusters are
sorted according to their p-value: the cluster with the smallest p-value
comes first, followed by the cluster with the second-smallest, etc. Thus,
if the k-th cluster has a p-value that is larger than the critical
alpha-level (e.g., 0.025), then so does the (k+1)-th. Type
stat.posclusters(k) on the MATLAB command line to see the information for
the k-th cluster.

The field stat.posclusterslabelmat is a spatiotemporal matrix. This
matrix contains numbers that identify the clusters to which the
(channel,time)-pairs (the samples) belong. For example, all
(channel,time)-pairs that belong to the third cluster, are identified by
the number 3. As will be shown in the following, this information can be
used to visualize the topography of the clusters.

For the negative clusters, the output is given in the following pair of
fields: stat1.negclusters and stat1.negclusterslabelmat. These fields
contain the same type of information as stat.posclusters and
stat1.posclusterslabelmat, but now for the negative clusters.

By inspecting stat1.posclusters and stat1.negclusters, it can be seen that
only the first positive and the first negative cluster have a p-value
less than the critical alpha-level of 0.025. This critical alpha-level
corresponds to a false alarm rate of 0.05 in a two-sided test. By typing
stat1.posclusters(1) on the MATLAB command line, you should obtain the
following:

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

It is possible that the p-values in your output are a little bit
different from 0. This is because
**[ft_freqstatistics](/reference/ft_freqstatistics)** calculated
as a Monte Carlo approximation of the permutation p-values: the p-value
for the k-th positive cluster is calculated as the proportion of random
draws from the permutation distribution in which the maximum of the
cluster-level statistics is larger than stat.posclusters(k).clusterstat.

### Plotting the results

    get the 1st positive and negative cluster
    sigposmask = (stat1.posclusterslabelmat==1) & stat1.mask;
    signegmask = (stat1.negclusterslabelmat==1) & stat1.mask;

    cfg = [];
    cfg.frequency  = foi_contrast;
    cfg.avgoverrpt = 'yes';
    cfg.parameter  = {'powspctrm','powspctrm_b'};
    base_sedation_avg = ft_selectdata(cfg,base_sedation);
    mild_sedation_avg = ft_selectdata(cfg,mild_sedation);
    mode_sedation_avg = ft_selectdata(cfg,mode_sedation);
    reco_sedation_avg = ft_selectdata(cfg,reco_sedation);

  choose the cluster you want to see: POSITIVE or NEGATIVE

    base_sedation_avg.mask = signegmask;
    mode_sedation_avg.mask = signegmask;

    cfg = [];
    cfg.elec          = elec;
    cfg.colorbar      = 'no';
    cfg.maskparameter = 'mask';  % use the thresholded probability to mask the data
    cfg.maskstyle     = 'box';
    cfg.parameter     = 'powspctrm_b';
    cfg.maskfacealpha = 0.5;
    figure;ft_multiplotER(cfg,base_sedation_avg,mode_sedation_avg);
    title('within-participant BASELINE vs MODERATE');

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig3_stats_with.png" width="600" %}

## 2. Compute  **between**-participants contrasts

In a between-participatn experiment, we analyze the data of multiple
participants observed during different experimental conditions. By means
of a statistical test, we want to answer the question whether there is a
systematic difference in the EEG recorded on responsive and drowsy groups

First we compute the hit rate of each participant and condition knowing
that the number of correct responses in that task is 40. See [point 5)](https://www.repository.cam.ac.uk/handle/1810/252736).

    hit_rate = (covariates(:,:,3)./40).*100;

Chennu et al 2016 made a proper behavioral analysis to detect the drowsy
group. Here we just used to select arbitrarily 70% threshold to match
Figure 1B of the [paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004669#sec008)

We now describe how we can statistically test the difference between the
PSD averages for the responsive and the drowsy groups. The format for
these variables, are a prime example of how you should organise your data
to be suitable for ft_XXXstatistics. Specifically, each variable is a
structure, with each subject's averaged stored in one cell. To create
this data structure we will make copies and we will select the subgroups
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

    [base_sedation_respon base_sedation_drowsy]=deal(base_sedation);
    [mild_sedation_respon mild_sedation_drowsy]=deal(mild_sedation);
    [mode_sedation_respon mode_sedation_drowsy]=deal(mode_sedation);
    [reco_sedation_respon reco_sedation_drowsy]=deal(reco_sedation);

    cfg = [];
    cfg.trials      = respon_group; % cfg.trials will select the 'subj' dimension
    cfg.parameter   = {'powspctrm','powspctrm_b'};
    base_sedation_respon = ft_selectdata(cfg,base_sedation_respon);
    mild_sedation_respon = ft_selectdata(cfg,mild_sedation_respon);
    mode_sedation_respon = ft_selectdata(cfg,mode_sedation_respon);
    reco_sedation_respon = ft_selectdata(cfg,reco_sedation_respon);

    cfg.trials      = drowsy_group;
    base_sedation_drowsy = ft_selectdata(cfg,base_sedation_drowsy);
    mild_sedation_drowsy = ft_selectdata(cfg,mild_sedation_drowsy);
    mode_sedation_drowsy = ft_selectdata(cfg,mode_sedation_drowsy);
    reco_sedation_drowsy = ft_selectdata(cfg,reco_sedation_drowsy);

We now perform the permutation test using
**[ft_freqstatistics](/reference/ft_freqstatistics)**. The
configuration settings for this analysis differ from the previous
settings in several fields:

 1.  We have to select a different measure to evaluate the effect at sample level (in cfg.statistic)
 2.  The design matrix is different (i.c., it now contains only one line instead of two)
 3.  The so-called *unit variable* has to be defined.

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

-  Instead of an dependent samples T-statistic, we use the **independent
samples T-statistic** to evaluate the effect at the sample level
(cfg.statistic = **[ft_statfun_indepsamplesT](/reference/ft_statfun_indepsamplesT)**). This is because we are
dealing with a between-UO instead of a within-UO design.

-  The **design matrix** in a between-UO design is different from the
design matrix in a within-UO design. In the design matix for a between-UO
design, you have to specify the unit variable. The unit variable
specifies the units that have produced the different condition-specific
data structures. For example, consider a hypothetical study with 2
experimental groups of 4 participants. The design matrix may then look
like this: design = [1 1 1 1 2 2 2 2 ]. The first row of this matrix is
the unit variable

Now, use the configuration above to perform the following statistical
analysis

    stat2 = ft_freqstatistics(cfg, reco_sedation_respon,reco_sedation_drowsy);

### Plotting the results

    cfg           = [];
    cfg.alpha     = stat2.cfg.alpha;
    cfg.parameter = 'stat';
    cfg.zlim      = [-3 3];
    cfg.elec      = elec;
    ft_clusterplot(cfg, stat2);

    cfg           = [];
    cfg.elec      = elec;
    cfg.zlim      = [1.5 3];
    cfg.xlim      = [8 15];
    cfg.parameter = 'powspctrm_b';
    cfg.markersymbol = '.';
    cfg.comment   = 'no';
    cfg.colormap  = 'jet';
    cfg.colorbar  = 'no';

    figure('position',[680 240 1039 420]);
    subplot(241);ft_topoplotER(cfg,base_sedation_respon);colorbar;title('base Responsive');
    subplot(242);ft_topoplotER(cfg,mild_sedation_respon);colorbar;title('mild Responsive');
    subplot(243);ft_topoplotER(cfg,mode_sedation_respon);colorbar;title('mode Responsive');
    subplot(244);ft_topoplotER(cfg,reco_sedation_respon);colorbar;title('reco Responsive');

    subplot(245);ft_topoplotER(cfg,base_sedation_drowsy);colorbar;title('base Drowsy');
    subplot(246);ft_topoplotER(cfg,mild_sedation_drowsy);colorbar;title('mild Drowsy');
    subplot(247);ft_topoplotER(cfg,mode_sedation_drowsy);colorbar;title('mode Drowsy');
    subplot(248);ft_topoplotER(cfg,reco_sedation_drowsy);colorbar;title('reco Drowsy');

PSDs for each group separately as a function of sedative state

    figure('position',[680 240 1039 420]);
    subplot(241);loglog(base_sedation_respon.freq,...
      [squeeze(mean(mean(base_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(base_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    legend('Front ROI resp','Front ROI drow','Location','southwest');
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('baseline');

    subplot(242);loglog(mild_sedation_respon.freq,...
      [squeeze(mean(mean(mild_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(mild_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('mild');

    subplot(243);loglog(mode_sedation_respon.freq,...
      [squeeze(mean(mean(mode_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(mode_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('moderate');

    subplot(244);loglog(reco_sedation_respon.freq,...
      [squeeze(mean(mean(reco_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
      squeeze(mean(mean(reco_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('recover');

PSDs from occipital ROI

    subplot(245);loglog(base_sedation_respon.freq,...
      [squeeze(mean(mean(base_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
      squeeze(mean(mean(base_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    legend('Occip ROI resp','Occip ROI drow','Location','southwest');

    subplot(246);loglog(mild_sedation_respon.freq,...
      [squeeze(mean(mean(mild_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
      squeeze(mean(mean(mild_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);

    subplot(247);loglog(mode_sedation_respon.freq,...
      [squeeze(mean(mean(mode_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
      squeeze(mean(mean(mode_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);

    subplot(248);loglog(reco_sedation_respon.freq,...
      [squeeze(mean(mean(reco_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
      squeeze(mean(mean(reco_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig5_topo.png" width="800" %}

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig5_psd.png" width="800" %}


# CHALLENGING EXERCISES!!!
## 3. Compute a **multivariate ANOVA**  to test the effect of the (drug) intervention on the entire EEG spectrum.

Present Chennu et al. dataset is very rich and it will allow us to ask
more complex contrasts. Let's now consider not only two but the 4
sedative states involving multiple subjects. Every subject is summarized in 4 arrays
of condition-specific averages. The permutation test that is described in
this section informs us about the following **null hypothesis**: the
probability distribution of the condition-specific averages is
independent of the experimental conditions.

We now describe how we can statistically test the difference between the
event-related averages for fully incongruent (FIC) and the fully
congruent (FC) sentence endings. For this analysis we use planar gradient
data. For convenience we will not do the reading-in and preprocessing
steps on all subjects. Instead we begin by loading the timelock
structures containing the event-related averages (of the planar gradient
data) of all ten subjects.

    cfg = [];
    cfg.channel          = 'all';
    cfg.frequency        = foi_contrast;
    cfg.avgovergfreq     = 'no';
    cfg.parameter        = 'powspctrm_b';
    cfg.method           = 'ft_statistics_montecarlo';
    cfg.statistic        = 'ft_statfun_depsamplesFmultivariate';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';%'maxsum', 'maxsize', 'wcm'
    cfg.clusterthreshold = 'nonparametric_common';
    cfg.minnbchan        = 2;
    cfg.tail             = 1; % For a F-statistic, it only make sense to calculate the right tail
    cfg.clustertail      = cfg.tail;
    cfg.alpha            = 0.05;
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 500;
    cfg.neighbours       = cfg_neigh.neighbours;

    subj = size(covariates,1);
    design = zeros(2,4*subj);
    design(1,1:subj)          = 1;
    design(1,subj+1:2*subj)   = 2;
    design(1,subj*2+1:3*subj) = 3;
    design(1,subj*3+1:4*subj) = 4;
    design(2,:) = repmat(1:subj,1,4);

    cfg.design = design;
    cfg.ivar   = 1;
    cfg.uvar   = 2;

-  We use the **[ft_statfun_depsamplesFmultivariate](/reference/ft_statfun_depsamplesFmultivariate)** to evaluate
calculates the MANOVA dependent samples to test

-  The **design matrix**, the **cfg.ivar** and the **cfg.uvar** will be
the same as in the within-UO design


~~~~
    stat3 = ft_freqstatistics(cfg, base_sedation, mild_sedation, mode_sedation, reco_sedation);
~~~~

### Plotting the results

    cfg            = [];
    cfg.frequency  = foi_contrast;
    cfg.avgoverrpt = 'yes';
    cfg.parameter  = {'powspctrm','powspctrm_b'};
    base_sedation_avg = ft_selectdata(cfg,base_sedation);
    mild_sedation_avg = ft_selectdata(cfg,mild_sedation);
    mode_sedation_avg = ft_selectdata(cfg,mode_sedation);
    reco_sedation_avg = ft_selectdata(cfg,reco_sedation);

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
    figure;ft_multiplotER(cfg,base_sedation_avg,mild_sedation_avg,mode_sedation_avg,reco_sedation_avg);

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig6_manova.png" width="600" %}

## 4. Compute a **2x2 interaction**

A very important contrast is the interaction. In this dataset we will
compute the interaction using the within-participant factor SEDATION
(baseline vs moderate) and the between-subject factor GROUP (responsive vs drowsy)
Based on this **["FAQ: how can I test an interaction effect using cluster-based permutation tests"](/faq/how_can_i_test_an_interaction_effect_using_cluster-based_permutation_tests)**

Let us prepare the data
-   1. Compute the within-participant contrast for each group: baseline vs moderate
-   2. Compute the between-participant contrast of the differences computed in step 1

The complexity here is that we are dealing with a between-within
participants design but the design matrix and statistical pipeline is the
one we used in between-participant contrast

    cfg = [];
    cfg.parameter = {'powspctrm','powspctrm_b'};
    cfg.operation = 'subtract';

ROI contrast in RESPONSIVE group

    sedation_respon_d = ft_math(cfg,base_sedation_respon,mode_sedation_respon);
    sedation_drowsy_d = ft_math(cfg,base_sedation_drowsy,mode_sedation_drowsy);

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

Now select the significant sensors and frequencies and plot the interaction
get the 1st positive and negative cluster

    signegmask = (stat4.negclusterslabelmat==1) & stat4.mask;

pool all channels and frequencies that in the cluster

    chanoineg = match_str(stat4.label,stat4.label(sum(signegmask,2) > 0));
    foilimneg = stat4.freq(sum(signegmask,1) > 0);
    foilim = [min(foilimneg) max(foilimneg)];

choose the cluster you want to see

    base_sedation_avg.mask = signegmask;
    mode_sedation_avg.mask = signegmask;

choose the cluster you want to see: POSITIVE or NEGATIVE

    base_sedation_avg.mask = signegmask;
    mode_sedation_avg.mask = signegmask;

    cfg = [];
    cfg.frequency   = foilim;
    cfg.avgoverfreq = 'yes';
    cfg.channel     = chanoineg;
    cfg.avgoverchan = 'yes';
    cfg.parameter   = {'powspctrm','powspctrm_b'};
    b_r = ft_selectdata(cfg,base_sedation_respon);
    m_r = ft_selectdata(cfg,mode_sedation_respon);
    b_d = ft_selectdata(cfg,base_sedation_drowsy);
    m_d = ft_selectdata(cfg,mode_sedation_drowsy);

compute confidence intervals

    parameter = 'powspctrm_b';%make sure this 'parameter' is the same as the one you used in cfg.parameter in ft_freqstatistics

compute means

    x_b_r = mean(b_r.(parameter),1);
    x_m_r = mean(m_r.(parameter),1);
    x_b_d = mean(b_d.(parameter),1);
    x_m_d = mean(m_d.(parameter),1);

    sem_b_r = sem(b_r.(parameter),1);
    sem_m_r = sem(m_r.(parameter),1);
    sem_b_d = sem(b_d.(parameter),1);
    sem_m_d = sem(m_d.(parameter),1);

    figure('position',[517   246   446   420]);
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

## 5. Compute a **correlation** between a variable and the EEG spectrum

Here we will test for correlations between EEG data and quantitative
variables, the drug dosage

A common perspective on the statistical testing starts from the
distinction between dependent and independent variables. When analysing
neurobiological signals, these are typically considered to be the
dependent variable. In these studies, the independent variable can be the
experimental conditions, as defined by task instructions, stimulus type,
learning history, etc. The label *independent variable* suggests that it
must be under the experimenter's control. However, this is not
necessarily the case, and this is exemplified by response accuracy, which
may very well serve as the independent variable in a study in which the
relation is investigated between behaviour (actually, one aspect of it,
drug dosage) and neural activity. Because neither of these variables
(dosage and neural activity) is under experimental control, it is
arbitrary how the roles of dependent and independent variable are
assigned. In FieldTrip, we use the convention that the variable with the
smallest dimensionality is assigned the role of independent variable. For
our example, this implies that accuracy is assigned the role of
independent and the neurobiological signal the role of dependent
variable. In fact, accuracy is represented by a single number, whereas
the neurobiological signal often has a spatial (the channels) and a
spectral (the frequencies) dimension. More information can be found in
this **[FAQ: how can I test for correlations between neuronal data and quantitative stimulus and behavioural variables](/faq/how_can_i_test_for_correlations_between_neuronal_data_and_quantitative_stimulus_and_behavioural_variables)**

### The Permutation Distribution Results From Breaking the Association Between Dependent and Independent Variable

The null hypothesis that is tested by a permutation test involves that
the probability distribution of the dependent variable is identical for
all possible values of the independent variable. Quantitative independent
variables, such us drug dosage, may have an infinite number of values, and in this case it is
more difficult to conceptualise the probability distributions within each
of these values. However, there is a null hypothesis for quantitative
independent variables: **statistical independence** between the dependent
and the independent variable. Testing for this statistical independence
is possible in the same way for categorical as for quantitative
independent variables: breaking the association between dependent and
independent variable by randomly permuting the values of the independent
variable. In a between-UO design, these values are permuted across the
UOs, and in a within-UO design, they are permuted across the conditions
in which the UO has been observed.

It is important to point out that the hypothesis of statistical
independence rules out *all possible* relations between the dependent and
a quantitative independent variable, and not only the linear relation.
This contrasts with the three test statistics for quantitative
independent variables that are implemented in FieldTrip: these are only
sensitive to deviations from statistical independence that can be
captured as a **linear** relation between the dependent and the
independent variable. Of course, new test statistics can be formulated
(and implemented as statfuns) with a sensitivity profile that is
optimised for particular non-linear deviations from statistical
independence.

### Statistical Testing of the Relation Between a Neurobiological and a Behavioural Variable

Now, it is time to prepare the data as follows:

   1. Compute the within-participant contrast for each group: baseline vs moderate
   2. Compute the between-participant contrast of the differences computed in step 1


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

    {'drug concentration' 'reaction time' 'correct responses'};
    design(1,:)  = covariates(:,3,1)./1000;
    cfg.design   = design;
    cfg.ivar     = 1;

    stat5 = ft_freqstatistics(cfg,mode_sedation);

    cfg            = [];
    cfg.alpha      = stat5.cfg.alpha;
    cfg.parameter  = 'stat';
    cfg.zlim       = [-3 3];
    cfg.elec       = elec;
    ft_clusterplot(cfg,stat5);

{% include image src="/assets/img/workshop/madrid2019/tutorial_stats/fig8_corr.png" width="800" %}
