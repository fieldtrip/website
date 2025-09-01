---
title: Getting started with BrainVision Analyzer and Easycap
category: getting_started
tags: [dataformat, brainvision, easycap, eeg, layout]
redirect_from:
    - /getting_started/brainvision/
---

## Introduction

[BrainProducts GmbH](http://www.brainproducts.com) provides technical and software solutions for neurophysiological and psychophysiological research and clinical applications. Their BrainAmp ExG amplifier allows to record signals with a sampling rate up to 5000 Hz and a broad hardware bandwidth ranging from DC to 1000 Hz.

BrainProducts also provides EEG caps with the electrodes distributed over the head according to the 1020 standard or to an equidistant scheme. Most of the caps provided by BrainProducts are actually fabricated by [EasyCap](http://www.easycap.de), on whose website you can find more information. Although it is possible to use a BrainAmp amplifier with another type of cap, or to use an Easycap with an different amplifier, the most common case is to use them together and that is why we describe them jointly on this page.

##  BrainVision data format

The BrainVision data format consists of three separate files:

1. A text header file (`.vhdr`) containing meta data
2. A text marker file (`.vmrk`) containing information about events in the data
3. A binary data file (`.eeg`) containing the voltage values of the EEG

Both text files are based on the Microsoft Windows INI format consisting of:

- sections marked as `[square brackets]`
- comments marked as `; comment`
- key-value pairs marked as `key=value`

{% include markup/skyblue %}
The BrainVision Recorded and Analyzer software packages use a well-defined file format that is supported by many software packages (e.g., FieldTrip, EEGLAB, SPM, MNE-Python) and that is used in [BIDS for EEG](https://psyarxiv.com/63a4y). The details of the BrainVision data format are available from the [BrainProducts website](https://www.brainproducts.com/productdetails.php?id=21&tab=5).
{% include markup/end %}

For example, see this excerpt from a BrainVision header file (.vhdr):

    Brain Vision Data Exchange Header File Version 1.0
    ; Data synthesized by MNE-BIDS

    [Common Infos]
    DataFile=test.eeg
    MarkerFile=test.vmrk

In this short example we can observe a challenge that is caused by having three separate files for each dataset: It means that the single files have internal pointers to each other's locations (see the DataFile and MarkerFile keys in the example).

{% include markup/skyblue %}
Manually renaming BrainVision datasets may lead to errors, since the .vhdr and .vmrk file headers contain the name of the linked data file. Paul Czienskowski from the MPI for Human Development in Berlin, Germany, has written a small windows program that you can use: http://code.google.com/p/eeg-renamer/. Or you can use [this MATLAB function](https://gist.github.com/CPernet/e037df46e064ca83a49fb4c595d4566a). When renaming a single or small number of datasets, you could also use a text editor to fix the header.
{% include markup/end %}

{% include markup/green %}
For validation of BrainVision file triplets, you can use the [brainvision-validator](https://github.com/sappelhoff/brainvision-validator), which is a command line tool developed in nodejs.
{% include markup/end %}

## Preprocessing of raw EEG data

FieldTrip needs the user to define what file to read in. The BrainVision Recorder software usually stores different filetypes (.vhdr, .eeg, .vmrk). For reading the data into FieldTrip you can refer to the .eeg file, for example.

    cfg = [];
    cfg.dataset = '/users/karlheinz/EEG/myrecording.eeg';
    ...

The .eeg files are the raw data files, i.e. they contain the data as it has been stored upon acquisition.

You can subsequently epoch your data using [ft_definetrial](/reference/ft_definetrial), and you can read in the data and preprocess it using [ft_preprocessing](/reference/ft_preprocessing). Note that in FieldTrip, no unit conversion takes place.

Even for raw data, the data are considered segmented by FieldTrip. The data file is considered as a very long segment starting with the event "New Segment" and ending at the end of the recording. As a way to investigate the specificities of the BrainVision file, I would recommend always checking the .vmrk file by either opening it in a text editor, or using the function ft_definetrial with configuration cfg.trialdef.eventtype = '?'.

## Exporting raw EEG data after doing processing in BrainVision Analyzer

Sometimes users have already done some processing (e.g., rereferencing, epoching, artifact identification) in BrainVision Analyzer, and in order to avoid repeating the time consuming / subjective selection steps, it might be preferable to start from the processed data. BrainVision Analyzer stores the processing steps in a so called history file, keeping the raw data unchanged, and applying the processing steps on-the-fly. This is not something that FieldTrip can work with, so you need to export your data first.

The following describes the recipe to export the processed data into a format the FieldTrip can deal with. It produces a triplet of files (.vhdr, .vmrk and .dat (instead of .eeg)), that can be imported into FieldTrip, in much the same way as described above.
You can do all the preprocessing you want to do in BrainVision Analyzer (e.g., filtering and rereferencing can be done too) and once you have the data segmented the way you want it select 'export > generic data'. You'll get a window (maybe 2 consecutive windows) popping up asking for various settings. Leave everything as it is, except make sure the following are set:

1.  The filename for output should be .dat instead of .eeg (which I think is the default)
2.  DataFormat should be 'BINARY'
3.  DataOrientation should be 'MULTIPLEXED'
4.  Encoding should be 'UTF-8'
5.  DataType should be 'TIMEDOMAIN'
6.  BinaryFormat should be 'IEEE_FLOAT_32'

{% include markup/skyblue %}
When comparing your preprocessed data from FieldTrip to preprocessed data from BrainVision Analyzer, you might notice subtle differences. This might be due to two reasons: First, the filtersettings of BVA are hard to mimic using FieldTrip, because FieldTrip is using different defaults. Also, the order of preprocessing steps is fixed in FieldTrip, whereas you have to perform them manually, which makes it possible to do them in any order in BVA. The effect filters have on your data depend on the order of the preprocessing steps.
{% include markup/end %}

## Plotting

Using FieldTrip, data recorded with BrainProducts hard- and software is readily plotted. It is important that the channel labels match that of the manufacturer specifications.

FieldTrip provides template electrode layouts for plotting data recorded with BrainProducts and EasyCap electrode caps. These layouts are stored in .mat files and are based on the manufacturer's original drawings, which can also be found bitmaps on the [template layout](/template/layout/#easycap) page.

Specify the layout that matches your set-up when plotting, for example:

    cfg.layout = 'easycapM1.mat';

Examples regarding the type of plots can be observed [here](/tutorial/plotting). In the [template](/template/layout) directory you can find a collection of template layouts for plotting. If you want to create your own custom layout files, please have a look [here](/tutorial/plotting/layout).

## See also

{% include seealso tag="brainvision" %}
