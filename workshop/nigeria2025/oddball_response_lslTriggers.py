# A simple oddball experiment for EEG demo
#   cf Näätänen et al 1978 (https://doi.org/10.1016/0001-6918(78)90006-9)
from psychopy import visual, core, sound, event
import random
import serial
import pylsl

# Parameters
n_trials        = 1000  # Total number of trials
deviant_prob    = 0.2  # Probability of a deviant tone

# Create a window
win = visual.Window([800, 600])

################################################################################
# FUNCITONS
################################################################################

# MAKE TRIAL STRUCTURE
def make_triallist(length, ratio):
    num_ones = int(length*ratio)
    num_zeros = length-num_ones
    array = [1]*num_ones

    pos = 2  # Ensure the first 3 stimuli are standard
    for ii in range(num_zeros):
        pos = pos + random.randint(2, 8)
        if pos < len(array):
            array.insert(pos, 0)
    
    print(array)
    return array
    
# EEG TRIGGER WITH LSL
name = "oddball_task"
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
print("Now publishing stream:", info.name(), info.type(), info.channel_count(), "channels at", info.nominal_srate(), "Hz")

def trigger(code=1):
    outlet.push_sample(str(code))
    print("Pushed marker {}" .format(code))

# RUN TASK
def run_task(n_trials, ratio):
    
    trl_list = make_triallist(n_trials, ratio)

    # Define the standard and deviant sounds
    standard_tone = sound.Sound(1000, sampleRate=44100, secs=0.031, stereo=True)             # Standard tone
    deviant_tone = sound.Sound(1140, octave=4, sampleRate=44100, secs=0.031, stereo=True)    # Deviant tone

    # Define visual stimuli (here a text showing what tone is playes)
    standard_text = visual.TextStim(win, text='Standard', color='blue')
    deviant_text = visual.TextStim(win, text='Deviant', color='red')
    blank_text = visual.TextStim(win, text='', color='red')
    fixation = visual.TextStim(win, text='+', color='white')

    # Trial loop
    for tt, trl in enumerate(trl_list):
        nextFlip = win.getFutureFlipTime()
        # Find the tone to play and set stimuli accordingly
        if trl == 0:
            deviant_tone.play(when = nextFlip)
            deviant_text.draw()
            trig = 2
        else:
            standard_tone.play(when = nextFlip)
            standard_text.draw()
            trig = 1
        
        # Que the trigger and present stimuli
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
                    trigger(3)
                else:
                    print('wrong!')
                    trigger(4)
            
            if timer.getTime() > 0.25 and timeout is None:
                timeout = True
                blank_text.draw()
                win.flip()
        
        # Check for quit (the Esc or q key)
        if event.getKeys(keyList=["escape","q"]):
            core.quit()

    # Close the window
    win.close()
    core.quit()

################################################################################
# RUN
################################################################################
run_task(n_trials, deviant_prob)

