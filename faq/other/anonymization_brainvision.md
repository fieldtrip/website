---
title: How can I anonymize or deidentify a BrainVision dataset?
category: faq
tags: [brainvision, raw, anonymize, sharing]
redirect_from:
    - /faq/how_can_i_anonymize_a_brainvision_dataset/
    - /faq/anonymization_brainvision/
---

The BrainVision recorder and analyzer software writes EEG data in a combination of three separate files

1. A text header file (`.vhdr`) containing the header information
2. A text marker file (`.vmrk`) containing information about events in the data
3. A binary data file (`.eeg`) containing the voltage values of the EEG

We usually refer to such a dataset by pointing to the header file, since that includes pointers to the events and data file.

The header and the marker file might contain potentially identifying information, such as the name of the subject (when used in the original file name) or the data and time at which the recording was done. You can check for yourself by opening the `.vhdr` and .`vmrk` files in a text editor.

The vmrk file will have a line like this

    Mk1=New Segment,,1,1,0,20190705163846757252 

where 20190705 is the date of recording and the rest the time (i.e., this recording was started at 16:38 in the afternoon). 

## Scrubbing or shifting the dates

If the data is continuous there is only one segment, which is not interesting for analysis. A quick solution in that case is to remove the `New Segment` marker completely. However, if the recording was paused, there can be multiple `New Segment` markers. In that case you should not remove them, as they indicate a gap or hole in the data that you should consider in the analysis. The start of the new segment could for example introduce a jump in the data, and thereby a filter artifact, and you would not want to segment the data in trials that cross the new segment boundary.

To keep the time of day, for example when it is relevant in the analysis as a potential variable or confound, you can replace the first 6 digits. The [BIDS specification](https://bids-specification.readthedocs.io/en/stable/02-common-principles.html#units) recommends to take a date before  1925, as nobody would interpret that as a realistic recording date. Using a text editor, you could replace the first 8 digits by `19000101`, i.e., 1 January 1900.

If you also want to keep the relative order in which participants were measured, or the time between subsequent sessions on the same subject, you can shift all the dates with a random amount, where that amount is the same for all recordings. Shifting with a certain amount of years is easy, but better (i.e., less identifiable) is to shift with YY years, MM months and DD days, where only _you_ know how large that shift is. Doing that by hand is a bit tricky, especially when the date subsequently crosses boundaries between months and/or years. You can use MATLAB to help with that, for example using something like this: 

    >> datetime('20190705', 'InputFormat', 'yyyyMMdd') % today
    ans = 
      datetime
       05-Jul-2019

    >> datetime('20190705', 'InputFormat', 'yyyyMMdd') - years(10) - days(45) % shift it
    ans = 
      datetime
       20-May-2009 13:48:00

    >> yyyymmdd(ans) % this is a MATLAB function to convert the datetime back into a string
    ans =
        20090520
    

## Rewriting the files

Alternatively, you can use the following code to anonymize the BrainVision recordings:

    hdr   = ft_read_header(inputfile);
    dat   = ft_read_data(inputfile, 'header', hdr);
    event = ft_read_event(inputfile);

    hdr = rmfield(hdr, 'orig');

    ft_write_data(inputfile, dat, 'dataformat', 'brainvision_eeg', 'header', hdr, 'event', event)

This reads and writes the data. The original header information in `hdr.orig` contains the full ASCII description and therefore is potentially identifying. Hence we remove it prior to  passing it on to **[ft_write_data](/reference/fileio/ft_write_data)**. 

A disadvantage of this approach is that there can be additional information such as filter settings, electrode positions, and impedance measurements in the `.vhdr` file that are not read or represented in the `hdr` structure, and hence also not written. Also comments in the `.vhdr` file (starting with a semicolon) will be removed by this as well.
