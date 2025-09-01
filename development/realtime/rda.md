---
title: Streaming realtime data from BrainVision Recorder Remote Data Access (RDA)
tags: [realtime, brainvision]
---

BrainVision Recorder is the EEG acquisition software that accompanies the BrainAmp EEG amplifier from [BrainProducts](http://www.brainproducts.com/).

The recorder software allows the incoming data to be sent out to the network via the TCP/IP protocol using the Remote Data Access module to the BrainVision RecView software or any homemade software (such as FieldTrip or BCI2000) for real time data analyses.

## Transporting data from an RDA server to a FieldTrip buffer

To facilitate using the same processing logic (e.g., FieldTrip functions) for data coming from an RDA server, we provide helper applications that connect the RDA server as a client and write the incoming data to a [FieldTrip buffer](/development/realtime/buffer).

### MATLAB-based interface

{% include markup/skyblue %}
The MATLAB implementation is mainly for educational and testing purposes. For proper real-time analyses we recommend you to use the standalone interface, which is faster and requires less system resources.
{% include markup/end %}

The remote data access (RDA) interface of the BrainVision Recorder can stream the data over a TCP/IP connection. The **[ft_realtime_brainampproxy](/reference/realtime/example/ft_realtime_brainampproxy)** function (part of the realtime module in FieldTrip) reads the EEG data stream from the TCP/IP connection and writes to a [FieldTrip buffer](/development/realtime). The FieldTrip buffer is a multi-threaded and network transparent buffer that allows data to be streamed to it, while at the same time allowing another MATLAB session on the same or another computer to read data from the buffer for analysis.

Subsequently in another MATLAB session you can read from the FieldTrip buffer using the **[ft_read_header](/reference/fileio/ft_read_header)**, **[ft_read_data](/reference/fileio/ft_read_data)** and **[ft_read_event](/reference/fileio/ft_read_event)** functions by specifying %%'buffer://hostname:port'%% as the filename to the reading functions, e.g.

    hdr = ft_read_header('buffer://hostname:port');
    dat = ft_read_data('buffer://hostname:port', 'begsample', 1, 'endsample', hdr.Fs);

The TCP/IP interface in MATLAB is implemented in the freely available [TCP/UDP/IP toolbox](http://mathworks.com/matlabcentral/fileexchange/345). You should download this toolbox and add it to your MATLAB path if you want to use the **[ft_realtime_brainampproxy](/reference/realtime/example/ft_realtime_brainampproxy)** function.

### Standalone interface with rda2ft

Instead of **[ft_realtime_brainampproxy](/reference/realtime/example/ft_realtime_brainampproxy)** and MATLAB, you can use **rda2ft**. It transports data from an RDA server to a FieldTrip buffer and is available in source code or compiled for different operating systems. **rda2ft** is written in C and takes 4 command line arguments, where the first two are mandatory:

    rda2ft rdaHostname rdaPort [ftHostname] [ftPort]

For example, if you run rda2ft on the BrainVision acquisition computer (i.e. the 32-bit RDA server is running on localhost) and if you want to stream the data to a remote buffer on mentat205:1972, you would type:

    rda2ft localhost 51244 mentat205 1972

For spawning a local FieldTrip buffer within **rda2ft** at port 1234, you would use a dash (-) instead of the second hostname and write:

    rda2ft localhost 51244 - 1234

Leaving out the last two arguments spawns a local buffer on the default port 1972.

    rda2ft localhost 51244
    
To execute this in combination with MNE, you can modify [this code](https://mne.tools/mne-realtime/auto_examples/plot_ftclient_rt_average.html) to run the above command. The `FieldTripClient` class will receive the data.

#### Compilation

On the command line, change to the "realtime/datasource/BrainAmp" directory and type "make". The Makefile will also work with the MinGW compiler on Windows. You will need to [compile](/development/realtime/reference_implementation#compiling_the_code) the **libbuffer** library first.

### Alternative interface using BCI2000

The RDA interface to BrainVision Recorder is also supported by [BCI2000](http://www.bci2000.org), which means that you can use the interface between BCI2000 and FieldTrip as an alternative to the **[ft_realtime_brainampproxy](/reference/realtime/example/ft_realtime_brainampproxy)**. That interface is documented [here](/development/realtime/bci2000) and [here](http://www.bci2000.org/wiki/index.php/Contributions:FieldTripBuffer).

## Streaming data from a FieldTrip buffer to an RDA client

We have also developed a tool that acts as an RDA _server_ with a FieldTrip buffer as its data source. This enables users to connect any data acquisition system that can write to a FieldTrip buffer to any piece of analysis software that can read from the RDA client interface. This tool is written in C with a simple API to spawn the server thread, and as such can be easily embedded in bigger applications. So far we only provide one example, namely **demo_buffer_rda** in the `realtime/buffer/test` directory. Usually the RDA server will be spawned by the same application that hosts the FieldTrip buffer, but this is not necessary - actually the two servers can even run on different machines.

Users can spawn both a server for 16-bit integer data (default port 51234), which only streams out data if the FieldTrip buffer actually contains 16-bit data itself, and a server for 32-bit floating point data (default port 51244), which automatically converts the data contained in the FieldTrip buffer on the fly.

### Rewriting header information and stopping acquisition

While the RDA protocol knows a "STOP" packet to indicate that data acquisition has stopped, the FieldTrip buffer does not know such a thing. On the other hand, a FieldTrip buffer can easily be rewritten with different headers (also different numbers of channels) at any time.

Currently, the FieldTrip to RDA converter tries to detect this by keeping track of the number of samples that are present in the buffer. If this number decreases (most often to 0), the tool assumes a new header has been written, sends an RDA stop packet to all connected clients, re-reads the header information from the FieldTrip buffer, and restarts the clients (if they are still connected) with a new START packet.

### Block numbers

All data packets in an RDA stream contain a block number, which is unknown in the FieldTrip buffer. The conversion tool uses _one_ internal counter of blocks it read from the buffer since the header information was picked up, and sends this along. This means that multiple RDA clients get the same block number, even if one of them has connected much later and thus missed lots of blocks.

### Translation of events to markers

In the FieldTrip buffer, **events** are represented by a triple (sample,offset,duration) for the timing, as well as _type_ and _value_ fields, where the latter two can contain an arbitrary number of almost arbitrary elements (integers, characters, real numbers, ...). Somehow this needs to be matched to the **markers** that RDA knows about, which means a representation by (nPosition,nPoints) for the timing, a channel number _nChannel_ that refers to the source of the event, and a single _type_ string.

Currently, the translation scheme is the following:

| FT event element | RDA marker element |
| ---------------- | ------------------ |
| sample           | nPosition (\*)     |
| duration         | nPoints            |
| offset           | -                  |
| -                | nChannel = -1      |
| type:value       | typeString         |

where the fixed value -1 for _nChannel_ is defined as the "don't care" value by the RDA protocol.
To clarify the last row, the following rules are applied for the _type_ and \*value\* field:

- If both are strings, e.g., _type_="button" and _value_="right", the RDA marker will contain the type string "button:right"
- If the _value_ field is not a string, it will be replace by "-". For example, if button presses are encoded by a number, the RDA marker might look like "button:-"
- If the _type_ field is not a string, it will be replaced by "FT", yielding something like "FT:right"
- If neither _type_ nor _value_ are strings, the marker description is always "FT:-"

(_) Actually, the \_nPosition_ field of RDA markers is supposed to be relative to the same data block, that is, if the current data block starts at sample index 4000, and a marker with _nPosition=10_ is sent along, the corresponding \_sample\* index would be 4010. Now, a difficulty lies in the fact that in the FieldTrip buffer, events that relate to a certain sample might only be present after that specific sample has already been sent out by the RDA server. This means that it needs to be send as a marker in the next data block, but then the sample index cannot be represented as a positive number anymore, because it refers to a block in the past.

### Block size setting in BCI2000

If the FieldTrip-to-RDA streaming tool is used for sending data to BCI2000, care should be taken to select a reasonable block size in the BCI2000 RDA client setup: This should match the block size of the acquisition system that writes to the FieldTrip buffer, since the attached RDA server will usually stream out the data using the same blocks. However, there is no guarantee that all data blocks sent out will be of equal size.

## Differences in the format of events

RDA -> FieldTrip: Channel number field of RDA markers should be matched to value field of FieldTrip buffer events, type string should be converted to FieldTrip event _type_ field (keep as string, but remove trailing zero).

## External links

- <http://www.brainproducts.com>
- <http://www.bci2000.org>
- <http://mathworks.com/matlabcentral/fileexchange/345>
