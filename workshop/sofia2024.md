---
title: FieldTrip workshop in Sofia, Bulgaria
parent: FieldTrip courses and workshops
category: workshop
tags: [sofia2024]
---

# FieldTrip workshop Sofia 07-10.02.2024

[The Institute of Neurobiology](https://inb.bas.bg/index-en.html) at  the [Bulgarian Academy of Science](https://www.bas.bg/?lang=en) is organizing a FieldTrip workshop in Sofia.

# Where

The workshop will take place at **[заседателната зала на Института по Биофизика и Биомедицинско Инженерство при БАН - блок 105](https://www.bas.bg/?page_id=3395)**

# Who

Tzvetan Popov with local organizers and the generous hardware support by [MBrainTrain](https://mbraintrain.com/).

## Program

### **Day 1 - 7.02.2024**

**Session I**

- **09:00 – 09:15** Registration and welcome
- **09:15 – 10:15** **_Lecture_**: Introduction to EEG and the FieldTrip Toolbox
- **10:15 – 10:30** Coffee break
- **10:30 – 12:30** **_Hands-on_**: [Initiation to FieldTrip; Analyzing EEG data (event-related potentials)](https://www.notion.so/9b48e6f48d824aa488b7cea8084a827c?pvs=21)

**Session II**

- **12:30 – 13:30** Lunch
- **13:30 – 14:30** **_Lecture_**: Fundamentals of neuronal oscillations and synchrony
- **14:30 – 14:45** Coffee break
- **14:45 – 16:30** **_Hands-on_**: Time-frequency Analysis of Power
- **16:30 – 17:00** Wrap-up-the-day and Summary

### **Day 2- 08.02.2024**

**Session III**

- **9:00 – 10:45** **_Hyperscanning Demo_**: Demonstration and data acquisition of multiple participants in social cognition context [Ivan Gligorijevic](https://rs.linkedin.com/in/ivan-gligorijevic) from  [MBrainTrain](https://mbraintrain.com/)
- **10:45 – 11:00** Coffee break
- **11:00 – 12:30** **_Hyperscanning Demo_**: Continued
- **12:30 – 13:30** Lunch
- **13:30 – 14:45** **_Lecture_**: Non-parametric permutation techniques
- **14:45 – 15:00** Coffee break
- **15:00 – 16:30** **_Hands-On_**: Statistical Analyses- cluster permutation strategies, MVPA and decoding
- **16:30 – 17:00** Wrap-up-the-day and Summary


### **Day 3 - 09.02.2024**

**Session IV**

- **9:00 – 10:30** **_Lecture_**: Source reconstruction in FieldTrip
- **10:30 – 10:45** Coffee break
- **10:45 – 12:30** **_Hands-on_**: Source Reconstruction on oscillatory data (beamformer)
- **12:30 – 13:30** Lunch

**Session V**

- **13:30 – 15:30** **_Lecture_**: Connectivity analysis
- **15:30 – 15:45** Coffee break
- **15:45 – 16:30** **_Hands-on_**: Connectivity analysis
- **16:30 – 17:00** Wrap-up-the-day and Closing remarks

### **Day 4 - 10.02.2024**

**Session V**

- **09:30 – 11:30** **_FieldTrip Playground_** (bring your own data)
- **11:30 – 11:45** Coffee break
- **11:45 – 13:30** **_FieldTrip Playground continued_**
- **13:30 – 14:00** Wrap-up-the-day and Closing remarks

## Getting started with the hands-on sessions

For the hands-on sessions you have to start MATLAB. Make sure you
have downloaded the hands-on data prior to the start of the workshop as
it is quite a large download. A recent version of FieldTrip can be
downloaded [here](https://cloud.uni-konstanz.de/index.php/s/EkqPeQ9sxYqpCcB),
and the tutorial data can be downloaded
[here](https://www.dropbox.com/scl/fo/29r037lr39mbfzvgrcjmn/h?rlkey=skpwe3ggpx6jeava7udrej4h5&dl=0).

Depending on the unzip program you are using (e.g., Winrar), the
name of the zip file might also appear as directory, resulting in
path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the
FieldTrip directory in a FieldTrip directory. Please fix that by moving
all files one level up.

After copying all files to your computer and unzipping then, you
start MATLAB. To ensure that the right version of FieldTrip is used, and
 not another version (such as the one included in SPM or EEGLAB), you
type in the MATLAB command window

```matlab
restoredefaultpath
cd path_to_directory/fieldtrip-xxxxxxxx
addpath(pwd)
ft_defaults
```

Please do NOT use the graphical path management tool from MATLAB.
In this hands-on session we’ll manage the path from the command line,
but in general you are much better off using a startup.m file than the
path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories
 will be added automatically when needed, but only when needed.

The `restoredefaultpath` command clears your path, keeping only the
official MATLAB toolboxes. The `addpath(pwd)` statement adds the
present working directory, i.e. the directory containing the fieldtrip
main functions. The `ft_defaults` command ensures that all required
subdirectories are added to the path.

If you get the error “can’t find the command ft_defaults” you should check the present working directory.

After installing FieldTrip to your path, you change into the data directory

```matlab
cd path_to_directory/data
```
