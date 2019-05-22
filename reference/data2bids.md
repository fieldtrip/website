---
title: data2bids
---
```
 DATA2BIDS is a helper function to convert MEG, EEG, iEEG or anatomical MRI data to
 the Brain Imaging Data Structure.

 The overall idea is that you write a MATLAB script in which you call this
 function multiple times, once for each data files. For each data file it will
 write the corresponding JSON file. For MEG/EEG/iEEG data files it will also
 write the corresponding _channels.tsv and _events.tsv file.

 Use as
   data2bids(cfg)
 or as
   data2bids(cfg, data)

 The first input argument 'cfg' is the configuration structure, which contains the
 details for the (meta)data and which specifies the sidecar files you want to write.
 The optional 'data' argument corresponds to preprocessed raw data according to
 FT_DATAYPE_RAW or an anatomical MRI according to FT_DATAYPE_VOLUME. The optional
 data argument allows you to write a preprocessed and realigned anatomical MRI to
 disk, or to write a preprocessed electrophysiological dataset to disk.

 The configuration structure should contains
   cfg.method                  = string, can be 'decorate', 'convert' or 'copy', see below (default = 'convert')
   cfg.dataset                 = string, filename of the input data
   cfg.outputfile              = string, optional filename for the output data
   cfg.mri.deface              = string, 'yes' or 'no' (default = 'no')
   cfg.mri.writesidecar        = string, 'yes', 'replace', 'merge' or 'no' (default = 'yes')
   cfg.meg.writesidecar        = string, 'yes', 'replace', 'merge' or 'no' (default = 'yes')
   cfg.eeg.writesidecar        = string, 'yes', 'replace', 'merge' or 'no' (default = 'yes')
   cfg.ieeg.writesidecar       = string, 'yes', 'replace', 'merge' or 'no' (default = 'yes')
   cfg.events.writesidecar     = string, 'yes', 'replace', 'merge' or 'no' (default = 'yes')
   cfg.coordystem.writesidecar = string, 'yes', 'replace', 'merge' or 'no' (default = 'yes')
   cfg.channels.writesidecar   = string, 'yes', 'replace', 'merge' or 'no' (default = 'yes')

 This function in general starts from existing data file on disk or from a FieldTrip
 compatible data structure in MATLAB memory that is passed as second input argument.
 Depending on cfg.method it will add the sidecar files, copy the dataset and add
 sidecar files, or convert the dataset and add the sidecar files. Each of the
 methods is discussed here.

 DECORATE - data2bids will read the header and event details from the data and write
 the appropriate sidecar files alongside the existing dataset. You would use this to
 obtain the sidecar files for a dataset that already has the correct BIDS name.

 CONVERT - data2bids will read the data from the input data file and write it to a
 new output file that is BIDS compliant. The output format is NIFTI for MRI data,
 and BrainVision for EEG and iEEG. MEG data files are stored in BIDS in their native
 format and this function will NOT convert or rename them for you.

 COPY - data2bids will copy the data from the input data file to the output data
 file, which renames it but does not change its content. Furthermore, it will read
 the header and event details from the data and construct the appropriate sidecar
 files.

 Although you can explicitly specify cfg.outputfile yourself, it is recommended to
 use the following configuration options. This results in a BIDS compliant output
 directory and file name. When specifying these options, data2bids will also write
 or update the participants.tsv and the scans.tsv files.
   cfg.bidsroot                = string, top level directory for the BIDS output
   cfg.sub                     = string, subject name
   cfg.ses                     = string, optional session name
   cfg.run                     = number, optional
   cfg.task                    = string, task name is required for functional data
   cfg.datatype                = string, can be any of 'FLAIR', 'FLASH', 'PD', 'PDT2', 'PDmap', 'T1map', 'T1rho', 'T1w', 'T2map', 'T2star', 'T2w', 'angio', 'bold', 'bval', 'bvec', 'channels', 'coordsystem', 'defacemask', 'dwi', 'eeg', 'epi', 'events', 'fieldmap', 'headshape', 'ieeg', 'inplaneT1', 'inplaneT2', 'magnitude', 'magnitude1', 'magnitude2', 'meg', 'phase1', 'phase2', 'phasediff', 'photo', 'physio', 'sbref', 'stim'
   cfg.acq                     = string
   cfg.ce                      = string
   cfg.rec                     = string
   cfg.dir                     = string
   cfg.mod                     = string
   cfg.echo                    = string
   cfg.proc                    = string

 When specifying the output directory in cfg.bidsroot, you can also specify
 additional information that will be added to the participants.tsv and the scans.tsv
 files. For example
   cfg.participant.age         = scalar
   cfg.participant.sex         = string, 'm' or 'f'
   cfg.scan.acq_time           = string, should be formatted according to  RFC3339 as '2019-05-22T15:13:38'
 In case any of these values is specified as empty (i.e. []) or as nan, it will be
 written to the tsv file as 'n/a'.

 You can specify cfg.mri.dicomfile in combination with a NIFTI file. This will
 read the detailed header information (MR scanner and sequence details) from
 the DICOM file and used to fill in the details of the JSON file.
   cfg.mri.dicomfile           = string, filename of a matching DICOM file for header details (default = [])

 You can specify cfg.events.trl as a Nx3 matrix with the trial definition (see
 FT_DEFINETRIAL) or as a MATLAB table. When specified as table, the first three
 columns containing integer values corresponding to the begsample, endsample and
 offset, the additional colums can be of another type and can have any name. If you
 do not specify the trial definition, the events will be read from the MEG/EEG/iEEG
 dataset.
   cfg.events.trl              = trial definition, see below

 You can specify cfg.presentationfile with the name of a NBS presentation log file,
 which will be aligned with the data based on triggers (MEG/EEG/iEEG) or based on
 the volumes (fMRI). To indicate how triggers (in MEG/EEG/iEEG) or volumes (in fMRI)
 match the presentation events, you should also specify the mapping between them.
   cfg.presentationfile        = string, optional filename for the presentation log file
   cfg.trigger.eventtype       = string (default = [])
   cfg.trigger.eventvalue      = string or number
   cfg.presentation.eventtype  = string (default = [])
   cfg.presentation.eventvalue = string or number
   cfg.presentation.skip       = 'last'/'first'/'none'

 General BIDS options that apply to all data types are
   cfg.TaskName                    = string
   cfg.InstitutionName             = string
   cfg.InstitutionAddress          = string
   cfg.InstitutionalDepartmentName = string
   cfg.Manufacturer                = string
   cfg.ManufacturersModelName      = string
   cfg.DeviceSerialNumber          = string
   cfg.SoftwareVersions            = string

 General BIDS options that apply to all functional data types are
   cfg.TaskDescription             = string
   cfg.Instructions                = string
   cfg.CogAtlasID                  = string
   cfg.CogPOID                     = string

 There are many more BIDS options for the JSON files for specific datatypes. Rather
 than listing them here in the help, please open this function in the MATLAB editor,
 and scroll down a bit to see what those are.

 Example with a CTF dataset on disk that needs no conversion
   cfg = [];
   cfg.method                      = 'decorate';
   cfg.dataset                     = 'sub-01_ses-meg_task-language_meg.ds';
   cfg.TaskName                    = 'language';
   cfg.meg.PowerLineFrequency      = 50;
   cfg.InstitutionName             = 'Radboud University';
   cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
   data2bids(cfg)

 Example with an anatomical MRI on disk that needs no conversion
   cfg = [];
   cfg.method                      = 'decorate';
   cfg.dataset                     = 'sub-01_ses-mri_T1w.nii';
   cfg.mri.dicomfile               = '00080_1.3.12.2.1107.5.2.43.66068.2017082413175824865636649.IMA'
   cfg.mri.MagneticFieldStrength   = 3; % this is usually not needed, as it will be obtained from the DICOM file
   cfg.InstitutionName             = 'Radboud University';
   cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
   data2bids(cfg)

 Example with a NeuroScan EEG dataset on disk that needs to be converted
   cfg = [];
   cfg.method                      = 'convert';
   cfg.dataset                     = 'subject01.cnt';
   cfg.outputfile                  = 'sub-001_task-visual_eeg.vhdr';
   cfg.InstitutionName             = 'Radboud University';
   cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
   data2bids(cfg)

 Example with preprocessed EEG data in memory
   cfg = [];
   cfg.dataset                     = 'subject01.cnt';
   cfg.bpfilter                    = 'yes';
   cfg.bpfreq                      = [0.1 40];
   data = ft_preprocessing(cfg);
   cfg = [];
   cfg.method                      = 'convert';
   cfg.outputfile                  = 'sub-001_task-visual_eeg.vhdr';
   cfg.InstitutionName             = 'Radboud University';
   cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
   data2bids(cfg, data)

 Example with realigned and resliced anatomical MRI data in memory
   cfg = [];
   cfg.method                      = 'convert';
   cfg.outputfile                  = 'sub-01_ses-mri_T1w.nii';
   cfg.mri.MagneticFieldStrength   = 3;
   cfg.InstitutionName             = 'Radboud University';
   cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
   data2bids(cfg, mri)

 This function corresponds to version 1.2 of the BIDS specification. See
 https://bids-specification.readthedocs.io/ for the full specification and
 http://bids.neuroimaging.io/ for further details.
```
