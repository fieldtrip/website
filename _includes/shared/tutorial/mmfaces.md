## Details on the multimodal faces dataset

The "mmfaces" dataset contains EEG, MEG, functional MRI and structural MRI data from 16 subjects who undertook multiple runs of a simple task performed on a large number of Famous, Unfamiliar and Scrambled faces. It is described in more detail in [doi:10.3389/fnhum.2011.00076](http://journal.frontiersin.org/Journal/10.3389/fnhum.2011.00076/abstract).

The complete dataset is available from the [MRC-CBU ftp server](ftp://ftp.mrc-cbu.cam.ac.uk/personal/rik.henson/wakemandg_hensonrn/).

The MEG data consist of 102 magnetometers and 204 planar gradiometers from a Neuromag/Elekta VectorView system. The same system was used to simultaneously record EEG data from 70 electrodes (using a nose reference), which are stored in the same “FIF” format file. The above FTP site includes a raw FIF file for each run/subject, but also a second .fif file in which the MEG data have been “cleaned” using Signal-Space Separation as implemented in MaxFilter 2.1. We use the latter here.

A Polhemus digitizer was used to digitise three fiducial points and a large number of other points across the scalp, which can be used to coregister the M/EEG data with the structural MRI image. Six runs (sessions ) of approximately 10mins were acquired for each subject, while they judged the left-right symmetry of each stimulus (face or scrambled), leading to nearly 300 trials in total for each of the 3 conditions.

The MRI data were acquired on a 3T Siemens TIM Trio, and include a 1x1x1mm T1-weighted structural MRI (sMRI) as well as a large number of 3x3x4mm T2\*-weighted functional MRI (fMRI) EPI volumes acquired during 9 runs of the same task (performed by same subjects with different set of stimuli on a separate visit). (The FTP site also contains DTI and ME-FLASH MRI images from the same subject, which could be used for improved head modelling for example, but these are not used here.) For full description of the data and paradigm, see README.txt on the FTP site or [Wakeman & Henson](http://journal.frontiersin.org/Journal/10.3389/fnhum.2011.00076/abstract).
