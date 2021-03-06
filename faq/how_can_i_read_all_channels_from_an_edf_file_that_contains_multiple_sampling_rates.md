---
title: How can I read all channels from an EDF file that contains multiple sampling rates?
tags: [faq, edf, preprocessing]
---

# How can I read all channels from an EDF file that contains multiple sampling rates?

The representation of time series data in FieldTrip requires that all channels have the same number of samples, since the data is stored in a Nchan by Nsamples matrix.

EDF files can have channels with different sampling rates. By default the channels with the most common frequency will be read and represented by the low-level functions **[ft_read_header](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_header.m)**, **[ft_read_data](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_data.m)**, and by the high-level **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)** function. Using the _chanindx_ option to **[ft_read_header](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_header.m)**, you can specify another subset of channels from the original EDF file. To represent all channels in a single FieldTrip raw data structure, it is necessary to up-sample (i.e. interpolate) the channels to the highest sampling rate.

The **[edf2fieldtrip](https://github.com/fieldtrip/fieldtrip/blob/release/edf2fieldtrip.m)** detects all sampling frequencies, reads the channels, up-samples and concatenates the channels in a single data structure.
