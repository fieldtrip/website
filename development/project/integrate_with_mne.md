---
title: Integrate FieldTrip and MNE-Python
---

{% include /shared/development/warning.md %}

Not all the information contained in either MATLAB or Python can be completely copied into the other format.

We cannot assure that the API in MNE-Python will remain the same in the future. Please, report any error on [bugzilla](/bugzilla) and include this address ''bugzilla@gpiantoni.com'' to the CC list in the bugreport.

Code under development, the mne-python community currently works on reader functions for FieldTrip data structure
[https://github.com/mne-tools/mne-python/pull/5141](https://github.com/mne-tools/mne-python/pull/5141), [https://github.com/mne-tools/mne-python/issues/4833](https://github.com/mne-tools/mne-python/issues/4833)

More functions to work with files coming from MNE-python in MATLAB are available at [https://github.com/mne-tools/mne-matlab](https://github.com/mne-tools/mne-matlab).

# Integrate FieldTrip and MNE-Python

## Introduction

FieldTrip and MNE-Python offer tools to analyze electrophysiological activity.
[MNE-Python](http://martinos.org/mne/stable/index.html), with code available at [github.com](https://github.com/mne-tools/mne-python), facilitates the access to the FIFF files and integrates with the [MNE suite](http://martinos.org/mne/stable/index.html), written in C (FieldTrip can also use some of the functions in the MNE suite, as explained in the [minimum-norm estimate tutorial](/tutorial/minimumnormestimate)). In addition, MNE-Python allows for a variety of tools for the analysis of electrophysiological data, as demonstrated in the [example gallery](http://martinos.org/mne/stable/auto_examples/index.html).

Primary use cases for the integration of FieldTrip and MNE-Python are

- the ability for MNE users do channel-level time-frequency analysis and sensor-level statistics in FieldTrip.
- the ability for FieldTrip users to do source reconstruction in MNE.

## Background

FieldTrip and MNE-Python have similar but not identical processing pipelines. A common pipeline in FieldTrip is to create trials by reading the data directly from disk (in order to have a **[ft_datatype_raw](/reference/ft_datatype_raw)**) and then use this preprocessed data to create ERP (**[ft_datatype_timelock](/reference/ft_datatype_timelock)**). In MNE-Python, the whole continuous recording is imported (with the **Raw** class), then trials are extracted with the **Epochs** class and finally trials are averaged into the **Evoked** class. To recap, this is the correspondence between datatypes in the two package

| Conceptual                                   | FieldTrip                                               | MNE-Python                                                                  |
| -------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------- |
| one continuous segment of data               | [ft_datatype_raw](/reference/ft_datatype_raw)           | Raw                                                                         |
| multiple segments of data, e.g. trials       | [ft_datatype_raw](/reference/ft_datatype_raw)           | Epochs ((This datatype is not part of the original MNE Suite written in C)) |
| averaged ERFs for one or multiple conditions | [ft_datatype_timelock](/reference/ft_datatype_timelock) | Evoked                                                                      |

Therefore, we will need to import and export Raw, Epochs, and Evoked datatypes.

The aim is to pass the channel=level data between FieldTrip and MNE. Reading is implemented through the **[ft_read_header](/reference/ft_read_header)** and **[ft_read_data](/reference/ft_read_data)** functions. Writing is implemented through the ad-hoc **[fieldtrip2fiff](/reference/fieldtrip2fiff)** function.

## Procedure

### datatype_raw (one trial) `<->` Raw

For these examples, we'll use the example data of [dataset 10](/faq/what_types_of_datasets_and_their_respective_analyses_are_used_on_fieldtrip#meg-tactile_dipole_fitting). Download [SubjectBraille.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/SubjectBraille.zip) and extract the ''.ds'' folder in a convenient location.

#### Export to Raw

First, we read the data, as usua

    cfg = [];
    cfg.dataset = 'SubjectBraille.ds';
    cfg.trialdef.triallength = Inf;
    cfg = ft_definetrial(cfg);

    cfg.continuous = 'yes';
    cfg.channel = {'MEG', '-MLP31', '-MLO12'};
    data = ft_preprocessing(cfg);

Then, we export them

    fiff_file  = 'ctf_raw.fif';
    fieldtrip2fiff(fiff_file, data)

This function will also attempt to create an event file, called ''ctf_raw-eve.fif''. Because the fiff format is less flexible than the MATLAB files, events might be recoded using numbers.

You can then read the file into Python (MNE-Python 0.8)

```python
    from mne.io import Raw
    raw = Raw('ctf_raw.fif')
    print(raw)
    print(raw.info)

    from mne import read_events
    events = read_events('ctf_raw-eve.fif')
    print(events)
```

#### Import Raw

Once you have the data in Python as Raw, you can use the ''save'' method.

```python
    raw.save('mne_python_raw.fif')
```

Then use FieldTrip to read the file

    fiff_file = 'mne_python_raw.fif';

    cfg = []
    cfg.dataset = fiff_file;
    data1 = ft_preprocessing(cfg);
    ft_datatype(data1)  % returns 'raw'

    event = mne_read_events('ctf_raw-eve.fif')

So, ''data1'' is of type ''datatype_raw'' with one trial.

Events are in Nx3 matrix, where the first column contains the samples and the third column the index of the events. You can use this information to create the trials in FieldTrip.

### datatype_raw (many trials) `<->` Epochs

#### Export to Epochs

Currently, there is no export functionality to create mne-Epochs from fieldtrip. Feel free to add it on [https://github.com/fieldtrip/fieldtrip](https://github.com/fieldtrip/fieldtrip).

And then in Python, you can read the ''Epochs'' with:

```python
    from mne import read_epochs
    epochs = read_epochs('ctf-epo.fif')
    print(type(epochs))
```

#### Import Epochs

If we have the data as ''Raw'' in MNE-Python, we can create epochs, using the ''Epochs'' class

```python
    from mne import read_events, Epochs
    from mne.fiff import Raw

    raw = Raw('ctf_raw.fif')
    events = read_events('ctf_raw-eve.fif')
    print(events)

    # create events based on the index in the third column of events
    event_ids = {'eventA': 4, 'eventB': 8}
    tmin = -0.5
    tmax = 1
    epochs = Epochs(raw, events, event_ids, tmin, tmax, baseline=(None, 0))
    epochs.save('mne_python-epo.fif')
    mne.write_events('mne_python-eve.fif', epochs.events)
```

And then in MATLAB

    fiff_file = 'mne_python-epo.fif';
    events_file = 'mne_python-eve.fif';
    cfg = [];
    cfg.dataset = fiff_file;
    data1 = ft_preprocessing(cfg);

    event_file = mne_read_events(events_file);
    data1.trialinfo = event_file(:,3);
    data1.cfg.trl(:,4) = event_file(:,3);

    ft_datatype(data1)  % returns 'raw'

where ''data1'' contains the data organized in multiple trials.

Better, one could also use the inbuilt-function [ft_definetrial](/reference/ft_definetrial

    fiff_file = 'mne_python-epo.fif';
    cfg = [];
    cfg.dataset = fiff_file_epo;
    cfg.trialdef.eventtype  = 'trial';
    cfg.trialfun = 'ft_trialfun_general';
    cfg = ft_definetrial(cfg);

where ''data1'' contains the data organized in multiple trials including condition labelling.

### datatype_timelock `<->` Evoked

#### Export to Evoked

Create evoked in FieldTrip:

    cfg = [];
    cfg.dataset = 'SubjectBraille.ds';
    cfg.trialdef.eventtype      = 'backpanel trigger';
    cfg.trialdef.prestim        = 1;
    cfg.trialdef.poststim       = 2;
    cfg.trialdef.eventvalue     = 3;                    % event value of FIC
    cfg = ft_definetrial(cfg);
    cfg.channel   = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
    data = ft_preprocessing(cfg);

    cfg = [];
    avg = ft_timelockanalysis(cfg, data);
    fiff_file = 'ctf-ave.fif';
    fieldtrip2fiff(fiff_file, avg)

Now we can read it in MNE-Python

```python
    from mne.fiff import read_evoked
    evoked = read_evoked('ctf-ave.fif')
    print(type(evoked))
```

#### Import Evoked

We just continue using the instance ''epochs'' that was defined [before](#datatype_raw_many_trials_-_epochs). We then create an instance of class ''Evoked'' using the method ''average'

```python
    evoked = epochs.average()
    print(type(evoked))  # returns mne.fiff.evoked.Evoked
    evoked.save('mne_python-ave.fif')
```

And then in MATLAB, we can read the data

    fiff_file = 'mne_python-ave.fif';
    cfg = [];
    cfg.dataset = fiff_file;
    data1 = ft_preprocessing(cfg);
    avg1 = ft_timelockanalysis([], data1);

    ft_datatype(avg1)  % returns 'timelock'

In addition, we can read multiple conditions too, if there are present in the ''evoked'' fif fil

    cfg = [];
    cfg.dataset = fiff_file;
    data1 = ft_preprocessing(cfg);  % E.g. with 3 conditions -> mapped to 3 trials

    cfg = [];
    cfg.trials = 1;
    avg1 = ft_timelockanalysis(cfg, data1);
    cfg.trials = 2;
    avg2 = ft_timelockanalysis(cfg, data1);
    cfg.trials = 3;
    avg3 = ft_timelockanalysis(cfg, data1);
