---
layout: default
---

{{tag>faq dataformat preprocessing}}

# How can I extend the reading functions with a new dataformat?

Implementing a new dataformat is done by extending the **[ft_read_header](/reference/ft_read_header)**, **[ft_read_data](/reference/ft_read_data)** and **[ft_read_event](/reference/ft_read_event)** functions. These functions are basically wrappers around many different fileformats, providing a common interface so that FieldTrip does not have to deal with format-specific details.

To ensure that the appropriate low-level reading functions are executed, the **[ft_filetype](/reference/ft_filetype)** function should be extended to allow auto-detection of the file format. This detection can be based on the filename extension, but preferably is done on some magic bytes at the start of the file, or by simultaneously detecting a collection of files (i.e. a header file with a corresponding data and trigger file). 

If the new file format contains MEG data, the magnetometer/gradiometer sensor description is also important. For that we usually make a xxx2grad function. Have a look in fieldtrip/fileio/private/ for some examples.

Each of the ft_read_xxx functions starts with a common section, then has a long switch-ladder with all formats, and ends again with a common section. When implementing the new format, you probably don't have to worry about the common sections at the beginning and end. 

Note that the FieldTrip reading functions are shared with SPM and EEGLAB, so adding it to FieldTrip also makes the new format accessible for those packages. 


