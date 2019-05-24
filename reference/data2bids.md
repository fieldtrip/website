---
title: data2bids
---
```
 DATA2BIDS is a helper function to convert MEG, EEG, iEEG or MRI data to the Brain
 Imaging Data Structure. The overall idea is that you write a MATLAB script in which
 you call this function multiple times, once for each individually recorded data
 file (or data set). It will write the corresponding sidecar JSON and TSV files for
 each data file.

 Use as
   data2bids(cfg)
 or as
   data2bids(cfg, data)

 The first input argument 'cfg' is the configuration structure, which contains the
 details for the (meta)data and which specifies the sidecar files you want to write.
 The optional 'data' argument corresponds to preprocessed raw data according to
 FT_DATAYPE_RAW or an anatomical MRI according to FT_DATAYPE_VOLUME. The optional
 data input argument allows you to write preprocessed electrophysiological data
 and/or realigned and defaced anatomical MRI to disk.

 The configuration structure should contains
   cfg.method                  = string, can be 'decorate', 'convert' or 'copy', see below (default is automatic)
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
   cfg.electrodes.writesidecar = string, 'yes', 'replace', 'merge' or 'no' (default = 'yes')

 This function starts from existing data file on disk or from a FieldTrip compatible
 data structure in MATLAB memory that is passed as the second input argument.
 Depending on cfg.method it will add the sidecar files, copy the dataset and add
 sidecar files, or convert the dataset and add the sidecar files. Each of the
 methods is discussed here.

 DECORATE - data2bids will read the header details and events from the data and write
 the appropriate sidecar files alongside the existing dataset. You would use this to
 obtain the sidecar files for a dataset that already has the correct BIDS name.

 CONVERT - data2bids will read the input data (or use the specified input data) and
 write it to a new output file that is BIDS compliant. The output format is NIFTI
 for MRI data, and BrainVision for EEG and iEEG. Note that MEG data files are stored
 in BIDS in their native format and this function will NOT convert them for you.

 COPY - data2bids will copy the data from the input data file to the output data
 file, which renames it, but does not change its content. Furthermore, it will read
 the header details and events from the data and construct the appropriate sidecar
 files.

 Although you can explicitly specify cfg.outputfile yourself, it is recommended to
 use the following configuration options. This results in a BIDS compliant output
 directory and file name. With these options data2bids will also write, or if
 already present update the participants.tsv and scans.tsv files.
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
 additional information to be added to the participants.tsv and scans.tsv files.
 For example:
   cfg.participant.age         = scalar
   cfg.participant.sex         = string, 'm' or 'f'
   cfg.scan.acq_time           = string, should be formatted according to  RFC3339 as '2019-05-22T15:13:38'
   cfg.dataset_description.
```
