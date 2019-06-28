---
title: Getting started with Nicolet data
tags: [nicolet, eeg, dataformat]
---

# Getting started with Nicolet data

Please add information if you're using Nicolet data and want to share info with other FieldTrip users.

## Introduction to the Nicolet file formats

The Nicolet system was once known as Nervus, launched in 1994/5 by Taugagreining in Iceland.  This company was acquired by Viasys, then Carefusion, then Natus. Along the way the EEG system was renamed to Nicolet, then NicoletOne.

It is a popular clinical EEG format, especially in the Nordic countries.

The file format has been through some revisions. FieldTrip can read code from at least 2006 through 2018

- .e can be read in by FieldTrip 
- Older .eeg files probably have the same format with minor changes.

## Limits
The file format supports different sampling rates. Currently the fieldtrip code only reads the channels with the most popular sampling rate. This works well for clinical EEG.

## Integrations
This code enables EEGLAB users to read Nicolet eeg files through the fieldtrip plugin in EEGLAB.

## Short howto
    nicoletfile = 'someNicoletFile.e';
    hdr = ft_read_header();
    dataopts = {};
    data = ft_read_data(nicoletfile, 'header', hdr, dataopts{:});

    % open databrowser for file
    cfg            = [];
    cfg.dataset    = nicoletfile;
    cfg.continuous = 'yes';
    cfg.channel    = 'all';
    data           = ft_preprocessing(cfg);
    cfg.viewmode   = 'vertical';
    ft_databrowser(cfg, data);

