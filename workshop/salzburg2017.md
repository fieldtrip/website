---
title: FieldTrip workshop in Salzburg, Austria
---

There will be a FieldTrip training event linked to the first [Salzburg Mind-Brain Annual Meeting](https://samba.ccns.sbg.ac.at).

- By whom: Robert Oostenveld and Jan-Mathijs Schoffelen
- When: 11-12 July 2017
- Where: Centre for Cognitive Neuroscience ([CCNS](https://ccns.sbg.ac.at/about/)) at the Paris Lodron University of Salzburg ([PLUS](https://www.uni-salzburg.at/)).
- Local organization: Nathan Weisz and Thomas Hartmann.

More details are provided by the local organizers [here](https://samba.ccns.sbg.ac.at/fieldtrip/).

## How should you prepare for the workshop?

{% include markup/yellow %}
In this workshop we will have a steep learning curve. We will move from basic preprocessing to channel and source-level connectivity. Given the limited amount of time, it is **important** that you come well prepared.
{% include markup/end %}

If you are not familiar with MATLAB or are not certain about your MATLAB skills, please go through the "MATLAB for psychologists" tutorial on <http://www.antoniahamilton.com/matlab.html>

Please read the [FieldTrip reference paper](http://www.hindawi.com/journals/cin/2011/156869/) to understand the toolbox design.

Furthermore, we recommend you to watch the [MEG basics and instrumentation video](https://www.youtube.com/watch?v=CPj4jJACeIs)prior to the workshop.

In the first workshop hands-on session we will start with preprocessing MEG data, but will not spend too much time on understanding how MATLAB works and how FieldTrip organizes the data. Therefore if you have never done any FieldTrip analysis in MATLAB before, you should read this [introduction tutorial](/tutorial/intro/introduction).

_We will start each day at 9:00 sharp and will finish around 17:30._

## Getting started with the hands-on sessions

For the hands-on sessions you have to start MATLAB. To ensure that everything runs smooth, we will work with a clean and well-tested version of FieldTrip that is already 'installed' on your computer.

To get going, you need to start MATLAB. Then, you need to issue the following command

    restoredefaultpath
    cd C:\FieldTrip_workshop\toolkit_salzburg\fieldtrip
    addpath(pwd)
    ft_defaults

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed.
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you need to change into the hands-on specific directory, containing the data that is necessary to run the specific hands-on session. These folders are located in C:\\FieldTrip_workshop\\toolkit_salzburg\\fieldtrip\\data.

### Tuesday

- morning

  - 1h welcome and intro lecture - [slides](https://download.fieldtriptoolbox.org/workshop/salzburg2017/slides/introduction.pdf)
  - 2h hands-on <https://www.fieldtriptoolbox.org/tutorial/eventrelatedaveraging>

- afternoon

  - 1h neuronal oscillations lecture - [slides](https://download.fieldtriptoolbox.org/workshop/salzburg2017/slides/frequency_analysis.pdf)
  - 2h hands-on <https://www.fieldtriptoolbox.org/tutorial/timefrequencyanalysis>
  - wrap up of the day

- evening
  - dinner and drinks + visit to Mozart Geburtshaus

### Wednesday

- morning

  - 1h forward and inverse modeling lecture - [slides](https://download.fieldtriptoolbox.org/workshop/salzburg2017/slides/source_reconstruction.pdf)
  - 2h hands on <https://www.fieldtriptoolbox.org/tutorial/beamformer>

- afternoon

  - 1h non-parametric permutation statistics lecture - [slides](https://download.fieldtriptoolbox.org/workshop/salzburg2017/slides/cluster_statistics.pdf)
  - 2h hands-on
    - <https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock>
    - <https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_freq>
  - wrap up of the day

- evening
  - drinks and dinner + visit to Mozart Wohnhaus, and if time permits visit to the Von Trapp family mansion.
