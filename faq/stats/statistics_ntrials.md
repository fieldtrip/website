---
title: How does a difference in trial numbers per condition affect my statistical test
parent: Statistical analysis
grand_parent: Frequently asked questions
category: faq
tags: [statistics]
redirect_from:
    - /faq/how_does_a_difference_in_trial_numbers_per_condition_affect_my_statistical_test/
    - /faq/statistics_ntrials/
---

{% include markup/red %}
The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas.

After making changes to the code and/or documentation, this page should remain on the website as a reminder of what was done and how it was done. However, there is no guarantee that this page is updated in the end to reflect the final state of the project

So chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
{% include markup/end %}

# How does a difference in trial numbers per condition affect my statistical test

## The problem

When comparing conditions in an analysis, you often run into the situation that amount of trials for one condition is different than the other. If the amount differs by a few trials this might not be problematic, but are there cases in which it becomes problematic? What could happen if there is a systematic bias in the amount of trials per condition?

## Simulating biased data

The easiest way to see whether a difference in the number of trials can be a problem for you is to simulate such a scenario and run the same statistical tests you are planning to use in your study. In the following example we will consider a within-subjects design with 20 subjects and two conditions. We will generate the data with [ft_freqsimulation](/reference/ft_freqsimulation), average the data with [ft_timelockaverage](/reference/ft_timelockanalysis) and [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage) followed by running statistical tests with [ft_timelockstatistics](/reference/ft_timelockstatistics).

First we will start with simulating the data for all subjects:

    n_subjects = 20;
    data = cell(1,n_subjects);

    cfg = [];
    cfg.method = 'broadband';
    cfg.output = 'mixed';
    cfg.fsample = 1200;
    cfg.trllen = 1;
    cfg.numtrl = 100;
    for i=1:n_subjects
      data{i} = ft_freqsimulation(cfg);
    end

Now that we have simulated the data for all subjects we are going to divide the data into conditions A and B. Note that the assignment into one or the other condition is random and there should be no difference between conditions! After we have divided the data into two conditions, we will average the data per condition and test the difference on the group level. We will repeat this process 100 times and check the distribution of p-values for this particular test and ratio of trials. We will start out with an equal amount of trials in both conditions:

    % Divide the data 1. case, equal amount of trial

    nA = 50; % amont of trials in condition A
    nB = 50; % amount of trials in condition B
    design = [ones(1,nA) 2.*ones(1,nB)];

    % Set the parameters for the statistical comparison
    cfg_stats = [];
    cfg_stats.channel     = 'mix';
    cfg_stats.parameter   = 'avg';
    cfg_stats.method      = 'analytic';
    cfg_stats.statistic   = 'ft_statfun_depsamplesT';
    cfg_stats.alpha       = 0.05;
    cfg_stats.correctm    = 'no';

    cfg_stats.design(1,1:2*n_subjects)  = [ones(1,n_subjects) 2*ones(1,n_subjects)];
    cfg_stats.design(2,1:2*n_subjects)  = [1:n_subjects 1:n_subjects];
    cfg_stats.ivar                = 1; % the 1st row in cfg.design contains the independent variable
    cfg_stats.uvar                = 2; % the 2nd row in cfg.design contains the subject number

    cfg = [];


    n_tests = 100;

    % Run all the tests.
    h = zeros(1,n_tests);
    for j = 1:n_tests
    for i = 1:n_subjects
      temp_design = design(randperm(numel(design)));
      cfg.trials = find(temp_design==1);
      avg_A{i} = ft_timelockanalysis(cfg, data{i});

      cfg.trials = find(temp_design==2);
      avg_B{i} = ft_timelockanalysis(cfg, data{i});
    end
    stat = ft_timelockstatistics(cfg_stats, avg_A{:},avg_B{:});   % don't forget the {:}!
    h(j) = sum(stat.mask)/numel(stat.mask); % calculate proportion of significant tests
    end

## Assumptions of statistical tests

## Skewed distributions

{% include markup/red %}
H0: The data are exchangeable between the conditions, i.e. the data in the conditions cannot be distinguished.

H1: The data are not exchangeable between the conditions, i.e. the data are different.
{% include markup/end %}
