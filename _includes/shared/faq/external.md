### Free toolboxes

Besides the non-free MathWorks toolboxes that are used by some functions, FieldTrip also makes use of other free toolboxes for certain functionality, such as access to specific file formats. Using these external toolboxes allows us to focus on specifically improving FieldTrip and to join forces with other open source software projects. Whether you need these non-commercial external toolboxes depends on the dataformats that you will use and whether you want to use their specific functionality. Most of these are also developed as open source projects and they all can be downloaded from the internet. Some of them are not open source, but can be redistributed in compiled form (e.g. mex files, p-files, compiled binaries). There are also certain toolboxes that FieldTrip can use which have even more strict copyright restrictions attached (e.g. signing a Non-Disclosure Agreement), which we are not allowed to redistribute.

A considerable number of external toolboxes is included in the FieldTrip release zip file inside the "fieldtrip/external" subdirectory. These include

- [afni](http://afni.nimh.nih.gov/afni/matlab) MATLAB functions (to read AFNI data)
- [bci2000](http://bci2000.org/)
- [besa](http://besa.de/)
- [biosig](http://biosig.sourceforge.net/) (to read various EEG file formats)
- [eeglab](http://sccn.ucsd.edu/eeglab/) (only for independent component analysis)
- [eeprobe](http://www.ant-neuro.com/products/eeprobe)
- [fastica](http://research.ics.tkk.fi/ica/fastica/)
- [megdp](http://www.kolumbus.fi/kuutela/programs/meg-pd/) (to read Neuromag fif data)
- [openmeeg](http://www-sop.inria.fr/athena/software/OpenMEEG/)
- [spm2](http://www.fil.ion.ucl.ac.uk/spm/software/spm2/) (to read some MRI formats, for spatial normalization and segmentation)
- [spm8](http://www.fil.ion.ucl.ac.uk/spm/software/spm8/) (to read some MRI formats, for spatial normalization and segmentation)
- ctf (to read CTF data)
- mne (to read Neuromag fif data)
- yokogawa (to read data from the Yokogawa MEG system)
- dipoli (for forward EEG modeling using BEM)
- simbio (for forward EEG modeling using FEM)

Although we distribute these toolboxes along with FieldTrip to facilitate their use, we do not develop or support them. Each of the corresponding toolboxes has its own license agreement, and in the corresponding directories you can find more information on who is responsible for them.

### Optional toolboxes

The following toolboxes are also used for specific computations, but are not included in the default FieldTrip release. You can download them separately and place them in the "fieldtrip/external" directory (where they will be automatically found) or anywhere else on your path.

- nlxnetcom
- meg-pd
- meg-calc
- tcp_udp_ip
