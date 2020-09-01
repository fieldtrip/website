---
title: Getting started with Blackrock data
tags: [dataformat, blackrock, lfp, spike]
---

# Getting started with Blackrock data

FIXME This getting started guide and the reading code are still under development, see [bugzilla](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=2964).

However, we very much welcome you to start using this functionality, and would be happy with any feedback provided.

## Introduction

The specifications of this data format can be found on [the company's website](http://support.blackrockmicro.com/KB/View/166838-file-specifications-packet-details-headers-etc). Basically, the files come in 2 flavors. One type of file has as extension .nev, and contains information about extracellularly recorded spiking activity. The other file type has as extension .nsX, with X any number between 1 and 9. These files contain continuously sampled data (e.g. Local Field Potentials).

To read Blackrock data into FieldTrip, you will need the NPMK toolbox. The latest version of it can be cloned from github: https://github.com/BlackrockMicrosystems/NPMK. This is a MATLAB-toolbox provided by Blackrock microsystems. FieldTrip relies on the low-level reading functionality of this code. Make sure that the .m files in the NPMK toolbox are on the MATLAB path.

To get started, you should add the FieldTrip main directory to your path, and execute the **[ft_defaults](https://github.com/fieldtrip/fieldtrip/blob/release/ft_defaults.m)** function, which sets the defaults and configures up the minimal required path settings. See also this [frequently asked question](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path).

    addpath <path_to_fieldtrip>
    ft_defaults

## Reading header information

To read header information, use

    filename = 'your_cyberkinetics_file.nev';
    hdr = ft_read_header(filename, 'headerformat', 'neuroshare');

This calls the NPMK toolbox and gives back the header structure in FieldTrip format, which includes the original header information (included as hdr.orig) as retrieved with the neuroshare functions _openNSx_ or _openNEV_.

## Reading triggers and other events

To read events, use

    filename = 'your_datafile';
    event = ft_read_event(filename, 'eventformat', 'neuroshare');

TO BE DONE.

## Reading LFP data

To read analog data, use

    filename = 'your_datafile.ns1';
    data = ft_read_data(filename);

This calls the NPMK toolbox (using the function _openNSx_) and gives back a data structure in FieldTrip format.

Optional input arguments should be specified in key-value pairs and may include

    %   'chanindx'   = list with channel indices to read
    %   'begsample   = first sample to read
    %   'endsample   = last sample to read

TO BE DONE.

## Reading spike data

To read spike data, use

    filename = 'your_cyberkinetics_file.nev';
    spike = ft_read_spike(filename, 'spikeformat', 'neuroshare');

TO BE DONE.

## External links

- [Blackrock Microsystems](http://www.blackrockmicro.com), formerly the Research Products Division of Cyberkinetics Inc.
