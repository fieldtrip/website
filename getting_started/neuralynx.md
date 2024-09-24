---
title: Getting started with Neuralynx data
category: getting_started
tags: [dataformat, neuralynx, lfp, spike]
---

# Getting started with Neuralynx data

## Introduction

The Neuralynx acquisition software writes a variety of file formats.

- .ncs single continuous channel file
- .nse single electrode waveform file
- .nts single stereotrode file
- .nst spike timestamps
- .ntt single tetrode file
- .nev event information

All files acquired during one recording are combined in a common directory. We refer to that directory as the "dataset".

Neuralynx also writes a raw data file (.nrd) in which all the channels are sampled at 32kHz and multiplexed. This file can get very large for the 256 channel recordings (up to 200GB). The standard output format for Neuralynx writes a single file for each channel. All channels together are combined in the "dataset directory". All channels/files within that directory can be read simultaneously.

## Set the path

To get started, you should add the FieldTrip main directory to your path, and execute the **[ft_defaults](/reference/ft_defaults)** function, which sets the defaults and configures up the minimal required path settings. See also this [frequently asked question](/faq/installation).

    addpath <path_to_fieldtrip>
    ft_defaults

## Low-level reading functions

FieldTrip includes a number of low-level reading functions, located in fieldtrip/fileio/private:

- read_neuralynx_bin.m
- read_neuralynx_cds.m
- read_neuralynx_dma.m
- read_neuralynx_ds.m
- read_neuralynx_ncs.m
- read_neuralynx_nev.m
- read_neuralynx_nse.m
- read_neuralynx_nst.m
- read_neuralynx_nts.m
- read_neuralynx_ntt.m
- read_neuralynx_sdma.m
- read_neuralynx_tsh.m
- read_neuralynx_tsl.m
- read_neuralynx_ttl.m

These functions are used to read the actual files. If you are not sure whether your particular file is supported, you can "cd fieldtrip/fileio/private" and do

    read_neuralynx_xxx('fullpath/filename.xxx')   % where XXX is the file format

This returns the content of a single-channel file as a MATLAB structure.

## Working with a complete dataset

To facilitate working with multichannel recordings, FieldTrip has an additional layer on top of the low-level Neuralynx file reading functions. The idea is that all files belonging to a single recording are located in a single directory, which represents the "dataset" as a whole. The FieldTrip functions **[ft_read_header](/reference/fileio/ft_read_header)**, **[ft_read_data](/reference/fileio/ft_read_data)**, **[ft_read_event](/reference/fileio/ft_read_event)** operate on the LFP and spike files in the dataset directory.

The LFP files are used for setting the sample "time" axis. If you only have spike files during a recording, you cannot merge them automatically. Merging is done by reading the LFP files (.nsc), determining the first and last timestamp, and subsequently the spikes are represented as "1" in an other wise "0" channel. So the spike and LFP channels are jointly represented by **[ft_read_data](/reference/fileio/ft_read_data)** in a nchan X nsamples matrix. This is also how the FieldTrip high-level **[ft_preprocessing](/reference/ft_preprocessing)** function accesses the collection of LFP and spike channels in the dataset.

    >> ls dataset/
    Events.Nev  csc01.ncs  csc02.ncs  csc03.ncs  sc1.nse    sc2.nse

    >> hdr = ft_read_header('dataset')

    hdr =
                  nChans: 5
                   label: {'csc028'  'csc028'  'csc028'  'Sc1'  'Sc1'}
                filename: {'dataset/csc01.ncs'  'dataset/csc02.ncs'  'dataset/csc03.ncs'  'dataset/sc1.nse'  'dataset/sc2.nse'}
                 nTrials: 1
                      Fs: 32556
             nSamplesPre: 0
                nSamples: 97792
          FirstTimeStamp: 1007379572
           LastTimeStamp: 1010383712
      TimeStampPerSample: 30.7200
                    orig: [5x1 struct]

You can see from the header that some additional fields are included, such as the filename (needed to link a channel label to the corresponding file), the first timestamp, the last timestamp and the number of timestamps per channel.

It might be that you first only want to process the LFP channels and keep the spike channels separate. You can do that using the **[ft_read_spike](/reference/fileio/ft_read_spike)** function and the **[ft_appendspike](/reference/ft_appendspike)** function.

## Regarding events

The events.nev file (which you probably use) only contains timestamps and not sample numbers. For writing trialfuns (see documentation) and using preprocessing to read the data, you should compute the corresponding sample numbers yourself by using hdr.FirstTimesStamp and hdr.TimeStampPerSample according to

    hdr   = ft_read_header('dataset_directory');
    event = ft_read_event('dataset_directory');

    for i=1:length(event)
      % the first sample in the datafile is 1
      event(i).sample = (event(i).timestamp-double(hdr.FirstTimeStamp))./hdr.TimeStampPerSample + 1;
    end

## Using timestamps to synchronize between spikes and LFP

For data that is read from Neuralynx data files, the timestamps are defined in microseconds, expressed as long integers and hence rounded off to the nearest integer. This corresponds to `1000000/32556=30.7163`, so approximately 31 timestamps per sample.
  
## See also

{% include seealso tag="neuralynx" %}

- [Data File Formats](https://support.neuralynx.com/hc/en-us/articles/360040444811-TechTip-Neuralynx-Data-File-Formats) explained by Neuralynx
