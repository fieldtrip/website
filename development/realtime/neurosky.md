---
title: Streaming realtime data from Neurosky ThinkCap
tags: [realtime, neurosky]
---

This page describes the interface between the 7 channel wireless ThinkCap of Neurosky and the FieldTrip buffer.

We provide a standalone tool (see "realtime/acquisition/neurosky") to grab raw data packets from the serial port (via bluetooth), and stream it to a FieldTrip buffer. The application is called **thinkgear2ft** and allows to specify which channels to stream and save in a configuration file like this:

    [select]
    1=Ns1
    2=Ns2
    ...
    7=Ns7

You would then call the application like this:

    thinkgear2ft COM5: config.txt localhost 1972 8000

where `COM5:` is the serial port that the operating system created for the bluetooth connection. This depends on how you set up the device, and you might use something like "/dev/tty.thinkcap" on macOS. "config.txt" is the name of the configuration file, "localhost" and "1972" are the address and port number of the buffer server, and the argument is the number of the TCP port that the tool should listen to for OnlineDataManager commands. Actually, the last three parameters in the example above are the defaults for these arguments, so you can leave them out). In case you want to have the buffer server
inside this application, replace the hostname by a minus (-).

## Compilation

On the command line, change to the "realtime/datasource/neurosky" directory and type "make". The Makefile will also work with the MinGW compiler on Windows. Note that you might need to [compile](/development/realtime/buffer) the **libbuffer** library first.

## External links

- http://www.neurosky.com/
