---
title: FieldTrip Workshop in Göttingen in 2019
---

# FieldTrip workshop in Göttingen in 2019

The Clinic for Clinical Neurophysiology (Georg-August University) in Göttingen Germany will be hosting a FieldTrip Course on MEG Analysis
with Tzvetan Popov and Mats van Es from 4 to 6 of February 2019.

### Where

[Georg-August University Göttingen](https://www.uni-goettingen.de/en/1.html)

### When

Mon 4 Feb - Wed 6 Feb, 2019.

### Who

Tzvetan Popov and Mats van Es.
Local organizer: Daniel van de Velden.

## Program

### Monday 4 February

- **09:00 - 09:15** Registration, welcome and coffee
- **09:15 - 10:15** Lecture I: Introduction to EEG/MEG and introduction to the FieldTrip toolbox _Mats van Es_ - [lecture](/assets/pdf/workshop/goettingen2019/1_introduction.pdf)
- **10:15 - 12:00** Hands-On I: [Introduction to Event-Related Fields](/tutorial/eventrelatedaveraging) - “Preprocessing”
- **12:00 - 13:15** Lunch

- **13:15 - 14:30** Lecture II: Fundamentals of neuronal oscillations and synchrony - “Time-Frequency Analysis” _Mats van Es_ - [lecture](/assets/pdf/workshop/goettingen2019/2_frequency_analysis.pdf)
- **14:30 - 14:45** Q&A so far
- **14:45 - 15:15** Coffee break
- **15:15 - 17:00** Hands On II: [Time-frequency analysis of power](/tutorial/timefrequencyanalysis) - “Time-Frequency Analysis”
- **17:00 - 17:30** Wrap-up-the-day and questions

### Tuesday 5 February 2019

- **09:00 - 10:15** Lecture IV: Source reconstruction using beamformers - “Source Analysis” _Tzvetan Popov_ - [lecture](/assets/pdf/workshop/goettingen2019/3_source_reconstruction.pdf)
- **10:15 - 10:30** Coffee break
- **10:30 - 12:00** Hands On III: [Identifying oscillatory sources using Beamformers](/tutorial/beamformer) – “Source Analysis”
- **12:00 - 13:00** Lunch

- **13:00 - 14:00** Lecture IV: Connectivity analysis of MEG and EEG data - “Connectivity” _Tzvetan Popov_ - [lecture](/assets/pdf/workshop/goettingen2019/4_connectivity_analysis.pdf)
- **14:00 - 14:15** Coffee break
- **14:15 - 15:15** Hands On IV: [Analysis of sensor- and source-level connectivity](/tutorial/connectivity) – “Connectivity”
- **15:15 - 16:15** Lecture V: Statistics using non-parametric randomization techniques - “Statistical Testing/Methods” _Tzvetan Popov_ - [lecture](/assets/pdf/workshop/goettingen2019/5_cluster_statistics.pdf)
- **16:15 - 16:45** Wrap-up-the-day and questions
- **19:00 - 23:00** Social Event

### Wednesday 6 February 2019

- **9:00 - 10:00** Hands On V: [Statistics using non-parametric randomization techniques](/tutorial/cluster_permutation_freq) - “Statistical Testing/Methods”
- **10:00- 10:15** Coffee break
- **10:15- 13:00** FieldTrip Playground (bring your own data)
- **13:00- 13:45** Wrap-up-the-day and Closing remarks

## Getting started with the hands-on sessions

For the hands-on sessions you have to start MATLAB. Make sure you have downloaded the hands-on data prior to the start of the workshop as it is quite a large download. A recent version of FieldTrip can be downloaded [here](https://depot.uni-konstanz.de/cgi-bin/exchange.pl?g=8qar4m9rlc), and the tutorial data can be downloaded [here](https://depot.uni-konstanz.de/cgi-bin/exchange.pl?g=25qbtdhtpp).

{% include markup/red %}
Depending on the unzip program you are using (e.g., Winrar), the name of the zip file might also appear as directory, resulting in path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the FieldTrip directory in a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the MATLAB command window

    restoredefaultpath
    cd path_to_directory/fieldtrip-xxxxxxxx
    addpath(pwd)
    ft_defaults

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using a startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, but only when needed.
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the
official MATLAB toolboxes. The `addpath(pwd)` statement adds the
present working directory, i.e. the directory containing the fieldtrip
main functions. The `ft_defaults` command ensures that all required
subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the data directory

    cd path_to_directory/data
