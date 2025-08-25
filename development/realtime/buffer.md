---
title: Overview of the realtime buffer
tags: [realtime]
redirect_from:
  - /development/realtime/buffer_overview/
---

# Overview of the realtime buffer

This page is part of the documentation series of the FieldTrip buffer for realtime acquisition. The FieldTrip buffer is a standard that defines a central hub (the [FieldTrip buffer](/development/realtime)) that facilitates realtime exchange of neurophysiological data. The documentation is organized in five main sections, being:

1.  description and general [overview of the buffer](/development/realtime/buffer),
2.  definition of the [buffer protocol](/development/realtime/buffer_protocol),
3.  the [reference implementation](/development/realtime/reference_implementation), and
4.  specific [implementations](/development/realtime/implementation) that interface with acquisition software, or software platforms.
5.  the [getting started](/getting_started/realtime/bci) documentation which takes you through the first steps of real-time data streaming and analysis in MATLAB

This page documents the general concept behind the FieldTrip buffer.

## Introduction

There is no fundamental problem in reading data that is acquired in real-time into MATLAB. Even if those data come streaming directly from an EEG amplifier, you still could read one sample at a time and collect it all in one matrix. But since MATLAB is a single threaded application, collecting the continuously streaming data AND processing them at the same time is challenging. Imagine acquiring some samples of the EEG stream and then doing a big computation on those samples, like an fft. During the time that MATLAB needs to compute the fft, the new data that come streaming from your amplifier would get lost. Assuming that the data are streamed over the network, the low-level TCP/IP network stack of your operating system will buffer it for some time, but the duration for which the data remain in that network stack buffer is not guaranteed.

Processing EEG/MEG data in real-time in MATLAB first and foremost requires access to those data. The data are acquired in real-time by the acquisition system (EEG/MEG hardware and acquisition software) and can be streamed into a processing pipeline. To allow for full control of the timing in MATLAB, and to implement the processing pipeline in MATLAB, the stream of data has to be buffered. The FieldTrip buffer is a network transparent TCP server that allows the acquisition client to stream data to it per sample or in small blocks, while at the same time previous data can be analyzed.

More generally, the FieldTrip buffer is used to communicate between separate application programs. One application program is responsible for the acquisition of the data, and it will write the data (and optionally also trigger events) to the buffer. Other application programs can connect to read the data and the events from the buffer and optionally also write new events (e.g., as output of some BCI classification algorithm) to the buffer. The buffer is implemented as a multithreaded application in C/C++ and it allows multiple clients to connect and read/write the data and events simultaneously.

The source code of the buffer can be integrated in any EEG/MEG acquisition or analysis system. The buffer server is instantiated by the acquisition software by first writing the header information to it, describing the number of channels and the sampling frequency. Subsequently, data and/or events can be written to it. There is also a command to flush (or empty) the buffer, which is needed, for example, when a new experimental run is started.

The buffer is compiled into a MATLAB mex file, which means that you can read from, and write to, the buffer in MATLAB. This allows you to process small segments of the real-time streaming EEG data in MATLAB, while incoming new data are buffered in a separate thread. Since the buffer allows multiple concurrent read connections, multiple MATLAB clients can connect to it, each analyzing a specific aspect of the data concurrently. The MATLAB mex file can be used to

- access a remote buffer linked to the acquisition software, which runs as a separate program and possibly even on a separate computer
- instantiate a local buffer, linked to the MATLAB process as a separate thread

Besides the native C/C++ and the MATLAB implementation, we also provide implementations for [Java](/development/realtime/buffer_java) and [Python](/development/realtime/buffer_python).
