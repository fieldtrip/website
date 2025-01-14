---
title: Getting started with BIDS
category: getting_started
tags: [dataformat, bids]
redirect_from:
    - /getting_started/bids/
---

# Getting started with BIDS

[BIDS](https://bids.neuroimaging.io), the Brain Imaging Data Structure, is a community driven standard to organize neuroimaging data _and_ metadata to make it easier to analyze, archive and share. BIDS is not a data format on itself, but rather a standardized directory structure with standardized file names and agreements on the strategy on sharing metadata to make the dataset more [FAIR](https://www.go-fair.org/fair-principles/).

To read more about BIDS, please see the [website](https://bids.neuroimaging.io) or look up the details in the [specification](https://bids-specification.readthedocs.io/).

## Reading data from a BIDS dataset

FieldTrip has direct support for all data file formats that are used in BIDS. This includes:

- structural and functional MRI
  - NIfTI format (`.nii` and `.nii.gz`)
- MEG
  - [CTF](/getting_started/ctf)
  - [Neuromag/Elekta/Megin](/getting_started/neuromag)
  - [BTi/4D](/getting_started/bti)
- EEG
  - [BrainVision](/getting_started/brainvision)
  - [European Data Format](/getting_started/edf) (`.edf`)
  - [EEGLAB](/getting_started/eeglab)
  - [Biosemi](/getting_started/biosemi) (`.bdf`)
- intracranial EEG
  - [BrainVision](/getting_started/brainvision)
  - [European Data Format](/getting_started/edf) (`.edf`)
  - [Neurodata Without Borders](/getting_started/nwb) (`.nwb`)
  - Multiscale Electrophysiology File Format

Furthermore, there are a number of BIDS extension proposals (so called BEPs) that are likely to be part of the BIDS specification in the near future. Some of these are:

- PET, see <http://bids.neuroimaging.io/bep009>
  - NIfTI format (`.nii` and `.nii.gz`)
- NIRS, see <http://bids.neuroimaging.io/bep030>
  - [SNIRF](/getting_started/snirf)
- motion capture, see <http://bids.neuroimaging.io/bep029>
  - tab-separated files (`.tsv`)

When you read raw data that is represented in the BIDS organization, the corresponding sidecar files are also read. In the case of MEG, EEG and iEEG that means that the corresponding json file and the `_channels.tsv` file are read. Channel names in the original (binary) file format will be overruled with those in the channels file. Also the `_events.tsv` file will be read, events that are in the original (binary) file will be replaced by those from the events file.

If you want to avoid reading the channels and/or events from the BIDS sidecar files, you can specify in the low-level functions the `readbids` or `cfg.readbids` option as 'no'.

## Writing data to a BIDS dataset

Using the **[data2bids](/reference/data2bids)** function you can organize your data according to BIDS. It supports three methods:

- **decorate**: use this if the data is already in the right file format, with the right filename and in the right directory
- **copy**: use this if the data is already in the right file format, but not with the right filename and not in the right directory
- **convert**: use this if the data is in a file format that is not supported by BIDS, or with raw or minimally preprocessed data in MATLAB memory

There are various examples that show how to convert different types of data:

{% include seealso category="example" tag1="bids" %}

## See also

{% include seealso tag="bids" %}