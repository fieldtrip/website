---
title: Installation and setting up the path
parent: MATLAB questions
category: faq
tags: [matlab, path, warning]
redirect_from:
  - /faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path/
---

# Installation and setting up the path

In general you should *not* add FieldTrip with all subdirectories to your path. In other words, don't use a command such as ```addpath(genpath(<path_to_fieldtrip>))```, nor use MATLAB's graphical user interface to set the path. There are a number of external toolboxes in `fieldtrip/external` that are irrelevant for most users, and even can cause some problems if they overlap with other (custom) toolboxes on your path. Furthermore, there are some functions for backward compatibility in `fieldtrip/compat`, which should *only* be added to your path in case you use the corresponding old MATLAB release.

## Step 0

As a preliminary, you may want to consider to restore the default MATLAB path. This is done by

    restoredefaultpath

This ensures that no trailing instances of potentially clashing functions are present on the path, including parts of the FieldTrip code that are shipped with other toolboxes such as SPM or EEGLAB.

## Step 1

Next, you should do

    addpath <path_to_fieldtrip>

where path_to_fieldtrip is the location where the FieldTrip directory is located. Inside the Donders Centre for Cognitive Neuroimaging (DCCN), this would be on Linux

    addpath /home/common/matlab/fieldtrip

and on Windows

    addpath H:\common\matlab\fieldtrip

whereas on your personal computer it might be

    addpath D:\fieldtrip-201900813

## Step 2

After adding the FieldTrip main path, you should execute the **[ft_defaults](/reference/ft_defaults)** function (formerly called fieldtripdefs.m), which sets the defaults and configures up the minimal required path settings.

    ft_defaults

If a subsequent FieldTrip function need an external toolbox that is present in fieldtrip/external, the **[ft_hastoolbox](//reference/utilities/ft_hastoolbox)** function will be called by the respective function and the path will be updated on the fly.

## Making it persistent

It is most convenient to have the addpath and **[ft_defaults](/reference/ft_defaults)** in a script with the name `startup.m`, which is located in your own MATLAB directory. See [this information from MathWorks](http://www.mathworks.com/access/helpdesk/help/techdoc/ref/startup.html).

## Avoid addpath(genpath(...))

Please be aware that you should *not* do

    addpath(genpath('/home/user/fieldtrip'))

because that will add many toolbox directories to your path that you won't use. Furthermore, it would cause some toolboxes to be on your path twice (such as SPM) and creates problems with builtin MATLAB functions for which FieldTrip has backward-compatibility replacements.

## Avoid using the graphical path setup tool

We recommend *not* to use the graphical path setup tool that MATLAB offers and especially not the "add with subdirectories" button. The graphical path setup tool often results in multiple versions of the same toolbox being on the path, or in outdated versions of a toolbox being on the path. It can even cause MathWorks own toolboxes to become messed up, for example by including the image processing toolbox of MATLAB version `xxx` to be added to the path of MATLAB `yyy` when you upgrade.

Instead we recommend to create a [startup.m](https://nl.mathworks.com/help/matlab/ref/startup.html) file and use that to explicitly manage the toolboxes and versions.

## Clean up your path

If you want to ensure that you have a totally clean version of the FieldTrip toolbox on your MATLAB path, please use [restoredefaultpath](https://nl.mathworks.com/help/matlab/ref/restoredefaultpath.htm) like this

    restoredefaultpath
    addpath <path_to_fieldtrip>
    ft_defaults

All dependencies will subsequently be added automatically as needed.

## How to deal with toolboxes that FieldTrip uses?

In case FieldTrip function needs additional functions (e.g., for reading a specific data format such as CTF, or for performing a specific computation such as runica), it uses the **[ft_hastoolbox](//reference/utilities/ft_hastoolbox)** helper function to determine whether a toolbox is present. If the toolbox is present on your path, it will not add it once more. If the toolbox "xxx" is not yet present, but the directory seems to be present in fieldtrip/external/xxx, then it will add that directory to your path.

The main FieldTrip functions such as **[ft_preprocessing](/reference/ft_preprocessing)** and **[ft_freqanalysis](/reference/ft_freqanalysis)** all call the **[ft_defaults](/reference/ft_defaults)** function at the beginning. The **[ft_defaults](/reference/ft_defaults)** function ensures that the required subdirectories such as fieldtrip/preproc and fieldtrip/fileio are added. All other toolboxes in fieldtrip/external will only be added upon request, i.e. only when a function from one of those toolboxes is really needed.

You might be worried that this automatic path-checking and path-adding on every function call makes it slow. The **[ft_hastoolbox](//reference/utilities/ft_hastoolbox)** function remembers (with a persistent variable) whether a certain toolbox has already been checked, and therefore does not check the same toolbox twice. In case FieldTrip folders are removed, for instance by using rmpath or restoredefaultpath, make sure to reset the persistent variable in the ft_hastoolbox function again by executing `clear ft_hastoolbox`.
