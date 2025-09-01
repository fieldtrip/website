---
title: Getting started with Artinis NIRS data
category: getting_started
tags: [dataformat, nirs, artinis]
redirect_from:
    - /getting_started/artinis/
---

# Getting started with Artinis NIRS data

[Artinis Medical Systems BV](http://www.artinis.com/) is a Dutch company located close to Nijmegen, which develops and produces systems for functional NIRS. Artinis has multiple hardware designs, which all work with the same [Oxysoft](http://www.artinis.com/oxysoft) acquisition and analysis software.

The data that is recorded with Oxysoft is organized in various files: all data recorded during a measurement is contained in binary `.oxy3` or `.oxy4` files. The information about the transmitter and receiver optodes is represented in `optodetemplates.xml`, which is usually located in `C:\Program files\Artinis Medical Systems\Oxysoft\`. Following data acquisition, some processing can be done using OxySoft, the results of this are stored in a project file, which again is an XML file.

{% include markup/yellow %}
The `optodetemplates.xml` file should be in the same directory as the oxy3 or oxy4 files.
{% include markup/end %}

{% include markup/red %}
The `.oxy4` file format is currently only supported when you run MATLAB on a Windows computer.
{% include markup/end %}

The oxy3/oxy4 file contains the optical signals and data from the auxiliary accelerometer and ADC-channels. The file will also contain any triggers recorded during the measurement, which allow for synchronization with a stimulus presentation computer. In FieldTrip we can use **[ft_read_header](/reference/fileio/ft_read_header)** and **[ft_read_data](/reference/fileio/ft_read_data)** to read the content, but usually we prefer to use the higher level **[ft_preprocessing](/reference/ft_preprocessing)**

The optode template specifies the configuration of the transmitting and receiving optodes, i.e. which optodes were combined in channels, and how the channels are to be visualized in the acquisition software. This file contains different groups of configurations, also called optode "templates" or "montages". Each individual optode template has an unique ID, which is stored with the measurement in the binary file. It can be read using **[ft_prepare_layout](/reference/ft_prepare_layout)** and used for plotting. See also the [layout](/tutorial/plotting/layout) and [plotting](/tutorial/plotting) tutorial.

The project file can contain data that was added _after_ the measurement, e.g., events extracted from the trigger channel, or events that were manually added after the measurement. This makes the project file relevant in **[ft_definetrial](/reference/ft_definetrial)** and Artinis will upon request provide a custom trial function to parse this file and to use it for segmenting the continuous data in trials. Furthermore, the project file can contain spatial 3D MNI-coordinates of the optodes. Note that the project file can refer to multiple recordings, but also that one oxy3/oxy4 file can be included in multiple project files. This means that there is no guaranteed unique mapping between oxy3/oxy4 files and project files.

The use of datasets from an Artinis NIRS system is demonstrated in the [single-channel](/tutorial/nirs/nirs_singlechannel) and [multi-channel](/tutorial/nirs/nirs_multichannel) NIRS tutorials.

## See also

{% include seealso tag="artinis" %}