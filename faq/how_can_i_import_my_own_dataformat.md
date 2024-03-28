---
title: How can I import my own data format?
tags: [faq, dataformat, preprocessing]
---

# How can I import my own data format?

There are two approaches for importing data from an unsupported format: you can extend FieldTrip with new code, or you can circumvent the import procedure.

## Extend the FieldTrip reading functions

The first and preferred way of implementing a new data format is by extending the **[ft_read_header](/reference/fileio/ft_read_header)**, **[ft_read_data](/reference/fileio/ft_read_data)** and **[ft_read_event](/reference/fileio/ft_read_event)** functions. These functions are wrappers around the code for many different file formats and provide a common interface. Probably you will also have to add your file format to the **[ft_filetype](/reference/fileio/ft_filetype)** function so that the files are properly recognized.

## Using your own low-level reading functions when calling ft_read_header/data/event

If you want to use ft_read_header/data/event for reading in your data, but your data format is atypical and not widely used outside your lab, it is perfectly fine **not to add** the format to the FieldTrip code-base but to only share it inside your lab.

There is a simple way you can use your own reading functions: make your own function `YourFormat.m`. When calling for example **[ft_preprocessing](/reference/ft_preprocessing)**, you should specify the name of your specific function as the 'headerformat', 'dataformat' and 'eventformat' option. This will result in your reading function being called under the hood.

For example:

    cfg = [];
    cfg.headerfile   = 'yourfile.ext'
    cfg.headerformat = 'YourFormat'
    cfg.datafile     = 'yourfile.ext'
    cfg.dataformat   = 'YourFormat'
    cfg.eventfile    = 'yourfile.ext'
    cfg.eventformat  = 'YourFormat'
    ...
    data = ft_preprocessing(cfg)

Your reading function has to use the following input/output format:

    hdr   = YourFormat(filename)
    dat   = YourFormat(filename, hdr, begsample, endsample, chanindx)
    event = YourFormat(filename, hdr)

Depending on the number of input arguments that your function receives (1, 5 or 2), it should return the header, the data or the events.

Please look at the help and especially the code of **[ft_read_header](/reference/fileio/ft_read_header)**, **[ft_read_data](/reference/fileio/ft_read_data)** and **[ft_read_event](/reference/fileio/ft_read_event)** for the details of the implementation. Some examples of file formats implemented in FieldTrip using this approach are [biopac_acq.m](https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/biopac_acq.m), [snirf.m](https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/snirf.m), [motion_c3d.m](https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/motion_c3d.m), [qualisys_tsv.m](https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/qualisys_tsv.m), and [liberty_csv.m](https://github.com/fieldtrip/fieldtrip/blob/master/fileio/private/liberty_csv.m).

## Circumvent the FieldTrip reading functions

Alternatively, if you have already somehow read the data into MATLAB, you can reformat that data into a data structure that is compatible with FieldTrip. Raw data that is comparable with the output of preprocessing should consist of a structure with the fields

    data.label      % cell-array containing strings, Nchan*1
    data.fsample    % sampling frequency in Hz, single number
    data.trial      % cell-array containing a data matrix for each
                    % trial (1*Ntrial), each data matrix is a Nchan*Nsamples matrix
    data.time       % cell-array containing a time axis for each
                    % trial (1*Ntrial), each time axis is a 1*Nsamples vector
    data.trialinfo  % this field is optional, but can be used to store
                    % trial-specific information, such as condition numbers,
                    % reaction times, correct responses etc. The dimensionality
                    % is Ntrial*M, where M is an arbitrary number of columns.
    data.sampleinfo % optional array (Ntrial*2) containing the start and end
                    % sample of each trial

Each trial can have a different number of samples (i.e. variable length), that is why each trial needs an individual time axis. If your data consists of trials with a fixed length, then each vector data.time{i} is equal to data.time{1}. If your data consists of a single trial, e.g., when it is a continuous recording, there is only a single data.time{1} and single data.trial{1}. The data format is described in more detail in **[ft_datatype_raw](/reference/utilities/ft_datatype_raw)**. The main FieldTrip data structures are jointly described in [this FAQ](/faq/how_are_the_various_data_structures_defined).

If your data represents a continuous recording, you can also consider taking a simple two-step approach by first representing your data into _one long trial_ as described above, and then cutting it up into individual trials using **[ft_redefinetrial](/reference/ft_redefinetrial)**. Note also that if you want to add trial-specific information related to the short trials you cut out of the continuous representation, you need to create the trialinfo field only _after_ your call to ft_redefinetrial. If your data is a single continuous trial, you can simply call **[ft_redefinetrial](/reference/ft_redefinetrial)**, supplying a trial definition in the config, e.g.

    cfg.trl = [  1  100 -10;
               101  200 -10;
               201  300 -10];
    newdata = ft_redefinetrial(cfg, data);

## Converting already processed data

It might also be that you do not want to read raw data from file, i.e. you do not want to do everything (starting with preprocessing) using FieldTrip, but you only want the later stages of an analysis that you already performed with other software. This is the approach for example taken in the **[eeglab2fieldtrip](/reference/external/eeglab/eeglab2fieldtrip)**, **[besa2fieldtrip](/reference/besa2fieldtrip)**, and **[spm2fieldtrip](/reference/spm2fieldtrip)** functions.
