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

We will use `ft_timelockstatistics` to determine the classification accuracy between the three classes FIC, FC, and IC. As features, we will use the average activity in the 0.5-0.7 s interval. This yields XXX features for the classifier, one for each MEG channel, to try to differentiate between FIC, FC, and IC trials. Let us first determine the number of trials in each class:

    nFIC = numel(dataFIC_LP.trial);
    nFC = numel(dataFC_LP.trial);
    nIC = numel(dataIC_LP.trial);

Now we need to define the configuration struct

    cfg = [] ;
    cfg.method      = 'mvpa';
    cfg.classifier  = 'multiclass_lda';
    cfg.metric      = 'accuracy';
    cfg.k           = 3;
    cfg.latency     = [0.5, 0.7];
    cfg.avgovertime = 'yes';
    cfg.design      = [ones(nFIC,1); 2*ones(nFC,1); 3*ones(nIC,1)];

Let us unpack this a bit:

- `cfg.classifier` indicates which classifier we want to use. Here, we use multi-class Linear Discriminant Analysis (LDA).  [Click here](https://github.com/treder/MVPA-Light#classifiers-for-two-classes) for a full list of available classifiers.
- `cfg.metric` indicates the metric we use to measure classifier performance. Here, *classification accuracy* is used. Other metrics such as AUC and F1-score are available. [Click here](https://github.com/treder/MVPA-Light#classifier-performance-metrics) for a full list of available metrics.
- `cfg.k` specifies the number of folds used to calculate the cross-validated performance. Cross-validation is explained in more detail in the next section.
- `cfg.latency` restrict the classification analysis to a specific time window (here 0.5-0.7s).
- `cfg.avgovertime` specifies whether the activity in latency window should be averaged prior to classification. If `'no'`, a separate classification is performed for every time point (see section Classification across time).
- `cfg.design` specifies the vector of *class labels*. Class labels indicate which class (or experimental condition) trials belong to. The task of the classifier is to predict these class labels given the data. To this end, we create a vector with *1*'s
for the trials belonging to class 1, *2*'s for trials
belonging to class 2, and so on. Note that the order of the classes does not usually matter (i.e., if you swap the class labels the classification performance does not change). For the [MEG-language dataset](/faq/what_types_of_datasets_and_their_respective_analyses_are_used_on_fieldtrip),
there is three classes, namely FIC (class 1), FC (class 2), and IC (class 3).

Now we can call

    stat = ft_timelockstatistics(cfg, dataFIC_LP, dataFC_LP, dataIC_LP)

to perform the analysis. It is important to make sure that the order of class labels (FIC, FC, IC) matches the order that the data is passed in to `ft_timelockstatistics`. Let us print the resulting classification
accuracy

    fprintf('Classification accuracy: %0.2f\n', stat.metric.accuracy)

For multi-class problems, the [confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) is
a useful metric. In a confusion matrix, rows corresponds to the true class labels,
columns correspond to predicted class labels. The (i,j)-th element gives the
proportion of samples of class i that have been classified as class j.

    cfg.metric      = 'confusion';
    stat = ft_timelockstatistics(cfg, dataFIC_LP, dataFC_LP, dataIC_LP)

    stat.metric.confusion

Looking at the diagonal of the matrix tells us that the classifier is doing better
at predicting classes 1 (0.51) and 2 (0.55) than it is at correctly predicting class 3 (0.32).
For a simple visualisation of this result, we can use a plotting function from [MVPA-Light](https://github.com/treder/MVPA-Light)
called [`mv_plot_result`](https://github.com/treder/MVPA-Light/blob/master/plot/mv_plot_result.m).
It takes the result structure returned in `stat.mvpa_result` which contains the
classification results in a format required by the function. As an additional parameter,
we can pass the values for the time axis.

    mv_plot_result(stat.mvpa_result)

    {% include image src="/assets/img/tutorial/mvpa_light/confusion_matrix.png" width="300" %}


### Cross-validation

To obtain a realistic estimate of classifier performance and control for overfitting, a classifier should be tested on an independent dataset that has not been used for training. In most neuroimaging experiments, there is only one dataset with a restricted number of trials. K-fold [cross-validation](https://en.wikipedia.org/wiki/Cross-validation) makes efficient use of this data by splitting it into k different folds. In each iteration, one of the k folds is held out and used as test set, whereas all other folds are used for training the model. This process is repeated until every fold has been used as test set once. Cross-validation is controlled by the following parameters:

- `cfg.cv`: cross-validation type, either 'kfold', 'leaveout' or 'holdout' (default 'kfold')
- `cfg.k`: number of folds or partitions in k-fold cross-validation (default 5)
- `cfg.repeat`: number of times the whole cross-validation analysis is repeated with new randomly assigned folds (default 5)
- `cfg.p`: if `cfg.cv` is 'holdout', `p` is the fraction of test samples (default 0.1)
- `cfg.stratify`: if 1, the class proportions are approximately preserved in each test fold (default 1)

The total number of training and testing iterations is equal to `cfg.k * cfg.repeat`. The result returned by `ft_timelockstatistics` is an average of the metrics calculated for each test set.

## Classification across time ('when')

Many neuroimaging datasets have a 3-D structure (trials x channels x time). Classification across time can help identify at which time point in a trial ('when') discriminative information shows up. To this end, classification is performed across trials, for each time point separately. The resulting metric (e.g. classification accuracy) can then be plotted as a function of time.
To perform classification across time, we need to make sure that the time dimension preserved by not averaging the data over time. We can set `cfg.avgovertime = 'no'`, but since the default value is `'no'` we can also simply omit this parameter.

    cfg = [] ;  
    cfg.method      = 'mvpa';
    cfg.classifier  = 'lda';
    cfg.metric      = 'auc';
    cfg.design      = [ones(nFIC,1); 2*ones(nFC,1)];
    cfg.k           = 10;
    cfg.repeat      = 2;

For simplicity, we will limit ourselves to comparing only FIC and FC. As classifier,
we use Linear Discriminant Analysis (LDA). As metric, we use area under the ROC curve (AUC).
It is calculated using 10-fold cross-validation with 2 repetitions.

    stat = ft_timelockstatistics(cfg, dataFIC_LP, dataFC_LP)

Note that the metric is now a vector with 900 values, one for each time point.
It can be plotted using

    plot(stat.metric.auc)

For a slightly nicer plot, we can again use `mv_plot_result`. As an additional parameter,
we can pass the values for the time axis. This makes sure that the x-axis is scaled
correctly.

    mv_plot_result(stat.mvpa_result, dataFC_LP.time{1})

The resultant plot shows the AUC across time in the trial. The shaded area
is the standard deviation of the AUC metric across the different test sets in the
cross-validation.


    {% include image src="/assets/img/tutorial/mvpa_light/classify_across_time1.png" width="200" %}



#### Exercise 1

{% include markup/info %}
Perform classification across time using all three classes FIC, FC, and IC. As
classifier, use kernel FDA. As metric, use classification accuracy.
{% include markup/end %}


## Searchlight analysis ('where')

Which channels contribute most to classification performance? The answer to this question can be used to better interpret the data or to perform feature selection. To this end, we will perform classification for each feature separately. The result of the searchlight analysis is a classification performance measure for each channel.

    cfg = [] ;  
    cfg.method      = 'mvpa';
    cfg.searchlight = 'yes';
    cfg.design      = [ones(nFIC,1); 2*ones(nFC,1)];
    cfg.latency     = [0.3, 0.7];
    cfg.avgovertime = 'yes';
    stat = ft_timelockstatistics(cfg, dataFIC_LP, dataFC_LP)

Since we have not specified a classifier and a metric, the default values (LDA and classification accuracy)
are used. Note that in searchlight analysis, the *time points* in a trial are used as
features, for each channel separately. Set `cfg.latency` to restrict the analysis to
a specific time window, and set `cfg.avgovertime='yes'` if you want the values in the time
window to be averaged.

Since we receive one value for each channel we can plot the classification accuracy
as a topography. To achieve this, we first need to set `accuracy` as a field of `stat`.
Then we can call `ft_topoplotER` to do the plotting.

    stat.accuracy = stat.metric.accuracy;

    cfg              = [];
    cfg.parameter    = 'accuracy';
    cfg.layout       = 'CTF151.lay';            
    cfg.xlim         = [0, 0];
    cfg.colorbar     = 'yes';
    cfg.interplimits = 'electrodes';
    ft_topoplotER(cfg, stat);


{% include image src="/assets/img/tutorial/mvpa_light/searchlight_topo1.png" width="200" %}

So far we have performed the classification for each channel separately.
However, since the MEG channels have a spatial structure (e.g. neighbouring channels),
we can also consider groups of neighbouring channels. To do this, we must provide
a distance matrix that specifies which channels are neighbours of each other.

    %%% Get layout
    cfg = [];
    cfg.layout      = 'CTF151.lay';
    cfg.skipscale   = 'yes';
    cfg.skipcomnt   = 'yes';
    cfg.channel     = dataFIC_LP.label;
    lay = ft_prepare_layout(cfg);

    %%% Get distance matrix
    nb_mat = squareform(pdist(lay.pos));

We are now ready to re-run the searchlight analysis

      cfg = [] ;  
      cfg.method      = 'mvpa';
      cfg.searchlight = 'yes';
      cfg.design      = [ones(nFIC,1); 2*ones(nFC,1)];
      cfg.latency     = [0.3, 0.7];
      cfg.avgovertime = 'yes';

      cfg.nb = nb_mat;
      cfg.size = 3;

      stat = ft_timelockstatistics(cfg, dataFIC_LP, dataFC_LP)

As expected, the resultant topography is slightly more smeared out. Also the
maximum classification accuracy is higher which is due to the classifier now
being able to combine information across neighbouring channels.

      {% include image src="/assets/img/tutorial/mvpa_light/searchlight_topo2.png" width="200" %}


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

### Unbalanced classes


### Classifier weights vs activation patterns


## Summary

In a way, searchlight analysis is orthogonal to classification across time: in searchlight analysis,
the time points serve as features and classification is performed for each channel separately.
In classification across time, the channels serve as features and classification is performed for each
time point separately.
