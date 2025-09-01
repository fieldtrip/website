---
title: Reading and writing of EEG/MEG time series data
tags: [development, fileio]
redirect_from:
  - /development/fileio/
---

FieldTrip has a flexible way of supporting dataformats. It uses three wrapper functions that provide a common interface to all electrophysiological file formats: **[ft_read_header](/reference/fileio/ft_read_header)**, **[ft_read_data](/reference/fileio/ft_read_data)** and **[ft_read_event](/reference/fileio/ft_read_event)**. Other data that is commonly used in electrophysiological analysis such as anatomical measurements can be read with **[ft_read_mri](/reference/fileio/ft_read_mri)**, **[ft_read_sens](/reference/fileio/ft_read_sens)** and **[ft_read_headshape](/reference/fileio/ft_read_headshape)**. Furthermore, **[ft_read_headmodel](/reference/fileio/ft_read_headmodel)** can be used for reading EEG and MEG volume conduction models of the head, and neuronal spiking data can be read with **[ft_read_spike](/reference/fileio/ft_read_spike)**.

All these ft_read_xxx functions automatically detect the file format and subsequently will call the appropriate low-level function for each file format. Some of the low-level functions are written by ourselves, some are supplied by the manufacturers and some are obtained from other open source toolboxes.

The objective of supplying the low-level EEG and MEG reading functions as a separate module/toolbox are to

1.  facilitate the reuse of the ft_read_xxx functions in other open source projects (e.g., EEGLAB, SPM)
2.  facilitate the implementation and support for new data formats, esp. for external users/contributors
3.  facilitate the implementation of advanced features without complicating the standard use

A list of the data formats that are supported is given [here](/faq/preproc/datahandling/dataformat). The low-level reading functions are combined in the **fileio** module, which is released together with FieldTrip but can also be downloaded [here](https://download.fieldtriptoolbox.org/modules) as a separate and fully self-contained MATLAB toolbox.

## Module layout

The fileio module contains high-level functions that are publicly available for the end-user. The functionality of the functions within this module depends on low-level functions for reading particular data formats from varying acquisition systems and are not available for the end-user and combined in a private directory.

The remainder of this page mainly describes the core features for reading electrophysiological data. The other functions for reading sensor sensor information, headshapes, anatomical MRIs and spikes are pretty much self-explanatory.

## Features

The following features are implemented in the fileio module

- the API for the functions is transparent to the data format
- adding support for new file formats require only little change to the existing functions
- the data is returned in a 2-D array (Nchans x Nsamples), or in a 3-D array (Ntrials x Nchans x Nsamples)
- the header information is represented in a structure that is common to all data formats
- the event information is represented in a structure that is common to all data formats

Other options that have been suggested, but that are not implemented yet are

- supporting data in multiple files (i.e. an EEG session with a break in the acquisition)
- storing the file identifier in the header (prevent fopen+fseek for reading each block)
- downsampling on the fly, support for different sampling rates in one dataset
- rereference EEG data while reading in, and/or add the implicit reference channel
- instead of specifying a refchan, use a complete linear projection matrix (c.f. LDR in NeuroScan)

## Definition of the function-calls (API)

The API allows for reading header information, event information and blocks of data. The API consists of two parts: a clearly defined function call, and a clearly defined output of that function call.

    hdr    = ft_read_header(filename)    % returns a structure with the header information
    event  = ft_read_event(filename)     % returns a structure with trigger information
    dat    = ft_read_data(filename, ...) % returns a 2-D or 3-D array with the data

The data-reading function has additional variable input arguments for selecting segments and channels.

The motivation for separating the reading into header/event/data is (among others) inspired by the CTF and by the BrainVision data formats. Based on the header, you want to decide how to approach reading the data, e.g., read everything for an average ERP, read an epoch for trial-based data, read a segment for continuous data. Based on the events (triggers and such), you want to decide which segments of data to read, e.g., read a pre/post-stimulus data segment around each trigger. These decisions are part of the FieldTrip/SPM/EEGLAB/enduser code.

### Header format

In order to make the API transparent to the final application, the header structure by default only contains those elements that are common to all file types

- sampling frequency
- number of samples
- number of trials
- number of channels
- channel labels
- ...

Additional header information that is present for only specific file formats is stored in a substructure ("orig"). An example header for a CTF MEG dataset looks like this

    hdr =
            Fs: 600            % sampling rate in Hz
        nChans: 218            % number of channels, in this case 151 MEG channels  and some additional EEG channels
         label: {218x1 cell}   % channel labels
      nSamples: 6000           % number of samples per trial, in this case 10 seconds long

      nSamplesPre: 0 % baseline period in each trial
      nTrials: 49 % number of trials
      grad: [1x1 struct] % details on the position and orientation of the MEG sensors
      orig: [1x1 struct] % the original CTF header structure

### Data format

The electrophysiological data is returned as a Nchans X Nsamples matrix (for continuous data), or as a Nchans X Nsamples X Ntrials matrix (for trial based data).

### Event format

The event structure allows for various events, which can be coded as numbers (trigger values) or as strings (annotations and trial classifications). Events have a location in the file (sample number) and may have a duration. In the end-user application, it should be easy to search for events of a particular type. Selected events should be used to fetch the data of interest from the file.

An example event structure for a CTF MEG dataset looks like this

    >> event
    event =
    1x577 struct array with field
      type
      sample
      value
      offset
      duration

    >> event(1)
    ans =
          type: 'trial'
        sample: 1
         value: []
        offset: 0
      duration: 6000

    >> event(2)
    ans =
          type: 'backpanel trigger'
        sample: 1451
         value: 4
        offset: []
      duration: []

In case of events with duration that define trials event.sample is the first sample of a trial and event.offset is the offset of the trigger with respect to the trial. An offset of 0 means that the first sample of the trial corresponds to the trigger. A positive offset indicates that the first sample is later than the trigger, a negative offset indicates that the trial begins before the trigger.

## Example use of the ft_read_xxx functions

The following piece of code will read each trial in an trial-based dataset that has a trigger with value "1"

```
hdr = ft_read_header(filename);
event = ft_read_event(filename);
trig1 = find(cell2mat({event.value})==1);
for i=1:length(trig1)
dat(i,:,:) = ft_read_data(filename, 'trial', trig1(i));
end
```

The following piece of code will read all trial with trigger value "1" all at once

```
hdr = ft_read_header(filename);
event = ft_read_event(filename);
trig1 = find(cell2mat({event.value})==1);
dat = ft_read_data(filename, 'trial', trig1);
```

The following piece of code will read the first 10 seconds data from a continuous file

```
hdr = ft_read_header(filename);
dat = ft_read_data(filename, 'begsample', 1, 'endsample', 10*hdr.Fs);
```

The following piece of code will read a one-second segment of data from a continuous dataset around the first trigger with value "4"

```
hdr = ft_read_header(filename);
event = ft_read_event(filename);
sel = [];
for i=1:length(event)
  % test each event, we are looking for a trigger with value 4
  if isequal(event(i).type, 'trigger') && isequal(event(i).value, 4)
    sel = [sel; i];
  end
end
sel = sel(1); % select only the first trigger that was found
begsample = event(sel(1)).sample - 0.3*hdr.Fs; % select 300ms before the sample of the trigger
endsample = event(sel(1)).sample + 0.7*hdr.Fs; % select 700ms after the sample of the trigger
dat = ft_read_data(filename, 'begsample', begsample, 'endsample', endsample);
```

## The representation of discontinuous data on disk

The event.sample relates to the sample index into the file, disregarding any internal structure in the file. Different data formats that are supported allow for

1. fully continuous data
2. continuous recordings that are stored in blocks, with no gaps in between (e.g., EDF)
3. epoched recordings, i.e. a fixed block representation with known or unknown gaps in between
4. continuous recordings with an occasional break (e.g., a pause)

1 and 2 are continuous or pseudo-continuous respectively.

2 and 3 can most of the times not be distinguished based on the file content, but can sometimes be distinguished by external information (e.g., EDF is meant to represent continuous data, but for CTF it can be either continuous or have gaps in between).

4 has segments ("trials" in fieldtrip-speak) of unequal length.

To support all of these with ft_read_header, ft_read_data and ft_read_event, some conventions have been adopted. Say we do

```
hdr = ft_read_header(filename)
event = ft_read_event(filename)
```

then in all cases hdr.nSamples*ndr.nTrials reflects the total number of samples present in the datafile. Each sample in the datafile is indexed, starting from 1, up to hdr.nSamples*ndr.nTrials.

- In case 1, hdr.nTrials = 1.
- In case 2 and 3, hdr.nTrials is usually the number of segments that can be represented in the file and hdr.nSamples is the number of samples in a segment (fixed for all segments).
- In case 3, hdr.nSamplesPre is sometimes known from the file and is returned as non-zero (by default it is zero).
- In case 4, hdr.nSamples does not apply as a single number to the variable length segments.

To deal with the more detailed structure in the file, the output of ft_read_event is needed

- In case 1, there are events for each trigger.
- In case 2, there are events for each trigger, but there is also a "trial" event for each segment in the file
- In case 3, there are events for each trigger, but there is also a "trial" event for each segment in the file.
- In case 4, it is the same as case 2, but sometimes it has another name (e.g., BrainVision calls them "New Segment" markers).

So if in case 3 you want to know where a trigger is relative to its corresponding trial, you have to look in the events at both the triggers AND at the trials, which are both represented in the event array.

If you want to know which trigger (or triggers) happen in which trial, you have to make some combinatorial MATLAB code (i.e. the "trialfun" that you specify in **[ft_definetrial](/reference/ft_definetrial)**). In the trialfun you write the code that parses the sequence of events, combining them where needed. e.g., you might have trials, each with a target and a response event, but in some trials there is no response trigger because the subject was too late to respond. Some of the trials might be catch trials in which no target was presented (and no response was given). But you might also have trials in which the subject (inadvertently) pressed the response button twice. In short: there does not have to be a one-to-one mapping between triggers and trials, and hence you have use your expert knowledge about the experiment to decipher the sequence of events and pick the data segments that are of interest to your analysis.

## Guidelines for adding support for other file formats

The ft_read_data, ft_read_header and ft_read_event functions strongly depend on the **[ft_filetype](/reference/fileio/ft_filetype)** helper function. That function automatically determines the format of the file, for example by looking at the extension, by looking at the first few bytes of the file or any other characteristic feature. So adding support for a new file format also requires that new file format to be added to the ft_filetype function.

The **[ft_filetype](/reference/fileio/ft_filetype)** function is often called like this (e.g., in ft_read_data)

    var = ft_filetype(filename)
    if strcmp(var, something)
    % do something
    elseif strcmp(var, something_else)
    % do something else
    ...

or like this

    switch ft_filetype(filename)
    case 'ctf'
    % do something
    case 'neuroscan'
    % do something else
    ...

The ft_filetype function does its checks in one long if-elseif-elseif ladder. The consequence is that the detection sometimes is order sensitive: the first match in ft_filetype will be the one returned. So for common file extensions like ".dat" it can be problematic. The solution for identical file extensions is to have the most stringent check first (e.g., "extension is .dat and header contains a few magic bytes") followed by the less stringent check ("extension is .dat").

Another recommendation for file type detection is to use the potential context, e.g., the simultaneous presence of multiple files. That is used for example in BrainAnalyzer, which always has a set of three files (an ASCII .vhdr, another ASCII .vmrk and one binary file with extension .dat, .eeg or .seg). The .dat file in then easy to recognize because it is always accompanied by the .vhdr and .vmrk file.

## Related documentation

Related projects on electrophysiology (EEG, MEG) data I/O are

- [Biosig](http://biosig.sourceforge.net/)
- [NeuroShare](http://www.neuroshare.org/)
- [EEG toolbox](http://eeg.sourceforge.net/)
- [FIFF access](http://ltl.tkk.fi/~kuutela/meg-pd/)
