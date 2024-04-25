---
title: Reading is slow, can I write my raw data to a more efficient file format?
tags: [faq, preprocessing, dataformat, raw]
---

# Reading is slow, can I write my raw data to a more efficient file format?

Usually the **[ft_preprocessing](/reference/ft_preprocessing)** function will read small segments of data from your original data file, corresponding to the trials in your experiment. Some file formats are inefficient to read in, and if you read many small segments from such a file, you may notice that it is very slow. One method to speed it up is by converting your original raw data into a more efficient format. Another method is to first preprocess all data as a single long continuous segment. Subsequently the data can be cut into smaller pieces, corresponding with the trials as indicated by the trigger events.

## Preprocessing all continuous data at once, cut out the trials later

If the file format is continuous, you can simply call **[ft_preprocessing](/reference/ft_preprocessing)** without defining any trial

    cfg = [];
    cfg.dataset = 'yourfile.ext';
    % other options ...
    data_all = ft_preprocessing(cfg);

Subsequently you can use **[ft_definetrial](/reference/ft_definetrial)** and/or your own trial function to define segments of interest. These segments or "trials" are specified in a Nx3 matrix with the begin sample, end sample and offset of each trial. The **[ft_redefinetrial](/reference/ft_redefinetrial)** function can be used to cut the selected trials out of the preprocessed continuous data.

## Converting to another format

A very simple and efficient file format supported by FieldTrip is labeled 'fcdc_matbin'. It is not an official file format, but was invented here at the FCDC. It consists of two files: a .mat MATLAB file that contains the header (and optionally the events) and a .bin binary file that contains the data.

The mat file is just a standard MATLAB file and it contains the header (and optionally events) just like they are returned by the **[ft_read_header](/reference/fileio/ft_read_header)** and **[ft_read_event](/reference/fileio/ft_read_event)** functions. So you don't lose any information in the mat file.

The bin file contains the data samples as double precision floating point values, precisely the same as it is returned by the **[ft_read_data](/reference/fileio/ft_read_data)** function. The bin file is channel-multiplexed and little-endian. Reading from the data file is fast because the reading function can jump immediately to the desired location in the file with fseek and read the data, without any processing, conversion or calibration.

Below is an example how you can convert an arbitrary file (here a BCI2000 file) to the fcdc_matbin format.

    hdr = ft_read_header('eeg1_2.dat');
    dat = ft_read_data('eeg1_2.dat', 'header', hdr);

    >> whos dat hdr
    Name       Size                  Bytes  Class     Attributes
    dat       64x19696            10084352  double
    hdr        1x1                  128768  struct

    ft_write_data('test.bin', dat, 'header', hdr, 'dataformat', 'fcdc_matbin');

    >> ls test.*
    test.bin  test.mat

You can read the fcdc_matbin file just like any other file format in FieldTrip, i.e. by using the **[ft_read_header](/reference/fileio/ft_read_header)** and **[ft_read_data](/reference/fileio/ft_read_data)** function. For **[ft_preprocessing](/reference/ft_preprocessing)** you can specify the name of the dataset like this

    cfg = []
    cfg.dataset = 'test.bin'

and the **[ft_preprocessing](/reference/ft_preprocessing)** function (or any other function that needs to read from the file) will automatically figure out that the data is contained in the bin/mat pair.

{% include markup/skyblue %}
With the code above the events (e.g., trigger codes) are not stored in the output. Since the sample indexing remains exactly the same, you can simply do

    event = ft_read_event('eeg1_2.dat')
    save event.mat event

i.e. and simply save the events to a MATLAB file for later reuse.
{% include markup/end %}
