---
title: Getting started with TMSi data
tags: [dataformat, tmsi, eeg]
category: getting_started
redirect_from:
    - /getting_started/tmsi/
---

[Twente Medical Systems International](https://www.tmsi.com) or TMSi is a Dutch company with a focusses on EEG amplifiers. Some of the TMSi amplifiers are or have been used by other companies under their own brand names, notably the [Refa](https://www.tmsi.com/products/refa/) system which was integrated by ANT Neuro and by BrainProducts in their own systems.

TMSi has its own acquisition software for its amplifiers, Polybench, which is probably the software that you are using if you purchased your EEG hardware directly from TMSi. The remainder of this page deals with the EEG data recorded using Polybench.

The Polybench acquisition software writes the data to the `.Poly5` file format. To read the data in the normal and recommended fashion, you would do

    cfg = [];
    cfg.dataset = 'Filename.Poly5';
    data = ft_preprocessing(cfg);
  
Prior to calling **[ft_preprocessing](/reference/ft_preprocessing)** you can use **[ft_definetrial](/reference/ft_preprocessing)** to define segments of interest based on triggers in the data. That is explained in more detail in the preprocessing [tutorials](/tutorial).

The way that stimulus presentation systems (such as NBS Presentation, E-Prime, PsychoPy, or Psychophysics Toolbox) are hooked up to the EEG acquisition setup appears to vary between labs and between different TMSi systems. Sometimes triggers are represented as 8-bit integer numbers, ranging from 1-255. In other cases, each of the trigger bits is controlled with a separate TTL signal, leading to 8 different event codes that can be used. If the default settings of ft_definetrial does not return the trigger codes that you were expecting, you can use the low-level reading functions to figure out the specific options that apply to your recordings.
 
You can read the header with **[ft_read_header](/reference/fileio/ft_read_header)**, the data with
**[ft_read_data](/reference/fileio/ft_read_data)** and the events with **[ft_read_event](/reference/fileio/ft_read_event)**. These functions **do not** return valid FieldTrip data structures to be used with other FieldTrip functions, but help in debugging.  

    hdr = ft_read_header('Filename.Poly5')  % do _not_ use a semicolon at the end of the line, so you can see the header details
    dat = ft_read_data('Filename.Poly5');   % use a semicolon, since you do not want the complete data printed on screen
    event = ft_read_event('Filename.Poly5')

    % show the first 10 events  
    for i=1:10
      disp(event(i))
    end

    % show the event types, i.e. the name of the trigger channel
    unique({event.type})

    sample = [event.sample]
    value = [event.value]
    figure
    plot(sample/hdr.Fs, value, '.')
    xlabel('time (s)')
    ylabel('trigger value')
  
If this does **not** show the triggers at the moment you were expecting, or the trigger values are not as you would expect, you can try again with the `detectflank` option:

    event_up       = ft_read_event('Filename.Poly5', 'detectflank', 'up')       % this is the default
    event_updiff   = ft_read_event('Filename.Poly5', 'detectflank', 'updiff')
    event_down     = ft_read_event('Filename.Poly5', 'detectflank', 'down')     % this is to be used with pull-down triggers
    event_downdiff = ft_read_event('Filename.Poly5', 'detectflank', 'downdiff')
    event_any      = ft_read_event('Filename.Poly5', 'detectflank', 'any')
    event_biton    = ft_read_event('Filename.Poly5', 'detectflank', 'biton')    % this is when you use single TTL channels
    event_bitoff   = ft_read_event('Filename.Poly5', 'detectflank', 'bitoff')   % this is when you use single TTL channels with pull-down triggers

If this still does not give the expected results, you should check whether the correct trigger channel is being used. For that you can look in the header (i.e. `hdr.label`), you can plot the data, and you can specify the trigger channels like this

    event_up = ft_read_event('Filename.Poly5', 'detectflank', 'up', 'chanindx', 33)       % channel 33 contains the triggers
    event_up = ft_read_event('Filename.Poly5', 'detectflank', 'biton', 'chanindx', 41:48) % channels 41:48 contains bit-wise triggers
    
Once you have figured out what the proper low-level settings are for your setup and recording, you can use them with the high-level FieldTrip functions as follows

    cfg = [];
    cfg.dataset               = 'Filename.Poly5';
    cfg.trialfun              = 'ft_trialfun_general';
    cfg.trialdef.eventtype    = ...
    cfg.trialdef.eventvalue   = ...
    cfg.trialdef.prestim      = 0.2; % in seconds
    cfg.trialdef.poststim     = 0.8; % in seconds
    cfg.trialdef.detectflank  = 'biton';
    cfg.trialdef.chanindx     = 41:48;

    % define the segments of interest
    cfg = ft_definetrial(cfg);

    % read the segments of interest
    data = ft_preprocessing(cfg);
    

## See also

{% include seealso tag="tmsi" %}
