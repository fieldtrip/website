---
title: Advanced MEG/OPM toolkit at the Donders
tags: [toolkit2026]
---

From October 12-16 2026 we will host our annual MEG/OPM Tool-kit course in Nijmegen. This year will be the first time with a strong focus on OPMs. During the 5-day toolkit course we will teach you advanced MEG data analysis skills. Among others, pre-processing, source reconstruction and statistics will be covered. Furthermore, we will give special attention to new OPM-specific methods for denoising, coregistration and for custom helmet design.

The toolkit consists of a number of lectures, followed by hands-on sessions in which you will be tutored through the analysis of SQUID-MEG and OPM-MEG data using the FieldTrip toolbox. Furthermore, we will schedule time for you to work on your own MEG data under supervision of experienced tutors.

There is a limited number of places available for this toolkit. The selection of participants will be based on the background experience, the research interest and the expectations on what you will learn. We prefer the group to be reasonably homogeneous in level and expertise of the participants, as this improves the overall interaction. Note that we will **not cover EEG analysis** and that we will focus on MEG methods using both SQUID and OPM systems.  

You will soon be able to pre-register [here](https://www.ru.nl/en/donders-institute/services/donders-toolkits). The deadline for pre-registration is TBD. We will inform you as to whether you obtained a place in this course not later than TBD.

## Program

Note that the tentative program below still might change a bit.

### Monday October 12, 2026

| 09:00-09:30 | Registration and coffee |
| 09:30-10:00 | Welcome and personal introduction round |
| 10:00-11:00 | Introduction to MEG/OPM and introduction to the FieldTrip toolbox - lecture by Robert Oostenveld |
| 11:00-11:15 | Coffee Break |
| 11:15-12:30 | MEG and OPM lab demonstrations |
| 12:30-13:30 | Lunch |
| 13:30-15:45 | Pre-processing of MEG/OPM data - [hands-on](/tutorial/sensor/eventrelatedaveraging) and/or [hands-on](/tutorial/sensor/preprocessing_opm) |
| 15:45-16:00 | Tea Break |
| 16:00-17:30 | FieldTrip playground, apply your newly acquired knowledge and skills |

### Tuesday October 13, 2026

| 09:00-10:30 | Denoising of OPM-MEG data - lecture by Jan-Mathijs Schoffelen |
| 10:30-10:45 | Coffee Break |
| 10:45-12:30 | Denoising of OPM-MEG data - [hands-on](/tutorial/sensor/opm_denoising) |
| 12:30-13:30 | Lunch |
| 13:30-14:30 | hands-on (continued) |
| 14:30-15:45 | Coregistration of OPM-MEG data - lecture by Robert Oostenveld |
| 15:45-16:00 | Tea Break |
| 16:00-17:30 | OPM coregistration - [hands-on](/tutorial/source/coregistration_opm) |
| 18:30-22:00 | Drinks & dinner, TBA |

### Wednesday October 14, 2026

| 09:00-09:30 | Morning chill or workout |
| 09:30-11:00 | Special interest lecture - Developmental research using EEG and OPMs - lecture by Marlene Meyer |
| 11:00-11:15 | Coffee Break |
| 11:15-12:30 | Source reconstruction of MEG data - lecture by Robert Oostenveld |
| 12:30-13:30 | Lunch |
| 13:30-15:45 | Source reconstruction of MEG data - [hands-on](/tutorial/source/beamformer) |
| 15:45-16:00 | Tea Break |
| 16:00-17:30 | FieldTrip playground, apply your newly acquired knowledge and skills |

### Thursday October 15, 2026

| 09:00-09:30 | Morning chill or workout |
| 09:45-11:00 | Custom helmet design for OPM-MEG data - lecture by Robert Oostenveld |
| 11:00-11:15 | Coffee Break |
| 11:15-12:30 | OPM helmet design - [hands-on](/tutorial/sensor/opm_helmet_design) |
| 12:30-13:30 | Lunch |
| 13:30-14:30 | Statistics using non-parametric randomization techniques - lecture by Robert Oostenveld |
| 14:30-17:30 | Statistics of OPM-MEG data - [hands-on](/tutorial/stats/cluster_permutation_timelock) |

### Friday October 16, 2026

| 09:00-09:30 | Morning chill or workout |
| 09:45-11:00 | Open science and good practices - lecture by Robert Oostenveld |
| 11:00-11:15 | Coffee Break |
| 11:15-12:30 | FieldTrip playground, apply your newly acquired knowledge and skills |
| 12:30-13:30 | Lunch |
| 13:30-15:30 | FieldTrip playground, apply your newly acquired knowledge and skills |
| 15:30-15:45 | Tea Break |
| 15:45-16:00 | Evaluation and testimonials |

## Practicalities

This will be an in-person event with no possibilities for hybrid or online attendance.

### Wifi access

If you need wifi access and you don't have a eduroam account through your institution, it is possible to get a visitor access. We will organize this with you on-site.

### Playground sessions: bring-your-own-data

A large part of the toolkit will consist of playground sessions, in which ideally you will be working on your own MEG data. Please think a bit about what you want to achieve, and ensure that you have your data easily accessible (preferably, if possible on the laptop that you bring yourself, or on an external USB-drive). If you don't have data to work with, please let us know in time so that we can think about an alternative. We have plenty of tutorial data available, so this can be used to practice your data analysis skills.

### Test your installation in advance

For the hands-on sessions we assume that you will work on your own laptop computer. To have a smooth experience - and to avoid having to spend precious debugging time during the hands-on sessions - we recommend that you [test your MATLAB and FieldTrip installation in advance](/workshop/toolkit2026/test_installation), and download the data that we will need during the hands-on sessions. Before running this test, we recommend that you prepare your laptop as per the instructions in the next section, which explains in some more detail what needs to be downloaded in advance, as well as how you can easily obtain (and install) a copy of FieldTrip on your computer.

## Getting started with the hands-on sessions

For the hands-on sessions we assume that you have a computer with a relatively recent version of MATLAB installed (preferably < 5 years old, so R2021a or later).

To ensure that everything runs smoothly, we recommend that you set up your computer with a clean and well-tested version of FieldTrip, and download the data that are needed for the hands-on sessions in advance.

{% include markup/red %}
You can either 'click around' using web browsers and/or explorer windows to grab the data that are needed, or instead (less work, at least if it works) execute the MATLAB code below.
{% include markup/end %}

### Download and install FieldTrip

To get a recent copy of FieldTrip, you can follow this [link](https://github.com/fieldtrip/fieldtrip/releases/tag/20260901), download the zip-file, and unzip it at a convenient location on your laptop's hard drive. Alternatively, you could do the following in the MATLAB command window.

```matlab
% create a folder that will contain the code and the data, and change directory
mkdir('toolkit2026');
cd('toolkit2026');

% download and unzip fieldtrip into the newly created folder
url_fieldtrip = 'https://github.com/fieldtrip/fieldtrip/archive/refs/tags/20260901.zip';
unzip(url_fieldtrip);
```

Upon completion of this step, the folder structure should look something like this: 

```bash
fieldtrip-20260901/
|-- bin
|-- compat
|-- connectivity
|-- contrib
|-- external
|-- fileio
|-- forward
|-- inverse
|-- plotting
|-- preproc
|-- private
|-- qsub
|-- realtime
|-- specest
|-- src
|-- statfun
|-- template
|-- test
|-- trialfun
`-- utilities
```

{% include markup/red %}
If you have downloaded and unzipped by hand, it could be that there's an 'extra folder layer' in your directory structure. We recommend that you remove this extra layer, i.e. move all content one level up.
{% include markup/end %}

### Download and install the tutorial data

Next, we proceed with downloading the relevant data. The data that are used in the hands-on sessions, are stored on the FieldTrip [download server](https://download.fieldtriptoolbox.org/tutorial/). The tutorial documentation contains links to the relevant files, but it is easier to pre-install (and if needed to unzip) the data. To this end, you can use the recipe below. Please ensure that your present working directory is the `toolkit2026` folder, which you created in the previous step.

```matlab
% create a folder (within toolkit2026) that will contain the data, to keep a clean structure
mkdir('data');
cd('data');

% then download and unzip the Subject01 dataset
url_subject01 = 'https://download.fieldtriptoolbox.org/tutorial/Subject01.zip';
unzip(url_subject01);

%  the rest of the instructions will follow later  ...
```

At this stage, you ideally have a directory structure that looks like the following one:

```bash
.
|-- data
|   |-- Subject01.ds
|   |-- beamformer
|   |-- cluster_permutation_timelock
|   |-- opm_denoising
|   |-- coregistration_opm
|   `-- opm_helmet_design
`-- fieldtrip-20260901
    |-- bin
    |-- compat
    |-- connectivity
    |-- contrib
    |-- external
    |-- fileio
    |-- forward
    |-- inverse
    |-- plotting
    |-- preproc
    |-- private
    |-- qsub
    |-- realtime
    |-- specest
    |-- src
    |-- statfun
    |-- template
    |-- test
    |-- trialfun
    `-- utilities
```

### Set up MATLAB

If you from now on - that is for the duration of the toolkit - *ALWAYS* execute the following steps after starting a fresh MATLAB session, you should be all good to go:

```matlab
% change into the 'toolkit2026' folder and then do the following
restoredefaultpath
addpath('fieldtrip-20260901');
addpath(genpath('data'));
ft_defaults;
```

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath` statement adds the `fieldtrip-20260901` directory, i.e. the directory containing the FieldTrip main functions. The other `addpath` statement tells MATLAB where to find the relevant data, and the `ft_defaults` command ensures that all of FieldTrip's required subdirectories are added to the path.

{% include markup/red %}
In general, please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using a startup.m file than the path GUI. You can find more information about startup files in the MATLAB documentation.

Furthermore, please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/matlab/installation).
{% include markup/end %}

## Code of conduct

Please spend a couple of minutes to have a look at our [Code of Conduct](/workshop/toolkit2026/code_of_conduct) to make sure we all are taking responsibility to look after each other and make sure we are contributing towards an inclusive and supportive community. Please let us know if you have any questions regarding it. All toolkit participants are responsible to follow the rules listed here, as well as making sure that everyone in the toolkit follows it.
