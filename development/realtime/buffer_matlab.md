---
title: FieldTrip buffer MATLAB interface
tags: [realtime, development]
---

The FieldTrip toolbox includes an interface to the buffer through the following functions

- **[ft_read_header](/reference/fileio/ft_read_header)**
- **[ft_read_data](/reference/fileio/ft_read_data)**
- **[ft_read_event](/reference/fileio/ft_read_event)**
- **[ft_write_data](/reference/fileio/ft_write_data)**
- **[ft_write_event](/reference/fileio/ft_write_event)**

Access to the real-time buffer provided by the standard FieldTrip reading functions from the fileio module. The API allows for reading header information, event information, and blocks of data.

    % this returns a structure with header information
    hdr    = ft_read_header('buffer://localhost:port')

    % this returns a structure with event/trigger information
    event  = ft_read_event('buffer://localhost:port')

    % this returns a Nchans X Nsamples matrix with the data
    dat    = ft_read_data('buffer://localhost:port', ...)

The interface between MATLAB and the real-time buffer is network transparent. That means that the buffering can be done on one computer, e.g., the one attached to the EEG amplifier, and the computations in MATLAB can be done on another.

## Details on the MATLAB mex-file implementation

In principle the only support that has to be implemented specifically in MATLAB is to allow it connect as client to the buffer server. That could be done using the pnet function from the tcp_udp_ip toolbox. For efficiency reasons and for simplicity, we also have made a direct implementation of the buffer source code in MATLAB by wrappint it into a mex file.

The primary responsibility of the mex file is to allow you from within MATLAB to make a connection to a local or remote buffer and read or write header information, data and/or events.

Furthermore, it is possible to instantiate the buffer as network transparent server, linked to the MATLAB application (the "tcpserver" thread). It is even possible to start a second thread that emulates an EEG acquisition system (the "sinewave" thread).

## Writing a new proxy for acquiring data in MATLAB

You should start by studying the example scripts in the 'realtime' directory, e.g., **[ft_realtime_signalproxy](/reference/realtime/example/ft_realtime_signalproxy)** as an example of how to write random data to a buffer, or **[ft_realtime_pooraudioproxy](/reference/realtime/example/ft_realtime_pooraudioproxy)** as a simple example for reading data from some hardware device and writing into a buffer.

Therefore we have decided to link the streaming of the data with a buffer, i.e. instead of having MATLAB read one sample at a time, we created another standalone application that buffers the data. In MATLAB, you can read any data from this buffer at a time that suits you. e.g., you can read the last 100 milliseconds of data (as a Nchans X Nsamples matrix) and then do your computation on that. During the computation MATLAB will be busy, but the standalone buffer still captures the new data that comes in.
