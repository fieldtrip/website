---
title: Streaming realtime data from Micromed
tags: [realtime, micromed]
---

Micromed is company based in Italy that develops systems for clinical neurophysiology. One of the systems that is used commonly in combination with real-time analysis and BCI is their ECoG amplifier, with which neuronal activity can be recorded directly from the brain surface using up to 128 channels. The Micromed ECoG system has the feature of sending the data over the network to be analyzed in external software. The Micromed acquisition software can connect to a remote TCP server. Once the connection is made, the data is streamed from the acquisition software TCP client towards the TCP server.

## Interface with MATLAB and FieldTrip

The **[ft_realtime_micromedproxy](/reference/realtime/example/ft_realtime_micromedproxy)** function implements the interface between the Micromed acquisition software and the [FieldTrip buffer](/development/realtime/buffer). Using the tcp_udp_ip toolbox, it implements the TCP server on port 5000 to which the Micromed acquisition software can connect. In the Micromed acquisition software, you have to specify the computer on which MATLAB and **[ft_realtime_micromedproxy](/reference/realtime/example/ft_realtime_micromedproxy)** are running.

Once the connection is initiated by the Micromed acquisition software, **[ft_realtime_micromedproxy](/reference/realtime/example/ft_realtime_micromedproxy)** will receive the header information (number of channels and sampling frequency) and subsequently the data. The header and subsequent data that is streaming from the Micromed acquisition software is copied over to the FieldTrip buffer.

Interfacing MATLAB and/or FieldTrip to the realtime Micromed ECoG data stream therefore is as simple as starting the **[ft_realtime_micromedproxy](/reference/realtime/example/ft_realtime_micromedproxy)** in one MATLAB instance, configure the Micromed acquisition software to send the data to that computer, and in another MATLAB instance (which can run on yet another computer) use the function

    ft_read_header(filename)
    ft_read_data(filename, ...)
    ft_read_event(filename, ...)

where you specify

    'buffer://hostname:port'

as the filename to the reading functions.

## License and access to the source code

The **[ft_realtime_micromedproxy](/reference/realtime/example/ft_realtime_micromedproxy)** function is included in the FieldTrip release as pre-compiled .p file. That means that you cannot see or modify the source code. The rt_realtime_micromedproxy function is not released under an open source license, because the Micromed system is licensed according to certain ISO regulations. Since the external link interferes with their system, Micromed does not allow the external TCP link to be documented. However, the company has indicated that upon request from registered Micromed users the source code of the **[ft_realtime_micromedproxy](/reference/realtime/example/ft_realtime_micromedproxy)** can be released to that user.

If you want to have the source code of the **[ft_realtime_micromedproxy](/reference/realtime/example/ft_realtime_micromedproxy)**, please contact Cristiano Rizzo at Micromed (for the permission) and Robert Oostenveld at the Donders Centre (for the copy of the latest code).

## Alternative interface using BCI2000

The Micromed system is also supported by [BCI2000](http://www.bci2000.org), which means that you can use the interface between BCI2000 and FieldTrip as an alternative to the rt_micromedproxy function. That interface is documented [here](/development/realtime/bci2000) and [here](http://www.bci2000.org/wiki/index.php/Contributions:FieldTripBuffer).

## External links

- http://www.micromed.eu
