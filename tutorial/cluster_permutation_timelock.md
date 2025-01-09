---
title: Cluster-based permutation tests on event-related fields
parent: Statistical analysis
category: tutorial
tags: [statistics, eeg, meg, timelock, plotting, meg-language, neighbours]
---

# Cluster-based permutation tests on event-related fields

## Introduction

The objective of this tutorial is to give an introduction to the statistical analysis of event-related EEG and MEG data (denoted as M/EEG data in the following) by means of cluster-based permutation tests. The tutorial starts with a long background section that sketches the background of permutation tests. Subsequently it is shown how to use FieldTrip to perform cluster-based permutation tests on actual axial and planar event-related fields in a between-trials (using single-subject data) and in a within-subjects design (using data from multiple subjects).

In this tutorial we will continue working on the [dataset](/tutorial/meg_language) of a single subject described in previous tutorials. Below we will repeat some code to select the trials and preprocess the data as described in the earlier tutorials on [Preprocessing - Segmenting and reading trial-based EEG and MEG data](/tutorial/preprocessing), [artifact rejection](/tutorial/artifacts), and [Event-related averaging and MEG planar gradient](/tutorial/eventrelatedaveraging). We assume that the preprocessing and averaging steps of the analysis are already clear for the reader.

This tutorial is not covering statistical test on time-frequency representations. If you are interested in that, you can read the [Cluster-based permutation tests on time-frequency data](/tutorial/cluster_permutation_freq) tutorial. If you are interested how parametric statistical tests can be used with FieldTrip, you can read the [Parametric and non-parametric statistics on event-related fields](/tutorial/eventrelatedstatistics) tutorial.

{% include markup/skyblue %}
This tutorial contains hands-on material that we use for the [MEG/EEG toolkit course](/workshop/toolkit2015) and it is complemented by this lecture.

{% include youtube id="x0hR-VsHZj8" %}
{% include markup/end %}

## Background

{% include /shared/tutorial/cluster_permutation_background.md %}

## Procedure

In this tutorial we will consider a **between-trials** experiment, in which we analyse the data of a single subject. The statistical analysis for this experiment we perform both on _axial_ and _planar_ ERFs. The steps we perform are as follow

- Preprocessing and time-locked analysis with the **[ft_definetrial](/reference/ft_definetrial)**, **[ft_preprocessing](/reference/ft_preprocessing)** and **[ft_timelockanalysis](/reference/ft_timelockanalysis)** functions
- (Calculation of the planar gradient with the **[ft_megplanar](/reference/ft_megplanar)** and **[ft_combineplanar](/reference/ft_combineplanar)** functions)
- Permutation test with the **[ft_timelockstatistics](/reference/ft_timelockstatistics)** function
- Plotting the result with the **[ft_topoplotER](/reference/ft_topoplotER)** function

{% include image src="/assets/img/tutorial/cluster_permutation_timelock/figure1.png" width="300" %}

_Figure 1. Analysis protocol of a between-trials experiment with axial data_

{% include image src="/assets/img/tutorial/cluster_permutation_timelock/figure2.png" width="300" %}

_Figure 2. Analysis protocol of a between-trials experiment with planar data_

Subsequently, we consider a **within-subjects** experiment, in which we compare differences between (planar gradient) ERFs over all subjects. The steps we perform are as follow

- Preprocessing and time-locked analysis with **[ft_definetrial](/reference/ft_definetrial)**, **[ft_preprocessing](/reference/ft_preprocessing)** and **[ft_timelockanalysis](/reference/ft_timelockanalysis)** functions
- Calculation of the planar gradient with the **[ft_megplanar](/reference/ft_megplanar)** and **[ft_combineplanar](/reference/ft_combineplanar)** functions
- Make grandaverage with the **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)** function
- Permutation test with the **[ft_timelockstatistics](/reference/ft_timelockstatistics)** function
- Plotting the result with the **[ft_topoplotER](/reference/ft_topoplotER)** function

{% include image src="/assets/img/tutorial/cluster_permutation_timelock/figure3.png" width="600" %}

_Figure 3. Analysis protocol of a within-subjects experiment with planar data_

## Between-trials experiments

In a between-trials experiment, we analyze the data of a single subject. By means of a statistical test, we want to answer the question whether there is a systematic difference in the MEG recorded on trials with a fully congruent and trials with a fully incongruent sentence ending. (This comparison is the MEG-version of the classical comparison that showed the N400-component in EEG-data).

### Preprocessing and time-locked analysis

### Reading in the data

We will now read and preprocess the data. If you would like to continue directly with the already preprocessed data, you can download it from [dataFIC_LP.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock/dataFIC_LP.mat) and [dataFC_LP.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock/dataFC_LP.mat). Load the data into MATLAB with the command `load` and skip to [Permutation test](#permutation-test).

Otherwise run the following code:

{% include /shared/tutorial/definetrial_all.md %}

### Cleaning

{% include /shared/tutorial/preprocessing_lp.md %}

For subsequent analysis we split the data into two different data structures, the fully incongruent condition FIC and the fully congruent condition FC.

    cfg = [];
    cfg.trials = data_all.trialinfo == 3;
    dataFIC_LP = ft_redefinetrial(cfg, data_all);

    cfg = [];
    cfg.trials = data_all.trialinfo == 9;
    dataFC_LP = ft_redefinetrial(cfg, data_all);

Subsequently you can save the data to disk.

      save dataFIC_LP dataFIC_LP
      save dataFC_LP dataFC_LP

Using the preprocessed data, we now create a data structure that is the average across trials, time-locked to a particular event, using **[ft_timelockanalysis](/reference/ft_timelockanalysis)**. The output of **[ft_timelockanalysis](/reference/ft_timelockanalysis)** contains an .avg field with the average event-related field, and a .trial field with the individual trial data. The output is stored in timelockFIC and timelockFC for the fully incongruent and the fully congruent condition. This output is then suitable, as well, for statistical analyses.

To obtain the preprocessed data required by **[ft_timelockanalysis](/reference/ft_timelockanalysis)** you can get it here from our download server: [dataFIC_LP](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock/dataFIC_LP.mat) and [dataFC_LP.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock/dataFC_LP.mat).

    load dataFIC_LP
    load dataFC_LP

    cfg = [];
    cfg.keeptrials = 'yes';
    timelockFIC    = ft_timelockanalysis(cfg, dataFIC_LP);
    timelockFC     = ft_timelockanalysis(cfg, dataFC_LP);

### Permutation test

Cluster-level permutation tests for event-related fields are performed by the function **[ft_timelockstatistics](/reference/ft_timelockstatistics)**. This function takes as its input arguments a configuration structure `cfg` and two or more data structures. These data structures must be produced by **[ft_timelockanalysis](/reference/ft_timelockanalysis)** or **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)**, which all operate on preprocessed data. The argument list of **[ft_timelockstatistics](/reference/ft_timelockstatistics)** must contain one data structure for every experimental condition. 

#### The configuration settings

Some fields of the configuration (cfg), such as channel and latency, are not specific for **[ft_timelockstatistics](/reference/ft_timelockstatistics)**; their role is similar in other FieldTrip functions. We first concentrate on the fields that are specific for **[ft_timelockstatistics](/reference/ft_timelockstatistics)**.

    cfg                  = [];
    cfg.method           = 'montecarlo'; % use the Monte Carlo Method to calculate the significance probability
    cfg.statistic        = 'indepsamplesT'; % use the independent samples T-statistic as a measure to
                                       % evaluate the effect at the sample level
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;       % alpha level of the sample-specific test statistic that
                                       % will be used for thresholding
    cfg.clusterstatistic = 'maxsum';   % test statistic that will be evaluated under the
                                       % permutation distribution.
    cfg.minnbchan        = 2;          % minimum number of neighborhood channels that is
                                       % required for a selected sample to be included
                                       % in the clustering algorithm (default=0).
    % cfg.neighbours     = neighbours; % see below
    cfg.tail             = 0;          % -1, 1 or 0 (default = 0); one-sided or two-sided test
    cfg.clustertail      = 0;
    cfg.alpha            = 0.025;      % alpha level of the permutation test
    cfg.numrandomization = 100;        % number of draws from the permutation distribution

    n_fc  = size(timelockFC.trial, 1);
    n_fic = size(timelockFIC.trial, 1);

    cfg.design           = [ones(1,n_fic), ones(1,n_fc)*2]; % design matrix
    cfg.ivar             = 1; % number or list with indices indicating the independent variable(s)

We now describe these options one-by-one.

- With **cfg.method** = 'montecarlo' we choose the Monte Carlo method for calculating the significance probability. This significance probability is a Monte Carlo estimate of the p-value under the permutation distribution.

- With **cfg.statistic** = 'indepsamplesT', we choose the independent samples T-statistic to evaluate the effect (the difference between the fully congruent and the fully incongruent condition) at the sample level. In cfg.statistic, many other test statistics can be specified. Which test statistic is appropriate depends on your research question and your experimental design. For instance, in a within-UO design, one must use the dependent samples T-statistic ('ft_statfun_depsamplesT'). And if you want to compare more than two experimental conditions, you should choose an F-statistic ('ft_statfun_indepsamplesF' or 'ft_statfun_depsamplesFmultivariate'). The 'ft_statfun' can be omitted in the specification of cfg.statistic, FieldTrip will look for functions on the MATLAB that are named 'ft_statfun_<cfg.statistic>' automatically, but it's also OK to specify the full filename, i.e. 'ft_statfun_indepsamplesT'. Also, you can write your own 'statfun' with another test-statistic that you deem relevant.

- We use **cfg.clusteralpha** to choose the critical value that will be used for thresholding the sample-specific T-statistics. With cfg.clusteralpha = 0.05, every sample-specific T-statistic is compared with the critical value of the univariate T-test with a critical alpha-level of 0.05. (This statistical test would have been the most appropriate test if we had observed a single channel at a single time-point.) The value of cfg.clusteralpha does not affect the false alarm rate of the statistical test at the cluster-level. It is a rational threshold for deciding whether a sample should be considered a member of some large cluster of samples (which may or may not be significant at the cluster-level).

- We use **cfg.clusterstatistic** to choose the test statistic that will be evaluated under the permutation distribution. This is the actual test statistic and it must be distinguished from the sample-specific T-statistics that are used for thresholding. With cfg.clusterstatistic = 'maxsum', the actual test statistic is the maximum of the cluster-level statistics. A cluster-level statistic is equal to the sum of the sample-specific T-statistics that belong to this cluster. Taking the largest of these cluster-level statistics of the different clusters produces the actual test statistic.

- The value of **cfg.minnbchan** is a tuning parameter that determines the way the clusters are formed. More specifically, we use cfg.minnbchan to specify the minimum number of neighbourhood channels that is required for a selected sample (i.e., a sample who's T-value exceeds the threshold) to be included in the clustering algorithm. With cfg.minnbchan = 0 (the default), it sometimes happens that two clusters are spatially connected via a narrow bridge of samples. Because they are connected, these two clusters are considered as a single cluster. If clusters are interpreted as reflecting spatially distinct sources, such a combined cluster does not make much sense. To suppress this type of combined clusters, one can choose to ignore all selected samples (on the basis of their T-values) if they have less than some minimum number of neighbors that were also selected. This minimum number is assigned to cfg.minnbchan. This number must be chosen independently of the data.

- **cfg.neighbours** is a structure that you need to have previously created using [ft_prepare_neighbours](/reference/ft_prepare_neighbours).

- We use **cfg.tail** to choose between a one-sided and a two-sided statistical test. Choosing cfg.tail = 0 affects the calculations in three ways. First, the sample-specific T-values are thresholded from below as well as from above. This implies that both large negative and large positive T-statistics are selected for later clustering. Second, clustering is performed separately for thresholded positive and thresholded negative T-statistics. And third, the critical value for the cluster-level test statistic (determined by cfg.alpha; see further) is now two-sided: negative cluster-level statistics must be compared with the negative critical value, and positive cluster-level statistics must be compared with the positive critical value.

- We use **cfg.alpha** to control the false alarm rate of the permutation test (the probability of falsely rejecting the null hypothesis). The value of cfg.alpha determines the critical values with which we must compare the test statistic (i.e., the maximum and the minimum cluster-level statistic). _Note that if you want to run a two-sided test, you have to split the critical alpha value by setting cfg.correcttail = 'alpha'; i.e. this sets cfg.alpha = 0.025, corresponding to a false alarm rate of 0.05 in a two-sided test._ The field cfg.alpha is not crucial. This is because the output of **[ft_timelockstatistics](/reference/ft_timelockstatistics)** (see further) contains a p-value for every cluster (calculated under the permutation distribution of the maximum/minimum cluster-level statistic). Instead of the critical values, we can also use these p-values to determine the significance of the clusters.

- We use **cfg.numrandomization** to control the number of draws from the permutation distribution. Remember that **[ft_timelockstatistics](/reference/ft_timelockstatistics)** approximates the permutation distribution by means of a histogram. This histogram is a so-called Monte Carlo approximation of the permutation distribution. This Monte Carlo approximation is used to calculate the p-values and the critical values that are shown in the output of **[ft_timelockstatistics](/reference/ft_timelockstatistics)**. In this tutorial, we use cfg.numrandomization = 100. This number is too small for actual applications. As a rule of thumb, use cfg.numrandomization = 500, and double this number if it turns out that the p-value differs from the critical alpha-level (0.05 or 0.01) by less than 0.02.

- We use **cfg.design** to store information about the UOs. The content of cfg.design must be a matrix. Consider the hypothetical case that your subject has performed 5 trials in the first condition and 4 trials in the second condition. Then the correct design matrix looks like this: cfg.design = [1 1 1 1 1 2 2 2 2].

- We use **cfg.ivar** to indicate the row of the design matrix that contains the independent variable. For a between-trials statistical analysis, the minimum design matrix contains only a single row, and cfg.ivar is superfluous. However, in other statistical analyses (e.g., those for a within-UO design) the design matrix must contain more than one row, and specifying cfg.ivar is essential.

We now briefly discuss the configuration fields that are not specific for **[ft_timelockstatistics](/reference/ft_timelockstatistics)**:

    cfg_neighb        = [];
    cfg_neighb.method = 'distance';
    neighbours        = ft_prepare_neighbours(cfg_neighb, dataFC_LP);

    cfg.neighbours    = neighbours;  % the neighbours specify for each sensor with
                                     % which other sensors it can form clusters
    cfg.channel       = {'MEG'};     % cell-array with selected channel labels
    cfg.latency       = [0 1];       % time interval over which the experimental
                                     % conditions must be compared (in seconds)

With these two options, we select the spatio-temporal dataset involving all MEG channels and the time interval between 0 and 1 second. The two experimental conditions will only be compared on this selection of the complete spatio-temporal dataset. Also, feel free to consult
[our frequently asked questions about ft_prepare_neighbours](/faq/how_can_i_define_neighbouring_sensors)

One should be aware of the fact that the sensitivity of **[ft_timelockstatistics](/reference/ft_timelockstatistics)** (i.e., the probability of detecting an effect) depends on the length of the time interval that is analyzed, as specified in cfg.latency. For instance, assume that the difference between the two experimental conditions extends over a short time interval only (e.g., between 0.3 and 0.4 sec.). If it is known in advance that this short time interval is the only interval where an effect is likely to occur, then one should limit the analysis to this time interval (i.e., choose cfg.latency = [0.3 0.4]). Choosing a time interval on the basis of prior information about the time course of the effect will increase the sensitivity of the statistical test. If there is no prior information, then one must compare the experimental conditions over the complete time interval. This is accomplished by choosing cfg.latency = 'all'. In this tutorial, we choose cfg.latency = [0 1] because EEG-studies have shown that the strongest effect of semantic incongruity is observed in the first second after stimulus presentation.

Now, run **[ft_timelockstatistics](/reference/ft_timelockstatistics)** to compare timelockFIC and timelockFC using the configuration described above.

    [stat] = ft_timelockstatistics(cfg, timelockFIC, timelockFC);

Save the output to disk:

    save stat_ERF_axial_FICvsFC stat;

#### The format of the output

The output can also be obtained from [stat_ERF_axial_FICvsFC.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock/stat_ERF_axial_FICvsFC.mat). If you need to reload the statistics output, use:

    load stat_ERF_axial_FICvsFC

The output of **[ft_timelockstatistics](/reference/ft_timelockstatistics)** has separate fields for positive and negative clusters. For the positive clusters, the output is given in the following pair of fields: stat.posclusters and stat.posclusterslabelmat. The field **stat.posclusters** is an array that provides the following information for every cluster:

- The field **clusterstat** contains the cluster-level test statistic (here: the sum of the T-values in this cluster).

- The field **prob** contains the proportion of draws from the permutation distribution with a maximum cluster-level statistic that is larger than the cluster-level test statistic.
  The elements in the array stat.posclusters are sorted according to these probabilities: the cluster with the smallest p-value comes first, followed by the cluster with the second-smallest, etc. Thus, if the k-th cluster has a p-value that is larger than the critical alpha-level (e.g., 0.025), then so does the (k+1)-th. Type stat.posclusters(k) on the MATLAB command line to see the information for the k-th cluster. Note, however, that in fact for the statistical inferential decision (i.e. reject or not the null hypothesis), only the p-value of the largest cluster is relevant. Therefore, importantly, it is a bit silly to use the terminology 'significant clusters' in this context, by evaluating the cluster-associated p-values.

The field stat.posclusterslabelmat is a spatiotemporal matrix. This matrix contains numbers that identify the clusters to which the (channel,time)-pairs (the samples) belong. For example, all (channel,time)-pairs that belong to the third cluster, are identified by the number 3. As will be shown in the following, this information can be used to visualize the topography of the clusters.

For the negative clusters, the output is given in the following pair of fields: stat.negclusters and stat.negclusterslabelmat. These fields contain the same type of information as stat.posclusters and stat.posclusterslabelmat, but now for the negative clusters.

By inspecting stat.posclusters and stat.negclusters, it can be seen that only the first positive and the first negative cluster have a p-value less than the critical alpha-level of 0.025. This critical alpha-level corresponds to a false alarm rate of 0.05 in a two-sided test. By typing stat.posclusters(1) on the MATLAB command line, you should obtain more or less the following:

    stat.posclusters(1)
    ans =

               prob: 0.0099
        clusterstat: 8.2721e+03
             stddev: 0.0099
            cirange: 0.0194

And by typing stat.negclusters(1), you should obtain more or less the following:

    stat.negclusters(1)
    ans =
              prob: 0.0099
       clusterstat: -1.0251e+04
            stddev: 0.0099
           cirange: 0.0194

It is possible that the p-values in your output are a little bit different from 0. This is because **[ft_timelockstatistics](/reference/ft_timelockstatistics)** calculated as a Monte Carlo approximation of the permutation p-values: the p-value for the k-th positive cluster is calculated as the proportion of random draws from the permutation distribution in which the maximum of the cluster-level statistics is larger than stat.posclusters(k).clusterstat. Also, given the Monte Carlo approximation, the probability values are not exact, and their confidence interval and standard deviation are given by the cirange, and stddev, respectively.

### Plotting of the results

To plot the results of the permutation test, we use the plotting function **[ft_topoplotER](/reference/ft_topoplotER)**. In doing so, we will plot a topography of the difference between the two experimental conditions (FIC and FC). On top of that, and for each timestep of interest, we will highlight the sensors which are members of significant clusters. First, however, we must calculate the difference between conditions using **[ft_math](/reference/ft_math)**.

    cfg    = [];
    avgFIC = ft_timelockanalysis(cfg, dataFIC_LP);
    avgFC  = ft_timelockanalysis(cfg, dataFC_LP);

    % Then take the difference of the averages using ft_math
    cfg           = [];
    cfg.operation = 'subtract';
    cfg.parameter = 'avg';
    raweffectFICvsFC = ft_math(cfg, avgFIC, avgFC);

We then construct a boolean matrix indicating whether a channel/time point belongs to a cluster that we deem interesting to inspect. This matrix has size [Number_of_MEG_channels x Number_of_time_samples], like stat.posclusterslabelmat. We'll make two such matrices: one for positive clusters (named pos), and one for negative (neg). All (channel,time)-pairs belonging to the large clusters whose probability of occurrence is sufficiently low in relation to the associated randomization distribution of clusterstats will be coded in the new boolean matrix as 1, and all those that don't will be coded as 0.

    % Make a vector of all p-values associated with the clusters from ft_timelockstatistics.
    pos_cluster_pvals = [stat.posclusters(:).prob];

    % Then, find which clusters are deemed interesting to visualize, here we use a cutoff criterion based on the
    % cluster-associated p-value, and take a 5% two-sided cutoff (i.e. 0.025 for the positive and negative clusters,
    % respectively
    pos_clust = find(pos_cluster_pvals < 0.025);
    pos       = ismember(stat.posclusterslabelmat, pos_clust);

    % and now for the negative clusters...
    neg_cluster_pvals = [stat.negclusters(:).prob];
    neg_clust         = find(neg_cluster_pvals < 0.025);
    neg               = ismember(stat.negclusterslabelmat, neg_clust);

Alternatively, we can manually select which clusters we want to plot. If we only want to see the extent of the first (i.e. most significant) positive and negative clusters, for instance, we can do so as follows:

    pos = stat.posclusterslabelmat == 1; % or == 2, or 3, etc.
    neg = stat.negclusterslabelmat == 1;

To plot a sequence of twenty topographic plots equally spaced between 0 and 1 second, we define the vector j of time steps. These time intervals correspond to the samples m in stat and in the variables pos. and neg. m and j must, therefore, have the same length.

To be sure that your sample-based time windows align with your time windows in seconds, check the following:

    timestep      = 0.05; % timestep between time windows for each subplot (in seconds)
    sampling_rate = dataFC_LP.fsample; % Data has a temporal resolution of 300 Hz
    sample_count  = length(stat.time);
    % number of temporal samples in the statistics object
    j = [0:timestep:1]; % Temporal endpoints (in seconds) of the ERP average computed in each subplot
    m = [1:timestep*sampling_rate:sample_count]; % temporal endpoints in M/EEG samples

To plot the data use the following for-loop:

    % First ensure the channels to have the same order in the average and in the statistical output.
    % This might not be the case, because ft_math might shuffle the order
    [i1,i2] = match_str(raweffectFICvsFC.label, stat.label);

    for k = 1:20
       subplot(4,5,k);
       cfg = [];
       cfg.xlim = [j(k) j(k+1)];   % time interval of the subplot
       cfg.zlim = [-2.5e-13 2.5e-13];
       % If a channel is in a to-be-plotted cluster, then
       % the element of pos_int with an index equal to that channel
       % number will be set to 1 (otherwise 0).

       % Next, check which channels are in the clusters over the
       % entire time interval of interest.
       pos_int = zeros(numel(raweffectFICvsFC.label),1);
       neg_int = zeros(numel(raweffectFICvsFC.label),1);
       pos_int(i1) = all(pos(i2, m(k):m(k+1)), 2);
       neg_int(i1) = all(neg(i2, m(k):m(k+1)), 2);

       cfg.highlight   = 'on';
       % Get the index of the to-be-highlighted channel
       cfg.highlightchannel = find(pos_int | neg_int);
       cfg.comment     = 'xlim';
       cfg.commentpos  = 'title';
       cfg.layout      = 'CTF151_helmet.mat';
       cfg.interactive = 'no';
       cfg.figure      = 'gca'; % plots in the current axes, here in a subplot
       ft_topoplotER(cfg, raweffectFICvsFC);
    end

In this for-loop, cfg.xlim defines the time interval of each subplot. The variables pos_int and neg_int boolean vectors indicating which channels of pos and neg are significant in the time interval of interest. This is defined in cfg.highlightchannel. The for-loop plots 20 subplots covering a time interval of 50 ms each. Running this for-loop creates the following figure:

{% include image src="/assets/img/tutorial/cluster_permutation_timelock/figure4.png" width="600" %}

_Figure 4: Raw effect (FIC-FC) on the ERFs of subject 1, significant clusters are highlighted.._

### Using planar gradient data

To perform the permutation test using synthetic planar gradient data, the data must first be converted using the functions **[ft_megplanar](/reference/ft_megplanar)** and **[ft_combineplanar](/reference/ft_combineplanar)**. These functions were described in the tutorial on event-related fields. After running these functions, the statistical analysis using **[ft_timelockstatistics ](/reference/ft_timelockstatistics)** involves the same configuration options as for ordinary event-related averages (no synthetic planar gradients). There is only one additional step, which is needed to add the gradiometer structure to one of the planar gradient data sets.

    cfg = [];
    cfg.planarmethod   = 'sincos';
    cfg.neighbours     = neighbours; % also here, neighbouring sensors needs to be defined
    timelockFIC_planar = ft_megplanar(cfg, timelockFIC);
    timelockFC_planar  = ft_megplanar(cfg, timelockFC);

    timelockFIC_planar_cmb = ft_combineplanar(cfg, timelockFIC_planar);
    timelockFC_planar_cmb  = ft_combineplanar(cfg, timelockFC_planar);

    timelockFIC_planar_cmb.grad = timelockFIC.grad;  % add the gradiometer structure
    timelockFC_planar_cmb.grad  = timelockFC.grad;

Having calculated synthetic planar gradient data, one can use the same configuration parameters as used for the analysis of the original data.

    cfg                  = [];
    cfg.channel          = {'MEG'};
    cfg.latency          = [0 1];
    cfg.neighbours       = neighbours;
    cfg.method           = 'montecarlo';
    cfg.statistic        = 'indepsamplesT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = 0;
    cfg.alpha            = 0.025;
    cfg.numrandomization = 100;

    n_fc  = size(timelockFC_planar_cmb.trial, 1);
    n_fic = size(timelockFIC_planar_cmb.trial, 1);

    cfg.design           = [ones(1,n_fic), ones(1,n_fc)*2]; % design matrix
    cfg.ivar             = 1; % number or list with indices indicating the independent variable(s)
    [stat]               = ft_timelockstatistics(cfg, timelockFIC_planar_cmb, timelockFC_planar_cmb)

    save stat_ERF_planar_FICvsFC stat

The output can also be obtained from [here](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock/stat_ERF_planar_FICvsFC.mat). If you need to reload the statistics output, use:

    load stat_ERF_planar_FICvsFC

We now calculate the raw effect in the average with planar gradient data using the following configuration:

    cfg = [];
    cfg.keeptrials = 'no';   % now only the average, not the single trials
    avgFIC_planar  = ft_timelockanalysis(cfg, timelockFIC_planar);
    avgFC_planar   = ft_timelockanalysis(cfg, timelockFC_planar);
    cfg = [];
    avgFIC_planar_cmb = ft_combineplanar(cfg, avgFIC_planar);
    avgFC_planar_cmb  = ft_combineplanar(cfg, avgFC_planar);

    % subtract avgFC from avgFIC
    cfg = [];
    cfg.operation    = 'subtract'
    cfg.parameter    = 'avg';
    raweffectFICvsFC = ft_math(cfg, avgFIC_planar_cmb, avgFC_planar_cmb);

Using the following configuration for **[ft_topoplotER](/reference/ft_topoplotER)** we can plot the raw effect and highlight the channels contributing to the largest cluster

    figure;
    timestep      = 0.05; %(in seconds)
    sampling_rate = dataFC_LP.fsample;
    sample_count  = length(stat.time);
    j = [0:timestep:1]; % Temporal endpoints (in seconds) of the ERP average computed in each subplot
    m = [1:timestep*sampling_rate:sample_count]; % temporal endpoints in M/EEG samples

    pos_cluster_pvals = [stat.posclusters(:).prob];
    pos_clust         = find(pos_cluster_pvals < 0.025);
    pos               = ismember(stat.posclusterslabelmat, pos_clust);

    % Remember to do the same for negative clusters if you want them!

    % First ensure the channels to have the same order in the average and in the statistical output.
    % This might not be the case, because ft_math might shuffle the order
    [i1,i2] = match_str(raweffectFICvsFC.label, stat.label);

    for k = 1:20;
       subplot(4,5,k);
       cfg                  = [];
       cfg.xlim             = [j(k) j(k+1)];
       cfg.zlim             = [-1.0e-13 1.0e-13];
       pos_int              = zeros(numel(raweffectFICvsFC.label),1);
       pos_int(i1)          = all(pos(i2, m(k):m(k+1)), 2);
       cfg.highlight        = 'on';
       cfg.highlightchannel = find(pos_int);
       cfg.comment          = 'xlim';
       cfg.commentpos       = 'title';
       cfg.layout           = 'CTF151_helmet.mat';
       cfg.figure           = 'gca';
       ft_topoplotER(cfg, raweffectFICvsFC);
    end

{% include image src="/assets/img/tutorial/cluster_permutation_timelock/figure5.png" width="600" %}

_Figure 5: Raw effect (FIC-FC) on the planar gradient ERFs of subject 1, the most prominent clusters are highlighted.._

## Within-subjects experiments

We now consider experiments involving multiple subjects that are each observed in multiple experimental conditions. Typically, every subject is observed in a large number of trials, each one belonging to one experimental condition. Usually, for every subject, averages are computed over all trials belonging to each of the experimental conditions. Thus, for every subject, the data are summarized in an array of condition-specific averages. The permutation test that is described in this section informs us about the following **null hypothesis**: the probability distribution of the condition-specific averages is independent of the experimental conditions.

### Reading-in, preprocessing, timelockanalysis, planar gradient, and grandaveraging

We now describe how we can statistically test the difference between the event-related averages for fully incongruent (FIC) and the fully congruent (FC) sentence endings. For this analysis we use planar gradient data. For convenience we will not do the reading-in and preprocessing steps on all subjects. Instead we begin by loading the timelock structures containing the event-related averages (of the planar gradient data) of all ten subjects. The data is available from [ERF_orig.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock/ERF_orig.mat).

    load ERF_orig

ERF_orig contains allsubjFIC and allsubjFC, each storing the event-related averages for the fully incongruent, and the fully congruent sentence endings, respectively.

The format for these variables, are a prime example of how you should organise your data to be suitable for ft_XXXstatistics. Specifically, each variable is a cell-array of structures, with each subject's averaged stored in one cell. To create this data structure two steps are required. First, the single-subject averages were calculated individually for each subject using the function [ft_timelockanalysis](/reference/ft_timelockanalysis). Second, using a for-loop we have combined the data from each subject, within each condition, into one variable (allsubj_FIC/allsubj_FC). We suggest that you adopt this procedure as well.

On a technical note, it is preferred to represent the multi-subject data as a cell-array of structures, rather than a so-called struct-array. The reason for this is that the cell-array representation allows for easy expansion into a MATLAB function that allows for a variable number of input arguments (which is how the ft_XXXstatistics functions have been designed).

### Permutation test

We now perform the permutation test using **[ft_timelockstatistics](/reference/ft_timelockstatistics)**. The configuration settings for this analysis differ from the previous settings in several fields:

1.  We have to select a different measure to evaluate the effect at sample level (in cfg.statistic)
2.  The design matrix is different (i.c., it now contains two lines instead of one)
3.  The so-called _unit variable_ has to be defined.

The configuration looks as follows:

    cfg         = [];
    cfg.channel = {'MEG'};
    cfg.latency = [0 1];

    cfg.method           = 'montecarlo';
    cfg.statistic        = 'depsamplesT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.minnbchan        = 2;
    cfg.neighbours       = neighbours;  % same as defined for the between-trials experiment
    cfg.tail             = 0;
    cfg.clustertail      = 0;
    cfg.alpha            = 0.025;
    cfg.numrandomization = 500;

    Nsubj  = 10;
    design = zeros(2, Nsubj*2);
    design(1,:) = [1:Nsubj 1:Nsubj];
    design(2,:) = [ones(1,Nsubj) ones(1,Nsubj)*2];

    cfg.design = design;
    cfg.uvar   = 1;
    cfg.ivar   = 2;

We now describe the differences between this configuration and the configuration for a between-trials experiment.

- Instead of an independent samples T-statistic, we use the **dependent samples T-statistic** to evaluate the effect at the sample level (cfg.statistic = 'depsamplesT'). This is because we are dealing with a within-UO instead of a between-UO design.

- The **design matrix** in a within-UO design is different from the design matrix in a between-UO design. In the design matrix for a within-UO design, you have to specify the unit variable. The unit variable specifies the units that have produced the different condition-specific data structures. For example, consider a hypothetical study with 4 subjects and 2 experimental conditions. The design matrix may then look like this: design = [1 2 3 4 1 2 3 4; 1 1 1 1 2 2 2 2 ]. The first row of this matrix is the unit variable: it specifies that the first subject produced the first and the fifth data structure, the second subject produced the second and the sixth data structure, etc. The second row of the design matrix is the independent variable.

- Because the design matrix contains both a unit variable and an independent variable, it has to be specified in the configuration which row contains which variable. This information is passed in the fields **cfg.uvar** (for the unit variable) and **cfg.ivar** (for the independent variable).

Now, use the configuration above to perform the following statistical analysis:

    [stat] = ft_timelockstatistics(cfg, allsubjFIC{:}, allsubjFC{:})

    save stat_ERF_planar_FICvsFC_GA stat

The output can also be obtained from [stat_ERF_planar_FICvsFC_GA.mat](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock/stat_ERF_planar_FICvsFC_GA.mat). If you need to reload the statistics output, use:

    load stat_ERF_planar_FICvsFC_GA

From inspection of stat.posclusters and stat.negclusters, we observe that there is only one significant positive cluster and no significant negative cluster.

### Plotting the results

For plotting we first use [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage) to calculate the grand average (average across all subject's average).

    % load individual subject data
    load('ERF_orig');
    % calculate the grand average for each condition
    cfg = [];
    cfg.channel   = 'all';
    cfg.latency   = 'all';
    cfg.parameter = 'avg';
    GA_FIC        = ft_timelockgrandaverage(cfg, allsubjFIC{:});
    GA_FC         = ft_timelockgrandaverage(cfg, allsubjFC{:});
    % "{:}" means to use data from all elements of the variable

With the output, we can now create the plots

    cfg = [];
    cfg.operation = 'subtract';
    cfg.parameter = 'avg';
    GA_FICvsFC    = ft_math(cfg, GA_FIC, GA_FC);

    figure;
    % define parameters for plotting
    timestep      = 0.05; %(in seconds)
    sampling_rate = dataFIC_LP.fsample;
    sample_count  = length(stat.time);
    j = [0:timestep:1];   % Temporal endpoints (in seconds) of the ERP average computed in each subplot
    m = [1:timestep*sampling_rate:sample_count];  % temporal endpoints in M/EEG samples

    % get relevant values
    pos_cluster_pvals = [stat.posclusters(:).prob];
    pos_clust = find(pos_cluster_pvals < 0.025);
    pos       = ismember(stat.posclusterslabelmat, pos_clust);

    % First ensure the channels to have the same order in the average and in the statistical output.
    % This might not be the case, because ft_math might shuffle the order
    [i1,i2] = match_str(GA_FICvsFC.label, stat.label);

    % plot
    for k = 1:20;
       cfg.figure     = subplot(4,5,k);
       cfg.xlim       = [j(k) j(k+1)];
       cfg.zlim       = [-5e-14 5e-14];
       pos_int        = zeros(numel(GA_FICvsFC.label),1);
       pos_int(i1)    = all(pos(i2, m(k):m(k+1)), 2);
       cfg.highlight  = 'on';
       cfg.highlightchannel = find(pos_int);
       cfg.comment    = 'xlim';
       cfg.commentpos = 'title';
       cfg.layout     = 'CTF151_helmet.mat';
       cfg.figure     = 'gca';
       ft_topoplotER(cfg, GA_FICvsFC);
    end

{% include image src="/assets/img/tutorial/cluster_permutation_timelock/figure6.png" width="600" %}

_Figure 6: Raw effect (FIC-FC) on the grand average planar gradient ERFs with the prominent clusters highlighted._

## Summary and suggested further reading

In this tutorial, it was shown how to do non-parametric statistics on axial and planar ERFs in a between-trials and in within-subjects design. It was also shown how to plot the results.

If you are interested in parametric tests in FieldTrip, you can read the [Parametric and non-parametric statistics on event-related fields](/tutorial/eventrelatedstatistics) tutorial. If you are interested in how to do the same statistics on time-frequency representations, you can read the [Cluster-based permutation tests on time-frequency data](/tutorial/cluster_permutation_freq) tutorial.

If you would like to read more about statistical analysis, you can look at the following FAQs:

{% include seealso category="faq" tag1="statistics" %}
{% include seealso category="faq" tag1="cluster"    %}
{% include seealso category="faq" tag1="neighbour"  %}

and example scripts:

{% include seealso category="example" tag1="statistics" %}
{% include seealso category="example" tag1="cluster"    %}
{% include seealso category="example" tag1="neighbour"  %}
