---
title: How can I extend the reading functions with a new dataformat?
parent: Specific data formats
category: faq
tags: [dataformat, preprocessing]
redirect_from:
    - /faq/how_can_i_extend_the_reading_functions_with_a_new_dataformat/
---

# How can I extend the reading functions with a new dataformat?

Implementing reading of a new file format is done by extending the **[ft_read_header](/reference/fileio/ft_read_header)**, **[ft_read_data](/reference/fileio/ft_read_data)** and **[ft_read_event](/reference/fileio/ft_read_event)** functions. These functions are basically wrappers around many different file formats, providing a common interface so that FieldTrip does not have to deal with format-specific details.

To ensure that the appropriate low-level reading functions are executed, the **[ft_filetype](/reference/fileio/ft_filetype)** function should be extended to allow auto-detection of the file format. This detection can be based on the filename extension, but preferably is done on some magic bytes at the start of the file, or by detecting the simultaneous presence of multiple files (i.e. a header file with a corresponding data file and a trigger file).

Each of the ft_read_xxx functions starts with a common section, then has a long switch-ladder with all formats, and ends again with a common section. When implementing the new format, you probably don't have to worry about the common sections at the beginning and end.

Rather than changing the code in ft_read_xxx itself, we recommend that you make use of the section

    otherwise
       if exist(headerformat, 'file')
         % attempt to run "headerformat" as a function, this allows the user to specify an external reading function
         % this is also used for bids_tsv, biopac_acq, motion_c3d, opensignals_txt, qualisys_tsv, sccn_xdf, and possibly others
         hdr = feval(headerformat, filename);
       else
        ...

Here it is shown for `ft_read_header`, the others have a similar section with `dataformat` and `eventformat` respectively. If you implement your fileformat as `manufacturer_extension`, then this code will look for a function with the corresponding name and call it like this:

    hdr = manufacturer_extension(filename)
    dat = manufacturer_extension(filename, hdr, begsample, endsample, chanindx)
    evt = manufacturer_extension(filename, hdr)

You provide the `fieldtrip/fileio/private/manufacturer_extension.m` function and implement it such that - depending on the number of input arguments - it returns the header, the data or the events. Please check one of the already available implementations as example. If your reading function depends on an external library, please add that library to `fieldtrip/external` and use **[ft_hastoolbox](//reference/utilities/ft_hastoolbox)** to detect its presence and/or add it to the path.

If the new file format contains MEG data, the magnetometer/gradiometer sensor description is also important. For that we usually implement a conversion in a xxx2grad function. Have a look in `fieldtrip/fileio/private/` for some examples.

Note that the FieldTrip reading functions are shared with SPM and EEGLAB, so adding it to FieldTrip also makes the new format accessible for those packages.
