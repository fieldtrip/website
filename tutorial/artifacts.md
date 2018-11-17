---
title: Introduction - dealing with artifacts
layout: default
tags: [tutorial, artifact, preprocessing, eeg, meg]
toc: true
---

# Introduction: dealing with artifacts

This tutorial explains the general approach on how to deal with artifacts in FieldTrip.

{% include markup/danger %}
Since FieldTrip supports the data of many different acquisition systems, the particular artifacts in your data might behave very different from the artifata. Therefore you should be aware of the different approaches and of the variability of artifact rejection (automatic/manual) procedures described onwards.

At the end of an automated procedure, consider always to visual inspect your data, after rejection.
{% include markup/end %}

# Background: what is an artifact?

Generally speaking, an artifact (or artefact) is some unexpected or unwanted feature in the data. More specifically, it can be referred to as an undesired contribution to the brain signals that we acquired with our EEG or MEG system. Artifacts can be physiological or non-physiological in origin.

# How does FieldTrip manage artifacts?

FieldTrip deals with artifacts by first identifying them, and subsequently removing them. Detection of artifacts can be done visually, or using automatic routines (or a combination of both). After you know what the artifacts are, they are removed by

*  rejecting the piece of data containing the artifact (e.g. for a short-lived artifact)   
*  subtracting the spatio-temporal contribution of the artifact from the data (e.g. for line noise)

For the artifact detection the functions FieldTrip provides depend on whether your data is continuous or trial-based (i.e. segmented with holes between the segments) and depending on whether your data is stored on disk or already in memory.

Detecting the artifacts without reading the complete data into memory allows you to work with datasets that are too large to fit in memory all at once. Detecting the artifacts in continuous data allows you to apply filters (e.g. a band-pass filter to zoom in on the muscle artifacts on the temporal channels) without having to worry about edge effects due to the filter (i.e. filter ringing). Having the data in memory after segmenting is however a very efficient way of browsing through the data which helps in visualizing. So to conclude, there is not a single most optimal manner to detect the artifacts: it just depends on the data properties and your own preferences.

## Rejecting segments of data containing artifacts

In this type of artifact detection and rejection, pieces of data that contain artifacts are identified and removed from the data set. For example, complete trials or parts of trials, are removed entirely from the data.

### Manual/visual detection

In manual artifact detection, the user visually inspects the data and identifies the trials or data segments and the channels that are affected and that should be removed. The visual inspection results in a list of noisy data segments and channels.

The functions that are available for manual artifact detection are

* **[ft_rejectvisual](/reference/ft_rejectvisual)**
* **[ft_databrowser](/reference/ft_databrowser)**

The **[ft_rejectvisual](/reference/ft_rejectvisual)** function works only for segmented data (i.e. trials) that have already been read into memory. It allows you to browse through the large amounts of data in a MATLAB figure by either showing all channels at once (per trial) or showing all trials at once (per channel) or by showing a summary of all channels and trials. Using the mouse, you can select trials and/or channels that should be removed from the data. This function directly returns the data with the noise parts removed and you don't have to call **[ft_rejectartifact](/reference/ft_rejectartifact)** or **[ft_rejectcomponent](/reference/ft_rejectcomponent)**.

The **[ft_databrowser](/reference/ft_databrowser)** function works both for continuous and segmented data and also works with the data either on disk or already read into memory. It allows you to browse through the data and to select with the mouse sections of data that contain an artifact. Those time-segments are marked. Contrary to ft_rejectvisual, the ft_databrowser function does not return the cleaned data and also does not allow you to delete bad channels (though you can switch them off from visualisation). After detecting the time-segments with the artifacts, you should call **[ft_rejectartifact](/reference/ft_rejectartifact)** to remove them from your data (when the data is already in memory) or from your trial definition (when the data is still on disk).

Noteworthy is that the **[ft_databrowser](/reference/ft_databrowser)** function can also be used to visualise the timecourse of the ICA components and thus easily allows you to identify the components corresponding to eye blinks, heart beat and line noise. Note that a proper ICA unmixing of your data requires that the atypical artifacts (e.g. electrode movement, squid jumps) are removed **prior** to calling **[ft_componentanalysis](/reference/ft_componentanalysis)**. After you have determined what the bad components are, you can call **[ft_rejectcomponent](/reference/ft_rejectcomponent)** to project the data back to the sensor level, excluding the bad components.

More information about manually dealing with artifacts is found in the [Visual artifact rejection](/tutorial/visual_artifact_rejection) tutorial.

### Automatic detection

To speed up the processing of many or of very large datasets, and to facilitate the use of objective criteria for artifacts, FieldTrip also includes a collection of functions for automatic artifact detection. Although the automatic artifact detection algorithm works efficiently for well-known artifacts in well-behaved data, you should **not** use the automatic detection functions as your default method.

Most of the automatic artifact detection functions are based on filtering the data and subsequently  combining the data over channels. The relevant parameters for this are the various linear and non-linear filtering and the data padding options are set *a priori* for each of them via the configuration options. For example, in continuous datasets these might be the bandpass filter frequencies or the padding length.

The available functions for automatic artifact detection are:

*  **[ft_artifact_clip](/reference/ft_artifact_clip)**
*  **[ft_artifact_ecg](/reference/ft_artifact_ecg)**
*  **[ft_artifact_threshold](/reference/ft_artifact_threshold)**
*  **[ft_artifact_eog](/reference/ft_artifact_eog)**
*  **[ft_artifact_jump](/reference/ft_artifact_jump)**
*  **[ft_artifact_muscle](/reference/ft_artifact_muscle)**
*  **[ft_artifact_zvalue](/reference/ft_artifact_zvalue)**

Note that the eog, jump and muscle detection functions are all just wrappers around **[ft_artifact_zvalue](/reference/ft_artifact_zvalue)** where the filter and padding options are set to reasonable defaults.

More information about automatic detection of artifacts is found in the [Automatic artifact rejection](/tutorial/automatic_artifact_rejection) tutorial.

#### Removing artifacts from the data

If you use manual or automatic detection of time segments that contain an artifact, you usually would proceed to reject those segments from subsequent analysis with **[ft_rejectartifact](/reference/ft_rejectartifact)**. FieldTrip supports variable trial length data, which allows you to reject only those pieces of data containing the artifact, keeping the rest of the trial. This is especially useful if your experiment consists of very long trials.

## Subtracting spatial/temporal/spectral aspects of data reflecting artifacts

In this type of artifact detection and rejection, spatial/temporal/spectral aspects of the data that contain artifacts are identified and removed from the data set. For example, certain spectral components such as line noise, are subtracted from the data.

### Using ICA to identify artifacts

Another commonly used approach is to make a linear decomposition of the data using methods such as ICA (independent component analysis) or PCA (principal component analysis). These methods consist of applying a set of spatial filters to the data, after which the data is no longer represented at the level of recorded (scalp) channels, but as a set of virtual channels or components. In the case of ICA decomposition, the filters are chosen to produce the maximally temporally independent signals available in the channel-level data. Certain artifacts, such as those caused by eye blinks, are often reflected by a few components which are, with some experience, fairly easy to identify. These visually identified components can then be removed from the data and the remaining components can be projected back to the sensor level.

#### Removing artifacts from the data

If you use ICA to detect artifacts, you usually would proceed with projecting the decomposed data (excluding the artifact components) back to the sensor level. This is done with **[ft_rejectcomponent](/reference/ft_rejectcomponent)**.

The following example scripts explain how to use ICA to detect and remove [EOG](/example/use_independent_component_analysis_ica_to_remove_eog_artifacts) and [ECG](/example/use_independent_component_analysis_ica_to_remove_ecg_artifacts) artifacts.

## Suggested further reading

Following this introduction on how you can deal with artifacts in FieldTrip, you can continue with the [visual artifact rejection](/tutorial/visual_artifact_rejection) and the [automatic artifact rejection](/tutorial/automatic_artifact_rejection) tutorials. More information on dealing with artifacts can also be found in some example scripts and frequently asked questions. Furthermore, this topic is often discussed on the email discussion list which can be searched [like this](http://www.google.com/search?q=artifact&sitesearch=mailman.science.ru.nl%2Fpipermail%2Ffieldtrip%2F).

#### Example scripts

{% include seealso tag1="artifact" tag2="example" %}

#### Frequently asked questions

{% include seealso tag1="artifact" tag2="faq" %}
