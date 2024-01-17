---
title: Converting an example NIRS dataset for sharing in BIDS
tags: [example, bids, sharing, nirs, artinis, homer, snirf]
---

# Converting an example NIRS dataset for sharing in BIDS

{% include markup/warning %}
NIRS is part of the [BIDS standard](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/11-near-infrared-spectroscopy.html) as of version 1.8.0 and uses the [SNIRF file format](https://github.com/fNIRS/snirf/blob/v1.1/snirf_specification.md).
{% include markup/end %}

## Artinis

Artinis is a company specialized in NIRS that is located close to Nijmegen, and hence at the Donders we regularly have shared projects with them. Artinis makes large laser-based, but also diode-based wearable NIRS systems.

The windows software that comes with the Arinis system is called "Oxysoft" and it writes data in the proprietary `.oxy3` or `.oxy4` formats. Although the file format is not open, FieldTrip has reading functions for it (as pre-compiled MATLAB code) in the `external/artinis` folder, which are automatically called by the normal reading functions and **[ft_preprocessing](/reference/ft_preprocessing)**. A peculiarity of the Artinis data format is that you always have to provide an extra file called `optodetemplates.xml` with the data. That XML file (used in Oxysoft) contains additional header information about the measurement setup, including the optode and channel configuration and template optode locations for display on screen.

### Example

The example here is based on the dataset that is also used in the tutorial on [preprocessing and averaging of multi-channel NIRS data](/tutorial/nirs_multichannel). The data was recorded in an auditory oddball task. Details can be found in the tutorial.

{% include markup/success %}
The raw data is available on our download server, together with the script to convert the data to BIDS and the resulting BIDS dataset. You can find all three [here](https://download.fieldtriptoolbox.org/example/bids_nirs/artinis/).
{% include markup/end %}

    % the Artinis oxy3 files come with an optodetemplates.xml file, this has to be in
    % the same directory as the oxy3 file and it cannot be a subdirectory
    % hence we have to change to the correct directory

    % if we don't change to the data directory, a graphical user interface dialog will pop up

    cd('original')

    %%

    % this data is from https://www.fieldtriptoolbox.org/tutorial/nirs_multichannel/

    filelist = {
      'LR-01-2015-06-01-0002.oxy3'
      'LR-02-2015-06-08-0001.oxy3'
      'LR-03-2015-06-15-0001.oxy3'
      'LR-04-2015-06-17-0001.oxy3'
      'LR-05-2015-06-23-0001.oxy3'
      };


    %%

    for i=1:length(filelist)
      filename = filelist{i};

      cfg = [];
      cfg.dataset = filename;
      cfg.method = 'convert';
      cfg.writejson = 'replace';
      cfg.writetsv = 'replace';

      % the following settings relate to the directory structure and file names
      cfg.bidsroot = '../bids'; % we are running this code in the "original" directory
      cfg.sub = filename([1 2 4 5]); % the first characters minus the "-"
      cfg.ses = [];
      cfg.run = [];
      cfg.task = 'auditoryoddball';
      cfg.datatype = 'nirs';

      % the following settings relate to the dataset_description.json
      cfg.dataset_description.Name                = '48-channel NIRS measured during auditory oddball task';
      cfg.dataset_description.Authors             = 'Marc van Wanrooij';
      cfg.dataset_description.ReferencesAndLinks  = {'https://www.fieldtriptoolbox.org/tutorial/nirs_multichannel/'}; % this can be a list
      cfg.dataset_description.BIDSVersion         = 'BEP030'; % this does not correspnd to an official version, but a BIDS Extension Proposal. See http://bids.neuroimaging.io/bep030

      data2bids(cfg)
    end

In the organization of the data to BIDS, the data is also converted to the SNIRF format. In the binary SNIRF format it is not specified what the channel names are, only which pair of sources/transmitters and detectors/receivers is being combined in each channel. Since SNIRF looks rather similar to the Homer format (see further down), the default nomenclature for SNIRF channels is `'Sx-Dx [wavelength]'` where `x` is a number. In the Artinis software it is slightly different and channels are called `'Rx-Tx [wavelength]'`.

For data that is in the BIDS format, FieldTrip version 20200911 or later uses the BIDS `.json` and `.tsv` sidecar files to overrule the header and event details. You can see that with the following code

    hdr1   = ft_read_header('../bids/sub-LR01/nirs/sub-LR01_task-auditoryoddball_nirs.snirf', 'readbids', true)
    event1 = ft_read_event('../bids/sub-LR01/nirs/sub-LR01_task-auditoryoddball_nirs.snirf', 'readbids', true)

which will return the channel names as `'Rx-Tx'` according to the Artinis standard, since that is represented in the `_channels.tsv` sidecar. By specifying the readbids option as false, you can skip the BIDS json and tsv and the channel names correspond to the SNIRF defaults, i.e., `'Sx-Dx'` rather than `'Rx-Tx'`.

    hdr2   = ft_read_header('../bids/sub-LR01/nirs/sub-LR01_task-auditoryoddball_nirs.snirf', 'readbids', false)
    event2 = ft_read_event('../bids/sub-LR01/nirs/sub-LR01_task-auditoryoddball_nirs.snirf', 'readbids', false)

## Homer

Homer is MATLAB-based software for the analysis of NIRS and is developed by researchers in the [lab](http://cbs.unix.fas.harvard.edu/science/core-facilities/neuroimaging/facilities/nirs-lab) of David Boas. If you have used Homer to import your data, you can use **[data2bids](/reference/data2bids)** to convert the `.nirs` files to SNIRF and to organize them according to BIDS.

### Example

For the example here we are using the dataset that is shared on Mendeley by Jessica Defenderfer and Aaron Buss in [fNIRS data files for event-related vocoding/background noise study](http://dx.doi.org/10.17632/4cjgvyg5p2.1). The same dataset is also used in [another example](/example/nirs_speech) script here on the website.

To convert the dataset from Homer `.nirs` format to BIDS and SNIRF, we use the following script. Since we do not have so much information about the actual dataset, we can only provide some general metadata. The original data is shared under the "CC BY 4.0 license", which allows redistribution of the data and derived data. This is also one of the fields in the required `dataset_description.json`.

{% include markup/success %}
The complete original dataset is available from Mendeley, a subset of the raw data has been made available on our download server, together with the script to convert the data to BIDS and the resulting BIDS dataset. You can find all three [here](https://download.fieldtriptoolbox.org/example/bids_nirs/homer/).
{% include markup/end %}

    % the original dataset includes data from 40 subjects
    % we are just using a subset here to demonstrate the principle

    filenames = {
      'S1001_run01.nirs'
      'S1003_run01.nirs'
      'S1004_run01.nirs'
      'S1005_run01.nirs'
      };

    %%

    for i=1:length(filenames)
      filename = filenames{i};

      cfg = [];
      cfg.dataset = fullfile('original', filename);
      cfg.method = 'convert';

      % the following settings relate to the directory structure and file names
      cfg.bidsroot = 'bids';
      cfg.sub = filename(1:5);
      cfg.ses = [];
      cfg.run = [];
      cfg.task = 'listenandrepeat';
      cfg.datatype = 'nirs';

      % the following settings relate to the dataset_description.json
      cfg.dataset_description.Name                = 'Defenderfer 2019; fNIRS data files for event-related vocoding/background noise study';
      cfg.dataset_description.Authors             = {'Defenderfer, Jessica', 'Buss, Aaron'};
      cfg.dataset_description.DatasetDOI          = 'http://dx.doi.org/10.17632/4cjgvyg5p2.1';
      cfg.dataset_description.License             = 'CC BY 4.0';
      cfg.dataset_description.ReferencesAndLinks  = {'https://www.fieldtriptoolbox.org/example/nirs_speech/'}; % this can be a list
      cfg.dataset_description.BIDSVersion         = 'BEP030'; % this does not correspnd to an official version, but a BIDS Extension Proposal. See http://bids.neuroimaging.io/bep030

      data2bids(cfg)
    end

## SNIRF

It can also be that you already have your data converted to the SNIRF format, but that the directory organization and the sidecar files with the metadata are not according to BIDS. In that case you can also use the **[data2bids](/reference/data2bids)** function.

### Example

In this example we will reuse the files that we have converted from Artinis format to SNIRF format in an earlier step. You can use **[data2bids](/reference/data2bids)** for that conversion, or **[ft_write_data](/reference/fileio/ft_write_data)**, but also Artinis' `oxysoft2matlab` toolbox.

The raw data is available on our download server, together with the script to convert the data to BIDS and the resulting BIDS dataset. You can find all three [here](https://download.fieldtriptoolbox.org/example/bids_nirs/snirf/).

    filelist = {
      'LR01_rawdata.snirf'
      'LR02_rawdata.snirf'
      'LR03_rawdata.snirf'
      'LR04_rawdata.snirf'
      'LR05_rawdata.snirf'
      };

    %%

    for i=1:numel(filelist)

      filename = filelist{i};

      cfg = [];
      cfg.dataset = fullfile('original', filename);
      cfg.method = 'copy';

      % the following settings relate to the directory structure and file names
      cfg.bidsroot = 'bids';
      cfg.sub = filename(1:4); % the first four characters
      cfg.ses = [];
      cfg.run = [];
      cfg.task = 'auditoryoddball';
      cfg.datatype = 'nirs';

      % the following settings relate to the dataset_description.json
      cfg.dataset_description.Name                = '48-channel NIRS measured during auditory oddball task';
      cfg.dataset_description.Authors             = 'Marc van Wanrooij';
      cfg.dataset_description.ReferencesAndLinks  = {'https://www.fieldtriptoolbox.org/tutorial/nirs_multichannel/'}; % this can be a list
      cfg.dataset_description.BIDSVersion         = 'BEP030'; % this does not correspnd to an official version, but a BIDS Extension Proposal. See http://bids.neuroimaging.io/bep030

      data2bids(cfg)

    end
