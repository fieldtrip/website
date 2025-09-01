---
title: Spike and LFP dataformats
tags: [dataformat, spike, lfp]
---

## Neuralynx

The standard output format for Neuralynx writes a single file for each channel. All channels together are combined in a directory. This directory can be referred to as the "dataset directory". All channels/files within that directory can be read simultaneously.

Regarding events: the events.nev file (which you probably use) only contains timestamps and not sample numbers. For writing trialfuns (see documentation) and using preprocessing to read the data, you should compute the corresponding sample numbers yourself by using hdr.FirstTimesStamp and hdr.TimeStampPerSample according to

    hdr   = ft_read_header('dataset_directory');
    event = ft_read_event('dataset_directory');

    for i=1:length(event)
      % the first sample in the datafile is 1
      event(i).sample = (event(i).timestamp-double(hdr.FirstTimesStamp))./hdr.TimeStampPerSample + 1;
    end

Regarding spike timestamps (nse, nts): our usual way of dealing with them is by making an all-zero virtual continuous channel, and insert a one at the location of each spike. This is automatically done by the low-level code if you select a spike channel in preprocessing (by means of the low-level neuralynx specific function that is called by **[ft_read_data](/reference/fileio/ft_read_data)**).
