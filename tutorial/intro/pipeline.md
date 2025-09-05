---
title: Creating a clean analysis pipeline
weight: 30
category: tutorial
tags: [matlab, script]
redirect_from:
    - /tutorial/pipeline/
---

{% include markup/yellow %}
If you are completely new to FieldTrip, we recommend that you skip this tutorial for now. You can read the [introduction tutorial](/tutorial/introduction/) and then move on with the tutorials on [preprocessing](/tutorial/#reading-and-preprocessing-data). Once you get the hang of it, you can return to this tutorial on the technical aspects of coding.
{% include markup/end %}

## Introduction

This tutorial provides some guidelines and suggestions how to set up an analysis pipeline or chain of analysis steps that makes most efficient use of your (and your computer's) time and is in accordance to the FieldTrip philosophy. Some MATLAB basics regarding scripting and data handling are introduced, as well as the idea of batching.

The examples here are mainly about preprocessing of the data, but it does not provide detailed information about it. If you are interested in how to preprocess your data, you can check for example, [this](/tutorial/preproc/preprocessing) tutorial.

{% include markup/skyblue %}
The paper [Seven quick tips for analysis scripts in neuroimaging](https://doi.org/10.1371/journal.pcbi.1007358) by Marijn van Vliet (2020, Plos Comp Biol) provides very useful guidelines for writing and organizing your analysis code. Although the examples it provides are based on Python, the ideas it presents apply equally well to MATLAB.

{% include badge doi="10.1371/journal.pcbi.1007358" pmid="32214316" pmcid="PMC7098566" %}
{% include markup/end %}

## Background

The analysis of an experiment typically involves a lot of repetition, as similar analysis steps are taken for every condition and for every subject. Also, the same steps are often repeated with only slightly different settings (e.g., filters, timings). Because of this, we write scripts that call the corresponding FieldTrip functions. FieldTrip functions are **not** intended to be just typed into MATLAB's command window. If you do, you are guaranteed to lose record of preceding steps, repeat yourself unnecessarily, or unknowingly change settings between subjects or conditions.

Another '**no-no**' is the practice of collecting all your steps in a single large m-file and copy-pasting parts in the command window. Besides becoming easily cluttered with previous attempts, different filter settings, etc., it does not create a clear continuity between steps, and most importantly, does not permit batching. Batching is the ultimate aim of any analysis pipeline. It means that in the end most of your analysis steps can be repeated over all subjects and/or conditions with a single command, and that at the end of your analysis you have a set of scripts with all details that allows you to exactly replicate the analysis.

## Convert your data to BIDS

It is recommended to start your analysis by first [converting your data to BIDS](/example/other/bids). This pushes some of the challenging data curation and coding steps to the early phase of your analysis. It also requires that you identify and resolve inconsistencies at the start, rather than as you are going along. It comes at the expense of investing in data management and curation up-front, but it will save you time later, as the actual analysis becomes simpler.

Converting your data into BIDS early on also means practically that your data acquisition was not so long ago and you better remember the peculiarities of your subjects and the recordings.

If you incrementally bidsify your data immediately following the recording of each subject, you are furthermore more likely to notice potential issues in your experimental procedure, which you can improve for the subsequent subjects.

## Separating subject-specific details from the code

As stated before, by making our own scripts, we can in a later stage easily repeat them, e.g., over multiple subjects. It is common that every subject might have different and possibly slightly inconsistent filenames, different trials that have to be rejected, etc. A good idea, therefore, is to first **write all your subject-specific details in a separate m-file**. You can choose to have a single m-file per subject, like `Subject01.m`, `Subject02.m`, etcetera , or one in which you combine all subjects. In the current example we will use the first option, and we specify these m-files to be a [function](https://www.mathworks.com/help/matlab/ref/function.html):

    function [subjectinfo] = Subject01

    % This function returns the subject-specific details
    %
    % the first few lines with comments are displayed as help

    % define the filenames, parameters and other information that is subject specific
    subjectinfo.subjectid   = 'Subject01';
    subjectinfo.eegfilename = 'myProject/rawdata/EEG/subject01.eeg';
    subjectinfo.mrifilename = 'myProject/rawdata/MRI/01_mri.nii';
    subjectinfo.badtrials   = [1 3]; % subject made a mistake on the first and third trial

    % more information can be added to this script when needed
    ...

Save this as `Subject01.m` in a personal folder that you will need to add to the MATLAB path. Using the command line you can now simply retrieve this personal data by calling `Subject01` on the MATLAB command line or from any script by using `eval('Subject01')`. This will return the structure `subjectinfo` containing all the specified fields.

We can now use this in our own functions, giving flexibility in combining generic functions and subject-specific settings. In addition, you could use this file to add further notes, such as `% subject pressed the response button twice on the first trial`.

{% include markup/skyblue %}
An example that uses subject-specific m-files can be found [here](https://github.com/robertoostenveld/Wakeman-and-Henson-2015). The same dataset has later also been [converted to BIDS](https://doi.org/10.18112/openneuro.ds000117.v1.0.5) and a version of the analysis that starts from the BIDS dataset is documented [here](/workshop/practicalmeeg2022) and [here](https://download.fieldtriptoolbox.org/workshop/practicalmeeg2022/code).

A similar example is [this one](https://github.com/Donders-Institute/infant-cluster-effectsize), which also starts from a consistent [BIDS dataset](https://doi.org/10.34973/gvr3-6g88) (hence fewer exceptions needed) and which stores subject-specific details like the selected trials and the bad segments and channels in [mat-files](https://doi.org/10.34973/g4we-5v66) rather than m-files.
{% include markup/end %}

When the data is nicely curated and represented in [BIDS](/example/other/bids), including an enriched `events.tsv` file, the organization of the data is very predictable and the `participants.tsv` can be used to loop over subjects using [ft_read_tsv](/reference/fileio/ft_read_tsv) and the subject-specific `events.tsv` can be used with [ft_trialfun_bids](/reference/trialfun/ft_trialfun_bids). In this case you may choose not to use subject-specific m-files, but to store the lists of bad channels and segments to mat-files.

## Splitting the code over scripts

You construct your analysis pipeline by calling a sequence of FieldTrip functions from the command line or from your own scripts. Initially you are likely to start with a single script, but once that gets too large, you split it up into multiple scripts.

There are a number of analysis phases that you are likely to encounter and that you can represent over multiple scripts. For example, you can have the following scripts

    do_complete_analysis.m
    do_convert_data_to_bids.m
    do_prepare_layout.m
    do_prepare_neighbours.m
    do_singlesubject_analysis.m
    do_group_analysis.m

The `do_complete_analysis` script calls the others and could look like this

    % prepare the data in the BIDS organization
    do_convert_data_to_bids

    % prepare the layout for plotting and neighbours for interpolation and cluster-stats
    do_prepare_layout
    do_prepare_neighbours

    for i=1:20
      % load the subject-specific information
      eval(sprintf('Subject%02d', i))
      % do the analysis for the current subject
      do_single_subject_analysis
    end

    % do the group-level statistics
    do_group_analysis

In reality it is likely that you will not be executing `do_complete_analysis` like this all at once, because the construction of the BIDS conversion script and the general preparatory scripts for the [layout](/tutorial/plotting/layout) and [neighbours](/example/stats/neighbours) will take you some time and effort. While you are writing these, you are already trying them out and executing them piecewise to get everything right. However, the `do_complete_analysis` script does explain to others (and your future self) how to rerun the analysis.

The construction of the `do_singlesubject_analysis` will likely involve some trial-and-error and takes time, probably multiple days. While you are writing the single-subject analysis, you can repeatedly run a part of that script. Only once it is complete, you run the for-loop that executes it for all participants. If you are doing more sophisticated analyses, such as MEG or EEG source reconstruction, it makes sense to split `do_singlesubject_analysis` into multiple scripts: for example one for the anatomical processing, one for the channel-level processing, and one for the source reconstruction.

{% include markup/red %}
Do not save your own scripts inside the FieldTrip folder as it makes it harder to update your FieldTrip toolbox to a new version.

In general we recommend to keep your raw data, your code or scripts, and your results in three separate directories. See below for an example directory layout.
{% include markup/end %}

## Saving your results to disk

Saving intermediate or final results to disk is done with the [save](https://www.mathworks.com/help/matlab/ref/save.html) command. So you would call

    save('data_raw.mat', 'data_raw');

to save the output to `data_raw.mat` in the present working directory, i.e., the directory you are currently in. To determine the present working directory, you can use [pwd](https://www.mathworks.com/help/matlab/ref/pwd.html).

{% include markup/skyblue %}
We recommend in general storing a single FieldTrip data structure per file, and to give the file the same name as the data structure that it contains. This makes it more predictable what ends up in memory if you load the file. Furthermore, with a consistent naming scheme you can more easily delete files with intermediate results or outdated files.

A consequence of the one-variable-per-file strategy is that the files will have the same name for every subject, hence you need to store them in subject-specific directories.
{% include markup/end %}

Let's say you defined an output folder as in the first paragraph:

    subjectinfo.subjectid = 'Subject01';

you can program a generic solution to save all analysis steps of every subject in their own output folder:

    save([subjectinfo.subjectid filesep 'data_raw.mat'], 'data_raw');

In this way all your scripts (i.e., analysis steps) can read the input of the previous step and write their results as `.mat` files based upon the subject number.

{% include markup/skyblue %}
We recommend padding numbers in filenames and variables with zeros, so that they nicely align and are sorted consistently. Rather than '1, 2, 3, ..., 10, 11, 12', you are better off with '01, 02, 03, ..., 10, 11, 12'. One way to achieve this in your script is by using [sprintf](https://www.mathworks.com/help/matlab/ref/sprintf.html).

    outputdir = sprintf('Subject%02d', i);

where the `%02d` results in a zero-padded number of two digits long, which is useful if you have up to 99 subjects. With 100 subjects or more, you would use `%03d`.

Another useful MATLAB commands are [fullfile](https://www.mathworks.com/help/matlab/ref/fullfile.html) to construct a path, or [filesep](https://www.mathworks.com/help/matlab/ref/filesep.html) for the forward and backward slashes in the path, which are different between Windows (`/`) and Linux/macOS (`/`).

For example

    rawdatadir = '/Users/robert/myProject/rawdata'
    resultsdir = '/Users/robert/myProject/results'
    outputfile = fullfile(resultsdir, sprintf('Subject%02d', i), 'data_raw.mat')
    save(outputfile, 'data_raw')
{% include markup/end %}

Saving a single variable per file makes it possible to easily read only what is necessary. You can sort in the file manager on filename, as well as on creation date. The latter is convenient to quickly get an overview of the most recent files after you notice a bug in your analysis script 😁 and you have to rerun some analyses.

The file and folder organization on disk could then look something like this:

```bash
myProject/
├── code
│   ├── MyOwnFunction.m
│   ├── Subject01.m
│   ├── Subject02.m
│   ├── Subject03.m
│   └── Subject04.m
├── rawdata
│   ├── EEG
│   │   ├── subject01.eeg
│   │   ├── subject02.eeg
│   │   ├── subject03.eeg
│   │   └── subject04.eeg
│   └── MRI
│       ├── 01_mri.nii
│       └── 02_mri.nii
└── results
    ├── Subject01
    │   ├── avg_cond1.mat
    │   ├── avg_cond1_filtered.mat
    │   ├── avg_cond2.mat
    │   ├── avg_cond2_filtered.mat
    │   ├── avg_cond3.mat
    │   ├── avg_cond3_filtered.mat
    │   ├── rawdata.mat
    │   └── rawdata_filtered.mat
    ├── Subject02
    ├── Subject03
    └── Subject04
```

Along the way, you will most likely expand the subject-specific information. For instance, in the first step you may have used **[ft_databrowser](/reference/ft_databrowser)** to identify some unusual artifacts in a subject, which you could store in your subject-specific .m file:

    subjectinfo.artfctdef.visual.artifact = [
       160611  162906
       473717  492076
       604850  606076
       702196  703615
       736261  738205
       850361  852159
       887956  895200
       959974  972785
      1096344 1099772
     ];

## Batching

In the end we'll end up with a collection of several function calls that are organized inscripts, for example defining trials, preprocessing, artifact rejection, averaging. This could result in an analysis pipeline such as this (simplified) one:

{% include image src="/assets/img/tutorial/scripting/figure1.png" width="600" %}

Interactive or manual steps are often required for the the visual inspection and identification of artifacts, to identify artifactual ICA components, to localize electrodes in a 3D scan, to coregister the data with an MRI, and for quality control. Separating the interactive/manual steps from the non-interactive steps allows us to automate the non-interactive parts. This is called _batching_.

Large datasets often require quite some processing time, hence it is convenient to run a batch of analysis steps overnight. The worst that can happen is that the next morning you'll see some red lines in your MATLAB command window just because of a small mistake in one of the first subjects. Therefore, you might want to try using the [try-catch](https://www.mathworks.com/help/matlab/ref/try.html) syntax in MATLAB. Whenever something goes wrong between the `try` and `catch` it will jump to the catch after which it will simply continue. For example:

    for i=1:20
      try
        do_preprocessing_script
        % do_freqanalysis_script_v1
        do_freqanalysis_script_v2
        do_sourceanalysis_script
      catch
        disp(sprintf('Something went wrong with Subject %d', i));
      end
    end

The steps that do not require user interaction can even be executed in parallel to speed up the processing. This is explained in the [parfor](/tutorial/scripting/distributedcomputing_parfor) and [qsub](/tutorial/scripting/distributedcomputing_qsub) tutorials.

## Summary and suggested further reading

This tutorial explained how to write your own functions and how to do batching in order to increase the efficiency of your analysis. If you are interested in improving memory usage and the speed of your analysis, you can check [this](/tutorial/scripting/memory) and the tutorials on distributed computing using [qsub](/tutorial/scripting/distributedcomputing_qsub) and [parfor](/tutorial/scripting/distributedcomputing_parfor) tutorial.

When you have more questions about the topic of any tutorial, don't forget to check the [frequently asked questions](/faq) and the [example scripts](/example).

### See also these frequently asked questions

{% include seealso category="faq" tag1="matlab" %}

### See also these examples

{% include seealso category="example" tag1="matlab" %}
