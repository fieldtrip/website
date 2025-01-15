---
title: Getting started with CTF data
parent: MEG
grand_parent: Getting started
category: getting_started
tags: [dataformat, ctf, meg]
redirect_from:
    - /getting_started/ctf/
---

# Getting started with CTF data

{% include markup/green %}
The company based in Coquitlam (BC, Canada) making these MEG systems was initially called CTF, later renamed to VSM-MedTech, then operated as MISL (MEG International Services Ltd.), and now goes with the name CTF again. We refer to all of these incarnations with "CTF".
{% include markup/end %}

## Introduction

The following data files can be read and used in FieldTrip: .meg4, .res4, .mri, .hdm, ClassFile.cls, MarkerFile.mrk. All required CTF reading functions are supplied with the FieldTrip toolbox.

Initially, reading functions for CTF files were implemented from scratch by the FieldTrip developers. However, in 2008 we switched to the reading functions that are provided (but not officially maintained) by CTF. The new CTF reading functions are located in the external/ctf directory and will be automatically called by the appropriate FieldTrip functions.

These low-level functions are written by Dr. Harold Wilson and courtesy of MISL. These are not used for clinical studies and the user assumes all risk with their use. Although the functions originate from MISL, these are included in in FieldTrip under the explicit agreement that MISL does not support these functions. If you find bugs or have suggestions for improvements, please contact the FieldTrip developers and not MISL.

An alternative ("old") implementation for reading the CTF data is available in the read_ctf_xxx functions, which can be used by specifying 'ctf_old' as headerformat and dataformat.

The following types of CTF data can be read and used in FieldTrip:

- MEG/EEG and AUX data: .res4, .meg4, .1_meg4, .2_meg4, etc.
- event information: .meg4, ClassFile.cls, MarkerFile.mrk
- single sphere and multi-sphere volume conduction models: .hdm
- anatomical MRI: .mri

This page explains how to get started reading and using each of these file types in FieldTrip.

## Background

The CTF system records all data in a file format that consists of epochs or trials. These epochs can be linked to a trigger that was specified prior to acquisition, in which case there is a time gap between the epochs in which no data is present in the file. Another option is to specify that the epochs are to be continuously recorded. The file still represents the epochs, but triggers are not located at a specific sample in each epochs and there are no time gaps in between epochs. When there are no time-gaps between the epochs in the file, the data in the file is pseudo-continuous.

Besides the main CTF recording modus in epoched files (with or without gaps between trials), the CTF acquisition software also allows for additionally writing the data to an auxiliary file that represents the data in a proper continuous representation. Although the representation in the AUX file is conceptually more convenient than the pseudo-continuous format, the disadvantage is that acquisition takes 2x more space on disk. Hence, in many labs only the pseudo-continuous format is stored to disk.

MEG datasets recorded with CTF acquisition software are written in a xxx.ds folder (with xxx the name of your dataset). This folder contains, among others, the xxx.meg4 file which contains the data of your recording, and the xxx.res4 file which contains the header information.

You should not store any scripts or mat files in the xxx.ds folder. When analyzing your CTF MEG data with FieldTrip, it is good practice to keep three separate folder

1.  a folder with the raw recorded data (i.e., containing your xxx.ds dataset)
2.  a folder that contains your MATLAB scripts
3.  a folder that contains the MATLAB/FieldTrip data that you want to save

## Set the path

To get started, you should add the FieldTrip main directory to your path, and execute the **[ft_defaults](/reference/ft_defaults)** function, which sets the defaults and configures up the minimal required path settings. See also this [frequently asked question](/faq/installation).

    addpath <path_to_fieldtrip>
    ft_defaults

## Reading MEG data

To analyze your CTF MEG data in FieldTrip, you would usually start by calling high-level functions such as **[ft_definetrial](/reference/ft_definetrial)** or **[ft_preprocessing](/reference/ft_preprocessing)** (see the [tutorial documentation](/tutorial)). These functions read the raw MEG data by calling low-level functions such as **[ft_read_header](/reference/fileio/ft_read_header)** and **[ft_read_data](/reference/fileio/ft_read_data)**. The header and data are in different files, and the data itself can be split over multiple 2GB files. You specify the combination of files as a dataset, i.e. with the directory

    cfg.dataset = 'Subject01.ds';

FieldTrip automatically figures out what the actual header and datafiles are.

To get started with reading your CTF MEG data into FieldTrip, it might be a good check to call the low-level reading functions directly. As an example for the code below, we will use the [Subject01.zip](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip) tutorial dataset.

### Read header

The **[ft_read_header](/reference/fileio/ft_read_header)** function reads header information and represents it in a common data-independent format. It takes the dataset filename as input. Alternatively, you can directly specify the header file.

To read the header from the tutorial dataset, use

    hdr = ft_read_header('Subject01.ds')

or

    hdr = ft_read_header('Subject01.ds/Subject01.res4')

This should return a header structure with the following element

    hdr =

               Fs: 300           % sampling frequency
           nChans: 187           % number of channels
         nSamples: 900           % number of samples per trial
      nSamplesPre: 300           % number of pre-trigger samples in each trial
          nTrials: 266           % number of trials
            label: {187x1 cell}  % cell-array with labels of each channel
             grad: [1x1 struct]  % gradiometer structure
             orig: [1x1 struct]  % additional header information

Make sure that the header information is correctly read.

### Read data

The **[ft_read_data](/reference/fileio/ft_read_data)** function reads the CTF MEG data and represents it in a common data-independent format. It takes the dataset filename as input. Alternatively, you can directly specify the data file.

To read the data from the tutorial dataset, use

    dat = ft_read_data('Subject01.ds');

or

    dat = ft_read_data('Subject01.ds/Subject01.meg4');

This returns a 3-D matrix of size Nchans*Nsamples*Ntrials: 187x900x266 in case of the tutorial data, which is a trial-based dataset. In case of continuous data, this function returns a 2-D matrix of size Nchans\*Nsamples.

Additional options should be specified in key-value pairs (see **[ft_read_data](/reference/fileio/ft_read_data)**). When only the filename is specified, all data in the dataset will be read. To only read the first 3 trials from channels 5-9, us

    dat = ft_read_data('Subject01.ds', 'begtrial', 1, 'endtrial', 3, 'chanindx', [5:9]);

This returns a 3-D matrix of size Nchans*Nsamples*Ntrials: 5x900x3.

You can explicitly specify the data format (also [see below](#Specifying the low-level reading functions)), e.g.

    dat = ft_read_data('Subject01.ds', 'dataformat', 'ctf_ds');

### Preprocessing

After checking that the low-level reading functions successfully read your CTF dataset, you are ready to start working with the high-level FieldTrip functions, such as **[ft_preprocessing](/reference/ft_preprocessing)**. To preprocess the tutorial data, us

    cfg=[];
    cfg.dataset = 'Subject01.ds';
    data = ft_preprocessing(cfg)

This should return the following data structure:

    data =

          hdr: [1x1 struct]    % header information
        label: {187x1 cell}    % channel labels
        trial: {1x266 cell}    % data (Nchans*Nsamples) for each trial
         time: {1x266 cell}    % time axis for each trial
      fsample: 300             % sampling frequency
         grad: [1x1 struct]    % gradiometer structure
          cfg: [1x1 struct]    % the configuration used for processing the data

With cfg.continuous = 'yes' or 'no' you can specify whether the file contains continuous data. The default is determined automatically. Data that is measured pseudo-continuously should be treated as cfg.continuous = 'yes'.

For more preprocessing options and information on how to define trials, see the [tutorial documentation](/tutorial).

### Specifying the low-level reading functions

The default low-level reading functions for the MEG data are the functions supplied by CTF, which are located in the fieldtrip/external/ctf directory. There is also an old implementation of the reading functions, which will be used if you specify

    cfg.headerformat = 'ctf_old'
    cfg.dataformat   = 'ctf_old'

in **[ft_preprocessing](/reference/ft_preprocessing)** or in any of the other FieldTrip functions that reads the data from disk.
Other dataformat options include 'ctf_ds', 'ctf_meg4' and 'ctf_res4'.

### Reading 64-channel CTF data

The old 64-channel CTF datasets are not supported in the native CTF reading functions. However, they do seem to work with the old reading functions. So if you specify the headerformat, eventformat and the dataformat as 'ctf_old', you can analyze the old 64-channel data.

## Reading events

Usually, you would call **[ft_definetrial](/reference/ft_definetrial)** to select pieces of data around those events in the data that interest you, either using a generic definition or using your own “trialfun”. The trialfunction calls the low-level reading function **[ft_read_event](/reference/fileio/ft_read_event)**. The **[ft_read_event](/reference/fileio/ft_read_event)** function reads event information and represents it in a common data-independent format. It takes the dataset filename as input. Alternatively, you can directly specify the data file.

**[ft_read_event](/reference/fileio/ft_read_event)** reads the triggers from the trigger channels in the MEG dataset (.meg4), and if available classified trials from the classification file (ClassFile.cls) and markers from the marker file (MarkerFile.mrk), and combines all the available events into one structure. For more information on events, triggers and trials refer to the [faq](/faq/what_is_the_relation_between_events_such_as_triggers_and_trials?).

To read the events from the [tutorial data](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip), use

    event = ft_read_event('Subject01.ds')

This automatically reads the events from the trigger channels, from the class file and from the marker file and combines them in a single uniform representation. On the tutorial dataset it returns the following event structure:

    event =
        1343x1 struct array with fields:
        type
        sample
        value
        offset
        duration

To access the first event, use

    >> event(1)

    ans =
          type: 'trial'
        sample: 1
         value: []
        offset: -300
      duration: 900

### Frontpanel and Backpanel triggers

The 151 channel MEG system we started off with at the Donders in 2002 had an electronics rack which was placed such that there was a clear front and back side. Each side of the rack exposed 16 binary inputs (i.e. bits) for connecting external triggers. To the front we connected the button boxes, to the back we connected the stimulus presentation computer. The 16 bits from the front and from the back were combined in the 32-bit STIM channel.

Given the connections of the button boxes and stimulus computers, in the analysis the 32-bit STIM channel values did not match the users' expectations with respect to button box and presentation trigger codes. Therefore the FieldTrip reading software back then was implemented to split the 32-bits into the 16 frontpanel and the 16 backpanel bits. This also shifts the bits to recover the trigger codes that were used in the presentation software by the users. This situation from early '2000 at the Donders in Nijmegen is still supported by FieldTrip. The "Subject01.ds" tutorial dataset is from that time, so that is why you still see it in the tutorials.

The front and back panel at other CTF sites with the old electronics rack may be (or have been) connected differently. Furthermore, the present CTF systems have more trigger input options and no front and back side any more, so better don't use those any more in your analyses. In many cases UPPT001 and similarly named channels are the interesting trigger channels. MEG data acquired with the older CTF systems uses the STIM channel. If you want to relate FieldTrip to the CTF software, you will have to focus on the STIM and UPPT channels.

So please be aware that "frontpanel" and "backpanel" are Donders conventions that have ended up in FieldTrip, but may not be of any relevance to you.

## Reading headmodels

Single sphere and multi sphere headmodels can be prepared using the CTF software MRIViewer and the CTF command-line utility localSpheres. Both CTF programs will write the headmodel to a .hdm file. The .hdm headmodel files can be read using **[ft_read_headmodel](/reference/fileio/ft_read_headmodel)** and visualized using **[ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)**. Alternative to using the CTF software, you can also use the FieldTrip function **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** to create MEG headmodels.

For example, to read and plot the single sphere model produced with CTF software for the [tutorial data](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip), use

    % read and plot the head shape
    headshape = ft_read_headshape('Subject01.shape');
    ft_plot_headshape(headshape)

    % read and plot the single sphere head model that was constructed with the CTF software
    headmodel = ft_read_headmodel('Subject01.hdm');
    ft_plot_headmodel(headmodel)
    alpha 0.8
    camlight

    % read and plot the gradiometers
    grad = ft_read_sens('Subject01.ds', 'senstype', 'meg');
    ft_plot_sens(grad, 'chantype', 'meggrad') % not the reference channels

For more information on reading, creating and plotting headmodels refer to [this page](/example/make_leadfields_using_different_headmodels).

## Reading MRI files

Anatomical MRI files can be converted into CTF compatible data using the CTF software MRIConverter and MRIViewer. After this process, a .mri file is saved which can be used in FieldTrip.

- Open the original MRI data in MRIConverter
- Make sure that the View Direction and Image Orientation are correctly set
- Save the file in the .mri format
- Open the newly created .mri file in MRIViewer
- Mark the fiducials: left and right ear and nasion; they should reflect the location of the MEG coils
- Save the changes in the .mri file

The .mri file can be read into FieldTrip using **[ft_read_mri](/reference/fileio/ft_read_mri)**. To read the mri file of the [tutorial data](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip), use

    mri = ft_read_mri('Subject01.mri');

The anatomical mri can be visualized using **[ft_sourceplot](/reference/ft_sourceplot)**,

    cfg = [];
    ft_sourceplot(cfg, mri)

To enter interactive mode, i.e, to browse through the volume, use

    cfg = [];
    cfg.interactive = 'yes';
    ft_sourceplot(cfg, mri)

The anatomical MRI can subsequently be used for e.g., plotting source localization results (see the [plotting tutorial](/tutorial/plotting#plotting_data_at_the_source_level)) or for preparing a headmodel (see the [beamformer tutorial](/tutorial/beamformer#the_forward_model_and_lead_field_matrix)).

## See also

{% include seealso tag="ctf" %}