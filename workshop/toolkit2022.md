---
title: Advanced MEG/EEG toolkit at the Donders
tags: [toolkit2022]
---

# Advanced MEG/EEG toolkit at the Donders

This 5-day toolkit course (May 9-13, 2022) will teach you advanced MEG and EEG data analysis skills. Pre-processing, frequency analysis, source reconstruction and various statistical methods will be covered. The toolkit will consist of a number of lectures, followed by hands-on sessions in which you will be tutored through the analysis of a MEG data set using the FieldTrip toolbox.

We hope and expect that we will be able to teach this toolkit on site. Whether or not this will be possible depends on the covid restrictions imposed by the Dutch government. We will notify you in case we need to fall back to an online or hybrid option.

There are 38 places available for this toolkit. The selection of participants will be based on the background experience, the research interest and the expectations on what you will learn (see the questions below). We prefer the group to be reasonably homogeneous in level and expertise of the participants, as this improves the overall interaction.

You can [pre-register here](https://www.ru.nl/donders/agenda/donders-tool-kits/vm-tool-kits/donders-meg-eeg-toolkit/), the deadline for pre-registration is April 10, 2022.

We will inform you as to whether you obtained a place in this course not later than Friday April 22, 2022. The fee for PhD students is € 400; and € 600 for senior researchers; this  fee might be reduced if we have lower expenses due to organizing it completely online.

## Detailed Program

### Monday May 9, 2022

| 09:00-09:30 | Registration and coffee|
| 09:30-10:00 | Welcome|
| 10:00-11:00 | Data acquisition demonstration in the EEG and MEG labs|
| 11:00-11:15 | Coffee Break|
| 11:15-12:30 | Introduction to EEG/MEG and introduction to the FieldTrip toolbox - [lecture by Robert Oostenveld](https://download.fieldtriptoolbox.org/workshop/toolkit2022/slides/introduction.pdf)|
| 12:30-13:30 | Lunch|
| 13:30-15:45 | Pre-processing - [hands-on](/tutorial/eventrelatedaveraging)|
| 15:45-16:00 | Tea Break|
| 16:00-17:30 | FieldTrip playground, apply your newly acquired knowledge and skills|
  
  
### Tuesday May 10, 2022

| 09:00-09:30 | Morning chill or workout|
| 09:45-11:00 | Speaking: evidence from electrophysiology and brain lesions - [lecture by Vitória Piai](https://download.fieldtriptoolbox.org/workshop/toolkit2022/slides/speaking.pdf)|
| 11:00-11:15 | Coffee Break|
| 11:15-12:30 | Time frequency analysis of power - [lecture by Jan-Mathijs Schoffelen](https://download.fieldtriptoolbox.org/workshop/toolkit2022/slides/frequency.pdf)|
| 12:30-13:30 | Lunch|
| 13:30-15:45 | Time-frequency analysis of power - [hands-on](/tutorial/timefrequencyanalysis)|
| 15:45-16:00 | Tea Break|
| 16:00-17:30 | FieldTrip playground, apply your newly acquired knowledge and skills|
| 18:30-22:00 | Drinks & dinner at [De Hemel](https://restaurantdehemel.nl/en/) |
  
  
### Wednesday May 11, 2022

| 09:00-09:30 | Morning chill or workout|
| 09:45-11:00 | Forward and inverse - [lecture by Robert](https://download.fieldtriptoolbox.org/workshop/toolkit2022/slides/forward_inverse.pdf)|
| 11:00-11:15 | Coffee Break|
| 11:15-12:30 | Source reconstruction using beamformers - [lecture by Britta Westner](https://download.fieldtriptoolbox.org/workshop/toolkit2022/slides/beamforming.pdf)|
| 12:30-13:30 | Lunch|
| 13:30-15:45 | Beamforming - [hands-on](/tutorial/beamformer)|
| 15:45-16:00 | Tea Break|
| 16:00-17:30 | FieldTrip playground, apply your newly acquired knowledge and skills|
  
  
### Thursday May 12, 2022

| 09:00-09:30 | Morning chill or workout|
| 09:45-11:00 | Connectivity analysis of MEG and EEG data - [lecture by Jan-Mathijs](https://download.fieldtriptoolbox.org/workshop/toolkit2022/slides/connectivity.pdf)|
| 11:00-11:15 | Coffee Break|
| 11:15-12:30 | Statistics using non-parametric randomization techniques - [lecture by Robert](https://download.fieldtriptoolbox.org/workshop/toolkit2022/slides/statistics.pdf)|
| 12:30-13:30 | Lunch|
| 13:30-15:45 | Statistics - [hands-on](/tutorial/cluster_permutation_timelock)|
| 15:45-16:00 | Tea Break|
| 16:00-17:30 | FieldTrip playground, apply your newly acquired knowledge and skills|
  
  
### Friday May 13, 2022

| 09:00-09:30 | Morning chill or workout|
| 09:45-11:00 | Open science and good practices - [lecture by Robert](https://download.fieldtriptoolbox.org/workshop/toolkit2022/slides/openscience.pdf)|
| 11:00-11:15 | Coffee Break|
| 11:15-12:30 | FieldTrip playground, apply your newly acquired knowledge and skills|
| 12:30-13:30 | Lunch|
| 13:30-15:45 | FieldTrip playground, apply your newly acquired knowledge and skills|
| 15:45-16:00 | Tea Break|
| 16:00-16:30 | Evaluation and testimonials|

## Practicalities

This will be an in-person event.  

### FieldTrip playground sessions: BYOD (bring-your-own-data)
  
A large part of the toolkit will consist of playground sessions, in which ideally you will be working on your own data. Please think a bit about what you want to achieve, and ensure that you have your data easily accessible (preferably, if possible on a laptop that you bring yourself, or on an external USB-drive). If you don't have data to work with, please let us know in time so that we can think about an alternative. We have plenty of tutorial data available, so this can be used to practice your data analysis skills.  

### Test your MATLAB and FieldTrip installation in advance

For the hands-on sessions you will work on a PC that is provided by us. If you want, you can work on your own computer during the FieldTrip playground. If that's the case, we recommend that you [test your MATLAB and FieldTrip installation in advance](/workshop/toolkit2022/test_installation).


## Getting started with the hands-on sessions

For the hands-on sessions we will use MATLAB R2021b, which is installed on the PCs in the instruction rooms. If you log in with the credentials that are provided for each of the course computers, you should start MATLAB using the Desktop shortcut, named 'toolkit2022'. To ensure that everything runs smoothly, we will work with a clean and well-tested version of FieldTrip that we have installed on all computers. Importantly, the tutorial data does not have to be downloaded and has already been placed in the course accounts' home directories. These home directories are mounted as the computer's M-drive, and the FieldTrip code + necessary data are located in M:\toolkit2022. If you start MATLAB from the Desktop shortcut, FieldTrip will be automatically added to the MATLAB path, and you will be taken to the directory that contains the course data. 

{% include markup/red %}
Please do not use another MATLAB version than 2021b. It should be available on all hands-on computers.
{% include markup/end %}

A recent copy of FieldTrip and the data have been preinstalled on the computer and you do not have to download anything. Also, it should NOT be necessary to execute the following lines of code. These are only needed if you DO NOT start the MATLAB from the Desktop shortcut. In other words, you will probably always want to start MATLAB from the Desktop shortcut.

    restoredefaultpath
    cd M:\toolkit2022
    startup

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The addpath statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `startup` command runs the startup.m file in the toolkit2022, which ensures that all required subdirectories are added to the path.

{% include markup/red %}
In general, please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Furthermore, please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/installation).
{% include markup/end %}


## Code of conduct

Please spend a couple of minutes to have a look at our [Code of Conduct](/workshop/toolkit2022/code_of_conduct) to make sure we all are taking responsibility to look after each other and make sure we are contributing towards an inclusive and supportive community. Please let us know if you have any questions regarding it. All toolkit participants are responsible to follow the rules listed here, as well as making sure that everyone in the toolkit follows it.
