---
title: Getting started with Plexon data
category: getting_started
tags: [dataformat, plexon, lfp, spike]
redirect_from:
    - /getting_started/plexon/
---

The Plexon acquisition system writes data to .plx files, and more recent systems like the Omniplex also support a new efficient .pl2 format. Furthermore, the Plexon software and the accompanying NeuroExplorer and OfflineSorter software can write data to .ddt and .nex files. Currently FieldTrip supports legacy .plx file reading code (filetype = plexon_plx), though there is a [plexon V2 patch (filetype = plexon_plx_v2)](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=1795) that uses the official Plexon SDK to make file loading much faster and more robust.

## Introduction

FieldTrip can read Plexon data from the following file formats.

- .ddt
- .nex
- .plx

The .plx files contain the multiplexed raw acquisition data. During acquisition the data arrives in random order from the different continuous and spike channels. The .plx file therefore contains data in many small fragments, which causes the reading of plx files to be slow. The newer plexon .pl2 file recording format doesn't have this limitation. One option for the slow .plx format is to convert the data to the .nex file format. These .nex files also contain the continuous and spike data, but in a orderer format that allows much faster read-access. Using the newer plexon_plx_v2 filetype also greatly speeds up .plx file reading by using the official Plexon SDK (see below).

There are some constraints related to the way that FieldTrip represents continuous and spike data. All main FieldTrip functions read continuous data using the **[ft_read_header](/reference/fileio/ft_read_header)** and **[ft_read_data](/reference/fileio/ft_read_data)** functions. These functions require the continuous data in all channels contained in the file to have the same sampling frequency. This can be a problem because Plexon file formats often contain both 40kHz spike data and 1kHz sampled LFP data in the same file. One solution is to resave all source files into two separate files. The other is to modify the fileio functions to select the correct sampling frequency and channels.

To get started, you should add the FieldTrip main directory to your path, and execute the **[ft_defaults](/reference/ft_defaults)** function, which sets the defaults and configures up the minimal required path settings. See also this [frequently asked question](/faq/matlab/installation).

    addpath <path_to_fieldtrip>
    ft_defaults

## Reading continuous data from a .ddt file

The .ddt format is a Plexon continuous data file optimized for continuous (streaming) recording where every channel is continuously recorded without gaps and the recording includes any dead time between spikes. You can test the .ddt file by trying to read the header and some data from i

    >> hdr = ft_read_header('test1.ddt')
    Warning: creating fake channel names
    > In ft_read_header at 1273

    hdr =
           nChans: 2
               Fs: 40000
         nSamples: 534400
      nSamplesPre: 0
          nTrials: 1
            label: {'1'  '2'}
             orig: [1x1 struct]

    >> dat = ft_read_data('test1.ddt');
    >> plot(dat');

## Reading continuous data from a .nex file

The .nex file format can contain continuous and spike data. To test the reading of continuous data, you can use the **[ft_read_header](/reference/fileio/ft_read_header)** and **[ft_read_data](/reference/fileio/ft_read_data)** functions.

    >> hdr = ft_read_header('p021parall.nex')

    hdr =
                  nChans: 15
                      Fs: 1000
                nSamples: 9463587
                 nTrials: 1
             nSamplesPre: 0
                   label: {15x1 cell}
          FirstTimeStamp: 0
      TimeStampPerSample: 40
                    orig: [1x1 struct]

    % read and plot the first 10 seconds of the first channel
    >> dat = ft_read_data('p021parall.nex', 'chanindx', 1, 'begsample', 1, 'endsample', 10000);
    >> plot(dat);
    % read the events a.k.a. the triggers
    >> event = ft_read_event('p021parall.nex')

After having tested the reading of continuous data, you can use the **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)** functions as explained in the [tutorial documentation](/tutorial).

## Reading spike data from a .nex file

To read the spike data, you should use the **[ft_read_spike](/reference/fileio/ft_read_spike)** function. Since spikes take very little memory, all spikes in all spike channels will be read at once.

    >> spike = ft_read_spike('p021parall.nex')

    spike =
          label: {'sig001a'  'sig002a'  'sig003a'  'sig004a'}
       waveform: {1x4 cell}
           unit: {1x4 cell}
      timestamp: {1x4 cell}
            hdr: [1x1 struct]

If you have read the continuous data using the standard FieldTrip **[ft_preprocessing](/reference/ft_preprocessing)** function, you can subsequently use the **[ft_appendspike](/reference/ft_appendspike)** function to add the spike channels to the continuous LFP data. Once the LFP and spike data are represented in the same datastructure, you can for example compute field-field, field-spike and spike-spike coherence using **[ft_freqanalysis](/reference/ft_freqanalysis)**.

## Reading continuous or spike data from a .plx file

The low-level functions ft_read_header and ft_read_data also work on .plx files, which means that you can use the standard FieldTrip **[ft_preprocessing](/reference/ft_preprocessing)** function. However, the .plx format is a very inefficient format, which makes the reading of subsequent trials rather slow. Instead of reading individual trials, it is recommended that you use the approach that is explained [here](/faq/preproc/datahandling/writedata_matbin).

The FieldTrip **[ft_read_spike](/reference/fileio/ft_read_spike)** function works fine on .plx files. However, note that the .plx files only contain the unsorted spikes.

## Reading triggers and other events

Triggers are in FieldTrip represented as events. These events are read using the **[ft_read_event](/reference/fileio/ft_read_event)** function. The **[ft_definetrial](/reference/ft_definetrial)** function is used to define data segments of interest, i.e. trials, based on the trigger events. After defining the trials, you should use the **[ft_preprocessing](/reference/ft_preprocessing)** function to read the continuous LFP data.

## Using timestamps to synchronize between spikes and LFP

For data that is read from Plexon data files, the timestamps are defined in samples at 40kHz. This is the highest sampling rate of the system annd used for the spikes, whereas the LFP is sampled at 1000 Hz. For the LFP this results in 40 timestamps per sample.

## Using Newer Reading Functions

If you use the [plexon V2 patch (filetype = plexon_plx_v2)](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=1795), then the various fileio reading functions will use the newer official SDK and enable loading of the new .pl2 files. To do so you must specify plexon_plx_v2 when using the fileio functions.

## External links

- http://www.plexoninc.com
- http://www.neuroexplorer.com
