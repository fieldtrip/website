---
title: Preprocessing of EEG data
tags: [eeg, brainvision, preprocessing, eeg-language, nigeria2025]
---

## Introduction

Preprocessing of MEG or EEG data refers to reading the data into memory, segmenting the data around interesting events such as triggers, temporal filtering, and optionally rereferencing in the case of EEG. The **[ft_preprocessing](/reference/ft_preprocessing)** function takes care of all these steps, i.e., it reads the data and applies the preprocessing options. Furthermore, preprocessing involves the detection and removal of artifacts, for which FieldTrip offers a number of visual and semiautomatic methods.

There is not a single preprocessing pipeline that will be optimal for all EEG datasets, as the preprocessing steps that you will take and the order of those steps depends on the experimental design and your preferences for exploring the data and identifying and dealing with the artifacts.

There are largely two alternative approaches for preprocessing, which differ in the amount of memory required in the order of the individual analysis steps. The *first* approach is to read all data from the file into memory, apply filters, and subsequently cut the data into interesting segments. The *second* approach is to first identify the interesting segments, read those segments from the data file and apply the filters to those segments only. In the remainder of this tutorial we will explore both options and see how those affect the procedure for the artifact detection.

Towards the end of this tutorial we will also look at rereferencing. Normally that would be something that we might want to do early in in the processing pipeline, since the bipolar EOG channels that we can compute in this specific EEG dataset would facilitate the detection of eye blinks. However, here we first focus on the trial-based versus continuous processing.

## The dataset used in this tutorial

The [eeg-language](/tutorial/eeg_language) dataset was acquired by Irina Siminova in a study investigating semantic processing of stimuli presented as pictures, visually displayed text or as auditory presented words. Data was acquired with a 64-channel BrainProducts BrainAmp EEG amplifier from 60 scalp electrodes placed in an electrode cap, one electrode placed under the right eye; signals "EOGv" and "EOGh" are computed after acquisition using rereferencing. During acquisition all channels were referenced to the left mastoid and an electrode placed at the earlobe was used as the ground. Channels 1-60 correspond to electrodes that are located on the head, except for channel 53 which is located at the right mastoid. Channels 61, 62, 63 are not connected to an electrode at all. Channel 64 is connected to an electrode placed below the left eye. Hence we have 62 channels of interest: 60 for the scalp EEG electrodes plus one EOGH and one EOGV channel. More details on the experiment and data can be found [here](/tutorial/eeg_language).

## Procedure

We will first explore the data to understand how it is structured. The following steps are taken to read the data, and the header details and events.

- read the continuous data using **[ft_preprocessing](/reference/ft_preprocessing)**
- visualize the continuous data using **[ft_databrowser](/reference/ft_databrowser)**
- read the continuous data using low-level functions and plot all stimulus events
- determine the trials based on the triggers using **[ft_definetrial](/reference/ft_definetrial)**
- read the segmented data using **[ft_preprocessing](/reference/ft_preprocessing)**
- average the trials to get the event-related potential using **[ft_timelockanalysis](/reference/ft_timelockanalysis)**

Subsequently, we will demonstrate a more elaborate preprocessing pipeline, both using the approach of continuous and of trial-based processing. We will start with the based approach, segmenting the data prior to filtering and artifact detection.

- determine the trials based on the triggers using **[ft_definetrial](/reference/ft_definetrial)**
- read the segmented data using **[ft_preprocessing](/reference/ft_preprocessing)** and apply some filters
- identify and remove artifacts using **[ft_rejectvisual](/reference/ft_rejectvisual)**
- average the trials to get the event-related potential using **[ft_timelockanalysis](/reference/ft_timelockanalysis)**

Subsequently, we will show the continuous approach where we do the filtering and artifact removal on the continuous data prior to segmenting and averaging.

- read the continuous data using **[ft_preprocessing](/reference/ft_preprocessing)** and apply some filters
- identify artifacts using **[ft_databrowser](/reference/ft_databrowser)**
- remove artifacts from the continuous data using **[ft_rejectartifact](/reference/ft_rejectartifact)**
- determine the trials based on the triggers using **[ft_definetrial](/reference/ft_definetrial)**
- segment the trials from the semi-continuous data using **[ft_redefinetrial](/reference/ft_redefinetrial)**

Finally, we will look at re-referencing of the EEG data and of the electrodes around the eyes to construct the EOG channels.

- compute the linked-mastoid referenced EEG data using **[ft_preprocessing](/reference/ft_preprocessing)**
- compute the horizontal and vertical bipolar EOG derivations using **[ft_preprocessing](/reference/ft_preprocessing)**
- combine the rereferenced EEG and the EOG into a single data representation using **[ft_appenddata](/reference/ft_appenddata)**

## Exploring the EEG data structure

We start by simply reading the data into memory without any further preprocessing.

    filename = 'language.vhdr';

    % read the EEG data into memory without any further preprocessing

    cfg = [];
    cfg.dataset = filename;
    data = ft_preprocessing(cfg);

This results in a MATLAB structure that has the EEG data and some descriptive fields, such as the sampling frequency, the time axis, and the channel labels.

    disp(data)

The output of **[ft_preprocessing](/reference/ft_preprocessing)** always represents the data in "trials", even if it is continuous. The data now consists of one very long trial.

    disp(data.trial)

The data is a matrix of the size Nchans by Nsamples. There is a time axis that specifies the latency of each sample.

    size(data.time{1})

The actual data of the first (and only) trial is in the trial cell-array.

    size(data.trial{1})

Note that curly brackets '{' and '}' are used to index elements from a cell-array, whereas round brackets '(' and ')' are used to index vectors and matrices (and to pass arguments to a function) and square brackets '[' and ']' are used to construct vectors and matrices.

### Plotting the data using MATLAB functions

We can make a figure and plot the data using standard MATLAB functions

    close all

    figure
    plot(data.time{1}, data.trial{1})
    xlabel('time (s)')
    ylabel('channel amplitude (uV)')
    legend(data.label)

This plots all channels and all timepoints. Since the data is a matrix, we can select a single channel (row) and only plot that.

    chansel = 1;

    figure
    plot(data.time{1}, data.trial{1}(chansel, :))
    xlabel('time (s)')
    ylabel('channel amplitude (uV)')
    legend(data.label(chansel))

The colon ':' here means "take all columns".

We can make a selection of 15 seconds of data, and plot that to further zoom in.

    timesel = 1:(500*15);

    figure
    plot(data.time{1}(timesel), data.trial{1}(chansel, timesel))
    xlabel('time (s)')
    ylabel('channel amplitude (uV)')
    legend(data.label(chansel))

The `timesel` vector specifies the samples (columns) that we take from the EEG data matrix. We take the same samples from the time vector, so that the horizontal axis remains consistent with the data

To plot 15 seconds of data elsewhere in the data matrix, for example after one minute or 60 seconds into the recording, we can shift the selected samples.

    timesel = 1:(500*15) + 60*500;

### Browsing the data prior to preprocessing

The databrowser can also be used to look at your raw or preprocessed data and annotate time windows in which specific events happen. Originally designed to identify sleep spindles, it's current main purpose is to do quality checks and visual artifact detection.

The databrowser supports three viewmodes: butterfly, vertical or component. In 'butterfly' viewmode, all signal traces will be plotted on top of each other, in 'vertical' viewmode, the traces will be below each other. The 'component' viewmode is to be used for data that is decomposed into independent components, see **[ft_componentanalysis](/reference/ft_componentanalysis)**. Components will be plotted as in the vertical viewmode, but including the coponent topography to the left of the time trace. As an alternative to these three viewmodes, if you provide a cfg.layout, then the function will try to plot your data according to the sensor positions specified in the layout.

When the databrowser opens, you will see buttons to navigate along the bottom of the screen and buttons for artifact annotation to the right. Note that also artifacts that were marked with the automatic artifact detection methods will be displayed here, see the [automatic artifact rejection tutorial](/tutorial/preproc/automatic_artifact_rejection). You can click on one of the artifact types, drag over a timewindow to select the start and the end of the artifact and then double click into the selected area to mark this artifact. To remove such an artifact, simply repeat the same procedure.

{% include markup/yellow %}
The databrowser will **not** change your data in any way. If you specify a cfg as output, it will just store your selected or de-selected artifacts in your cfg.
{% include markup/end %}

Here we use the databrowser to scroll through the data, reading 15 second steps from disk at a time.

    cfg = [];
    cfg.dataset = filename;
    cfg.blocksize = 15;
    ft_databrowser(cfg);

You can use the buttons to zoom in and out, but you can also set the horizontal and vertical scale in the configuration.

    cfg = [];
    cfg.blocksize = 15;     % set the horizontal block size (in seconds)
    cfg.ylim = [-30 30];    % set the vertical limits (in uV)
    ft_databrowser(cfg, data);

### Looking at low-level data characteristics

The databrowser is useful to look at the content of the data. Sometimes it also helps to look at the structure of the data, i.e., the technical details. For that we can use the low-level FieldTrip functions. Note that these are not the functions we recommend to use for a complete analysis pipeline, as the high-level functions are more robust and take better care of the data handling. But for looking at details they are useful.

    % look at the low-level details of the file

    hdr = ft_read_header(filename);
    dat = ft_read_data(filename);
    event = ft_read_event(filename);

Rather than the data being represents in a MATLAB structure, it is now simply a matrix.

    size(dat)

The header has the details on the channel names and the sampling rate, which you could use to construct the time axis.

    disp(hdr)

The events are a structure array, i.e., a list of structures. Each event correspond to "something" that happened during the recording, such as a trigger or marker.

    for i=1:10
      disp('----------------------')
      disp(event(i))
    end

### Define the trials from the triggers

To look at event-related potentials we need to cut the data into segments around the stimulus. These segments are sometimes also called "epochs" or "trials". To cut the data segments of interest, we need to know the begin and end sample of each segment. These can be determined either

- according to a specific trigger or marker that is present in the data
- according to your own criteria when you write your own trial function, e.g., for conditional trigger sequences, or by detecting the onset of movement in an EMG channel

Both depend on **[ft_definetrial](/reference/ft_definetrial)**. The output of **[ft_definetrial](/reference/ft_definetrial)** is a configuration structure containing the field `cfg.trl`. This is a matrix representing the relevant parts of the raw datafile which are to be selected for further processing. Each row in the `trl` matrix represents a single epoch-of-interest, and the `trl` matrix has 3 or more columns. The first column defines (in samples) the beginpoint of each epoch with respect to how the data are stored in the raw datafile. The second column defines (in samples) the endpoint of each epoch, and the third column specifies the offset (in samples) of the first sample within each epoch with respect to timepoint 0 within that epoch. The subsequent columns can be used to keep information about each trial.

If you do not specify your own trial function, the 4th column will by default contain the trigger or marker value. When you use your own trial function, you can add any number of extra columns to the `trl` matrix. These will be added to the data in the `.trialinfo` field. This is very handy if you want to add information of e.g., response-buttons, response-times, etc., to each trial. As you will see, we will use this functionality to preprocess both the different stimuli together, and then separating them later for averaging.

### Looking at the trigger codes

When we look at the event structure, we mainly see many "Stimulus" events. Those are the ones that correspond to the stimuli that were presented. There are some other event types as well, which we ignore for now.

    % select the stimulus events
    select = strcmp({event.type}, 'Stimulus');

    time = [event(select).sample] / hdr.Fs;
    value = {event(select).value};

The event values are formatted as "S123", so as a string. For plotting it is easier to convert them into numbers. We remove the first "S" character and convert the remaining string into a number

    for i=1:numel(value)
      numericvalue(i) = str2num(value{i}(2:end));
    end

    figure
    plot(time, numericvalue, '.')
    xlabel('time (s)')
    ylabel('trigger value')

The figure of the trigger values reveals the temporal structure of the experiment. You can see which trigger codes were sent when (i.e., which stimuli were presented), and you can see that there was a break in the middle of the recording during which no triggers were sent.

### Defining and reading trials

Now that we know about the structure and values of the events, we can go back to the data on disk, search for a specific stimulus, and define trials around that stimulus event.

    % read all trials of one stimulus condition

    cfg = [];
    cfg.dataset = filename;
    cfg.trialdef.eventtype = 'Stimulus';
    cfg.trialdef.eventvalue = 'S123';
    cfg.trialdef.prestim = 0.5;
    cfg.trialdef.poststim = 1;
    cfg = ft_definetrial(cfg);

Following ft_definetrial, the output configuration structure has the additional field `cfg.trl` which represents the beginsample, the endsample and the offset (the amount of samples that the trial is shifted relative to the trigger). See the help of ft_definetrial for more details.

Using the updated configuration structure, we can call **[ft_preprocessing](/reference/ft_preprocessing)** to read only the segments of interest.

    data_S123 = ft_preprocessing(cfg);

The data now has multiple trials or segments

    disp(data);

We can use the databrowser to plot the trials, one-by-one. The time of each trial is now relative to the trigger.

    cfg = [];
    cfg.plotevents = 'no';
    cfg.continuous = 'no';
    ft_databrowser(cfg, data_S123);

We can also use the databrowser to plot the data continuously, relative to the start of the recording. This allows us to see where in the recording the segments or trials were coming from.

    cfg = [];
    cfg.plotevents = 'no';
    cfg.continuous = 'yes';
    cfg.blocksize = 60;
    ft_databrowser(cfg, data_S123);

All the data in between of the trials, but also at the start of the recording when the experiment had not yet started and during the break when the participant had a pause, is now not present any more in the data structure.

### Compute the average ERP

Now that we have the trials of this one condition we can compute the event-related potential by averaging the data over trials.

    cfg = [];
    erp_S123 = ft_timelockanalysis(cfg, data_S123);

The **[ft_timelockanalysis](/reference/ft_timelockanalysis)** function results in a MATLAB structure that is similar to the one from **[ft_preprocessing](/reference/ft_preprocessing)**, but now there is only one matrix that contains the EEG data averaged over trials. We can again use the standard MATLAB plotting function.

    figure
    plot(erp_S123.time, erp_S123.avg);

## Segmenting, preprocessing, and averaging the EEG data

When we read the data from disk, we can apply preprocessing options such as filtering. This can be done on the continuous data, but also on the data corresponding to only the trials of interest. Since we only read the data of interest, and only filter the short segments, th e processing is much faster and requires less memory. The disadvantage is that the discontinuous signal at the start and end of the trials might cause [filter ringing artifacts](https://en.wikipedia.org/wiki/Ringing_artifacts).

    cfg = [];
    cfg.dataset = filename;
    cfg.trialdef.eventtype = 'Stimulus';
    cfg.trialdef.eventvalue = 'S123';
    cfg.trialdef.prestim = 0.5;
    cfg.trialdef.poststim = 1;
    cfg.representation = 'table';
    cfg = ft_definetrial(cfg);

    cfg.lpfilter = 'yes';
    cfg.lpfreq = 30;
    cfg.baselinewindow = [-0.5 0]; % 500 ms prior to the trigger
    cfg.demean = 'yes';
    data_S123 = ft_preprocessing(cfg);

Note that baseline correction is not possible for continuous data, as the baseline window is defined for each trial as the time window prior to the trigger.

Again we average the trials and can plot the ERP.

    cfg = [];
    erp_S123 = ft_timelockanalysis(cfg, data_S123);

    figure
    plot(erp_S123.time, erp_S123.avg);

### Removing artifacts in segmented data

While looking at the data in the databrowser it was clear that there are artifacts, like eye blinks. We can take a step back and, prior to averaging the ER, remove the trials that are affected by these artifacts. There are three ways we can look at the data to identify artifacts.

We can look at one channel at a time, showing all trials, and browse through the channels. This is useful if you know that some channels (like the frontal ones) are likely to see the artifacts.

    cfg = [];
    cfg.method = 'channel';
    data_S123_clean = ft_rejectvisual(cfg, data_S123);

We can look at one trial at a time, showing all channels, browsing through all trials. This is useful to see how the artifact behaves over all channels.

    cfg = [];
    cfg.method = 'trial';
    data_S123_clean = ft_rejectvisual(cfg, data_S123);

We can make a summary for each channel and each trial, and use that to reject channels and/or trials that for example show a lot of variance (indicating that there is a lot of noise).

    cfg = [];
    cfg.method = 'summary';
    data_S123_clean = ft_rejectvisual(cfg, data_S123);

Regardless of which we use, or whether we use them sequentially (feeding the output of one cleaning step in the next cleaning step), after removing the trials and/or channels affected by artifacts we can recompute the ERP by averaging over trials.

    cfg = [];
    erp_S123_clean = ft_timelockanalysis(cfg, data_S123_clean);

    figure
    plot(erp_S123_clean.time, erp_S123_clean.avg);

## Preprocessing, segmenting, and averaging the EEG data

Rather than first defining the trials, reading and filtering each trial individually, we can also start with reading and filtering the continuous data and only then cut the trials out of the continuous data. This prevents [filter ringing artifacts](https://en.wikipedia.org/wiki/Ringing_artifacts), but comes at the expense that more data needs to be processed and held in memory, and that the data review for artifacts might be more tedious.

    cfg = [];
    cfg.dataset = filename;
    cfg.lpfilter = 'yes';
    cfg.lpfreq = 30;
    data_S123_continuous = ft_preprocessing(cfg);

    cfg = [];
    cfg.dataset = filename;
    cfg.trialdef.eventtype = 'Stimulus';
    cfg.trialdef.eventvalue = 'S123';
    cfg.trialdef.prestim = 0.5;
    cfg.trialdef.poststim = 1;
    cfg.representation = 'table';
    cfg = ft_definetrial(cfg);

    % remember the trial definition
    trl_S123 = cfg.trl;
    
    cfg = [];
    cfg.trl = trl_S123;
    data_S123_segmented = ft_redefinetrial(cfg, data_S123_continuous);

The resulting data segments are the same as the ones that we read earlier, except that the filtering now has been done on the continuous data prior to segmenting. This has the advantage that there is less chance of filter ringing artifacts at the start and end of each trial.

The baseline correction of the trials on basis of the time window prior to the trigger has not yet been done now, so that is a step that we still need to do after segmenting.

    cfg = [];
    cfg.demean = 'yes';
    cfg.baselinewindow = [-0.5 0]; % 500 ms prior to the trigger
    data_S123_segmented = ft_preprocessing(cfg, data_S123_segmented);

We can call **[ft_preprocessing](/reference/ft_preprocessing)** as many times in succession as we like, and the order of many of the preprocessing options can be swapped around without affecting the final result.

### Removing artifacts in continuous data

We cannot directly use **[ft_rejectvisual](/reference/ft_rejectvisual)** to detect artifacts in the continuous data, since **[ft_rejectvisual](/reference/ft_rejectvisual)** works trial-by-trial. But we can use **[ft_databrowser](/reference/ft_databrowser)** to mark sections of the data with artifacts.

    cfg = [];
    cfg.blocksize = 15;
    cfg.ylim = [-30 30];
    cfg = ft_databrowser(cfg, data_S123_continuous);

    % the data is not yet cleaned, but the begin and end sample of the marked artifacts is stored
    artifact = cfg.artfctdef.visual.artifact;

    cfg = [];
    cfg.reject = 'partial';
    cfg.artfctdef.visual.artifact = artifact;
    data_S123_clean = ft_rejectartifact(cfg, data_S123_continuous);

    disp(data_S123_clean)

The cleaned data now consists of a few segments, since the parts with the artifacts have been removed. The remaining segments do not yet correspond to trials. As before we can define trials using the events in the original data file, and segment the cleaned semi-continuous data.

    cfg = [];
    cfg.dataset = filename;
    cfg.trialdef.eventtype = 'Stimulus';
    cfg.trialdef.eventvalue = 'S123';
    cfg.trialdef.prestim = 0.5;
    cfg.trialdef.poststim = 1;
    cfg.representation = 'table';
    cfg = ft_definetrial(cfg);

    % remember the trial definition
    trl_S123 = cfg.trl;

    cfg = [];
    cfg.trl = trl_S123;
    data_S123_clean_nantrials = ft_redefinetrial(cfg, data_S123_clean);

    % the trials that fall in the segments that were removed are represented with NaN values
    % we can remove them completely with ft_rejectartifact
    cfg = [];
    cfg.reject = 'complete';
    cfg.artfctdef.visual.artifact = artifact;
    data_S123_clean_trials = ft_rejectartifact(cfg, data_S123_clean_nantrials);

The resulting trials can be visualized with **[ft_databrowser](/reference/ft_databrowser)**, and averaged to get the ERP.

    cfg = [];
    ft_databrowser(cfg, data_S123_clean_trials);

    cfg = [];
    erp_S123_clean = ft_timelockanalysis(cfg, data_S123_clean_trials);

    figure
    plot(erp_S123_clean.time, erp_S123_clean.avg);

### Using the summary mode on continuous data

A work-around for using **[ft_rejectvisual](/reference/ft_rejectvisual)** on continuous data is to read the continuous data, to segment it into non-overlapping one-second trials using ft_redefinetrial, and to use those to detect artifacts. After the affected one-second segments have been removed, you can "glue" the data back together in longer semi-continuous segments with ft_redefinetrial, or you can use ft_definetrial and ft_redefinetrial to cut out the trials of interest.

We start again with the continuous data.

    cfg = [];
    cfg.dataset = filename;
    cfg.lpfilter = 'yes';
    cfg.lpfreq = 30;
    data_S123_continuous = ft_preprocessing(cfg);

We cut it into one-second segments.

    cfg = [];
    cfg.length = 1;
    cfg.overlap = 0;
    data_S123_1sec = ft_redefinetrial(cfg, data_S123_continuous);

With the summary mode of **[ft_rejectvisual](/reference/ft_rejectvisual)** we can very quickly identify the parts of the data that are noisy since the participant had a break.

    cfg = [];
    cfg.method = 'summary';
    data_S123_1sec_clean = ft_rejectvisual(cfg, data_S123_1sec);

After removing the affected one-second segments, we can glue the remaining segments back together again.

    cfg = [];
    cfg.continuous = 'yes';
    data_S123_continuous_clean = ft_redefinetrial(cfg, data_S123_1sec_clean);

## Rereferencing

We can improve the preprocessing by optimizing the reference. During acquisition the reference channel of the EEG amplifier was attached to the left mastoid, and one electrode was placed below the left eye. We would like to analyze the EEG data with a linked-mastoid reference (also known as an average-mastoid reference). Furthermore, the detection of eye movement and blink artifacts is facilitated by computing a bipolar derivation for the electrodes that were placed horizontally and vertically around the eyes.

The channel names that were configured in the BrainAmp Recorder software correspond to the labels of the locations in the electrode cap. These electrode locations are numbered 1 to 60, and the corresponding channel names as ASCII strings are '1', '2', ... '60'. Electrode location 53 correspond to the right mastoid (M2). Since the electrode on the left mastoid (M1) was used as the reference during acquisition, it is not represented in the data file; this is because the voltage at that electrode is zero by definition.

    cfg = [];
    cfg.dataset     = filename;
    cfg.reref       = 'yes';
    cfg.channel     = 'all';
    cfg.implicitref = 'M1';         % the implicit (non-recorded) reference channel is added to the data representation
    cfg.refchannel  = {'M1', '53'}; % the average of these two is used as the new reference, channel '53' corresponds to the right mastoid (M2)
    data_eeg        = ft_preprocessing(cfg);

For consistency we will rename the channel with the name '53' located at the right mastoid to 'M2'

    chanindx = find(strcmp(data_eeg.label, '53'));
    data_eeg.label{chanindx} = 'M2';

To discard channels that we do not need any more we can do

    cfg = [];
    cfg.channel     = [1:61 65];                      % keep channels 1 to 61 and the newly inserted M1 channel
    data_eeg        = ft_selectdata(cfg, data_eeg);

If you look at the data, you will see that it contains a single trial. That single trial represents the complete continuous recording and therefore it is approximately one hour long.

    plot(data_eeg.time{1}, data_eeg.trial{1}(1:3,:));
    legend(data_eeg.label(1:3));

Subsequently we read the data for the horizontal EOG

    cfg = [];
    cfg.dataset    = filename;
    cfg.channel    = {'51', '60'};
    cfg.reref      = 'yes';
    cfg.refchannel = '51';
    data_eogh      = ft_preprocessing(cfg);

The resulting channel 51 in this representation of the data is now referenced to itself, which means that it only contains zero values. This can be checked by

    figure
    plot(data_eogh.time{1}, data_eogh.trial{1}(1,:));
    hold on
    plot(data_eogh.time{1}, data_eogh.trial{1}(2,:),'g');
    legend({'51' '60'});

For convenience we rename channel 60 into EOGH and use the **[ft_selectdata](/reference/ft_selectdata)** function to select the horizontal EOG channel and discard the channel 51 that is now zero.

    data_eogh.label{2} = 'EOGH';

    cfg = [];
    cfg.channel = 'EOGH';
    data_eogh   = ft_selectdata(cfg, data_eogh); % nothing will be done, only the selection of the interesting channel

The processing of the vertical EOG is done similar, using the difference between channel 50 and 64 as the bipolar EOG.

    cfg = [];
    cfg.dataset    = filename;
    cfg.channel    = {'50', '64'};
    cfg.reref      = 'yes';
    cfg.refchannel = '50';
    data_eogv      = ft_preprocessing(cfg);

    data_eogv.label{2} = 'EOGV';

    cfg = [];
    cfg.channel = 'EOGV';
    data_eogv   = ft_preprocessing(cfg, data_eogv); % nothing will be done, only the selection of the interesting channel

Now that we have the EEG data rereferenced to linked mastoids, and the horizontal and vertical bipolar EOG, we can combine the three raw data structures into a single representation using:

    cfg = [];
    data_all = ft_appenddata(cfg, data_eeg, data_eogh, data_eogv);

If we now use **[ft_databrowser](/reference/ft_databrowser)** or **[ft_rejectvisual](/reference/ft_rejectvisual)**, it is easier to zoom in on the eye channels and to remove the trials or data segments where the participant blinked or looked away from the center of the screen.

{% include markup/yellow %}
Now that you know how to compute the linked-mastoids EEG data, and the bipolar EOGH and EOGV, you could go back in your preprocessing script and use the EOG channels to speed up the detection of trials in which the participant blinked or looked away from the stimulus on screen.
{% include markup/end %}
