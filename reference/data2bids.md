---
layout: default
---

##  DATA2BIDS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help data2bids".

`<html>``<pre>`
    `<a href=/reference/data2bids>``<font color=green>`DATA2BIDS`</font>``</a>` is a helper function to convert MEG, EEG, iEEG or anatomical MRI data to
    the Brain Imaging Data Structure. This function starts from an existing dataset on
    disk and creates the required sidecar files. The overall idea is that you would
    write a MATLAB script in which you call this function multiple times, once for each
    of the data files. For each data file it will write the corresponding JSON file.
    When operating on MEG data files, it will also write a corresponding channels.tsv
    and events.tsv file.
 
    Use as
    data2bids(cfg)
    or as
    data2bids(cfg, data)
 
    The first input argument "cfg" is the configuration structure, which contains the
    details for the (meta)data and which specifies the sidecar files you want to write.
    The optional "data" argument corresponds to preprocessed raw data according to
    FT_DATAYPE_RAW or an anatomical MRI according to FT_DATAYPE_VOLUME. The optional
    data argument allows you to write a preprocessed and realigned anatomical MRI to
    disk, or to write a preprocessed electrophysiological dataset to disk.
 
    The configuration structure should contains
    cfg.dataset               = string, filename of the input data
    cfg.outputfile            = string, optional filename for the output data, see below
    cfg.anat.writesidecar     = string, 'yes' or 'no' (default = 'yes')
    cfg.anat.dicomfile        = string, filename of a matching DICOM file
    cfg.meg.writesidecar      = string, 'yes' or 'no' (default = 'yes')
    cfg.eeg.writesidecar      = string, 'yes' or 'no' (default = 'yes')
    cfg.ieeg.writesidecar     = string, 'yes' or 'no' (default = 'yes')
    cfg.channels.writesidecar = string, 'yes' or 'no' (default = 'yes')
    cfg.events.writesidecar   = string, 'yes' or 'no' (default = 'yes')
    cfg.events.trl            = trial definition, see below
 
    If you specify cfg.dataset without cfg.outputfile, this function will only
    construct and write the appropriate sidecar files matching the header details that
    it will get from the dataset. If you also specify cfg.outputfile, this function
    will furthermore read the data from the input dataset, convert it and write it to
    the output dataset.
 
    The output format is NIFTI for anatomical MRIs, and BrainVision for EEG and iEEG.
    Note that in principle you can also convert MEG data to BrainVision, but that is
    not recommended.
 
    You can specify cfg.anat.dicomfile in combination with a NIFTI anatomical MRI. This
    will cause the detailled header information with MR scanner ans sequence details to
    be read from the DICOM file and used to fill in the details of the JSON file.
 
    You can specify cfg.events.trl as a Nx3 matrix with the trial definition (see
    `<a href=/reference/ft_definetrial>``<font color=green>`FT_DEFINETRIAL`</font>``</a>`) or as a MATLAB table. When specified as table, the first three
    columns containing integer values corresponding to the begsample, endsample and
    offset, the additional colums can be of another type and can have any name. If you
    do not specify the trial definition, the events will be read from the dataset and
    used.
 
    General options that apply to all data types are
    cfg.TaskName                    = string
    cfg.InstitutionName             = string
    cfg.InstitutionAddress          = string
    cfg.InstitutionalDepartmentName = string
    cfg.Manufacturer                = string
    cfg.ManufacturersModelName      = string
    cfg.DeviceSerialNumber          = string
    cfg.SoftwareVersions            = string
 
    General options that apply to all functional data types are
    cfg.TaskDescription             = string
    cfg.Instructions                = string
    cfg.CogAtlasID                  = string
    cfg.CogPOID                     = string
 
    There are many more datatype specific options for the JSON files than can be listed
    here. Please open this function in the MATLAB editor to see what those are.
 
    Example with a CTF dataset on disk
    cfg = [];
    cfg.dataset                     = 'sub-01_ses-meg_task-language_meg.ds';
    cfg.TaskName                    = 'language';
    cfg.meg.PowerLineFrequency      = 50;
    cfg.InstitutionName             = 'Radboud University';
    cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
    data2bids(cfg)
 
    Example with an anatomical MRI on disk
    cfg = [];
    cfg.dataset                     = 'sub-01_ses-mri_T1w.nii';
    cfg.anat.dicomfile              = '00080_1.3.12.2.1107.5.2.43.66068.2017082413175824865636649.IMA'
    % cfg.anat.MagneticFieldStrength  = 3; % this is not needed, as it will be obtained from the DICOM file
    cfg.InstitutionName             = 'Radboud University';
    cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
    data2bids(cfg)
 
    Example with a NeuroScan EEG dataset on disk that needs to be converted
    cfg = [];
    cfg.dataset                     = 'subject01.cnt';
    cfg.outputfile                  = 'sub-001_task-visual.vhdr';
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
    cfg.outputfile                  = 'sub-001_task-visual.vhdr';
    cfg.InstitutionName             = 'Radboud University';
    cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
    data2bids(cfg, data)
 
    Example with realigned and resliced anatomical MRI data in memory
    cfg = [];
    cfg.outputfile                  = 'sub-01_ses-mri_T1w.nii';
    cfg.anat.MagneticFieldStrength  = 3;
    cfg.InstitutionName             = 'Radboud University';
    cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
    data2bids(cfg, mri)
 
    This function tries to correspond to version 1.1.0 of the BIDS specification.
    See http://bids.neuroimaging.io/ for further details.
`</pre>``</html>`

