---
title: MATLAB does not see the functions in the "private" directory
---

# MATLAB does not see the functions in the "private" directory

The functions in the fieldtrip/private directory are only available for functions that are located in fieldtrip. You cannot call them from the command line, and you cannot call them from functions (or scripts) that are located outside the FieldTrip directory.

See http://www.mathworks.nl/help/techdoc/matlab_prog/f4-70335.html for more general information.

The private directory provides a convenient way of separating the high-level functions that a normal user would call (i.e. the User Interface to the toolbox) and the low-level functions. However, if you are a "power user" and also want to directly call the low-level functions, you can do the followin

(on the unix command line, or using a Windows equivalent)

    cd /your/path/to/fieldtrip
    mv private ../fieldtrip_private

(on the MATLAB prompt)

    addpath /your/path/to/fieldtrip
    addpath /your/path/to/fieldtrip_private

If you are using FieldTrip within the F.C. Donders Centre, you can add the following two lines to your startup.m file.

    addpath /home/common/matlab/fieldtrip
    addpath /home/common/matlab/fieldtrip_private
