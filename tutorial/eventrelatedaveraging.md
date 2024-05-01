---
title: Event-related averaging and MEG planar gradient
tags: [tutorial, meg, timelock, preprocessing, plotting, meg-language]
---

# Event-related averaging and MEG planar gradient

## Introduction

This tutorial works on the MEG-language dataset, you can click [here](/tutorial/meg_language) for details on the dataset. This tutorial is a continuation from the preprocessing tutorials. We will begin by repeating some code used to select the trials and preprocess the data as described in the earlier tutorials ([trigger-based trial selection](/tutorial/preprocessing), [visual artifact rejection](/tutorial/visual_artifact_rejection)).

In this tutorial you can find information about how to compute an event-related potential (ERP) or event-related field (ERF) and how to calculate the planar gradient (in case the MEG data was acquired by axial-gradiometer sensors). You can find also information in this tutorial about how to visualize the results of the ERP/ERF analysis, and about how to average the results across subjects.

This tutorial assumes that the steps of preprocessing are already clear for the reader. This tutorial does not show how to do statistical analysis on the ERF/ERPs. You can find more information about the statistics in the [Parametric and non-parametric statistics on event-related fields](/tutorial/eventrelatedstatistics) tutorial. If you are interested in the event-related changes in the oscillatory components of the EEG/MEG signal, you can check out the [Time-frequency analysis using Hanning window, multitapers and wavelets](/tutorial/timefrequencyanalysis) tutorial.

## Background

### ERP / ERF

When analyzing EEG or MEG signals, the aim is to investigate the modulation of the measured brain signals with respect to a certain event. However, due to intrinsic and extrinsic noise in the signals - which in single trials is often higher than the signal evoked by the brain - it is typically required to average data from several trials to increase the signal-to-noise ratio(SNR). One approach is to repeat a given event in your experiment and average the corresponding EEG/MEG signals. The assumption is that the noise is independent of the events and thus reduced when averaging, while the effect of interest is time-locked to the event. The approach results in ERPs and ERFs for respectively EEG and MEG. Timelock analysis can be used to calculate ERPs/ ERFs.

### Planar gradient

The CTF MEG system has (151 in this dataset, or 275 in newer systems) first-order axial gradiometer sensors that measure the gradient of the magnetic field in the radial direction, i.e. orthogonal to the scalp. Often it is helpful to interpret the MEG fields after transforming the data to a planar gradient configuration, i.e. by computing the gradient tangential to the scalp. This representation of MEG data is comparable to the field measured by planar gradiometer sensors. One advantage of the planar gradient transformation is that the signal amplitude typically is largest directly above a source.

### The dataset used for this tutorial 

The dataset that we use in this (and many other) tutorial(s), is the [Subject01.ds](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip) dataset. This is data obtained with a 151-channel CTF MEG system, while the participant listened to Dutch sentences. The experimental manipulation was designed to investigate the brain effects of semantic (in)congruency.

## Procedure

To calculate the event-related field / potential for the example dataset we will perform the following steps:

- Read the data into MATLAB using **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)**
- Seperate the trials from each condition using **[ft_selectdata](/reference/utilities/ft_selectdata)**
- Compute the average over trials using the function **[ft_timelockanalysis](/reference/ft_timelockanalysis)**
- Calculate the planar gradient with the functions **[ft_megplanar](/reference/ft_megplanar)** and **[ft_combineplanar](/reference/ft_combineplanar)**
- Visualize the results. You can plot the ERF/ ERP of one channel with **[ft_singleplotER](/reference/ft_singleplotER)** or several channels with **[ft_multiplotER](/reference/ft_multiplotER)**, or by creating a topographic plot for a specified time- interval with **[ft_topoplotER](/reference/ft_topoplotER)**
- Grandaverage and realignment (optional). When you have data from more than one subject you can make a grand average of the ERPs / ERFs with **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)**.

{% include image src="/assets/img/tutorial/eventrelatedaveraging/figure1.png" %}

_Figure: A schematic overview of the steps in averaging of event-related fields._

## Preprocessing

### Reading in the data

We will now read and preprocess the data. If you would like to continue directly with the already preprocessed data, you can download [dataFIC_LP.mat](https://download.fieldtriptoolbox.org/tutorial/eventrelatedaveraging/dataFIC_LP.mat), [dataFC_LP.mat](https://download.fieldtriptoolbox.org/tutorial/eventrelatedaveraging/dataFC_LP.mat) and [dataIC_LP.mat](https://download.fieldtriptoolbox.org/tutorial/eventrelatedaveraging/dataIC_LP.mat). Load the data into MATLAB with the command `load` and skip to [Timelockanalysis](#timelockanalysis).

Otherwise run the following code:

{% include /shared/tutorial/definetrial_all.md %}

### Cleaning

{% include /shared/tutorial/preprocessing_lp.md %}

{% include markup/skyblue %}
A note about padding: The padding parameter (cfg.padding) defines the duration to which the data in the trial will be padded (i.e. data-padded, not zero-padded). The padding is removed from the trial after filtering. Padding the data is beneficial, since the edge artifacts that are typically seen after filtering will be in the padding and not in the part of interest. Padding can also be relevant for DFT filtering of the 50Hz line noise artifact: long padding ensures a higher frequency resolution for the DFT filter, causing a narrower notch to be removed from the data. Padding can only be done on data that is stored in continuous format, therefore it is not used here.
{% include markup/end %}

For subsequent analysis we split the data into three different data structures, one for each condition (fully incongruent condition FIC, fully congruent condition FC, and initially congruent IC).

    cfg = [];
    cfg.trials = data_all.trialinfo == 3;
    dataFIC_LP = ft_selectdata(cfg, data_all);

    cfg = [];
    cfg.trials = data_all.trialinfo == 5;
    dataIC_LP = ft_selectdata(cfg, data_all);

    cfg = [];
    cfg.trials = data_all.trialinfo == 9;
    dataFC_LP = ft_selectdata(cfg, data_all);

Subsequently you can save the data to disk.

      save dataFIC_LP dataFIC_LP
      save dataFC_LP dataFC_LP
      save dataIC_LP dataIC_LP

If preprocessing was done as described, the data structure will have the following fields:

    dataFIC_LP =
             hdr: [1x1 struct]
           label: {149x1 cell}
            time: {1x77 cell}
           trial: {1x77 cell}
         fsample: 300
      sampleinfo: [77x2 double]
       trialinfo: [77x1 double]
            grad: [1x1 struct]
            elec: [1x1 struct]
             cfg: [1x1 struct]

Note that 'dataFIC_LP.label' has 149 in stead of 151 labels since channels MLP31 and MLO12 were excluded. 'dataFIC-LP.trial' has 76 in stead of 87 trials because 10 trials were rejected because of artifacts.

The most important fields are 'dataFIC_LP.trial' containing the individual trials and 'data.time' containing the time vector for each trial. To visualize the single trial data (trial 1) of a single channel (channel 130) you can do the following:

    plot(dataFIC_LP.time{1}, dataFIC_LP.trial{1}(130,:))

{% include image src="/assets/img/tutorial/eventrelatedaveraging/figure2.png" width="400" %}

_Figure: The MEG data from a single trial in a single sensor obtained after ft_preprocessing._

## Timelockanalysis

The function **[ft_timelockanalysis](/reference/ft_timelockanalysis)** makes averages of all the trials in a data structure. It requires preprocessed data (see above), which is available from [dataFIC_LP.mat](https://download.fieldtriptoolbox.org/tutorial/eventrelatedaveraging/dataFIC_LP.mat), [dataFC_LP.mat](https://download.fieldtriptoolbox.org/tutorial/eventrelatedaveraging/dataFC_LP.mat) and [dataIC_LP.mat](https://download.fieldtriptoolbox.org/tutorial/eventrelatedaveraging/dataIC_LP.mat).

    load dataFIC_LP
    load dataFC_LP
    load dataIC_LP

The trials belonging to one condition will now be averaged with the onset of the stimulus time aligned to the zero-time point (the onset of the last word in the sentence). This is done with the function **[ft_timelockanalysis](/reference/ft_timelockanalysis)**. The input to this procedure is the dataFIC_LP structure generated by **[ft_preprocessing](/reference/ft_preprocessing)**. No special settings are necessary here. Thus specify an empty configuration.

    cfg = [];
    avgFIC = ft_timelockanalysis(cfg, dataFIC_LP);
    avgFC = ft_timelockanalysis(cfg, dataFC_LP);
    avgIC = ft_timelockanalysis(cfg, dataIC_LP);

The output is the data structure avgFIC with the following fields:

    avgFIC =
          time: [-1 -0.9967 -0.9933 -0.9900 -0.9867 … ]
         label: {149x1 cell}
          elec: [1x1 struct]
          grad: [1x1 struct]
           avg: [149x900 double]
           var: [149x900 double]
           dof: [149x900 double]
        dimord: 'chan_time'
           cfg: [1x1 struct]

The most important field is avgFIC.avg, containing the average over all trials for each sensor.

## Plot the results (axial gradients)

Using the plot functions **[ft_multiplotER](/reference/ft_multiplotER)**, **[ft_singleplotER](/reference/ft_singleplotER)** and **[ft_topoplotER](/reference/ft_topoplotER)** you can make plots of the average. You can find information about plotting also in the [Plotting data at the channel and source level](/tutorial/plotting) tutorial.

Use **[ft_multiplotER](/reference/ft_multiplotER)** to plot all sensors in one figure:

    cfg = [];
    cfg.showlabels = 'yes';
    cfg.fontsize = 6;
    cfg.layout = 'CTF151_helmet.mat';
    cfg.ylim = [-3e-13 3e-13];
    ft_multiplotER(cfg, avgFIC);

{% include image src="/assets/img/tutorial/eventrelatedaveraging/figure3.png" width="700" %}

_Figure: The event-related fields plotted using ft_multiplotER. The event-related fields were calculated using ft_preprocessing followed by ft_timelockanalysis._

This plots the event-related fields for all sensors arranged topographically according to their position in the helmet. You can use the zoom button (magnifying glass) to enlarge parts of the figure. You can use multiple data arguments in the input, and these will be displayed together:

    cfg = [];
    cfg.showlabels = 'no';
    cfg.fontsize = 6;
    cfg.layout = 'CTF151_helmet.mat';
    cfg.baseline = [-0.2 0];
    cfg.xlim = [-0.2 1.0];
    cfg.ylim = [-3e-13 3e-13];
    ft_multiplotER(cfg, avgFC, avgIC, avgFIC);

{% include image src="/assets/img/tutorial/eventrelatedaveraging/figure4.png" width="700" %}

_Figure: The event-related fields for three conditions plotted simultaneously using ft_multiplotER._

To plot the data of a single sensor you can use **[ft_singleplotER](/reference/ft_singleplotER)** while specifying the name of the channel you are interested in, for instance MLC24:

    cfg = [];
    cfg.xlim = [-0.2 1.0];
    cfg.ylim = [-1e-13 3e-13];
    cfg.channel = 'MLC24';
    ft_singleplotER(cfg, avgFC, avgIC, avgFIC);

{% include image src="/assets/img/tutorial/eventrelatedaveraging/figure5.png" width="400" %}

_Figure: The event-related fields plotted for three conditions for sensor MLC24 using ft_singleplotER._

To plot the topographic distribution of the data averaged over the time interval from 0.3 to 0.5 seconds you can use the following command:

    cfg = [];
    cfg.xlim = [0.3 0.5];
    cfg.colorbar = 'yes';
    cfg.layout = 'CTF151_helmet.mat';
    ft_topoplotER(cfg, avgFIC);

{% include image src="/assets/img/tutorial/eventrelatedaveraging/figure6.png" width="400" %}

_Figure: A topographic plot of the event-related fields obtained using ft_topoplotER._

To plot a sequence of topographic plots you can define cfg.xlim to be a vector:

    cfg        = [];
    cfg.xlim   = [-0.2 : 0.1 : 1.0];  % Define 12 time intervals
    cfg.zlim   = [-2e-13 2e-13];      % Set the 'color' limits.
    cfg.layout = 'CTF151_helmet.mat';
    ft_topoplotER(cfg, avgFIC);

{% include image src="/assets/img/tutorial/eventrelatedaveraging/figure7.png" width="700" %}

_Figure: The topography of event-related fields over time obtained using ft_topoplotER._

#### Exercise 1

{% include markup/skyblue %}
What changes in the data if you extend the baseline correction (which is initially from -200 ms to 0 ms) to a longer period from -500 ms to 0?

Apply a band-pass filter in the preprocessing instead of only a low-pass filter. Use for example the values from 1 Hz to 30 Hz. What changes in the data? What are the pros and cons of using a high-pass filter?
{% include markup/end %}

#### Exercise 2

{% include markup/skyblue %}
Which type of source configuration can explain the topography?
{% include markup/end %}

## Calculate the planar gradient

With **[ft_megplanar](/reference/ft_megplanar)** we calculate the planar gradient of the averaged data. **[Ft_megplanar](/reference/ft_megplanar)** is used to compute the gradient of the magnetic field that is tangential to the head surface. This leads to a 2-dimensional signal at each of the sensor locations, which are denoted as 'horizontal' and 'vertical' components of the planar gradient. This terminology is based on the analogy with a 2-dimensional Cartesian coordinate system, with a horizontal and vertical axis: the gradient axes are not 'horizontal' and 'vertical' w.r.t. the surroundings.

The planar gradient at a given sensor location can be approximated by comparing the field at that sensor with its neighbors (i.e. by means of a finite difference estimate of the derivative). To compute the magnitude of the gradient, the two orthogonal gradients on a single sensor location can be combined using Pythagoras rule with the FieldTrip function **[ft_combineplanar](/reference/ft_combineplanar)**.

Calculate the planar gradient of the averaged data:

    cfg                 = [];
    cfg.feedback        = 'yes';
    cfg.method          = 'template';
    cfg.neighbours      = ft_prepare_neighbours(cfg, avgFIC);

    cfg.planarmethod    = 'sincos';
    avgFICplanar        = ft_megplanar(cfg, avgFIC);

Compute the magnitude of the planar gradient by combining the horizontal and vertical components of the planar gradient according to Pythagoras rule:

    cfg = [];
    avgFICplanarComb = ft_combineplanar(cfg, avgFICplanar);

## Plot the results (planar gradients)

To compare the axial gradient data to the planar gradient data we plot them both in one figure here.

Plot the results of the field of the axial gradiometers and the planar gradient to compare the topographies:

    cfg = [];
    cfg.xlim = [0.3 0.5];
    cfg.zlim = 'maxmin';
    cfg.colorbar = 'yes';
    cfg.layout = 'CTF151_helmet.mat';
    cfg.figure  = subplot(121);
    ft_topoplotER(cfg, avgFIC)

    colorbar; % you can also try out cfg.colorbar = 'south'
    
    cfg.zlim = 'maxabs';
    cfg.layout = 'CTF151_helmet.mat';
    cfg.figure  = subplot(122);
    ft_topoplotER(cfg, avgFICplanarComb);

{% include image src="/assets/img/tutorial/eventrelatedaveraging/figure8.png" width="500" %}

_Figure: A comparison of event-related fields from the axial gradiometers (left) and the planar gradient (right). The planar gradient was calculated using ft_megplanar and ft_combineplanar._

#### Exercise 3

{% include markup/skyblue %}
Compare the axial and planar gradient field

Why are there only positive values above the sources in the representation of the combined planar gradient?

Explain the topography of the planar gradient from the fields of the axial gradient
{% include markup/end %}

## Grand average over subjects

Finally you can make a grand-average over all our four subjects with **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)**. Before calculating the grand average, the data of each subject can be realigned to standard sensor positions with **[ft_megrealign](/reference/ft_megrealign)**. For this step, there are the additional datasets [Subject02.zip](https://download.fieldtriptoolbox.org/tutorial/Subject02.zip), [Subject03.zip](https://download.fieldtriptoolbox.org/tutorial/Subject03.zip), and [Subject04.zip](https://download.fieldtriptoolbox.org/tutorial/Subject04.zip).

For more information about this, type the following commands in the MATLAB command window.

    help ft_timelockgrandaverage
    help ft_megrealign

## Summary and suggested further reading

This tutorial covered how to do event-related averaging on EEG/MEG data, and on how to plot the results. The tutorial gave also information about how to average the results across subjects. After calculating the ERPs/ERFs for each subject and for each condition in an experiment, it is a relevant next step to see if there are statistically significant differences in the amplitude of the ERPs/ERFs between the conditions. If you are interested in this, you can continue with the [event-related statistics](/tutorial/eventrelatedstatistics) tutorial.

If you are interested in a different analysis of your data that shows event-related changes in the oscillatory components of the signal, you can continue with the [time-frequency analysis](/tutorial/timefrequencyanalysis) tutorial.

## See also

{% include seealso tag1="timelock" tag2="faq" %}
{% include seealso tag1="timelock" tag2="example" %}
