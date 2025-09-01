---
title: Testing with sine waves and pre-recorded EEG data
---

To test the FieldTrip buffer interface between MATLAB and/or other software, you can use a simple sine wave generator.

## MATLAB test function

The **[ft_realtime_signalproxy](/reference/realtime/example/ft_realtime_signalproxy)** is a small MATLAB function that writes data to the buffer. It creates band-pass filtered random noise and streams it continuously to the buffer.

## Stand-alone test application

The **sine2ft** is a test application with a graphical user interface that allows you to set the number of channels, sampling rate, and the frequency and amplitude of the signals that are written to the buffer. It combines well with the [viewer](/development/realtime/viewer) application.

{% include image src="/assets/img/development/realtime/eeg/screen_shot_2015-05-06_at_21.41.03.png" %}
