---
title: Visual or manual artifact rejection
tags: [tutorial, artifact, meg, raw, preprocessing, meg-language]
---

# Visual or manual artifact rejection

## Introduction

This tutorial makes use of the preprocessed data from the [preprocessing tutorial](/tutorial/preprocessing). Run the script from that section in order to produce the single trial data structure, or download [PreprocData.mat](https://download.fieldtriptoolbox.org/tutorial/visual_artifact_rejection/PreprocData.mat). Load the data into MATLAB memory with the following command:

    load PreprocData data_all

## Background

For a successful analysis of EEG or MEG signals you want to have "clean" data. That means that you should try to reduce the variance in the data due to factors that you cannot influence. One of those factors is the presence of artifacts in the data. These artifact can be physiological, can relate to the behaviour of the subject, or can result from the acquisition electronics or environmental sources. The strongest physiological artifacts stem from eye blinks, eye movements and head movements. Muscle artifact from swallowing and neck contraction can be a problem as well. Artifacts related to the electronics are for example 'SQUID jumps' in MEG.

In general it is best to avoid artifacts during the recording. You can instruct the subject not to blink during the trial, and instead give him some well-defined time between the trials in which he is allowed to blink. But of course there will always be some artifacts in the raw data.

While detecting artifacts by visual inspection, keep in mind that it is a subjective decision to reject certain trials and keep other trials. Which type of artifacts should be rejected depends on the analysis you would like to do on the clean data. If you would like to do a time-frequency analysis of power in the gamma band it is important to reject all trials with muscle artifacts, but for a ERF analysis it is more important to reject trials with drifts and eye artifacts.

In visual artifact detection, the user visually inspects the data and identifies the trials or data segments and the channels that are affected and that should be removed. The visual inspection results in a list of noisy data segments and channels.

The functions that are available for visual artifact detection are

- **[ft_rejectvisual](/reference/ft_rejectvisual)**
- **[ft_databrowser](/reference/ft_databrowser)**

The **[ft_rejectvisual](/reference/ft_rejectvisual)** function works only for segmented data (i.e. trials) that have already been read into memory. It allows you to browse through the large amounts of data in a MATLAB figure by either showing all channels at once (per trial) or showing all trials at once (per channel) or by showing a summary of all channels and trials. Using the mouse, you can select trials and/or channels that should be removed from the data. This function directly returns the data with the noise parts removed and you don't have to call **[ft_rejectartifact](/reference/ft_rejectartifact)** or **[ft_rejectcomponent](/reference/ft_rejectcomponent)**.

The **[ft_databrowser](/reference/ft_databrowser)** function works both for continuous and segmented data and also works with the data either on disk or already read into memory. It allows you to browse through the data and to select with the mouse sections of data that contain an artifact. Those time-segments are marked. Contrary to **[ft_rejectvisual](/reference/ft_rejectvisual)**, the **[ft_databrowser](/reference/ft_databrowser)** function does not return the cleaned data and also does not allow you to delete bad channels (though you can switch them off from visualization). After detecting the time-segments with the artifacts, you should call **[ft_rejectartifact](/reference/ft_rejectartifact)** to remove them from your data (when the data is already in memory) or from your trial definition (when the data is still on disk).

Noteworthy is that the **[ft_databrowser](/reference/ft_databrowser)** function can also be used to visualise the timecourse of the ICA components and thus easily allows you to identify the components corresponding to eye blinks, heart beat and line noise. Note that a proper ICA unmixing of your data requires that the atypical artifacts (e.g., electrode movement, squid jumps) are removed **prior** to calling **[ft_componentanalysis](/reference/ft_componentanalysis)**. After you have determined what the bad components are, you can call **[ft_rejectcomponent](/reference/ft_rejectcomponent)** to project the data back to the sensor level, excluding the bad components.

## Procedure

The following steps are used for visual artifact rejection

- Read the data into MATLAB using **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)**, as explained in the [preprocessing tutorial](/tutorial/preprocessing)
- Visual inspection of the trials and rejection of artifacts using **[ft_rejectvisual](/reference/ft_rejectvisual)**
- Alternatively you can use **[ft_databrowser](/reference/ft_databrowser)** and mark the artifacts manually by interactively paging trial by trial

### Manual artifact rejection - display one trial at a time

The function **[ft_rejectvisual](/reference/ft_rejectvisual)** provides various ways of identifying trials contaminated with artifacts.

The configuration option `cfg.method` provides the possibility of browsing through the data channel by channel with `cfg.method= 'channel'`, trial by trial with `cfg.method = 'trial'` or displaying all the data at once with `cfg.method = 'summary'`. The field `cfg.latency` determines the time window of interest with respect to the trigger signals. In the example below the whole trial is inspected as the latency is by default the whole trial).

The scaling of the plots is automatically adjusted according to the maximum amplitude over all channels. The scaling can be set using `cfg.ylim`. For EOG/EEG channels `cfg.ylim=[-50e-6 50e-6]` (50 micro Volt) is a useful scale and for the MEG channels `cfg.ylim=[-1e-12 1e-12]` (1 pT).

To browse through the data trial by trial while viewing all channels write:

    cfg          = [];
    cfg.method   = 'trial';
    cfg.ylim     = [-1e-12 1e-12];
    dummy        = ft_rejectvisual(cfg, data_all);

Click through the trials using the `>` button to inspect each trial.

If your dataset contains MEG and ExG channels like this dataset, the MEG and ExG channels are scaled differently when using only `cfg.ylim` (the ExG channels show up as big black bars on the screen). One of the reasons to record ExG (i.e., EOG, EMG or ECG) is to check these channels while identifying eye, muscle and heart artifacts. The following code can be used to scale MEG and ExG channels both properly:

    cfg          = [];
    cfg.method   = 'trial';
    cfg.ylim     = [-1e-12 1e-12];
    cfg.megscale = 1;
    cfg.eogscale = 5e-8;
    dummy        = ft_rejectvisual(cfg, data_all);

In trial 46 notice the slower drift observed over a larger group of sensors. This is most likely due to a head movement.

{% include image src="/assets/img/tutorial/visual_artifact_rejection/figure1.png" width="600" %}

Trial 250 shows an artifact which is caused by the electronics. Notice the jump in sensor MLT41.

{% include image src="/assets/img/tutorial/visual_artifact_rejection/figure2.png" width="600" %}

By browsing artifacts become evident in the trials 2, 5, 6, 8, 9, 10, 12, 39, 43, 46, 49, 52, 58, 84, 102, 107, 114, 115, 116, 119, 121, 123, 126, 127, 128, 132, 133, 137, 143, 144, 147, 149, 158, 181, 229, 230, 233, 241, 243, 245, 250, 254, 260. They should be marked as 'bad'. After pressing the 'quit' button the trials marked 'bad' are now removed from the data structure.

If you would like to keep track of which trials you reject, keep in mind that the trial numbers change when you call **[ft_rejectvisual](/reference/ft_rejectvisual)** more than once. An example: There are 261 trials in your data and first you reject trial 2, 5 and 6. Then trial number 8 becomes trial number 5. Later when you also want to reject more trials you should be very careful and subtract 3 from all the old trial numbers. If you would like to know which trials you rejected, it is best to call **[ft_rejectvisual](/reference/ft_rejectvisual)** only once.

### Manual artifact rejection - display one channel at a time

It can also be convenient to view data from one channel at a time. This can be particularly relevant for the EOG channel. To do so, write:

    cfg          = [];
    cfg.method   = 'channel';
    cfg.ylim     = [-1e-12 1e-12];
    cfg.megscale = 1;
    cfg.eogscale = 5e-8;
    dummy        = ft_rejectvisual(cfg, data_all);

Click through the data using the `>` button. While clicking through all the trials you see that channels MLO12 and MLP31 contain a lot of artifacts (see the figure below ). They should be marked as 'bad'. After pressing the 'quit' button the channels marked 'bad' are now removed from the data structure.

{% include image src="/assets/img/tutorial/visual_artifact_rejection/figure3.png" width="600" %}

### Manual artifact rejection - display a summary

To produce an overview of the data choose the cfg.method 'summary':

    cfg          = [];
    cfg.method   = 'summary';
    cfg.ylim     = [-1e-12 1e-12];
    dummy        = ft_rejectvisual(cfg, data_all);

This gives you a plot with the variance for each channel and trial.

{% include image src="/assets/img/tutorial/visual_artifact_rejection/figure4.png" width="600" %}

You should note that there is one channel which has a very high variance. That is the EOG channel, which contains numbers in uV which are of a very different order of magnitude than all MEG channels in T. Toggling the EOG channel will also change the figure with the maximal variance per trial (second row, left) a lot. Then you only see the variance in each trial in the MEG channels.

The command window allows for toggling trials and channels on and off. The first choice could be of toggling channels off. Enter either a channel number or its name in the edit box and enter it again to toggle it back on.

Alternatively use the mouse directly to toggle (e.g.) channels off as following: drag the mouse on the top right panel, and include the rightmost dot in the selection box. In a couple of successive steps remove the 4 channels with bigger variance and press 'quit'.

Before pressing the 'quit' button, you can always toggle the channels/trials back on, by using the edit boxes 'toggle trial' or 'toggle channel'.

{% include image src="/assets/img/tutorial/visual_artifact_rejection/figure5.png" width="600" %}

After quitting, the trials/channels will be rejected from the data set and the command line output appears as follows:

    the input is raw data with 152 channels and 261 trials
    showing a summary of the data for all channels and trials
    computing metric [---------------------------------------------------------]
    261 trials marked as GOOD, 0 trials marked as BAD
    148 channels marked as GOOD, 4 channels marked as BAD
    no trials were removed
    the following channels were removed: MLT31, MLT33, MLT41, EOG
    the call to "ft_selectdata" took 0 seconds
    the call to "ft_rejectvisual" took 243 seconds

This operation could be repeated for each of the metrics, by selecting the metric 'var', 'min', 'max', etc.

{% include markup/blue %}
The summary mode in **[ft_rejectvisual](/reference/ft_rejectvisual)** has been primarily designed to visually screen for artefacts in channels of a consistent type, i.e., only for the axial MEG gradiometers in this example.

If you have EEG data, the EOG channels have the same physical units and very similar amplitudes and therefore can be visualised simultaneously.

If you have data from a 306-channel Neuromag system, you will have both magnetometers and planar gradiometers, which have different physical units and rather different numbers. Combining them in a single visualization is likely to result in a biassed selection, either mainly relying on the magnetometers or the gradiometers being used to find artefacts.

You can use the following options in **[ft_rejectvisual](/reference/ft_rejectvisual)** to apply a scaling to the channels prior to visualization: _cfg.eegscale, cfg.eogscale, cfg.ecgscale, cfg.emgscale, cfg.megscale, cfg.gradscale_ and _cfg.magscale_.

You can also call **[ft_rejectvisual](/reference/ft_rejectvisual)** multiple times, once for every type of channels in your data. If you use _cfg.keepchannel='yes'_, channels will not be removed from the data on the subsequent calls. For example:

    cfg = [];
    cfg.method = 'summary'
    cfg.keepchannel = 'yes';

    cfg.channel = 'MEGMAG';
    clean1  = ft_rejectvisual(cfg, orig);

    cfg.channel = 'MEGGRAD';
    clean2  = ft_rejectvisual(cfg, clean1);

    cfg.channel = 'EEG';
    clean3  = ft_rejectvisual(cfg, clean2);

The previous example of calling ft_rejectvisual sequentially does not allow to exclude bad channels from the data structure. If youw ant to select both trials _and_ channels, you can use the following approach:

    % split the data over three different channel types
    cfg = [];
    cfg.channel = 'MEGMAG';
    dummy1 = ft_selectdata(cfg, orig);
    cfg.channel = 'MEGGRAD';
    dummy2 = ft_selectdata(cfg, orig);
    cfg.channel = 'EEG';
    dummy3 = ft_selectdata(cfg, orig);

    cfg = [];
    cfg.method = 'summary';
    cfg.keepchannel = 'no'; % actually this does not matter
    cfg.keeptrials = 'no';  % actually this does not matter

    % select channels and trials in each dataset
    dummy1 = ft_rejectvisual(cfg, dummy1);
    dummy2 = ft_rejectvisual(cfg, dummy2);
    dummy3 = ft_rejectvisual(cfg, dummy3);

    % make the final selection of channels and trials in the ORIGINAL data
    cfg = [];
    cfg.channel = union(dummy1.cfg.channel, dummy1.cfg.channel, dummy1.cfg.channel);
    cfg.trials  = intersect(dummy1.cfg.trials, dummy1.cfg.trials, dummy1.cfg.trials);
    clean = ft_selectdata(cfg, orig);

{% include markup/end %}

### Use ft_databrowser to mark the artifacts

An alternative way to remove artifacts is to page through the butterfly plots of the single trials, by using the **[ft_databrowser](/reference/ft_databrowser)** function. Call the function like

    % first select only the MEG channels
    cfg = [];
    cfg.channel = 'MEG';
    data_meg = ft_preprocessing(cfg, data_all);

    % open the browser and page through the trials
    cfg = [];
    cfg = ft_databrowser(cfg, data_meg);

In the image below are two figures for the same trial (trial 228). As in the left figure first drag the mouse on the artifact to create dotted lines on either side of the artifact (left image). Then, as in the right figure click within the dotted lines

{% include image src="/assets/img/tutorial/visual_artifact_rejection/figure6.png" width="600" %}

The resulting variable contains the field `cfg.artfctdef.visual.artifact` with an Nx2 matrix that represents the begin and end sample for each of the N marked sections. You can use **[ft_rejectartifact](/reference/ft_rejectartifact)** to reject the artifacts.

## Summary and conclusion

Channels MLO12 and MLP31 are removed because of artifacts.

The following trials contain artifacts:
- 2, 5, 6, 8, 9, 10, 12, 39, 43, 46, 49, 52, 58, 84, 102, 107, 114, 115, 116, 119, 121, 123, 126, 127, 128, 132, 133, 137, 143, 144, 147, 149, 158, 181, 229, 230, 233, 241, 243, 245, 250, 254, 260

With the trials split per condition, this corresponds to the following trials:
- FIC: 15, 36, 39, 42, 43, 49, 50, 81, 82, 84
- IC: 1, 2, 3, 4, 14, 15, 16, 17, 20, 35, 39, 40, 47, 78, 79, 80, 86
- FC: 2, 3, 4, 30, 39, 40, 41, 45, 46, 47, 51, 53, 59, 77, 85

## Suggested further reading

For an introduction to how you can deal with artifacts in FieldTrip in general, you should have a look at the [Introduction: dealing with artifacts](/tutorial/artifacts) tutorial. As an alternative to visual artifact detection, you can do it automatically, see the [automatic artifact rejection](/tutorial/automatic_artifact_rejection) tutorial. Furthermore, you use ICA to remove artifacts from your data, this is explained in the [cleaning artifacts using ICA](/tutorial/ica_artifact_cleaning) tutorial.

More information on dealing with artifacts can also be found in some example scripts and frequently asked questions. Furthermore, this topic is often discussed on the [email discussion list](/discussion_list) which can be searched [like this](https://www.google.com/search?q=site%3Amailman.science.ru.nl%2Fpipermail%2Ffieldtrip&q=artifacts).

#### Example scripts

{% include seealso tag1="artifact" tag2="example" %}

#### Frequently asked questions

{% include seealso tag1="artifact" tag2="faq" %}
