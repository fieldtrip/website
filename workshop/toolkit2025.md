---
title: Advanced MEG/EEG toolkit at the Donders
tags: [toolkit2025]
---

# Advanced MEG/EEG toolkit at the Donders

From May 19-23 2025 we will host our annual MEG/EEG Tool-kit course in Nijmegen. During this 5-day toolkit course we will teach you advanced MEG and EEG data analysis skills. Pre-processing, frequency analysis, source reconstruction, analysis methods such as RSA and TRFs, and various statistical methods will be covered. Furthermore, we will give special attention to new opportunities in experimental design and measurements with Optically Pumped Magnetometer (OPM) systems and mobile EEG.

The toolkit consists of a number of lectures, followed by hands-on sessions in which you will be tutored through the analysis of a MEG data set using the FieldTrip toolbox. Furthermore, we will schedule time for you to work on your own data under supervision of experienced tutors.

There is a limited number of places available for this toolkit. The selection of participants will be based on the background experience, the research interest and the expectations on what you will learn. We prefer the group to be reasonably homogeneous in level and expertise of the participants, as this improves the overall interaction. Note that the course is specifically aimed at participants that already have designed and conducted their own experiment(s) and already have data that they can bring along for analysis. This means that first year PhD students, as well as master students, should consider taking the course at a somewhat later career stage.

You can now pre-register [here](https://www.ru.nl/en/donders-institute/services/donders-toolkits). The deadline for pre-registration is April 11, 2025. We will inform you as to whether you obtained a place in this course not later than April 22, 2025.

## Program

Note that the tentative program below still might change a bit.

### Monday May 19, 2025

| 09:00-09:30 | Registration and coffee |
| 09:30-10:00 | Welcome and personal introduction round |
| 10:00-11:00 | Introduction to EEG/MEG and introduction to the FieldTrip toolbox - [lecture](/assets/pdf/workshop/toolkit2025/02_introduction.pdf) by Robert Oostenveld |
| 11:00-11:15 | Coffee Break |
| 11:15-12:30 | EEG, MEG and OPM lab demonstrations |
| 12:30-13:30 | Lunch |
| 13:30-15:45 | Pre-processing - [hands-on](/tutorial/eventrelatedaveraging) |
| 15:45-16:00 | Tea Break |
| 16:00-17:30 | FieldTrip playground, apply your newly acquired knowledge and skills |

### Tuesday May 20, 2025

| 09:00-10:30 | Time frequency analysis of power - [lecture](/assets/pdf/workshop/toolkit2025/03_frequency.pdf) by Jan-Mathijs Schoffelen (NOTE: LOCATION=RED ROOM)|
| 10:30-10:45 | Coffee Break |
| 10:45-12:30 | Time-frequency analysis of power - [hands-on](/tutorial/timefrequencyanalysis) |
| 12:30-13:30 | Lunch |
| 13:30-14:30 | hands-on (continued) |
| 14:30-15:45 | Forward and inverse - [lecture](/assets/pdf/workshop/toolkit2025/04_forward_inverse.pdf) by Robert |
| 15:45-16:00 | Tea Break |
| 16:00-17:30 | FieldTrip playground, apply your newly acquired knowledge and skills |
| 18:30-22:00 | Drinks & dinner, eetbar [Mikmak](https://www.eetbarmikmak.nl), which is located [here](https://www.google.nl/maps/place/Kelfkensbos+45,+6511+TB+Nijmegen) |

### Wednesday May 21, 2025

| 09:00-09:30 | Morning chill or workout |
| 09:30-11:00 | Special interest [lecture](/assets/pdf/workshop/toolkit2025/05_infant_eeg.pdf): The beauty and the beast of developmental EEG  - lecture by Marlene Meyer |
| 11:00-11:15 | Coffee Break |
| 11:15-12:30 | Source reconstruction using beamformers - [lecture](/assets/pdf/workshop/toolkit2025/06_beamforming.pdf) by Britta Westner |
| 12:30-13:30 | Lunch |
| 13:30-15:45 | Beamforming - [hands-on](/tutorial/beamformer) |
| 15:45-16:00 | Tea Break |
| 16:00-17:30 | FieldTrip playground, apply your newly acquired knowledge and skills |

### Thursday May 22, 2025

| 09:00-09:30 | Morning chill or workout |
| 09:45-11:00 | New methods for experimental design and analysis - [lecture](/assets/pdf/workshop/toolkit2025/07_new_methods.pdf) by JM |
| 11:00-11:15 | Coffee Break |
| 11:15-12:30 | Statistics using non-parametric randomization techniques - [lecture](/assets/pdf/workshop/toolkit2025/08_statistics.pdf) by JM |
| 12:30-13:30 | Lunch |
| 13:30-15:45 | Statistics - [hands-on](/tutorial/cluster_permutation_timelock) |
| 15:45-16:00 | Tea Break |
| 16:00-17:30 | FieldTrip playground, apply your newly acquired knowledge and skills |

### Friday May 23, 2025

| 09:00-09:30 | Morning chill or workout |
| 09:45-11:00 | Open science and good practices - [lecture](/assets/pdf/workshop/toolkit2025/09_open_science.pdf) by Robert |
| 11:00-11:15 | Coffee Break |
| 11:15-12:30 | FieldTrip playground, apply your newly acquired knowledge and skills |
| 12:30-13:30 | Lunch |
| 13:30-15:45 | FieldTrip playground, apply your newly acquired knowledge and skills |
| 15:45-16:00 | Tea Break |
| 16:00-16:30 | Evaluation and testimonials |

## Practicalities

This will be an in-person event with no possibilities for hybrid or online attendance.

### Wifi access

If you need wifi access and you don't have a eduroam account through your institution, it is possible to get a visitor access. This needs to be renewed each day. Please follow the instructions on [this intranet page](https://intranet.donders.ru.nl/index.php?id=eva).

### Playground sessions: bring-your-own-data

A large part of the toolkit will consist of playground sessions, in which ideally you will be working on your own data. Please think a bit about what you want to achieve, and ensure that you have your data easily accessible (preferably, if possible on the laptop that you bring yourself, or on an external USB-drive). If you don't have data to work with, please let us know in time so that we can think about an alternative. We have plenty of tutorial data available, so this can be used to practice your data analysis skills.

### Test your installation in advance

For the hands-on sessions we assume that you will work on your own laptop computer. To have a smooth experience - and to avoid having to spend precious debugging time during the hands-on sessions - we recommend that you [test your MATLAB and FieldTrip installation in advance](/workshop/toolkit2025/test_installation), and download the data that we will need during the hands-on sessions. Before running this test, we recommend that you prepare your laptop as per the instructions in the next section, which explains in some more detail what needs to be downloaded in advance, as well as how you can easily obtain (and install) a copy of FieldTrip on your computer.

## Getting started with the hands-on sessions

For the hands-on sessions we assume that you have a computer with a relatively recent version of MATLAB installed (preferably < 5 years old, >= 2020a/b).

To ensure that everything runs smoothly, we recommend that you set up your computer with a clean and well-tested version of FieldTrip, and download the data that are needed for the hands-on sessions in advance.

{% include markup/red %}
You can either 'click around' using web browsers and/or explorer windows to grab the data that are needed, or instead (less work, at least if it works) execute the MATLAB code below.
{% include markup/end %}

To get a recent copy of FieldTrip, you can follow this [link](https://github.com/fieldtrip/fieldtrip/releases/tag/20250310), download the zip-file, and unzip it at a convenient location on your laptop's hard drive. Alternatively, you could do the following in the MATLAB command window. 

```
% create a folder that will contain the code and the data, and change directory
mkdir('toolkit2025');
cd('toolkit2025');

% download and unzip fieldtrip into the newly created folder
url_fieldtrip = 'https://github.com/fieldtrip/fieldtrip/archive/refs/tags/20250310.zip';
unzip(url_fieldtrip);
```

Upon completion of this step, the folder structure should look something like this: 

```bash
fieldtrip-20250310/
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
`-- utilities
```

{% include markup/red %}
If you have downloaded and unzipped by hand, it could be that there's an 'extra folder layer' in your directory structure. We recommend that you remove this extra layer, i.e. move all content one level up.
{% include markup/end %}

Next, we proceed with downloading the relevant data. The data that are used in the hands-on sessions, are stored on the FieldTrip [download server](https://download.fieldtriptoolbox.org/tutorial/). The tutorial documentation contains links to the relevant files, but it is easier to pre-install (and if needed to unzip) the data. To this end, you can use the recipe below. Please ensure that your present working directory is the ```toolkit2025``` folder, which you created in the previous step.

```
% create a folder (within toolkit2025) that will contain the data, to keep a clean structure
mkdir('data');
cd('data');

% then download and unzip the Subject01 dataset
url_subject01 = 'https://download.fieldtriptoolbox.org/tutorial/Subject01.zip';
unzip(url_subject01);

% next, create for each of the tutorials a folder, and download the data
mkdir('eventrelatedaveraging');
cd('eventrelatedaveraging');
url_tutorial = 'https://download.fieldtriptoolbox.org/tutorial/eventrelatedaveraging';
fnames = {'dataFC_LP.mat' 'dataFIC_LP.mat' 'dataIC_LP.mat'};
for k = 1:numel(fnames)
  websave(fnames{k}, fullfile(url_tutorial, fnames{k}));
end
cd('../');

mkdir('timefrequencyanalysis');
cd('timefrequencyanalysis');
url_tutorial = 'https://download.fieldtriptoolbox.org/tutorial/timefrequencyanalysis';
fnames = {'dataFIC.mat'};
for k = 1:numel(fnames)
  websave(fnames{k}, fullfile(url_tutorial, fnames{k}));
end
cd('../');

mkdir('beamformer');
cd('beamformer');
url_tutorial = 'https://download.fieldtriptoolbox.org/tutorial/beamformer';
fnames = {'Subject01.mri' 'dataPost.mat' 'dataPre.mat' 'data_all.mat' 'freqPost.mat' 'freqPre.mat' 'headmodel.mat' 'segmentedmri.mat' 'sourcePost_con.mat' 'sourcePost_nocon.mat' 'sourcePre_con.mat' 'sourcemodel.mat'};
for k = 1:numel(fnames)
  websave(fnames{k}, fullfile(url_tutorial, fnames{k}));
end
cd('../');

mkdir('cluster_permutation_timelock');
cd('cluster_permutation_timelock');
url_tutorial = 'https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock';
fnames = {'ERF_orig.mat' 'GA_ERF_orig.mat' 'dataFC_LP.mat' 'dataFIC_LP.mat' 'stat_ERF_axial_FICvsFC.mat' 'stat_ERF_planar_FICvsFC.mat'};
for k = 1:numel(fnames)
  websave(fnames{k}, fullfile(url_tutorial, fnames{k}));
end
cd('../../');
```
At this stage, you ideally have a directory structure that looks like the following one:
```bash
.
|-- data
|   |-- Subject01.ds
|   |-- beamformer
|   |-- cluster_permutation_timelock
|   |-- eventrelatedaveraging
|   `-- timefrequencyanalysis
`-- fieldtrip-20250310
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
    `-- utilities
```
So, if you from now on - that is for the duration of the toolkit - *ALWAYS* execute the following steps after starting a fresh MATLAB session, you should be all good to go:

```
% change into the 'toolkit2025' folder and then do the following
restoredefaultpath
addpath('fieldtrip-20250310');
addpath(genpath('data'));
ft_defaults;
```

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath` statement adds the `fieldtrip-20250310` directory, i.e. the directory containing the FieldTrip main functions. The other `addpath` statement tells MATLAB where to find the relevant data, and the `ft_defaults` command ensures that all of FieldTrip's required subdirectories are added to the path.

{% include markup/red %}
In general, please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using a startup.m file than the path GUI. You can find more information about startup files in the MATLAB documentation.

Furthermore, please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/installation).
{% include markup/end %}

## Code of conduct

Please spend a couple of minutes to have a look at our [Code of Conduct](/workshop/toolkit2025/code_of_conduct) to make sure we all are taking responsibility to look after each other and make sure we are contributing towards an inclusive and supportive community. Please let us know if you have any questions regarding it. All toolkit participants are responsible to follow the rules listed here, as well as making sure that everyone in the toolkit follows it.
