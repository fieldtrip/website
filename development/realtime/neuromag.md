---
title: Streaming realtime data from Neuromag/Elekta/Megin
tags: [realtime, neuromag]
---

# Streaming realtime data from Neuromag/Elekta/Megin

This software has been developed as a collaboration between [Gustavo Sudre](mailto:gsudre@andrew.cmu.edu) (Carnegie Mellon University), [Lauri Parkkonen](mailto:lauri@neuro.hut.fi) (Aalto University School of Science and Technology), [Elizabeth Bock](mailto:ebock@mcw.edu) and [Sylvain Baillet](mailto:sbaillet@mcw.edu) (Medical College of Wisconsin), and [Wei Wang](mailto:wangwei3@pitt.edu) and [Doug Weber](mailto:djw50@pitt.edu) (University of Pittsburgh). We would also like to thank Robert Oostenveld and Stefan Klanke (Donders/DCCN) for their assistance with the integration with the FieldTrip buffer. Please cite the paper [rtMEG: A Real-time Software Interface for Magnetoencephalography](http://www.hindawi.com/journals/cin/2011/327953/) (Computational Intelligence and Neuroscience,
Volume 2011) in any work that uses it.

The rtMEG software relays signals from a 306-channel Neuromag/Elekta/Megin MEG device in real-time to a FieldTrip buffer. This buffer can then be read by any computer in the same network as the computer hosting the buffer. The data is still stored by the Acquisition computer (i.e. where you run the Acquisition software by Neuromag) as a FIF file, and it can be read by as many computers in the network as necessary. The rtMEG software has the capability of running the FieldTrip buffer by itself, or it can output the data to a separate computer hosting the buffer when necessary. The delay introduced by the software to the data being relayed has been measured to be smaller than 50ms, which is sufficient for most real-time studies.

For more information on how to read from a FieldTrip buffer, please check [here](/development/realtime) for a collection of technical documents or the [getting started section](/getting_started/realtime/bci).

## Usage

You start it as follows

    neuromag2ft [--option1 value1] [--option2 value2] ...

Without any arguments, the software creates the FieldTrip buffer in the same computer where the Neuromag Acquisition software is running (localhost), with port 1972 and using the length of the buffer currently set in the real-time computer.

The following are the optional arguments available to the use

- chunksize: sets the size of the chunks of data (number of samples, i.e. buffer length) to be sent to the FieldTrip buffer, which determines how many data points (per channel) will be sent to the FieldTrip buffer. This changes the value set in the real-time computer (rtMEG sets it back to the previous value when the program is terminated). The smaller the buffer length, the shorter the delay in the system, but the higher the load in the computer running rtMEG. However, given that in the default settings the DSPs communicate 28 samples to the real-time computer per packet, setting buflen to a value smaller than 28 is unwise (see below for further information on how the system works). In our experiments, the Acquisition computer was able to handle a buffer with length 29 with a delay smaller than 50ms without any problems.
- bufhost: specifies the hostname of the computer hosting the FieldTrip buffer. This option automatically makes rtMEG communicate with an external host and not lunch its own thread of the FieldTrip buffer.
- bufport: what port to use for communications. If --ftbuffer is specified, this is the port to send the data to in the computer hosting the FieldTrip buffer. If 'ftbuffer' was not specified, then this is the port the buffer will be listening to for reading requests.
- fixchunksize: **ONLY USE IT IN CASE OF ABNORMAL PROGRAM TERMINATION!** If a problem occur and the program unlikely crashes with an unclean exit, it might not properly reset the chunk size to the old value (i.e. if the program was invoked with the chunksize flag when it crashed). Therefore, this argument sets the chunk size to the parameter set in the argument and then quits the program.
- magmul: scales the MEG magnetometer signals by a given factor (no scaling by default).
- gradmul: scales the MEG gradiometer signals by a given factor (no scaling by default).
- eegmul: scales the EEG signals by a given factor (no scaling by default).
- version: displays version information and exits the program.
- help: shows the help text for the different arguments.

## Example scenario

1.  Open a terminal window in the Acquisition computer and go to the folder where you copied the neuromag2ft executable (cd folder). Run it by typing ./neuromag2ft
2.  Because no extra parameters were specified, rtMEG runs its own FieldTrip buffer on port 1972. Start your software that will read from the FieldTrip buffer (see above for options) and point it the acquisition computer's address (e.g., hostname=sinuhe, port=1972).
3.  Start you measurement as you would usually do. Right after you press the Go button, you should start to see MEG data being read by your program. If you don't, there's something wrong.
4.  When you're done, press Ctrl+C in the terminal window where you executed rtMEG.

## How it works

This section gives a simplistic overview of the Acquisition system and how rtMEG fits in. This knowledge is not necessary to run the program, but it might come handy if you want to understand a bit of what is going on behind the scenes.

Each DSP (Digital Signal Processor) manages 12 different channels in the MEG machine (in the most common setup). The several DSPs then send the data they acquire from the channels to the real-time computer (in packets of 28 samples per channel, in the usual setup). The real-time computer sorts the data and applies some calibration values to them. The Acquisition computer talks to the real-time computer to receive the data. It receives the data by requesting "buflen" datapoints per packet, and hence the need for the 'buflen' option. If not used, rtMEG uses the default settings, which are usually around 1s second of data (e.g., buflen=1000 for sampling rate of 1Khz), which is fine for the regular data saving operations, but will be too long for a real-time application.

The data received from the real-time computer are then stored in a local buffer that is used by different Neuromag programs, such as the visualization interface. So, rtMEG taps into this local buffer and reads the data being retrieved from the real-time computer. Once the data has been read, rtMEG writes them to a FieldTrip buffer, which can be easily read by several different clients (see above) using an open source format. This FieldTrip buffer can be run by rtMEG itself, or by a separate computer in the network (i.e. the 'ftbuffer' option).

### Tips

- It's been reported that closing the visualizer window in the Acquisition computer helps when using small buflen values. When this is the case, the data will pass by too fast in the visualizer for anything to be seen anyways, so having it open only consumes computer resources unnecessarily.

- Make sure that the computer reading the data from the FieldTrip buffer can see the computer storing the buffer in the network (i.e. no firewalls blocking the traffic in the necessary ports). That also applies to the case when rtMEG is writing to a different computer that hosts the FieldTrip buffer.

## Distribution

Binaries have been provided for the HP-UX and Linux platforms, which are the two platforms where the Neuromag acquisition software runs. But, if you need to re-compile the software, the sources have also been provided to compile the binary file neuromag2ft. You'll need gcc, gmake, the **buffer** library (provided by FieldTrip), as well as a few libraries provided by Neuromag/Elekta.

For questions, suggestions, or reporting a bug, please email Gustavo Sudre or Lauri Parkkonen. The source code and binaries for rtMEG are available in the FieldTrip repository, or can also be obtained by contacting one of the authors.
