---
title: How can I use my MacBook Pro for stimulus presentation in the MEG lab?
category: faq
tags: [matlab]
redirect_from:
    - /faq/how_can_i_use_my_macbook_pro_for_stimulus_presentation_in_the_meg_lab/
---

# How can I use my MacBook Pro for stimulus presentation in the MEG lab?

It can be useful to use your MacBook Pro for stimulus presentation instead of the normal windows based presentation machine. Together with [Psychtoolbox](http://psychtoolbox.org/wikka.php?wakka=HomePage) this offers the possibility to implement complex experimental designs while maintaining reasonably accurate control of stimulus timing.

In order to make use of this setup:

1.  Install the latest version of Psychtoolbox on you Mac
2.  Run MATLAB in 32-bit mode (Psychtoolbox doesn't offer 64-bit support at the moment)
3.  Connect the VGA output to the beamer to your Mac using a minidvi-to-vga adapter
4.  Connect the serial port cable from the presentation machine to your Mac using a usb-to-serial adapter (keyspan)

Within MATLAB you can send trigger events to the acquisition machine as follows:

    delete(instrfind);
    serobjw = serial('/dev/tty.PL2303-00001004'); % Creating serial port object via the keyspan
    serobjw.Baudrate = 115200;             % Set the baud rate at the specific value
    set(serobjw, 'Parity', 'none');        % Set parity as none
    set(serobjw, 'Databits', 8);           % set the number of data bits
    set(serobjw, 'StopBits', 1);           % set number of stop bits as 1
    set(serobjw, 'Terminator', '');        % set the terminator value to newline
    set(serobjw, 'OutputBufferSize', 512); % Buffer for write

    fopen(serobjw);
    fwrite(serobjw,100); % send trigger 100 to acquisition machine
    fclose(serobjw);

The important bit here is to create a serial device which makes use of the keyspan device.
