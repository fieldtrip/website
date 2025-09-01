---
title: Real-time data processing
tags: [realtime]
---

Although the FieldTrip toolbox is primarily developed for offline analysis, you can also use it for real-time data analysis, feature extraction and classification. To implement Brain-Computer Interface (BCI) and neurofeedback applications, the toolbox includes functionality for real-time processing of all sorts of neuroimaging data (including EEG, MEG, LFP, ECoG, sEEG, NIRS, fMRI) using a common interface to all types of data.

This page is part of the documentation series of the FieldTrip buffer for realtime acquisition. The FieldTrip buffer is a standard that defines a central hub (the [FieldTrip buffer](/development/realtime)) that facilitates realtime exchange of neurophysiological data. The documentation is organized in five main sections, being

1.  description and general [overview of the buffer](/development/realtime/buffer),
2.  definition of the [buffer protocol](/development/realtime/buffer_protocol),
3.  the [reference implementation](/development/realtime/reference_implementation), and
4.  specific [implementations](/development/realtime/implementation) that interface with acquisition software, or software platforms.
5.  the [getting started](/getting_started/realtime/bci) documentation which takes you through the first steps of real-time data streaming and analysis in MATLAB

The page [scratchpad](/development/realtime/scratchpad) contains some loose ends that have no clear place.

### Frequently asked questions

{% include seealso category="faq" tag1="realtime" %}

### Example scripts

{% include seealso category="example" tag1="realtime" %}

### General tips and tricks

If you find you're getting problems you might want to think about the following:

- It's useful to distinguish between reading your data (say, from a hardware device), processing steps, and writing the data (say, to a buffer). Try to separate these things both in your head and your program.
- Can you nail down the source of the problems, or rather, are you really sure which of the components fails? If not, try to swap your components with something simpler. For example, in MATLAB you can initially try to write the data to `empty://` instead of a FieldTrip buffer. This will help you determining whether your acquisition part works correctly. The other way round, you can use the **[ft_realtime_signalproxy](/reference/realtime/example/ft_realtime_signalproxy)** (or ideas from it) to check whether the writing part works.
- Are you having performance problems? Maybe you can initially try to reduce the number of channels or the sample rate, and check whether the program logic is right.
- How much data are you trying to move? If for example you want to write to a buffer on a remote machine, you need to be aware of the physical limits of the network connection.
- You can try moving the actual buffer to another machine, and you do not need to have the buffer attached to a MATLAB session (try using the ''buffer'' application that you will find in fieldtrip/realtime/bin).
- You can try to report and compare the wall clock time with the sample time. Here, wall clock time refers to the real time your computer has run since you started the acquisition loop, while sample time is given by the amount of data processed so far, divided by your sampling frequency. These two numbers should ideally be the same or have a small constant offset, but they should not drift apart. Successive sample and clock times should also match your block size; that is, if you always read 500 samples at a time from a device, and your sampling rate is 1000 Hz, your measured clock time and calculated sample time should increase roughly by 0.5 seconds after each block.

### Ongoing development of the realtime interface

{% include seealso tag1="realtime" tag2="development" %}
