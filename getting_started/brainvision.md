---
title: Getting started with BrainVision Analyzer and Easycap
layout: default
tags: [dataformat, brainvision, eeg, layout]
---

# Getting started with BrainVision Analyzer and Easycap

### Introduction

[Brain Products](http://www.brainproducts.com) provides technical and software solutions for neurophysiological and psychophysiological research and clinical applications. Their BrainAmp ExG amplifier allows to record signals with a sampling rate up to 5000 Hz and a broad hardware bandwidth ranging from DC to 1000 Hz. Brain Products also provides EEG caps, i.e. 'Easycaps', which contain the electrodes distributed over the head. These Easycaps are actually fabricated by http://www.easycap.de, where you can also find more information. Although it is possible to use a BrainAmp amplifier with another type of cap, or to use an Easycap with an different amplifier, the most common case is to use them together and that is why we describe them jointly on this page.

### Preprocessing of raw eeg data

FieldTrip needs the user to define what file to read in. The BrainVision Recorder software usually stores different filetypes (.vhdr, .eeg, .vmrk). For reading the data into FieldTrip you can refer to the .eeg file, for exampl

    cfg = [];
    cfg.dataset = '/users/karlheinz/EEG/myrecording.eeg';
    ...

The .eeg files are the raw data files, i.e. they contain the data as it has been stored upon acquisition.

You can subsequently epoch your data using [ft_definetrial](/reference/ft_definetrial), and you can read in the data and preprocess it using [ft_preprocessing](/reference/ft_preprocessing). Note that in FieldTrip, no unit conversion takes place.

Sometimes users have already done some processing (e.g., rereferencing, epoching, artifact identification) in BrainVision Analyzer, and in order to avoid repeating the time consuming / subjective selection steps it might be preferable to start from the processed data. BrainVision Analyzer stores the processing steps in a so called history file, keeping the raw data unchanged, and applying the processing steps on-the-fly. This is not something that FieldTrip can work with, so you need to export your data first.

### Exporting raw eeg data, applying BVA processing steps

The following describes the recipe to export the processed data into a format the FieldTrip can deal with. It produces a triplet of files (.vhdr, .vmrk and .seg (instead of .eeg)), that can be imported into FieldTrip, in much the same way as described above.
You can do all the preprocessing you want to do in BrainVision Analyzer (e.g. iltering and re-referencing can be done too) and once you have the data segmented the way you want it select 'export > generic data'.  You'll get a window (maybe 2 consecutive windows) popping up asking for various settings.  Leave everything as it is, except make sure the following are se

 1.  For the filename output you should set it to be .seg instead of .eeg (which I think is the default).
 2.  DataFormat should be 'BINARY'
 3.  DataOrientation should be 'MULTIPLEXED'
 4.  Encoding should be 'UTF-8'
 5.  DataType should be 'TIMEDOMAIN'
 6.  BinaryFormat should be 'IEEE_FLOAT_32'

{:.alert-danger}
 At this moment, FieldTrip has problems reading in .dat files, [see our Bugzilla page](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=1567).

{:.alert-info}
Manually renaming BrainVision datafiles will lead to an error because of not simulatenously updated header information. Paul Czienskowski from the MPI for Human Development in Berlin, Germany, has written a small program for renaming that we advise to use:  http://code.google.com/p/eeg-renamer/

{:.alert-info}
When comparing your preprocessed data to preprocessed data from BrainVision Analyzer you might notice subtle differences. This might be due to two reasons: First, the filtersettings of BVA are hard to mimic using FieldTrip, because FieldTrip is using different default settings than BVA. Also, the order of preprocessing steps is fixed in FieldTrip, whereas you have to perform them manually in any order in BVA. The effect of filters or the like will strongly depend on the order of the preprocessing steps.

### Plotting

FieldTrip provides digital layouts for the purpose of plotting data recorded by means of an easycap. These layouts are stored in .mat files and are based on the manufacturer's original drawings, which can also be found as .gif files in the /template/layout directory.

Using FieldTrip, data recorded with Brain Vision hard- and software is readily plotted. It is important that the channel labels match that of the manufacturer specifications. Specify the layout that matches your set-up/easycap when plotting, e.g.

   cfg.layout = 'easycapM1.lay';

Examples regarding the type of plots can be observed **[here](/tutorial/plotting)**. If you want to prepare/create your own layout files, please have a look **[here](/tutorial/layout)**.
