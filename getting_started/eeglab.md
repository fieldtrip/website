---
title: Getting started with EEGLAB
tags: [dataformat, eeglab, eeg]
---

# Getting started with EEGLAB

## Background

EEGLAB is an interactive MATLAB toolbox for processing continuous and event-related EEG, MEG and other electrophysiological data using independent component analysis (ICA), time/frequency analysis, and other methods including artifact rejection. EEGLAB incorporates and extends the ICA/EEG toolbox of Makeig, and it provides the user with a graphical interface. The homepage of EEGLAB is located at <http://www.sccn.ucsd.edu/eeglab/>.

## Using the EEGLAB DIPFIT plug-in

EEGLAB supports external plug-ins and one of them is DIPFIT. With the DIPFIT plugin, you can localize the sources of signal components that have been separated using ICA. The DIPFIT plugin is based on code from Robert Oostenveld, and the same code is included in FieldTrip.

The old version 1.x of DIPFIT only fitted dipoles to EEG data using a 4-shell spherical head model using code that was specific to EEGLAB. The new version 2.x of DIPFIT is completely based on FieldTrip and also supports realistic BEM and FEM volume conduction models for EEG. Currently, EEGLAB cannot support some critical informations about the MEG sensors (the orientations of the gradiometers, mainly) so DIPFIT cannot be use with MEG signals.

To prevent overlapping programming efforts, the DIPFIT version 2.0 plugin uses the forward and inverse methods that are already implemented in FieldTrips **[ft_dipolefitting](https://github.com/fieldtrip/fieldtrip/blob/release/ft_dipolefitting.m)**) function. That means that you can use the DIPFIT graphical interface in EEGLAB, but you should have installed FieldTrip on your MATLAB path.

## Using other FieldTrip functions

Besides using FieldTrip as the underlying "engine" for the DIPFIT plug-in of EEGLAB, it is also possible to export various aspects of your EEGLAB data structure completely to FieldTrip. Subsequently, you can continue your analysis of the data using the command-line FieldTrip functions

Exporting data from EEGLAB to FieldTrip most conveniently done on the MATLAB command line using the **eeglab2fieldtrip** function. That function takes an "EEG" MATLAB structure as input, and will give a MATLAB structure as output that is identical to the output format of one of the standard FieldTrip functions, for example **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)**, **[ft_timelockanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_timelockanalysis.m)** or **[ft_freqanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_freqanalysis.m)**.

The alternative to **eeglab2fieldtrip** is to save the data to disk and use the standard FieldTrip reading and preprocessing functions to read the data directly from disk.

## Converting data between EEGLAB and FieldTrip

Both EEGLAB and FieldTrip work with data structures in MATLAB memory. The design philosophy in EEGLAB is to gather all data from one subject in a single "EEG" structure, and all data from a group of subjects in a "STUDY" structure. This is different from the design philosophy of FieldTrip, which does not gather all results in a single structure, but keeps the results from different analyses in [different structures](/faq/how_are_the_various_data_structures_defined).

Together with the EEGLAB developers we maintain two functions for converting the data back and forth: **fieldtrip2eeglab** and **eeglab2fieldtrip**.

## Reading data in EEGLAB .set format

In EEGLAB you can write your (pre)processed data to disk in the `.set` format, which are accompanied by an `.fdt` file. The `.set` file is actually a MATLAB file in disguise, you can read it using

   load('filename.set', '-mat')
   
which will give you an `EEG` structure in your main workspace. The accompanying `.fdt` files contain the time-series data of all EEG channels in a multiplexed float32 format.

The EEGLAB `.set` and `.fdt` formats are directly supported by the low-level **[ft_read_header](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_header.m)**, **[ft_read_data](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_data.m)** and **[ft_read_event](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_event.m)** functions. This also means that you can use the high-level **[ft_definetrial](https://github.com/fieldtrip/fieldtrip/blob/release/ft_definetrial.m)** and **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)** functions for your analysis script, as explained in the [tutorials](/tutorial).
