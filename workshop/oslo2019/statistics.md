---
title: Statistical analysis and multiple comparison correction for EEG data
tags: [oslo2019, eeg-audodd, statistics]
---

# Statistical analysis and multiple comparison correction for EEG data (WORK IN PROGRESS)

## Introduction

The objective of this tutorial is to give an introduction to the statistical analysis of EEG data using different methods to control for the false alarm rate. The tutorial starts with sketching
the background of cluster-based permutation tests. Subsequently it is shown how to use FieldTrip to perform statistical analysis (including cluster-based permutation tests) on the time-frequency response to a movement, and to the auditory mismatch negativity. The tutorial makes use of a between-trials (within-subject) design.

In this tutorial we will continue working on the dataset described in the [Preprocessing and event-related activity](/workshop/oslo2019/introduction) and the [Time-frequency analysis of MEG and EEG](/workshop/natmeg/timefrequency) tutorials. We will repeat some code here to select the trials and preprocess the data. We assume that the preprocessing and the computation of the ERFs/TFRs are already clear to the reader.

This tutorial is not covering group analysis. If you are interested in that, you can read the other tutorials that cover cluster-based permutation tests on [event related fields](/tutorial/cluster_permutation_timelock) and on [time-frequency data](/tutorial/cluster_permutation_freq). If you are interested in a more gentle introduction as to how parametric statistical tests can be used with FieldTrip, you can read the [Parametric and non-parametric statistics on event-related fields](/tutorial/eventrelatedstatistics) tutorial.

{% include markup/info %}
This tutorial contains the hands-on material of the [NatMEG workshop](/workshop/natmeg). The background is explained in this lecture, which was recorded at the [Aston MEG-UK workshop](/workshop/birmingham).

{% include youtube id="vOSfabsDUNg" %}
{% include markup/end %}

## Background

The topic of this tutorial is the statistical analysis of multi-channel EEG data. In cognitive experiments, the data is usually collected in different experimental conditions, and the experimenter wants to know whether there is a difference in the data observed in these conditions. In statistics, a result (for example, a difference among conditions) is statistically significant if it is unlikely given the null hypothesis that there is no difference between the conditions. The "unlikeliness" is evaluated according to a predetermined threshold probability, the alpha level.

An important feature of EEG data is that it has spatio-temporal structure, i.e. the data is sampled at multiple time-points and sensors. The nature of the data influences which kind of statistics is the most suitable for comparing conditions. If the experimenter is interested in a difference in the signal at a certain time-point and sensor, then the more widely used parametric tests are sufficient. If it is not possible to predict where the differences are, then many statistical comparisons are necessary which lead to the _multiple comparisons problem_ (MCP). The MCP arises from the fact that the effect of interest (i.e., a difference between experimental conditions) is evaluated at an extremely large number of (channel,time)-pairs. This number is usually in the order of several thousands. Now, the MCP involves that, due to the large number of statistical comparisons (one per (channel,time)-pair), it is not possible to control the so called _family-wise error rate_ (FWER) by means of the standard statistical procedures that operate at the level of single (channel,time)-pairs. The FWER is the probability, under the hypothesis of no effect, of falsely concluding that there is a difference between the experimental conditions at one or more (channel,time)-pairs. A solution of the MCP requires a procedure that controls the FWER at some critical alpha-level (typically, 0.05 or 0.01). The FWER is also called the _false alarm rate_.

When parametric statistics are used, one method that addresses this problem is the so-called Bonferroni correction. The idea is if the experimenter is conducting _n_ number of statistical tests then each of the individual tests should be tested under a significance level that is divided by _n_. The Bonferroni correction was derived from the observation that if _n_ tests are performed with an _alpha_ significance level then the probability that one test comes out significant is smaller than or equal to _n_ times _alpha_ (Boole's inequality). In order to keep this probability lower, we can use an _alpha_ that is divided by _n_ for each test. However, the correction comes at the cost of increasing the probability of false negatives, i.e. the test does not have enough power to reveal differences among conditions.

In constrast to the familiar parametric statistical framework, it is straightforward to solve the MCP in the nonparametric framework. Nonparametric tests offer more freedom to the experimenter regarding which test statistics are used for comparing conditions, and help to maximize the sensitivity to the expected effect. For more details see the publication by [Maris and Oostenveld (2007)](/references_to_implemented_methods#statistical_inference_by_means_of_permutation).

## Load the ERP data and preprocess

    load cleaned_data_ERP.mat
    load ERP_deviant.mat
    load ERP_standard.mat
    load difference_wave.mat
    load elec.mat

First, we load the data that we created in the [ERP tutorial](workshop/oslo2019/introduction)

{% include markup/info %}
Note the naming convention used - each saved _.mat-file_ contains _one and only one_ variable, which has the _same_ name as the _.mat-file_  
This makes it clear what variables are loaded into the workspace
{% include markup/end %}

We then apply the same preprocessing as before

    cfg                = [];
    cfg.lpfilter       = 'yes';
    cfg.lpfreq         = 30;
    cfg.demean         = 'yes'; % we demean (baseline correct) ...
    cfg.detrend        = 'yes'; % removing linear trends
    cfg.baselinewindow = [-Inf 0];% using the mean activity in this window

    data_EEG_filt = ft_preprocessing(cfg, cleaned_data_ERP);

## The Student's t-test

A ubiquitous test used to assess statistical significance is the Student's t-test [Wikipedia entry](https://en.wikipedia.org/wiki/Student's_t-test) [original article](https://doi.org/10.1093/biomet/6.1.1)  
To perform the t-test, _t-values_ need to be calculated, which a bit simplified are: \frac{µ}{SEM}, where µ is the mean difference between the conditions and SEM is the standard devation divided by \sqrt{n}, where _n_ is the number of observations.

We will do a within-subject between-trials statistical test  
We proceed by computing the statistical tets, which returns the t-value, the probability and a binary mask that contains a 0 for all data points where the probability is below the a-priori threshold, and 1 where it is above the threshold. The _cfg.design_ field specifies the condition in which each of the trials is observed. For the _indepsamplesT_ statistic, it should contain 1’s and 2’s.

    cfg           = [];

    cfg.method    = 'analytic'; % using a paarmetric test
    cfg.statistic = 'ft_statfun_indepsamplesT'; % using independent samples
    cfg.correctm  = 'no'; % no multiple comparisons correction
    cfg.alpha     = 0.05;

    cfg.design    = data_EEG_filt.trialinfo; % indicating which trials belong ...
                                             % to what category
    cfg.ivar      = 1; % indicating that the independent variable is found in ...
                       % first row of cfg.design

    stat_t = ft_timelockstatistics(cfg, data_EEG_filt);

_stat\_t_ contains:

    stat_t =

           stat: [128x200 double]
             df: 572
        critval: [-1.9641 1.9641]
           prob: [128x200 double]
           mask: [128x200 logical]
         dimord: 'chan_time'
           elec: [1x1 struct]
          label: {128x1 cell}
           time: [1x200 double]
            cfg: [1x1 struct]

- _stat_    contains the _t-values_ at all channels and time points
- _df_      is the degrees of freedom determining the _t-distribution_ that the _t-value_ is compared against to obtain the _p-values_
- _critval_ contains the critical values for the test performed; if a _t-value_ is lesser than the negative value or greater than the positive value, the difference is declared significant. The _critval_ is dependent on _cfg.alpha_ and the degrees of freedom (_df_)
- _prob_    contains the _p-values_ assciated with the _t-values_ given the degrees of freedom (_df_)
- _mask_    is a _logical_ matrix, 0's are where _p-values_ (_prob_) are greater than _cfg.alpha_, 1's are where they are lesser than _cfg.alpha_
- _dimord_  indicates the ordering of dimensions, rows are channels and columns are time
- _elec_    contains information about the electrodes, e.g. positions and names
- _label_   contains the names of all channels
- _time_    is a row vector with the time points in seconds
- _cfg_     shows the cfg that gave rise to this structure

We can now plot the ERPs using the field _cfg.maskparameter_ of the plotting functions: **[ft_multiplotER](/reference/ft_multiplotER)**, **[ft_singleplotER](/reference/ft_singleplotER)** and **[ft_topoplotER](/reference/ft_topoplotER)**

Here, we will show **[ft_singleplotER](/reference/ft_singleplotER)**

    ERP_standard.mask = stat_t.mask; % adding mask to ERP

    figure

    cfg               = [];
    cfg.layout        = 'natmeg_customized_eeg1005.lay';
    cfg.maskparameter = 'mask';
    cfg.maskstyle     = 'box';
    cfg.maskfacealpha = 0.5; % transparency of mask
    cfg.channel       = 'EEG124';
    cfg.ylim          = [-5e-6 5e-6]; % Volts

    ft_singleplotER(cfg, ERP_standard, ERP_deviant);
    hold on
    xlabel('Time (s)')
    ylabel('Electric Potential (V)')
    plot([ERP_standard.time(1), ERP_standard.time(end)], [0 0], 'k--') % hor. line
    plot([0 0], cfg.ylim, 'k--') % vert. l
    axes = gca;
    legend(axes.Children([10 3]), {'Standard', 'Deviant'})

    print -dpng singleplot_t_uncorrected.png

{% include image src="/assets/img/workshop/oslo2019/singleplot_t_uncorrected.png" width="650" %}
_Figure 1: Single channel plot - no correction_

{% include markup/info %}
Note that we see the MMN difference (~120-200 ms), but we also see other differences and even a pre-zero one. We cannot decide which are _true positives_ and which are _false positives_. In fact, we know that there will be a lot _false positives_ (assuming that the data were from identical distributions, i.e. the null hypothesis is true, we would expect that 5% of our significant differences are _false positives_)
{% include markup/end %}

## Bonferroni correction

We will now control the _false positives_ by using the Bonferroni Correction [Wikipedia article](https://en.wikipedia.org/wiki/Bonferroni_correction)

    cfg           = [];

    cfg.method    = 'analytic'; % using a parametric test
    cfg.statistic = 'ft_statfun_indepsamplesT'; % using independent samples
    cfg.correctm  = 'bonferroni'; % correction method
    cfg.alpha     = 0.05;

    cfg.design    = data_EEG_filt.trialinfo; % indicating which trials belong ...
                                             % to what category
    cfg.ivar      = 1; % indicating that the independent variable is found in ...
                       % first row of cfg.design

    stat_t_bonferroni = ft_timelockstatistics(cfg, data_EEG_filt);

{% include image src="/assets/img/workshop/oslo2019/singleplot_t_bonferroni.png" width="650" %}
_Figure 2: Single channel plot - Bonferroni correction_

{% include markup/info %}
The Bonferroni correction has eliminated some likely _false positives_, but probably at the expense of introducing some _false negatives_. According to our image, only the peak of our MMN is significant. But EEG responses are not peaky in nature, they wax and wane smoothly in time and are smeared out over several electrodes. The Bonferroni correction implicitly assumes that EEG responses are uncorrelated, which they are patently not. Our next correction, the _cluster correction_ addresses the issue of correlation.
{% include markup/end %}


## Cluster correction

As noted above, EEG data is smooth over the spatio-temporal dimensions. We can easily imaging how we can build clusters in the temporal dimension. These are simply data points that are neighboring each other in time. For the spatial dimension, it is necessary to build a neighbor structure using **[ft_prepare_neighbours](/reference/ft_prepare_neighbours)**. This uses the (digitized) positions of the electrodes.

### Neighbors

    cleaned_data_ERP.elec = elec; % add the elec structure

    cfg          = [];
    cfg.method   = 'triangulation';
    cfg.feedback = 'yes'; % visualizes the neighbors

    neighbors = ft_prepare_neighbours(cfg, cleaned_data_ERP);

    print -dpng neighbor_structure.png

{% include image src="/assets/img/workshop/oslo2019/neighbour_structure.png" width="650" %}
_Figure 3: Single channel plot - Electrode neighbor structure_

### Permutation

The cluster correction is not meaningful for parametric statistics, e.g. _t-tests_, therefore we are going to use a non-parameteric test.  
We will first run it and then discuss some of the options and details afterwards.

    cfg                  = [];
    cfg.method           = 'montecarlo'; % use montecarlo to permute the data
    cfg.statistic        = 'ft_statfun_indepsamplesT'; % function to use when ...
                                                       % calculating the ...
                                                       % parametric t-values

    cfg.correctm         = 'cluster'; % the correction to use
    cfg.clusteralpha     = 0.05; % the alpha level used to determine whether or ...
                                 % not a channel/time pair can be included in a ...
                                 % cluster
    cfg.alpha            = 0.025; % corresponds to an alpha level of 0.05, since ...
                                  % two tests are made ...
                                  % (negative and positive: 2*0.025=0.05)
    cfg.numrandomization = 100;  % number of permutations run

    cfg.design           = data_EEG_filt.trialinfo; % same design as before
    cfg.ivar             = 1; % indicating that the independent variable is found in ...
                              % first row of cfg.design
    cfg.neighbours       = neighbors; % the spatial structire
    cfg.minnbchan        = 2; % minimum number of channels required to form a cluster

    stat_t_cluster = ft_timelockstatistics(cfg, data_EEG_filt);

The output of _stat\_t\_cluster_ is:

    stat_t_cluster =

                       prob: [128x200 double]
                posclusters: [1x11 struct]
        posclusterslabelmat: [128x200 double]
            posdistribution: [1x100 double]
                negclusters: [1x14 struct]
        negclusterslabelmat: [128x200 double]
            negdistribution: [1x100 double]
                    cirange: [128x200 double]
                       mask: [128x200 logical]
                       stat: [128x200 double]
                        ref: [128x200 double]
                     dimord: 'chan_time'
                      label: {128x1 cell}
                       time: [1x200 double]
                        cfg: [1x1 struct]

- _prob_                contains the _p-values_ for each channel/time pair inhterited from the cluster that pair is part of
- _posclusters_         contains a structure for each positive cluster found that contains
    - _prob_               contains the _p-value_ associated with the cluster
    - _clusterstat_        contains the _T-value_ associated with this cluster
    - _stddev_             contains the standard deviation of the _prob_ of this cluster
    - _cirange_            contains the 95% confidence interval for the _prob_ of thus cluster - if this range include _cfg.alpha_ a warning is issued recommending increasing the number of permutations
- _posclusterslabelmat_ contains a matrix with a number indicating which positive cluster each channel/time pair belongs (0 if is doens't belong to any)
- _posdistribution_     contains a row vector containing the _T-value_ for each of the permutations
- _negclusters_         contains the negative equivalent of _posclusters_
- _negclusterslabelmat_ contains the negative equivalent of _negclusterslabelmat_
- _negdistribution_     contains the negative equivalent of _posdistribution_
- _cirange_             contains the 95% confidence interval for the _prob_
- _mask_                is a _logical_ matrix, 0's are where _p-values_ (_prob_) are greater than _cfg.alpha_, 1's are where they are lesser than _cfg.alpha_
- _stat_                contains the _t-values_ (the first step)
- _ref_                 contains the mean value of the _t-value_ over all of the permutations
- _dimord_              indicates the ordering of dimensions, rows are channels and columns are time
- _label_               contains the names of all channels
- _time_                is a row vector with the time points in seconds
- _cfg_                 shows the cfg that gave rise to this structure

There's quite a lot to unpack here. It is critical to distinguish between _t-values_ and _T-values_ here. We will now state the procedure step by step


1. Do a _t-test_ similar to above (_stat\_t_) - these provide the _t-values_ in _stat\_t\_cluster.stat_
{% include markup/exercise %}
See for yourself that _stat\_t.stat_ and _stat\_t\_cluster.stat_ are identical (use e.g. _isequal_ or _plot)
{% include markup/end %}

2. Find the _T-values_ for each cluster of _t-values_ that pass the analytic significance test based on _cfg.clusteralpha_. The _T-value_ for a cluster is the sum of all the _t-values_ in that cluster
3. Permute the condition labels (_cfg.design_) as many times as set in _cfg.numrandomization_; then compute the _t-values_ (as in step 1 above), and compute the _T-values_ for each of the clusters that pass the analytic significance test based on _cfg.clusteralpha_ (as in step 2 above).
4. For each of the _cfg.numrandomization_ permutations, retrieve the maximum _T-value_, and create a permutation based distribution of _T-values_
5. Observe the likelihood of the maximum _T-value_ under the permuted distribution for the _positive clusters_ direction and evaluate at _cfg.alpha_
6. Repeat step 5 for the _negative clusters_

Below follows some figures and operations illustrating key features of these steps

#### Equivalence of the _t-values_ (step 1)

    >> isequal(stat_t.stat, stat_t_cluster.stat)

    ans =

         1

{% include image src="/assets/img/workshop/oslo2019/stat_equivalence.png" width="650" %}
_Figure 4: Equivalence of_ t-values

#### Cluster _T-values_ (step 2)

{% include image src="/assets/img/workshop/oslo2019/cluster_T_values.png" width="650" %}
_Figure 5: The_ T-values _of each of the clusters_

#### Maximum positive and negative cluster _T-values_ compared to the permuted distributions (steps 3 and 4)

{% include image src="/assets/img/workshop/oslo2019/permutation_distributions.png" width="650" %}
_Figure 6: The observed positive and negative_ T-values compared to the permuted distributions

#### Compare against _cfg.alpha_ (steps 5 and 6)

Since both the _positive_ and _negative p-values_ are lesser than _cfg.alpha_ (0.025), we reject the null hypothesis for both the positive and negative directions.  
Put informally_: **our way of labeling the conditions _does_ matter**

Let's have a look at the cluster corrected channel:

**WORK IN PROGRESS**
