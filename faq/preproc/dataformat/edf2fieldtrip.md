---
title: How can I read all channels from an EDF file that contains multiple sampling rates?
tags: [edf, preprocessing]
category: faq
redirect_from:
    - /faq/how_can_i_read_all_channels_from_an_edf_file_that_contains_multiple_sampling_rates/
    - /faq/edf2fieldtrip/
---

The representation of time series data in FieldTrip requires that all channels have the same number of samples, since the data is stored in a Nchan by Nsamples matrix.

EDF files can have channels with different sampling rates. By default the channels with the most common frequency will be read and represented by the low-level functions **[ft_read_header](/reference/fileio/ft_read_header)**, **[ft_read_data](/reference/fileio/ft_read_data)**, and by the high-level **[ft_preprocessing](/reference/ft_preprocessing)** function. Using the _chanindx_ option to **[ft_read_header](/reference/fileio/ft_read_header)**, you can specify another subset of channels from the original EDF file. To represent all channels in a single FieldTrip raw data structure, it is necessary to up-sample (i.e. interpolate) the channels to the highest sampling rate.

The **[edf2fieldtrip](/reference/edf2fieldtrip)** detects all sampling frequencies, reads the channels, up-samples and concatenates the channels in a single data structure.
