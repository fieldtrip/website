---
title: Getting started with Neurodata Without Borders (NWB) data
tags: [dataformat, spike, nwb]
---

# Getting started with Neurodata Without Borders (NWB) data

[Neurodata Without Borders (NWB)](https://www.nwb.org) is a consortium founded to promote data sharing in neuroscience. Among their efforts, NWB created a data standard called *NWB: Neurophysiology (NWB:N)*. Many datasets in this format are already freely available (e.g., [here](https://www.nwb.org/example-datasets/)).

## Introduction

FieldTrip allows reading in spike and LFP data from .nwb files. Importantly, the user has to install the NWB Matlab interface *MatNWB* ([instructions on how to install MatNWB](https://neurodatawithoutborders.github.io/matnwb/)) and run the MatNWB function [*generateCore*](https://neurodatawithoutborders.github.io/matnwb/doc/generateCore.html) successfully before attempting to read files with FieldTrip.

## Example script

```
% Data taken from https://osf.io/hv7ja/
% About the data: https://github.com/rutishauserlab/recogmem-release-NWB

% Optional: Make sure no duplicate versions of +types are in the search path
% restoredefaultpath()

% Navigate to an appropriate working directory (necessary because a few folders and files will be created by MatNWB here)
cd('X:/examplefolder') % change as needed

% Add fieldtrip to search path and initialize
addpath('../fieldtrip') % change as needed
ft_defaults

% Add matnwb to search path
addpath(genpath('../matnwb'))

% (re-)generate core classes for matNWB from it's schema (lands in +types)
generateCore()

% Filename and path
nwbFile = 'X:/examplefolder/sub-YutaMouse41_ses-YutaMouse41-150831_behavior+ecephys.nwb';

% Show schema version of the file. If this does not match your installed version, see 'Change NWB schema version' below
disp(util.getSchemaVersion(nwbFile))

% Load data in nwb format
nwb = nwbRead(nwbFile);
disp(nwb)

% Try to obtain hdr, lfp data and spike data in FieldTrip format
try
	hdr = ft_read_header(nwbFile); % contains no lfp data: throws error
catch ME
	disp('Could not load in hdr information')
	rethrow(ME)
end
try
	dat = ft_read_data(nwbFile); % contains no lfp data: throws error
catch ME
	disp('Could not load in NWB data')
	rethrow(ME)
end
try
	spike = ft_read_spike(nwbFile); % contains spike data: Converts
catch ME
	disp('Could not read in spike data from NWB file.')
	rethrow(ME)
end
 ```

## Change NWB schema version
In case you are trying to load a file using a different schema version than the one installed on your system this may cause an error (often something like 'Unable to resolve the name types.core.DynamicTableRegion'). If so:
- go to the [NWB release site](https://github.com/NeurodataWithoutBorders/nwb-schema/releases),
- choose the schema closest to your file's schema,
- download the zip file associated with that schema,
- copy the files in the zip's \nwb-schema-2.2.1\core into the \nwb-schema\core subfolder of your MatNWB directory (you probably want to make a backup of the original files first).

## Missing functionality

At its current stage, the NWB integration into FieldTrip is not feature-complete. For example:

- Reading events (ft_read_event). NWB:N is a pretty generic dataformat and can contain very diverse types of data. Therefore, it is not trivial to programmatically and reliably create an event output that could be used in a trial function.

- Reading waveforms (voltage time series around identified spikes) by ft_read_spike.
