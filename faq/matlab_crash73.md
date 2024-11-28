---
title: MATLAB version 7.3 (2006b) crashes when I try to do ...
category: faq
tags: [matlab]
redirect_from:
    - /faq/matlab_version_7.3_2006b_crashes_when_i_try_to_do/
---

# MATLAB version 7.3 (2006b) crashes when I try to do ...

This may relate to a known bug in MATLAB 2006b with persistent variables. The bug relates to aggressive optimization of for-loops introduced in MATLAB 2006b, which is incompatible with persistent variables inside the for-loop. The progress indicator used in FieldTrip (i.e. the one that is dealing with the cfg.feedback options) is using a persistent variable so that it only updates the progress bar maximum ~100 times, instead of 10000 times (e.g., if you do a dipole scan for 10000 grid points).

You can determine whether this bug is actually the problem for MATLAB crashing by

    starting matlab
    cd fieldtrip-xxx/private
    progress('init')

If MATLAB crashes, then this is indeed the problem. You can try the following work around.

First try typing

    feature accel off

on the MATLAB command line and try reproducing the bug (see above). If that indeed solves it, I suggest that you add

    if strcmp(getfield(ver('MATLAB'), 'Version'), '7.3')
    feature accel off
    end

to your startup.m file.
