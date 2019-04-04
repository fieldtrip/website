---
title: What dataformats are supported?
tags: [faq, dataformat, preprocessing, raw]
---

# What dataformats are supported?

FieldTrip has a flexible way of supporting data formats. It uses a number of functions that provide a common interface to all electrophysiological (EEG/MEG) file formats: **[ft_read_header](/reference/ft_read_header)**, **[ft_read_data](/reference/ft_read_data)** and **[ft_read_event](/reference/ft_read_event)**. Where needed, these functions will call the appropriate low-level functions for each file format. Some of the low-level functions are written by ourselves, others are supplied by the manufacturers and again others are obtained from other open source toolboxes. You can find more technical information on the reading functions on [this](/development/module/fileio) page.

Here is a summary of the data formats that are supported by FieldTrip. Below you can find more details on some of the formats, especially regarding the MEG systems and their auxiliary files (e.g. MRI and volume conduction models). We regularly implement new data formats and this documentation may be out of date, so if yours is not listed here, please check the code.

The following MEG data formats are supported by **[ft_read_header](/reference/ft_read_header)**, **[ft_read_data](/reference/ft_read_data)** and **[ft_read_event](/reference/ft_read_event)**

- [CTF](/getting_started/ctf) (.ds, .res4, .meg4)
- [Neuromag/Elekta](/getting_started/neuromag) (.fif)
- [BTi/4D](/getting_started/bti) (.m4d, .pdf, .xyz, and 4D's raw data files)
- [Yokogawa/Ricoh](/getting_started/yokogawa) (.ave, .con, .raw)
- ITAB
- Tristan BabySquid

The following EEG data formats are supported by **[ft_read_header](/reference/ft_read_header)**, **[ft_read_data](/reference/ft_read_data)** and **[ft_read_event](/reference/ft_read_event)**

- [ANT Neuro](/getting_started/antneuro) (.avr, .cnt, .trg)
- [Biosemi BDF](/getting_started/biosemi) (.bdf)
- CED - Cambridge Electronic Design (. smr)
- [Electrical Geodesics, Inc. (EGI)](/getting_started/egi) (.egis, .ave, .gave, .ses, .raw, Meta File Format (mff))
- BESA (.avr, .swf)
- EEGLAB (.set)
- NeuroScan (.eeg, .cnt, .avg)
- Nexstim (.nxe)
- [BrainVision](/getting_started/brainvision) (.eeg, .seg, .dat, .vhdr, .vmrk)
- TMSi (.Poly5)
- generic standard formats (.edf, .gdf)

The following EEG/MEG sensor formats are supported by **[ft_read_sens](/reference/ft_read_sens)**

- ASA electrode file
- FCDC Polhemus
- FIL Polhemus
- BESA positions (numeric file with accompanying .elp and .ela)
- BESA sfp
- MEG systems (CTF, Elekta/Neuromag, Yokogawa, 4D/BTi)
- SPM8 EEG

The following spike and LFP data formats are supported by **[ft_read_spike](/reference/ft_read_spike)** and **[ft_read_data](/reference/ft_read_data)**

- [Plexon](/getting_started/plexon) (.nex, .plx, .ddt)
- [Neuralynx](/getting_started/neuralynx) (.ncs, .nse, .nts, .nev, .nrd, .dma, .log)
- CED - Cambridge Electronic Design (.smr)
- MPI - Max Planck Institute (.dap)
- Windaq (.wdq)

The following NIRS data formats are supported by **[ft_read_header](/reference/ft_read_header)** and **[ft_read_data](/reference/ft_read_data)**

- ASCII-formatted data from the NIRS system from Birkbeck college, London (.txt)
- Artinis Medical Systems (.oxy3)

The following eye-tracker data formats are supported by **[ft_read_header](/reference/ft_read_header)** and **[ft_read_data](/reference/ft_read_data)**

- EyeLink - SR Research (.asc)

The following anatomical MRI data formats are supported by **[ft_read_mri](/reference/ft_read_mri)**

- nifti (.nii / .nii.gz), using the FreeSurfer toolbox
- mgz (.mgz), using the FreeSurfer toolbox
- Analzye (.hdr, .img), using the SPM toolbox
- MINC (.mnc), using the SPM toolbox
- CTF (.mri)
- ASA (.mri, .iso)
- DICOM (.ima)

The following surface and volume mesh formats are supported by **[ft_read_headshape](/reference/ft_read_headshape)**

- Generic meshes (.stl, .off)
- Visualisation Toolkit (.vtk)
- Tetgen
- BrainVista
- gifti
- Caret
- FreeSurfer
- BrainSuite
- Wavefront .obj

## See also

{% include seealso tag1="faq" tag2="dataformat" %}
