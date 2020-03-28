---
title: How can I import my own data format?
tags: [faq, dataformat, preprocessing]
---

# How can I import my own data format?

There are two approaches for importing data from an unsupported format: you can extend FieldTrip with new code, or you can circumvent the import procedure.

## Extend the FieldTrip reading functions

The first and preferred way of implementing a new data format is by extending the **[ft_read_header](/reference/ft_read_header)**, **[ft_read_data](/reference/ft_read_data)** and **[ft_read_event](/reference/ft_read_event)** functions. These functions are wrappers around the code for many different file formats and provide a common interface. Probably you will also have to add your file format to the **[ft_filetype](/reference/ft_filetype)** function so that the files are properly recognized.

## Using your own low-level reading functions when calling ft_read_header/data/event

If you want to use ft_read_header/data/event for reading in your data, but your data format is very atypical and used only by your lab, it is preferred **not to add** the format to FieldTrip. However, there is a simple way you can still use your own reading functions: make your `read_xxx_header`, `read_xxx_data` and `read_xxx_event` functions, and be sure they are on the path. When calling for example **[ft_preprocessing](/reference/ft_preprocessing)**, you should specify the headerformat, dataformat and eventformat configuration options as the name of your specific function.

For example:

    cfg = [];
    cfg.headerfile   = 'yourxxxfile'
    cfg.headerformat = 'read_xxx_header'
    cfg.datafile     = 'yourxxxfile'
    cfg.dataformat   = 'read_xxx_data'
    cfg.eventfile    = 'yourxxxfile'
    cfg.eventformat  = 'read_xxx_event'
    ...
    data = ft_preprocessing(cfg)

Keep in mind that your reading functions have to follow the following input/output format.  

    hdr   = read_xxx_header(filename)
    dat   = read_xxx_data(filename, hdr, begsample, endsample, chanindx)
    event = read_xxx_event(filename, hdr)

See the help and the code of ft_read_header, ft_read_data and ft_read_event for the details of each of these variables.

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

Each trial can have a different number of samples (i.e. variable length), that is why each trial needs an individual time axis. If your data consists of trials with a fixed length, then each vector data.time{i} is equal to data.time{1}. If your data consists of a single trial, e.g. when it is a continuous recording, there is only a single data.time{1} and single data.trial{1}. The data format is described in more detail in **[ft_datatype_raw](/reference/ft_datatype_raw)**. The main FieldTrip data structures are jointly described in [this FAQ](/faq/how_are_the_various_data_structures_defined).

If your data represents a continuous recording, you can also consider taking a simple two-step approach by first representing your data into _one long trial_ as described above, and then cutting it up into individual trials using **[ft_redefinetrial](/reference/ft_redefinetrial)**. Note also that if you want to add trial-specific information related to the short trials you cut out of the continuous representation, you need to create the trialinfo field only _after_ your call to ft_redefinetrial. If your data is a single continuous trial, you can simply call **[ft_redefinetrial](/reference/ft_redefinetrial)**, supplying a trial definition in the config, e.g.

    cfg.trl = [1    100 -10;
               101  200 -10;
               201  300 -10];
    newdata = ft_redefinetrial(cfg, data);

## Converting already processed data

It might also be that you do not want to read raw data from file, i.e. you do not want to do everything (starting with preprocessing) using FieldTrip, but you only want the later stages of an analysis that you already performed with other software. This is the approach for example taken in the **[besa2fieldtrip](/reference/besa2fieldtrip)** and **[spm2fieldtrip](/reference/spm2fieldtrip)** functions.
