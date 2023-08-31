### Free toolboxes

Besides the non-free MathWorks toolboxes that are used by some functions, FieldTrip also makes use of other free toolboxes for certain functionality, such as access to specific file formats. Using these external toolboxes allows us to focus on specifically improving FieldTrip and to join forces with other open source software projects. Whether you need these non-commercial external toolboxes depends on the data formats that you will use and whether you want to use their specific functionality. Most of these are also developed as open source projects and they all can be downloaded from the internet. Some of them are not open source, but can be redistributed in compiled form (e.g., mex files, p-files, compiled binaries). There are also certain toolboxes that FieldTrip functions can use, but which have even more strict copyright restrictions attached (e.g., signing a Non-Disclosure Agreement) and hence we are not able to redistribute.

A number of external toolboxes is included in the `fieldtrip/external` subdirectory. These include

- [afni](http://afni.nimh.nih.gov/afni/matlab) to read AFNI data
- artinis to read Artinis fNIRS data
- bayesFactor
- [bci2000](http://bci2000.org/) to read BCI200 data
- bct
- bemcp for forward EEG modeling using BEM
- [besa](http://besa.de/) to read BESA data
- [biosig](http://biosig.sourceforge.net/) to read various EEG file formats
- [brainstorm](http://neuroimage.usc.edu/brainstorm/)
- brewermap
- bsmart
- cca
- cmocean
- comm
- ctf to read CTF data
- dipoli for forward EEG modeling using BEM
- dss
- duneuro
- [eeglab](http://sccn.ucsd.edu/eeglab/) for independent component analysis
- [eeprobe](http://www.ant-neuro.com/products/eeprobe) to read ANT-Neuro data
- egi_mff_v2
- ezc3d
- [fastica](http://research.ics.tkk.fi/ica/fastica/) for independent component analysis
- [fileexchange](https://www.mathworks.com/matlabcentral/fileexchange) various functions from Mathworks File Exchange
- fns
- freesurfer to read MRI data
- gcmi
- gifti
- gtec
- homer3 to read fNIRS data
- ibtb
- icasso
- iso2mesh for operations on triangulated surface meshes
- itab
- jsonlab
- lagextraction
- mars
- matplotlib
- mffmatlabio to read EGI data
- mne to read Neuromag/Elekta/MEGIN data
- mrtrix
- netcdf
- neurone
- neuroscope
- neuroshare
- npmk
- [openmeeg](https://openmeeg.github.io) for BEM head modeling
- plot2svg
- ricoh_meg_reader to read data from the Ricoh MEG system
- simbio for forward EEG modeling using FEM
- [spm12, spm8 and spm2](http://www.fil.ion.ucl.ac.uk/spm/software/spm2/) to read some MRI formats, for spatial normalization and segmentation
- sqdproject
- vgrid
- videomeg
- wavefront
- xdf
- xml4mat
- yokogawa to read data from the Yokogawa MEG system
- yokogawa_meg_reader to read data from the Yokogawa MEG system

Although we distribute these toolboxes along with FieldTrip to facilitate their use, we do not develop or support these ourselves. Each of the corresponding toolboxes has its own license agreement, and in the corresponding directories you can find more information on who is responsible for their maintenance and support.

### Optional toolboxes

The following toolboxes are also used for specific computations, but are not included in the default FieldTrip release. You can download them separately and place them in the `fieldtrip/external` directory (where they will be automatically found) or anywhere else on your path.

- nlxnetcom
- meg-pd
- meg-calc
- tcp_udp_ip
