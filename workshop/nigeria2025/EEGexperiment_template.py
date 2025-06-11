################################################################################
# Experiment template
# This is a basic template for a PsychoPy experiment. 
################################################################################
# 1. IMPORT

from psychopy import ... # Import necessary modules from PsychoPy, typically including visual, event, core, and data

# Other imports may include: random, serial, pylsl, parallel depending on your setup and requirements. See examples below.

################################################################################
# 2. EXPERIMENT PARAMETERS
# Define experiment parameters such as window size, colors, etc.

n_trials = ...  # Number of trials


# Create a PsychoPy window for visual stimuli.
# see options at https://www.psychopy.org/api/visual/window.html
win = visual.Window() 

################################################################################
# 3. DEFINE STIMULI
# Create stimuli for the experiment.
stimulus = visual.TextStim(win, text='Hello, World!', color='white', height=0.1)

################################################################################
# 4. SETUP EEG TRIGGERS
# If you are using EEG triggers, set up the connection here.
# For example, using a serial port or parallel port for sending triggers.
# Below are three example methods to set up triggers. Only use the one that matches your setup.

# option A: parallel port
try:
    port = parallel.setPortAddress(0x378)  # address for parallel port on many machines (CHECK!!)
    port_type = 'parallel'

# Option C: parallel port
try:
    port = serial.Serial("COM9", 115200)  # Change COM port to match your setup
    port_type = 'serial'

# Option C: LSL
name = "My Experiment"
strm_type = "Markers"
chans = 1
srate = 0
fmt = 'string'

info = pylsl.StreamInfo(
    name=name,
    type=strm_type,
    channel_count=chans,
    nominal_srate=srate,
    channel_format=fmt,
    )
    
outlet = pylsl.StreamOutlet(info)

# Make a trigger function based on the port type
# Option A: parallel port
def trigger(code=1):
    port.setData(code)
    print('trigger sent {}'.format(code)) # Print code for debugging
# Option B: serial port
def trigger(code=1):
    port.write(code.to_bytes(1, 'big'))
    print('trigger sent {}'.format(code)) # Print code for debugging
# Option C: LSL
def trigger(code=1):
    outlet.push_sample(str(code))
    print('trigger sent {}'.format(code)) # Print code for debugging

################################################################################
# 4. DEFINE TRIAL LIST
# For multiple experimental conditions, it is a good idea to define a trial list and randomise it in advance.
...

################################################################################
# 5. RUN EXPERIMENT

# loop through the number of trials and present stimuli
for trial in range(n_trials):
    # Draw the stimulus
    stimulus.draw()
    
    # Flip the window to show the stimulus
    win.flip()
    
    # Wait for a key press to proceed to the next trial
    event.waitKeys()

# Close the window and end the experiment
win.close()
core.quit()