---
title: Cleaning artifacts using ICA
tags: [artifact, meg, raw, preprocessing, meg-artifact]
category: tutorial
weight: 43
redirect_from:
    - /tutorial/ica_artifact_cleaning/
---

## Introduction

In this tutorial we will demonstrate ICA cleaning on the [ArtifactMEG.zip](https://download.fieldtriptoolbox.org/tutorial/ArtifactMEG.zip) example MEG dataset. This is a resting state recording without an explicit experimental task, however in this recording the subject was on putpose making certain types of artifacts, such as blinking with the eyes, looking back and forth, making headmovements, and biting their teeth to induce EMG activity in the jaw muscles.

This dataset not only includes MEG data, but also separate bipolar recordings from the EOG and ECG, plus two bipolar EMG channels that record activity from neck and jaw muscles. In principle we could use these extra channels to find artifacts or to facilitate or even automate the identification of artifactual ICA components. In the remainder we will _not_ make use of the EOG, ECG and EMG channels, we will only show how ICA can be used on the MEG channels.

## Background

Independent component analysis (ICA) is a spatio-temporal decomposition strategy that assumes that the underlying sources of the EEG or MEG have a stationary spatial projection to the channels, and are temporally maximally independent. Using ICA it is possible to estimate as many components as there are channels. We know that there are many more neuronal sources than channels, especially if the recordings are very long. As such, the ICA decomposition will only be an approximation of the most visible independent components. We also know that the number of prominent artifactual contributions to the data is usually rather limited, so that means that we probably only need a few components to explain the artifacts. Following the ICA decomposition we can identify the artifactual components, and backproject all other components to the channel level, excluding the artifacts.

As ICA assumes spatially stationary sources and can only estimate a limited set of sources, we should try to preprocess our data so that we don't "loose" ICA components to trivial artifacts in the data. If your subject is still moving in the first few minutes of the recording because the experiment did not start yet, you would want to exclude that section from the ICA decomposition.

For efficiency reasons we often do the preprocessing by first identifying the trials of interest and only reading those into memory. However, it might be that certain stereotypical artifacts are more frequent in the inter-trial intervals,for example when the subject was not required to maintain fixation and was more likely to blink or make saccades. Including these inter-trial intervals can therefore contribute to the identification of the eye-related components.

## Procedure

To clean the MEG data using ICA, we will follow the following procedure

-   read the data with minimal preprocessing using **[ft_preprocessing](/reference/ft_preprocessing)**
-   remove segments with infrequent atypical artifacts using either **[ft_rejectvisual](/reference/ft_rejectvisual)** or **[ft_databrowser](/reference/ft_databrowser) (or both)
-   ICA decomposition of the data using **[ft_componentanalysis](/reference/ft_componentanalysis)**
-   identifying the components that reflect eye and heart artifacts using **[ft_topoplotIC](/reference/ft_topoplotIC)** and **[ft_databrowser](/reference/ft_databrowser)
-   removing those components and backprojecting the data using **[ft_rejectcomponent](/reference/ft_rejectcomponent)**

{% include image src="/assets/img/tutorial/ica_artifact_cleaning/figure1.png" width="600" %}

In the schematic outline of the procedure you can see that we will use either **[ft_rejectvisual](/reference/ft_rejectvisual)** or **[ft_databrowser](/reference/ft_databrowser)** to identify the atypical artifacts. The databrowser will give you a good understanding of the features in the data, which is especially relevant if you did not record it yourself. The visual summary mode can be very fast and efficient, which is especially important for datasets that have many channels or that are very long.

Furthermore, the schematic outline shows that we might have to cycle back to **[ft_rejectvisual](/reference/ft_rejectvisual)** or **[ft_databrowser](/reference/ft_databrowser)** in case we identify atypical artifacts or bad channels _after_ having done the ICA. In that case we iterate the initial cleaning and repeat the ICA.

## Preprocessing

The MEG data is recorded with a 151-channel CTF system. Although the data is continuous, the CTF dataset is organized in trials of 10 seconds. As there are no discontinuities between trials, we can treat it as a continuous recording.

To load this dataset into MATLAB and preprocess with FieldTrip, use:

    cfg            = [];
    cfg.dataset    = 'ArtifactMEG.ds';
    cfg.continuous = 'yes'; % see https://www.fieldtriptoolbox.org/faq/continuous/
    cfg.hpfilter   = 'yes';
    cfg.hpfreq     = 0.1; % this is for later segmenting, see below
    cfg.hpfiltord  = 2;
    cfg.channel    = {'MEG', 'MEGREF', 'EOG', 'ECG', 'jaw', 'neck'};
    data = ft_preprocessing(cfg);

The ICA decomposition can take a long time, especially if you have to do it multiple times. If it takes too long, you can consider to downsample the data to a lower sampling rate, here from 1200Hz to 300Hz. Using the downsampled dataset you can estimate the ICA components and subsequently remove those from the original data. However, you should be aware that downsampling potentially affect some data features and artifacts. For example, high frequency muscle artifacts will be less well captured. The consequence is that the removal of those artifacts might also be less optimal.

    data_orig = data;

    cfg              = [];
    cfg.resamplefs   = 300;
    cfg.detrend      = 'no';
    data = ft_resampledata(cfg, data_orig);

For the purpose of this tutorial and since we want you to try out various settings, we will continue with the downsampled data. If you apply this on your own data, please do try to work with the original instead the downsampled data; that will improve the quality of the decomposition.

## Rejecting atypical artifacts

ICA assumes a mixing of stationary components and cannot estimate more components than the number of channels. If you have a few infrequent and atypical artifacts, these will be represented in components. This comes at the cost of loosingsome components for the interesting stuff, and may lead to a suboptimal decomposition. Hence we firrst want to remove sparse atypical artifacts.

### Using ft_databrowser

We can use **[ft_databrowser](/reference/ft_databrowser)** to have a look at the data. Since we are looking at infrequent artifacts that might happen anywhere in the data, we should look at _all_ channels and at the _complete_ time course. It helps to "zoom out" for the time, so that we see a large time window of the data at once.

    cfg                 = [];
    cfg.continuous      = 'yes; % this can also be used on trial-based data to paste them together
    cfg.blocksize       = 60;   % show 60 seconds at the time
    cfg.plotevents      = 'no';
    cfg.preproc.demean  = 'yes';
    cfg.layout          = 'CTF151.lay';
    cfg = ft_databrowser(cfg, data);

    % remember the time of the artifacts
    cfg_artfctdef = cfg.artfctdef;

Note that we are interested in the output `cfg` of **[ft_databrowser](/reference/ft_databrowser)**: that will contain the artifacts that we have marked.

{% include image src="/assets/img/tutorial/ica_artifact_cleaning/figure2.png" width="600" %}

All the way at the end of the recording something weird is happening: the CTF acquisition software writes data in blocks of 10 seconds. If the acquisition is ended prior to the last block being complete (which is always the case), the remainder of that block will be written to disk as all zeros. Hence you should mark the last section of the data as an artifact.

In channel MLT024 (and simultaneously at some others) you can observe so-called SQUID jumps. These are the consequence of a hardware instability in the SQUID, causing a large change of one flux quantum in the signal. These show up as large jumps. Identify each of the jumps in MLT024 and mark it as an artifact.

For reference, these are the artifacts that I identified in the downsampled data:

    >> cfg.artfctdef.visual.artifact
    ans =
      196859      230777
      257741      283558
      333814      361770
      862239      912000

and this is the time in seconds at which they happen in the continuous recording:

    >> mean(cfg.artfctdef.visual.artifact, 2)/data.fsample
    ans =
      178.1817
      225.5412
      289.8267
      739.2663

Note that the jumps are easier to identify if you would not have applied a high-pass filter at the initial preprocessing and if we would not have downsampled the data. Especially the high-pass filter is a bit annoying here: it spreads the jumps over a much longer time range.

#### Exercise

{% include markup/skyblue %}
Preprocessing and filtering serves to reduce artifacts (such as drifts) and hence makes artifacts less visible. Unpreprocessed data gives the best representation of the artifacts.

Repeat the inspection with ft_databrowser on the original data, without high-pass filter and without resampling. That requires that you have to call ft_preprocessing again. Look at the channels that start with `MTL*` around 178 seconds into the recording and compare the jump to the one you observed in the filtered and downsampled data.

Be aware that artifacts (and trials) are expressed in samples, so you can look at the same time in the recording, but you cannot refer to the artifacts in the original and downsampled data using the same sample numbers.
{% include markup/end %}

Following the identification of atypical artifacts, you can remove them from further analysis. For the purpose of this tutorial and working on continuous data, we will not reject them but rather fill them with NaNs (not-a-number values). It is also possible on the continuous data to use **[ft_rejectartifact](/reference/ft_rejectartifact)** with the option `cfg.artfctdef.reject = 'partial'`. Here we will use the option `nan`.

    cfg                   = [];
    cfg.artifactdef       = cfg_artfctdef;
    cfg.artfctdef.reject  = 'nan';
    data_clean = ft_rejectartifact(cfg, data);

{% include markup/yellow %}
Note that here we are reusing the `data` and the `data_clean` variables in different ways, as we are going back ant forth demonstrating different ways of processing and cleaning the data. Don't get confused with what the clean data represents.

To get back to the original data, you can always do `data = data_orig`.
{% include markup/end %}

### Using ft_rejectvisual

Another strategy to remove infrequent and atypical artifacts is to use **[ft_rejectvisual](/reference/ft_rejectvisual)**. However, this requires the data to be segmented in trials. In this case we can segment the data in a continuous stream of one-second segments.

Note that here we are relying on the `cfg.hpfilter='yes'` option during preprocessing. The low-frequency drift in the signal is of no interest and affects the ICA decomposition; hence we want to get rid of that anyway. Since we are working with continuous data, we use a high-pass filter. Had we started off with trial-based data, then `cfg.demean='yes'` at the stage of the very first preprocessing would have been an simpler option.

    cfg         = [];
    cfg.length  = 1;
    cfg.overlap = 0;
    data_segmented = ft_redefinetrial(cfg, data);

Now that the data is cut into segments (aka trials) of a second each, we can identify the segments that have atypical artifacts. For that we use **[ft_rejectvisual](/reference/ft_rejectvisual)** with the summary method. This  directly returns the cleaned data. Since we don't want to exclude any channels from further analysis, we specify that we want to keep all channels. Since we want the data again to be continuously represented later on, we specify that artifacts are to be replaced by NaNs.

    cfg             = [];
    cfg.method      = 'summary';
    cfg.keepchannel = 'yes';
    cfg.keeptrial   = 'nan';
    cfg.channel     = {'MEG', 'MEGREF'};
    cfg.layout      = 'CTF151.lay';
    data_segmented_clean = ft_rejectvisual(cfg, data_segmented);

{% include image src="/assets/img/tutorial/ica_artifact_cleaning/figure3.png" width="600" %}

We can now "stitch" the segmented data back together in a continuous representation:

    cfg = [];
    cfg.continuous = 'yes';
    data_clean = ft_redefinetrial(cfg, data_segmented_clean);

If you inspect `data_clean`in ft_databrowser, you will see that parts of the data are not visible, those are replaced by NaNs.

## ICA decomposition

We use **[ft_componentanalysis](/reference/ft_componentanalysis)** for the ICA decomposition. It has many options, and supports different methods for decomposing the data, including PCA and different ICA algorithms. Here we will be using the Extended Infomax algorithm using the `runica` method from EEGLAB. You do not have to have EEGLAB installed for this, the required functions are included in the `fieldtrip/external` directory.

{% include markup/green %}
There are other ICA algorithms that you can consider. For example, the `fastica` algorithm is fast and does not need to do a complete decomposition of the data; it can also identify a few components only. The components that fastica identifies first are the components with the largest variance, these are often the artifacts. The `amica` algorithm is among the best algorithms for identifying biophysically plausible ICA components. It results in components that are _more_ independent than `runica`.

The paper Delorme et al. [Independent EEG sources are dipolar.](https://doi.org/10.1371/journal.pone.0030135) PLoS One (2012) compares many ICA algorithms and concludes that more independent components are also more dipolar, which is compatible with an interpretation of many maximally independent EEG components as being volume-conducted projections of partially-synchronous local cortical field activity within single compact cortical domains.

Another strategy for component analysis that is not completely blind is "denoising source separation" or `dss`, a method in which specific explicit features are maximized during the ICA decomposition. If you know how your EOG or ECG artifacts look like in advance, you can use `dss` to capitalize on that and efficiently clean the data.
{% include markup/end %}

To perform the ICA decomposition, you can use the following code. Here we use a PCA reduction of the data prior to the decomposition to speed up the processing for the purpose of this tutorial. Note that the PCA reduction can negatively affect the quality of the decomposition, so in general it is better to have some more patience when the computation runs through.

    % with 10 components and 300Hz it takes about 55 seconds on my computer
    % with 20 components and 300Hz it takes about 165 seconds
    % with 30 components and 300Hz it takes about xxx seconds

    cfg              = [];
    cfg.method       = 'runica';
    cfg.numcomponent = 20;
    cfg.channel      = {'MEG', 'MEGREF'};
    data_comp = ft_componentanalysis(cfg, data_clean); % using the data without atypical artifacts

You should do similar way and that together represent a linear mixture of the underlying sources. If you have EEG and EOG channels that are recorded using the same reference, the EEEG and EOG channels can goin there together. If you have EEG relative to one reference and bipolar EOG channels, you should not combine them in a single ICA decomposition. When you have combined MEG and EEG data, the MEG and EEG channels will both see the brain and artifactual sources, but have different sensitivity to them and to effects due to movement of the head relative to the MEG helmet; in that case we also recommend to use the ICA separately on the MEG and on the EEG channels.

## Identifying artifactual components

The decomposed data structure `data_comp` represents the topographies of the components, i.e. how each source projects to the channels, and represents the temporal activation of each source. These can both be used to identify components that correspond to artifacts.

    cfg           = [];
    cfg.layout    = 'CTF151.lay';
    cfg.component = 1:20;
    cfg.marker    = 'off';
    ft_topoplotIC(cfg, data_comp)

{% include image src="/assets/img/tutorial/ica_artifact_cleaning/figure4.png" width="600" %}

With some experience, you can relatively quickly identify components that are suspect for artifacts. Eye-related components are spatially localized on the frontal channels, blinks and vertical saccades are symmetric and horizontal saccades show a distinct left-right pattern. Heart-related components in MEG show up as a very deep source with a bipolar projecting over the left and right side of the helmet. It is common for both eye and heart components that you will see a few of them. You may want to write down the number of each of the suspect components.

In the figure above, components 10 and 12 look like eye-related components. Component 5 and 6 probably still relate to the SQUID jumps on MLT24 and neighbouring channels. In this case there are no obvous heart-related component visible

Subsequently you can look at the time course of the components. The heart-related components will show a regular heartbeat that you should be able to recognize already in the first few seconds of the decomposition. The eye-related components only show deflections in the time series if the subject blinks or makes a saccade; to see those you probably have to scroll though the data or to zoom out to see a larger piece of data.

    cfg = [];
    cfg.viewmode  = 'component';
    cfg.layout    = 'CTF151.lay';
    cfg.blocksize = 45;
    ft_databrowser(cfg, data_comp);

{% include image src="/assets/img/tutorial/ica_artifact_cleaning/figure5.png" width="600" %}

Again you write down the components that represent artifacts.

Note that due to eye components in MEG look different than eye components in EEG, that is due to the orientation of the MEG channels: on the left side of the head the channels point to the right and on the right side they point to the left, this cause their "polarity" to flip. With EEG electrodes all frontal electrodes have the same polarity. In combination with the component time series you can figure out which component reflects horizontal movements and which reflects blinks.

## Identifying bad channels

Both EEG and MEG give a relatively blurry representation of the physiological activity. Components that are very localized in space, i.e., that are only active on a single of very few channels, are not likely to represent physiological sources in the brain or from the heart. If you would not have removed the SQUID jumps earlier, those would show up as very localized artifacts. EEG electrodes that move or that have a sudden change in impedance can also show up as very localized.

If that happens, you can use ft_databrowser on the component time series to identify when the jump or other short-lived artifact lives, you can bark the time window as visual artifact, andusing the output `cfg` of ft_databrowser you can goback and remove that section from the data prior to ICA decomposition (or fill that section with NaNs as we did here). Subsequently, you would redo the ICA decomposition and once more check the cpomponent topographies and time series.

It can also happen that you find one or a few componens that are very localized in space due to the corresponding channels being bad or noisy over a long time segment. In that case you will want to reject those channels from your data and to do the ICA decomposition and backprojecting without those channels. If many of your participants have bad channels, and/or if those bad channels are very varying over participants, you may want to interpolate those channels using **[ft_channelrepair](/reference/ft_channelrepair)**; this is something you would do _after_ the backprojection of the components to get clean channel-level data, but _prior_ to doing time-locked ERP or frequency/time-frequency analysis.

With high-density EEG, you may sometimes see very localized muscle twitches, especially over the temporal region but possibly also elsewhere over the scalp. These can be less or more frequent, depending on your participant and task. Although these are spatially quite compact, they do represent a physiological source and ICA is an appropriate technique to remove them.

## Removing artifactual components

After identification of the artifactual components you can use **[ft_rejectcomponent](/reference/ft_rejectcomponent)** to back-project all components to the channel-level representation of the data, excluding the artifacts.

    cfg = [];
    cfg.component = [10 12]; % to be removed
    data_clean = ft_rejectcomponent(cfg, comp)

If you have computed the components on a resampled version of the data, you can also use **[ft_rejectcomponent](/reference/ft_rejectcomponent)** to project the artifacts out of the original data. That only requires the component topographies, which are then applied to unmix and re-mix the data at the original sampling rate.

    cfg = [];
    cfg.component = [10 12]; % to be removed
    data_orig_clean = ft_rejectcomponent(cfg, comp, data_orig)

## Summary and conclusion

In this tutorial we have looked at how to prepare your data for ICA decomposition, how todeal with infrequent and atypical artifacts. We shortly discussed different ICA approaches and, using a specific approach, show how you can speed up your ICA by downsampling the data and by reducing the number of components that are estimated. Given the ICA decomposition we demonstrated how to visualize them and identify the artifacts, and discussed that - if you get very focal components (in space and/or in time) you might want to remove that part of your data and start again. After obtaining a clean ICA decomposition, we explained how to back-project the components to a channel-level representation for further analysis or how to use the components to clean the original data.

What we _did not_ show in this tutorial is that you can also interpret the ICA components as sources in the brain. Just as it is possible to use all FieldTrip plotting and analysis strategies on artifactual components, it is also possible to analyze the brain components. All of the components are represented as channel time-series and all channel-level analyses can be applied. For example, following segmentation of your data in stimulus-locked trials, you can use **[ft_timelockanalysis](/reference/ft_timelockanalysis)**, **[ft_freqanalysis](/reference/ft_freqanalysis)** or **[ft_componentanalysis](/reference/ft_componentanalysis)** to investigate each of the components of interest and to use statistics to compare them between conditions.

The decomposition not only gives you the component time-series but also their topography. Besides using these to identify artifacts, you can also cleary recognize components that represent activity in the brain. You can use **[ft_dipolefitting](/reference/ft_dipolefitting)** to localize these components with simple dipole models, or **[ft_sourceanalysis](/reference/ft_sourceanalysis)** to localize them with distributed models. The only source reconstruction strategy that you cannot apply (easily) is beamforming, since at the component-level you only have a single topography, but no data covariance matrix. As a spatial filtering technique, beamforming is too similar to independent component analysis (although based on a biophysical model and the assumption of uncorrelated rather than independent sources).

## Suggested further reading

For an introduction to how you can deal with artifacts in FieldTrip in general, you should have a look at the [Introduction: dealing with artifacts](/tutorial/preproc/artifacts) tutorial. After this tutorial on cleaning your data using ICA, you may want to go back to the [visual artifact rejection](/tutorial/preproc/visual_artifact_rejection) and the [automatic artifact rejection](/tutorial/preproc/automatic_artifact_rejection) tutorials.

More information on dealing with artifacts can also be found in some example scripts and frequently asked questions. Furthermore, this topic is often discussed on the [email discussion list](/discussion_list) which can be searched [like this](https://www.google.com/search?q=site%3Amailman.science.ru.nl%2Fpipermail%2Ffieldtrip&q=artifacts).

#### Example scripts

{% include seealso category="example" tag1="artifact" %}

#### Frequently asked questions

{% include seealso category="faq" tag1="artifact" %}
