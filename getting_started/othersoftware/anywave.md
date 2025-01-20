---
title: Getting started with AnyWave
parent: Other software
grand_parent: Getting started
category: getting_started
tags: [dataformat, anywave]
redirect_from:
    - /getting_started/anywave/
---

# Getting started with AnyWave

[AnyWave](http://meg.univ-amu.fr/wiki/AnyWave) is an external tool that can be used for visualizing and reviewing continuous EEG, iEEG, and MEG data. It is implemented in C++ and available for Windows, Linux and macOS. The graphics of AnyWave is much faster than **[ft_databrowser](/reference/ft_databrowser)** or MATLAB figure sin general, which is especially valuable if you have many channels and/or a very high sampling rate.

You can export data that has been processing in FieldTrip to a format that AnyWave understands, such as the BrainVision .vhdr format, review the data in AnyWave, and import the marked time windows back into MATLAB.

    % start with the normal preprocessing of your data
    cfg = ...
    data = ft_preprocessing(cfg);


    dat = ft_fetch_data(data);
    hdr = ft_fetch_header(data);
    filename = 'exportfile.vhdr';

    ft_write_data(filename, dat, 'header', hdr);

After writing the data to disk, you open AnyWave, read the data and mark the time windows of interest. You can export the markers to a .mrk file and read that back into MATLAB.

## See also

{% include seealso tag="anywave" %}