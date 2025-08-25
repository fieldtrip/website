---
title: Getting started with MNE(-python)
category: getting_started
tags: [dataformat, mne, eeg, meg]
redirect_from:
    - /getting_started/mne/
---

# Getting started with MNE(-python)

## Background

MNE-python is an interactive python toolbox for processing EEG, MEG and other electrophysiological data. The homepage of MNE-python is located at <https://mne.tools/stable/>. MNE-python is built on the older MNE-suite software, which has developed around the fif-file format (i.e. the native file format for neuromag/elekta/megin MEG devices), with a strong focus on Minimum Norm source estimation techniques. Based on this historical development scheme, the fif-file format and the representation of data in those files are central to the way in which MNE-python handles their data internally.

## How does FieldTrip use MNE-python?

FieldTrip relies on the m-files in fieldtrip/external/mne, which are copied over from the MNE-matlab toolbox, which is a companion repository to the MNE-python code on [github](https://github.com/mne-tools). FieldTrip data structures can be exported to fif-files, using the **[fieldtrip2fiff](/reference/fieldtrip2fiff)** function. Besides writing the time series into a fif-file, this function makes an attempt to also write some of the metadata in a format the MNE-python can work with.

## How does MNE-python use FieldTrip?

MNE-python has functionality to extract channel time series from FieldTrip structures, by operating on matfiles that contain a supported data structure, **[Raw](https://mne.tools/stable/generated/mne.read_raw_fieldtrip.html)** data containing a single trial, **[Epoched](https://mne.tools/stable/generated/mne.read_epochs_fieldtrip.html)** data containing multiple trials, or **[Evoked](https://mne.tools/stable/generated/mne.read_evoked_fieldtrip.html)** data. This functionality does not allow for the extraction of the relevant metadata from the FieldTrip structures, such as channel position information or events. In many occasions, using this route to import data from FieldTrip, access to the original dataset's header information would be needed (or some metadata needs to be creatively hand-crafted).

## Complementary use of both toolboxes

Both toolboxes share a lot of functionality with respect to time series processing and forward/inverse modelling. FieldTrip's historical perspective is based on CTF MEG data, advanced spectral analysis and beamformers for source reconstruction. MNE-python's historical perspective is based in Elekta/neuromag MEG data, evoked-field analysis, and minimum norm estimation for source reconstruction. These days, however, both toolboxes have moved ahead substantially.

## Practical issues

FieldTrip and MNE-Python have conceptually similar but not identical processing pipelines and data representations. A common pipeline in FieldTrip is to create trials by reading the data directly from disk (in order to have a **[ft_datatype_raw](/reference/utilities/ft_datatype_raw)**) and then use this preprocessed data to create ERP (**[ft_datatype_timelock](/reference/utilities/ft_datatype_timelock)**). In MNE-Python, the whole continuous recording is imported (with the **[Raw](https://mne.tools/stable/generated/mne.read_raw_fieldtrip.html)** class), then trials are extracted with the **[Epoched](https://mne.tools/stable/generated/mne.read_epochs_fieldtrip.html)** class and finally trials are averaged into the **[Evoked](https://mne.tools/stable/generated/mne.read_evoked_fieldtrip.html)** class. The below table shows the correspondence between datatypes in the two packages

| Conceptual                                   | FieldTrip                                               | MNE-Python                                                                  |
| -------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------- |
| one continuous segment of data               | [ft_datatype_raw](/reference/utilities/ft_datatype_raw)           | Raw                                                                         |
| multiple segments of data, e.g., trials       | [ft_datatype_raw](/reference/utilities/ft_datatype_raw), variable length trials are allowed           | Epochs (This datatype is not part of the original MNE Suite written in C), only equal length trials are allowed |
| averaged ERFs for one or multiple conditions | [ft_datatype_timelock](/reference/utilities/ft_datatype_timelock) | Evoked                                                                      |

In order to import data from MNE-python into FieldTrip, it is most straightforward to save the data as a fif-file in MNE-python, and read it into FieldTrip using **[ft_preprocessing](/reference/ft_preprocessing)**. A FieldTrip data structure can be exported to a fif-file using the **[fieldtrip2fiff](/reference/fieldtrip2fiff)** function. Alternatively, MNE-python has functionality to read in mat-files that contain a FieldTrip data structure. In this latter case, however, only the time series information will be imported, and the original header information of the raw data file will often be needed to obtain relevant metadata (or this metadata needs to be handcrafted in MNE-python). **[fieldtrip2fiff](/reference/fieldtrip2fiff)** tries to write channel positions (and events/headshape information) directly into the fif-file, provided that this information is present in the data.

Below are some practical examples that demonstrate how to export FieldTrip data to a fif-file. For this we use the [SubjectBraille.ds](/faq/datasets/#meg-tactile_dipole_fitting) dataset. If you want to try this out yourself, please download [SubjectBraille.zip](https://download.fieldtriptoolbox.org/tutorial/SubjectBraille.zip) and extract the `.ds` folder in a convenient location.

### Example: export raw - single trial - data structure

As a first example, we read the data as a continuous chunk. Note that the example dataset used has actually been acquired in 'trial'-mode, which means that it consists of discontinuous segments of data.

    datadir = <path-to-data>;
    dataset = fullfile(datadir, 'SubjectBraille.ds');
    
    cfg                 = [];
    cfg.dataset         = dataset;
    cfg.trialdef.length = Inf;
    cfg                 = ft_definetrial(cfg);

    cfg.continuous = 'yes'; % see https://www.fieldtriptoolbox.org/faq/continuous/
    cfg.channel    = {'MEG', '-MLP31', '-MLO12'};
    data           = ft_preprocessing(cfg);
    hs             = ft_read_headshape(cfg.dataset); % let's also read this information
    event          = ft_read_event(cfg.dataset);

We can now export the data to a fiff file, pretending as if it's raw data. Note that the original fiff-file definition stores the data in single precision (32-bit per data point) format. By default, FieldTrip stores the data in the same precision of the actual data, which usually is double (and even complex-valued). MNE-python should be capable of dealing with this type of numeric precision, but other software might not. If the data needs to be stored in single precision, you can use the key-value pair `'precision', 'single'`. Also, note that the current example is a bit silly, given that MNE-python is perfectly capable of reading in native CTF data. Here, it is presented as a proof-of-principle.

    fiff_file  = fullfile(datadir, 'ctf-raw.fif');
    fieldtrip2fiff(fiff_file, data, 'headshape', hs, 'event', event);
    save(fullfile(datadir, 'ctf-raw.mat'), 'data'); % for comparison

Including the headshape information as an extra input argument will result in the fif-file to also contain the information about the location of the HPI-coils. This might be relevant for a smooth experience in MNE-python, e.g., if one wishes to apply tSSS to the data.

Also, **[fieldtrip2fiff](/reference/fieldtrip2fiff)** will add the events as specified in the event-structure to the data, provided it is passed as an additional argument to the function. The events will be represented as numbers, in a Nx3 matrix, where the first column contains the sample index of the event, and the third column contains the value. As of April 2023, also an interpretative comment will be saved in the data file (i.e. the mapping from numeric events to annotations), that allows to map the numbered events in the event file back onto the FieldTrip-style event representation.  

### Example: export raw - multiple trial - data structure

MNE-python also allows to work with so-called **Epoched** objects, which are similar to a FieldTrip raw data structure with multiple trials, with the constraint that each of the trials has exactly the same time axis. Let's start by reading the trials into FieldTrip, from the original dataset, and then save the data object as a fiff-file. Event information, if present in the `data` structure's `trialinfo` field will be stored in the fiff-file as well.

    cfg                     = [];
    cfg.dataset             = dataset;
    cfg.trialdef.eventtype  = 'backpanel trigger';
    cfg.trialdef.prestim    = 0.6; % this is constrained by the way the data were collected
    cfg.trialdef.poststim   = 0.6;
    cfg.trialdef.eventvalue = [4 8]; % these are the trigger values coded on the backpanel trigger, indicating targets and non-targets
    cfg                     = ft_definetrial(cfg);
    cfg.channel             = {'MEG', '-MLP31', '-MLO12'}; % read all MEG channels except MLP31 and MLO12
    data                    = ft_preprocessing(cfg);

    fiff_file  = fullfile(datadir, 'ctf-epo.fif');
    fieldtrip2fiff(fiff_file, data);
    save(fullfile(datadir, 'ctf-epo.mat'), 'data');

### Example: export timelocked - evoked field - data structure

Timelocked data can be exported to an **Evoked** object representation:

    cfg        = [];
    cfg.trials = data.trialinfo==8;
    avg        = ft_timelockanalysis(cfg, data);
    fiff_file  = fullfile(datadir, 'ctf-ave.fif');
    fieldtrip2fiff(fiff_file, avg);
    save(fullfile(datadir, 'ctf-ave.mat'), 'avg');
