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


Statistics are called *metrics* in MVPA-Light.
See [classifier performance metrics](https://github.com/treder/MVPA-Light/blob/master/README.md#classifier-performance-metrics) for a full overview over the currently available statistics.


## Procedure

We will use classifiers to analyze the [MEG-language dataset](/faq/what_types_of_datasets_and_their_respective_analyses_are_used_on_fieldtrip) which
features one subject with three types of trials: fully incongruent (FIC), fully congruent (FC),
initially congruent (IC). These three classes are stored in different files available here:
 [[dataFIC_LP.mat](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/eventrelatedaveraging/dataFIC_LP.mat), [dataFC_LP.mat](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/eventrelatedaveraging/dataFC_LP.mat) and [dataIC_LP.mat](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/eventrelatedaveraging/dataIC_LP.mat).

Now load the data into MATLAB using

    load dataFIC_LP
    load dataFC_LP
    load dataIC_LP

* Can we discriminate between the three classes using the average activity in the 300-500 ms interval?

We will then focus on two out of the three classes, FIC vs FC, and we will investigate the following questions:

* At what times in a trial can we discriminate between FIC and FC?
* At which sensor locations can we discriminate between FIC and FC?
* At which sensor locations can we discriminate between FIC and FC?


### Sensor level classification in the time domain

Make sure that the multivariate toolbox at /fieldtrip_xxx/external/dmlt/ is in your MATLAB path.

    addpath(genpath('/your-path-to-fieldtrip/external/dmlt'))

We will start by analyzing the data in the time domain for our subject.

    load covatt;

We now perform a timelock analysis in order to make the data suitable as input to **[ft_timelockstatistics](/reference/ft_timelockstatistics)**. That is, we are going to predict attention direction from temporal data. For the purpose of demonstration we will focus on occipital channels only.

    cfg             = [];
    cfg.parameter   = 'trial';
    cfg.keeptrials  = 'yes';         % classifiers operate on individual trials
    cfg.channel     = {'MLO' 'MRO'}; % occipital channels only
    tleft   = ft_timelockanalysis(cfg, left);
    tright  = ft_timelockanalysis(cfg, right);

Now we specify cross-validation as a method for timelock statistics. This ensures that we will perform a classification of our data based on five-fold cross-validation. This splits up the data into five partitions or folds and attempts to build five different classifiers using the remaining four folds. The end result is then averaged over folds.

    cfg         = [];
    cfg.layout  = 'CTF275.lay';
    cfg.method  = 'crossvalidate';

We also need to specify a design matrix; this is simply a vector with labels *1* for the trials belonging to data for the first condition and labels *2* for trials belonging to data for the second condition

    cfg.design  = [ones(size(tleft.trial,1),1); 2*ones(size(tright.trial,1),1)]';

Let's focus on the last segment of the data

    cfg.latency = [2.0 2.5]; % final bit of the attention period

Finally, we call **[ft_timelockstatistics](/reference/ft_timelockstatistics)** which uses the default classification procedure; namely a standardization of the data (subtraction of the mean and division by the standard deviation), followed by applying a linear support vector machin

    stat = ft_timelockstatistics(cfg, tleft, tright);

The stat.statistic field now contains some useful statistics. By default it contains stat.accuracy (proportion of correctly classified trials) and a binomial significance test

    stat.statistic

Here, it indicates that classification performance is above chance level (0.5) and it is significant according to the binomial test (p<0.05). Note that we may be interested in other representations of classification performance such as the contingency matrix with true classes in rows and predicted classes in columns. Statistics may be specified as follow

    cfg.statistic = {'accuracy' 'binomial' 'contingency'};

when running **[ft_timelockstatistics](/reference/ft_timelockstatistics)**. We can now, in addition, look at the contingency matri

    stat = ft_timelockstatistics(cfg,tleft,tright);
    stat.statistic.contingency

We may also plot the parameters of the used classifier as if it were electrophysiological data. This is represented in the stat.model field. For each fold we have a model and each such model may contain different parameters. For example, for the default support vector machine ([SVM](http://en.wikipedia.org/wiki/Support_vector_machine)), we have a stat.model{i}.primal field for each fold i. The easiest way to plot one of the parameters is to assign it to a different field in the stat object:

    stat.mymodel = stat.model{1}.primal;

and subsequently to treat the stat object as if it were data. The *parameter* field is then used to determine what to plo

    cfg              = [];
    cfg.parameter    = 'mymodel';
    cfg.layout       = 'CTF275.lay';
    cfg.xlim         = [2.0 2.5];
    cfg.comments     = '';
    cfg.colorbar     = 'yes';
    cfg.interplimits = 'electrodes';
    ft_topoplotER(cfg, stat);

{% include image src="/assets/img/tutorial/multivariateanalysis/clf_1.png" width="200" %}

In practice, we may want to average the parameters over folds to get an average estimate of the parameters. Note further that the plot is hard to interpret. The fact that contributions extend beyond the selected channels is due to interpolation artifacts. If we look at individual features using *imagesc(stat.mymodel)* then it will be found that all features are used due to the way classifier operates. One way to solve this is to use *dimensionality reduction* or *feature selection*. We will see examples later in this tutorial.

#### Exercise 1

{% include markup/info %}
Explain which information the contingency matrix gives you, which the accuracy does not.  
{% include markup/end %}

Redo the above analysis with a latency of [0 0.5]. Explain what you believe to be the optimal latency with which to analyse this data.

Suppose you use a dataset consisting of randomly generated data. What do you expect when you test classifier performance using the same data? And what do you expect if you use a second randomly generated dataset to test the classifier? Use the concepts of *overfitting* and *generalization* in your explanation.

Suppose you try multiple different classification procedures and find at some point that you reach a classification performance that is significantly better than chance at p=0.05. Should you trust this result? Why (not)?
{% include markup/end %}

### Sensor level classification in the frequency domain

We now try to classify the same data in the frequency domain. Therefore, we need to perform a frequency analysis. Let's focus on the alpha band at the end of the attention period.

    cfg              = [];
    cfg.output       = 'pow';
    cfg.method       = 'mtmconvol';
    cfg.taper        = 'hanning';
    cfg.foi          = 8:2:14;
    cfg.t_ftimwin    = ones(length(cfg.foi),1).*0.5;
    cfg.channel      = {'MLO' 'MRO'};
    cfg.toi          = 2.0:0.1:2.5;
    cfg.keeptrials   = 'yes'; % classifiers operate on individual trials

    tfrleft          = ft_freqanalysis(cfg, left);
    tfrright         = ft_freqanalysis(cfg, right);

Now we call freqstatistics with crossvalidate as our method.

    cfg         = [];
    cfg.layout  = 'CTF275.lay';
    cfg.method  = 'crossvalidate';
    cfg.design  = [ones(size(tfrleft.powspctrm,1),1); 2*ones(size(tfrright.powspctrm,1),1)]';
    stat        = ft_freqstatistics(cfg,tfrleft,tfrright);

We can compare classification performance with the previous results

    stat.statistic

and we see a major improvement since we are focusing on the physiologically relevant alpha band. Again, we may plot the classifier parameters to obtain a so-called importance map

    stat.mymodel = stat.model{1}.primal;

    cfg              = [];
    cfg.layout       = 'CTF275.lay';
    cfg.parameter    = 'mymodel';
    cfg.comment      = '';
    cfg.colorbar     = 'yes';
    cfg.interplimits = 'electrodes';
    ft_topoplotTFR(cfg, stat);

{% include image src="/assets/img/tutorial/multivariateanalysis/clf_2.png" width="200" %}

#### Exercise 2

{% include markup/info %}
Rerun the previous cross-validation with 'cfg.nfolds=2'. Explain the difference and motivate why it is important to perform cross-validation instead of just dividing the data into one training and one test set.
{% include markup/end %}

### Dimensionality reduction and feature selection

One important thing to consider when classifying electrophysiological data is that we wish to reduce as much as possible the number of features used to classify the data. There are two ways to achieve this: either we map the input data to another space with a smaller number of dimensions or we select a number of dimensions from the original space.
Going back to our analysis of timelocked data, we could for instance use common spatial patterns (see this [paper](http://dx.doi.org/10.1016/j.neuroimage.2010.06.048) for an explanation) to map our data to a different space. Here, instead, we perform a feature selection in the original space using a regularized classification approach. This is done by overriding the default classification procedure using the *cfg.mva* field:

    cfg         = [];
    cfg.layout  = 'CTF275.lay';
    cfg.method  = 'crossvalidate';
    cfg.design  = [ones(size(tfrleft.powspctrm,1),1); 2*ones(size(tfrright.powspctrm,1),1)]';
    cfg.mva     = {dml.standardizer dml.enet('family','binomial','alpha',0.2)};

This multivariate analysis standardizes the data and subsequently calls an elastic net logistic regression with regularization parameter alpha equal to 0.2. This parameter influences how many features will be selected for classification. The larger the parameter, the fewer features will be used. For a description of the used algorithm, you may consult the following [paper](http://www.jstatsoft.org/v33/i01/). The elastic net algorithm gives the following result

    stat = ft_freqstatistics(cfg, tfrleft, tfrright);
    stat.statistic

If we inspect stat.model{1} then we find that a different set of parameters is estimated (weights and bias). The weights are the regression coefficients of interest and bias is just an offset term.
If we look at the weights then we find that just a very small number of features from the total of 912 possible features are used. This is also reflected in the topoplot.

    stat.mymodel     = stat.model{1}.weights;

    cfg              = [];
    cfg.layout       = 'CTF275.lay';
    cfg.parameter    = 'mymodel';
    cfg.comment      = '';
    cfg.colorbar     = 'yes';
    cfg.interplimits = 'electrodes';
    ft_topoplotTFR(cfg, stat);

{% include image src="/assets/img/tutorial/multivariateanalysis/clf_3.png" width="200" %}

#### Exercise 3

{% include markup/info %}
Use MATLAB to compute the number of non-zero elements in stat.model{1}.weights.

Why is it useful to have a representation in terms of a small number of non-zero elements?

Repeat the above analysis with a different value for alpha. Explain the results.

Alpha is a free parameter in our model. How would you determine the optimal setting for this parameter?

If we use more and more features then classification performance will first go up but eventually starts to degrade. Explain why this may happen.

Suppose we wish to select the optimal feature subset by testing all possible subsets. How many subsets do we need to test when we have *n* features in total?
{% include markup/end %}

## Conclusion

In this tutorial we have touched on a number of important issues in the classification of electrophysiological data. However, we barely scratched the surface of this field since there are many more possibilities to explore. First, many different procedures can be devised that use different forms of preprocessing, feature selection  and/or prediction. For example, we may want to deal with continuous instead of discrete outputs (regression versus classification), we may want to perform a Bayesian analysis which also gives error bars on the predictions, or we may want to use timeseries analysis in order to predict changes in ongoing activity.

To use some of the more advanced methods it is required to call lower level functions. We recommend looking at the tutorials which have been written for DMLT. These can be accessed through MATLAB's *doc* facility.

To construct online experimental designs that make use of multivariate analysis, for example to build BCI or neurofeedback applications, we have developed the [realtime](/development/realtime) module.
