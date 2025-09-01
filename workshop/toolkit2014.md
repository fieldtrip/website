---
title: Toolkit of Cognitive Neuroscience - EEG/MEG
---

- Where: Donders Institute, Radboud University Nijmegen
- When: 6-9 May 2014
- Who: Robert Oostenveld, Jan-Mathijs Schoffelen, et al.

## Installing FieldTrip and Tutorial preparation

For the hands-on sessions you have to start MATLAB. To ensure that everything runs smooth, we have prepareda clean and well-tested version of FieldTrip that is pre-installed on the hands-on computers. Importantly, you also do _not_ need to download the tutorial data, these are already available on your computer.

After starting MATLAB, please ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB). Type in the MATLAB command window

    which ft_defaults

If you see that ft_defaults is found by MATLAB, you are all set. Otherwise (e.g., if you are working on personal laptop on the last day), you will have to set the path to FieldTrip using

    restoredefaultpath
    cd path_to_directory/fieldtrip-xxxxxxxx
    addpath(pwd)
    ft_defaults

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed.
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you change into the tutorial directory

    cd d:/toolkit

## Program

A [PDF with the detailed program](https://download.fieldtriptoolbox.org/workshop/toolkit2014/program.pdf) is available. See below for the relevant tutorials for the hands-on sessions.

### Tuesday 6 May

- morning
  - 1h welcome and intro lecture
  - 1h data acquisition demo
- afternoon
  - 2h hands-on <https://www.fieldtriptoolbox.org/tutorial/eventrelatedaveraging>
  - 1h neuronal oscillations lecture
  - 1h wrap-up session
- evening
  - pub?

### Wednesday 7 May

- morning
  - 2h hands-on <https://www.fieldtriptoolbox.org/tutorial/timefrequencyanalysis>
  - 1h forward and inverse modeling lecture
- afternoon
  - 1h beamforming lecture
  - 2h hands on <https://www.fieldtriptoolbox.org/tutorial/beamformer>
  - 1h wrap-up session
- evening
  - dinner <http://goo.gl/maps/jwrEI>

### Thursday 8 May

- morning

  - 1h non-parametric permutation statistics lecture
  - 2h hands-on
    - <https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock>
    - <https://www.fieldtriptoolbox.org/tutorial/cluster_permutation_freq>

- afternoon
  - 1h connectivity lecture
  - 2h hands on <https://www.fieldtriptoolbox.org/tutorial/connectivity>
  - 1h wrap-up session

### Friday 9 May

- morning-afternoon
  - 5h playground (working on own data)
  - 1h testimonial & evaluation
