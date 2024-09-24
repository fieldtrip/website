---
title: Getting started with SNIRF data
category: getting_started
tags: [dataformat, snirf, nirs]
---

# Getting started with SNIRF data

The [Shared Near Infrared Spectroscopy Format](https://fnirs.org/resources/software/snirf/) (SNIRF) is designed to facilitate sharing and analysis of NIRS data. The specification itself can be found on GitHub [here](https://github.com/fNIRS/snirf).

The SNIRF format itself is base on the Hierarchical Data format [HDF5](https://www.hdfgroup.org/solutions/hdf5/). This is a very flexible [container file format](https://en.wikipedia.org/wiki/Container_format_(computing)) which in fact is also used by MATLAB for the `.mat` file format from version 7.3 onward, see [here](https://nl.mathworks.com/help/matlab/import_export/mat-file-versions.html). Specifying that it is HDF5 is not enough to standardize, it is also required to specify how data and metadata is organized inside the container. This is what has been defined in the [SNIRF format specification](https://github.com/fNIRS/snirf/blob/master/snirf_specification.md). The SNIRF format resembles the Homer NIRS format, but is more elaborate and flexible.

## Reading SNIRF data

In FieldTrip you can read SNIRF files using the low-level reading functions **[ft_read_header](/reference/fileio/ft_read_header)**, **[ft_read_data](/reference/fileio/ft_read_header)** and **[ft_read_event](/reference/fileio/ft_read_header)**, which also means that you can browse, import and preprocess the data in the standard way as explained in the tutorials using **[ft_databrowser](/reference/ft_databrowser)** and **[ft_preprocessing](/reference/ft_preprocessing)**.

## Writing SNIRF data

You can write data that is represented as a continuous FieldTrip raw data structure (see this [FAQ](/faq/how_are_the_various_data_structures_defined)) to a SNIRF file. That means that any data format supported by FieldTrip can be converted to SNIRF; this includes NIRS formats such as Artinis and Homer, but also non-NIRS data such as EEG. Channels in the raw data structure that are recognized as NIRS will be written in the [data](https://github.com/fNIRS/snirf/blob/master/snirf_specification.md#nirsidataj) field, all other channels will be written in the [aux](https://github.com/fNIRS/snirf/blob/master/snirf_specification.md#nirsiauxj) field.

Events or triggers are represented very differently in the different file formats; in FieldTrip we always use the format as returned by **[ft_read_event](/reference/fileio/ft_read_header)**. To write events to a SNIRF file you have to pass them as additional argument to **[ft_write_data](/reference/fileio/ft_read_header)** like this

    ft_write_data(filename, dat, 'header', hdr, 'event', event)

where the filename has the `.snirf` extension. For the `hdr` argument you can use the `data.hdr` field, for the `dat` argument you can use `data.trial{1}`, i.e. the Nchans\*Nsamples matrix that contains the data. In case you selected a subset of channels, you should use the `chanindx` argument to ensure that the mapping between `hdr.label` and the rows from the `dat` matrix is consistent.
