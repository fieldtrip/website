---
title: Getting started with MNE(-python)
tags: [dataformat, mne, eeg, meg]
---

# Getting started with MNE(-python)

## Background

MNE-python is an interactive python toolbox for processing EEG, MEG and other electrophysiological data. The homepage of MNE-python is located at <https://mne.tools/stable/>. MNE-python is built on the older MNE-suite software, which has developed around the fif-file format (i.e. the native file format for neuromag/elekta/megin MEG devices), with a strong focus on Minimum Norm source estimation techniques. Based on this historical development scheme, the fif-file format and the representation of data in those files are central to the way in which MNE-python handles their data internally.

## How does FieldTrip use MNE-python?

FieldTrip relies on the m-files in fieldtrip/external/mne, which are copied over from the MNE-matlab toolbox, which is a companion repository to the MNE-python code on [github](https://github.com/mne-tools). FieldTrip data structures can be exported to fif-files, using the **[fieldtrip2fiff](/reference/fieldtrip2fiff)** function.  

## How does MNE-python use FieldTrip?

MNE-python has functionality to extract channel time series from FieldTrip structures, by operating on matfiles that contain a supported data structure, [raw](https://mne.tools/stable/generated/mne.read_raw_fieldtrip.html) data containing a single trial, [epoched](https://mne.tools/stable/generated/mne.read_epochs_fieldtrip.html) data containing multiple trials, or [evoked](https://mne.tools/stable/generated/mne.read_evoked_fieldtrip.html) data. 

## Complementary use of both toolboxes

## Practical issues 
