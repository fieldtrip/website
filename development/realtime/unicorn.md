---
title: Streaming realtime data from Unicorn Hybrid Black
tags: [realtime, unicorn]
---

# Streaming realtime data from Unicorn Hybrid Black

The [Unicorn Hybrid Black](https://www.unicorn-bi.com) 8-channel EEG is a low-cost head-mounted and wireless EEG system that is developed and distributed by [Gtec](https://www.gtec.at). Besides 8 channels of EEG, it provides 3 accelerometer channels, 3 gyroscope channel, the battery status and a sample counter.

The Unicorn is available in a "Black" version, including head-mounted enclosure, and in a "Naked" PCB-only version.

## Interface with MATLAB and FieldTrip

{% include markup/skyblue %}
This MATLAB implementation mainly serves the purpose to test and demonstrate whether the Bluetooth protocol can directly be used on other (non-Windows) computers and to decipher the data stream. This implementation is inefficient and unstable, hence we recommend not to use this for serious research.
{% include markup/end %}

The **[ft_realtime_unicornproxy](/reference/realtime/example/ft_realtime_unicornproxy)** function implements a native interface between the Bluetooth-connected Unicorn system and the [FieldTrip buffer](/development/realtime/buffer).

## Alternative interfaces

### Windows and LSL

The Unicorn system comes with a Windows-only software suite, which uncludes the UnicornLSL application that streams data directly to [LabStreamingLayer (LSL)](https://labstreaminglayer.readthedocs.io). Since LSL is compatible with MATLAB, Python and C/C++, you can use this. This is a robust solution, but requires a Windows data acquisition computer.

### BrainFlow

[BrainFlow](https://brainflow.readthedocs.io/en/stable/SupportedBoards.html) lists the Unicorn as one of the supported systems. It seems that it makes use of Python bindings to the proprietary dynamically linked library (dll) which is available for Windows and Linux (on Intel and Raspberry Pi).  
