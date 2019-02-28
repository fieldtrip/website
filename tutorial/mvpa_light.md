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

To get started, we will address the question whether we can discriminate between the three classes
FIC, FC, and IC, using the average activity in the 0.5-0.7 s interval. We will then focus
on two out of the three classes, FIC vs FC, and we will investigate the following questions:

* At *what times* ('when') in a trial can one discriminate between FIC and FC?
* At *which sensor locations* ('where') can one discriminate between FIC and FC?
* Which representations that discriminate between FIC and FC *generalise across time*?

Note that the classification is performed for a single subject using single trials. To make sure that the MVPA-Light functions are in the MATLAB path, call

    startup_MVPA_Light


## Classification in the 0.5-0.7 s interval

We will use `ft_timelockstatistics` to determine the classification accuracy between the three classes FIC, FC, and IC. As features, we will use the average activity in the 0.5-0.7 s interval. This yields XXX features for the classifier, one for each MEG channel, to try to differentiate between FIC, FC, and IC trials. Let us first determine the number of trials in each class

    nFIC = numel(FIC.trial);
    nFC = numel(FC.trial);
    nIC = numel(IC.trial);

Then, we need to define the configuration struct

    cfg = [] ;
    cfg.method      = 'mvpa';
    cfg.classifier  = 'lda';
    cfg.metric      = 'accuracy';
    cfg.k = 3;
    cfg.latency = [0.5, 0.7];
    cfg.avgovertime = 'yes';
    cfg.design = [ones(nFIC,1); 2*ones(nFC,1); 3*ones(nIC,1)];

Let us unpack this a bit:

- `cfg.method='mvpa'`: indicates that the [MVPA-Light](https://github.com/treder/MVPA-Light) toolbox should be used for the `ft_freqanalysis`.
- `cfg.classifier = 'lda'`: indicates that a Linear Discriminant Analysis (LDA) classifier should be used. See the [MVPA-Light documentation for a full list of available classifiers](https://github.com/treder/MVPA-Light#classifiers).
- `cfg.metric = 'accuracy'`: indicates that we want to use *classification accuracy* to measure classifier performance. Other metrics such as Area under the ROC curve (AUC) and F1-score are available. See the [MVPA-Light documentation for a full list of available metrics](https://github.com/treder/MVPA-Light#classifier-performance-metrics).
- `cfg.k = 3`: specifies that we want to use 3 folds to calculate the cross-validated performance. Cross-validation is explained in more detail in the next section.
- `cfg.latency = [0.5, 0.7]`: restricts the classification analysis to the 0.5-0.7 s time window.
- `cfg.avgovertime = 'yes'`: specifies that the activity in the 0.5-0.7 s interval should be averaged prior to classification. If `'no'`, a separate classification is performed for every time point (see section Classification across time).
- `cfg.design = [ones(nFIC,1); 2*ones(nFC,1); 3*ones(nIC,1)]`: specifies the vector of *class labels*.
Class labels specify which trials belong to
which class (or experimental condition). The task of the classifier is to predict these class labels given the data. To this end, we create a vector with *1*'s
for the trials belonging to class 1, *2*'s for trials
belonging to class 2, and so on. Note that the order of the classes does not usually matter (i.e., if you swap the class labels the classification performance does not change). For the [MEG-language dataset](/faq/what_types_of_datasets_and_their_respective_analyses_are_used_on_fieldtrip),
there is three classes, namely FIC (class 1), FC (class 2), and IC (class 3).

Now we can call

    stat = ft_timelockstatistics(cfg, dataFIC_LP, dataFC_LP, dataIC_LP)

to perform the analysis. It is important to make sure that the order of class labels (FIC, FC, IC) matches the order that the data is passed in to `ft_timelockstatistics`.



### Cross-validation

To obtain a realistic estimate of classifier performance and control for overfitting, a classifier should be tested on an independent dataset that has not been used for training. In most neuroimaging experiments, there is only one dataset with a restricted number of trials. K-fold [cross-validation](https://en.wikipedia.org/wiki/Cross-validation) makes efficient use of this data by splitting it into k different folds. In each iteration, one of the k folds is held out and used as test set, whereas all other folds are used for training the model. This process is repeated until every fold has been used as test set once. Cross-validation is controlled by the following parameters:

    `cfg.cv`: cross-validation type, either 'kfold', 'leaveout' or 'holdout' (default 'kfold')
    `cfg.k`: number of folds or partitions in k-fold cross-validation (default 5)
    `cfg.repeat`: number of times the whole cross-validation analysis is repeated with new randomly assigned folds (default 5)
    `cfg.p`: if `cfg.cv` is 'holdout', `p` is the fraction of test samples (default 0.1)
    `cfg.stratify`: if 1, the class proportions are approximately preserved in each test fold (default 1)

The total number of training and testing iterations is equal to `cfg.k * cfg.repeat`. The result returned by `ft_timelockstatistics` is an average of the metrics calculated for each test set.

## Classification across time ('when')

Many neuroimaging datasets have a 3-D structure (trials x channels x time). The start of the trial (t=0) typically corresponds to stimulus or response onset. Classification across time can help identify at which time point in a trial discriminative information shows up. To this end, classification is performed across trials, for each time point separately. The resulting metric (e.g. classification accuracy) can then be plotted as a function of time.
To perform classification across time, we need to make sure that the time dimension preserved by not averaging the data over time. We can set `cfg.avgovertime = 'no'`, but since the default value is `'no'` we can also simply omit this parameter. Likewise, we want to classify across the whole length
of the trial. Hence, we also omit setting the `cfg.latency` parameter.

    cfg = [] ;  
    cfg.method      = 'mvpa';
    cfg.classifier  = 'lda';
    cfg.metric      = 'auc';
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



## Advanced topics

### Hyperparameters

The `param` substruct contains the hyperparameters for the classifier.
Here, we only set `lambda = 'auto'`. This is the default, so in general
setting param is not required unless one wants to change the default
settings.

    cfg.param           = [];
    cfg.param.lambda    = 'auto';
