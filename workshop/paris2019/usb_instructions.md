---
title: Instructions for the USB stick
tags: [paris2019]
---

## The software

The USB stick contains a recent [release](https://github.com/fieldtrip/fieldtrip/releases) of the toolbox, called `fieldtrip-yyyymmdd.zip`. Please copy it to your computer and unzip it. Once FieldTrip is on your computer, the toolbox needs to be added to the MATLAB path. To achieve this, do the following:

- Change directory to the location of the FieldTrip package. Note the subfolders present.
- Add the FieldTrip folder to the path with

  addpath(pwd)

Note: **do not** add the folder recursively, i.e., do not use `addpath(genpath('path_to_fieldtrip'))`.

- Run 'ft_defaults' in MATLAB.
- Confirm that FT has been successfully added to your path, for example by typing 'which ft_preprocessing' in Matlab; the correct path should be displayed.

{% include markup/red %}
If you get any warnings about specific functions or SPM or EEGLAB being on your path multiple times, you should type

    restoredefaultpath
    addpath(pwd)
    ft_defaults

This ensures that FieldTrip is the only non-MATLAB toolbox on your path.
{% include markup/end %}

## The data

The USB stick contains three versions of the data:

- ds000117-pruned
- ds000117-zipped
- ds000117-practical.tar

### ds000117-pruned

This is a a subset of the original data. It contains the complete data from subject 15 and can be used as is. To reduce the size without changing the organization of the BIDS structure, we have zero'ed all large data files, just like for the [BIDS examples](https://github.com/bids-standard/bids-examples). This pruned version also contains (in the derivatives folder) the results of all pipelines used in these tutorials.

Copying many small and empty files can take a lot of time, hence we expect that copying the zipped version will be faster.

### ds000117-zipped

{% include markup/red %}
It turned out that this approach with the multiple zip files did not work to distribute the data reliably; Windows users would unzip with the graphical user interface and get all files scattered over different places.
{% include markup/end %}

This is a zipped version that contains the same as the pruned version. Different subdirectories have been added to separate zip files. You can copy these zip files to your computer and subsequently unzip them. The unzipping should be done in a specific order. You should start with

```bash
unzip ds000117-pruned-root.zip
```

For the following ones subject 15 is required, the others are optional:

```bash
unzip ds000117-pruned-sub-01.zip
unzip ds000117-pruned-sub-02.zip
unzip ds000117-pruned-sub-03.zip
unzip ds000117-pruned-sub-04.zip
unzip ds000117-pruned-sub-05.zip
unzip ds000117-pruned-sub-06.zip
unzip ds000117-pruned-sub-07.zip
unzip ds000117-pruned-sub-08.zip
unzip ds000117-pruned-sub-09.zip
unzip ds000117-pruned-sub-10.zip
unzip ds000117-pruned-sub-11.zip
unzip ds000117-pruned-sub-12.zip
unzip ds000117-pruned-sub-13.zip
unzip ds000117-pruned-sub-14.zip
unzip ds000117-pruned-sub-15.zip
unzip ds000117-pruned-sub-16.zip
```

Again, subject 15 is required, the others are optional:

```bash
unzip ds000117-pruned-derivatives-freesurfer-sub-01.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-02.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-03.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-04.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-05.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-06.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-07.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-08.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-09.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-10.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-11.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-12.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-13.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-14.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-15.zip
unzip ds000117-pruned-derivatives-freesurfer-sub-16.zip
```

The full data for subject 15 is too large to fit in a single zip file:

```bash
unzip ds000117-zipped/ds000117-pruned-derivatives-meg_derivatives-sub-15-run-01.zip
unzip ds000117-zipped/ds000117-pruned-derivatives-meg_derivatives-sub-15-run-02.zip
unzip ds000117-zipped/ds000117-pruned-derivatives-meg_derivatives-sub-15-run-03.zip
unzip ds000117-zipped/ds000117-pruned-derivatives-meg_derivatives-sub-15-run-04.zip
unzip ds000117-zipped/ds000117-pruned-derivatives-meg_derivatives-sub-15-run-05.zip
unzip ds000117-zipped/ds000117-pruned-derivatives-meg_derivatives-sub-15-run-06.zip
```

The others are optional:

```bash
unzip ds000117-pruned-derivatives-meg_derivatives-sub-01.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-02.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-03.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-04.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-05.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-06.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-07.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-08.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-09.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-10.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-11.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-12.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-13.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-14.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-15.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-16.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sub-emptyroom.zip
```

The results of the FieldTrip hands-on pipelines are each contained in
a single zip file:

```bash
unzip ds000117-pruned-derivatives-meg_derivatives-anatomy.zip
unzip ds000117-pruned-derivatives-meg_derivatives-groupanalysis.zip
unzip ds000117-pruned-derivatives-meg_derivatives-raw2erp.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sensoranalysis.zip
unzip ds000117-pruned-derivatives-meg_derivatives-sourceanalysis.zip
```

### ds000117-practical

This is a version that has even been trimmed down further. It contains the data of one run of one subject. Note that it is not subject 15, as used in the FieldTrip tutorials, but subject 01. You can use the single run of this single subject in the same fashion, but you will have to change the file name in some tutorials.

For the group analysis tutorial you will need all processed data from all subjects. That is not included here, please get it from one of the other versions.
