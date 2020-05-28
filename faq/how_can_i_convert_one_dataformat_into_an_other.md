---
title: How can I convert one dataformat into an other?
tags: [faq, dataformat, preprocessing]
---

# How can I convert one dataformat into an other?

You can read in the data from the original data format using **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)** and subsequently use the **[ft_write_data](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_write_data.m)** function to write the data to another format that you can specify.

The **[ft_write_data](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_write_data.m)** function requires that you construct a header structure that describes the data (i.e. channel names, sampling frequency) similar to what is returned by **[ft_read_header](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_header.m)**. If your data is represented as a FieldTrip raw data structure, i.e. consistent with the documentation in **[ft_datatype_raw](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_raw.m)**, you can use **[ft_fetch_header](https://github.com/fieldtrip/fieldtrip/blob/release/ft_fetch_header.m)** to construct a header on the fly, e.g.

    hdr = ft_fetch_header(data);

If your data is continuous and hence the data structure contains only a single (very long) trial:

    dat = data.trial{1};
    ft_write_data('yourfile.ext', dat, 'header', hdr, ...)

If you want to write multiple trials, you have to concatenate them like this:

    dat = cat(2,data.trial{:})
    ft_write_data('yourfile.ext', dat, 'header', hdr, ...)

Note that in the additional options to ft_write_data you should specify the file format. The **[ft_write_data](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_write_data.m)** function can export data to the following file formats

- edf
- gdf
- anywave_ades
- brainvision_eeg
- neuralynx_ncs
- neuralynx_sdma
- plexon_nex
- fcdc_matbin
- fcdc_mysql
- fcdc_buffer
- flac, m4a, mp4, oga, ogg, wav (audio formats)
- MATLAB
