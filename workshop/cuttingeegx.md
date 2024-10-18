---
title: CuttingEEG X workshop at the Donders
tags: [cuttingeegx]
---

# CuttingEEG X workshop at the Donders

CuttingEEG is turning 10 years old! This milestone calls for a special edition, looking back at the EEG and MEG fields of the past 10 years and looking ahead at the next 10 years and beyond!

Alongside the [CuttingEEG X](https://cuttingeegx.org) conference we will be organizing some local workshops in the morning.

- Who: Konstantinos Tsilimparis, Robert Oostenveld
- When: 31 October 2024
- Where: Nijmegen
- See <https://cuttingeegx.org/registration/#Nijmegen> for more details

## The tutorial

We will run a tutorial on [preprocessing and coregistration of SQUID-based and OPM-based data](/workshop/cuttingeegx/squids_vs_opms). We will explore the differences in data analysis between the two systems. 

## Getting started with the hands-on session

In this workshop you will work on your own laptop computer. It will be an in-person event with no possibilities for hybrid or online attendance.

### Wifi access

If you need wifi access and you don't have a eduroam account through your institution, it is possible to get a visitor access. This needs to be renewed each day. Please follow the instructions on [this intranet page](https://intranet.donders.ru.nl/index.php?id=eva).

### MATLAB

For the hands-on sessions we assume that you have a computer with a relatively recent version of MATLAB installed (preferably < 5 years old, >= 2019a/b). 

### FieldTrip

To get the most recent copy of FieldTrip, you can follow this [link](https://github.com/fieldtrip/fieldtrip/releases/tag/20240916), download the zip-file, and unzip it at a convenient location on your laptop's hard drive. 

Alternatively, you could do the following in the MATLAB command window. 

```
% create a folder that will contain the code and the data, and change directory
mkdir('cuttingeegx');
cd('cuttingeegx');

% download and unzip fieldtrip into the newly created folder
url_fieldtrip = 'https://github.com/fieldtrip/fieldtrip/releases/tag/20240916.zip';
unzip(url_fieldtrip);
```

Upon completion of this step, the folder structure should look something like this: 

```bash
cuttingeegx/
|-- fieldtrip-20240916
    |-- bin
    |-- compat
    |-- connectivity
    |-- contrib
    |-- external
    |-- fileio
    |-- forward
    |-- inverse
    |-- plotting
    |-- preproc
    |-- private
    |-- qsub
    |-- realtime
    |-- specest
    |-- src
    |-- statfun
    |-- template
    |-- test
    |-- trialfun
    |-- utilities
```

{% include markup/red %}
If you have downloaded and unzipped by hand, it could be that there's an 'extra folder layer' in your directory structure. We recommend that you remove this extra layer, i.e. move all content one level up.
{% include markup/end %}

### Test your installation in advance

To have a smooth experience - and to avoid having to spend precious debugging time during the hands-on sessions - we recommend that you [test your MATLAB and FieldTrip installation in advance](/workshop/toolkit2024/test_installation).

## The data used in this tutorial

Next, we proceed with downloading the relevant data. The data that are used in the hands-on sessions, are stored on the FieldTrip [download-server](https://download.fieldtriptoolbox.org/workshop/cuttingeegx). You can either ‘click around’ using web browsers and/or explorer windows to grab the data that are needed, or instead (less work, at least if it works) execute the MATLAB code below.

Please ensure that your present working directory is the ```cuttingeegx``` folder, which you created in the previous step.

```
% create a folder (within cuttingeegx) that will contain the data, to keep a clean structure
mkdir('data');
cd('data');

% create a folder and download the SQUID and OPM dataset
url_tutorial = 'https://download.fieldtriptoolbox.org/workshop/cuttingeegx';
fnames = {''};
for k = 1:numel(fnames)
  websave(fnames{k}, fullfile(url_tutorial, fnames{k}));
end
cd('../');
```

At this stage, you ideally have a directory structure that looks like the following one:

```bash
cuttingeegx/
|-- data
    |-- opm
    |-- squid
    |-- mri
|-- fieldtrip-20240916
    |-- bin
    |-- compat
    |-- connectivity
    |-- contrib
    |-- external
    |-- fileio
    |-- forward
    |-- inverse
    |-- plotting
    |-- preproc
    |-- private
    |-- qsub
    |-- realtime
    |-- specest
    |-- src
    |-- statfun
    |-- template
    |-- test
    |-- trialfun
    |-- utilities
```


Whenever starting a fresh MATLAB session, to configure the right FieldTrip paths, execute the following: 

```
% change into the 'cuttingeegx' folder and then do the following
restoredefaultpath
addpath('fieldtrip-20240417');
addpath(genpath('data'));
ft_defaults;
```

 `ft_defaults` command ensures that all of FieldTrip's required subdirectories are added to the path.

{% include markup/red %}
Furthermore, please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/installation).
{% include markup/end %}
