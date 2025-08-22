---
title: Introduction on dealing with artifacts
category: tutorial
tags: [artifact, preprocessing, eeg, meg]
redirect_from:
    - /tutorial/artifacts/
---

# Introduction on dealing with artifacts

This tutorial explains the general approach on how to deal with artifacts.

{% include markup/red %}
Since FieldTrip supports the data of many different acquisition systems, the particular artifacts in your data might behave very different from the examples demonstrated and discussed here. Therefore you should be aware of the different approaches and of the variability of artifact rejection (automatic/manual) procedures described onwards.

At the end of an automated procedure, consider always to visual inspect your data, after rejection.
{% include markup/end %}

## Background

Generally speaking, an artifact (American English spelling) or artefact (British English spelling) is some unexpected or unwanted feature in the data that we acquired with our EEG or MEG system. Artifacts can be physiological or non-physiological in origin.

An eyeblink is an example of a physiological artifact that shows up in the EEG. The retina is electrically charged and the movement of the eye causesa a deflection of the scalp potential. The contribution of this so-called electrooculogram is mainly visible on frontal  electrodes, but when looking carefully enough, you can see it on all electrodes. An example of a non-physiological artifact is an EEG electrode that has poor contact with the scalp. The corresponding EEG channel will show a flat line, or potentially a lot of noise.

Besides considering the physiological or non-physiological aspect of the artifact, you can also think about whether the artifact is caused by the behavior of the participant (e.g., an eye movement), whether it is caused by something in the environment (e.g., 50Hz line noise) or whether it is caused by a malfunction of the equipment (e.g., a poorly attached electrode). Behavioral artifacts are typically short-lived, whereas environmental and instrumentation artifacts are typically more persistent.

There is not a single most optimal manner to detect the artifacts: it depends on the data properties, the type of artifacts that you anticipate to be present (given your recording setup, your task, and your participants) and your own preferences.

## How does FieldTrip manage artifacts?

FieldTrip deals with artifacts by first identifying them, and subsequently removing them. Detection of artifacts can be done visually, or using automatic routines, or a combination of both. After you know what the artifacts are, they are removed by either

- rejecting the piece of data containing the artifact, e.g., for a short-lived artifact or poorly attached EEG electrode, or
- subtracting the spatio-temporal contribution of the artifact from the data, e.g., using a filter or ICA

The functions in FieldTrip that you can use for artifact detection depend on whether your data is continuous or trial-based (i.e. segmented with time gaps between the segments) and whether your data is stored on disk or already read into memory.

Detecting the artifacts in continuous data _prior to segmenting_ allows you to apply filters (e.g., a band-pass filter to zoom in on the muscle artifacts on the temporal channels) without having to worry about edge effects due to the filter (i.e. filter ringing). Having the data in memory _after segmenting_ is an efficient way of visually browsing through the data segments of interest, especially if you know that there are artifacts in between the trials (e.g., EOG artifacts in the blink period).

Detecting the artifacts without reading the complete data into memory allows you to work with datasets that are too large to fit in memory all at once.

## Rejecting segments with artifacts

With this strategy, pieces of data contaminated by artifacts are identified and removed from further analysis. For example, a bad channel is excluded, or trials with artifacts are removed. You may want to use this strategy not only to deal with the artifact, but also to deal with undesired behaviour of your participant. For example if in a visual stimulus-detection task the subject blinks exactly at the moment that the (short) stimulus appears on screen, chances are that they did not see the stimulus. In that case the reason to exclude the trial is not because of the EOG artifact, but because of the subject's brain activity in that trial not being of interest.

### Manual/visual detection

In manual/visual artifact detection, the user visually inspects the data and identifies the trials or data segments and/or channels that are affected. The visual inspection results in a list of noisy data segments and/or channels.

These functions are available for manual/visual artifact detection:

- **[ft_rejectvisual](/reference/ft_rejectvisual)**
- **[ft_databrowser](/reference/ft_databrowser)**

The **[ft_rejectvisual](/reference/ft_rejectvisual)** function works only for segmented data (i.e. trials) that have already been read into memory. It allows you to browse through the large amounts of data in a MATLAB figure by showing all channels at once (per trial), or by showing all trials at once (per channel), or by showing a summary of all channels and trials in a single figure. Using the mouse, you can select trials and/or channels that are to be removed. This function directly returns the data with the noisy parts removed and you don't have to call **[ft_rejectartifact](/reference/ft_rejectartifact)** or **[ft_rejectcomponent](/reference/ft_rejectcomponent)**.

{% include markup/skyblue %}
If you want to use **[ft_rejectvisual](/reference/ft_rejectvisual)** on continuous data, you can first segment it in one-second pieces using **[ft_redefinetrial](/reference/ft_redefinetrial)** and then call ft_rejectvisual. Segmenting continuous data is explained in [this FAQ](/faq/how_can_i_process_continuous_data_without_triggers).
{% include markup/end %}

The **[ft_databrowser](/reference/ft_databrowser)** function works both for continuous and segmented data, and works with the data either still on disk or already read into memory. It allows you to browse through the data and to mark with the mouse segments with an artifact.  Contrary to ft_rejectvisual, ft_databrowser does not return the cleaned data and also does not allow you to delete bad channels (though you can switch them off from visualization). Instead it returns in the output `cfg` a list of segments, expressed as begin and end sample relative to the recording. After detecting the segments with the artifacts, you call **[ft_rejectartifact](/reference/ft_rejectartifact)** to remove them from your data (when the data is already in memory) or from your trial definition (when the data is still on disk).

Noteworthy is that the **[ft_databrowser](/reference/ft_databrowser)** function can also be used to visualize the time course of the ICA components and thus easily allows you to identify the components corresponding to eye blinks, heart beat and line noise. A good ICA unmixing of your data requires that the atypical artifacts (e.g., electrode movement, squid jumps) are removed **prior** to calling **[ft_componentanalysis](/reference/ft_componentanalysis)**. After you have determined what the bad components are, you can call **[ft_rejectcomponent](/reference/ft_rejectcomponent)** to project the data back to the sensor level, excluding the bad components.

More information about manually dealing with artifacts is found in the [visual artifact rejection](/tutorial/visual_artifact_rejection) tutorial.

### Automatic detection

To speed up the processing of many and/or large datasets, and to facilitate the use of objective criteria for artifacts, FieldTrip also includes a number of functions for automatic artifact detection. Although these work efficiently for well-known artifacts in well-behaved data, you should **not** use the automatic detection functions as your default method if you do not (yet) know your data that well.

The automatic artifact detection functions allow to apply some filtering and preprocessing of the data to make the artifacts more visible. The relevant parameters for this are set _a priori_ for each of them via the `cfg` structure.

These functions are available for automatic artifact detection:

- **[ft_artifact_clip](/reference/ft_artifact_clip)**
- **[ft_artifact_ecg](/reference/ft_artifact_ecg)**
- **[ft_artifact_threshold](/reference/ft_artifact_threshold)**
- **[ft_artifact_eog](/reference/ft_artifact_eog)**
- **[ft_artifact_jump](/reference/ft_artifact_jump)**
- **[ft_artifact_muscle](/reference/ft_artifact_muscle)**
- **[ft_artifact_zvalue](/reference/ft_artifact_zvalue)**
- **[ft_badchannel](/reference/ft_badchannel)**
- **[ft_badsegment](/reference/ft_badsegment)**

The functions to detect eog, jump and muscle artifacts are all just wrappers around **[ft_artifact_zvalue](/reference/ft_artifact_zvalue)** where the filter and padding options are set to reasonable defaults. The **[ft_artifact_zvalue](/reference/ft_artifact_zvalue)** computes a preprocessed representation of each channel, converts it into z-values by subtracting the channel mean and dividing by its standard deviation, and then sums the z-values over channels. This works well for artifacts that are expected to be present in multiple channels, such as eye blinks and muscle activity.

The **[ft_badchannel](/reference/ft_badchannel)** and **[ft_badsegment](/reference/ft_badsegment)** functions implement the same metrics as the **[ft_rejectvisual](/reference/ft_rejectvisual)** function with `cfg.method='summary'` and allow setting fixed a-priori thresholds to exclude channels or segments.

More information can be found in the [automatic artifact rejection](/tutorial/automatic_artifact_rejection) tutorial.

### Rejecting segments with artifacts from the data

If you use either manual/visual or automatic detection of artifactual segments, you usually would proceed to reject those segments from subsequent analysis with **[ft_rejectartifact](/reference/ft_rejectartifact)**. FieldTrip supports variable trial length data, which allows you to reject only those pieces of data containing the artifact, keeping the rest of the trial. This is especially useful if your experiment consists of very long trials.

### Rejecting channels with artifacts from the data

If you have identified channels that are bad, you can exclude them from subsequent processing by specifying them in the `cfg.channel` option. Rather than specifying all channels you want to keep, you can also specify explicit channels that you want to remove like this

    cfg.channel = {'all', '-P7', 'T8'};

## Subtracting the artifacts from the data

Rather than excluding segments with artifacts, in some cases you can assume that the artifact is a linear addition to the signal of interest. If you arte able to identify the artifact, you can subtract it, leaving you with the EEG or MEG signal of interest. This works well for certain types of artifacts, such as high frequency noise in EEG, or line noise at 50 or 60 Hz. This also can be used to remove the contribution of eye movements to EEG data, assuming that the eye blinks and movements are not a problem for the correct execution of the task.

### Using filters to remove artifacts

Some artifacts are represented in specific frequency bands. For example, artifacts can show up in low frequencies due to electrode drift, or at high frequencies where you do not expect EEG activity of interest, or at very specific frequencies, like 50 Hz line noise. You can use a filter in **[ft_preprocessing](/reference/ft_preprocessing)** to remove these artifactual contributions to the data.

### Using ICA to identify and remove artifacts

You can make a linear decomposition of the data using independent component analysis (ICA) or principal component analysis (PCA). With these methods you apply  a set of spatial filters to the data, after which the data is no longer represented at the level of recorded (scalp) channels, but as a set of virtual channels or components. In the case of ICA decomposition, the filters are chosen to produce maximally independent time courses of the components. In the case of PCA, the filters produce orthogonal time courses. Certain artifacts, such as those caused by eye blinks, are often reflected by a few components which are fairly easy to identify. These visually identified components can then be removed from the data and the remaining components can be projected back to the channel level with **[ft_rejectcomponent](/reference/ft_rejectcomponent)**.

The following example scripts explain how to use ICA to detect and remove [EOG](/example/ica_eog) and [ECG](/example/ica_ecg) artifacts.

## Suggested further reading

Following this short introduction on dealing with artifacts in FieldTrip, you can continue with the [visual artifact rejection](/tutorial/visual_artifact_rejection) and the [automatic artifact rejection](/tutorial/automatic_artifact_rejection) tutorials. More information on dealing with artifacts can also be found in some example scripts and frequently asked questions. Furthermore, this topic is frequently discussed on the [email discussion list](/discussion_list).

### Example scripts

{% include seealso category="example" tag1="artifact" %}

### Frequently asked questions

{% include seealso category="faq" tag1="artifact" %}
