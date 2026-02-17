---
title: Add support for reading data from any file format supported by neuroshare
---

{% include /shared/development/warning.md %}

## Objectives

- should be general function that can work with any of the formats supported by neuroshare
- test and implement for cyberkinetics data

## Steps

**read_neuroshare function:**

- read header
- read event
- read data (analog)
- read spike (timestamps and waveforms)

**documentation:**

- getting started with cyberkinetics data

## Code

    %% read_header

    tmp = read_neuroshare(filename);

    % This returns a header structure with the following elements
    %   hdr.Fs                  sampling frequency
    %   hdr.nChans              number of channels
    %   hdr.nSamples            number of samples per trial
    %   hdr.nSamplesPre         number of pre-trigger samples in each trial
    %   hdr.nTrials             number of trials
    %   hdr.label               cell-array with labels of each channel
    %   hdr.FirstTimeStamp      integer, only available for some subformats (mainly animal electrophysiology systems)
    %   hdr.TimeStampPerSample  integer, only available for some subformats (mainly animal electrophysiology systems)
    %
    % Depending on the file format, additional header information can be
    % returned in the hdr.orig subfield.

    hdr = [];
    hdr.Fs                  = tmp.hdr.seginfo(1).SampleRate; % take the fs from the first chan (assuming this is the same for all chans)
    hdr.nChans              = tmp.hdr.fileinfo.EntityCount;
    hdr.nSamples            = max([tmp.hdr.entityinfo.ItemCount]); % take the number of samples from the longest channel
    hdr.nSamplesPre         = 0; % continuous data
    hdr.nTrials             = 1; % continuous data
    hdr.label               = {tmp.hdr.entityinfo.EntityLabel}; %%% contains non-unique chans

    % FIXME: onderstaande gaat alleen als readspike == 'yes' %
    hdr.FirstTimeStamp      = tmp.spikew.timestamp(1); % tmp.spiket.data(1) = same ???
    hdr.TimeStampPerSample  = [];

    %% read_event

    tmp = read_neuroshare(filename, 'readevent', 'yes');

    % This function returns an event structure with the following fields
    %   event.type      = string
    %   event.sample    = expressed in samples, the first sample of a recording is 1
    %   event.value     = number or string
    %   event.offset    = expressed in samples
    %   event.duration  = expressed in samples
    %   event.timestamp = expressed in timestamp units, which vary over systems (optional)
    %
    % The event type and sample fields are always defined, other fields can be empty,
    % depending on the type of event file. Events are sorted by the sample on
    % which they occur.

    for i=1:length(tmp.hdr.eventinfo)
      event(i).type      = tmp.hdr.eventinfo(i).EventType;
      event(i).value     = tmp.event.data(i);
      event(i).timestamp = tmp.event.timestamp(i);
      event(i).sample    = tmp.event.sample(i);
    end

    % FIXME: i don't understand the neuroshare event structure yet...
    % for i=1:length(tmp.event.timestamp)
    %     event(i).type      = tmp.hdr.eventinfo(i).EventType;
    %     event(i).value     = tmp.event.data(i);
    %     event(i).timestamp = tmp.event.timestamp(i);
    %     event(i).sample    = tmp.event.sample(i);
    % end

    %% read_data

    tmp = read_neuroshare(filename, 'readanalog', 'yes', 'chanindx', chanindx, 'begsample', begsample, 'endsample', endsample);

    % This function returns a 2-D matrix of size Nchans*Nsamples for
    % continuous data when begevent and endevent are specified, or a 3-D
    % matrix of size Nchans*Nsamples*Ntrials for epoched or trial-based
    % data when begtrial and endtrial are specified.

    dat = tmp.analog.data';

    %% read_spike

    tmp = read_neuroshare(filename, 'readspike', 'yes');

    % The output spike structure contains
    %   spike.label     = 1xNchans cell-array, with channel labels
    %   spike.waveform  = 1xNchans cell-array, each element contains a matrix (Nsamples X Nspikes)
    %   spike.timestamp = 1xNchans cell-array, each element contains a vector (1 X Nspikes)
    %   spike.unit      = 1xNchans cell-array, each element contains a vector (1 X Nspikes)

    spike.label = {tmp.hdr.entityinfo(tmp.list.segment).EntityLabel};
    for i=1:length(spike.label)
      spike.waveform{i}  = tmp.spikew.data(:,:,i);
      spike.timestamp{i} = tmp.spikew.timestamp(:,i)';
      spike.unit{i}      = tmp.spikew.unitID(:,i)';
    end

    % FIXME: spiket is somehow similar to spikew.timestamp, but without the nan/zero elements...?

## Links

http://neuroshare.sourceforge.net/DLLLinks.shtml
