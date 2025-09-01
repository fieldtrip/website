---
title: Streaming realtime data from TMSI EEG amplifiers
tags: [realtime, tmsi]
---

We provide two tools for grabbing EEG data from [TMSi](http://www.tmsi.com) amplifiers. The code for both can be found in the directory "realtime/acquisition/tmsi". As far as I know, the FieldTrip code can be used both with the standard REFA and the mobile PORTI systems.

{% include image src="/assets/img/development/realtime/tmsi/refa.jpg" width="200" %}
{% include image src="/assets/img/development/realtime/tmsi/porti.jpg" width="200" %}

Note that the PORTI amplifier is in real life much smaller than it seems to be on the photo above (~20% of the size of the REFA). The type of connectors that you can see on both photos are identical.

### tmsidriver

Bart Niehuis has contributed an acquisition interface and tested it for the TMSI Refa amplifier.

A parameter.txt file lets you edit the sample frequency and the (relative) block size of the data packages that are sent to the FieldTrip buffer. At the moment all channels are sent to the buffer. The first one indicates the sample number. Start the buffer by executing the tmsidriver.exe which will start a cmd window showing the sample frequency and block size. Now you can read the buffer with the FieldTrip buffer functions. Closing the cmd window will stop the tmsi driver.

The interface also saves the data to a text file, which is named after the date and time of the data recording, and will be saved in the same folder as the tmsi-buffer executable file.

### tmsi2ft

Based on code from **tmsidriver**, but also heavily relying on the [common C++](/development/realtime/buffer_cpp) Online Data Manger framework, Stefan Klanke made an alternative implementation and briefly tested it on a PORTI device. In contrast to **tmsidriver**, **tmsi2ft** can save the data to GDF while streaming it out, and the user can select channels and downsampling properties via a configuration file or using the TCP command interface of the OnlineDataManager. This tool will also decode a digital (trigger) channel and write corresponding events to the FieldTrip buffer. You can start the acquisition tool from the command line using

    tmsi2ft config.txt [hostname [port [ctrlPort]]]

where only the first parameter (configuration file) is mandatory. Defaults for the remaining three parameters are "localhost", "1972", and "8000". If you want **tmsi2ft** to spawn its own FieldTrip buffer server, pass a minus (-) for the hostname parameter.

### Compatibility

It is currently not quite clear which driver versions work with the SDK that we use
to compile the aforementioned tools. A brief test with a recent beta version of the driver
for Windows 7 (64-bit), using the old SDK failed.

### Compilation

There is a Visual C++ project file for **tmsidriver**, but both tools can also be compiled using [MinGW](http://www.mingw.org) using the provided "Makefile".
