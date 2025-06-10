################################################################################
# Oddball EEG Experiment Tutorial
################################################################################
# This script demonstrates a simple "oddball" paradigm for EEG experiments.
# The oddball paradigm is used to study how the brain responds to rare ("deviant")
# stimuli among frequent ("standard") stimuli, as in Näätänen et al. (1978).
#
# The experiment presents a sequence of tones:
#   - Most are "standard" (1000 Hz, blue text)
#   - Some are "deviant" (1140 Hz, red text)
# Participants are instructed to press SPACE when they hear a deviant tone.
# EEG triggers are sent for each stimulus and response.
#
# Key Sections:
# 1. Imports and Parameters
# 2. Trial List Generation
# 3. EEG Trigger Setup
# 4. Main Experiment Loop
#
# Walk through the code and see comments for explanations!
# Try modifying parameters or the trial structure to see how the experiment changes!

################################################################################

# 1. IMPORTS AND PARAMETERS
# Import necessary libraries for stimulus presentation, timing, sound, and EEG triggers.
from psychopy import visual, core, sound, event, parallel
import random
import serial

# Set the number of trials and the probability of a deviant tone.
n_trials        = 1000  # Total number of trials
deviant_prob    = 0.2  # Probability of a deviant tone

# Create a PsychoPy window for visual stimuli.
win = visual.Window([800, 600])

################################################################################
# 2. TRIAL LIST GENERATION
################################################################################

# This function creates a list of trials, with 1 = standard, 0 = deviant.
# Deviants are spaced out so the first three are always standard.
def make_triallist(length, ratio):
    num_ones = int(length*ratio)
    num_zeros = length-num_ones
    array = [1]*num_ones

    pos = 2  # Ensure the first 3 stimuli are standard
    for ii in range(num_zeros):
        pos = pos + random.randint(2, 8)
        if pos < len(array):
            array.insert(pos, 0)
    
    print(array)  # For debugging: shows the trial sequence
    return array

################################################################################
# 3. EEG TRIGGER SETUP
################################################################################

# The script tries to connect to a serial port for EEG triggers.
# If unavailable, it tries the parallel port. If neither, triggers are not sent.
try:
    port = serial.Serial("COM9", 115200)  # Change COM port to match your setup
    port_type = 'serial'
except NotImplementedError:
    port = parallel.setPortAddress(0x378) # address for parallel port on many machines (CHECK!!)
    port_type = 'parallel'
except:
    port_type = 'Not set'

print('port type: {}'.format(port_type))

# Define the trigger function based on available port type.
if port_type == 'parallel':
    def trigger(code=1):
        port.setData(code)
        print('trigger sent {}'.format(code))
elif port_type == 'serial':
    def trigger(code=1):
        port.write(code.to_bytes(1, 'big'))
        print('trigger sent {}'.format(code))
else:
    def trigger(code=1):
        print('trigger not sent {}'.format(code))

################################################################################
# 4. MAIN EXPERIMENT LOOP
################################################################################

def run_task(n_trials, ratio):
    
    trl_list = make_triallist(n_trials, ratio)

    # Define standard and deviant tones
    standard_tone = sound.Sound(1000, sampleRate=44100, secs=0.031, stereo=True)
    deviant_tone = sound.Sound(1140, octave=4, sampleRate=44100, secs=0.031, stereo=True)

    # Visual feedback for each tone
    standard_text = visual.TextStim(win, text='Standard', color='blue')
    deviant_text = visual.TextStim(win, text='Deviant', color='red')
    blank_text = visual.TextStim(win, text='', color='red')

    # Loop through each trial
    for tt, trl in enumerate(trl_list):
        nextFlip = win.getFutureFlipTime()
        if trl == 0:
            deviant_tone.play(when=nextFlip)
            deviant_text.draw()
            trig = 2
        else:
            standard_tone.play(when=nextFlip)
            standard_text.draw()
            trig = 1

        win.callOnFlip(trigger, trig)
        win.flip()  # Show the visual stimulus

        # Collect responses during the stimulus duration
        response = None
        timeout = None
        timer = core.Clock()
        while timer.getTime() < 0.80:
            keys = event.getKeys(keyList=["SPACE", "space"])
            if keys and response is None:
                response = True
                if trl == 0:
                    print('correct!')
                    trigger(4)
                else:
                    print('wrong!')
                    trigger(8)
            
            if timer.getTime() > 0.25 and timeout is None:
                timeout = True
                blank_text.draw()
                win.flip()

        # Allow quitting with Esc or q
        if event.getKeys(keyList=["escape", "q"]):
            core.quit()

    # Close the window at the end
    win.close()
    core.quit()

################################################################################
# 5. RUN THE EXPERIMENT
################################################################################
run_task(n_trials, deviant_prob)
################################################################################
