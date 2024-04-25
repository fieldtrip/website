---
title: Preprocessing and event-related potentials in EEG data
tags: [oslo2019, eeg-audodd, preprocessing]
---

# Preprocessing and event-related potentials in EEG data

## Introduction

This tutorial describes how to define epochs of interest (trials) from recorded EEG data, and how to apply different preprocessing steps such as filtering, cleaning data and re-referencing electrodes. Subsequently, we will average our epochs/trials and acquire so-called event-related potentials (ERPs). We will also compare two different types of stimuli (standard versus deviant tones) and investigate the differing ERPs they give rise to.

In this tutorial, preprocessing and segmenting the data into epochs/trials are done in a single step. If you are interested in how to do preprocessing on continuous data prior to segmenting it into epochs/trials, you can check the [Preprocessing - Reading continuous data](/tutorial/continuous) tutorial.

{% include markup/skyblue %}
This data in this tutorial is originally from the [NatMEG workshop](/workshop/natmeg2014) and it is complemented by this lecture. This lectured featured the combination of MEG and EEG. Please go [here](/workshop/natmeg2014) to see in its entirety.

{% include youtube id="zOxCqcYmIfA" %}
{% include markup/end %}

## Background

In FieldTrip, the preprocessing of data refers to the reading of the data, segmenting the data around interesting events, which are defined by triggers in the data, temporal filtering and (optionally) re-referencing. The **[ft_preprocessing](/reference/ft_preprocessing)** function takes care of all these steps, i.e., it reads the data and applies the preprocessing options.

There are largely two alternative approaches for preprocessing, which especially differ in the amount of memory required.

1. Read all data from the file into memory, apply filters, and subsequently cut the data into interesting segments
2. Identify the interesting segments, read those segments from the data file and apply filters to those segments only

An advantage of the first approach is that it allows you to apply most temporal filters to your data without the distorting the data. In the latter approach, you have to be more careful with the temporal filtering you apply, but it is much more memory-friendly, especially for big datasets.
 Here we are using the second approach. The approach for reading and filtering continuous data and segmenting afterwards is explained in [another tutorial](/tutorial/continuous).

We are going to define segments of interest (epochs/trials) based on triggers encoded in a specific trigger channel.
This depends on the function **[ft_definetrial](/reference/ft_preprocessing)**. The output of **[ft_definetrial](/reference/ft_preprocessing)** is a so-called configuration structure (typically called _cfg_), which contains the field _cfg.trl_. This is a matrix representing the relevant parts of the raw data, which are to be selected for further processing. Each row in `trl` matrix represents a single epoch-of-interest (trial), and the `trl` matrix has three or more columns. The first column defines (in samples) the beginning point of each epoch with respect to how the data are stored in the raw data file. The second column defines (in samples) the end point of each epoch. The third column specifies the offset (in sample) of the first sample within each epoch with respect to time point 0 within than epoch. In essence they contain information about when the epoch begins, end and when time 0 appears. The trial matrix can contain more columns with more (user-chosen) information about the trial.

You can either use a default trial function or design your own. When using the default trial function, the fourth column will contain the trigger value of the trigger channel. If you do use your own trial function, you can add as many columns as you wish to the _trl_ matrix, which will be contained in your segmented data in the _.trialinfo_ field. Here, you can add information of for example response buttons, response times.

## Details of the auditory oddball MEG+EEG Dataset

_Please note that we will only be using the EEG data from this dataset._

{% include /shared/workshop/natmeg2014/meg_audodd.md %}

## Have a look at the data prior to preprocessing

Before we start preprocessing our data and calculate event-related potentials (ERPs), we will first have a look at our data while it is unprocessed and not yet cut into trial (following FieldTrip nomenclature: _raw_ data). To do this, we use **[ft_databrowser](/reference/ft_databrowser)**. Note that **[ft_databrowser](/reference/ft_databrowser)** is very memory efficient, as it does not read all data into memory - only the part that it displays.

### How can I use the data browser?

The data browser can be used to look at your raw or preprocessed data. The main purpose is to do quality checks and visual artifact detection and also annotate time periods during which specific artifacts happens. However, it also supports annotation of the data, such as annotating sleep spindles or epileptic spikes.

The data browser supports three view modes: _butterfly_, _vertical_ and _component_. In _butterfly_, all signal traces will be plotted on top of one another; in _vertical_, the traces will be below one another. The _component_ view mode is to be used for data that is decomposed into independent components (see **[ft_componentanalysis](/reference/ft_componentanalysis)**. Components will be plotted as in the vertical view mode, but will include the component topography to the left of the time trace. As an alternative to these three view modes, you can provide a _cfg.layout_, and **[ft_databrowser](/reference/ft_databrowser)** will try to plot the data according to the sensor positions specified in that layout.

When the data browser opens, you will see button to navigate along the bottom of the screen and buttons for artifact annotation to the right. Note that also artifacts that were marked with automatic artifact detection methods will be displayed here (see the [automatic artifact rejection tutorial](/tutorial/automatic_artifact_rejection)). You can click on one of the artifact types, drag over a time window to select the beginning and the end of the artifact and then double-click in the selected area to mark it as an artifact. Double-clicking again will remove the selection.

{% include markup/yellow %}
The data browser will **not** change your data in an way. If you specify a _cfg_ as output, it will just store your selected artifacts in that output cfg.
{% include markup/end %}

### Before we begin

We will clear all variables that we have in the workspace, restore the default path, add fieldtrip and run _ft_defaults_

    clear variables
    restoredefaultpath

    addpath /home/lau/matlab/fieldtrip/ %% set your own path
    ft_defaults

### Visualization of raw EEG data

The EEG dataset used in this tutorial is available [here](https://download.fieldtriptoolbox.org/workshop/oslo2019/)

    cfg            = [];
    cfg.dataset    = 'oddball1_mc_downsampled_eeg.eeg';
    cfg.continuous = 'yes';
    cfg.viewmode   = 'vertical';
    cfg.blocksize  = 1; % duration of data to display, in seconds

    ft_databrowser(cfg);

    set(gcf, 'units', 'normalized', 'outerposition', [0 0 1 1]) % full screen
    print -dpng databrowser_oslo2019.png

{% include markup/yellow %}
If your recorded is continuous, specify _cfg.continuous = 'yes'_. If your data is segmented into epochs/trials, specify _cfg.continuous = 'no'_.
{% include markup/end %}

{% include image src="/assets/img/workshop/oslo2019/databrowser.png" width="650" %}
_Figure 1: Raw plot of electrodes using ft_databrowser_

{% include markup/skyblue %}
Get a feel of your data by browsing through it. Do you see any obvious artifacts?
{% include markup/end %}

## Preprocessing and averaging EEG

In this step, we will preprocess and subsequently average our epochs/trials to obtain ERPs.

### Procedure

We will take the following steps

- Define segments of data of interest (the trial definition) using **[ft_definetrial](/reference/ft_definetrial)**
- Read the data into MATLAB using **[ft_preprocessing](/reference/ft_preprocessing)**
- Clean the data in a semi-automatic way using **[ft_rejectvisual](/reference/ft_rejectvisual)**
- Calculate event-related potentials (ERPs) using **[ft_timelockanalysis](/reference/ft_timelockanalysis)**
- Visualize the results using **[ft_multiplotER](/reference/ft_multiplotER)**, **[ft_singleplotER](/reference/ft_singleplotER)** and **[ft_topoplotER](/reference/ft_topoplotER)**

### Reading and preprocessing the epochs/trials of interest

    cfg = [];
    cfg.dataset             = 'oddball1_mc_downsampled_eeg.vhdr';

    cfg.trialdef.eventtype  = 'STI101'; % name of trigger channel
    cfg.trialdef.eventvalue = {1 2}; % 1 is standard, 2 is deviant
    cfg.trialdef.prestim    = 0.200; % seconds
    cfg.trialdef.poststim   = 0.600; % seconds
    cfg.trialfun = 'ft_trialfun_general';

    cfg = ft_definetrial(cfg); %% note that a new cfg is created here

    % and we add more stuff to it here

    cfg.continuous          = 'yes';    % data is continuous
    cfg.hpfilter            = 'no';     % we do not apply a high-pass filter
    cfg.detrend             = 'no';     % we do not detrend
    cfg.demean              = 'yes';    % we demean (baseline correct) ...
    cfg.baselinewindow      = [-Inf 0]; % using the mean activity in this window
    cfg.dftfilter           = 'yes';    % a notch filter ...
    cfg.dftfreq             = [50 100]; % hitting the (European) power frequency
                                        % (and its first harmonic)
    cfg.channel             = 'EEG';

    cfg.reref               = 'yes';    % was recorded with left mastoid but is ...
    cfg.refchannel          = 'all';    % re-referenced to all (also called common average

    data                    = ft_preprocessing(cfg);

The output of _ft_preprocessing(cfg)_ is _data_, which is a structure that has the following fields:

    data =

               hdr: [1x1 struct]
             label: {128x1 cell}
              time: {1x600 cell}
             trial: {1x600 cell}
           fsample: 250
        sampleinfo: [600x2 double]
         trialinfo: [600x1 double]
               cfg: [1x1 struct]

- _hdr_ contains header information about the data structure (metadata)
- _label_ contains the names of all channels
- _time_ contains the time courses for each of the 600 trials
- _trial_ contains the _voltages_ for each of the 600 trials
- _fsample_ indicates the sampling frequency in Hz
- _sampleinfo_ is a matrix the samples at which sample points trials begin and end
- _trialinfo_ is a column vector indicating the type of trial (1=standard, 2=deviant)
- _cfg_ contains information about the call leading to this output

{% include markup/yellow %}
Make absolutely sure that you have **no** bad channels in your data before you do an average reference. Or more generally, make sure your reference isn't bad.
{% include markup/end %}

Let's have a closer look at the first entries in _time_ and _trial_:

    >> size(data.time{1})

    ans =
         1   200

    >> size(data.trial{1})

    ans =
       128   200

- For _time_ this is a row vector which has 200 entries, thus there are 200 time points in this epoch
- For _trial_ this is a matrix with 128 rows and 200 columns, having the voltage for each of the 128 channels and the 200 time points

### Cleaning data using visual summaries

In this tutorial, we are going to use a visual summary tool for rejecting bad trials. It is also possible to annotate artifacts using a more automatic procedure (see the  [automatic artifact rejection tutorial](/tutorial/automatic_artifact_rejection)).

    cfg        = [];
    cfg.layout = 'natmeg_customized_eeg1005.lay';

    cleaned_data_ERP = ft_rejectvisual(cfg, data);

{% include image src="/assets/img/workshop/oslo2019/reject_visual.png" width="650" %}
_Figure 2: The visual summary plot tool_

You can use different metrics to calculate the summary, but variance is usually a good metric.

{% include markup/skyblue %}
What is best - using an _objective_ automatic procedure with a common threshold between subjects, or should you use this more _"subjective"_ method?
{% include markup/end %}

In my case, I removed 26 trials

    cleaned_data_ERP =

               hdr: [1x1 struct]
             label: {128x1 cell}
              time: {1x574 cell}
             trial: {1x574 cell}
           fsample: 250
        sampleinfo: [574x2 double]
         trialinfo: [574x1 double]
               cfg: [1x1 struct]

If you want to carry on with the data cleaned by the organizers, load the data using the command below.

    load cleaned_data_ERP.mat

### Event-Related Potentials (ERPs) (also unfortunately known as time-locked responses)

The function **[ft_timelockanalysis](/reference/ft_timelockanalysis)** makes an average (ERP) over all the trials in a segmented data structure. For purposes of visualization, we will also apply a low-pass filter. Note that we could have done that earlier as well, but rather we decided to clean before applying low- or high-pass filters.

    cfg                = [];
    cfg.lpfilter       = 'yes';
    cfg.lpfreq         = 30;
    cfg.detrend        = 'yes';     % removing linear trends
    cfg.baselinewindow = [-Inf 0];  % using the mean activity in this window

    data_EEG_filt = ft_preprocessing(cfg, cleaned_data_ERP);

We are creating two ERPs, one for the standard and one for the deviant.

    cfg          = [];
    cfg.trials   = find(data_EEG_filt.trialinfo == 1);
    ERP_standard = ft_timelockanalysis(cfg, data_EEG_filt);

    cfg         = [];
    cfg.trials  = find(data_EEG_filt.trialinfo == 2);
    ERP_deviant = ft_timelockanalysis(cfg, data_EEG_filt);

The output of **[ft_timelockanalysis](/reference/ft_timelockanalysis)** looks like this:

    ERP_standard =

          time: [1x200 double]
         label: {128x1 cell}
           avg: [128x200 double]
           var: [128x200 double]
           dof: [128x200 double]
        dimord: 'chan_time'
           cfg: [1x1 struct]

- _time_ is now just a row vector with the time points in seconds (before we had a cell array with 600 cells in it)
- _label_ is still our 128 names
- _avg_ contains our averages for each of the 128 channels at each of the 200 time points
- _var_ contains the variance for each of the 128 channels at each of the 200 time points (can be used e.g., for calculating standard deviations)
- _dof_ contains the degrees of freedoms for each of the 128 channels at each of the 200 time points
- _dimord_ indicates the ordering of dimensions, rows are channels and columns are time
- _cfg_ shows the cfg that gave rise to this structure

These can be plotted using **[ft_multiplotER](/reference/ft_multiplotER)**, **[ft_singleplotER](/reference/ft_singleplotER)** and **[ft_topoplotER](/reference/ft_topoplotER)**

#### Multiplot

    cfg        = [];
    cfg.layout = 'natmeg_customized_eeg1005.lay';

    figure
    ft_multiplotER(cfg, ERP_standard, ERP_deviant);

    print -dpng multiplot.png

{% include image src="/assets/img/workshop/oslo2019/multiplot.png" width="650" %}
_Figure 3: A plot of all channels_

#### Singleplot

    cfg         = [];
    cfg.layout  = 'natmeg_customized_eeg1005.lay';
    cfg.channel = 'EEG124';
    cfg.ylim    = [-5e-6 5e-6]; % Volts

    figure
    ft_singleplotER(cfg, ERP_standard, ERP_deviant);

    hold on
    xlabel('Time (s)')
    ylabel('Electric Potential (V)')
    plot([ERP_standard.time(1), ERP_standard.time(end)], [0 0], 'k--') % add horizontal line
    plot([0 0], cfg.ylim, 'k--') % vert. l
    legend({'Standard', 'Deviant'})

    print -dpng singleplot.png

{% include image src="/assets/img/workshop/oslo2019/singleplot.png" width="650" %}
_Figure 4: A plot of a single channel_

#### Topoplot

    figure

    cfg              = [];
    cfg.layout       = 'natmeg_customized_eeg1005.lay';
    cfg.xlim         = [0.100 0.170]; % seconds
    cfg.zlim         = [-4e-6 4e-6]; % Volts
    cfg.colorbar     = 'yes';
    cfg.colorbartext =  'Electric Potential (V)';

    ft_topoplotER(cfg, ERP_standard);
    title('Auditory Response: Standard')
    print -dpng standard_aud.png

    figure
    ft_topoplotER(cfg, ERP_deviant);
    title('Auditory Response: Deviant')
    print -dpng deviant_aud.png

{% include image src="/assets/img/workshop/oslo2019/standard_aud.png" width="650" %}
_Figure 5: A topographical plot showing the average electric potential between 100 and 170 ms for the **standard**_

{% include image src="/assets/img/workshop/oslo2019/deviant_aud.png" width="650" %}
_Figure 6: A topographical plot showing the average electric potential between 100 and 170 ms for the **deviant**_

### Difference Wave

We can calculate the difference wave, the subtraction of one ERP from another

    cfg           = [];
    cfg.operation = 'x2-x1';
    cfg.parameter = 'avg';

    difference_wave = ft_math(cfg, ERP_standard, ERP_deviant);

These can be plotted using the same tools as before

#### Multiplot

    cfg        = [];
    cfg.layout = 'natmeg_customized_eeg1005.lay';

    figure
    ft_multiplotER(cfg, difference_wave);

    print -dpng multiplot_diff.png

{% include image src="/assets/img/workshop/oslo2019/multiplot_diff.png" width="650" %}
_Figure 7: A plot of all channels showing the MMN_

    cfg         = [];
    cfg.layout  = 'natmeg_customized_eeg1005.lay';
    cfg.channel = 'EEG124';
    cfg.ylim    = [-5e-6 5e-6]; % Volts

    figure
    ft_singleplotER(cfg, difference_wave);

    hold on
    xlabel('Time (s)')
    ylabel('Difference in Electric Potential (V)')
    plot([ERP_standard.time(1), ERP_standard.time(end)], [0 0], 'k--') % add horizontal line
    plot([0 0], cfg.ylim, 'k--') % vert. l

    print -dpng singleplot_MMN.png

{% include image src="/assets/img/workshop/oslo2019/singleplot_MMN.png" width="650" %}
_Figure 8: A plot of a single channel showing the MMN_

    cfg              = [];
    cfg.layout       = 'natmeg_customized_eeg1005.lay';
    cfg.xlim         = [0.100 0.170]; % seconds
    cfg.zlim         = [-1.5e-6 1.5e-6]; % Volts
    cfg.colorbar     = 'yes';
    cfg.colorbartext =  'Electric Potential Difference (V)';

    figure
    ft_topoplotER(cfg, difference_wave);
    title('Mismatch Negativity (MMN)')

    print -dpng MMN.png

{% include image src="/assets/img/workshop/oslo2019/MMN.png" width="650" %}
_Figure 9: A topographical plot showing the MMN (average over 100 to 170 ms)_

## Bonus: Visualize the temporal evolution of the ERP as a movie

    figure

    cfg        = [];
    cfg.layout = 'natmeg_customized_eeg1005.lay';

    ft_movieplotER(cfg, difference_wave);

Play around with the _zlim_ to get a feeling for how the _difference_wave_ changes topography. Try also plotting the the ERPs themselves.

{% include markup/skyblue %}
**Exercise:** The topographies that we have seen in the figures and movie have a rather loose fit of the circle (representing the head) around the electrodes. Explore the **[ft_prepare_layout](/reference/ft_prepare_layout)** function and [documentation](/tutorial/layout) to improve the topographic representation.
{% include markup/end %}
