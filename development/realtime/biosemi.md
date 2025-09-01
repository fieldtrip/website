---
title: Streaming realtime data from BioSemi ActiveTwo EEG amplifier
tags: [realtime, biosemi]
---

This page describes the interface between the [BioSemi EEG amplifier](http://www.biosemi.com) and the [FieldTrip buffer](/development/realtime/buffer).

The acquisition setup consists of a battery box, the AD box, an analog input box, and the USB receiver device. We provide a standalone tool called **biosemi2ft** (see "realtime/bin/`<your OS>`) that interfaces directly to the USB driver and thus does not depend on the Actiview software that BioSemi ships. We have tested the tool on Windows XP (32-bit), Windows (64-bit), macOS (32-bit), and Linux (32-bit). It is called on the command line like this:

    biosemi2ft <config-file> <gdf-file> <hostname> <port>

The first argument must be the name of a configuration file (see below). The second argument determines the base name of a GDF file that data is written to. The suffix `.gdf` will be added automatically, as well as session counters (see below) and additional file name parts `_1`, `_2` and so on for splitting the data over multiple files (to avoid 2 GB limits). The optional third and fourth argument are the hostname and port of the FieldTrip buffer. Defaults are "localhost" and "1972". Replacing "hostname" by a minus (-) tells the software to spawn its own buffer server on the given port.

Most users will probably want to use the built-in buffer and specify (note the "minus" as last argument)

    biosemi2ft config.txt outputfile -

where the `config.txt` has to match your hardware.

### Sessions

In the current implementation, the user needs to press "S" to start saving to the GDF file, and "D" to disable it again. Every time saving is re-enabled, a new GDF file is created with the suffix `_Si.gdf` where "i" is replaced by a number that is increased each time (starting with 1). On top of that, keep in mind that files are split at the 2GB boundary in order to avoid compatibility problems. For example, if you specify "mydata" as the second argument for `biosemi2ft`, the first GDF file will be called `mydata_S1.gdf`. If you record more than 2 GB, you will automatically get a file `mydata_S1_1.gdf`. If you then stop the acquisition and restart it, the next file to be created is `mydata_S2.gdf`.

### Configuration file

The ActiveTwo can send out 312 data channels in total, out of which there are 256 EEG channels, 8 EXG channels, 8 JAZZ channels, further 8 specialised channels, and finally (optionally) up to 32 channels from the analog input box. If used with the analog input box, the sampling frequency is fixed at 2048 Hz. Streaming out all that data is an overkill for most applications, so we provide the following configuration file syntax for selection acquisition parameters (example "config.txt").

```ini
# comments start with a hash
; ... or with a semicolon
; empty lines are fine as well

# Write n=label to select hardware channel number n (starting from 1)
# and attach a label to it. This will show up in the FieldTrip buffer
# and the GDF file.
# Currently, there is no check for double inclusion of channels.
# That is, if you define 1=FOO and 1=BAR, the first hardware channel
# will show up twice, with different names.
# Channels listed before the first [save] or [stream] line will be added
# to both saving and streaming selections. Write [select] to enable
# selection for both saving and streaming.
[select]
1=A1
2=A2

# Now we add some more channel for saving only
[save]
33=B1
34=B2

# And some channels we only want to stream
[stream]
65=C1
66=C2

# Please take note that the channels will be written out in the order specified here,
# that is, they will not be sorted according to the hardware channel number!

# Write "downsample X" with a positive number X to set the downsampling
# factor for streaming. The GDF file will receive full-rate data.
downsample 8

# Write "bandwidth X" with a positive real number X to set the cutoff frequency
# of a Butterworth low-pass filter.
bandwidth 50

# Write "bworder N" to set the order of the lowpass Butterworth filter for downsampling
bworder 4

# Refresh period (in seconds) for inserting extra events.
# Battery events are sent out in a fixed interval (set 0 to disable).
# Status events are sent out when the status changes, OR when the specified
# time has elapsed after the last event was sent out.
statusrefresh 4
batteryrefresh 20

# Triggers will be written as FieldTrip buffer events with type="TRIGGER" and a
# value corresponding to the 16-bit trigger signal.
# With the keyword splittrigger, you can opt to split the 16-bit trigger signal
# into two 8-bit signals, and give names to the events that are sent out for the
# low and high byte of the original signal, respectively.
splittrigger stimulus response
```

### Compilation

You will need the Labview DLL (or shared object), which you can download from [the BioSemi website](http://www.biosemi.com/download.htm).
Depending on your platform, you might be able to get ready-made binaries, or you need to compile this yourself.

For compiling the **biosemi2ft** tool, change to the `realtime/datasource/biosemi` directory and type `make`. The Makefile will
also work with the MinGW compiler on Windows. Note that you might need to compile the buffer library first.

### Multi-EEG using the Mk2 A/D box

Using the **biosemi2ft** tool with the Mk2 A/D box in a daisy-chained multi-EEG setup may return wrong sampling frequencies, given the changed meaning of the "SpeedMode" switch. For example, a multi-EEG setup and "SpeedMode" set to 1 returns a sampling frequency of 4 kHz, whereas data is actually sampled at 2 kHz (note that multi-EEG always operates at 2 kHz). This results in an incorrect data header and may cause problems in real-time analyses and online filtering.

The problem can be fixed by recompiling `biosemi2ft.exe` after setting the sampling frequency independent of the detected speed mode to 2 kHz in `BioSemiClient.cc`. However, this recompiled version will no longer work with single EEG setup using other sampling frequencies than 2 kHz.

A recompiled version for Win64 is provided as `biosemi2ft_2khz.exe`. This has been tested using Mk2 + Mk1 A/D box in dual EEG setup under 64-bit Windows 10.

## External links

- <http://www.biosemi.com>
