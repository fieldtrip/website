---
title: Getting started with Blackrock data
category: getting_started
tags: [dataformat, blackrock, lfp, spike]
---

# Getting started with Blackrock data

The specifications of the Blackrock file formats can be found on [the company's website](http://support.blackrockmicro.com/). Blackrock files come in 2 flavors. One file type has the extension `.nev`, and contains information about extracellularly recorded spiking activity. The other file type has as extension `.nsX`, with X any number between 1 and 9. These files contain continuously sampled data, e.g.,  local field potentials.

To read Blackrock data, you will need the NPMK toolbox. The latest version is available from <https://github.com/BlackrockMicrosystems/NPMK>.

## Set the path

To get started, you should add the FieldTrip main directory to your path, and execute the **[ft_defaults](/reference/ft_defaults)** function, which sets the defaults and configures up the minimal required path settings. See also this [frequently asked question](/faq/installation).

    addpath <path_to_fieldtrip>
    ft_defaults

## Reading spike data

To read spike data from `.nev` files, you would do the following

    spike = ft_read_spike('yourfile.nev')

This returns the spike timestamps and waveforms in a format according to **[ft_datatype_spike](/reference/utilities/ft_datatype_spike)**.

## Reading continuous LFP data

To read continuous LFP data from `.nsX` files, you can use the following high-level FieldTrip code

    cfg = [];
    cfg.dataset = 'yourfile.nsX'
    % you can specify additional preprocessing options, such as filters
    data = ft_preprocessing(cfg)

This returns the LFP data in a format according to **[ft_datatype_raw](/reference/utilities/ft_datatype_raw)**.

You can also use the low-level reading functions like this

    hdr = ft_read_header ('yourfile.nsX')
    dat = ft_read_data   ('yourfile.nsX')
    evt = ft_read_event  ('yourfile.nev')  % note that the nsX file does not contain trigger events, but the corresponding nev file does

See this [FAQ](/faq/how_can_i_import_my_own_dataformat) for more details about the high-level and low-level functions.
