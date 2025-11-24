---
title: Getting started with EGI/Philips/Magstim data
tags: [dataformat, egi, eeg]
category: getting_started
redirect_from:
    - /getting_started/egi/
---

{% include markup/green %}
Electrical Geodesics Inc. (EGI) was a company specialized in high density EEG systems using their geodesic net with wet sponges as electrodes. It was acquired by Philips in 2017, and in 2020 sold to Magstim. It currently again operates under the name [EGI](https://www.egi.com), which is also the name we continued to use in FieldTrip code and documentation.
{% include markup/end %}

Please add information if you're using an EGI/Philips/Magstim system and/or data and want to share info with other FieldTrip users.

## Introduction to the EGI file formats

Net Station can export data to several data formats that FieldTrip can read in.

- Data in the .egis, .sbin, and .mff formats can be read in by FieldTrip. We don't have details on how well they work, and what the known issues are.
- For the simple binary (.raw) format only the channels from the hdEEG net are exported, the PIB channels, for instance, are not. Channel labels are not present in this format, and are thus made on the fly by FieldTrip. Events are present and read in correctly. Data sets containing multiple epochs are exported by NetStation as separate .raw files. The events are, however, exported as one file, which make it tricky (read impossible) to align data and events properly when having multiple discontinuous epochs.
- After exporting to EDF/EDF+ (.edf) all channels, including PIB channels, are read in correctly, including channel labels. However, the events, which are stored on the annotation channel, are written in a way by Net Station that is not compatible with the edf+ reading implementation in FieldTrip. So, events do not come out properly. Also discontinuous epochs are "glued" together as one "continuous" data stream.
- Other formats like .ave, .gave, .ses are not supported, but the data can be read by first exporting to one of the supported formats.

## Meta File Format (mff)

The beta version of NetStation 4.5 (and up) writes data in .mff format, which is supported by FieldTrip as of 2011. FieldTrip reads in the data of all signals (hdEEG-net, PIB, etc). Data sets containing multiple epochs are supported, FieldTrip keeps track of the offset to the start of the recording for all epochs. Also events are read in, and also with discontinuous epochs aligning of events to data works.

The initial (v1) implementation was made by Ingrid Nieuwenhuis. It works for quite a few datasets but also has a number of known limitations (a.o. not full reading of info from triggers/events).

The second (v2) implementation is provided by the EGI company and is based on their general-purpose Java library and should support all data format features.

The third (v3) implementation is partially provided by EGI and has been reworked by Arno Delorme for EEGLAB. It supports both reading and writing.

In short, the code in ft_read_header and ft_read_data does

    case {'egi_mff_v1' 'egi_mff'}
      % do the old stuff
    case {'egi_mff_v2'}
      % do the newer stuff
    case {'egi_mff_v3'}
      % do the newest stuff

At this moment the default is to use the egi_mff_v1 implementation. This can be overruled by specifying

    cfg.dataformat = 'egi_mff_v3'
    cfg.headerformat = 'egi_mff_v3'

to **[ft_preprocessing](/reference/ft_preprocessing)** and all other high-level FT functions that read data. Furthermore, by specifying

    ft_read_header(...., 'headerformat', 'egi_mff_v3')
    ft_read_data(...., 'headerformat', 'egi_mff_v2', 'dataformat', 'egi_mff_v3')

also the low-level [fileio](/development/module/fileio) functions will use the v3 reading functions.

### Installing the EGI Java implementation for version 2

The egi_mff_v2 implementation in MATLAB depends on a generic Java implementation of the reading functions.

To ensure that MATLAB can find the .jar file, you have to add a path to the MFF-1.0.jar (java) file by typing the following on your MATLAB prompt

    javaaddpath path/to/fieldtrip/external/egi_mff_v2/java/MFF-1.2.jar

For more information have a look at [javaaddpath](http://www.mathworks.nl/help/techdoc/ref/javaaddpath.html) and [javaclasspath](http://www.mathworks.nl/help/techdoc/ref/javaclasspath.html).

### Installing the EGI Java implementation for version 3

Download the source code from <https://github.com/arnodelorme/mffmatlabio> and add it to your path.

## See also

{% include seealso tag="egi" %}
