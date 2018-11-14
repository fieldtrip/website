---
title: FieldTrip workshop in Madrid, Spain
layout: default
---

# FieldTrip workshop in Madrid, Spain

-   Who: Diego Soldevilla and Sophie Arana
-   When: January 2019
-   UAM
## Workshop Program

tba


## Installing FieldTrip and Tutorial preparation

For the hands-on sessions you have to start MATLAB. To ensure that
everything runs smooth, we will work with a clean and well-tested
version of fieldtrip that you can download [ here](https://www.dropbox.com/sh/4kvs5hvwkjqp07v/AAApX5HS-iilo5xvyH9y9IpTa?dl=0)). Importantly, the tutorial data does not have to be
downloaded but we strongly recommend to download before the workshop  at ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/fieldtrip-20160531.zip

1.  Copy the complete contents of the USB stick to your computer.
2.  Unzip the fieldtrip-20160531.zip file.
3.  Put all the data files in a directory called 'tutorial' (or something else you'll remember).

{% include markup/danger %}
Depending on the unzip program you are using (e.g. Winrar), the name of the zip file might also appear as directiory, resulting in path_to_directory/fieldtrip-20160531/fieldtrip-20160531, i.e. the fieldtrip directory in a fieldtrip directory. Please fix that by moving all files one level up.
{% include markup/end %}

After copying all files to your computer and unzipping then, you start MATLAB. To ensure that the right version of fieldtrip is used, and not another version (such as the one included in SPM or EEGLAB), you type in the MATLAB command window

    restoredefaultpath
    cd path_to_directory/fieldtrip-20160531
    addpath(pwd)
    ft_defaults

{% include markup/danger %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add fieldtrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed.
{% include markup/end %}

The restoredefaultpath command clears your path, keeping only the
official MATLAB toolboxes. The addpath(pwd) statement adds the
present working directory, i.e. the directory containing the fieldtrip
main functions. The ft_defaults command ensures that all required
subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing fieldtrip to your path, you change into the tutorial directory

    cd path_to_directory/tutorial
