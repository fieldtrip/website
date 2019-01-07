---
title: FieldTrip workshop Madrid
---

# FieldTrip workshop in Madrid

## Where

Facultad de Psicología, Universidad Autonoma de Madrid, Calle Iván Pavlov, 6, 28049 Madrid, Spain.

## When

Monday January 21st - Tuesday January 22nd.

## Who

The "Sociedad Española de Psicofisiología y Neurociencia Cognitiva y Afectiva" (SEPNECA) is the local organizer. Sophie Arana (Donders Institute, Nijmegen) and Diego Lozano-Soldevilla (CIBERER, Madrid; IDIBAPS, Barcelona) are the lecturers.

## PROGRAM


### Monday Jan 21st

- 09:30-10:00 	Registration, handouts and coffee

- 10:00-11:00	Introduction to MATLAB and the FieldTrip toolbox (Lecture) 

- 11:00-11:15	Coffee Break

- 11:15-12:45	Getting started with EEG data, quality checks and ERPs (Hands-on)

- 13:00-14:00 	Lunch

- 14:00-15:00	EEG acquisition, pre-processing, ICA, artifact rejection (Lecture)

- 15:00-15:15 	Tea Break 

- 15:30-17:30	    Cleaning and processing resting state EEG (Hands-on)

- 17:30-18:00 	Wrap-up-the-day: special topics, general questions and answers

### Tuesday Jan 22nd

- 10:00-11:00	Frequency and Time-frequency analysis (Lecture) 

- 11:00-11:15	Coffee Break

- 11:15-12:45	Frequency analysis of task and resting state EEG (Hands-on)

- 13:00-14:00 	Lunch

- 14:00-15:00	Cluster-based statistical testing of EEG data (Lecture)

- 15:00-15:15 	Tea Break 

- 15:30-17:30	    Cluster-based statistical testing on resting state EEG (Hands-on)

- 17:30-18:00 	Wrap-up-the-day and testimonial evaluation


## Installing FieldTrip and Tutorial preparation

For the hands-on sessions you have to start MATLAB. To ensure that
everything runs smooth, we will work with a clean and well-tested
version of FieldTrip that is distributed on a USB stick, rather than the version you might already
have installed. Furthermore, the tutorial data does not have to be
downloaded but will also be distributed on the USB stick.

1.  Copy the contents from the USB stick to your computer
2.  Unzip the fieldtrip-xxxxxxxx.zip file.
3.  Unzip the "data.zip" file, you should place the contents in the same directory, e.g. in a newly created directory called 'toolkit'.

{% include markup/danger %}
Depending on the unzip program you are using (e.g. Winrar), the name of the zip file might also appear as directiory, resulting in path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the FieldTrip directory in a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the MATLAB command window

    restoredefaultpath
    cd path_to_directory/fieldtrip-xxxxxxxx
    addpath(pwd)
    ft_defaults

{% include markup/danger %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using a startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, but only when needed.
{% include markup/end %}

The restoredefaultpath command clears your path, keeping only the
official MATLAB toolboxes. The addpath(pwd) statement adds the
present working directory, i.e. the directory containing the fieldtrip
main funcctions. The ft_defaults command ensures that all required
subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the data directory

    cd path_to_directory/data
