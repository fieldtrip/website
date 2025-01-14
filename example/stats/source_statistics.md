---
title: Source statistics
category: example
tags: [meg, source, statistics]
redirect_from:
    - /example/source_statistics/
---

# Source statistics

After source analysis (e.g., power estimation with the DICS method as explained in the [beamformer tutorial](/tutorial/beamformer)) you might want to subject the distributions of source power to statistical analysis. This can either be done on the single subject level or on the group level. For both cases, example code is presented.

## Single subject level, statistics over trials

In the following, it is assumed that there is a single subject source reconstruction (_source_) which contains the source estimates for the single trials, and a design matrix (_design_, 1xN vector) which indicates for each trial to which condition it belongs. By using **[ft_sourcestatistics](/reference/ft_sourcestatistics)** we will derive the statistical values for the source activation at each grid point.

To evaluate the reliability of the activation by a statistical measure we will calculate a dependent samples t statistic and plot t maps. Since we are testing for each grid point separately, we have to deal with the multiple comparison problem. One way to control for this is by using a cluster based randomization test. This is further explained in the cluster permutation tutorials for [ERFs](/tutorial/cluster_permutation_timelock) and [time frequency data](/tutorial/cluster_permutation_freq). We will now show how to use a cluster based multiple comparison correction on data for one subject

    % run sourcestatistics using cluster based correction %
    cfg = [];
    cfg.dim         = source.dim;
    cfg.method      = 'montecarlo';
    cfg.statistic   = 'ft_statfun_indepsamplesT';
    cfg.parameter   = 'pow';
    cfg.correctm    = 'cluster';
    cfg.numrandomization = 1000;
    cfg.alpha       = 0.05; % note that this only implies single-sided testing
    cfg.tail        = 0;
    cfg.design(1,:) = [1:length(find(design==1)) 1:length(find(design==2))];
    cfg.design(2,:) = design;
    cfg.uvar        = 1; % row of design matrix that contains unit variable (in this case: trials)
    cfg.ivar        = 2; % row of design matrix that contains independent variable (the conditions)

    stat = ft_sourcestatistics(cfg, source);

The output (_stat_) contains fields pertaining to the cluster based statistic. It contains the field _stat.prob_ with the p values for each grid point, and a field _stat.mask_ with a 1 for each grid point if it is significant and a 0 if it is not significant. In _stat.posclusters_ and _stat.negclusters_ you will find for each cluster the p and cluster-t values. For a further explanation of the output see the cluster permutation tutorials for [ERFs](/tutorial/cluster_permutation_timelock) and [time frequency data](/tutorial/cluster_permutation_freq).

Now the statistical values can be plotted on the subject's MRI, using _stat.mask_ to mask the data, meaning that only significant voxels are plotted.

    % interpolate the t maps to the structural MRI of the subject %
    cfg = [];
    cfg.parameter = 'all';
    statplot = ft_sourceinterpolate(cfg, stat, 'subject.mri');

    % plot the t values on the MRI %
    cfg = [];
    cfg.method        = 'slice';
    cfg.funparameter  = 'stat';
    cfg.maskparameter = 'mask';
    figure
    ft_sourceplot(cfg, statplot);

## Group level, statistics over subjects

In the following, it is assumed that there are two source reconstructions (_grandavgA_ and _grandavgB_) which contain the source estimates for all subjects in a cell-array, one cell per subject, for the conditions A and B respectively.

    % run statistics over subjects %
    cfg=[];
    cfg.dim         = grandavgA{1}.dim;
    cfg.method      = 'montecarlo';
    cfg.statistic   = 'ft_statfun_depsamplesT';
    cfg.parameter   = 'pow';
    cfg.correctm    = 'cluster';
    cfg.numrandomization = 1000;
    cfg.alpha       = 0.05; % note that this only implies single-sided testing
    cfg.tail        = 0;

    nsubj=numel(grandavgA);
    cfg.design(1,:) = [1:nsubj 1:nsubj];
    cfg.design(2,:) = [ones(1,nsubj)*1 ones(1,nsubj)*2];
    cfg.uvar        = 1; % row of design matrix that contains unit variable (in this case: subjects)
    cfg.ivar        = 2; % row of design matrix that contains independent variable (the conditions)

    stat = ft_sourcestatistics(cfg, grandavgA{:}, grandavgB{:});
