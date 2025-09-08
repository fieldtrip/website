---
title: How are the various MATLAB data structures defined?
tags: [datatype, dataformat]
category: faq
redirect_from:
    - /faq/how_are_the_various_data_structures_defined/
    - /faq/datatype/
---

To ensure that the functions implemented in the FieldTrip toolbox can be mixed and matched, we always try to keep a small number of data structures.

The general principle is that a data structure should be as small as possible, but nevertheless contain enough information to fully understand its contents. Information on the data in a structure should not be replicated. If there is replication, there would be the risk of one function might use one version of the information whereas another function would use the other version. Changing the data in a structure should only require changing the information once.

Wherever possible, use one of the existing data representations if you are implementing new functionality. If needed, these can be extended with additional information. The use of an existing data structure allows the reuse of existing functions for plotting and further analysis. e.g., you can do freqanalysis on the output of componentanalysis, because the IC timeseries are represented just as raw data that comes out of preprocessing.

If you give a structure as input to an existing function, the type of the input structure will be determined using the datatype helper-function.

A FieldTrip data structure consists at least of numeric data specific to that particular datatype, and of descriptive fields which are needed to interpret the data. The different datatypes, their features and their historical development are defined in the following reference documentation:

- **[ft_datatype_raw](/reference/utilities/ft_datatype_raw)** contains sensor level time domain data typically obtained after calling [ft_definetrial](/reference/ft_definetrial) and [ft_preprocessing](/reference/ft_preprocessing).
- **[ft_datatype_comp](/reference/utilities/ft_datatype_comp)** contains the spatial topographies of the components and the component time courses and is obtained from a call to [ft_componentanalysis](/reference/ft_componentanalysis). It is represented just as raw data, except that an additional matrix is added describing the spatial topographies of the components. The original channel labels are replaced by strings like 'ica001', 'ica002', ... After [ft_componentanalysis](/reference/ft_componentanalysis), you can call any function that can work with raw data, e.g., [ft_timelockanalysis](/reference/ft_timelockanalysis) or [ft_freqanalysis](/reference/ft_freqanalysis). The [ft_topoplotIC](/reference/ft_topoplotIC) function can be used to visualize the component topographies and the [ft_databrowser](/reference/ft_databrowser) to look at the component time courses.
- **[ft_datatype_timelock](/reference/utilities/ft_datatype_timelock)** contains sensor level data, time-locked to time point 0, either as an average over trials or represented as single trials in a 3-D array. It is obtained after a call to [ft_timelockanalysis](/reference/ft_timelockanalysis) or [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage). Optionally, it can contain the estimated covariance matrix (again averaged over trials or for each trial in a 3-D array).
- **[ft_datatype_freq](/reference/utilities/ft_datatype_freq)** contains the sensor level frequency domain data obtained after a call to [ft_freqanalysis](/reference/ft_freqanalysis) or [ft_freqgrandaverage](/reference/ft_freqgrandaverage). The power can represent the complete trial, or it can be estimated (e.g., using wavelets) for multiple time points within each trial, resulting in a time-frequency representation (TFR).
- **[ft_datatype_mvar](/reference/utilities/ft_datatype_mvar)** contains sensor level MVAR model data in the time or frequency domain obtained by [ft_mvaranalysis](/reference/ft_mvaranalysis).
- **[ft_datatype_volume](/reference/utilities/ft_datatype_volume)** represents data on a regular 3-D grid, like an anatomical MRI, a functional MRI. It can also represent a source reconstructed estimate of the activity measured with MEG in case the source reconstruction is done on a regular 3-D dipole grid (like a box).
- **[ft_datatype_source](/reference/utilities/ft_datatype_source)** represents data that corresponds to locations in 3-D space. Compared to volume data, this representation is more general and also supports irregular source locations, e.g., a folded cortical sheet. It is always possible to convert volume data to source data. If the source data represents a regular 3-D grid (i.e. like a box), it is also possible to convert source data back to volume data.
- **[ft_datatype_spike](/reference/utilities/ft_datatype_spike)** is characterised as a sparse point-process, i.e. each neuronal firing is only represented as the time at which the firing happened. Optionally, the spike waveform can also be represented. Using the spike waveform, the neuronal firing events can be sorted into their single units. Spike data is obtained using [ft_read_spike](/reference/fileio/ft_read_spike) to read it from a Plexon, Neuralynx or other animal electrophysiology system file format containing spikes.
- **[ft_datatype_dip](/reference/utilities/ft_datatype_dip)**
- **[ft_datatype_parcellation](/reference/utilities/ft_datatype_parcellation)**
- **[ft_datatype_segmentation](/reference/utilities/ft_datatype_segmentation)**
- **[ft_datatype_sens](/reference/utilities/ft_datatype_sens)**
- **[ft_datatype_headmodel](/reference/utilities/ft_datatype_headmodel)**

You can use **[ft_datatype](/reference/utilities/ft_datatype)** to determine the type of data that is represented in a certain MATLAB structure.

## Old and new source data representation

We are working on a new representation of source data that is more consistent with the other data representations. Since it requires many changes to the code and might also affect the users' scripts, the differences are listed belo

### Old-style

An example of a source structure obtained after performing a frequency domain source reconstruction using **[ft_sourceanalysis](/reference/ft_sourceanalysis)** is shown here:

            pos: [6732x3 double]           positions at which the source activity could have been estimated
         inside: [1x3415 double]           indices to the positions at which the source activity is actually estimated
        outside: [1x3317 double]           indices to the positions at which the source activity has not been estimated

            dim: [xdim ydim zdim]          if the positions are described as a regularly spaced 3D grid, this contains the
                                             dimensionality of the 3D volume
            vol: [1x1 struct]              volume conductor model
      cumtapcnt: [10x1 double]             information about the number of tapers per original trial
           freq: 6,                        the frequency of the oscillations at which the activity is estimated
         method: 'singletrial'             specifies how the data is represented
            cfg: [1x1 struct]              configuration structure used by the invoking FieldTrip function
          trial: [10x1 struct]             contain the numeric data, each structure source.trial(x) can look like this

                 source.trial(1)
                   pow: [6732x1 double]    Npositions x 1 array containing the power at each source location for the given trial
                 noise: [6732x1 double]    Npositions x 1 array containing an estimate of the noise at each source location
                   csd: {6732x1 cell}      Npositions x 1 cell-array containing the source cross-spectral density
                                             at each source location

### New style

This is the new definition of a data structure that represents data corresponding to locations in 3-D space. In the future this will replace the 'old style' definition. It has been designed to be more flexible and more easy to manage. Also, exchange with other software toolboxes and code development should be facilitated by this. An example of such a source structure obtained after performing a frequency domain source reconstruction is shown here:

            pos: [6732x3 double]       positions at which the source activity could have been estimated
         inside: [6732x1 logical]      logical vector of positions at which the source activity is actually estimated

            dim: [xdim ydim zdim]      if the positions can be described as a regularly spaced 3D grid, this contains the
                                         dimensionality of the 3D volume
            vol: [1x1 struct]          volume conductor model
      cumtapcnt: [120x1 double]        information about the number of tapers per original trial
           freq: 6                     the frequency of the oscillations at which the activity is estimated
         method: 'singletrial'         specifies how the data is represented
            cfg: [1x1 struct]          configuration structure used by the invoking FieldTrip function
            pow: [6732x120 double]     the numeric data
      powdimord: 'pos_rpt'             defines how the numeric data has to be interpreted, in this case
                                         6732 dipole positions x 120 observations
