---
title: Software architecture
tags: [development]
redirect_from:
  - /development/module/
---

# Software architecture

{% include markup/skyblue %}
The **[ft_examplefunction](/reference/ft_examplefunction)** provides a documented walkthrough of a typical high-level FieldTrip function that demonstrates a lot of the features presented below.
{% include markup/end %}

## Consistent configuration and backward compatibility

High-level FieldTrip functions take the `cfg` structure as first input argument which specifies how the function and/or algorithms will behave. Over the course of time time and when new methods and options are introduced, the available configuration options change. We use the **[ft_checkconfig](/reference/utilities/ft_checkconfig)** function at the start of all high-level FieldTrip functions to detect whether the user-specified cfg options are correct, give warnings if deprecated options are being used, and try to update old cfg options when these are for example used in an older analysis script.

## Consistent data and backward compatibility

High-level FieldTrip functions take [data structures](/development/datastructure) as input and/or return similar data structures. Due to new scientific and programming insights, these data structures change over time. In the **[ft_datatype](/reference/utilities/ft_datatype)** function we list all data types and link to the respective `ft_datatype_xxx` functions that define the specification of each structure, including the historical changes.

We use the **[ft_checkdata](/reference/utilities/ft_checkdata)** function at the start of all high-level FieldTrip functions to check internal consistency and - where needed and possible - to update the data structure to the latest standards. When researchers store or archive FieldTrip data structures in `.mat` files on disk and reuse them (much) later, the **[ft_checkdata](/reference/utilities/ft_checkdata)** call will update them.

## High-level, low-level and private functions

Users mainly use the high-level functions (which take a cfg argument) as the main building blocks in their [analysis scripts](/tutorial/intro/introduction).

The low-level utility functions can sometimes be handy as well in an analysis pipeline. The low-level algorithmic functions in the [modules](/development/architecture/#modular-organization) are accessible on the path but not meant to be used by regular experimental neuroscience researchers.

Finally, we have [private](/faq/matlab/privatefunctions_why) functions that by design cannot be called by the end-user.

## Modular organization

The source code in the FieldTrip toolbox is split over multiple directories, which reflect its modular organization. Furthermore, the directories have specific dependencies on each other, and additions to FieldTrip should follow this structure.

{% include image src="/assets/img/development/module/modules-general.png" %}

The main directory of FieldTrip and the different modules contain high-level functions that are publicly available for the end-user. The functionality of the functions within these directories often depends on low-level functions that are not available for the end-user and are stored in so-called private directories. Some of the module directories are shared with other open source MATLAB toolboxes.

All high-level functions within the FieldTrip directories may call functions within the same directory, from other directories at the same hierarchical level, or directories lower in the hierarchy. But, low-level functions should not call high-level functions. There is an exception for the utilities directory which allows lower-level functions to be called by the end-user at the level of the main FieldTrip functions.

We aim for the low-level modules in FieldTrip that they have a consistent API and are fully self-contained, i.e. if you copy the corresponding directory out of the main FieldTrip directory, they should still work. This facilitates the low+level code to be reused in other projects.

- [fileio](/development/module/fileio) import various EEG/MEG file formats into MATLAB
- [forward](/development/module/forward) volume conduction models for forward computation
- [inverse](/development/module/inverse) inverse computation of source reconstruction
- [preproc](/development/module/preproc) preprocessing of EEG/MEG data, such as filtering and detrending
- [specest](/development/module/specest) estimation of spectral content of EEG/MEG data
- [connectivity](/development/module/connectivity) computation of connectivity measures
- [plotting](/development/module/plotting) low-level functions for plotting and graphical user interfaces

## Pre- and postamble

The high-level functions (which take a cfg argument) mainly do data bookkeeping and subsequently pass the data over to the algorithms in the low-level functions. There are a number of features in the bookeeping that are always the same, hence these are shared over all high-level functions using the **[ft_preamble](/reference/utilities/ft_preamble)** and **[ft_postamble](/reference/utilities/ft_postamble)** functions, which are called at the start and end, respectively.

The pre- and postamble functions are implemented such that they execute a (private) script in the callers workspace, which means that these pre- and postamble scripts share the same workspace as the calling functions.

At the start of the high-level functions the preamble scripts ensure that the MATLAB path is set up correctly, that the notification system is initialized, that errors can be more easily debugged, that input data is read and provenance tracked.

At the end of the high-level functions the preamble scripts among others take care of debugging, handle the provenance and save the output data.
