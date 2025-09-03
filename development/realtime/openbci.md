---
title: Streaming realtime data from OpenBCI
tags: [realtime, openbci]
---

This page describes the interface between the 8-channel [OpenBCI](http://www.openbci.com) microcontroller board and the FieldTrip buffer. The OpenBCI Board is a versatile and affordable bio-sensing microcontroller that can be used to sample electrical brain activity (EEG), muscle activity (EMG), heart rate (EKG), and more. Besides the 8 ExG channels, it includes an accelerometer, resulting in a total of 11 channels.

{% include image src="/assets/img/development/realtime/openbci/8_perspective_1024x1024.jpg" width="400" %}

The FTDI chip on the OpenBCI dongle requires you to install the FTDI drivers on your machine. You may already have these installed, if you've worked with Arduino or other USB hardware accessories. You can download the latest FTDI drivers for your operating system [here](http://www.ftdichip.com/Drivers/VCP.htm).

## Standalone interface with openbci2ft

You can use **openbci2ft** to transport data from the Cyton USB dongle to a FieldTrip buffer. The **openbci2ft** application is written in C and takes 1 required and 2 optional command line arguments

    openbci2ft <device> [ftHostname] [ftPort]

For example, if you want to stream the data from a specific serial port to a remote buffer on mentat205:1972, you would type

    openbci2ft /dev/tty.usbserial-DN0094FY mentat205 1972

For spawning a local FieldTrip buffer within ** openbci2ft** at port 1234, you would use a dash (-) instead of the second hostname and write

    openbci2ft /dev/tty.usbserial-DN0094FY - 1234

Leaving out the two optional arguments spawns a local buffer on the default port 197

    openbci2ft /dev/tty.usbserial-DN0094FY

### Compilation

On the command line, change to the "realtime/src/acquisition/openbci" directory and type "make". Note that you might need to compile the buffer library first.

## Java implementation

The directory "realtime/src/acquisition/openbci/java" contains an alternative application implemented in Java, which also copies the data from the serial interface to a FieldTrip buffer.
