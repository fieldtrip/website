---
title: Combining simultaneous recordings in BIDS
category: example
tags: [bids, sharing]
---

# Combining simultaneous recordings in BIDS

The [BIDS standard](https://bids.neuroimaging.io) describes a simple and easy to adopt way of organizing neuroimaging and behavioral data. When studying cognition and/or behavior in relation to the brain, it is common to use multiple pieces of equipment at the same time. For the offline analysis of the biological activity in the brain in relation to the behaviour, we rely on the equipment recording digital data on disk. Each of the pieces of equipment has its own way of recording data and its own file formats. When we represent all data in BIDS, we combine all these recordings in a uniform fashion to facilitate the interpretation and (re)use of the data.

Here are some pieces of equipment that we use at the Donders Institute _and_ that record data to disk, together with a short description of the data that they record.

- Siemens MRI scanner, DICOM files
- CTF MEG system, dataset consisting of a `.ds` directory with multiple files
- BrainVision EEG/ExG system (see \* below), dataset consisting of a `.vhdr`, `.vmrk` and `.dat` file
- behavioral control software, events in an ascii file with a tabular format
  - NBS Presentation, ascii log files (both standard as `.log` and custom `.txt` files)
  - PsychoPy, custom formatted ascii log files
  - PsychToolbox, custom formatted ascii log files
- motion capture systems for dynamic positions
  - Qualisys, binary data in a proprietary `.qtm` format
  - NDI Optotrak
  - Virtual Reality (VR) setups
  - recording of static positions, e.g., for EEG electrodes
    - Polhemus electromagnetic tracker, ascii file with positions
    - Occipital Structure Sensor, 3D meshes and texture mapping in an `.obj` file
- eye tracker
  - S/R Research Eyelink, binary data in a proprietary `.edf` format
  - Tobii, binary data in a proprietary `.idf` format
  - SMI, binary data in a proprietary `.tgd` format
- audio recordings, one or multiple channels in a `.wav` or `.mp3` file
- video recordings, often with combined audio, in a `.mov`, `.avi` or `.mp4` file
- responses to questionnaires

This list does not cover all pieces of lab equipment, only those that record data on disk for later analysis. Also some types of "measurements" in the lab that do not result immediately in digital data are left out, such as drawing of blood samples, or acquiring DNA material using a cheek swab,

(\*) The BrainVision system cannot only be used for EEG, but also for ECG, EMG, EOG, ERG, and other physiological signals such as GSR, optical pulse sensors for blood flow, high-speed temperature sensors and elastic breathing belts for respiration, etc. Although not all of these correspond to bioelectric signals of nerve or muscle tissue, we will commonly refer to them as ExG recordings.

The data of each of these pieces of equipment can be stored in the BIDS structure, either according to the official specification (currently MRI, MEG, EEG, iEEG, behaviour), or by extending the BIDS specification a bit and storing it in a BIDS-like fashion. In this [example overview page](/example/bids) you can find links to specific examples for converting different types of data and/or organizing it according to BIDS.

The remainder of this example deals with simultaneous recordings and especially how to represent the timing information of those recordings. This excludes recordings with a static (non-time varying) nature, such as structural MRI, but also excludes relatively static information such as questionnaire data, or information about medication.

## Example dataset

The example dataset that we will use here was recorded as part of the [Parkinson op Maat](https://www.parkinsonopmaat.nl) (POM) study. The dataset presented here is limited to only two participants, and only includes the data recorded during the session in the MR lab at the DCCN. Note also that actual data is **not** being shared here; we only present an outline of the data to demonstrate the strategy for organizing the data in BIDS and aligning the timing of the different measurements.

The original collection of data is organized in a directory structure like this.

```bash
original
|-- emg
|-- eyetracker
|-- mri
|   |-- sub-POM1FM0023671
|   |   |-- 001-localizer
|   |   |-- 002-AAHead_Scout_32ch-head-coil
|   |   |-- 003-AAHead_Scout_32ch-head-coil_MPR_sag
|   |   |-- 004-AAHead_Scout_32ch-head-coil_MPR_cor
|   |   |-- 005-AAHead_Scout_32ch-head-coil_MPR_tra
|   |   |-- 006-T1_p2_1mm_fov256_sag_TI_880ukbiobank
|   |   |-- 007-T1_p2_1mm_fov256_sag_TI_880ukbiobank
|   |   |-- 008-MB8_fMRI_fov210_2.4mm_ukbiobank_SBRef
|   |   |-- 009-MB8_fMRI_fov210_2.4mm_ukbiobank
|   |   |-- 010-MB6_fMRI_2.0iso_TR1000TE34
|   |   |-- 011-diff_UkBioBankAdapted_MB3_50b1000_50b2000_8b0_SBRef
|   |   |-- 012-diff_UkBioBankAdapted_MB3_50b1000_50b2000_8b0
|   |   |-- 013-diff_UkBioBankAdapted_MB3_50b1000_50b2000_8b0_SBRef
|   |   |-- 014-diff_UkBioBankAdapted_MB3_50b1000_50b2000_8b0
|   |   |-- 015-diff_UKBioBankAdapted_MB3_inverted_SBRef
|   |   |-- 016-diff_UKBioBankAdapted_MB3_inverted
|   |   |-- 017-3dflair_1mm-serialimagingadapted_ND
|   |   |-- 018-3dflair_1mm-serialimagingadapted
|   |   |-- 019-AlternativeGRE5echos_PFshorter
|   |   |-- 020-AlternativeGRE5echos_PFshorter
|   |   |-- 021-tse_vfl_iso_1mm
|   |   `-- 022-tse_vfl_iso_1mm
|   `-- sub-POM1FM0031237
|       |-- 001-localizer
|       |-- 002-AAHead_Scout_32ch-head-coil
|       |-- 003-AAHead_Scout_32ch-head-coil_MPR_sag
|       |-- 004-AAHead_Scout_32ch-head-coil_MPR_cor
|       |-- 005-AAHead_Scout_32ch-head-coil_MPR_tra
|       |-- 006-T1_p2_1mm_fov256_sag_TI_880ukbiobank
|       |-- 007-T1_p2_1mm_fov256_sag_TI_880ukbiobank
|       |-- 008-MB8_fMRI_fov210_2.4mm_ukbiobank_SBRef
|       |-- 009-MB8_fMRI_fov210_2.4mm_ukbiobank
|       |-- 010-MB6_fMRI_2.0iso_TR1000TE34
|       |-- 011-diff_UkBioBankAdapted_MB3_50b1000_50b2000_8b0_SBRef
|       |-- 012-diff_UkBioBankAdapted_MB3_50b1000_50b2000_8b0
|       |-- 013-diff_UKBioBankAdapted_MB3_inverted_SBRef
|       |-- 014-diff_UKBioBankAdapted_MB3_inverted
|       |-- 015-3dflair_1mm-serialimagingadapted_ND
|       |-- 016-3dflair_1mm-serialimagingadapted
|       |-- 017-AlternativeGRE5echos_PFshorter
|       |-- 018-AlternativeGRE5echos_PFshorter
|       |-- 019-tse_vfl_iso_1mm
|       `-- 020-tse_vfl_iso_1mm
`-- task

48 directories, 12268 files
```

Each of these directories contain either a few files (for emg, eyetracker and task) or many files (for the MR scans).

After converting/reorganizing the data to the BIDS structure using [bidscoin](https://github.com/Donders-Institute/bidscoin) for the MR data and **[data2bids](/reference/data2bids)** for the rest (see below), we obtain the following directory and file structure.

```bash
bids
|-- README
|-- code
|   |-- bidscoin
|   |   |-- bidscoiner.errors
|   |   |-- bidscoiner.log
|   |   |-- bidsmap.yaml
|   |   |-- bidsmapper.errors
|   |   `-- bidsmapper.log
|   |-- bidseditor.log
|   |-- bidsmapper.log
|   `-- convert_to_bids.m
|-- dataset_description.json
|-- participants.json
|-- participants.tsv
|-- sub-POM1FM0023671
|   |-- anat
|   |   |-- sub-POM1FM0023671_acq-3D_run-1_FLAIR.json
|   |   |-- sub-POM1FM0023671_acq-3D_run-1_FLAIR.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE01_rec-magnitude_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE01_rec-magnitude_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE01_rec-phase_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE01_rec-phase_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE02_rec-magnitude_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE02_rec-magnitude_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE02_rec-phase_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE02_rec-phase_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE03_rec-magnitude_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE03_rec-magnitude_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE03_rec-phase_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE03_rec-phase_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE04_rec-magnitude_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE04_rec-magnitude_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE04_rec-phase_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE04_rec-phase_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE05_rec-magnitude_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE05_rec-magnitude_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE05_rec-phase_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE05_rec-phase_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE06_rec-magnitude_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE06_rec-magnitude_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE06_rec-phase_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE06_rec-phase_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE07_rec-magnitude_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE07_rec-magnitude_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE07_rec-phase_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE07_rec-phase_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE08_rec-magnitude_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE08_rec-magnitude_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE08_rec-phase_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE08_rec-phase_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE09_rec-magnitude_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE09_rec-magnitude_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-GREhighresE09_rec-phase_run-1_T2star.json
|   |   |-- sub-POM1FM0023671_acq-GREhighresE09_rec-phase_run-1_T2star.nii.gz
|   |   |-- sub-POM1FM0023671_acq-MPRAGE_rec-norm_run-1_T1w.json
|   |   |-- sub-POM1FM0023671_acq-MPRAGE_rec-norm_run-1_T1w.nii.gz
|   |   |-- sub-POM1FM0023671_acq-TSE_rec-norm_run-1_T2w.json
|   |   `-- sub-POM1FM0023671_acq-TSE_rec-norm_run-1_T2w.nii.gz
|   |-- beh
|   |   |-- sub-POM1FM0023671_task-prac_acq-txt_events.tsv
|   |   |-- sub-POM1FM0023671_task-rest_acq-smi_events.tsv
|   |   |-- sub-POM1FM0023671_task-rest_acq-smi_eyetracker.json
|   |   |-- sub-POM1FM0023671_task-rest_acq-smi_eyetracker.tsv
|   |   |-- sub-POM1FM0023671_task-motor_acq-log_events.tsv
|   |   |-- sub-POM1FM0023671_task-motor_acq-txt_events.tsv
|   |   |-- sub-POM1FM0023671_task-motor_acq-smi_events.tsv
|   |   |-- sub-POM1FM0023671_task-motor_acq-smi_eyetracker.json
|   |   `-- sub-POM1FM0023671_task-motor_acq-smi_eyetracker.tsv
|   |-- dwi
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-1_dwi.bval
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-1_dwi.bvec
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-1_dwi.json
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-1_dwi.nii.gz
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-1_sbref.bval
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-1_sbref.bvec
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-1_sbref.json
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-1_sbref.nii.gz
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-2_dwi.bval
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-2_dwi.bvec
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-2_dwi.json
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-2_dwi.nii.gz
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-2_sbref.bval
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-2_sbref.bvec
|   |   |-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-2_sbref.json
|   |   `-- sub-POM1FM0023671_acq-UkBioBankAdapted_dir-COL_run-2_sbref.nii.gz
|   |-- emg
|   |   |-- sub-POM1FM0023671_task-rest_channels.tsv
|   |   |-- sub-POM1FM0023671_task-rest_emg.eeg
|   |   |-- sub-POM1FM0023671_task-rest_emg.json
|   |   |-- sub-POM1FM0023671_task-rest_emg.vhdr
|   |   |-- sub-POM1FM0023671_task-rest_emg.vmrk
|   |   |-- sub-POM1FM0023671_task-rest_events.tsv
|   |   |-- sub-POM1FM0023671_task-motor_channels.tsv
|   |   |-- sub-POM1FM0023671_task-motor_emg.eeg
|   |   |-- sub-POM1FM0023671_task-motor_emg.json
|   |   |-- sub-POM1FM0023671_task-motor_emg.vhdr
|   |   |-- sub-POM1FM0023671_task-motor_emg.vmrk
|   |   `-- sub-POM1FM0023671_task-motor_events.tsv
|   |-- extra_data
|   |   |-- sub-POM1FM0023671_acq-3D_rec-ND_run-1_FLAIR.json
|   |   |-- sub-POM1FM0023671_acq-3D_rec-ND_run-1_FLAIR.nii.gz
|   |   |-- sub-POM1FM0023671_acq-MPRAGE_run-1_T1w.json
|   |   |-- sub-POM1FM0023671_acq-MPRAGE_run-1_T1w.nii.gz
|   |   |-- sub-POM1FM0023671_acq-TSE_run-1_T2w.json
|   |   `-- sub-POM1FM0023671_acq-TSE_run-1_T2w.nii.gz
|   |-- fmap
|   |   |-- sub-POM1FM0023671_acq-UKBioBankAdaptedSBRef_dir-COL_run-1_epi.json
|   |   |-- sub-POM1FM0023671_acq-UKBioBankAdaptedSBRef_dir-COL_run-1_epi.nii.gz
|   |   |-- sub-POM1FM0023671_acq-UKBioBankAdapted_dir-COL_run-1_epi.json
|   |   `-- sub-POM1FM0023671_acq-UKBioBankAdapted_dir-COL_run-1_epi.nii.gz
|   |-- func
|   |   |-- sub-POM1FM0023671_task-motor_acq-MB6_run-1_bold.json
|   |   |-- sub-POM1FM0023671_task-motor_acq-MB6_run-1_bold.nii.gz
|   |   |-- sub-POM1FM0023671_task-rest_acq-MB8_run-1_bold.json
|   |   |-- sub-POM1FM0023671_task-rest_acq-MB8_run-1_bold.nii.gz
|   |   |-- sub-POM1FM0023671_task-rest_acq-MB8_run-1_sbref.json
|   |   `-- sub-POM1FM0023671_task-rest_acq-MB8_run-1_sbref.nii.gz
|   `-- sub-POM1FM0023671_scans.tsv
`-- sub-POM1FM0031237
    |-- anat
    |   |-- sub-POM1FM0031237_acq-3D_run-1_FLAIR.json
    |   |-- sub-POM1FM0031237_acq-3D_run-1_FLAIR.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE01_rec-magnitude_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE01_rec-magnitude_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE01_rec-phase_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE01_rec-phase_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE02_rec-magnitude_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE02_rec-magnitude_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE02_rec-phase_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE02_rec-phase_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE03_rec-magnitude_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE03_rec-magnitude_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE03_rec-phase_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE03_rec-phase_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE04_rec-magnitude_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE04_rec-magnitude_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE04_rec-phase_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE04_rec-phase_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE05_rec-magnitude_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE05_rec-magnitude_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE05_rec-phase_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE05_rec-phase_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE06_rec-magnitude_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE06_rec-magnitude_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE06_rec-phase_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE06_rec-phase_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE07_rec-magnitude_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE07_rec-magnitude_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE07_rec-phase_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE07_rec-phase_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE08_rec-magnitude_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE08_rec-magnitude_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE08_rec-phase_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE08_rec-phase_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE09_rec-magnitude_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE09_rec-magnitude_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-GREhighresE09_rec-phase_run-1_T2star.json
    |   |-- sub-POM1FM0031237_acq-GREhighresE09_rec-phase_run-1_T2star.nii.gz
    |   |-- sub-POM1FM0031237_acq-MPRAGE_rec-norm_run-1_T1w.json
    |   |-- sub-POM1FM0031237_acq-MPRAGE_rec-norm_run-1_T1w.nii.gz
    |   |-- sub-POM1FM0031237_acq-TSE_rec-norm_run-1_T2w.json
    |   `-- sub-POM1FM0031237_acq-TSE_rec-norm_run-1_T2w.nii.gz
    |-- beh
    |   |-- sub-POM1FM0031237_task-prac_acq-txt_events.tsv
    |   |-- sub-POM1FM0031237_task-rest_acq-smi_events.tsv
    |   |-- sub-POM1FM0031237_task-rest_acq-smi_eyetracker.json
    |   |-- sub-POM1FM0031237_task-rest_acq-smi_eyetracker.tsv
    |   |-- sub-POM1FM0031237_task-motor_acq-log_events.tsv
    |   |-- sub-POM1FM0031237_task-motor_acq-txt_events.tsv
    |   |-- sub-POM1FM0031237_task-motor_acq-smi_events.tsv
    |   |-- sub-POM1FM0031237_task-motor_acq-smi_eyetracker.json
    |   `-- sub-POM1FM0031237_task-motor_acq-smi_eyetracker.tsv
    |-- dwi
    |   |-- sub-POM1FM0031237_acq-UkBioBankAdapted_dir-COL_run-1_dwi.bval
    |   |-- sub-POM1FM0031237_acq-UkBioBankAdapted_dir-COL_run-1_dwi.bvec
    |   |-- sub-POM1FM0031237_acq-UkBioBankAdapted_dir-COL_run-1_dwi.json
    |   |-- sub-POM1FM0031237_acq-UkBioBankAdapted_dir-COL_run-1_dwi.nii.gz
    |   |-- sub-POM1FM0031237_acq-UkBioBankAdapted_dir-COL_run-1_sbref.bval
    |   |-- sub-POM1FM0031237_acq-UkBioBankAdapted_dir-COL_run-1_sbref.bvec
    |   |-- sub-POM1FM0031237_acq-UkBioBankAdapted_dir-COL_run-1_sbref.json
    |   `-- sub-POM1FM0031237_acq-UkBioBankAdapted_dir-COL_run-1_sbref.nii.gz
    |-- emg
    |   |-- sub-POM1FM0031237_task-rest_channels.tsv
    |   |-- sub-POM1FM0031237_task-rest_emg.eeg
    |   |-- sub-POM1FM0031237_task-rest_emg.json
    |   |-- sub-POM1FM0031237_task-rest_emg.vhdr
    |   |-- sub-POM1FM0031237_task-rest_emg.vmrk
    |   |-- sub-POM1FM0031237_task-rest_events.tsv
    |   |-- sub-POM1FM0031237_task-motor_channels.tsv
    |   |-- sub-POM1FM0031237_task-motor_emg.eeg
    |   |-- sub-POM1FM0031237_task-motor_emg.json
    |   |-- sub-POM1FM0031237_task-motor_emg.vhdr
    |   |-- sub-POM1FM0031237_task-motor_emg.vmrk
    |   `-- sub-POM1FM0031237_task-motor_events.tsv
    |-- extra_data
    |   |-- sub-POM1FM0031237_acq-3D_rec-ND_run-1_FLAIR.json
    |   |-- sub-POM1FM0031237_acq-3D_rec-ND_run-1_FLAIR.nii.gz
    |   |-- sub-POM1FM0031237_acq-MPRAGE_run-1_T1w.json
    |   |-- sub-POM1FM0031237_acq-MPRAGE_run-1_T1w.nii.gz
    |   |-- sub-POM1FM0031237_acq-TSE_run-1_T2w.json
    |   `-- sub-POM1FM0031237_acq-TSE_run-1_T2w.nii.gz
    |-- fmap
    |   |-- sub-POM1FM0031237_acq-UKBioBankAdaptedSBRef_dir-COL_run-1_epi.json
    |   |-- sub-POM1FM0031237_acq-UKBioBankAdaptedSBRef_dir-COL_run-1_epi.nii.gz
    |   |-- sub-POM1FM0031237_acq-UKBioBankAdapted_dir-COL_run-1_epi.json
    |   `-- sub-POM1FM0031237_acq-UKBioBankAdapted_dir-COL_run-1_epi.nii.gz
    |-- func
    |   |-- sub-POM1FM0031237_task-motor_acq-MB6_run-1_bold.json
    |   |-- sub-POM1FM0031237_task-motor_acq-MB6_run-1_bold.nii.gz
    |   |-- sub-POM1FM0031237_task-rest_acq-MB8_run-1_bold.json
    |   |-- sub-POM1FM0031237_task-rest_acq-MB8_run-1_bold.nii.gz
    |   |-- sub-POM1FM0031237_task-rest_acq-MB8_run-1_sbref.json
    |   `-- sub-POM1FM0031237_task-rest_acq-MB8_run-1_sbref.nii.gz
    `-- sub-POM1FM0031237_scans.tsv

18 directories, 196 files
```

The anat, dwi, and fmap directories relate to static/structural data. The func, beh and emg directories relate to dynamic data, i.e. data with a time dimension where the participants behavior and physiology are simultaneously recorded, while the subject was executing a task.

## Converting the MRI data to BIDS

The MRI data was converted from DICOM to BIDS using [bidscoin](https://github.com/Donders-Institute/bidscoin). Marcel Zwiers (involved in the POM project and informed about the DICOM sequence details) assisted with the conversion by providing a `.yaml` file.

## Converting the non-MRI data to BIDS

The conversion of the EMG, eye tracker and behavioral data to BIDS uses **[data2bids](/reference/data2bids)** and follows the [other examples](/example/bids) that you can find on this website. Note that in the following code the Presentation files are converted to `_events.tsv` files, but these are not only linked the fMRI data, but also to the EMG and to the eye tracker, and therefore we choose here to place the events in the beh directory, rather than alongside the fMRI in the func directory.

The first part of the code is general metadata/documentation and applies to all data:

```
sourcepath = './original';
targetpath = './bids';

%%

general = [];

general.InstitutionName             = 'Radboud University';
general.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
general.InstitutionAddress          = 'Kapittelweg 29, 6525 EN, Nijmegen, The Netherlands';

% required for dataset_description.json
general.dataset_description.Name                = 'POM - Parkinson op maat';

% optional for dataset_description.json
general.dataset_description.Authors             = 'n/a';
general.dataset_description.DatasetDOI          = 'n/a';
general.dataset_description.License             = 'n/a';
general.dataset_description.Acknowledgements    = 'n/a';
general.dataset_description.Funding             = 'n/a';
general.dataset_description.ReferencesAndLinks  = {'https://www.parkinsonopmaat.nl'};
```

### Converting the EMG files

```
filename = {
 'POM1FM0023671_rest1.vhdr'
 'POM1FM0023671_task1.vhdr'
 'POM1FM0031237_rest1.vhdr'
 'POM1FM0031237_task1.vhdr'
 };

for i=1:numel(filename)
 [p, f, x] = fileparts(filename{i});
 piece = split(f, '_');
 sub  = piece{1};
 task = piece{2}(1:end-1);

 % start by including the general metadata
 cfg = general;
 cfg.dataset = fullfile(sourcepath, 'emg', filename{i});
 cfg.method = 'copy';

 % specify the type and target location
 cfg.bidsroot = targetpath;
 cfg.sub = sub;
 cfg.task = task;
 cfg.datatype = 'emg';

 cfg.participant.age = nan;
 cfg.participant.sex = 'n/a';

 data2bids(cfg);

end
```

### Converting the Presentation custom .txt files

```
filename = {
 'POM1FM0031237_prac1_logfile.txt'
 'POM1FM0023671_prac1_logfile.txt'
 'POM1FM0031237_task1_logfile.txt'
 'POM1FM0023671_task1_logfile.txt'
 };

for i=1:numel(filename)
 [p, f, x] = fileparts(filename{i});
 piece = split(f, '_');
 sub  = piece{1};
 task = piece{2}(1:end-1);

 % start by including the general metadata
 cfg = general;

 % specify the type and target location
 cfg.bidsroot = targetpath;
 cfg.datatype = 'events';
 cfg.sub = sub;
 switch task
 case 'prac1'
   cfg.task = 'prac';
 case 'task1'
   cfg.task = 'motor';
 end
 cfg.acq = 'txt'; % this is needed to distinguish the different recordings of the events

 cfg.writetsv = 'replace';

 % read the ascii log file
 log = readtable(fullfile(sourcepath, 'task', filename{i}));

 % add the onset and duration (both in seconds)
 % the Presentation software uses time stamps of 0.1 milliseconds
 % but these log files appear to be in 1 millisecond steps
 log.onset = (log.Fixation_Time)/1e3;
 log.duration = (log.Response_Time - log.Fixation_Time)/1e3;
 log.duration(log.Response_Time==0) = nan;

 cfg.events = log;
 data2bids(cfg);
end
```

### Converting the Presentation standard .log files

```
filename = {
 'POM1FM0031237_task1-MotorTaskEv_left.log'
 'POM1FM0023671_task1-MotorTaskEv_right.log'
 };

for i=1:numel(filename)
 [p, f, x] = fileparts(filename{i});
 piece = split(f, '_');
 sub = piece{1};

 % start by including the general metadata
 cfg = general;

 cfg.dataset = fullfile(sourcepath, 'task', filename{i});

 % specify the type and target location
 cfg.bidsroot = targetpath;
 cfg.datatype = 'events';
 cfg.sub = sub;
 cfg.task = 'motor';
 cfg.acq = 'log'; % this is needed to distinguish the different recordings of the events

 data2bids(cfg);
end
```

### Converting the SMI eye tracker files

Note that the SMI eye tracker files were first converted from the `.idf` format using the SMI converter software, since the `.idf` files cannot be read in MATLAB nor in most other software.

```
filename = {
 'POM1FM0023671_rest1 Samples.txt'
 'POM1FM0023671_task1 Samples.txt'
 'POM1FM0031237_rest1 Samples.txt'
 'POM1FM0031237_task1 Samples.txt'
 };

for i=1:numel(filename)
 [p, f, x] = fileparts(filename{i});
 f(f==' ') = '_'; % replace spaces in the file name
 piece = split(f, '_');
 sub  = piece{1};
 task = piece{2}(1:end-1);

 % start by including the general metadata
 cfg = general;

 % the ascii file will be convertet to TSV
 cfg.dataset = fullfile(sourcepath, 'eyetracker', filename{i});

 % specify the type and target location
 cfg.bidsroot = targetpath;
 cfg.datatype = 'eyetracker';
 cfg.sub = sub;
 switch task
 case 'rest1'
   cfg.task = 'rest';
 case 'task1'
   cfg.task = 'motor';
 end
 cfg.acq = 'smi'; % this is needed to distinguish the different recordings of the events

 data2bids(cfg);
end
```

## Aligning the time of the different measurements

All measurements that were performed are represented in the `_scans.tsv` file. This is what `sub-POM1FM0031237_scans.tsv` contains for the functional data after the initial conversion to BIDS:

| filename                                                    | acq_time            |
| ----------------------------------------------------------- | ------------------- |
| anat/sub-POM1FM0023671_acq-MPRAGE_rec-norm_run-1_T1w.nii.gz | 1900-01-01T18:50:23 |
| func/sub-POM1FM0023671_task-rest_acq-MB8_run-1_bold.nii.gz  | 1900-01-01T18:57:57 |
| func/sub-POM1FM0023671_task-motor_acq-MB6_run-1_bold.nii.gz | 1900-01-01T19:11:18 |
| emg/sub-POM1FM0023671_task-rest_emg.vhdr                    | n/a                 |
| emg/sub-POM1FM0023671_task-motor_emg.vhdr                   | n/a                 |
| beh/sub-POM1FM0023671_task-prac_acq-txt_events.tsv          | n/a                 |
| beh/sub-POM1FM0023671_task-rest_acq-smi_eyetracker.tsv      | n/a                 |
| beh/sub-POM1FM0023671_task-motor_acq-log_events.tsv         | n/a                 |
| beh/sub-POM1FM0023671_task-motor_acq-txt_events.tsv         | n/a                 |
| beh/sub-POM1FM0023671_task-motor_acq-smi_eyetracker.tsv     | n/a                 |

Contrary to most simple examples of functional MRI data on the [BIDS website](https://bids.neuroimaging.io), where the presentation log file is converted into an `_events.tsv` that is placed besides the functional `_bold.nii.gz` file as a "sidecar", here we represent the behavioral data explicitly in the `beh` folder. This allows the behavioral data to also be expressed in relation to the eyetracker data, or in relation to the EMG data.

{% include markup/yellow %}
We use the strategy that _each recording_ of data to disk is as important as _any other recording_. e.g., for people studying eye movements the eyetracker data is the most important, for people studying tremor the EMG might be the most important, and neuroimaging people would consider the MR data as the most important.

Keeping the different types of data represented symmetrically allows for arbitrary combinations of data to be recorded and investigated, e.g., video in combination with EEG, audio in combination with motion capture, iEEG in combination with MEG, or functional MRI in relation with behavior.

In cognitive or behavioral studies, it is very common to control the experiment using stimulus presentation software that records the timing of stimuli and responses. If during the experiment only one type of physiological data is recorded (e.g., fMRI, EEG, MEG or iEEG) the presentation events can be stored in the `_events.tsv` sidecar file that accompanies the physiological data, and the onset column in the events file should match the time of the corresponding recording. In cases with multiple recordings we recommend representing them separately, which means that behavioral events (stimuli and responses) are in the `beh` folder. The same holds for `physio` recordings in relation to functional MRI.
{% include markup/end %}

For the MR scans the acquisition time has been extracted from the DICOM files. The date of acquisition has been set to 1900-01-01 by [dcm2niix](https://www.nitrc.org/projects/dcm2nii) for privacy reasons, the time of acquisition does correspond to the actual time the scan was performed.

In principle the time of the other recordings could be determined from the original files as well, either by looking at the content of the files or by looking at the file creation time stamps. However, multiple computers were involved in the recording - one for each type of data - and the clocks of those computers are not guaranteed to be accurately synchronized. Furthermore, the interpretation of behavior, emg and eyetracker requires millisecond precision rather than the file system timestamps which is only 1 second precise. In the remainder we will assume that the MR acquisitions started exactly at the indicated time, i.e. at `1900-01-01T18:53:06.000` in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) time format, including milliseconds.

### General handling of time in MATLAB

This is a short demonstration how to deal with dates and times in MATLAB.

```
% MATLAB can describe date+time in a single number, or in a vector
t = now;
% show the current date and time
datestr(t, 'yyyy-mm-ddTHH:MM:SS')
% it is easier to do math when described as a vector
t = datevec(t);
% show the current date and time
datestr(t, 'yyyy-mm-ddTHH:MM:SS')

% let's ignore the milliseconds for now
t(6) = round(t(6));

% show the current date and time, plus one second
datestr(t+[0 0 0 0 0 1], 'yyyy-mm-ddTHH:MM:SS')
% show the current date and time, plus one minute
datestr(t+[0 0 0 0 1 0], 'yyyy-mm-ddTHH:MM:SS')
% show the current date and time, plus 0.5 second
datestr(t+[0 0 0 0 0 0.5], 'yyyy-mm-ddTHH:MM:SS.FFF')
```

### Aligning the resting state datasets

We start with aligning the resting state task, which consists of functional MRI, EMG and eyetracker data.

#### EMG

Looking at the `_events.tsv` files for the EMG recording - which were derived from the trigger channel in the BrainVision recording - we can see that the first `Response` event with value `R 1` happens after about 15 seconds. This indicates that EMG acquisition was started about 15 seconds _prior_ to the MRI scanner being switched on. This is the case for both motor task and resting state EMG recordings, and for both subjects. We can take the onset value of the first `R 1` event and subtract that from the acquisition time of the corresponding functional MRI scan (for 'task-motor' and 'task-rest, respectively).

From the `_scans.tsv` we can get for the start of the functional MRI acquisition

```bash
func/sub-POM1FM0023671_task-rest_acq-MB8_run-1_bold.nii.gz  1900-01-01T18:57:57
```

From the corresponding EMG `_events.tsv` we can get

```bash
14.5752    0.0002    72877    Response    R  1
```

which indicates that the first scan (coded in the EMG recording as response event "R 1") starts 14.5752 seconds _after_ the start of EMG acquisition. The EMG can therefore be aligned with the wall-time clock by means of the MRI triggers

    func_time = datevec('1900-01-01T18:57:57', 'yyyy-mm-ddTHH:MM:SS');
    emg_offset = [0 0 0 0 0 14.5752]; % the EMG starts earlier
    emg_time = func_time - emg_offset;  % subtract it from the start of the functional scan
    datestr(emg_time, 'yyyy-mm-ddTHH:MM:SS.FFF')

    ans =
        '1900-01-01T18:57:42.425'

which shows that the EMG in the resting state session in the `_scans.tsv` should be updated to the following.

| filename                                 | acq_time                |
| ---------------------------------------- | ----------------------- |
| emg/sub-POM1FM0023671_task-rest_emg.vhdr | 1900-01-01T18:57:42.425 |

To check that all MRI triggers are picked up, we can compare the number of events between EMG and eyetracker

    eyetracker_rest = readtable('sub-POM1FM0023671/beh/sub-POM1FM0023671_task-rest_acq-smi_events.tsv', 'FileType', 'Text', 'Delimiter', '\t');
    sum(eyetracker_rest.value==100)

    ans =
       805

    emg_rest = readtable('sub-POM1FM0023671/emg/sub-POM1FM0023671_task-rest_events.tsv', 'FileType', 'Text', 'Delimiter', '\t');
    sum(strcmp(emg_rest.value, 'R  1'))

    ans =
       805

This shows that for both EMG and eyetracker there are 805 triggers, which corresponds to the number of volumes in the resting state `func` dataset that we can check as follows:

    mri = ft_read_mri('sub-POM1FM0023671/func/sub-POM1FM0023671_task-MB8fMRIfov21024mmukbiobank_acq-epfid2d188_dir-COL_run-1_echo-1_bold.nii.gz')

    mri =
      struct with fields:

              dim: [88 88 64 805]
          anatomy: [88x88x64x805 int16]
              hdr: [1x1 struct]
        transform: [4x4 double]
             unit: 'mm'

#### Eye tracker data

The eyetracker data can be aligned with the clock in the same way as the EMG, i.e. by means of the MRI triggers

    func_time = datevec('1900-01-01T18:57:57', 'yyyy-mm-ddTHH:MM:SS');
    eyetracker_offset = [0 0 0 0 0 12.98]; % the eyetracker starts earlier
    eyetracker_time = func_time - eyetracker_offset; % subtract it from the start of the functional scan
    datestr(eyetracker_time, 'yyyy-mm-ddTHH:MM:SS.FFF')

    ans =
    '1900-01-01T18:57:44.020'

which shows that the eyetracker data in the `_scans.tsv` should be updated to the following.

| filename                                               | acq_time                |
| ------------------------------------------------------ | ----------------------- |
| beh/sub-POM1FM0023671_task-rest_acq-smi_eyetracker.tsv | 1900-01-01T18:57:44.020 |

### Aligning the motor task state datasets

Subsequently we can continue with aligning the data from the motor task, which consists of functional MRI, EMG, eyetracker, and behavioral data in the `.log` and `.txt` format.

#### EMG

This is similar to the procedure we used above.

    func_time = datevec('1900-01-01T19:11:18', 'yyyy-mm-ddTHH:MM:SS');
    emg_offset = [0 0 0 0 0 15.7948]; % the EMG starts earlier
    emg_time = func_time - emg_offset;  % subtract it from the start of the functional scan
    datestr(emg_time, 'yyyy-mm-ddTHH:MM:SS.FFF')

    ans =
        '1900-01-01T19:11:02.205'

#### Eye tracker data

This is similar to the procedure we used above.

    func_time = datevec('1900-01-01T19:11:18', 'yyyy-mm-ddTHH:MM:SS');
    eyetracker_offset = [0 0 0 0 0 13.42]; % the eyetracker starts earlier
    eyetracker_time = func_time - eyetracker_offset;  % subtract it from the start of the functional scan
    datestr(eyetracker_time, 'yyyy-mm-ddTHH:MM:SS.FFF')

    ans =
        '1900-01-01T19:11:04.580'

#### Presentation standard log file (.log)

The events from the presentation log file can also be aligned using the MRI triggers. The first MRI event that is visible is a "pulse" event with trigger value 10 at 74.231 seconds. That means that presentation was started 74 seconds prior to the MRI scanner.

    func_time = datevec('1900-01-01T19:11:18', 'yyyy-mm-ddTHH:MM:SS');
    preslog_offset = [0 0 0 0 0 74.231]; % the presentation log file starts earlier
    preslog_time = func_time - preslog_offset;  % subtract it from the start of the functional scan
    datestr(preslog_time, 'yyyy-mm-ddTHH:MM:SS.FFF')

    ans =
        '1900-01-01T19:10:03.769'

#### Presentation custom log file (.txt)

The events in the custom `.txt` log file from presentation was not processed by the **[ft_read_event](/reference/fileio/ft_read_event)** function, but rather using MATLAB [readtable](https://www.mathworks.com/help/matlab/ref/readtable.html). As a consequence, it has many more details, i.e. rows, however the rows are not standardized. Also, it does not contain one "event" per row, but it contains one "trial" per row, which consists of both a stimulus and response. Furthermore, each trial is scored as correct/incorrect.

There are 132 trials in the `.txt` file, hence we expect 132 corresponding events for the presentation log and the EMG.

    prestxt_task = readtable('sub-POM1FM0023671/beh/sub-POM1FM0023671_task-motor_acq-txt_events.tsv', 'FileType', 'Text', 'Delimiter', '\t');
    preslog_task = readtable('sub-POM1FM0023671/beh/sub-POM1FM0023671_task-motor_acq-log_events.tsv', 'FileType', 'Text', 'Delimiter', '\t');
    emg_task = readtable('sub-POM1FM0023671/emg/sub-POM1FM0023671_task-motor_events.tsv', 'FileType', 'Text', 'Delimiter', '\t');

The following code shows each event value of the presentation `.log` file, and how often it occurs:

    [c, ia, ic] = unique(preslog_task.value);

    for i=1:numel(c)
      disp([c(i) sum(ic==i)]);
    end

    1    32
    2    33
    3    33
    4    25
    5     1
    6     5
    7     2
    8   132
    9   132
    10  595

It reveals that value 8 and 9 both happen 132 times. It also shows 595 occurrences for value 10, which probably corresponds to the triggers of the functional MRI scan. This is something we could again check using **[ft_read_mri](/reference/fileio/ft_read_mri)**.

The first trial in the presentation `.txt` file is specified to be at 83.307391 seconds. The first "Picture 8" in the presentation log file is at 83.3074 seconds, which is nearly the same. It also matches that there are 132 "Picture 8" events. Hence the time of the presentation `.log` and `.txt` files is the same, which could have been expected since both are written by the same software on the same computer. The corresponding entry in the `_scans.tsv` file should therefore become '1900-01-01T19:10:03.769'.

### Final `_scans.tsv` file

Combining the timing of all datasets, we end up with the following updated `_scans.tsv` file.

| filename                                                    | acq_time                |
| ----------------------------------------------------------- | ----------------------- |
| anat/sub-POM1FM0023671_acq-MPRAGE_rec-norm_run-1_T1w.nii.gz | 1900-01-01T18:50:23     |
| func/sub-POM1FM0023671_task-rest_acq-MB8_run-1_bold.nii.gz  | 1900-01-01T18:57:57     |
| func/sub-POM1FM0023671_task-motor_acq-MB6_run-1_bold.nii.gz | 1900-01-01T19:11:18     |
| emg/sub-POM1FM0023671_task-rest_emg.vhdr                    | 1900-01-01T18:57:42.425 |
| emg/sub-POM1FM0023671_task-motor_emg.vhdr                   | 1900-01-01T19:11:02.205 |
| beh/sub-POM1FM0023671_task-prac_acq-txt_events.tsv          | n/a                     |
| beh/sub-POM1FM0023671_task-rest_acq-smi_eyetracker.tsv      | 1900-01-01T18:57:44.020 |
| beh/sub-POM1FM0023671_task-motor_acq-log_events.tsv         | 1900-01-01T19:11:04.580 |
| beh/sub-POM1FM0023671_task-motor_acq-txt_events.tsv         | 1900-01-01T19:10:03.769 |
| beh/sub-POM1FM0023671_task-motor_acq-smi_eyetracker.tsv     | 1900-01-01T19:10:03.769 |

The MRI scans are specified with a 1-second precision. All subsequent measurements are more precise (millisecond accuracy) and therefore described also using fractional seconds.

The only one that remains unknown is the presentation `.txt` file that was recorded during the practice task. This was done while no other recording equipment was running, so we cannot determine the relative time to the other datasets.
