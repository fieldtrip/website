---
title: FieldTrip Workshop in Marseille in November 2016
---

# FieldTrip Workshop in Marseille in November 2016

Together with Jean-Michel Badier, Christian Benar ([MEG laboratory in Marseille](http://meg.univ-amu.fr/wiki/Main_Page)), and Marie-Laure Olive (Inserm - Trainings office), we will run a FieldTrip workshop.

- Who: Jan-Mathijs Schoffelen and Cristiano Micheli, with help from local staff
- When: 21-22 November 2016
- For whom: The number of places at this workshop is limited, and reserved for researchers associated with Inserm or CNRS. Inserm people can apply through [this link](https://www.sirene.inserm.fr). CNRS people need to fill in some paperwork. For more information, please contact: demat-form.dr-marseille@inserm.fr
- Also see [this link](http://meg.univ-amu.fr/images/Fiche_annonce_-_Connectivité_en_MEG_et_EEG_-_2016.pdf) for more information (in French).
- Where: GLM CNRS Joseph Aiguier - Marseille.

We will keep this page up to date and post new information here when available.

#### Monday November 21

- Session I

  - 09:30 – 09:45 Opening remarks
  - 09:45 - 10:45 Lecture: Connectivity basics, methods and issues. - [slides](/assets/pdf/workshop/marseille2016b_connectivity.pdf)
  - 10:45 – 11:00 Coffee break
  - 11:00 – 12:30 Hands-on: Analysis of sensor- and source-level connectivity
    - <https://www.fieldtriptoolbox.org/tutorial/connectivity>
    - <https://www.fieldtriptoolbox.org/tutorial/connectivityextended>
    - <https://www.fieldtriptoolbox.org/tutorial/coherence>
  - 12:30 – 13:30 Lunch

- Session II
  - 13:30 - 14:30 Lecture: Connectivity basics, issues and how-to's. - [slides](/assets/pdf/workshop/marseille2016b_connectivity2.pdf)
  - 14:30 – 14:45 Coffee break
  - 14:45 – 16:15 Hands-on: Analysis of source-level connectivity and networks
    - <https://www.fieldtriptoolbox.org/tutorial/networkanalysis>
  - 16:15 – 17:00 Wrap-up-the-day: “Ask the expert” session

#### Tuesday November 22

- Session III

  - 09:00 – 12:00 FieldTrip playground
  - 12:00 – 13:00 Lunch

- Session IV
  - 13:00 – 16:00 FieldTrip playground
  - 16:00 – 17:00 Wrap-up-the-day: “Ask the expert” session

## Tutorial preparation

To maximally benefit from this course, we expect the users to have basic knowledge of MATLAB and FieldTrip. To prepare for the hands-on sessions, you should watch the following online videos prior to the workshop. Note that these lectures are about one hour each, which means that you should **plan ahead and take your time** to go through them. It is your own responsibility to come well-prepared. Starting one day in advance will not cut it!

- [FieldTrip intro (video and hands-on)](/tutorial/introduction)
- [spectral analysis (video and hands-on)](/tutorial/timefrequencyanalysis)

## Getting started with the hands-on sessions

For the hands-on sessions you have to start MATLAB. To ensure that everything runs smooth, we will work with a clean and well-tested version of FieldTrip that we have installed on all computers and that we will bring on on a USB stick. Importantly, the tutorial data does not have to be downloaded but will also be distributed on the computers and available on the USB stick.

If you work on your own laptop:

1.  Copy the complete contents of the USB stick to your computer.
2.  Unzip the fieldtrip-xxxxxxxx.zip file.
3.  Put Subject01.zip in a directory called 'tutorial'.

{% include markup/red %}
Depending on the unzip program you are using (e.g., Winrar), the name of the zip file might also appear as directory, resulting in path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the FieldTrip directory in a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the MATLAB command window

    restoredefaultpath
    cd path_to_directory/fieldtrip-2016104
    addpath(pwd)
    ft_defaults

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/installation)).
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the
official MATLAB toolboxes. The `addpath(pwd)` statement adds the
present working directory, i.e. the directory containing the fieldtrip
main functions. The `ft_defaults` command ensures that all required
subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial
