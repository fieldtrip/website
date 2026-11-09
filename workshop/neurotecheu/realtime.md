---
title: Realtime EEG data processing
tags: [neurotecheu, realtime, unicorn, eegsynth, lsl]
---

## Unicorn Hybrid Black

The [Unicorn Hybrid Black](https://www.gtec.at/product/unicorn-hybrid-black-bci-platform/) is a good-quality and affordable 8-channel EEG device that is very suited for rapid application development during teaching and hackathons. It comes with its own software (only for Windows) that helps you get started quickly visualizing the EEG signals, and streaming them over LSL or UDP. The Unicorn Recorder application also includes the OSCAR algorithm for real-time data cleaning, which allows both the raw and cleaned data to be streamed.

{% include markup/green %}
On the Unicorn Suite Hybrid Black [GitHub repository](https://github.com/unicorn-bi/Unicorn-Suite-Hybrid-Black/) you can find more documentation and instruction videos.  
{% include markup/end %}

The low-level serial-over-bluetooth Unicorn interface [protocol](https://download.fieldtriptoolbox.org/workshop/neurotecheu/UnicornBluetoothProtocol.pdf) is public, allowing for alternative implementations that are independent from the gtec software. [This page](https://robertoostenveld.nl/unicorn2lsl/) for example describes a native Python interface that also allows streaming data to LSL. [This page](https://github.com/robertoostenveld/unicorn2xx) contains a C/C++ applications for interfacing the Unicorn with a (virtual) audio device, allowing it to be used in Audacity, Ableton Live or Touchdesigner.

{% include markup/yellow %}
If you don't have a windows computer, please pair up during the hackathon with someone that does. The whole experience with the Unicorn Recorder application is just way better, you will get up and running much faster, and the realtime OSCAR cleaning algorithm is very useful.

If you read this at a later moment and if you do have your own Unicorn but no Windows laptop, consider buying a refurbished one.
{% include markup/end %}

### Install the Unicorn software

Please download the installer from the [gtec website](https://www.gtec.at/product/unicorn-suite/) and install it.

{% include image src="/assets/img/workshop/neurotecheu/unicorn_about.png" %}

After installation, you have to pair it with the Unicorn device over Bluetooth. There is a recommended USB Bluetooth dongle, but in my experience it works well enough with the builtin bluetooth of various laptops.

### Pair device over bluetooth

To pair your laptop with the Unicorn EEG system, you switch the Unicorn on by pressing the button a few seconds until it blinks, and then wait for it to appear in the right column. Subsequently, you click on it in the right column to pair it. A generic Windows pop-up will apear and you have to confirm. The Unicorn will then show up in the middle column.

{% include image src="/assets/img/workshop/neurotecheu/unicorn_pairing.png" %}

### Install applications

Besides managing the hardware and licenses (more on that below), the Unicorn Suite Hybrid Black software includes a number of apps that you have to install separately. The relevant ones to install are the recorder and the bandpower app.

The recorder app allows visualization of the data without or with filters, implements OSCAR for realtime denoising, and allows data to be sent over LSL.

{% include image src="/assets/img/workshop/neurotecheu/unicorn_recorder.png" %}

The bandpower app computes spectral power in specific bands, like alpha, beta, etc.

{% include image src="/assets/img/workshop/neurotecheu/unicorn_bandpower.png" %}

There are also a number of complete BCI applications that you can try, like the puzzle game which implements some sort of a visual steady-state evoked potential (SSVEP) interface.

{% include image src="/assets/img/workshop/neurotecheu/unicorn_puzzlegame.png" %}

### Explore APIs

The Unicorn Suite Hybrid Black also includes a number of development tools and [application programming interfaces (APIs)](https://github.com/unicorn-bi/Unicorn-Hybrid-Black-Windows-APIs). If you go through them and download and install them on your computer, you will see that a few of them are free to use, whereas others are licensed. The C/C++ and Net API are free, but the Python and Simulink interfaces require you to get a (paid) license.

{% include image src="/assets/img/workshop/neurotecheu/unicorn_python.png" %}

Luckily these APIs are **not needed** for this hackathon, since we will be using the Lab Streaming Layer (LSL) interface.

There is also a separate "UnicornLSL.exe" application that you can use (see below), but even that is **not needed**. The Unicorn Recorder application mentioned above can be used to stream the data over LSL and UDP.

{% include image src="/assets/img/workshop/neurotecheu/unicorn_lsl.png" %}

## Download and install FieldTrip

This requires that you already have MATLAB installed. Follow the instructions in the [offline](/workshop/neurotecheu/offline) section to download and install FieldTrip, and to add it properly to your path.

## Download and install Python

Follow online instructions elsewhere on the internet to install Python on your computer. Please ensure that you are able to create virtual environments for installing specific software (and their dependencies), either using [Anaconda or Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), or using [virtualenv](https://docs.python.org/3/tutorial/venv.html).

## Using LSL with MATLAB

Follow the installation instructions on the LSL [website](https://labstreaminglayer.org/) or [documentation](https://labstreaminglayer.readthedocs.io).

### Transmitting markers

```matlab
% instantiate the library
disp('Loading library...');
lib = lsl_loadlib();
disp(lsl_library_version(lib));

nchan = 1;
fsample = 0; % required for irregular streams
type = 'cf_string'; % can also be cf_int32 or cf_float32

% make a new stream outlet
disp('Creating a new streaminfo...');
info = lsl_streaminfo(lib, 'My marker stream', 'Marker', nchan, fsample, type, 'yourname');

disp('Opening an outlet...');
outlet = lsl_outlet(info);

% send markers into the outlet
disp('Now transmitting markers...');

% markers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
markers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'};
% markers = {'left_button', 'right_button', 'visual_stimulus', 'auditory_stimulus'};

while true
  % pick a random marker
  thismarker = markers{randi(length(markers))};
  fprintf('Now pushing %s\n', thismarker);
  outlet.push_sample({thismarker});   % note that the string is wrapped into a cell-array
  pause(rand()*2);
end
```

### Transmitting EEG data

```matlab
% instantiate the library
disp('Loading library...');
lib = lsl_loadlib();
disp(lsl_library_version(lib));

nchan = 8;
fsample = 250;
type = 'cf_float32'; % can also be cf_int32 or cf_string
blocksize = 25; % samples per block

% make a new stream outlet
disp('Creating a new streaminfo...');
info = lsl_streaminfo(lib, 'My EEG stream', 'EEG', nchan, fsample, type, 'yourname');

disp('Opening an outlet...');
outlet = lsl_outlet(info);

% send data into the outlet
disp('Now transmitting data...');

while true
  block = round(randn(nchan, blocksize)*100)/100;;
  outlet.push_sample(block);

  str = sprintf('%f, ', block(:,1)); % show only the first column
  fprintf('Pushed data [[%s], ...]\n', str(1:end-2)); % minus the last space and comma
  
  pause(blocksize/fsample);
end
```

### Receiving markers

```matlab
% Instantiate the library
disp('Loading library...');
lib = lsl_loadlib();
disp(lsl_library_version(lib));

% Look for marker streams on the lab network
fprintf('Looking for marker streams...\n');
streams = lsl_resolve_byprop(lib, 'type', 'Markers');

if isempty(streams)
  error('There are no marker streams\n');
else
  % Create a new inlet to read from the first stream
  fprintf('Found stream: %s\n', streams{1}.name());
  inlet = lsl_inlet(streams{1});
end

% Continuously read incoming markers
while true
    % Pull a sample (non-blocking)
    [sample, timestamp] = inlet.pull_sample(0);

    if ~isempty(sample)
      for i=1:length(sample)
        fprintf('Received marker %s\n', sample{i});
      end
    end

  % Avoid excessive CPU usage while polling
  pause(0.001);
end % while
```

### Receiving EEG data

```matlab
% Instantiate the library
disp('Loading library...');
lib = lsl_loadlib();
disp(lsl_library_version(lib));

% Look for marker streams on the lab network
fprintf('Looking for EEG data streams...\n');
streams = lsl_resolve_byprop(lib, 'type', 'EEG');

if isempty(streams)
  error('There are no EEG data streams\n');
else
  % Create a new inlet to read from the first stream
  fprintf('Found stream: %s\n', streams{1}.name());
  inlet = lsl_inlet(streams{1});
end

% Continuously read incoming samples
while true
  % Pull a sample (non-blocking)
  [sample, timestamp] = inlet.pull_sample();

  if ~isempty(sample)
    str = sprintf('%f, ', sample);
    fprintf('Received data [%s]\n', str(1:end-2)); % minus the last space and comma
  end

  % Avoid excessive CPU usage while polling
  pause(0.001);
end % while
```

## Using LSL with Python

Follow the installation instructions on the LSL [website](https://labstreaminglayer.org/) or [documentation](https://labstreaminglayer.readthedocs.io).

### Transmitting markers

```python
import pylsl
import time
import random

# on my M3 MacBook I had to recompile the LSL library and then this is needed
# export DYLD_LIBRARY_PATH=/Users/roboos/matlab/liblsl-maca64/bin

time.sleep(3)  # wait a bit to allow LSL to synchronize

info = pylsl.StreamInfo(
    name='My marker stream',
    type='Marker',
    channel_count=1,
    nominal_srate=0, # should be zero for markers
    channel_format=pylsl.cf_string,
    source_id='',
)

# Create a new outlet
outlet = pylsl.StreamOutlet(info)

# Print the stream info
print("Now publishing stream:", info.name(), info.type(), info.channel_count(), "channels at", info.nominal_srate(), "Hz")

# markers = ['left_button', 'right_button', 'visual_stimulus', 'auditory_stimulus']
markers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

print("now sending markers...")
while True:
    # pick a sample to send an wait for a bit
    thismarker = [random.choice(markers)]
    print("Pushing marker:", thismarker)
    outlet.push_sample(thismarker)
    time.sleep(random.random()*2)
```

### Transmitting EEG data

```python
import pylsl
import time
import random 

# on my M3 MacBook I had to recompile the LSL library and then this is needed
# export DYLD_LIBRARY_PATH=/Users/roboos/matlab/liblsl-maca64/bin

time.sleep(3)  # wait a bit to allow LSL to synchronize

nchan = 8
fsample = 250
blocksize = 25

info = pylsl.StreamInfo(
    name='My EEG stream',
    type='EEG',
    channel_count=nchan,
    nominal_srate=fsample,
    channel_format=pylsl.cf_float32,
    source_id='',
)

# Create a new outlet
outlet = pylsl.StreamOutlet(info)

# Print the stream info
print("Now publishing stream:", info.name(), info.type(), info.channel_count(), "channels at", info.nominal_srate(), "Hz")

# Continuously send blocks of data
while True:
    # Generate a block: 25 samples x 8 channels
    block = []
    for i in range(blocksize):
        row = [round(random.random(), 2) for ch in range(nchan)]
        block.append(row)

    # Push the entire block
    outlet.push_chunk(block)

    # Print the block for debugging
    print("Pushed block:", block)

    # Sleep for the duration of the block (100 ms)
    time.sleep(blocksize / fsample)
```

### Receiving markers

```python
import pylsl
import time

# on my M3 MacBook I had to recompile the LSL library and then this is needed
# export DYLD_LIBRARY_PATH=/Users/roboos/matlab/liblsl-maca64/bin

time.sleep(3)  # wait a bit to allow LSL to synchronize

# first resolve a marker stream on the lab network
print("Looking for a marker stream...")
streams = pylsl.resolve_byprop('type', 'Marker')
print(streams)

if len(streams)==0:
    raise Exception("There are no marker streams")
else:
    # Create an inlet for the first stream
    inlet = pylsl.StreamInlet(streams[0])

while True:
    sample, timestamp = inlet.pull_sample()
    if len(sample):
        print(f"Received marker {sample}")
```

### Receiving EEG data

```python
import pylsl
import time

# on my M3 MacBook I had to recompile the LSL library and then this is needed
# export DYLD_LIBRARY_PATH=/Users/roboos/matlab/liblsl-maca64/bin

time.sleep(3)  # wait a bit to allow LSL to synchronize

# first resolve a marker stream on the lab network
print("Looking for an EEG data stream...")
streams = pylsl.resolve_byprop('type', 'EEG')
print(streams)

if len(streams)==0:
    raise Exception("There are no marker streams")
else:
    # Create an inlet for the first stream
    inlet = pylsl.StreamInlet(streams[0])

while True:
    sample, timestamp = inlet.pull_sample()
    if len(sample):
        print(f"Received data {sample}")
```

## Plotting an EEG data stream

With some modifications to the code above, we can visualize the data stream that we are receiving by repeatedly plotting the last N seconds. For that you can make use of a [circular buffer](https://en.wikipedia.org/wiki/Circular_buffer) (also known as a ring buffer), i.e. a matrix where for every sample that you receive you remove the first column and then add the latest sample as the last column.

## Filtering an EEG data stream

An important difference between filtering data in real-time versus reading continuous data in memory and then filtering it, is that real-time data arrives in small blocks. First of al, we cannot use a two-pass filter. Furthermore, we don't want filter edge artifacts and hence have to maintain the filter state between the blocks.

In MATLAB this can be achieved with the low-level **[ft_preproc_online_filter_init](/reference/preproc/ft_preproc_online_filter_init)** and the **[ft_preproc_online_filter_apply](/reference/preproc/ft_preproc_online_filter_apply)** functions from the FieldTrip [preproc module](/development/module/preproc) (see also this [architecture](/development/architecture/#modular-organization) diagram).

In Python you should be able to use functions from the low-level [SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.sosfilt.html) package or from [MNE-Python](https://mne.tools/stable/index.html).

## Stimulus presentation in MATLAB

With MATLAB you can use [Psychtoolbox (PTB)](https://psychtoolbox.org) for stimulus presentation and experimental control. Although Psychtoolbox started as an open source project, at a certain point the developers switched to a paid license model for their ongoing efforts in maintenance and support. The latest version of Psychtoolbox that is completely free is [3.0.19.16 ("Last free desert")](https://github.com/Psychtoolbox-3/Psychtoolbox-3/releases/tag/3.0.19.16).

```matlab
% this implements a very basic visual oddball task using Psychtoolbox-3
% see https://en.wikipedia.org/wiki/Oddball_paradigm for more details

clear
clc

% Configuration
nTrials = 150;
stimulusDuration = 0.200;
fixationDuration = 0.850;
jitterRange = 0.300;
initialFixationDuration = 2.0;

% Initialize Psychtoolbox
PsychDefaultSetup(2);

% the sync tests are important for precise timing, but require all drivers and settings to be correct
% we can skip the test to allow running this example on non-optimized laptops
Screen('Preference', 'SkipSyncTests', 1);

screens = Screen('Screens');
screenNumber = max(screens);

black = BlackIndex(screenNumber);
white = WhiteIndex(screenNumber);
green = [0 1 0];
red = [1 0 0];

[window, windowRect] = PsychImaging('OpenWindow', screenNumber, black);
Screen('BlendFunction', window, 'GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA');
[xCenter, yCenter] = RectCenter(windowRect);
Screen('TextFont', window, 'Arial');

% Prepare stimuli
fixation = '+';
standard = 'STANDARD';
deviant  = 'DEVIANT';

% Keyboard configuration
KbName('UnifyKeyNames');
spaceKey = KbName('space');
escapeKey = KbName('ESCAPE');

% Wait for SPACE to start
DrawFormattedText(window, 'Press SPACE to start', 'center', 'center', white);
Screen('Flip', window);

while true
    [keyIsDown, ~, keyCode] = KbCheck;
    if keyIsDown && keyCode(spaceKey)
        break;
    end
    if keyIsDown && keyCode(escapeKey)
        sca;
        return;
    end
    WaitSecs(0.01);
end
KbReleaseWait;

% Initial fixation
DrawFormattedText(window, fixation, 'center', 'center', white);
Screen('Flip', window);
WaitSecs(initialFixationDuration);

% Generate randomized trial sequence with 80% standard and 20% deviant
conditions = [ ...
    repmat({'s'}, 1, round(nTrials * 0.8)), ...
    repmat({'d'}, 1, round(nTrials * 0.2)) ...
    ];
conditions = conditions(randperm(nTrials));

fprintf('Starting oddball task...\n');

for trial = 1:nTrials
    condition = conditions{trial};

    % Select stimulus
    if strcmp(condition, 's')
        stimulus = standard;
        color = green;
        textSize = 50;
    else
        stimulus = deviant;
        color = red;
        textSize = 100;
    end

    % Present stimulus
    fprintf('Trial %d/%d: %s\n',  trial, nTrials, condition);
    Screen('TextSize', window, textSize);
    DrawFormattedText(window, stimulus, 'center', 'center', color);
    onset = Screen('Flip', window);

    % Prepare fixation screen
    Screen('TextSize', window, 50);
    DrawFormattedText(window, fixation, 'center', 'center', white);

    % Schedule fixation onset 200 ms after stimulus onset
    ifi = Screen('GetFlipInterval', window);
    offset = Screen('Flip', window, onset + stimulusDuration - 0.5 * ifi);

    % Wait until next trial
    jitter = rand() * jitterRange;
    WaitSecs(fixationDuration + jitter);

    % Check for ESC
    [keyIsDown, ~, keyCode] = KbCheck;
    if keyIsDown && keyCode(escapeKey)
        fprintf('Pressed ESC\n');
        break;
    end
end

% Finish
DrawFormattedText(window, 'Done, press SPACE to finish', 'center', 'center', white);
Screen('Flip', window);

while true
    [keyIsDown, ~, keyCode] = KbCheck;
    if keyIsDown && keyCode(spaceKey)
        break;
    end
    WaitSecs(0.01);
end

% Clean up
sca;

fprintf('Oddball task finished.\n');
```

## Stimulus presentation in Python

With Python you can use [PsychoPy](https://psychopy.org) for stimulus presentation and experimental control. PsychoPy can be installed in a virtual environment using pip. Since PsychoPy comes with an (optional) graphical user interface, there is also a stand-alone version that you can download and run as a GUI. Since with the code above we have already been scripting in MATLAB and Python, I recommend not to use the GUI but rather also use scripting for PsychoPy.

The following example implements a simple visual experiment and can be used to get started.

```python
# this implements a very basic visual oddball task using PsychoPy
# see https://en.wikipedia.org/wiki/Oddball_paradigm for more details

from psychopy import visual, core
from utilities import wait_for_space
import random
import pylsl

# Prepare the LSL stream info
info = pylsl.StreamInfo(
    name='Stimulus computer',
    type='Markers',
    channel_count=1,
    nominal_srate=0, # should be zero for markers
    channel_format='string',
    source_id='',
)

# Create a new outlet
outlet = pylsl.StreamOutlet(info)

# Print the stream info
print("Now publishing stream:", info.name(), info.type(), info.channel_count(), "channels at", info.nominal_srate(), "Hz")

screen = visual.Window([800, 600], color='black', units='pix')
fixation = visual.TextStim(screen, text='+', color='white', height=50)
standard = visual.TextStim(screen, text='STANDARD', color='green', height=50)
deviant  = visual.TextStim(screen, text='DEVIANT', color='red', height=100)

wait_for_space(screen, 'Press SPACE to start')
fixation.draw()
screen.flip()
core.wait(2)

# present 10 trials of the oddball task
# where 80% of the stimuli are standard and 20% are deviant
for trial in range(10):
    # randomly choose a stimulus for each trial
    condition = random.choice(['s', 's', 's', 's', 'd'])  # 80% standard, 20% deviant

    if condition == 's':
        print('standard')
        stimulus = standard
    else:
        print('deviant')
        stimulus = deviant

    stimulus.draw()  # present the randomly chosen stimulus
    screen.flip()
    outlet.push_sample([condition])  # send marker to LSL
    core.wait(0.2)

    fixation.draw()
    screen.flip()
    jitter = random.uniform(0, 0.3)
    core.wait(0.85 + jitter)

wait_for_space(screen, 'Done, press SPACE to finish')

screen.close()
core.quit()
```
