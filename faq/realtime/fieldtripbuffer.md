---
title: Does the FieldTrip realtime buffer only work with MATLAB?
category: faq
tags: [realtime]
redirect_from:
    - /faq/does_the_fieldtrip_realtime_buffer_only_work_with_matlab/
    - /faq/fieldtripbuffer/
---

# Does the FieldTrip realtime buffer only work with MATLAB?

No, the FieldTrip realtime buffer defines a network communication protocol at the level of the TCP/IP protocol. It does not require any specific operating system, programming language or data analysis environment, although we happen to use it a lot in combination with MATLAB and with functions from the FieldTrip toolbox on the analysis side. Most of the applications on the data acquisition side are implemented in C or C++.

Furthermore, it helps to distinguish between the buffer server and the clients.

## C client

This is the [reference implementation](/development/realtime/reference_implementation), i.e. the authoritative example implementation. it is implemented in ANSI C to allow it to compile on a large number of platforms and available in `fieldtrip/realtime/src/buffer`. You can compile it as library and use it in your own software.

## C++ client

A C++ wrapper around the reference implementation is available in `fieldtrip/realtime/src/buffer/cpp`, together with a number of classes that facilitate the development of client applications in C++. Please see [this documentation](/development/realtime/buffer_cpp) for more details.

## Python client

A native Python implementation of the client-side functions is available in `fieldtrip/realtime/src/buffer/python`. Please see [this documentation](/development/realtime/buffer_python) for more details.

## Java client

A native Java implementation of the client-side functions is available in `fieldtrip/realtime/src/buffer/java`. Please see [this documentation](/development/realtime/buffer_java) for more details.

## MATLAB client

The MATLAB implementation consists of the **[ft_read_header](/reference/fileio/ft_read_header)**, **[ft_read_data](/reference/fileio/ft_read_data)** and **[ft_read_event](/reference/fileio/ft_read_event)** functions from the `fieldtrip/fileio` directory. Under the hood, these functions call a mex file in which the [reference implementation](/development/realtime/reference_implementation) is being used. Please see [this documentation](/development/realtime/buffer_matlab) for more details and go through the [getting started](/getting_started/realtime) documentation.
