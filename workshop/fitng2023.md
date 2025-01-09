---
title: Interactive Virtual Workshop organized by the Fetal, Infant, & Toddler Neuroimaging Group
parent: FieldTrip courses and workshops
category: workshop
tags: [fitng2023]
---

# Interactive Virtual Workshop organized by the Fetal, Infant, & Toddler Neuroimaging Group

FIT’NG is hosting a 10-day virtual workshop series covering basic and advanced methods in developmental EEG/ERP.

-   Where: online
-   When: 20 February - 3 March, 2023
-   Organizers: Dr Lindsay Bowman and Dr Sam Wass
-   More information: <https://fitng.org/virtual-interactive-workshop/>

This workshop provides a much-needed space for developmental EEG/ERP researchers (including advanced users/PIs, novice users, and total beginners) to come together to discuss issues in methodological and analytic techniques uniquely relevant to developmental data (especially from infants, toddlers, and preschool children). The workshop will also showcase cutting edge approaches to using EEG/ERP data to address open questions in developmental research.

In all sessions we aim to:

-   Introduce the basic principles of the featured methodological approach
-   Showcase the methodological approach via examples of current research in the invited speaker’s lab or relevant data,
-   Identify current best practices in the application of the featured approach
-   Brainstorm approaches to determining best practices where they are currently lacking.

The full program can be found [here](https://fitng.org/wp-content/uploads/2023/01/WorkshopSchedule_1.pdf).

On Thursday 2 March Robert Oostenveld will present a lecture on statistical analyses of EEG, focusing on parametric versus non- parametric methods, a-priori analyses to estimate sample sizes and how (and why) to report effect sizes. This will be followed in the same session by a hands-on, with Jan-Mathijs Schoffelen, Marlene Meyer and James Ernest White as additional tutors.

## Preparation

### Downloading material in advance

Please download the most recent copy of the FieldTrip toolbox and the data that we will be using from our [download server](https://download.fieldtriptoolbox.org/workshop/fitng2023). The data is about 1GB, so please do plan downloading it in advance.

You should make a new directory `fitng_stats` or so, and unzip both the FieldTrip toolbox and the data in that directory. After unzipping, the result on your computer should look like this

    fitng_stats
         |-- data
         `-- fieldtrip-20230215

Please ensure that the data directory contains the `results` and the `scripts` folder, and that the `fieldtrip-20230215` directory contains a bunch of m-files by simply looking into these directories.

Depending on your unzip utility, you might end up with a directory inside a directory, that is not what you want! If your directories look like this

    fitng_stats
        |-- data
        |      `-- data
        `-- fieldtrip-20230215
               `-- fieldtrip-20230215

you should take the content of `data/data` and move it one directory up, and idem for `fieldtrip-20230215/fieldtrip-20230215`.

For reference, the raw data (not needed for this workshop) is available from <https://doi.org/10.34973/gvr3-6g88>, the code is also available from <https://github.com/Donders-Institute/infant-cluster-effectsize> and the processed data is also available from <https://doi.org/10.34973/g4we-5v66>. But right now you can get all that you need for the workshop from our [download server](https://download.fieldtriptoolbox.org/workshop/fitng2023).

### Setting up MATLAB

{% include markup/red %}
Please download and unzip the version of FieldTrip that is listed above and don't use the FieldTrip version that you might already have on your computer, for example as part of EEGLAB or SPM.
{% include markup/end %}

To get going, you need to start MATLAB. If you do not have MATLAB you could consider installing a [trial version](https://nl.mathworks.com/campaigns/products/trials.html?s_iid=htb_trial_gtwy_ar). Then, you need to issue the following commands:

    restoredefaultpath
    cd <your_fieldtrip_location>
    addpath(pwd)
    cd fieldtrip-20230215
    addpath(pwd)
    ft_defaults

The `<your_fieldtrip_location>` is the directory in which all the code is after you have unzipped the downloaded folder. So it is probably something like `/Users/roboos/Desktop/fitng_stats/fieldtrip-20230215` or the corresponding location on Windows.

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "Can't find the command ft_defaults" you should check that you are in the correct directory.

After this, you should do

    cd ../data/scripts
    addpath(pwd)

to add the scripts directory to your path. This should work if you have unzipped fieldtrip and the data in the correct locations. If you get the error "Unable to change current folder" then you have not unzipped correctly. Please check the previous section.

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the `startup.m` file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed. See also this [frequently asked question](/faq/installation).
{% include markup/end %}

Finally, you have to tell the scripts where all the (input and output) data is with

    cd ..       % this brings you to the top-level data directory
    scripts     = fullfile(pwd, 'scripts');
    bidsroot    = fullfile(pwd, 'bidsdata');
    results     = fullfile(pwd, 'results');
    derivatives = fullfile(pwd, 'bidsresults');

This creates a bunch of variables with the directories of all the parts. You can check that everything is set up properly with

    ls(scripts)

which should show a bunch of m-files, and

    ls(results)

which should show a list of directories for all participants. Each of the participant directories contains a number of mat-files with the already processed data. These form the starting point for the `do_group_analysis.m` script that we will be looking at today.

The `sourcedata` directory is **not** installed (and not shared) as that contained privacy sensitive information, such as the date of recording; it was used for `do_convert_data_to_BIDS.m`.

The `bidsroot` directory with the original raw data is **not** installed, but can be obtained from <https://doi.org/10.34973/gvr3-6g88> if you would want to look at the preprocessing, or want to analyze the data in another way.

### Check your macOS security settings

{% include markup/red %}
This section is relevant to macOS users only.
{% include markup/end %}

If you have a MacBook with a recent version of macOS, chances are that your security settings don't trust the mex files that are included with FieldTrip.

    cd ../fieldtrip-20230215/utilities/
    ft_getopt()  % without any options

If you get the error "ft_getopt.mexmaci64 cannot be opened because the developer cannot be verified" and "Invalid MEX-file", then please do **not** move it to the bin, but press "Cancel". In [this](/faq/mexmaci64_cannot_be_opened_because_the_developer_cannot_be_verified/) frequently asked question it is explained.

Start the macOS `Terminal.app` application to get a command line window and type

    sudo xattr -r -d com.apple.quarantine LOCATION_OF_FIELDTRIP

    sudo find LOCATION_OF_FIELDTRIP -name \*.mexmaci64 -exec spctl --add {} \;

where LOCATION_OF_FIELDTRIP should be replaced with the full path where your FieldTrip copy is installed - for me that is `/Users/roboos/Desktop/fitng_stats/fieldtrip-20230215`.

If you get the error "Error using ft_getopt, incorrect number of input arguments", then you are all set! That is actually the error we expect to get if we fail to specify any input arguments and it means that the mex file was executed properly. You can go back to the data directory with

    cd ../../data

## Hands-on instructions

During the hands-on we will look in detail at the [do_group_analysis](/workshop/fitng2023/do_group_analysis) script.
