---
title: Streaming realtime data from Emotiv neuroheadset
tags: [realtime, emotiv]
---

This page describes the interface between the 14-channel Emotiv neuroheadset and the FieldTrip buffer.

{% include image src="/assets/img/development/realtime/emotiv/emotiv.jpg" %}

The acquisition setup consists of the headset itself and a bluetooth dongle, which we talk to using the Emotiv SDK on Windows. We provide a standalone tool called **emotiv2ft** (see "realtime/datasource/emotiv") to grab data from the headset, and stream it to a FieldTrip buffer. You can call this tool with the usual command line arguments, that is,

    emotiv2ft <configfile> [hostname=localhost [port=1972 [ctrlPort=8000]]]

where replacing "hostname" by a minus (-) tells the software to spawn its own buffer server on the given port. When called without arguments other than the configuration file,

**emotiv2ft** will use "localhost" and "1972" as the default settings. Data will always be streamed out at the full sampling rate (128 Hz)
from all the channels.

The default configuration file is emotiv_config.txt which can be found in the same directory with emotiv2ft.

Note: If port 1972 cannot be accessed on a Windows machine it may help to first initialize the port from MATLAB, e.g., via ft_realtime_fileproxy

### Installation

Please follow instructions [here](https://emotiv.com/quickstart-guides/QuickStartGuide2014.pdf). You should first confirm that the default Emotiv software works. Subsequently you should start a command window (**cmd.exe**) and in that command window start the **emotiv2ft.exe** application with the correct command line options (see above).

### Compilation

We provide a simple "Makefile" for the MinGW compiler, but you will need the Emotiv SDK. Please go to the "realtime/datasource/emotiv" directory and type "make" or "mingw32-make". Note that you might need to [compile](/development/realtime/buffer) the **libbuffer** library first.

## External links

- http://www.emotiv.com
