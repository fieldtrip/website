---
title: MEG dataformats
tags: [dataformat, meg, ctf, neuromag, 4d, yokogawa]
---

## Support for CTF MEG data

Initially the reading functions for CTF files were implemented from scratch by the FieldTrip developers. However, in 2008 we switched to the reading functions that are provided (but not officially maintained) by CTF. The new CTF reading functions are located in the external/ctf directory and will be automatically called by the appropriate FieldTrip functions.

The following data files can be read and used in FieldTrip: .meg4, .res4, .mri, .hdm, ClassFile.cls, MarkerFile.mrk. All required CTF reading functions are supplied with the FieldTrip toolbox.

You may want to continue reading the section on [getting started with CTF](/getting_started/meg/ctf).

## Support for Neuromag/Elekta/Megin MEG data

All Neuromag/Elekta/MEGIN data stored in .fif files, where the files can contain different data objects. The following data objects can be read and used in FieldTrip: MEG data, EEG data, gradiometer positions, single sphere models, BEM models (using the MEG-CALC toolbox). FieldTrip reads Neuromag fif files using low-level MATLAB functions from the MNE toolbox from Matti Hämäläinen, see [MNE software](http://www.nmr.mgh.harvard.edu/martinos/userInfo/data/MNE_register/index.php). This will work on any platform, as it is based on open source m-files.

Alternative support for Neuromag data is implemented by calling the mex files from [Kimmo Uutela's MEG-PD toolbox](http://www.kolumbus.fi/kuutela/programs/meg-pd/). The files in the MEG-PD toolbox are not included with FieldTrip, but you can download them[here](http://www.kolumbus.fi/kuutela/programs/meg-pd/). Extract the toolbox and put it on your MATLAB path, or copy the files into the "fieldtrip/private" directory. This is used if you select the file format as "neuromag_fif".

Note that the MEG-PD toolbox will only function on 32-bit machines, and requires either a Linux or HP-UX system to run. As the mex files are compiled code, it is not possible to modify these to run on 64-bit machines (which are becoming increasingly common), at present.

You may want to continue reading the section on [getting started with Neuromag](/getting_started/meg/neuromag).

## Support for BTi/4D MEG data

The recommended way of working with BTi/4D data is to work on the raw data files directly. The code for reading header information from the raw files is based on Eugene Kronberg's "msi2matlab" tools, and have been further developed by Gavin Paterson and Jan-Mathijs Schoffelen, at CCNi.

Alternatively, you can work with BTi/4D data using intermediate ASCII files (.m4d and .xyz), created with "pdf2set", which is a c-program linked to the 4D libraries. This "pdf2set" program should be available to all BTi/4D users.

All the required BTi/4D reading functions for MATLAB are supplied with the FieldTrip toolbox.

You may want to continue reading the section on [getting started with BTi/4D](/getting_started/meg/bti).

## Support for Yokogawa MEG data

The datafiles for the 64-, 160- and 440-channel Yokogawa MEG systems are supported by using the precompiled (i.e. closed source) p-files that are supplied by Yokogawa. The data in the following files can be read and used in FieldTrip: .sqd, .ave, .con, .raw. Furthermore, gradiometer positions and orientations are read from the header.

The low-level MATLAB reading functions are included in the FieldTrip release. Note that these files are not open source and **not covered by the GPL license**, but they are copyrighted by Yokogawa.

You may want to continue reading the section on [getting started with Yokogawa](/getting_started/meg/yokogawa).
