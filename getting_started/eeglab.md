---
title: Getting started with EEGLAB
tags: [dataformat, eeglab, eeg]
---

# Getting started with EEGLAB

## Background

EEGLAB is an interactive MATLAB toolbox for processing continuous and event-related EEG, MEG and other electrophysiological data using independent component analysis (ICA), time/frequency analysis, and other methods including artifact rejection. EEGLAB incorporates and extends the ICA/EEG toolbox of Makeig, and it provides the user with a graphical interface. The homepage of EEGLAB is located at <http://www.sccn.ucsd.edu/eeglab/>.

## How does FieldTrip use EEGLAB?

FieldTrip integrates EEGLAB functionalities to deal with component analysis. The function **[ft_componentanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_componentanalysis.m)** directly calls EEGLAB functions to perform the desired analysis as represented in the following figure:

![How does FieldTrip use EEGLAB](/assets/img/getting_started/eeglab/FieldTrip_uses_EEGLAB.png)

Note: DIPFIT graphical interface can be used in EEGLAB, but FieldTrip should be installed on the MATLAB path.

## How does EEGLAB use FieldTrip?

EEGLAB integrates FieldTrip functions through the DIPFIT plug-in. This tool allows the localisation of the source signals from the components that have been separated using ICA. The main function used by DIPFIT is **[ft_dipolefitting](https://github.com/fieldtrip/fieldtrip/blob/release/ft_dipolefitting.m)**. It performs a grid search and non-linear fit with one or multiple dipoles and try to find the location where the dipole model is best able to explain the measured EEG topography, using realistic BEM and FEM volume conduction models.
The following figure illustrates some FieldTrip functions used in DIPFIT:

![How does EEGLAB use FieldTrip](/assets/img/getting_started/eeglab/EEGLAB_uses_FieldTrip.png)


## Complementary use of both toolboxes

Users using EEGLAB GUI who want to implement some processing with FieldTrip can follow the following steps:
- Save the dataset from EEGLAB: File → Save current dataset (must be a `.set` file)
- Two methods can be used to import the `.set` file as a FieldTrip structure:
	1. (recommended) Using **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)**:
	```
	cfg 		= [];
	cfg.dataset = 'filename.set';
	eeg 		= ft_preprocessing(cfg);
	```
	2. Load the dataset through **[pop_loadset](https://sccn.ucsd.edu/~arno/eeglab/auto/pop_loadset.html)** and transform it to FieldTrip structure using **[eeglab2fieldtrip](https://github.com/fieldtrip/fieldtrip/blob/release/external/eeglab/eeglab2fieldtrip.m)** function:
	```
	EEG = pop_loadset(filename);
	ft_data = eeglab2fieldtrip(EEG, 'raw');
	```
- Once the data have been processed in FieldTrip, it can be converted back to EEGLAB format using **[fieldtrip2eeglab](https://github.com/fieldtrip/fieldtrip/blob/release/external/eeglab/eeglab2fieldtrip.m)** function. Note that the data (second argument) have to be passed as an array (not a cell):
```
eeglab_data = fieldtrip2eeglab(ft_data.hdr,cat(3,ft_data.trial{:}));
pop_saveset(eeglab_data, 'filename', 'myfilename.set')
```

Notes: 
- To import frequency or timelock data to FieldTrip, **[ft_freqanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_freqanalysis.m)** or **[ft_timelockanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_timelockanalysis.m)** can be used instead of ft_preprocessing, respectively.

- The EEGLAB `.set` and `.fdt` formats are directly supported by the low-level **[ft_read_header](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_header.m)**, **[ft_read_data](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_data.m)** and **[ft_read_event](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_event.m)** functions as well as the high-level function **[ft_definetrial](https://github.com/fieldtrip/fieldtrip/blob/release/ft_definetrial.m)**.

## Design philosophies

Both EEGLAB and FieldTrip work with data structures in MATLAB memory. The design philosophy in EEGLAB is to gather all data from one subject in a single "EEG" structure, and all data from a group of subjects in a "STUDY" structure. This is different from the design philosophy of FieldTrip, which does not gather all results in a single structure, but keeps the results from different analyses in [different structures](/faq/how_are_the_various_data_structures_defined). The following example shows this philosophycal difference:

![FieldTrip-EEGLAB philosophy](/assets/img/getting_started/eeglab/eeglab_FieldTrip_philosophy.png)


Together with the EEGLAB developers we maintain two functions for converting the data back and forth: **fieldtrip2eeglab** and **eeglab2fieldtrip**.