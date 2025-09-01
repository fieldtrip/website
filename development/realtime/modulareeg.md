---
title: Streaming realtime data from Modular EEG (aka OpenEEG)
tags: [realtime, modeeg, openeeg]
---

This page describes the interface between the 2-6 channel Modular EEG amplifier of the OpenEEG project and the FieldTrip [buffer](/development/realtime/buffer).

## Standalone program modeeg2ft/modeeg2ft_2chn

We provide two standalone tools (see "realtime/src/acquisition/modeeg" and "realtime/bin") to grab data from the serial port, and stream it to a FieldTrip buffer. The first one is called **modeeg2ft** and allows to specify which channels to stream and save in a configuration file like this:

    [select]
    1=Left
    2=Right

You would then call the application like this:

    modeeg2ft COM5: config.txt  nameOfGDF  localhost  1972

where "COM5:" is the serial port on which the amplifier is connected (use something like "/dev/ttyS0" on Linux), "config.txt" is the name of the configuration file, "nameOfGDF" is the name of the GDF file where data should be saved to (extension ".gdf" will be added automatically), and "localhost" and "1972" are the address and port number of the buffer server (actually, these are the defaults for the last two arguments, so you can leave them out). In case you want to have the buffer server
inside this application, replace the hostname by a minus (-).

The second tool is called **modeeg2ft_2chn** and is basically a simplification of **modeeg2ft**: For this, always two channels are read, and there is no need for a configuration file. Just call for example

    modeeg2ft_2chn COM5:  nameOfGDF  localhost  1972

If you don't want to save data to GDF, you can replace the second argument ("nameOfGdf") by a minus (-).

### Compilation

On the command line, change to the "realtime/datasource/modeeg" directory and type "make". The Makefile will also work with the MinGW compiler on
Windows. Note that you might need to [compile](/development/realtime/buffer) the **libbuffer** library first.

### Support for macOS

#### Using a USB cable

If your ModEEG uses the FT232RL USB-to-serial converter, you may have to install a driver to access it.

First check

    ls -al /dev/*usbserial*

If that is empty, download and install the driver from <http://www.ftdichip.com/Drivers/VCP.htm>. After that, you should see

    powermac> ls -al /dev/*usbserial*
    crw-rw-rw-  1 root  wheel   10,   5 Feb 27 16:16 /dev/cu.usbserial-A9003PV6
    crw-rw-rw-  1 root  wheel   10,   4 Feb 27 16:13 /dev/tty.usbserial-A9003PV6

#### Using Bluetooth

The device that we have at the Donders has a "BlueSmirf FireFly" bluetooth interface. To use it, go to "setup Bluetooth device" in the menu bar. After switching on the amplifier, you will see a FireFly-B106 device. Connect to the device using the passcode 1234. After that you can connect the modeeg2ft application to the serial port at /dev/tty.FireFly-B106.

    powermac> ls -al /dev/tty.FireFly*
    crw-rw-rw-  1 root  wheel   10,   4 Jan 24 12:54 /dev/tty.FireFly-B106-SPP

## Native MATLAB implementation

{% include markup/skyblue %}
The MATLAB implementation is mainly for educational and testing purposes. For proper real-time analyses we recommend you to use the standalone interface, which is faster and requires less system resources.
{% include markup/end %}

On Linux and macOS it is also possible to read from a serial port or bluetooth interface from within MATLAB. To help in decoding the communication protocol, i.e. the byte stream that is sent over the serial interface, we also made a MATLAB implementation.

The MATLAB implementation can be found in **[ft_realtime_modeegproxy](/reference/realtime/example/ft_realtime_modeegproxy)**. It reads the data from the serial interface and copies the first two channels to a FieldTrip [buffer](/development/realtime/buffer).

## Serial port communication protocol

The page <http://openeeg.sourceforge.net/doc/modeeg/firmware/modeeg-p2.c> describes the communication protocol as follows

    // Packet Format Version 2
    // 17-byte packets are transmitted from the ModularEEG at 256Hz,
    // using 1 start bit, 8 data bits, 1 stop bit, no parity, 57600 bits per second.
    // Minimial transmission speed is 256Hz _ sizeof(modeeg_packet) _ 10 = 43520 bps.

     struct modeeg_packet {
        uint8_t sync0; // = 0xA5
        uint8_t sync1; // = 0x5A
        uint8_t version; // = 2
        uint8_t count; // packet counter. Increases by 1 each packet
        uint16_t data[6]; // 10-bit sample (= 0 - 1023) in big endian (Motorola) format
        uint8_t switches; // State of PD5 to PD2, in bits 3 to 0
    };

    // Note that data is transmitted in big-endian format.
    // By this measure together with the unique pattern in sync0 and sync1 it is guaranteed,
    // that re-sync (i.e after disconnecting the data line) is always safe.

## External links

- <http://openeeg.sourceforge.net/doc/>
