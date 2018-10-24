---
layout: default
---

### Details of the tMEG Motor task

Sensory-motor processing is assessed using a task in which participants are presented with visual cues instructing the movement of either the right hand, left hand, right foot, or left foot. Movements are paced with a visual cue, which is presented in a blocked design. This task was adapted from the one developed by Buckner and colleagues¹. Participants are presented with visual cues that ask them to either tap their left or right index and thumb fingers or squeeze their left or right toes. Each block of a movement type lasts 12 seconds (10 movements), and is preceded by a 3 second cue. In each of the two runs, there are 32 blocks, with 16 of hand movements (8 right and 8 left), and 16 of foot movements (8 right and 8 left). In addition, there are nine 15-second fixation blocks per run. EMG signals were used for onset of event for hand and foot movement. EMG electrode stickers are applied as shown in MEG hardware specifications and sensor locations to the skin to the lateral superior surface of the foot on the extensor digitorum brevis muscle and near the medial malleolus, also the first dorsal interosseus muscle between thumb and index finger, and the styloid process of the ulna at the wrist.

#### ￼￼￼Stimulus Overview

In the Motor task, participants executed a simple hand or foot movement. The limb and the side were instructed by a visual cue, and the timing of each movement was controlled by a pacing arrow presented on the center of the screen (A, right). The paradigm included movement and rest blocks (B, right).

![image](/media/tutorial/shared/screen_shot_2015-09-15_at_14.21.52.png@200)

*Figure Caption: A. Hand and Foot movements during the Motor Task. B. Example sequence of stimuli in a block of Right Hand motor movements.*

#### Block/Trial Overview

Each block started with an instruction screen, indicating the side (left, right) and the limb (hand, foot) to be used by the subject in the current block. Then, 10 pacing stimuli were presented in sequence, each one instructing the participant to make a brisk movement. The pacing stimulus consisted of a small arrow in the center of the screen pointing to the side of the limb movement (left or right, above). The interval between consecutive stimuli was fixed to 1200 msec. The arrow stayed on the screen for 150 msec and for the remaining 1050 msec the screen was black.
In addition to the blocks of limb movements there were 10 interleaved resting blocks, each one of 15 sec duration. During these blocks the screen remained black. The last block was always a resting block after the last limb movement block.

The experiment was performed in 2 runs with a small break between them. The block/trial breakdown was identical in both runs. Each of the runs consisted of 42 blocks. 10 of these blocks were resting blocks, and there were 8 blocks of movement per motor effector. This yielded in total 80 movements per motor effector.

In addition to the recorded MEG channels, EMG activity was recorded from each limb. Also ECG and EOG electrodes were used to record heart- and eye movement-related electrophysiological activity.

#### Trigger Overview

The signal on the trigger channel consists of 2 superimposed trigger sequences. One from the Stimulus PC running the E-Prime protocol and one from a photodiode placed on the stimulus presentation screen. The trigger channel for one Motor task run is shown, top right.
The photodiode was activated whenever a cueing stimulus or pacing arrow was presented on the display. It was deactivated when the display was black. The trigger value for on is 255 and the trigger value for off is 0. The photodiode trigger sequence extracted from the trigger channel of one Motor task run is shown, bottom right.

![image](/media/tutorial/shared/screen_shot_2015-09-15_at_14.22.40.png@200)

*Figure Caption: Original Trigger channel sequence from one run of Motor Task. E-Prime and Photodiode triggers are superimposed.*

![image](/media/tutorial/shared/screen_shot_2015-09-15_at_14.22.49.png@200)

*Figure Caption: Photodiode trigger sequence extracted from the Trigger channel of one Motor Task run.*


￼￼
￼The E-Prime triggers contain the information about the experimental sequence. These triggers are superimposed on the photodiode triggers, in the following description it is assumed that the photodiode triggers have been subtracted from the trigger channel so that only the triggers from the E-Prime stimulation protocol remain. Such an E-Prime trigger sequence, extracted from the trigger channel is shown, right.

For descriptions of variables (column headers) to sync the tab- delimited E-Prime output for each run see Appendix 6: Task fMRI and tMEG E-Prime Key Variables². This task contains the following events, each of which is computed against the fixation baseline.

----
 1.  Localizer (Morioka et al. 1995; Bizzi et al. 2008; Buckner et al. 2011; Yeo et al. 2011).
 2.  http://www.humanconnectome.org/documentation/
