---
title: Preparing an EEG dataset for sharing
tags: [example, bids, sharing, anonymize]
---

# Preparing an EEG dataset for sharing

This example describes how to prepare an EEG dataset for sharing in the BIDS format. The example starts from a single publicly available EEG recording of a single subject, which is copied multiple times to simulate a dataset comprising data from ten subjects.

On this page you can find two versions of the preparation of a BIDS EEG dataset. The first version copies the existing data without changing its format, since the format is BIDS compliant. The second version also converts the data to (another) BIDS-compliant data format, which is what you would do in case your original data is in a format that is not directly supported by BIDS.

{% include markup/warning %}
If you want to share data, there are multiple things to consider. For example the file format of the data, the access mechanism for the data (ftp/http/sftp), the data use agreement, whether all data or some part of the data is shared, using pseudonyms in the description of the data, scrubbing the date and time of recording, removing identifying features from the data, etc.

In this example we will only be dealing with the format in which the data is organized (over directories) and stored (in files), for which we use the [Brain Imaging Data Structure](http://bids.neuroimaging.io).
{% include markup/end %}

Prior to conversion the data comprises 10 files (one file per subject). After conversion there are 52 or 72 files (for the two options described below), which includes the sidecar files with metadata.

The procedure for converting the original data consists of a number of steps:

1.  Create empty directory structure according to BIDS
2.  Collect the EEG data
3.  Create the sidecar files for each dataset
4.  Create the general sidecar files
5.  Finalize

Step 1, 2 and step 4 are implemented using [Bash](<https://en.wikipedia.org/wiki/Bash_(Unix_shell)>) scripts. The construction of the sidecar files in step 3 is implemented using the **[data2bids](/reference/data2bids)** function that is part of FieldTrip. The final step is not automated, but consists of some manual work.

We will describe two alternative approaches: in the first one the files are kept in their original file format, in the second one the files are explicitly converted to the recommended format for BIDS.

After each of the automated steps the results should be checked. For that I have been using the command line applications like `find DIR -name PATTERN \| wc -l` to count the number of files, but also a graphical databrowser to check the directory structure and a text editor to check the content of the JSON and TSV sidecar files.

It is important that you use appropriate tools. Command line utilities are very handy, but also a good graphical (code) editor that allows you to navigate through the full directory structure and check the file content. I have been using the Atom editor with the network directory mounted on my desktop computer. There are good [alternatives](https://alternativeto.net/software/atom/).

## Organize EEG data as BIDS dataset - keep the files in the same format

### Step 1a: create empty directory structure

```bash
BIDSROOT=$HOME/example

mkdir -p $BIDSROOT/code
mkdir -p $BIDSROOT/stimuli
mkdir -p $BIDSROOT/sourcedata

for SUB in 01 02 03 04 05 06 07 08 09 10; do
mkdir -p $BIDSROOT/sub-$SUB/eeg
done
```

### Step 2a: copy the EEG data to the BIDS organization

The original data gets copied and renamed to the location in the BIDS structure. In reality we would of course copy the data of each individual subject, rather than copying the same data 10 times.

In this case it is not needed to convert the data, since the EEGLAB .set format is explicitly allowed according to the BIDS standard (although BrainVision and EDF are preferred).

```bash
BIDSROOT=$HOME/example
SOURCEDATA=$BIDSROOT/sourcedata

cd $SOURCEDATA
wget --no-check-certificate https://sccn.ucsd.edu/mediawiki/images/9/9c/Eeglab_data.set

TASK=something

cp $SOURCEDATA/Eeglab_data.set $BIDSROOT/sub-01/eeg/sub-01_task-${TASK}_eeg.set
cp $SOURCEDATA/Eeglab_data.set $BIDSROOT/sub-02/eeg/sub-02_task-${TASK}_eeg.set
cp $SOURCEDATA/Eeglab_data.set $BIDSROOT/sub-03/eeg/sub-03_task-${TASK}_eeg.set
cp $SOURCEDATA/Eeglab_data.set $BIDSROOT/sub-04/eeg/sub-04_task-${TASK}_eeg.set
cp $SOURCEDATA/Eeglab_data.set $BIDSROOT/sub-05/eeg/sub-05_task-${TASK}_eeg.set
cp $SOURCEDATA/Eeglab_data.set $BIDSROOT/sub-06/eeg/sub-06_task-${TASK}_eeg.set
cp $SOURCEDATA/Eeglab_data.set $BIDSROOT/sub-07/eeg/sub-07_task-${TASK}_eeg.set
cp $SOURCEDATA/Eeglab_data.set $BIDSROOT/sub-08/eeg/sub-08_task-${TASK}_eeg.set
cp $SOURCEDATA/Eeglab_data.set $BIDSROOT/sub-09/eeg/sub-09_task-${TASK}_eeg.set
cp $SOURCEDATA/Eeglab_data.set $BIDSROOT/sub-10/eeg/sub-10_task-${TASK}_eeg.set
```

### Step 3a: use MATLAB to create the sidecar files for each subject

The **[data2bids](/reference/data2bids)** function will read each EEG recording and determine the metadata that is available in the file, such as the channel names, sampling frequency, etc. There is also information about the data that is not available in the file, which you have to specify in the configuration structure. It is also possible to overrule information that is incorrect/incomplete in the data file and to ensure that the correct metadata appears in the sidecar files.

    %% this is an example that starts with data in a supported format

    bidsroot = fullfile(getenv('HOME'), 'example');
    subject  = dir(fullfile(bidsroot, 'sub-*'));
    subject  = {subject.name};

    for i=1:numel(subject)

    anat = dir(fullfile(bidsroot, subject{i}, 'anat', '*.nii'));
    func = dir(fullfile(bidsroot, subject{i}, 'func', '*.nii'));
    dwi  = dir(fullfile(bidsroot, subject{i}, 'dwi',  '*.nii'));
    meg  = dir(fullfile(bidsroot, subject{i}, 'meg',  '*.ds'));
    eeg  = dir(fullfile(bidsroot, subject{i}, 'eeg',  '*.set'));

    catfile = @(p, f) fullfile(p, f);

    anat = cellfun(catfile, {anat.folder}, {anat.name}, 'UniformOutput', 0);
    func = cellfun(catfile, {func.folder}, {func.name}, 'UniformOutput', 0);
    dwi  = cellfun(catfile, {dwi.folder},  {dwi.name},  'UniformOutput', 0);
    meg  = cellfun(catfile, {meg.folder},  {meg.name},  'UniformOutput', 0);
    eeg  = cellfun(catfile, {eeg.folder},  {eeg.name},  'UniformOutput', 0);

    dataset = cat(1, anat(:), func(:), dwi(:), meg(:), eeg(:));

    for j=1:numel(dataset)
      cfg = [];
      cfg.dataset                     = dataset{j};

      cfg.eeg.writesidecar            = 'replace';
      cfg.channels.writesidecar       = 'replace';
      cfg.events.writesidecar         = 'replace';

      cfg.InstitutionName             = 'University of California San Diego';
      cfg.InstitutionalDepartmentName = 'Schwartz Center for Computational Neuroscience';
      cfg.InstitutionAddress          = '9500 Gilman Drive # 0559; La Jolla CA 92093, USA';

      % provide the long rescription of the task
      cfg.TaskName = 'Subjects were doing something.';

      % these are EEG specific
      cfg.eeg.PowerLineFrequency      = 60;  % recorded in the USA
      cfg.eeg.EEGReference            ='M1'; % actually I do not know, but let's assume it was left mastoid

      data2bids(cfg)

    end % for each dataset
    end % for each subject

### Step 4a: use Python to create the general sidecar files

This step is again done on the Linux command line, using some tools that are shared [here](https://github.com/robertoostenveld/bids-tools). Some of the other tools might be useful in creating scripts to gather and/or reorganize your EEG, MEG, Presentation or DICOM data.

```bash
BIDSROOT=$HOME/example
BIDSTOOLS=$HOME/bids-tools/bin

$BIDSTOOLS/create_sidecar_files  -f --description  $BIDSROOT # create the dataset_description.json file
$BIDSTOOLS/create_sidecar_files  -f --participants $BIDSROOT # create the participants.tsv file
$BIDSTOOLS/create_sidecar_files  -f --scans        $BIDSROOT # create the scans.tsv files (per subject and session)
```

### Step 5a: finalize

There are some things which are not implemented as a script, for example filling out the details in the top-level _dataset_description.json_ file, adding a _README_ file, updating the _CHANGES_ file.

I also manually renamed the subdirectories with the presentation log files in the _sourcedata_ directory, and added the presentation source code and stimulus material in the _stimuli_ directory.

Throughout the development of the scripts and and after having completed the conversion I used the [bids-validator](http://github.com/INCF/bids-validator/) to check compliance with BIDS.

## Organize EEG data as BIDS dataset - converting the files along the way

### Step 1b: create empty directory structure

```bash
BIDSROOT=$HOME/example

mkdir -p $BIDSROOT/code
mkdir -p $BIDSROOT/stimuli
mkdir -p $BIDSROOT/sourcedata

for SUB in 01 02 03 04 05 06 07 08 09 10; do
mkdir -p $BIDSROOT/sub-$SUB/eeg
done
```

### Step 2b: copy the EEG data for all participants

Here I am copying the single example file to each of the subjects. This would normally not be needed, since you would already have the original data somewhere in some structure. The original format data can be shared in BIDS in the _sourcedata_ directory.

```bash
BIDSROOT=$HOME/example
SOURCEDATA=$BIDSROOT/sourcedata

cd $SOURCEDATA
wget --no-check-certificate https://sccn.ucsd.edu/mediawiki/images/9/9c/Eeglab_data.set

cp $SOURCEDATA/Eeglab_data.set $SOURCEDATA/participant01.set
cp $SOURCEDATA/Eeglab_data.set $SOURCEDATA/participant02.set
cp $SOURCEDATA/Eeglab_data.set $SOURCEDATA/participant03.set
cp $SOURCEDATA/Eeglab_data.set $SOURCEDATA/participant04.set
cp $SOURCEDATA/Eeglab_data.set $SOURCEDATA/participant05.set
cp $SOURCEDATA/Eeglab_data.set $SOURCEDATA/participant06.set
cp $SOURCEDATA/Eeglab_data.set $SOURCEDATA/participant07.set
cp $SOURCEDATA/Eeglab_data.set $SOURCEDATA/participant08.set
cp $SOURCEDATA/Eeglab_data.set $SOURCEDATA/participant09.set
cp $SOURCEDATA/Eeglab_data.set $SOURCEDATA/participant10.set
rm $SOURCEDATA/Eeglab_data.set
```

### Step 3b: use MATLAB to convert the data and to create sidecar files for each subject

The **[data2bids](/reference/data2bids)** function will get the metadata that is available from the original file, such as the channel names, sampling frequency, etc. There is also information about the data that is not available in the file, which you have to specify in the configuration structure. It is also possible to overrule information that is incorrect/incomplete in the data file and to ensure that the correct metadata appears in the sidecar files.

Besides creating the sidecar files with the metadata, in this step we are also converting the data from EEGLAB .set format into BrainVision format. This is (along with EDF) the preferred format for EEG data in BIDS, since it is widely supported by many EEG analysis software packages.

In principle converting the data is not needed, since EEGLAB .set is also one of the (non-preferred) formats allowed for EEG data in BIDS.

    %% this is an example that converts the EEG data to BrainVision format

    bidsroot   = fullfile(getenv('HOME'), 'example');
    sourcedata = fullfile(bidsroot, 'sourcedata');

    dataset = {
    fullfile(sourcedata, 'participant01.set')
    fullfile(sourcedata, 'participant02.set')
    fullfile(sourcedata, 'participant03.set')
    fullfile(sourcedata, 'participant04.set')
    fullfile(sourcedata, 'participant05.set')
    fullfile(sourcedata, 'participant06.set')
    fullfile(sourcedata, 'participant07.set')
    fullfile(sourcedata, 'participant08.set')
    fullfile(sourcedata, 'participant09.set')
    fullfile(sourcedata, 'participant10.set')
    };

    nsubj = 10;
    task = 'something';

    for i=1:nsubj

    cfg = [];
    cfg.dataset                     = dataset{i};
    cfg.outputfile                  = fullfile(bidsroot, sprintf('sub-%02d', i), 'eeg', sprintf('sub-%02d_task-%s_eeg.vhdr', i, task));

    cfg.eeg.writesidecar            = 'replace';
    cfg.channels.writesidecar       = 'replace';
    cfg.events.writesidecar         = 'replace';

    cfg.InstitutionName             = 'University of California San Diego';
    cfg.InstitutionalDepartmentName = 'Schwartz Center for Computational Neuroscience';
    cfg.InstitutionAddress          = '9500 Gilman Drive # 0559; La Jolla CA 92093, USA';

    % provide the long rescription of the task
    cfg.TaskName = 'Subjects were doing something.';

    % these are EEG specific
    cfg.eeg.PowerLineFrequency      = 60;  % recorded in the USA
    cfg.eeg.EEGReference            ='M1'; % actually I do not know, but let's assume it was left mastoid

    data2bids(cfg)

    end % for each dataset

### Step 4b: use Python to create the general sidecar files

This step is again done on the Linux command line, using some tools that are shared [here](https://github.com/robertoostenveld/bids-tools). Some of the other tools might be useful in creating scripts to gather and/or reorganize your EEG, MEG, Presentation or DICOM data.

```bash
BIDSROOT=$HOME/example
BIDSTOOLS=$HOME/bids-tools/bin

$BIDSTOOLS/create_sidecar_files  -f --description  $BIDSROOT # create the dataset_description.json file
$BIDSTOOLS/create_sidecar_files  -f --participants $BIDSROOT # create the participants.tsv file
$BIDSTOOLS/create_sidecar_files  -f --scans        $BIDSROOT # create the scans.tsv files (per subject and session)
```

### Step 5b: finalize

There are some things which are not implemented as a script, for example filling out the details in the top-level _dataset_description.json_ file, adding a _README_ file, updating the _CHANGES_ file.

I also manually renamed the subdirectories with the presentation log files in the _sourcedata_ directory, and added the presentation source code and stimulus material in the _stimuli_ directory.

Throughout the development of the scripts and and after having completed the conversion I used the [bids-validator](http://github.com/INCF/bids-validator/) to check compliance with BIDS.

## Concluding remarks

In this example it all looks very simple, which is partially because the data is not only more-or-less the same, but actually perfectly identical. Usually the challenge in organizing the data arise due to inconsistencies between the different recordings. Although the inconsistencies will not be part of the experimental protocol, stuff happens and not all lab recordings can be guaranteed to be exactly according to the same protocol. For example

- one subject was recorded with different acquisition settings
- one subject was recorded with another EEG cap
- for one subject some channels were swapped around
- for one subject the experiment was paused, resulting in two recording files
- for one subject the triggers were recorded incorrectly
- etc.

{% include markup/warning %}
As a rule of thumb: if you have few exceptions, better don't try to make the scripts above too complex, but deal with them manually. If you have many exceptions of the same or similar type, it is worthwhile to invest into making these scripts smarter to automate the exception handling.
{% include markup/end %}

In reusing the data, either by yourself, your (future) colleagues in your lab, or people outside your lab, this type of information is very relevant. Although it can be frustrating to encounter these inconsistencies when converting to BIDS, it actually reveals that these aspects need to be represented and documented properly in the (meta)data.
