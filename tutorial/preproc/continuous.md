---
title: Preprocessing - Reading continuous EEG and MEG data
weight: 20
category: tutorial
tags: [preprocessing, continuous, eeg, raw, brainvision, memory, meg-language, eeg-language]
redirect_from:
    - /tutorial/continuous/
---

## Introduction

A convenient use of the **[ft_preprocessing](/reference/ft_preprocessing)** is to read the continuous data fully in memory. This is feasible if your data set is relatively small and if your computer has enough memory to hold all data in memory at once. The advantage of preprocessing data in a continuous format is that it can help to prevent filter artifacts, it can improve the quality of ICA decompositions, and  gives a better overview of all data features, including artifacts that may be more difficult to recognize in segmented data.

If your experiment consists of a sequence of trials, you may also want to start by segmenting the data and only read the trials of interest. This is described in the [Preprocessing - Segmenting and reading trial-based EEG and MEG data](/tutorial/preproc/preprocessing) tutorial.

## Background

Using this approach, you can read all data from the file into memory, apply filters, rereference (in case of EEG), identify and subtract artifacts using ICA, and subsequently cut the data into segments or trials of interest.

### The datasets used in this tutorial

In this tutorial we will be using two datasets, one with EEG data and one with MEG data.

The [SubjectEEG.zip](https://download.fieldtriptoolbox.org/tutorial/SubjectEEG.zip) EEG dataset was acquired by Irina Siminova in a study investigating semantic processing of stimuli presented as pictures, visually displayed text or as auditory presented words. Data was acquired with a 64-channel BrainProducts BrainAmp EEG amplifier from 60 scalp electrodes placed in an electrode cap, one electrode placed under the right eye; signals "EOGv" and "EOGh" are computed after acquisition using rereferencing. During acquisition all channels were referenced to the left mastoid and an electrode placed at the earlobe was used as the ground. Channels 1-60 correspond to electrodes that are located on the head, except for channel 53 which is located at the right mastoid. Channels 61, 62, 63 are not connected to an electrode at all. Channel 64 is connected to an electrode placed below the left eye. Hence we have 62 channels of interest: 60 for the scalp EEG electrodes plus one EOGH and one EOGV channel. More details on the experiment and data can be found [here](/tutorial/eeg_language).

The [Subject01.zip](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip) MEG dataset was acquired by Lin Wang in a language study on semantically congruent and incongruent sentences. Three types of sentences were used in the experiment: fully congruent (FC), fully incongruent (FIC), and initially congruent (IC). There were 87 trials per condition for each of the three conditions, and a set of 87 filler sentences (not used here). Note that the data was originally acquired and written to disk as 3-second trigger-locked epochs with discontinuities between the epochs; this data can therefore not be treated as continuous.  More details on the experiment and data can be found [here](/tutorial/meg_language).

## Procedure

The following steps are taken to read data, to apply filters and to rereference the data (in case of EEG), and optionally to select interesting segments of data around events or triggers or by cutting the continuous data into convenient constant-length segments.

- read the data for the EEG channels using **[ft_preprocessing](/reference/ft_preprocessing)**, apply a filter and rereference to linked mastoids
- read the data for the horizontal and vertical EOG channels using **[ft_preprocessing](/reference/ft_preprocessing)**, and compute the horizontal and vertical bipolar EOG derivations
- combine the EEG and EOG into a single data representation using **[ft_appenddata](/reference/ft_appenddata)**
- determine interesting pieces of data based on the trigger events using **[ft_definetrial](/reference/ft_definetrial)**
- segment the continuous data into trials using **[ft_redefinetrial](/reference/ft_redefinetrial)**
- segment the continuous data into one-second pieces using **[ft_redefinetrial](/reference/ft_redefinetrial)**

## Reading continuous EEG data into memory

The simplest method for preprocessing and reading the data into memory is by calling the **[ft_preprocessing](/reference/ft_preprocessing)** function with only the dataset as configuration argument.

    cfg = [];
    cfg.dataset = 'subj2.vhdr';
    data_eeg    = ft_preprocessing(cfg)

    >> data_eeg
    data_eeg =
        hdr: [1x1 struct]
      label: {64x1 cell}
      trial: {[64x2011220 double]}
       time: {[1x2011220 double]}
    fsample: 500
        cfg: [1x1 struct]

This reads the data from file as one long continuous segment without any additional filtering. The resulting data is represented as one very long trial. To plot the potential in one of the channels, you can simply use the MATLAB plot function.

    chansel = 1;
    plot(data_eeg.time{1}, data_eeg.trial{1}(chansel, :))
    xlabel('time (s)')
    ylabel('channel amplitude (uV)')
    legend(data_eeg.label(chansel))

## Reading continuous MEG data into memory

If the data on disk is stored in a segmented or epoched format, i.e. where the file format already reflects the trials in the experiment, a call to **[ft_preprocessing](/reference/ft_preprocessing)** will return in the data being read and segmented into the original trials.

    cfg = [];
    cfg.dataset     = 'Subject01.ds';
    data_meg        = ft_preprocessing(cfg);

    >> data_meg
    data_meg =
        hdr: [1x1 struct]
      label: {187x1 cell}
      trial: {1x266 cell}
       time: {1x266 cell}
    fsample: 300
       grad: [1x1 struct]
        cfg: [1x1 struct]

This segmented MEG data dataset contains 266 trials. The following example shows how you can plot the data in a subset of the trials.

    for trialsel=1:10
      chansel = 1; % this is the STIM channel that contains the trigger
      figure
      plot(data_meg.time{trialsel}, data_meg.trial{trialsel}(chansel, :))
      xlabel('time (s)')
      ylabel('channel amplitude (a.u.)')
      title(sprintf('trial %d', trialsel));
    end

If you want to force epoched data to be interpreted as continuous data, you can use the cfg.continuous option, like this:

    cfg = [];
    cfg.dataset     = 'Subject01.ds';
    cfg.continuous  = 'yes';              % force it to be continuous
    data_meg        = ft_preprocessing(cfg);

    chansel = 2;                          % this is SCLK01
    plot(data_meg.time{1}, data_meg.trial{1}(chansel, :))
    xlabel('time (s)')
    ylabel(data_meg.label{chansel})

If you zoom in and look in detail at the SCLK01 channel, you can see that there are small jumps every 3 seconds. These are due to the data being discontinuous on disk, i.e. only the 3 second segments around each stimulus are stored on disk and the data in-between the trials is not stored. Consequently the MEG channels will also have small jumps every 3 seconds and hence this particular dataset should **not be interpreted** as a continuous recording. Many other CTF recordings are stored on disk with data segments of 10 seconds each; these can be interpreted as continuous as there are no gaps between the long segments.

## Preprocessing, filtering and rereferencing

We can improve the preprocessing by optimizing the reference. During acquisition the reference channel of the EEG amplifier was attached to the left mastoid, and one electrode was placed below the left eye. We would like to analyze the EEG data with a linked-mastoid reference (also known as an average-mastoid reference). Furthermore, the detection of eye movement and blink artifacts is facilitated by computing a bipolar derivation for the electrodes that were placed horizontally and vertically around the eyes.

The channel names that were configured in the BrainAmp Recorder software correspond to the labels of the locations in the electrode cap. These electrode locations are numbered 1 to 60, and the corresponding channel names as ASCII strings are '1', '2', ... '60'. Channel 53 correspond to the right mastoid. Since the left mastoid was used as reference in the acquisition, it is not represented in the data file (because the Voltage at that electrode is zero by definition).

    cfg = [];
    cfg.dataset     = 'subj2.vhdr';
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
    cfg.dataset    = 'subj2.vhdr';
    cfg.channel    = {'51', '60'};
    cfg.reref      = 'yes';
    cfg.refchannel = '51';
    data_eogh      = ft_preprocessing(cfg);

The resulting channel 51 in this representation of the data is referenced to itself, which means that it contains zero values. This can be checked by

    figure
    plot(data_eogh.time{1}, data_eogh.trial{1}(1,:));
    hold on
    plot(data_eogh.time{1}, data_eogh.trial{1}(2,:),'g');
    legend({'51' '60'});

For convenience we rename channel 60 into EOGH and use the **[ft_preprocessing](/reference/ft_preprocessing)** function once more to select the horizontal EOG channel and discard the dummy channel.

    data_eogh.label{2} = 'EOGH';

    cfg = [];
    cfg.channel = 'EOGH';
    data_eogh   = ft_selectdata(cfg, data_eogh); % nothing will be done, only the selection of the interesting channel

The processing of the vertical EOG is done similar, using the difference between channel 50 and 64 as the bipolar EOG

    cfg = [];
    cfg.dataset    = 'subj2.vhdr';
    cfg.channel    = {'50', '64'};
    cfg.reref      = 'yes';
    cfg.refchannel = '50'
    data_eogv      = ft_preprocessing(cfg);

    data_eogv.label{2} = 'EOGV';

    cfg = [];
    cfg.channel = 'EOGV';
    data_eogv   = ft_preprocessing(cfg, data_eogv); % nothing will be done, only the selection of the interesting channel

Now that we have the EEG data rereferenced to linked mastoids, and the horizontal and vertical bipolar EOG, we can combine the three raw data structures into a single representation using:

    cfg = [];
    data_all = ft_appenddata(cfg, data_eeg, data_eogh, data_eogv);

In the example above, no filters were applied to the data. It is possible to apply filters to the data during the initial preprocessing/reading. It is also possible to apply filters afterwards by calling the **[ft_preprocessing](/reference/ft_preprocessing)** function with the data as second input argument. If you want to apply different preprocessing options (such as filters for EEG channels, rectification of EMG channels, rereferencing) to different channels, you should call **[ft_preprocessing](/reference/ft_preprocessing)** with the desired options for each of the channel types and subsequently append the data for the different channels types into one raw data structure.

## Segmenting continuous data into trials

Following the reading and channel specific preprocessing, you can identify interesting pieces of data based on the trigger codes and segment the continuous data into trials. Let's first look at the different trigger codes present in the data se

    cfg = [];
    cfg.dataset             = 'subj2.vhdr';
    cfg.trialdef.eventtype = '?';
    dummy                   = ft_definetrial(cfg);

This will display the event types and values on screen.

    evaluating trial function 'trialfun_general'
    the following events were found in the datafile
    event type: 'New Segment' with event values:
    event type: 'Response' with event values: 'R  8'
    event type: 'Stimulus' with event values: 'S  1' 'S 12' 'S 13' 'S 21' 'S 27' 'S111'
     'S112' 'S113' 'S121' 'S122' 'S123' 'S131' 'S132' 'S133' 'S141' 'S142' 'S143'
     'S151' 'S152' 'S153' 'S161' 'S162' 'S163' 'S171' 'S172' 'S173' 'S181' 'S182'
     'S183' 'S211' 'S212' 'S213' 'S221' 'S222' 'S223' 'S231' 'S232' 'S233' 'S241'
     'S242' 'S243'
    no trials have been defined yet, see FT_DEFINETRIAL for further help
    found 1570 events
    created 0 trials

The trigger codes S111, S121, S131, S141 correspond to the presented pictures of 4 different animals respectively. The trigger codes S151, S161, S171, S181 correspond to the presented pictures of 4 different tools. We can select the data for the animals and tools category with

    cfg = [];
    cfg.dataset             = 'subj2.vhdr';
    cfg.trialdef.eventtype = 'Stimulus';
    cfg.trialdef.eventvalue = {'S111', 'S121', 'S131', 'S141'};
    cfg_vis_animal          = ft_definetrial(cfg);

    cfg.trialdef.eventvalue = {'S151', 'S161', 'S171', 'S181'};
    cfg_vis_tool            = ft_definetrial(cfg);

The output configuration resulting from **[ft_definetrial](/reference/ft_definetrial)** contains the trial definition as a Nx3 matrix with the begin sample, the end sample and the offset of each trial. In principle you could now use this configuration to read these segments from the original data file on disk, but since we already have the complete continuous data in memory, we'll use **[ft_redefinetrial](/reference/ft_redefinetrial)** to cut these trials out of the continuous data segment.

    data_vis_animal = ft_redefinetrial(cfg_vis_animal, data_all);
    data_vis_tool   = ft_redefinetrial(cfg_vis_tool,   data_all);

Subsequently we could do artifact detection with **[ft_rejectvisual](/reference/ft_rejectvisual)** to remove trials with artifacts and average the trials using **[ft_timelockanalysis](/reference/ft_timelockanalysis)** to get the ERP, or use **[ft_freqanalysis](/reference/ft_freqanalysis)** to obtain an averaged time-frequency representation of the data in both conditions. If you use ft_timelockanalysis or ft_frequencyanalysis with the option cfg.keeptrials='yes', you subsequently could use ft_timelockstatistics or ft_freqstatistics for statistical comparison of the animal-tool contrast in these stimuli.

## Segmenting continuous data into one-second pieces

For processing of continuous data without triggers it is convenient to cut the data into constant-length pieces. This can be done while reading the data from disk, or it can be done after the complete continuous data is in memory.

The following example shows how to read and segment the data in one go.

    cfg = [];
    cfg.dataset              = 'subj2.vhdr';
    cfg.trialfun             = 'ft_trialfun_general';
    cfg.trialdef.triallength = 1;                      % duration in seconds
    cfg.trialdef.ntrials     = inf;                    % number of trials, inf results in as many as possible
    cfg                      = ft_definetrial(cfg);

    % read the data from disk and segment it into 1-second pieces
    data_segmented           = ft_preprocessing(cfg);

The following example shows how to first read the data as a single continuous segment, and subsequently cut it into one second pieces or segments.

    % read it from disk as a single continuous segment
    cfg = [];
    cfg.dataset              = 'subj2.vhdr';
    data_cont                = ft_preprocessing(cfg);

    % segment it into 1-second pieces
    cfg = [];
    cfg.length               = 1;
    data_segmented           = ft_redefinetrial(cfg, data_cont);

## Suggested further reading

After having finished this tutorial on preprocessing, you can continue with the tutorial on [Preprocessing of EEG data and compute ERPs](/tutorial/sensor/preprocessing_erp), with the [event-related averaging](/tutorial/sensor/eventrelatedaveraging) or with the [time-frequency analysis](/tutorial/sensor/timefrequencyanalysis) tutorial.

### See also these frequently asked questions

{% include seealso category="faq" tag1="preprocessing" %}

### See also these examples

{% include seealso category="example" tag1="preprocessing" %}
