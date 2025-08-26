---
title: FieldTrip buffer C++ implementation
tags: [realtime, development]
---

# FieldTrip buffer C++ implementation

This page describes the C++ wrappers around the reference implementation and a generic framework for writing an acquisition driver using a set of ready-made C++ modules.

## Components

What follows is a list of C++ classes and their purpose.

### MultiChannelFilter

Online filtering (IIR) of multi-channel signals, using the same filter coefficients for each channel.
This is a template class that allows arbitrary data types to be used for the input/output signal, as well
as the internally used data type to hold the filter states. For example, you can lowpass-filter 10 channels of
32-bit integer signals and use a double-precision floating point representation internally by calling

```cpp
  MultiChannelFilter`<int,double>` *filter = new MultiChannelFilter`<int,double>`(10, 4);  // 4th-order filter
  filter->setButterLP(0.1);  // normalised frequency, 1=Nyquist
  filter->process(out, in);  // out and in point to 10 integers each (=one sample)
```

### TemplateVectorMath

A small helper class to carry out vector operations (as used in MultiChannelFilter) on arbitrary data types.

### GDF_Writer

A class that allows to create GDF files (v2.20). It provides helper functions for setting up the header,
and adding blocks of data to the file. For example, to write 1 status + 10 continuous channels as 32-bit
integers, you would call something like

```cpp
  GDF_Writer gdfWriter = new GDF_Writer(1+10, 500, GDF_INT32);
  gdfWriter->setLabel(0, "Status");
  for (int i=0;i<10;i++) {
     gdfWriter->setLabel(1+i, yourLabel[i]);   // e.g., yourLabel[0] is label of first cont. channel
     gdfWriter->setPhysicalLimits(1+i, -262144.0, 262144.0);   // maximum physical value = 262144 ...
     gdfWriter->setPhysDimCode(1+i, GDF_MICRO + GDF_VOLT);     // ... in units of microVolt
  }
  ...
  gdfWriter->createAndWriteHeader(filename);
  ...
  gdfWriter->addSamples(num, data);      // data must point to 11*num integer values
```

### ChannelSelection & SignalConfiguration

The "ChannelSelection" class wraps up a list of channel indices and labels. It's used twice within
the "SignalConfiguration" class: Once for describing a selection of channels for streaming, and once for saving
to disk. On top of that, the "SignalConfiguration" provides a few commonly used properties such as the desired
bandwidth (cutoff frequency) and filter order for lowpass filtering, a decimation factor for downsampling streamed
data and so on. It also provides functions for parsing these configuration options from a text file (see the
wiki page for the [BioSemi acquisition driver](/development/realtime/biosemi) for an example).

"ChannelSelection" could actually be used in both ways:

1.  Say you have a hardware device with a fixed list of channels, which are not necessarily labeled. In this case, you would select the desired channels by their index, and then attach a name as in the configuration file described above.

2.  For other systems (e.g., CTF MEG) you might be given the channel names from the hardware vendor. In this case, you would specify the channel selection by a list of names, and then match those to the HW vendors list to determine which the channel indices (not implemented yet).

### StringServer

The "StringServer" class wraps up a mechanism to listen to ASCII messages on a TCP port. Multiple clients can connect
at the same time. Commands should be terminated by a line-feed ("\n"). The server will respond by line-feed terminated
ASCII strings in the same way. This is used to control the runtime behavior of the "OnlineDataManager" (see below).

### OnlineDataManager

This class will eventually wrap up all the generic parts of streaming data to a FieldTrip buffer
and saving it to a GDF file at the same time. The general scheme looks like this

    Setup HW device
    Setup OnlineDataManager (ODM)
     (read configuration file from disk)
    LOOP
     Check ODM status (in particular requests from the StringServer)
     Poll hardware (=> yields n new samples)
     Let ODM provide a new empty block (n samples)
     Fill samples (all HW channels) into that block
     Add events to ODM's event list
     Let ODM handle this block
        (stream out selected channels)
        (write selected channels to disk)
    ENDLOOP

Saving to disk will be handled in a separate thread to allow for smallest possible latencies + jitter.

#### Commands that influence runtime behavior

The OnlineDataManager will listen on a certain TCP port for incoming commands given as line-feed-terminated ASCII strings such a

- "STREAM START" will enable streaming.
- "STREAM STOP" will disable streaming.
- "STREAM SELECT index=label index=label ..." to select channels for streaming. Spaces can be used in labels by using double quotes, e.g., "STREAM SELECT 1="Channel 1""
- "STREAM FILTER bandwidth order factor" to enable low-pass filtering and downsampling
- "STREAM STATUS" to retrieve information about running state. The response will be of the form `numacquired=N numstreamed=S downsample=D bandwidth=B bworder=O` where "N" is the number of continuously sampled channels from the hardware, "S" is the number of channels selected for streaming, "D" is the downsampling factor, "B" is the bandwidth (cut-off frequency of lowpass filter), and "O" is the order of the Butterworth filter used. Notice that for "O=0" no filtering takes place, no matter which bandwidth is reported.
- "SAVE START" will enable saving to GDF. In case no new filename has been set (see below), a suffix "\_Si" with "i" being a counter will be appended.
- "SAVE STOP" will disable saving to GDF. The current file will be closed orderly.
- "SAVE SELECT index=label index=label ..." to select channels for streaming.
- "SAVE FILE filename" to set the filename for the next GDF file to be written.
- "SAVE STATUS" to retrieve information about running state. The response will be of the form `numacquired=N numsaved=S saving=T savingto="filename"` where "N" is the number of continuously sampled channels from the hardware, "S" is the number of channels selected for staving, "T" is either "true" or "false" depending on whether saving is enabled, and "filename" describes the file currently written to. Notice that the latter is always empty ("") in case "saving=false".
- "STATUS" to retrieve information about running state (both streaming and saving). The response is a combination of the responses or "SAVE STATUS" and "STREAM STATUS".

Generally, the SELECT, FILTER and FILE commands will only be accepted after a corresponding STOP command.
