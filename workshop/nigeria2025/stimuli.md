---
title: Experimental design and presenting stimuli
tags: [lsl, trigger, nigeria2025]
---

# Experimental design and presenting stimuli

The experimental design of a task can be implemented in a variety of software environments, such as the following:

- [NBS Presentation](https://www.neurobs.com/presentation)
- [PsychoPy](https://psychopy.org), based on Python
- [PsychToolbox](http://psychtoolbox.org), based on MATLAB

They all require some coding or scripting to be done to define the stimuli that will be presented, with their timing, and to deal with responses or input from the participants Furthermore, in the implementation of the experimental task triggers (or markers) need to be sent to the EEG system so that the precise synchronization between stimulus or response and th EEG recording can be used in the subsequent analysis.

## Running an experiment from PsychoPy

When designing an experimental task, we usually start small, and then add complexity.

### Presenting a text item

```python
# The PsychoPy library is used for creating experiments in psychology and neuroscience.
# This code creates a PsychoPy window and displays the text "Hello ABDN!" in white color for 2 seconds before closing the window.
# The window is not full screen, and the text is displayed in a pixel unit with a height of 50 pixels.
# For a proper experiment, we would present this in full screen.

from psychopy import visual, core

myWin = visual.Window([800, 600], color='black', units='pix')
myText = visual.TextStim(myWin, text='Hello ABDN! ', color='white', height=50)

myText.draw()
myWin.flip()
core.wait(2)  # Wait for 2 seconds before closing the window

myWin.close()
core.quit()
```

### Presenting multiple text items as a Stroop task

```python
# this implements a very basic Stroop task using PsychoPy
# see https://en.wikipedia.org/wiki/Stroop_effect for more details

from psychopy import visual, core

myWin = visual.Window([800, 600], color='black', units='pix')
fixation = visual.TextStim(myWin, text='+', color='white', height=50)
text1 = visual.TextStim(myWin, text='RED', color='green', height=50)
text2 = visual.TextStim(myWin, text='GREEN', color='blue', height=50)
text3 = visual.TextStim(myWin, text='BLUE', color='red', height=50)

fixation.draw()
myWin.flip()
core.wait(0.5)
text1.draw()  # present the word RED, in the color green
myWin.flip()
core.wait(0.5)

fixation.draw()
myWin.flip()
core.wait(0.5)
text2.draw() # present the word GREEN, in the color blue
myWin.flip()
core.wait(0.5)

fixation.draw()
myWin.flip()
core.wait(0.5)
text3.draw() # present the word BLUE, in the color red
myWin.flip()
core.wait(0.5)

myWin.close()
core.quit()
```

### Presenting random text as an oddball task

```python
# this implements a very basic oddball task using PsychoPy
# see https://en.wikipedia.org/wiki/Oddball_paradigm for more details

from psychopy import visual, core
import random

myWin = visual.Window([800, 600], color='black', units='pix')
fixation = visual.TextStim(myWin, text='+', color='white', height=50)
standard = visual.TextStim(myWin, text='STANDARD', color='green', height=50)
deviant  = visual.TextStim(myWin, text='DEVIANT', color='red', height=50)

# present 10 trials of the oddball task
# where 80% of the stimuli are standard and 20% are deviant
for trial in range(10):
    # Randomly choose a stimulus for each trial
    stimulus = random.choice([standard, standard, standard, standard, deviant])

    fixation.draw()
    myWin.flip()
    core.wait(0.5)
    stimulus.draw()  # present randomly chosen stimulus
    myWin.flip()
    core.wait(0.5)

myWin.close()
core.quit()
```

### Presenting an auditory oddball task

```python
# this implements a very basic auditory oddball task using PsychoPy
# see https://en.wikipedia.org/wiki/Oddball_paradigm for more details

from psychopy import visual, core, sound
import random

myWin = visual.Window([800, 600], color='black', units='pix')
fixation = visual.TextStim(myWin, text='+', color='white', height=50)
standard = sound.Sound('A', secs=0.5)  # standard sound stimulus
deviant = sound.Sound('C', secs=0.5)   # deviant sound stimulus

# present 10 trials of the oddball task
for trial in range(10):
    stimulus = random.choice([standard, standard, standard, standard, deviant])

    fixation.draw()
    myWin.flip()
    core.wait(0.5)
    stimulus.play()  # play the randomly chosen stimulus
    myWin.flip()

myWin.close()
core.quit()
```

## Synchronization

The most common strategy to synchronize the experimental task with the EEG recording is to use a trigger cable, i.e., a cable from the computer to the EEG amplifier or to the MEG system. In the past the parallel (printer) port of the computer would be used for that, but nowadays computers and laptops only have USB ports.

The USB port of a computer or laptop supports serial-over-usb, which is a common protocol to connect to an external device. Using the serial interface, we can connect to an external device such as an [Arduino](https://www.arduino.cc) development board, or a [BBT interface](https://www.blackboxtoolkit.com). These then translate the trigger value sent over the serial port into a sequence of parallel bits.

An alternative for a hardware cable is to use [LabStreamingLayer](http://labstreaminglayer.readthedocs.io/), which is also known as LSL. This does require that not only the makers are sent over LSL, but also that the EEG is sent over LSL and recorded along with the markers.

## Synchronization from Python

### Sending markers using LSL

```python
import pylsl
import time
import random

# on my M3 MacBook I had to recompile the LSL library and then this is needed
# export DYLD_LIBRARY_PATH=/Users/roboos/matlab/liblsl-maca64/bin

info = pylsl.StreamInfo(
    name='My Marker Stream',
    type='Markers',
    channel_count=1,
    nominal_srate=0, # should be zero for markers
    channel_format='string',
    source_id=None,
)

# Create a new outlet
outlet = pylsl.StreamOutlet(info)

# Print the stream info
print("Now publishing stream:", info.name(), info.type(), info.channel_count(), "channels at", info.nominal_srate(), "Hz")

print("now sending markers...")
markernames = ['fixation', 'stimulus', 'response', '1', '2', '4']
while True:
    # pick a sample to send an wait for a bit
    marker = [random.choice(markernames)]
    print("Pushing marker:", marker)
    outlet.push_sample(marker)
    time.sleep(random.random()*2)
```

### Sending simulated EEG data using LSL

```python
import pylsl
import time

# on my M3 MacBook I had to recompile the LSL library and then this is needed
# export DYLD_LIBRARY_PATH=/Users/roboos/matlab/liblsl-maca64/bin

info = pylsl.StreamInfo(
    name='My EEG Stream',
    type='EEG',
    channel_count=4,
    nominal_srate=1000.0,
    channel_format=pylsl.cf_float32,
    source_id=None,
)

# Create a new outlet
outlet = pylsl.StreamOutlet(info)

# Print the stream info
print("Now publishing stream:", info.name(), info.type(), info.channel_count(), "channels at", info.nominal_srate(), "Hz")

# Create a sample data array
sample = [0.0] * chans
# Continuously send data

while True:
    # Fill the sample with random data
    for i in range(chans):
        sample[i] = i * 0.1  # Replace with actual data acquisition logic
    # Push the sample to the outlet
    outlet.push_sample(sample)
    # Print the sample for debugging
    print("Pushed sample:", sample)
    # Sleep for a short duration to simulate real-time data acquisition
    time.sleep(0.1)  # Adjust the sleep duration as needed

```

### Sending triggers using parallel ports

Parallel ports sends values based on parallel "pins" that each represents a bit in a binary number. For example with eight pins, you can write values from 0-255. Parallel ports are generally the most reliable way of sending triggers as all information is send at the same time.

Be aware that modern PCs and laptops usually do not have parallel ports. In that case, see how to send "parallel" triggers with a serial ports below.

```python
from psychopy import parallel

# Define the port
port = parallel.ParallelPort(0x0378)  
```

The number `0x0378` is the default address (expressed in [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) numbers) for the parallel port on many Windows machines, but it can change from PC to PC. Change to match your machine. To find the address, find the parallel port in the Windows Systems Settings.

To send the triggers, place this code at the appropriate place in your experiment script:

```python
port.setData(code)        # Send trigger code 
port.setData(0)           # Send code 0 = reset pins
print('trigger sent {}'.format(code)) # Print code to terminal for debugging
```

This will send the signal `code` to the parallel port. `Code` should be an integer equal to the trigger value.

### Sending triggers using serial ports (incl. USB)

Serial ports can send different values where the information is send in series of "packages". This means that the timing and how the codes are read at the receiving end can be off if not handled correctly. Serial ports can be used to emulate parallel ports if given only length 1 and proper encoding.

Define the serial port using the `Serial` Python package:

```python
import serial

# Define the port
port = serial.Serial("COM4", 115200) 
```

In this example, the address for serial port is `COM4`. The port address change depending on the PC and how the external device is connected. Change the address to match your machine.

This example takes the integer `code` and transforms it to a code that can be send over serial to emulate a parallel trigger (note this only works for numbers 0-255):

```python
port.write(code.to_bytes(1, 'big'))     # Send trigger code
print('trigger sent {}'.format(code))   # Print code to terminal for debugging
```

#### Find the USB serial port address

Plug in the USB/parallel cable connected to the EEG system.

##### Windows

On most Windows machines the serial port is called "COM" and a number, e.g., "COM3". The exact name vary from machine to machine. Open the Device Manager (from the menu). Go to the overview of devices. Find the one corresponding to the connected device. Somewhere in the name it (usually) list the COM name.

If not, you can try a "brute force" test, and see if you get triggers with any addresses, starting with "COM1", "COM2", and so on.

##### macOS

On macOS, USB ports are found under "devices" and called `tty.<something>`. To find the name, connect the cable, then open a terminal and type:

```bash
ls /dev/tty.*
```

Then find the name that match the connected device. For example:

```python
port = serial.Serial('/dev/tty.usbserial-DN2Q03LO', 115200)
```

### Use win.callOnFlip() to time triggers in PsychoPy

PsychoPy has a build-in method that is supposed to control the timing in how it executes functions to deliver stimuli related to the `Window` module called `callOnFlip()`. The method takes a function and the input to the function as arguments and will call the function immediately after the next `flip()` command. If this the next `flip()` is when the visual stimuli is drawn, the should be function will be executed when the stimuli is drawn.

The first argument should be the function to call, the following arguments should be used exactly as you would for your normal call to the function (can use ordered arguments or keyword arguments as normal, like `callOnFlip(function, *args, **kwargs)`.

For example, if you have a function that you would normally call like this (code is the trigger value):

```python
port.write(code.to_bytes(1, 'big'))
```

You call it though `callOnFlip()` like this:

```python
win.callOnFlip(port.write, code.to_bytes(1, 'big')) 
```

Using this procedure should improve timing.

## Synchronization from MATLAB

### Sending markers using LSL

```matlab
% instantiate the library
disp('Loading library...');
lib = lsl_loadlib();
disp(lsl_library_version(lib));

% make a new stream outlet
disp('Creating a new streaminfo...');
info = lsl_streaminfo(lib, 'BioSemi', 'EEG', 8, 100, 'cf_float32', 'my_laptop');

disp('Opening an outlet...');
outlet = lsl_outlet(info);

% send markers to the outlet
disp('Now transmitting markers...');
markers = {'fixation', 'stimulus', 'response', '1', '2', '4'};
while true
  pause(rand()*3);
  % pick a random marker
  mrk = markers{min(length(markers), 1+floor(rand()*(length(markers))))};
  disp(['now sending ' mrk]);
  outlet.push_sample({mrk});   % note that the string is wrapped into a cell-array
end
```

### Sending triggers using serial ports (incl. USB)

At the Donders we are using trigger boxes that are based on the Arduino Uno or Arduino Mega development boards, which we call "Bitsi" boxes. These boxes have a number of TTL inputs and TTL outputs and are [programmed](https://github.com/robertoostenveld/arduino/tree/main/bitsi) to send the byte that they receive over the serial port to the parallel output. The parallel output is connected to the EEG or MEG system.

The following code can be used with PsychToolbox or generic MATLAB to send triggers over a USB cable via a Bitsi to an EEG system.

```matlab
% this uses the Bitsi MATLAB object to send triggers to a Bitsi device

% for a Windows computer this would be "COM1" or so
b = Bitsi('/dev/cu.usbmodem1101');

while 1
  for i=1:8
    fprintf('bit %d, decimal value %d\n', i, 2^(i-1))
    b.sendTrigger(2^(i-1))
    pause(0.5)
  end
end
```

The following code is the Bitsi helper object, it should be stored in a file that is called `Bitsi.m` (note the capitalization).

```matlab
% Class "Bitsi"
%
% %Constructor%
%
% Bitsi(comport)
%
% When creating a new 'bitsi' object, you can specify to which comport it
% is connected. On windows computers, this is usually something like
% 'com1'.
% When using an empty string for 'comport', the object will run in testing
% mode. In this case it's not required to have the BITSI physically
% connected to the computer. Responses will be read from the keyboard.
%
% *Methods*
% - sendTrigger(code)
% - getResponse(timeout, return_after_response)
% - clearResponses()
% - numberOfResponses()
% - close()
%
%
%
% *sendTrigger(code)*
% code - trigger code, allowed codes 1 - 255. This code is sent to the
% BITSI which will output it on it's parallel output port. The code will be
% reset after 10 miliseconds.
%
% * [response time] = getResponse(timeout, return_after_response)*
%
% This function will take maximally 'timeout' seconds to execute
% return_after_response - allowed values: true or false
%
% False:
% If return_after_response equals false, getResponse will wait for a fixed
% duration (timeout) and record the first response during the wait. The
% first response and it's timeout will be returned after the specified
% timeout.
%
%   <     timeout     >
%   +-----------------+
%   |          A      |
% --+          |      +----------------
%
%
%
% True:
% This method will return as soon as there is a response. Both
% the response and the timestamp of the response will be returned.
% If 'timeout' seconds have been expired without a response, a response
% of 0 will be returned.
%
%   <    timeout     >
%   +-----------+
%   |          A|
% --+          |+----------------
%
%
%
% *Example*
%
%  b = Bitsi('com1');
%
%  b.sendTrigger(20);
%
%  ... do more stuff here
%
%  [r t] = b.getResponse(10, false);
%
%  b.close();
%
%
% If the constructor is called with an empty com port string, no serial connection will be
% established. The serial commands will be echo'd to stdout:
%
%  b = Bitsi('')
%  ...
%
%

classdef Bitsi<handle % extend handle so that properties are modifiable (weird matlab behavior)

  properties (SetAccess = public)
    serobj;
    debugmode = false;
    validResponses = 1:255;
    triggerLog = [];
  end

  methods
    function B = Bitsi(comport)
      if (strcmp(comport, ''))
        fprintf('Bitsi: No Com port given, running in testing mode...\n')
        B.debugmode = true;

        KbName('UnifyKeyNames');
      end

      if (not(B.debugmode))
        delete(serialportfind);
        B.serobj = serialport(comport, 115200);

        % serial port configuration
        set(B.serobj, 'Parity',          'none');
        set(B.serobj, 'Databits',        8);       % number of data bits
        set(B.serobj, 'StopBits',        1);       % number of stop bits
        %set(B.serobj, 'Terminator',      'CR/LF'); % line ending character
        % see also:
        % http://www.mathworks.com/matlabcentral/newsreader/view_original/292759

        %set(B.serobj, 'InputBufferSize', 1);       % set read buffBuffer for read
        set(B.serobj, 'FlowControl',     'none');   %

        % open the serial port
        % fopen(B.serobj);

        % since matlab pulls the DTR line, the arduino will reset
        % so we have to wait for the initialization of the controller
        oldState = pause('query');
        pause on;
        pause(2.5);
        pause(oldState);

        % read all bytes available at the serial port
        status = '[nothing]';

        if B.serobj.BytesAvailable > 0
          status = fread(B.serobj, B.serobj.BytesAvailable);
        end

        %fprintf('BITSI says: %s', char(status));
        %fprintf('\n');
      end
    end

    function sendTrigger(B, code)
      % checking code range
      if code > 255
        fprintf('Bitsi: Error, code should not exeed 255\n');
        return;
      end

      %             if code < 1
      %                 fprintf('Bitsi: Error, code should be bigger than 0\n');
      %             end

      %fprintf('Bitsi: trigger code %i\n', code);

      % log trigger
      B.triggerLog(end+1).value = code;
      B.triggerLog(end).timestamp = GetSecs();

      if ~B.debugmode
        fwrite(B.serobj, code)
      end
    end


    function x = numberOfResponses(B)
      x = B.serobj.BytesAvailable;
    end


    function clearResponses(B)
      if ~B.debugmode
        numberOfBytes = B.serobj.BytesAvailable;
        if numberOfBytes > 0
          fread(B.serobj, numberOfBytes);
        end
      end
    end


    function [response, rt] = getResponse(B, timeout, return_after_response)
      response = 0;
      startTime = GetSecs;

      % start stopwatch
      tic
      if (B.debugmode)
        while toc < timeout
          % poll the state of the keyboard
          [keyisdown, when, keyCode] = KbCheck;

          % if there wasn't a response before and there is a
          % keyboard press available
          if response == 0 && keyisdown
            rt = when - startTime;
            response = find(keyCode);

            if return_after_response
              break;
            end
          end
        end

        % if no response yet after timeout
        if (response == 0)
          rt = GetSecs - startTime;
        end
      else

        % depending on 'return_after_response' this loop will run
        % for timeout seconds or until a response is given
        while toc < timeout

          % if there wasn't a response before and there is a
          % serial character available
          if response == 0 && B.serobj.BytesAvailable > 0

            response = fread(B.serobj, 1);

            % allow only characters present in the
            % validResponses array
            if (any(B.validResponses == response))

              rt = GetSecs - startTime;
              %fprintf('Bitsi: response code %i\n', response);

              if (return_after_response)
                break;
              end

            else
              response = 0;
            end

          end
        end

        % if no response yet after timeout
        if (response == 0)
          rt = GetSecs - startTime;
        end

        % now we waited 'duration' seconds and there might be a
        % button captured, there may be some additional responses
        % in the serial buffer
        B.clearResponses();
      end
    end


    % close
    function close(B)
      if (not(B.debugmode))
        fclose(B.serobj);
        delete(B.serobj);
      end
    end
  end
end

function timestamp = GetSecs()
switch (computer)
  case 'MACA64'
    timestamp = clock_gettime_nsec_np()/1e9; % implemented as a mex file
  otherwise
    error('not implemented')
end
end
```
