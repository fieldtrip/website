---
title: How can I anonymize or deidentify a BrainVision dataset?
tags: [faq, brainvision, raw, anonymize, sharing]
---

# How can I anonymize or deidentify a BrainVision dataset?

The BrainVision recorder and analyzer software writes EEG data in a combination of three separate files

1. A text header file (`.vhdr`) containing the header information
2. A text marker file (`.vmrk`) containing information about events in the data
3. A binary data file (`.eeg`) containing the voltage values of the EEG

We usually refer to such a dataset by pointing to the header file, since that includes pointers to the events and data file.

The header and the marker file might contain potentially identifying information, such as the name of the subject (when used in the original file name) or the data and time at which the recording was done. You can check for yourself by opening the `.vhdr` and .`vmrk` files in a text editor.

To anonymize the BrainVision dataset, you can use the following code:

    hdr   = ft_read_header(inputfile);
    dat   = ft_read_data(inputfile, 'header', hdr);
    event = ft_read_event(inputfile);

    hdr = rmfield(hdr, 'orig');

    ft_write_data(inputfile, dat, 'dataformat', 'brainvision_eeg', 'header', hdr, 'event', event)

The original header information in `hdr.orig` contains the full ASCII description and therefore is potentially identifying. Hence we remove it prior to  passing it on to **[ft_write_data](/reference/fileio/ft_write_data)** which writes the data, header and events back to disk.  

## Additional notes

When reading a BrainVision dataset and wwiting it back to disk, the comments in the `.vhdr` file (starting with a semicolon) are removed as well. Furthermore, there might be information in the header file about electrode impedances or electrode positions that is not parsed by the FieldTrip reading functions: that will also not be present in the output files.
