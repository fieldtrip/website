---
title: Getting started with real-time head localization in MEG
tags: [realtime, meg]
category: getting_started
redirect_from:
    - /getting_started/realtime_headlocalizer/
---

Using FieldTrip it is possible to [monitor](/faq/experiment/headlocalizer) a subject's head position during a MEG recording session. This allows you as experimenter to reposition your subject within sessions, e.g., after each experimental block. It also allows you to reposition your subject at the start of a session to the same head position of a previous session.

{% include markup/yellow %}
Please cite this paper when you use the realtime head localizer in your research:

Stolk A, Todorovic A, Schoffelen JM, Oostenveld R. **[Online and offline tools for head movement compensation in MEG.](https://doi.org/10.1016/j.neuroimage.2012.11.047)** Neuroimage. 2013 Mar;68:39-48. doi: 10.1016/j.neuroimage.2012.11.047.
{% include markup/end %}

The following documentation describes how to set up the interface between the [CTF](/development/realtime/ctf) or [Neuromag](/development/realtime/neuromag) system and FieldTrip. The recommended implementation uses two separate computers, one for the acquisition (i.e. the one provided by CTF / Neuromag) and another one for the visualization towards the experimenter and the subject. The second computer can be the presentation computer that is commonly available, or another computer.

There are multiple reasons for running the visualization separate from the acquisition computer. First of all, we do not want to interrupt the acquisition or put load on that computer. Furthermore, it is more convenient to display the screen of a second (presentation) computer on the beamer to the subject (see below).

The CTF / Neuromag acquisition computer only runs a small program in the background (acq2ftx / neuromag2ft). Note that MATLAB does not need to be installed on the acquisition computer as this program is written in C-code and provided in compiled form. This program reads the data from the real-time interface (using shared memory) and makes the data available on a TCP/IP socket in a [buffer](/development/realtime/buffer).

The second (visualization / real-time analysis) computer runs MATLAB, reads the data over the network from the buffer and does the plotting using **[ft_realtime_headlocalizer](/reference/realtime/online_meg/ft_realtime_headlocalizer)**.

{% include image src="/assets/img/getting_started/realtime/headlocalizer/headloc_flowchart.png" width="600" %}

## Step by step description for the CTF acquisition computer

1. Download and unzip fieldtrip

2. Run in a Linux terminal:

   sudo echo 67596000 > /proc/sys/kernel/shmmax

This command increases the amount of shared memory that the software is allowed to use; the RHEL3 default of 32MB is not enough for the CTF software realtime interface. Note that you can restore the default setting with

    sudo echo 33554432 > /proc/sys/kernel/shmmax

or by rebooting the system. To make this change permanent, you can update the file /etc/sysctl.conf.

3. Run in a Linux terminal:

   \$HOME/fieldtrip/realtime/src/acquisition/ctf/acq2ftx

4. Start Acquisition. You should see some information being printed in the terminal that you used to start acq2ftx.

## Step by step description for the Neuromag acquisition computer

1. Download and unzip fieldtrip

2. Run in a Linux terminal:

   \$HOME/fieldtrip/realtime/src/acquisition/neuromag/neuromag2ft

3. Start Acquisition. You should see some information being printed in the terminal that you used to start neuromag2ftx.

## Step by step description for the visualization computer

1. Download and unzip fieldtrip

2. Start MATLAB and make sure the online_meg directory is added to path:

   addpath ~/fieldtrip
   addpath ~/fieldtrip/realtime/online_meg
   ft_defaults

3. Type in the MATLAB command window:

   cfg = [];
   cfg.dataset = 'buffer://hostname:1972';
   ft_realtime_headlocalizer(cfg)

The hostname address should points to the location where the buffer is run - i.e. the CTF / Neuromag acquisition computer. You should now see the real-time head location being visualized. You can also explore **[ft_realtime_signalviewer](/reference/realtime/example/ft_realtime_signalviewer)** or the other [realtime examples](/getting_started/realtime/bci).

## Practical issues and suggestions

It is recommended to install a 'vga switch' or 'video matrix' in the lab that can overwrite the signal from the stimulus presentation computer by that of the realtime visualization computer. This way the visualization can also be presented to the subject in the magnetically shielded room, allowing the subject to reposition himself/herself.

{% include image src="/assets/img/getting_started/realtime/headlocalizer/switch-box-hd15-2-way-bestlink.jpg" %}

For **Neuromag** systems, the real-time head localizer uses a rigidbody constraint to optimally dipole fit the real time positions of the head position indicator (HPI) coils, and thus of the subject's head. This means a hypothetical magnetic field distribution of all coils combined, is generated, based on their relative digitized positions. The actual positions and orientations of the coils making up this rigid body are then approximated by fitting the resulting hypothetical field distribution to the actually recorded magnetic field distribution. It is, thus, important that all coils are working optimally. This can be [checked offline](/faq/how_can_i_visualize_the_neuromag_head_position_indicator_coils?), using an already recorded dataset.

## See also

{% include seealso tag1="realtime" tag2="meg" %}
