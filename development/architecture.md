---
title: Modular organization of the source code
tags: [development]
---

# Modular organization of the source code

The source code in the FieldTrip toolbox is split over multiple directories, which reflect its modular organization. Furthermore, the directories have specific dependencies on each other, and additions to FieldTrip should follow this structure.

{% include image src="/assets/img/development/module/modules-general.png" %}

The main directory of FieldTrip and the different modules contain high-level functions that are publicly available for the end-user. The functionality of the functions within these directories often depends on low-level functions that are not available for the end-user and are stored in so-called private directories. Some of the module directories are shared with other open source MATLAB toolboxes.

All high-level functions within the FieldTrip directories may call functions within the same directory, from other directories at the same hierarchical level, or directories lower in the hierarchy. But, low-level functions should not call high-level functions. There is an exception for the utilities directory which allows lower-level functions to be called by the end-user at the level of the main FieldTrip functions.

## Modules that act as sub-toolboxes

There are some low-level modules in FieldTrip that have a consistent API and are fully self-contained, i.e. if you copy the corresponding directory out of the main FieldTrip directory, they will still work.

- [fileio](/development/module/fileio) import various EEG/MEG file formats into MATLAB
- [forward](/development/module/forward) volume conduction models for forward computation
- [inverse](/development/module/inverse) inverse computation of source reconstruction
- [preproc](/development/module/preproc) preprocessing of EEG/MEG data, such as filtering and detrending
- [specest](/development/module/specest) estimation of spectral content of EEG/MEG data
- [connectivity](/development/module/connectivity) computation of connectivity measures
- [plotting](/development/module/plotting) low-level functions for plotting and graphical user interfaces

## Toolboxes for distributed computing

Besides the MathWorks Distributed Computing Toolbox, FieldTrip includes three options that you can use for distributed computing. These range from small to large scale distributed computing. Note that FieldTrip does not automatically distribute the workload; you have to implement the distributed computing in your own analysis scripts.

- [engine](/development/module/engine) distributed computing on a (massive) multi-core computer
- [peer](/development/module/peer) distributed computing on an ad-hoc multi-core and/or multi-node peer-to-peer cluster
- [qsub](/development/module/qsub) distributed computing on a Torque, Slurm or SGE cluster
