---
title: Translating characters received on a serial port to FieldTrip events
---

This page describes the tool **serial2event**, which is located in the directory "realtime/utilities/serial2event", and whose purpose is to write events to a FieldTrip buffer when a character is received on a serial port. The tool was developed specifically to be run on the presentation machines in the DCCN's MRI labs in order to forward TTL pulses from the scanner to the FieldTrip buffer.

The user has the option to either only react on specific characters, and to write events with
a fixed _type_ and _value_, or to forward the received character as the _value_ of the event.
The _sample_ field of the event can be auto-incremented, and reset by sending the string "RESET"
to the UDP port (default = 1990) on which the tool listens. The latter feature is used in the DCCN's MRI lab to reset the sample counter when a new sequence is started on the scanner host (which is then picked up by the [fMRI gui_streamer](/getting_started/realtime/fmri) tool).

The tool is started from the command line by typing

    serial2event [config-file]

If the "config-file" argument is not given, a default of "serial2event.conf" is assumed.

### Configuration file syntax

The operation mode of the tool is controlled by given a configuration file. A documented example follows below:

```ini
  # Comment lines must start with a hash, empty lines are silently ignored

  # buffer: FieldTrip buffer in the form hostname:port
  # without quotes
    buffer=mentat069:1972

  # serial: Parameters of the serial port in the form
  #   portname:baudrate:databits:stopbits:parity
  # all numbers must be >=0, parity may only be 0 or 1
    serial=COM3:115200:8:1:0

  # character: specify single character to react on, or
  # comment this out to react to every incoming character
    character=H

  # type: Type of event as either an integer, double
  # precision number, or string (e.g., "serial")
    type="serial"

  # value: Value of event, can be integer/double/string
  # or @ to pass on serial character
    value="click"

  # sample: number to transmit with first pulse plus
  # increment per pulse, e.g., 0+1  (sends 0,1,2,3,...)
    sample=-5+1

  # offset and duration: integer numbers
    duration=0
    offset=0

  # UDP port for RESET messages
    port=1990
```

### Compilation

We provide a simple "Makefile" for the MinGW compiler or GCC. Please go to the "realtime/utilities/serial2event" directory and type "make" or "mingw32-make". Note that you might need to [compile](/development/realtime/buffer) the **buffer** library first.
