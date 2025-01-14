---
title: Getting started with Homer
category: getting_started
tags: [dataformat, homer, nirs]
redirect_from:
    - /getting_started/homer/
---

# Getting started with Homer

## Background

Homer is a set of MATLAB scripts used for analyzing fNIRS data to obtain estimates and maps of brain activation. It has evolved since the early 1990s, first as the Photon Migration Imaging toolbox, then HOMER and [Homer2](https://homer-fnirs.org), and development now continues as [Homer3](https://github.com/BUNPC/Homer3)

The Homer software is described in the paper [HomER: a review of time-series analysis methods for near-infrared spectroscopy of the brain](https://doi.org/10.1364/ao.48.00d280). You can download Homer [here on NITRC](https://www.nitrc.org/projects/homer2/) and you can also find more technical documentation on NITRC, for example on the `.nirs` [file format](https://www.nitrc.org/plugins/mwiki/index.php/homer2:Homer_Input_Files#NIRS_data_file_format).

FieldTrip can read data in the `.nirs` format that has been (pre)processed in Homer. This also offers an opportunity to process NIRS data formats in FieldTrip for which we not (not yet) have import functions: you can read them into Homer (or use one of the conversion scripts to convert the data to Homer format), save it to `.nirs` and then continue your analysis using the FieldTrip data structures and functions.

## Reading data in Homer .nirs format

The Homer `.nirs` format is technically a MATLAB file in disguise. It contains multiple variables and structures that you should combine in one top-level `nirs` structure. You can read it with

    nirs = load(filename, '-mat');
    
By specifying the output variable `nirs` to the MATLAB [load](https://nl.mathworks.com/help/matlab/ref/load.html) function, all separate variables contained in the file are grouped together in a structure. Subsequently you could update/change that structure and save it back to disk with
    
    save(filename, 'nirs', -struct');
    
The `.nirs` files are directly supported by the low-level **[ft_read_header](/reference/fileio/ft_read_header)**, **[ft_read_data](/reference/fileio/ft_read_data)** and **[ft_read_event](/reference/fileio/ft_read_event)** functions. This also means that you can use the high-level **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)** functions for your analysis script, as explained in the [tutorials](/tutorial).
