---
title: How can I convert one dataformat into an other?
tags: [faq, dataformat, preprocessing]
---

# How can I convert one dataformat into an other?

You can read in the data from the original data format using **[ft_preprocessing](/reference/ft_preprocessing)** and subsequently use the **[ft_write_data](/reference/ft_write_data)** function to write the data to another format that you can specify.

The **[ft_write_data](/reference/ft_write_data)** function requires that you construct a header structure that describes the data (i.e. channel names, sampling frequency) similar to what is returned by **[ft_read_header](/reference/ft_read_header)**. If your data is represented as a FieldTrip raw data structure, i.e. consistent with the documentation in **[ft_datatype_raw](/reference/ft_datatype_raw)**, you can use **[ft_fetch_header](/reference/ft_fetch_header)** to construct a header on the fly, e.g.

    hdr = ft_fetch_header(data);

If your data is continuous and hence the data structure contains only a single (very long) trial do:

    dat = data.trial{1};
    ft_write_data('yourfile.ext', dat, 'header', hdr, ...)

If you want to write multiple trials, you have to concatenate them and like this:

    dat = cat(2,data.trial{:})
    ft_write_data('yourfile.ext', dat, 'header', hdr, ...)

Note that in the additional options to ft_write_data you should specify the file format. The **[ft_write_data](/reference/ft_write_data)** function can export data to the following file formats

- edf
- gdf
- brainvision_eeg
- neuralynx_ncs
- neuralynx_sdma
- plexon_nex
- riff_wave
- fcdc_matbin
- fcdc_mysql
- fcdc_buffer
- MATLAB
