The "mmfaces" dataset contains EEG, MEG, functional MRI and structural MRI data from research participants that were recorded in multiple runs of a simple task performed on a large number of Famous, Unfamiliar and Scrambled faces. It is described in more detail the data descriptor publication [doi:10.1038/sdata.2015.1](https://www.nature.com/articles/sdata20151) and analyzed in detail in [doi:10.3389/fnhum.2011.00076](http://journal.frontiersin.org/Journal/10.3389/fnhum.2011.00076/abstract).

The original multimodal dataset included simultaneous MEG/EEG recordings on 19 healthy subjects. In the original study, three subjects (sub001, sub005, sub016) were excluded from further analysis.

The dataset used to be available from the [MRC-CBU FTP server](ftp://ftp.mrc-cbu.cam.ac.uk/personal/rik.henson/wakemandg_hensonrn/), but is nowadays maintained on [OpenNeuro](https://openneuro.org/datasets/ds000117).

#### Stimulation details

- The start of a trial was indicated with a fixation cross of random duration between 400 to 600 ms
- The face stimuli was superimposed on the fixation cross for a random duration of 800 to 1,000 ms
- Inter-stimulus interval of 1,700 ms comprised a central white circle
- Two types of stimulation patterns:
  - Immediate: The image was presented consecutively
  - Long: The two images were presented with 5-15 intervening stimuli
- For the purposes of our analysis, we treat these two stimulation patterns of stimuli together
- To maintain attention, subjects were asked to judge the symmetry of the image and respond with a keypress

#### MEG/EEG acquisition details

The MEG data consist of 102 magnetometers and 204 planar gradiometers from a Neuromag/Elekta/Megin VectorView system. The same system was used to simultaneously record EEG data from 70 electrodes (using a nose reference), which are stored in the same “FIF” format file. The above FTP site includes a raw .fif file for each run/subject, but also a second .fif file in which the MEG data have been “cleaned” using Signal-Space Separation as implemented in MaxFilter 2.1.

A Polhemus was used to digitize three fiducial points and a large number of other points across the scalp, which can be used to co-register the M/EEG data with the structural MRI image. Six runs  of approximately 10 minutes each were acquired for each subject, while they judged the left-right symmetry of each stimulus (face or scrambled), leading to nearly 300 trials in total for each of the 3 conditions.

- Sampling frequency: 1100 Hz
- Stimulation triggers: The trigger channel is STI101 with the following event codes:
- Famous faces: 5 (first), 6 (immediate), and 7 (long)
- Unfamiliar faces: 13 (first), 14 (immediate), and 15 (long)
- Scrambled faces: 17 (first), 18 (immediate), and 19 (long)
- Sensors
  - 102 magnetometers
  - 204 planar gradiometers
  - 70 electrodes recorded with a nose reference (Easycap conforming to extended 10-20% system)
  - Two sets of bipolar electrodes were used to measure vertical (left eye; EEG062) and horizontal Electro-oculograms (EEG061). Another set was used to measure ECG (EEG063)
- A fixed 34 ms delay exists between the appearance of a trigger in the trigger channel STI101 and the appearance of the stimulus on the screen

#### MRI acquisition details

The MRI data were acquired on a 3T Siemens TIM Trio, and include a 1x1x1mm T1-weighted structural MRI (sMRI) as well as a large number of 3x3x4mm T2\*-weighted functional MRI (fMRI) EPI volumes acquired during 9 runs of the same task (performed by same subjects with different set of stimuli on a separate visit). (The FTP site also contains DTI and ME-FLASH MRI images from the same subject, which could be used for improved head modeling for example, but these are not used here.) For full description of the data and paradigm, see README.txt on the FTP site or [Wakeman & Henson](http://journal.frontiersin.org/Journal/10.3389/fnhum.2011.00076/abstract).
