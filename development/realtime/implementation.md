---
title: Specific software implementations for realtime EEG/MEG/fMRI/NIRS
tags: [realtime, development]
---

# Specific software implementations for realtime EEG/MEG/fMRI/NIRS

This page is part of the documentation series of the FieldTrip buffer for realtime acquisition. The FieldTrip buffer is a standard that defines a central hub (the [FieldTrip buffer](/development/realtime)) that facilitates realtime exchange of neurophysiological data. The documentation is organized in five main sections, being:

1.  description and general [overview of the buffer](/development/realtime/buffer),
2.  definition of the [buffer protocol](/development/realtime/buffer_protocol),
3.  the [reference implementation](/development/realtime/reference_implementation), and
4.  specific [implementations](/development/realtime/implementation) that interface with acquisition software, or software platforms.
5.  the [getting started](/getting_started/realtime) documentation which takes you through the first steps of real-time data streaming and analysis in MATLAB

This page deals with specific implemenations of the FieldTrip buffer protocol. This includes interfacing with specific hardware (e.g., TMSi, Biosemi, CTF, Unicorn), software platforms (e.g., BCI2000, BrainStream) and links to the implementation in specific programming languages (e.g., MATLAB, Java, C/C++, Python).

## Implementations for specific acquisition systems

- [ANT NeuroSDK](/development/realtime/neurosdk)
- [Artinis Medical Systems (NIRS)](/development/realtime/artinis)
- [BrainVision Recorder](/development/realtime/rda)
- [Biosemi](/development/realtime/biosemi)
- [CTF (MEG)](/development/realtime/ctf)
- [Emotiv](/development/realtime/emotiv)
- [Neuromag/Elekta/Megin (MEG)](/development/realtime/neuromag)
- [Jinga-Hi (LFP/EEG)](/development/realtime/jinga-hi)
- [Micromed (ECoG)](/development/realtime/micromed)
- [ModularEEG/OpenEEG](/development/realtime/modulareeg)
- [Neuralynx (LFP)](/development/realtime/neuralynx)
- [Neurosky ThinkCap](/development/realtime/neurosky)
- [OpenBCI](/development/realtime/openbci)
- [Sound card input](/development/realtime/audio2ft)
- [Siemens fMRI](/development/realtime/fmri)
- [TMSI](/development/realtime/tmsi)
- [TOBI](/development/realtime/tobi)
- [Unicorn Hybrid Black](/development/realtime/unicorn)

## Streaming data to other platforms

- [Java](/development/realtime/buffer_java) client-side implementation
- [Python](/development/realtime/buffer_python) client-side implementation
- [Arduino](/development/realtime/arduino) client-side implementation
- [BCI2000](/development/realtime/bci2000) includes the FieldTripBuffer and the FieldTripBufferSource modules
- [BrainVision RDA interface](/development/realtime/rda) allows streaming data in the RDA format
- [BrainStream](/development/realtime/brainstream) is directly supported through shared MATLAB code

## Additional useful tools

- [viewer](/development/realtime/viewer) is a graphical C++ application to visualize online signals from the FieldTrip buffer
- [serial_event](/development/realtime/serial_event) is a C application that turns incoming characters from a serial port into FieldTrip buffer events (used for translating TTL pulses in [realtime fMRI](/development/realtime/fmri))
- [buffer_java#MidiToBuffer](/development/realtime/buffer_java#MidiToBuffer) is a Java application that turns MIDI messages into FieldTrip buffer events
- [buffer_java#MarkerGUI](/development/realtime/buffer_java#MarkerGUI) is a graphical Java application that allows to write FieldTrip buffer events with a freely chosen _type_ and _value_ string.
- [Testing with sine waves and pre-recorded EEG data](/development/realtime/eeg)
- [Testing with pre-recorded fMRI data](/development/realtime/fmri#testing_with_pre-recorded_fmri_data)

## Recording and playing back online experiments

There are two applications, based on the FieldTrip buffer, that allow to record an online experiment for later playback at the original "speed", and thus help developers with debugging and testing different analysis schemes. The source code for both can be found in the _fieldtrip/realtime/src/utilities/playback_ directory, binaries are at the usual location in _fieldtrip/realtime/bin_.

The first application, **recording**, will act to the outside world as a normal FieldTrip buffer server. Internally, however, every incoming request is also handed to a callback function that stores all incoming data on disk. The program is called like this:

    recording someDirectory [port=1972]

This will spawn the callback-enabled buffer server on the given port, create the given directory (which must NOT exist already), and write a plain text file "contents.txt" into that directory. This file is always the same and just contains a general description of the way the **recording** writes data. Now, each time a header is written, a new subdirectory (starting with 0001) is created, the header is written there in binary and ASCII form, and all further samples and events are also written to binary files. The arrival time of incoming sample and event blocks is measured relative to the arrival time of the header, and logged in an ASCII file called "timing". For stopping the operation, the user may safely press CTRL-C which will close down the server thread and close any open files.

The other application, **playback**, can be started like this:

    playback someDirectory/0001 hostname port

This will replay the data recorded in the first "session" above, at almost exactly the original timing. In contrast to **recording**, this application will not spawn its own buffer server, but it can only stream data to a remote server. The design rational for this was that you might want to replay an experiment several times, but keep the buffer server running in a similar way as it's done with real acquisition systems.

## Creating a new implementation that uses the buffer

| Language | Client | Server | Notes                                                                                                                                      |
| -------- | ------ | ------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| C        | yes    | yes    | Reference implementation, please see [here](/development/realtime/buffer_c)                                                                |
| C++      | yes    | yes    | Thin wrapper classes around the reference implementation for handling client requests, please see [here](/development/realtime/buffer_cpp) |
| MATLAB   | yes    | yes    | Full support via MEX files, please see [here](/development/realtime/buffer_matlab)                                                         |
| Python   | yes    | no     | this depends on [Numpy](http://numpy.scipy.org), please see [here](/development/realtime/buffer_python)                                    |
| Java     | yes    | no     | please see [here](/development/realtime/buffer_java)                                                                                       |

## Closing the loop

For a real-time BCI system, it is important that a control signal somehow can be used to close the loop towards the subject. [Here](/development/realtime/closing_the_loop) you can find a description on the options that you have for [closing the loop](/development/realtime/closing_the_loop) from within your MATLAB-based BCI application.

Current plans and design considerations for building a general pipeline architecture can be found [here](/development/realtime/pipeline).
