---
title: Closing the loop in a real-time BCI application
tags: [realtime]
---

To close the loop in your BCI application, you have to communicate the control signal from the application/computer that does the feature extraction and feature translation to the application that is controlled by the BCI system. The application that is controlled by the BCI signal can be anything from a generic stimulus presentation software (e.g., NeuroBS Presentation, ERTS, ANT EEvoke, ...) to a spelling device or to custom-built hardware device (e.g., robot arm).

Before you attempt to close the loop, please make sure that the data is streaming properly and that you are able to process it fast enough. Some examples are given in the [getting started](/getting_started/realtime/bci) section.

## Communicating over a serial port connection

Standard MATLAB already includes functionality to read from and write to serial ports. This uses the **instrfind** and **fopen** functions.

The [Psychtoolbox IOPort](http://docs.psychtoolbox.org/IOPort) is a MEX file for precise control of input/output hardware, e.g., Serial ports (or emulated serial ports like Serial-over-USB etc.),
parallel ports, network ports, and special digital I/O boxes.

The **[ft_write_event](/reference/fileio/ft_write_event)** function includes `serial://<port>?key1=value1&key2=value2&...` as a target stream.

## Communicating to a serial port using a TCP network connection

[HW VSP](http://www.hw-group.com/products/hw_vsp/index_en.html) is a software driver that adds a virtual serial port (e.g., COM5) to the operating system and redirects the data from this port via a TCP/IP network to another hardware interface, which is specified by its IP address and port number. Alternative products are listed here <https://en.wikipedia.org/wiki/COM_port_redirector>.

## Communicating over a parallel port connection

The MathWorks Data Acquisition toolbox supports reading and writing to a parallel port through the **digitalio** function.

The [Psychtoolbox IOPort](http://docs.psychtoolbox.org/IOPort) is a MEX file for precise control of input/output hardware, e.g., Serial ports (or emulated serial ports like Serial-over-USB etc.),
parallel ports, network ports, and special digital I/O boxes.

## Communicating with a VNC server

VNC and derivatives use the Remote Frame Buffer (RFB) protocol for communication. More details and the full specification can be found at https://en.wikipedia.org/wiki/RFB.

The **[ft_write_event](/reference/fileio/ft_write_event)** function includes `rfb://<password>@<host>:<port>` as a target communication stream.

## Communicating over a TCP network connection

Communication over TCP or UDP is possible using the [TCP_UDP_IP toolbox](http://www.mathworks.com/matlabcentral/fileexchange/345).
