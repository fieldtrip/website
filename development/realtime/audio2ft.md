---
title: Streaming realtime data from soundcard using PortAudio
tags: [realtime, audio]
---

We provide a standalone tool called **audio2ft** (see "realtime/datasource/audio") to grab audio data from the soundcard using PortAudio, and stream it to a FieldTrip buffer.
You need to call this tool with a number that selects your sound card and driver architecture, and the usual command line arguments for selecting the FieldTrip
buffer server address, that is

    audio2ft device [hostname [port]]

where replacing "hostname" by a minus (-) tells the software to spawn its own buffer server on the given port. When called without arguments,

**audio2ft** will list the sound devices found by the PortAudio library, from which you can pick the desired device for the next call.
When called with only the "device" argument, the application will use "localhost" and "1972" as the default settings. Data will be captured at a sampling rate of 44100 Hz, but downsampling can be enabled in the configuration file "config.txt" (must be in the same directory), where you can select channels and attach labels.

### Compilation

We provide a simple "Makefile" for GCC and the MinGW compiler, but you will need the PortAudio library for your platform. For Windows, a pre-compiled DLL
is available. Please go to the "realtime/datasource/audio" directory and type "make" or "mingw32-make".
Note that you might need to [compile](/development/realtime/buffer) the **libbuffer** library first.

## External links

- http://www.portaudio.com cross-platform library for accessing audio devices
