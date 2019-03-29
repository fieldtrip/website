---
title: ft_read_event
---
```
 FT_READ_EVENT reads all events from an EEG/MEG dataset and returns
 them in a well defined structure. It is a wrapper around different
 EEG/MEG file importers, directly supported formats are CTF, Neuromag,
 EEP, BrainVision, Neuroscan, Neuralynx and Nervus/Nicolet.

 Use as
   [event] = ft_read_event(filename, ...)

 Additional options should be specified in key-value pairs and can be
   'dataformat'     string
   'headerformat'   string
   'eventformat'    string
   'header'         header structure, see FT_READ_HEADER
   'detectflank'    string, can be 'bit', 'up', 'down', 'both', 'peak', 'trough' or 'auto' (default is system specific)
   'chanindx'       list with channel indices in case of different sampling frequencies (only for EDF)
   'trigshift'      integer, number of samples to shift from flank to detect trigger value (default = 0)
   'trigindx'       list with channel numbers for the trigger detection, only for Yokogawa & Ricoh (default is automatic)
   'triglabel'      list of channel labels for the trigger detection (default is all ADC* channels for Artinis *.oxy3 files
   'threshold'      threshold for analog trigger channels (default is system specific)
   'blocking'       wait for the selected number of events (default = 'no')
   'timeout'        amount of time in seconds to wait when blocking (default = 5)
   'tolerance'      tolerance in samples when merging analogue trigger channels, only for Neuromag (default = 1, meaning
                    that an offset of one sample in both directions is compensated for)

 Furthermore, you can specify optional arguments as key-value pairs
 for filtering the events, e.g. to select only events of a specific
 type, of a specific value, or events between a specific begin and
 end sample. This event filtering is especially usefull for real-time
 processing. See FT_FILTER_EVENT for more details.

 Some data formats have trigger channels that are sampled continuously with
 the same rate as the electrophysiological data. The default is to detect
 only the up-going TTL flanks. The trigger events will correspond with the
 first sample where the TTL value is up. This behavior can be changed
 using the 'detectflank' option, which also allows for detecting the
 down-going flank or both. In case of detecting the down-going flank, the
 sample number of the event will correspond with the first sample at which
 the TTF went down, and the value will correspond to the TTL value just
 prior to going down.

 This function returns an event structure with the following fields
   event.type      = string
   event.sample    = expressed in samples, the first sample of a recording is 1
   event.value     = number or string
   event.offset    = expressed in samples
   event.duration  = expressed in samples
   event.timestamp = expressed in timestamp units, which vary over systems (optional)

 The event type and sample fields are always defined, other fields can be empty,
 depending on the type of event file. Events are sorted by the sample on
 which they occur. After reading the event structure, you can use the
 following tricks to extract information about those events in which you
 are interested.

 Determine the different event types
   unique({event.type})

 Get the index of all trial events
   find(strcmp('trial', {event.type}))

 Make a vector with all triggers that occurred on the backpanel
   [event(find(strcmp('backpanel trigger', {event.type}))).value]

 Find the events that occurred in trial 26
   t=26; samples_trials = [event(find(strcmp('trial', {event.type}))).sample];
   find([event.sample]>samples_trials(t) & [event.sample]<samples_trials(t+1))

 The list of supported file formats can be found in FT_READ_HEADER.

 To use an external reading function, use key-value pair: 'eventformat', FUNCTION_NAME.
 (Function needs to be on the path, and take as input: filename)

 See also FT_READ_HEADER, FT_READ_DATA, FT_WRITE_EVENT, FT_FILTER_EVENT
```
