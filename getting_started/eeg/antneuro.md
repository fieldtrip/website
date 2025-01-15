---
title: Getting started with ANT-Neuro, ASA and EEProbe data
parent: EEG
grand_parent: Getting started
category: getting_started
tags: [dataformat, eeg, ant, asa, eeprobe]
redirect_from:
    - /getting_started/antneuro/
---

# Getting started with ASA and EEProbe

ASA and EEProbe are software products developed by [ANT Neuro](http://www.ant-neuro.com/). These both use the eeprobe format, which consists of files with the following extensions:

- .cnt continuous data
- .trg trigger information, this complements the .cnt file
- .avr averaged (i.e. ERP) data

The data in the .cnt and .avr files is compressed with a zip-like algorithm, which makes the implementation of reading functions more difficult. The original source code (C-language) is available at this page [ANT Neuro Documentation and Download](http://ant-neuro.com/supporting-documentation-and-downloads). Contact [ANT Neuro support](mailto:support@ant-neuro.com) in case you need help to compile import/export functionality based on this source code.

The FieldTrip functionality for reading asa or eeprobe files depends on the mex files that are present in fieldtrip/external/eeprobe. The FieldTrip release includes these files as a service to the users, however, these files are not maintained or supported by the FieldTrip team. Any problems with the source code of the mex files files should be addressed to [ANT Neuro's support](http://www.ant-neuro.com/support).

## Known limitations

It has been reported that FieldTrip does not allow to read large files (above 1Mb, in the specific case with a sampling rate of 2048 Hz and 33 channels). A workaround for this limitation is to export the data as .avr in asa (Version 4.7.3.1), after which read_eep_avr can read files above 2Mb with no problems. For exporting, you can use Menu Data→Write→EEG/MEG, then choose eeprobe, and make sure to change extension to .avr.
