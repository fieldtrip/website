---
title: Advanced analysis and source modeling of EEG and MEG data
---

# Advanced analysis and source modeling of EEG and MEG data

On April 3-6, 2017 we will host the “Advanced MEG/EEG Tool-kit” at the Donders Institute in Nijmegen.

This intense 4-day toolkit course will teach you advanced MEG and EEG data analysis skills. Preprocessing, frequency analysis, source reconstruction, connectivity and various statistical methods will be covered. The toolkit will consist of a number of lectures, followed by hands-on sessions in which you will be tutored through the complete analysis of a MEG data, and there will also be plenty of opportunity to interact and ask questions to us about your research and data. On the final day you will have the opportunity to work on your own dataset under supervision of the tutors.

Organizers: Robert Oostenveld and Jan-Mathijs Schoffelen, with the help of many colleagues.

## Detailed Program

### Monday April 3, 2017

| 09:00-09:30 | Registration, handouts and coffee |  
| 09.30-09:45 | Welcome |  
| 09:45-10:45 | Introduction to EEG/MEG and introduction to the FieldTrip toolbox - [lecture](https://download.fieldtriptoolbox.org/workshop/toolkit2017/slides/introduction.pdf) |
| 10:45-11:00 | Coffee Break |  
| 11:00-12:00 | Data acquisition demonstration in the EEG and MEG labs |  
| 12:00-13:00 | Lunch |  
| 13:00-14:45 | Introduction to Event-Related Fields - [hands-on](/tutorial/eventrelatedaveraging) |  
| 14:45-15:15 | Tea Break |  
| 15:15-16:30 | Fundamentals of neuronal oscillations and synchrony - [lecture](https://download.fieldtriptoolbox.org/workshop/toolkit2017/slides/frequency_analysis.pdf) |
| 16:30-17:15 | Wrap-up-the-day: special topics, general questions and answers |

### Tuesday April 4, 2017

| 09:00-10:45 | Time-frequency analysis of power - [hands-on](/tutorial/timefrequencyanalysis) |  
| 10:45-11:00 | Coffee Break |  
| 11:00-12:15 | Forward and inverse modeling - [lecture](https://download.fieldtriptoolbox.org/workshop/toolkit2017/slides/forward_and_inverse.pdf) |
| 12:15-13:00 | Lunch |  
| 13:00-14:00 | Statistics using non-parametric randomization techniques - [lecture](https://download.fieldtriptoolbox.org/workshop/toolkit2017/slides/statistical_testing.pdf) |
| 14:00-15:00 | Statistics using non-parametric randomization techniques - [hands-on](/tutorial/cluster_permutation_timelock) |  
| 15:00-15:30 | Tea break |  
| 15:30-16:30 | Statistics using non-parametric randomization techniques - (continued) |  
| 16:30-17:15 | Wrap-up-the-day: special topics, general questions and answers |  
| 19:00-21:30 | Free DINNER - included in registration |

Mi Barrio
Fransestraat 58, Nijmegen
<http://mibarrio.nl>
[Google maps](https://www.google.nl/maps/dir/Mi+Barrio,+Fransestraat,+Nijmegen/Kapittelweg+29,+6525+EN+Nijmegen/@51.8321229,5.8524935,15z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x41701c8778dae51f/0xdc30bc96f7ed1418!2m2!1d5.860964!2d51.8383775!1m5!1m1!1s0x47c708f0ee77debd/0x2097068b19fc0afd!2m2!1d5.8633555!2d51.826093!3e2)

### Wednesday April 5, 2017

| 09:00-10:00 | Source reconstruction using beamformers - [lecture](https://download.fieldtriptoolbox.org/workshop/toolkit2017/slides/source_reconstruction.pdf) |
| 10:00-10:15 | Coffee Break |  
| 10:15-12:15 | Identifying oscillatory sources using beamformers - [hands-on](/tutorial/beamformer) |  
| 12:15-13:00 | Lunch |  
| 13:00-14:00 | Connectivity analysis of MEG and EEG data - [lecture](https://download.fieldtriptoolbox.org/workshop/toolkit2017/slides/connectivity_analysis.pdf) |
| 14:00-15:00 | Analysis of sensor- and source-level connectivity - [hands-on](/tutorial/connectivity) |  
| 15:00-15:30 | Tea Break |  
| 15:30-16:30 | Analysis of sensor- and source-level connectivity (continued) |  
| 16:30-17:15 | Wrap-up-the-day: special topics, general questions and answers |

### Thursday April 6, 2017

| 9:00-14:00 | FieldTrip playground, bring your own data! |
| 12:30-13:00 | Lunch |
| 13:00-14:00 | FieldTrip playground continued |
| 14:00-14:15 | Tea break |
| 14:15-15.00 | Testimonial & evaluation |

## Getting started with the hands-on sessions

For the hands-on sessions we will use MATLAB R2012b, which you can start from the Desktop shortcut. To ensure that everything runs smooth, we will work with a clean and well-tested version of FieldTrip that we have installed on all computers and that we will bring on on a USB stick. Importantly, the tutorial data does not have to be downloaded but will also be distributed on the computers and available on the USB stick.

{% include markup/red %}
Please do not use another MATLAB version than 2016b. It should be available on all hands-on computers.
{% include markup/end %}

A recent copy of FieldTrip and the data have been preinstalled on the computer and you do not have to download anything. Also, it should NOT be necessary to execute the following lines of code. These are only needed if you DO NOT start the MATLAB from the Desktop shortcut. In other words, you will probably always want to start MATLAB from the Desktop shortcut.

    restoredefaultpath
    cd D:\toolkit\fieldtrip
    addpath(pwd)
    ft_defaults

    cd D:\toolkit\data

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

{% include markup/red %}
In general, please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Furthermore, please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/installation)).
{% include markup/end %}
