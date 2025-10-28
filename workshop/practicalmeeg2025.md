---
title: PracticalMEEG workshop in Aix-en-Provence
tags: [practicalmeeg2025]
---

[PracticalMEEG](https://cuttingeeg.org/practicalmeeg2025/) offers an intensive three and a half day training program, featuring both plenary presentations of the theoretical concepts and immersive hands-on tutorials for four open-source packages: FieldTrip, EEGLAB, MNE-Python, and Brainstorm. Attendees will develop practical skills to create a complete MEEG analysis pipeline from preprocessing and source-level analysis to group-level statistics – based on exemplar or personal dataset using one or more of the four leading software packages.

## Where

The entire meeting will take place at the building named [Le Cube](https://www.univ-amu.fr/fr/public/le-cube-presentation) on the Aix-Marseille University – Schuman Campus. The address is [29 Av. Robert Schuman, 13100 Aix-en-Provence](https://maps.app.goo.gl/6vwBp5PGvkidT8gE6).

## When

Oct 28-31, 2025.

## Who

The FieldTrip hands-on tutorials will be presented and tutored by [Robert Oostenveld](https://www.ru.nl/en/people/oostenveld-r) and [Songyun Bai](https://www.ru.nl/en/people/bai-s) from the [Donders Institute for Brain, Cognition and Behaviour](https://www.ru.nl/en/donders-institute) in Nijmegen, the Netherlands.

Furthermore, we are glad with the trainEErs that help with the tutorials: Cristina Gil Ávila (Univ. Madrid, Spain), Paolo Canal (IUSS Pavia, Italy), and Judith Nicolas (CRNL, France).

There will also be other experts from MNE-Python, Brainstorm and EEGLAB with their respective tutorials, and jointly we will organize the plenary lectures.

## Hands-on program and training material

- [Preprocessing raw data and computing ERPs/ERFs](/workshop/practicalmeeg2025/handson_raw2erp)
- [Dealing with artifacts](/workshop/practicalmeeg2025/handson_artifacts)
- [Time-frequency analysis using Hanning window, multitapers and wavelets](/workshop/practicalmeeg2025/handson_sensoranalysis)
- [Creation of headmodels and sourcemodels for source reconstruction](/workshop/practicalmeeg2025/handson_anatomy)
- [Reconstructing source activity using beamformers](/workshop/practicalmeeg2025/handson_sourceanalysis)
- [Group-level statistics with parametric and non-parametric methods](/workshop/practicalmeeg2025/handson_groupanalysis)

## How to prepare

### Get an overview of FieldTrip

Please take a quick look at the [FieldTrip reference paper](https://doi.org/10.1155/2011/156869) if you have not done so already. If you have an hour or so, you can watch this [introductory lecture](https://www.youtube.com/watch?v=7B4rDZYwQLM). Note that more recorded lectures are available as [video](/video).

### Download and install a recent FieldTrip version

Please download the most recent version of the FieldTrip toolbox from [here](/download) or from [GitHub](https://github.com/fieldtrip/fieldtrip/tags). As we did some last minute bugfixes to make all tutorials run smoothly, you should have version [20250928](https://github.com/fieldtrip/fieldtrip/releases/tag/20250928) or later.

Please read [this FAQ](/faq/installation/) on how to set your path. After adding the FieldTrip main directory to your path, you should type `ft_defaults` which will add the required subdirectories (which depend on your MATLAB version). We recommend to put `ft_defaults` in your MATLAB [startup.m](https://nl.mathworks.com/help/matlab/ref/startup.html) file.

### Download and organize the scripts and data

We will use a small `datainfo_subject.m` function that specifies the input and output data files for each participant. You can download that along with some other scripts from the `code` folder on our [download server](https://download.fieldtriptoolbox.org/workshop/practicalmeeg2025/). Please organize the workshop data and code as follows:

```bash
/Volumes/SamsungT3/practicalmeeg2025/
├── code
│   ├── datainfo_subject.m
│   ├── atlas_subparc374_8k.mat
│   └── ...
└── ds000117-pruned
│   ├── CHANGES
│   ├── README
│   ├── dataset_description.json
│   ├── participants.tsv
│   ├── derivatives
│   ├── stimuli
│   ├── sub-01
│   ├── sub-02
│   └── ...
└── derivatives
    ├── raw2erp
    ├── sensoranalysis
    ├── anatomy
    ├── sourceanalysis
    └── groupanalysis
```

The `/Volumes/SamsungT3/practicalmeeg2025` directory is where I have the data on my laptop (actually on an external SSD), for you that would be somewhere else. There should be a code directory with (at least) the `datainfo_subject.m` function, there should be the `ds000117-pruned` directory with the raw data in subdirectories, and there should be a `derivatives` directory with one subdirectory per analysis step.

{% include markup/yellow %}
Since the whole dataset is too large, we provide a pruned version with only the MEG data of only a single subject. We have `pruned_sub-01` and `pruned_sub-15`, for subject 1 and 15.

Subject 1 is the one that is also analyzed by the other toolboxes (EEGLAB, Brainstorm, MNE-Python) at PracticalMEEG. Subject 15 is the one that was once upon a time selected as the "representative subject" for the SPM tutorial. The figures in the FieldTrip tutorials are based on subject 15, so we recommend that you download that.
{% include markup/end %}

The derivatives directory contains (or will contain) the results of the analysis, you can download some precomputed results as .mat files from our download server. For some steps that is not needed and you will compute them yourself, but for some lengthy analysis you will continue to work with the precomputed results that were saved by us.

### Download the raw data

You could download all data from [OpenNeuro](https://doi.org/10.18112/openneuro.ds000117.v1.0.5). However, that would be either a very large download, or you would have to install [datalad](https://www.datalad.org) to get the subset of the data used in this workshop. To make it easy for you, we provide a "pruned" version that only contains the subset of files needed.

You can download the pruned data as either the `pruned_sub-01` or `pruned_sub-15` folder on our [download server](https://download.fieldtriptoolbox.org/workshop/practicalmeeg2025/). Note that this is a WebDav server and you should use a WebDav client like [CyberDuck](https://cyberduck.io) or [FileZilla](https://filezilla-project.org). On Windows you can also [map it as a network drive](https://www.maketecheasier.com/map-webdav-drive-windows10/) and then drag the folders over to copy-and paste them to your own computer. It is important to maintain the BIDS folder structure!

Besides the raw data, we will also use some already processed data (as some computations take too long). Specifically, we have prepared and shared the headmodel and sourcemodel for the selected subject. Furthermore, we have processed all subjects up to and including to the source level, as that is what we will use for the group analysis. This processed data is available from the `derivatives` folder on our [download server](https://download.fieldtriptoolbox.org/workshop/practicalmeeg2025/). Please note that this is **not** the same as the derivatives that is contained within the BIDS ds000117-pruned data: that only contains the MaxFiltered data and the FreeSurfer output, not the FieldTrip-processed data.
