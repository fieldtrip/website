---
title: PracticalMEEG workshop in Aix-en-Provence
tags: [practicalmeeg2022]
---

# PracticalMEEG workshop in Aix-en-Provence

PracticalMEEG aims at providing an intensive three–day training to MEG and EEG analysts. It will provide its attendees with the ability to create a full analysis pipeline with exemplar (or their own) data in one or several of four leading software dedicated to MEG and EEG analysis (Brainstorm, FieldTrip, EEGLAB, and MNE-python). On demand, we hope to provide attendees with the opportunity to bridge across toolboxes and weave their own complex multi-software pipeline. More details can be found [here](https://practicalmeeg2022.org).

## Where

The entire meeting will take place at the building named [Le Cube](https://www.univ-amu.fr/fr/public/le-cube-presentation) on the Aix-Marseille University – Schuman Campus. The address is 29 Av. Robert Schuman, 13100 Aix-en-Provence.

## When

Dec 14-16, 2022

## Who

Anne-Sophie Dubarry and Maximilien Chaumon are the local organizers.

The FieldTrip tutorials will be presented and tutored by [Robert Oostenveld](https://www.ru.nl/en/people/oostenveld-r) (from the Donders Institute for Brain, Cognition and Behaviour, Nijmegen, NL) and [Christelle Zielinski](https://www.lpl-aix.fr/contact/christelle-zielinski/) (from the Institute of Language, Communication and the Brain, Aix-en-Provence, FR).

There will also be other experts from MNE-Python, BrainStorm and EEGLAB with their respective tutorials, and jointly we will organize the plenary lectures.

# Hands-on program and training material

- [From raw to ERPs](/workshop/practicalmeeg2022/handson_raw2erp)
- [Time-frequency analysis using Hanning window, multitapers and wavelets](/workshop/practicalmeeg2022/handson_sensoranalysis)
- [Creation of headmodels and sourcemodels for source reconstruction](/workshop/practicalmeeg2022/handson_anatomy)
- [Reconstructing source activity using beamformers](/workshop/practicalmeeg2022/handson_sourceanalysis)
- [Group-level statistics with parametric and non-parametric methods](/workshop/practicalmeeg2022/handson_groupanalysis)
 
# How to prepare

## Get an overview of FieldTrip

Please take a quick look at the [FieldTrip reference paper](https://doi.org/10.1155/2011/156869) if you havenot done so already. If you have an hour or so, you can watch this [introductory lecture](https://www.youtube.com/watch?v=7B4rDZYwQLM). Note that more recorded lectures are available as [video](/video).

## Download and install a recent version

Please download the most recent version of the FieldTrip toolbox from [here](https://www.fieldtriptoolbox.org/download/) or from [GitHub](https://github.com/fieldtrip/fieldtrip/tags). As we did some last miniute bugfixes tomake all tutorials run smoothly, you should have version **20221207** or later.

Please read [this FAQ](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path/) on how toset your path. After adding the FieldTrip main directory to your path, you should type `ft_defaults` which will add the required subdirectories (which depend on your MATLAB version). We recommend to put `ft_defaults` in your MATLAB [startup.m](https://nl.mathworks.com/help/matlab/ref/startup.html) file.

## Download the data

You can get the data that we will work with from [Zenodo](https://doi.org/10.5281/zenodo.7405048) or on [OpenNeuro](https://doi.org/10.18112/openneuro.ds000117.v1.0.5). The Zenodo version is pruned and only contains the raw data files needed for this workshop. The OpenNeuro version contains all data (and hence is very large).

You can alternatively download the raw data from our [download server](https://download.fieldtriptoolbox.org/workshop/practicalmeeg2022/ds000117-pruned/). Note that this is a WebDav server and you should use a WebDav client like CyberDuck or FileZilla. On Windows you can also [map it as a network drive](https://www.maketecheasier.com/map-webdav-drive-windows10/). By using a WebDav client you can maintain the folder structure when downloading, which is important!

Besides the raw data, we will also use some already processed data (as some computations take too long). Specifically, we have prepared and shared the headmodel and sourcemodel for the selected subject. Furthermore, we have processed all subjects up to and including to the source level, as that is what we will use for the group analysis. This processed or so-called derivative data is also available from our [download server](https://download.fieldtriptoolbox.org/workshop/practicalmeeg2022/derivatives/). Please note that this is **not** the same as the derivatives contained within the BIDS raw data: that only contains the MaxFiltered data and the FreeSurfer output, not the FieldTrip-processed data.







 
