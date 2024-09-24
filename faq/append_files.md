---
title: How can I append the files of two separate recordings?
category: faq
tags: [dataformat, preprocessing]
---

# How can I append the files of two separate recordings?

It can happen that in one experimental EEG session you have recorded the data in different runs or blocks, where the data of each run or block ends up in a separate file on disk. Since the definition of trials in FieldTrip is based on reading triggers from the original data and refers to the sample numbers in that recording (assuming the samples all refer to the same file), the handling of complex sequences of trials and triggers works best with recordings contained that in a single file.

To facilitate working with the data in the different runs or blocks, you can concatenate them and treat the data as if it were a continuous recording. For that you would do something like the following:

    hdr1 = ft_read_header(filename1);
    dat1 = ft_read_data(filename1);
    evt1 = ft_read_event(filename1);

    hdr2 = ft_read_header(filename2);
    dat2 = ft_read_data(filename2);
    evt2 = ft_read_event(filename2);

    hdr = hdr1;               % the headers are assumed to be the same wrt samping rate and channel names
    dat = cat(2, dat1, dat2);  % concatenate the data along the 2nd dimension

    % shift the sample of the events or triggers in the second block
    for i=1:length(evt2)
      evt2(i).sample = evt2(i).sample + nsamples1;
    end

    evt = cat(1, evt1, evt2); % concatenate the events

You can subsequently write the data back to disk with

    ft_write_data('concatenated.vhdr', dat, 'header', hdr, 'event', evt);

Note that in the additional options to **[ft_write_data](/reference/fileio/ft_write_data)** you should specify the file format.

{% include /markup/blue %}
We recommend the BrainVision `.vhdr` format, which results in a triple of files (vhdr/vmrk/eeg). This is also one of the formats recommended by [BIDS](https://bids.neuroimaging.io).
{% include /markup/end %}

The **[ft_write_data](/reference/fileio/ft_write_data)** function can export data to the following file formats.

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
