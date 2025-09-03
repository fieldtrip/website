---
title: FieldTrip Workshop in Marseille in January 2016
---

Together with Jean-Michel Badier and Christian Benar from the [MEG laboratory in Marseille](http://meg.univ-amu.fr/wiki/Main_Page), we will run a FieldTrip workshop.

- Who: Robert Oostenveld with help from local staff
- When: 11-13 January 2016
- Where: You should have received detailed instructions on the venue at INSERM Marseille. If you have questions, please contact demat-form.dr-marseille@inserm.fr.

We will keep this page up to date and post new information here when available.

## Dealing with the missing stats toolbox

Please download the ft_connectivitysimulation data from <https://download.fieldtriptoolbox.org/workshop/marseille/>.

## How should you prepare for the workshop?

{% include markup/yellow %}
In this workshop we will have a steep learning curve. We will move from basic preprocessing to channel and source-level connectivity. Given the limited amount of time, it is **important** that you come well prepared.
{% include markup/end %}

If you are not familiar with MATLAB or are not certain about your MATLAB skills, please go through the "MATLAB for psychologists" tutorial on <http://www.antoniahamilton.com/matlab.html>

Please read the [FieldTrip reference paper](http://www.hindawi.com/journals/cin/2011/156869/) to understand the toolbox design.

Furthermore, we recommend you to watch the following online videos prior to the workshop. Note that these video lectures cannot be quickly glanced over. You should **plan ahead and take your time** to go through them.

- [FieldTrip toolbox introduction, 1 hour](https://www.youtube.com/watch?v=eUVL_twWNdk)
- [MEG basics and instrumentation, 15 minutes](https://www.youtube.com/watch?v=CPj4jJACeIs)

The content of the shorter second lecture is also covered in the first, but presented differently and therefore possibly useful to get a good understanding of the signals that we deal with.

In the first workshop hands-on session we will start with preprocessing MEG data, but will not spend too much time on understanding how MATLAB works and how FieldTrip organizes the data. Therefore if you have never done any FieldTrip analysis in MATLAB before, you should read this [introduction tutorial](/tutorial/intro/introduction) and you should go through the [MEG preprocessing tutorial](/tutorial/sensor/eventrelatedaveraging). Depending on your understanding of MATLAB and MEG, you can **simply read** the preprocessing tutorial (which will take you 30 minutes) or download the example data and **go through it step by step** (which will take you 2 hours).

{% include markup/yellow %}
So over all there is about 2 to 5 hours of preparation required from you prior to the workshop!
{% include markup/end %}

## Program

_We will start each day at 9:00 sharp and will finish around 17:00 on Monday and Tuesday, and around 12:30 on Wednesday._

### Monday

- morning

  - 1h Lecture on frequency analysis - [slides](https://download.fieldtriptoolbox.org/workshop/marseille/slides/frequency.pdf)
  - 2h handson [Sensor-level ERF, TFR and connectivity analyses](/tutorial/sensor/sensor_analysis)

- afternoon

  - 1h Lecture on source reconstruction using beamforming - [slides](https://download.fieldtriptoolbox.org/workshop/marseille/slides/beamforming.pdf)
  - 2h handson [Localizing visual gamma and cortico-muscular coherence](/tutorial/source/beamformingextended)
  - wrap up of the day

- evening
  - dinner (not included, i.e. on own costs)

### Tuesday

- morning

  - 1h Lecture on connectivity analysis - [slides](https://download.fieldtriptoolbox.org/workshop/marseille/slides/connectivity.pdf)
  - 2h hands on [Analysis of sensor- and source-level connectivity](/tutorial/connectivity/connectivityextended)

- afternoon

  - 1h Lecture on nonparametric statistics using clustering - [slides](https://download.fieldtriptoolbox.org/workshop/marseille/slides/statistics.pdf)
  - 2h hands on [Cluster-based permutation tests on ERFs](/tutorial/stats/cluster_permutation_timelock) or on [Cluster-based permutation tests on time-frequency data](/tutorial/stats/cluster_permutation_freq)
  - wrap up of the day

- evening
  - pub (not included, i.e. on own costs)

### Wednesday

- Playground in which you will be working on own data (under supervision)
- Wrap up of the workshop

For the playground you should bring your own data. In case you don't have a suitable dataset for analysis (yet), we will provide you with a dataset and details on the experiment and analysis options.

## Setting the path

The data and FieldTrip have been installed on the computers at the workshop venue.

    cd /usr/local/fieldtrip-20151216/toolbox_FieldTrip/fieldtrip-20151216/
    ft_defaults
    cd ../../sensor_analysis/

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
    cd path_to_directory/fieldtrip-xxxxxxxx
    addpath(pwd)
    ft_defaults

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/matlab/installation)).
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial
