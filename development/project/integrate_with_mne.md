---
title: Import and export data to and from MNE-Python
---

{% include /shared/development/warning.md %}

# Import and export data to and from MNE-Python

Not all the information contained in either MATLAB or Python can be completely copied into the other format.

Code under development, the MNE-Python community currently works on reader functions for FieldTrip data structure
[https://github.com/mne-tools/mne-python/pull/5141](https://github.com/mne-tools/mne-python/pull/5141), [https://github.com/mne-tools/mne-python/issues/4833](https://github.com/mne-tools/mne-python/issues/4833)

More functions to work with files coming from MNE-Python in MATLAB are available at [https://github.com/mne-tools/mne-matlab](https://github.com/mne-tools/mne-matlab).

## Introduction

FieldTrip and MNE-Python offer tools to analyze electrophysiological activity. [MNE-Python](http://martinos.org/mne/stable/index.html), with code available at [github.com](https://github.com/mne-tools/mne-python), facilitates the access to the FIFF files and integrates with the [MNE suite](http://martinos.org/mne/stable/index.html), written in C (FieldTrip can also use some of the functions in the MNE suite, as explained in the [minimum-norm estimate tutorial](/tutorial/minimumnormestimate)). In addition, MNE-Python allows for a variety of tools for the analysis of electrophysiological data, as demonstrated in the [example gallery](http://martinos.org/mne/stable/auto_examples/index.html).

Primary use cases for the integration of FieldTrip and MNE-Python are

- the ability for MNE users do channel-level time-frequency analysis and sensor-level statistics in FieldTrip.
- the ability for FieldTrip users to do source reconstruction in MNE.

## Background

FieldTrip and MNE-Python have similar but not identical processing pipelines. A common pipeline in FieldTrip is to create trials by reading the data directly from disk (in order to have a **[ft_datatype_raw](/reference/utilities/ft_datatype_raw)**) and then use this preprocessed data to create ERP (**[ft_datatype_timelock](/reference/utilities/ft_datatype_timelock)**). In MNE-Python, the whole continuous recording is imported (with the **Raw** class), then trials are extracted with the **Epochs** class and finally trials are averaged into the **Evoked** class. To recap, this is the correspondence between datatypes in the two package

| Conceptual                                   | FieldTrip                                               | MNE-Python                                                                  |
| -------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------- |
| one continuous segment of data               | [ft_datatype_raw](/reference/utilities/ft_datatype_raw)           | Raw                                                                         |
| multiple segments of data, e.g., trials       | [ft_datatype_raw](/reference/utilities/ft_datatype_raw)           | Epochs (This datatype is not part of the original MNE Suite written in C) |
| averaged ERFs for one or multiple conditions | [ft_datatype_timelock](/reference/utilities/ft_datatype_timelock) | Evoked                                                                      |

Therefore, we will need to import and export Raw, Epochs, and Evoked datatypes.

The aim is to pass the channel=level data between FieldTrip and MNE. Reading is implemented through the **[ft_read_header](/reference/fileio/ft_read_header)** and **[ft_read_data](/reference/fileio/ft_read_data)** functions. Writing is implemented through the ad-hoc **[fieldtrip2fiff](/reference/fieldtrip2fiff)** function.

## Procedure

### datatype_raw (one trial) `<->` Raw

For these examples, we'll use the example data of [dataset 10](/faq/datasets#meg-tactile_dipole_fitting). Download [SubjectBraille.zip](https://download.fieldtriptoolbox.org/tutorial/SubjectBraille.zip) and extract the `.ds` folder in a convenient location.

#### Export a FieldTrip data structure with a single trial to Raw

First, we read the data as a continuous chunk. Note that the example dataset used has actually been acquired in 'trial'-mode, which means that it consists of discontinuous segments of data.

    cfg                 = [];
    cfg.dataset         = 'SubjectBraille.ds';
    cfg.trialdef.length = Inf;
    cfg                 = ft_definetrial(cfg);

    cfg.continuous = 'yes';
    cfg.channel    = {'MEG', '-MLP31', '-MLO12'};
    data           = ft_preprocessing(cfg);

We can now export the data to a fiff file, pretending as if it's raw data. Note that the original fiff-file definition stores the data in single precision (32-bit per data point) format. By default, FieldTrip stores the data in the same precision of data, which can be double (and even complex-valued). MNE-python should be capable of dealing with this type of numeric precision, but other software might not. If the data needs to be stored in single precision, you can use the key-value pair ''precision', 'single''.

    fiff_file  = 'ctf-raw.fif';
    fieldtrip2fiff(fiff_file, data)

This function will also attempt to create an event file, called ''ctf_raw-eve.fif''. The events will be represented as numbers, in a Nx3 matrix, where the first column contains the sample index of the event, and the third column contains the value. As of April 2023, also an interpretative comment will be saved in the event file, that allows to map the numbered events in the event file back onto the FieldTrip-style event representation.  

You can then read the file using MNE-Python

```python
    from mne.io import Raw
    raw = Raw('ctf-raw.fif')
    print(raw)
    print(raw.info)

    from mne import read_events
    events = read_events('ctf-raw-eve.fif')
    print(events)
```

#### Import an MNE-python Raw object into FieldTrip

Once you have the data in Python as a Raw object, you can use the ''save'' method to save it again as a fiff-file. This is a silly operation in itself, but we do it here, in order to be able to compare both versions of the files in MATLAB.

```python
    raw.save('mne_python-raw.fif',fmt='double')
```

Then we can use FieldTrip to read the file.

    fiff_file = 'mne_python-raw.fif';

    cfg         = []
    cfg.dataset = fiff_file;
    data_mp     = ft_preprocessing(cfg);
    ft_datatype(data_mp)  % should return 'raw'

    [event, mappings] = fiff_read_events('ctf-raw-eve.fif')

So, ''data_mp'' is of type ''datatype_raw'', containing a single trial.

Events are in Nx3 matrix, where the first column contains the samples and the third column the index of the events. You can use this information to create the trials in FieldTrip. The mappings string indicates how the indexed events map onto the events in the original FieldTrip style event structure. 

### datatype_raw (many trials) `<->` Epochs

#### Export to Epochs

MNE-python also allows to work with so-called ''Epochs'' objects, which are similar to a FieldTrip raw data structure with multiple trials, with the constraint that each of the trials has exactly the same time axis. Let's start by reading the trials into FieldTrip, from the original dataset, and then save the data object as a fiff-file.

    cfg                     = [];
    cfg.dataset             = 'SubjectBraille.ds';
    cfg.trialdef.eventtype  = 'backpanel trigger';
    cfg.trialdef.prestim    = 0.6;
    cfg.trialdef.poststim   = 0.6;
    cfg.trialdef.eventvalue = [4 8]; % these are the trigger values coded on the backpanel trigger, indicating targets and non-targets
    cfg                     = ft_definetrial(cfg);
    cfg.channel             = {'MEG', '-MLP31', '-MLO12'}; % read all MEG channels except MLP31 and MLO12
    data                    = ft_preprocessing(cfg);

    fiff_file  = 'ctf-epo.fif';
    fieldtrip2fiff(fiff_file, data)
    
And then in Python, you can read the ''Epochs'' with:

```python
    from mne import read_epochs
    epochs_ctf = read_epochs('ctf-epo.fif')
    print(type(epochs))
```

#### Import Epochs

If we have the data as ''Raw'' in MNE-Python, we can create epochs, using the ''Epochs'' class

```python
    from mne import read_events, write_events, Epochs
    from mne.io import Raw

    raw = Raw('ctf-raw.fif')
    events = read_events('ctf-raw-eve.fif')
    print(events)

    # create events based on the index in the third column of events
    event_ids = {'backpanel trigger_4': 5, 'backpanel trigger_8': 6}
    tmin = -0.6
    tmax = 0.6-1/600
    epochs = Epochs(raw, events, event_ids, tmin, tmax, baseline=None)
    epochs.save('mne_python-epo.fif')
```

And then in MATLAB

    fiff_file   = 'mne_python-epo.fif';
    
    cfg         = [];
    cfg.dataset = fiff_file;
    data_mp     = ft_preprocessing(cfg);

    [eventlist, mappings] = fiff_read_events(fiff_file); % an epoch file contains events
    data_mp.trialinfo = eventlist(:,3); % note that the events have been recoded w.r.t. the original trigger values
    
where ''data_mp'' contains the data organized in multiple trials.

Alternatively, one could also use the FieldTrip function [ft_definetrial](/reference/ft_definetrial/. 

    fiff_file = 'mne_python-epo.fif';
    
    cfg                    = [];
    cfg.dataset            = fiff_file;
    cfg.trialdef.eventtype = 'trial';
    cfg.trialfun           = 'ft_trialfun_general';
    cfg                    = ft_definetrial(cfg);

    data_mp                = ft_preprocessing(cfg);
    
Now ''data_mp'' contains the data organized in multiple trials including condition labels according to the original event naming scheme. Currently, this route is a bit less efficient in terms of time, because the low-level reading functions (''ft_read_header'', and ''ft_read_event''), load the full data matrix each time they are called. This can be sped up a little bit, by loading the hdr outside the calls to ''ft_definetrial'' and ''ft_preprocessing'', and passing it in the ''cfg''. 

### datatype_timelock `<->` Evoked

#### Export to Evoked

Create evoked in FieldTrip:

    cfg                     = [];
    cfg.dataset             = 'SubjectBraille.ds';
    cfg.trialdef.eventtype  = 'backpanel trigger';
    cfg.trialdef.prestim    = 0.6;
    cfg.trialdef.poststim   = 0.6;
    cfg.trialdef.eventvalue = [4 8];
    cfg                     = ft_definetrial(cfg);
    cfg.channel             = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
    data                    = ft_preprocessing(cfg);

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
    data1 = ft_preprocessing(cfg);  % e.g., with 3 conditions -> mapped to 3 trials

    cfg = [];
    cfg.trials = 1;
    avg1 = ft_timelockanalysis(cfg, data1);
    cfg.trials = 2;
    avg2 = ft_timelockanalysis(cfg, data1);
    cfg.trials = 3;
    avg3 = ft_timelockanalysis(cfg, data1);
