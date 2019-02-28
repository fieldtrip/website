---
title: Classification of event related MEG data using MVPA-Light
tags: [tutorial, eeg, meg, multivariate, timelock, freq]
---

# Classification of event related MEG data using MVPA-Light

## Introduction

The objective of this tutorial is to give an introduction to the classification of event related
data using the [MVPA-Light](https://github.com/treder/MVPA-Light) toolbox. For a general introduction and background on multivariate analysis, refer to the
[Multivariate analysis of electrophysiological data tutorial](/tutorial/multivariateanalysis)
and the [MVPA-Light readme file](https://github.com/treder/MVPA-Light/blob/master/README.md).
This tutorial builds on skills acquired in the [preprocessing](/tutorial/preprocessing), [event related averaging](/tutorial/eventrelatedaveraging) and [time-frequency analysis](/tutorial/timefrequencyanalysis) tutorials.


## Procedure

We will use classifiers to analyze the [MEG-language dataset](/faq/what_types_of_datasets_and_their_respective_analyses_are_used_on_fieldtrip) which
features one subject with three types of trials: fully incongruent (FIC), fully congruent (FC),
initially congruent (IC). These three classes are stored in different files available here:
 [dataFIC_LP.mat](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/eventrelatedaveraging/dataFIC_LP.mat), [dataFC_LP.mat](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/eventrelatedaveraging/dataFC_LP.mat) and [dataIC_LP.mat](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/eventrelatedaveraging/dataIC_LP.mat).

The data can be loaded into MATLAB using

    load dataFIC_LP
    load dataFC_LP
    load dataIC_LP

To get started, we will address the question whether we discriminate between the three classes
FIC, FC, and IC, using the average activity in the 300-500 ms interval. We will then focus
on two out of the three classes, FIC vs FC, and we will investigate the following questions:

* At *what times* ('when') in a trial can one discriminate between FIC and FC?
* At *which sensor locations* ('where') can one discriminate between FIC and FC?
* Which representations that discriminate between FIC and FC *generalise across time*?

To make sure that the MVPA-Light functions are in the MATLAB path, call

    startup_MVPA_Light


## Classification in the 0.5-0.7 s interval

First, we classify between ...  

    cfg = [] ;
    cfg.method      = 'mvpa';
    cfg.classifier  = 'lda';
    cfg.statistic   = {'accuracy' 'auc'};
    cfg.k = 3;

cfg.design      = clabel_FC_FIC;

% select time
cfg.avgovertime = 'yes';
cfg.latency = [0.5, 0.7];

stat = ft_timelockstatistics(cfg, dataFC_LP, dataFIC_LP)
% stat = ft_timelockstatistics(cfg, dat)


To get a realistic estimate of classification performance, we perform
10-fold (`cfg.k = 10`) cross-validation with 2 repetitions (`cfg.repeat = 10`).

    cfg = [];
    cfg.classifier      = 'lda';
    cfg.metric          = 'auc';
    cfg.cv              = 'kfold';
    cfg.k               = 10;
    cfg.repeat          = 2;


Statistics are called *metrics* in MVPA-Light.
See [classifier performance metrics](https://github.com/treder/MVPA-Light/blob/master/README.md#classifier-performance-metrics) for a full overview over the currently available statistics.


We also need to specify a design matrix containing class labels. The class labels specify which trials belong to
which class (experimental condition). The task of the classifier will be to predict
these class labels. To this end, we create a vector with *1*'s
for the trials belonging to data for the first condition, *2*'s for trials
belonging to data for the second condition, and so on. For the [MEG-language dataset](/faq/what_types_of_datasets_and_their_respective_analyses_are_used_on_fieldtrip),
we have three classes, namely FIC (class 1), FC (class 2), and IC (class 3):


    cfg.design = [ones(numel(dataFC_LP.trial),1); 2 * ones(numel(dataFIC_LP.trial),1); 3 * ones(numel(dataIC_LP.trial),1)];



The `param` substruct contains the hyperparameters for the classifier.
Here, we only set `lambda = 'auto'`. This is the default, so in general
setting param is not required unless one wants to change the default
settings.

    cfg.param           = [];
    cfg.param.lambda    = 'auto';

### Cross-validation

To obtain a realistic estimate of classifier performance and control for overfitting, a classifier should be tested on an independent dataset that has not been used for training. In most neuroimaging experiments, there is only one dataset with a restricted number of trials. K-fold [cross-validation](https://en.wikipedia.org/wiki/Cross-validation) makes efficient use of this data by splitting it into k different folds. In each iteration, one of the k folds is held out and used as test set, whereas all other folds are used for training. This is repeated until every fold has been used as test set once. See [Lemm2011](https://www.sciencedirect.com/science/article/pii/S1053811910014163) for a discussion of cross-validation and potential pitfalls. Cross-validation is controlled by the following parameters:

    `cfg.cv`: cross-validation type, either 'kfold', 'leaveout' or 'holdout' (default 'kfold')
    `cfg.k`: number of folds in k-fold cross-validation (default 5)
    `cfg.repeat`: number of times the cross-validation is repeated with new randomly assigned folds (default 5)
    `cfg.p`: if `cfg.cv` is 'holdout', `p` is the fraction of test samples (default 0.1)
    `cfg.stratify`: if 1, the class proportions are approximately preserved in each test fold (default 1)


## Classification across time ('when')

Many neuroimaging datasets have a 3-D structure (trials x channels x time). The start of the trial (t=0) typically corresponds to stimulus or response onset. Classification across time can help identify at which time point in a trial discriminative information shows up. To this end, classification is performed across trials, for each time point separately. The resulting statistic (e.g. classification accuracy) can then be plotted as a function of time.
The only thing we need to do to perform classification across time is to prevent averaging of the
voltage by *not* setting `cfg.avgovertime = 'yes'`. The default value is `'no'`, so
we can simply omit the parameter. Likewise, we want to classify across the whole length
of the trial. Hence, we also omit setting the `cfg.latency` parameter.

    cfg = [] ;  
    cfg.method      = 'mvpa';
    cfg.classifier  = 'lda';
    cfg.statistic   = 'auc';
    cfg.design      = clabel_FC_FIC;



#### Exercise 1

{% include markup/info %}
Perform classification across time using all three classes FIC, FC, and IC.
You need to change the design matrix
You can use the classifier `multiclass_lda` for this purpose.
{% include markup/end %}


## Searchlight analysis ('where')

Which spatial features contribute most to classification performance? The answer to this question can be used to better interpret the data or to perform feature selection. To this end, we will perform classification for each feature separately. Since our features are the MEG channels with a spatial structure (e.g. neighbouring channels), groups of features rather than single features can be considered. The result of the searchlight analysis is a classification performance measure for each channel.



## Time generalisation (time x time classification)

Classification across time does not give insight into whether information is shared across different time points. For example, is the information that the classifier uses early in a trial (t=80 ms) the same that it uses later (t=300ms)? In time generalisation, this question is answered by training the classifier at a certain time point t. The classifer is then tested at the same time point t but it is also tested at all other time points in the trial [King and Dehaene (2014)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5635958/). mv_classify_timextime implements time generalisation. It returns a 2D matrix of classification performance, with performance calculated for each combination of training time point and testing time point. mv_plot_result can be used to plot the result.
