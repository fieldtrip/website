---
title: Getting started with real-time analysis for BCI and neurofeedback
category: getting_started
tags: [realtime]
redirect_from:
    - /getting_started/realtime/
---

# Getting started with real-time analysis for BCI and neurofeedback

With FieldTrip it is possible to analyze EEG or MEG data in real-time and to create applications for BCI, neurofeedback or for other situations in which you want to be flexible in the analysis and display of data. The real-time support in FieldTrip is not yet as mature as the other functions, so it requires a little more programming from your side.

The general idea behind the real-time processing data in FieldTrip in particular, or in MATLAB in general, is to separate the streaming/buffering from the analysis. Below we'll first describe the buffering of the data, followed by some real-time analysis examples.

{% include markup/skyblue %}
To get some quick satisfaction with streaming data, you might want to try out the example given in this [frequently asked question](/faq/how_should_i_get_started_with_the_fieldtrip_realtime_buffer).
{% include markup/end %}

To get started, you should add the FieldTrip main directory to your path, and execute the **[ft_defaults](/reference/ft_defaults)** function, which sets the defaults and configures up the minimal required path settings. See also this [frequently asked question](/faq/installation).

    addpath <path_to_fieldtrip>
    ft_defaults

## Buffering a real data stream

MATLAB is basically a single-threaded application. There are some computations that MATLAB can do multi-threaded, like fft, but for most practical purposes MATLAB can only handle one task at a time. That means that if the MATLAB session is busy with a computation, it won't have time to capture the incoming data. To solve this, we have created the [FieldTrip buffer](/development/realtime/buffer). This is a piece of low-level c-code that implements a multi-threaded TCP server. The c-code can be compiled into a mex file and therefore can be run from within MATLAB, but it is also possible to include the code in a custom application.

The TCP server is non-blocking and allows for multiple simultaneous read and write requests. It constantly listens to the network for "write" and "read" requests. Upon a write-request, a new piece of data is added to the buffer. With a read-request you can get the latest data from the buffer, but you can also get slightly older data from the buffer. So if your application lags behind a little bit because it was busy with a lengthy computation, you still can catch up and no data will be lost. The actual implementation of the buffer is equivalent to a ring-buffer. For a typical acquisition system with 1kHz sampling rate and with the default settings during compilation, it will hold approximately 10 minutes of data (600000 Samples).

There are different possibilities for getting the data from your acquisition system into the FieldTrip buffer. A comprehensive list is [here](/development/realtime). With [BCI2000](/development/realtime/bci2000) you can use the FieldTrip Buffer to read the data from any of the in BCI2000 supported acquisition system and stream it into the FieldTrip buffer. For some selected acquisition systems, like CTF, Neuralynx and BrainVision a native MATLAB implementation has been created independent of BCI2000. These MATLAB functions act as a proxy between the acquisition system and the FieldTrip buffer. The "ft_realtime_xxxproxy" functions use some acquisition system specific code (e.g., Linux shared memory for CTF, Active-X for Neuralynx and TCP for BrainVision) to read the data from the acquisition system. Once the data is in MATLAB memory it is immediately copied into the FieldTrip buffer. The data in the FieldTrip buffer is subsequently available for analysis in another MATLAB instance.

The following text is tailored for users of ready-made acquisition systems and describes the logic of how to process the data. If you are concerned with integrating a new acquisition system or a similar task, you should read [this page](/development/realtime/buffer) as well.

## Simulating a data stream

Although in the end you'll want to analyze real data from your acquisition system in real-time, it is simpler to start with simulated data or offline data.

### Simulating real-time data from a file

Since the real-time processing in FieldTrip relies on the **[ft_read_header](/reference/fileio/ft_read_header)** and **[ft_read_data](/reference/fileio/ft_read_data)** functions and the [FieldTrip buffer](/development/realtime/buffer), you can get started with all online processing functions that are listed below by just pointing your real-time application to one of your data files on disk.

Instead of reading the data that you want to analyze from file, you can also emulate the acquisition by reading small segments to file and copying it to the FieldTrip buffer, which is implemented in the **[ft_realtime_fileproxy](/reference/realtime/example/ft_realtime_fileproxy)** function. The rt-fileproxy allows you to "replay" previously acquired data in real-time, just as if it is streaming from your acquisition system. The code to analyze the data in real-time would be running in another MATLAB session and would read the data from the buffer as it comes in.

### Simulating real-time data using random numbers

Instead of playing back real data to get a realistic experience , you can also simulate random data using the **[ft_realtime_signalproxy](/reference/realtime/example/ft_realtime_signalproxy)** function. It generates a random signal according to your specification of the number of channels and the sampling frequency. Subsequently the random signal is filtered and written to the buffer. In another MATLAB instance you can then read the signal from that buffer and analyze it. The ft_realtime_signalproxy function is especially useful to test the timing of your analysis code or to do a quick test of the network-transparent data streaming/buffering.

Both the **[ft_realtime_signalproxy](/reference/realtime/example/ft_realtime_signalproxy)** and **[ft_realtime_fileproxy](/reference/realtime/example/ft_realtime_fileproxy)** should be started in a separate MATLAB session, just like all other ft_realtime_XXXproxy functions, i.e. you should have one MATLAB session that generates or reads data from file or acquisition system and writes it to the buffer. In the other MATLAB session, which can be on another computer, you read from the buffer to do real-time analysis and visualization.

## Analyzing the data stream

There are two approaches for processing data in real-time. It might be that you want to analyze all data that comes from the amplifier, irrespective of triggers or events. Alternatively, you might want to analyze only pieces of data following a stimulus. An example of the first could be an imagined movement BCI control system, whereas an example of the second would be a P300 speller.

### Asynchronous/continuous

The basic idea behind continuous data processing is a loop in which you check for new data. You wait until there is new data, and if there is new data you process it. The simplest example for this data is a simple data viewer that lets the data scroll by while being streamed from the acquisition system. This example is implemented in the [ft_realtime_signalviewer](/example/ft_realtime_signalviewer) function.

It gets slightly more complex if you not only want to visualize the data, but also want to do computations on it. The [ft_realtime_powerestimate](/example/ft_realtime_powerestimate) function reads data in small chunks and continuously performs a spectral estimation. The output of this function is a figure with the powers spectrum, averaged over all selected channels, which is constantly being updated.

For a real BCI or neurofeedback application you probably would want to do online feature extraction (e.g., the ratio between the Mu-power over left and right motor areas) and link that to a classifier which makes a decision to control an external device. Starting from the [ft_realtime_signalviewer](/example/ft_realtime_signalviewer) example and then moving on to the [ft_realtime_powerestimate](/example/ft_realtime_powerestimate) example you'll quickly recognize where in the code you can insert your own ideas for the analysis of the data.

### Synchronous/triggered

If the data that you want to analyze is synchronous to some external trigger event, you should keep an eye on the external event. If a new trigger event is present, the corresponding data can be read and processed. A simple example for this is the [ft_realtime_average](/example/ft_realtime_average) function.

A slightly more elaborate example is the [ft_realtime_selectiveaverage](/example/ft_realtime_selectiveaverage) function. It not only checks for events, but it also splits the incoming data over multiple conditions based on the trigger value. Furthermore, this example shows how you can compute some simple t-statistics in real time. The idea behind this example it is that you continue with your experiment until enough "evidence" has been accumulated to distinguish the data in the two conditions.

The third example synchronous processing of data is the [ft_realtime_classification](/example/ft_realtime_classification) function. It reads the data following a trigger and depending on whether that data is marked as "training" data or "test" data, it trains a classifier or it uses the previously trained classifier for single trial classification of the test data. The idea behind this example is that in the first part of the experiment data is available for which the true class is known. In the second part of the experiment, the class is not known any more and the classifier should estimate to which class each trial belongs.

## Closing the loop in a real-time BCI application

To close the loop in your BCI application, you have to communicate the control signal from the application/computer that does the feature extraction and feature translation to the application that is controlled by the BCI system. The application that is controlled by the BCI signal can be anything from a generic stimulus presentation software (e.g., NeuroBS Presentation, ERTS, ANT EEvoke, ...) to a spelling device or to custom-built hardware device (e.g., robot arm).

There are various options for closing the loop documented [here](/development/realtime/closing_the_loop).

## Overview of all examples used here

- [ft_realtime_signalviewer](/example/ft_realtime_signalviewer)
- [ft_realtime_powerestimate](/example/ft_realtime_powerestimate)
- [ft_realtime_average](/example/ft_realtime_average)
- [ft_realtime_selectiveaverage](/example/ft_realtime_selectiveaverage)
- [ft_realtime_classification](/example/ft_realtime_classification)
