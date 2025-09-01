---
title: FieldTrip workshop in Trento, Italy
---

## When and where

Monday 22 October - Wednesday 24 October 2012

<http://www.unitn.it/en/cimec>

The local organizers of the workshop are Nathan Weisz and Angelika Lingnau.

## Using the tutorial data and the FieldTrip version provided

For the hands-on sessions you have to start MATLAB. To ensure that everything runs smooth, we will work with a **clean and well-tested** version of FieldTrip that is distributed on the workstations and on a USB stick. You should **not** work with an old version you might already have installed in the past. Furthermore, the tutorial data **does not have to be downloaded** but will also be distributed on the workstations and on a USB stick.

If you work on your own laptop you need the USB stick:

1.  Copy the complete content from the USB stick to your computer
2.  Unzip the fieldtrip-xxxxxxxx.zip file.
3.  Unzip the Subject01.zip file, you should place the contents in the tutorial directory.

{% include markup/red %}
Depending on the unzip program you are using (e.g., Winrar), the name of the zip file might also appear as directory, resulting in path_to_directory/fieldtrip-xxxxxxxx/fieldtrip-xxxxxxxx, i.e. the FieldTrip directory in a FieldTrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of FieldTrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the **MATLAB command window**

    restoredefaultpath
    cd path_to_directory/fieldtrip-xxxxxxxx
    ls
    addpath(pwd)
    ft_defaults

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes.

The ls statement shows the list of files in the present directory, and you can visually check that the contents are correct and for example not in another subfolder. You should see a long list of ft_xxx.m functions.

The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, but only when needed.
{% include markup/end %}

After installing FieldTrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial

In general the tutorials start by reading the raw data from "Subject01.ds", which is a data directory. You should **not** go into the Subject01.ds directory, but stay at the level of the tutorial directory. If a specific tutorial instructs you to load data (and if you want the skip the step just prior to that because of time limitations), you should go into the tutorial data directory.

## Program

Each of the topics consists of a 1h lecture and a 2h hands-on session.

### Monday

- morning: [intro and ERFs](/tutorial/sensor/eventrelatedaveraging)
- afternoon: [time-frequency analysis](/tutorial/sensor/timefrequencyanalysis)

### Tuesday

- morning: [beamforming](/tutorial/source/beamformer)
- afternoon: [randomization stats](/tutorial/stats/cluster_permutation_timelock)

### Wednesday

- playground, analyzing your own data

## Trial function for TMS data

    function trl = trialfun_tms(cfg)

    % TRIALFUN_TMS does a flank detection on one of the EEG channels
    % in a combined EEG-TMS recording
    %
    % Required fields in the configuration ar
    %   cfg.dataset             = 'elli_test2_tms2.vhdr'
    %   cfg.trialdef.tmschannel = 'POz'
    %   cfg.trialdef.threshold  = -12000;
    %   cfg.trialdef.pre        = 0.3
    %   cfg.trialdef.post       = 0.7

    hdr = ft_read_header(cfg.dataset);
    indx = find(strcmp(hdr.label, cfg.trialdef.tmschannel));
    dat = ft_read_data(cfg.dataset, 'chanindx', indx);

    if cfg.trialdef.threshold<0
      trig = (dat<cfg.trialdef.threshold);
    elseif cfg.trialdef.threshold>0
      trig = (dat>cfg.trialdef.threshold);
    end

    % find the onset and offset of the thresholded signal
    trig = [diff(trig) 0];

    % the TMS pulse happens at the onset
    tms_sample = find(trig==1);

    trialbeg = tms_sample(:) - hdr.Fs*cfg.trialdef.pre;
    trialend = tms_sample(:) + hdr.Fs*cfg.trialdef.post;
    offset   = -hdr.Fs*cfg.trialdef.pre;

    trl = [trialbeg trialend];
    trl(:,3) = offset;
