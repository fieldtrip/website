---
title: Project overview
tags: [development]
---

# Project overview

This section of the website lists information aimed at developers of FieldTrip and collaborating software projects. Most of the pages here are just meant as scratchpads for sharing ideas and for keeping track of the "to do" list and therefore will be of limited use to end-users.

We also use [GitHub](/development/git) and [Bugzilla](/bugzilla) to track projects.

## Open projects

- [clean up the buffer implementation](/development/project/buffer_v3)
- [Implement a common distributed computing backend](/development/project/distributed)
- [describe how to create design matrix (prepare_design to be deprecated)](/development/project/design)
- [document grad.tra, modifications to it, and effects on inverse](/development/project/tra)
- [ensure that all website pages exist](/development/project/orphans)
- [write a tutorial on how to work with the MEGSIM data](/development/project/megsim)
- [clean up tutorial documentation](/development/project/tutorial_documentation)
- [cleanup private functions](/development/project/cleanup_private_functions)
- [read_neuroshare](/development/project/read_neuroshare)
- [CSP for classification](/development/project/csp)
- [ensure consistency of the documentation](/development/project/documentation)
- [clean up inside_vol and similar functions](/development/project/inside_vol)
- [Ensure consistent units throughout fieldtrip](/development/project/units)
- [Z-scores](/development/project/zscores)
- [Implement support for a separation of data into a signal and noise subspace](/development/project/subspace)
- [Check the correctness of the implementation of the algorithms](/development/project/correctness)
- [Document the deprecated functions and configuration options](/development/deprecated)
- [improve interactive and non-interactive plotting of 4D bivariate data](/development/project/visualization)
- [Ensemblemethods](/development/project/ensemblemethods)
- [Restructure and rework all visualization functions](/development/project/restructure_and_rework_all_visualization_functions)
- [Checkdata and make source-structure definition consistent with other datatypes](/development/project/checkdata)
- [Import and export data to and from MNE-Python](/development/project/integrate_with_mne)
- [Example use of DSS for BCG removal](/development/project/dss)
- [Source-reconstruction using two dipoles - example script under construction](/development/project/symmetric_dipoles), see [1559](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=1559)
- [Improve the documentation of the source reconstruction methods](/development/project/documentation_source)

## Closed Projects

- [the rat beamformer](/development/project/rat) (won't be further worked on)
- Source reconstruction of event-related fields using minimum-norm estimate - (done and moved into place)
- [How to deal with forward model UNITS?](/development/project/fwdunits), see [686](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=686) (done)
- [Dealing with TMS-EEG datasets](/development/project/eeg_tms) (done)
- [move internal fcdc documentation onto the wiki](/development/project/move_internal_fcdc_documentation_onto_the_wiki) (done)
- [Create a tutorial on the processing of animal data](/development/project/animal) (done)
- [Support for NIRS data](/development/project/nirs) (done)
- [integration with SPM8](/development/project/spm8) (done)
- [integration with SPM12](/development/project/spm12) (done)
- [support for loading neighbour structure from templates, constructing your own templates and FAQ on how to use neighbourselection in general](/development/project/neighbourtemplates) (done)
- [How to create a volumetric CURRENT density](/development/project/curdens) (will not be done)
- [provide an interface to the FNS software for FDM modelling](/development/project/fns) (done)
- [dealing with the GEOMETRY of the forward model](/development/project/fwdarch2) (done)
- [Refurbishing the architecture of the FORWARD module](/development/project/fwdarch) (done)
- [clean up the documentation on head modeling, anatomical processing, etc.](/development/project/geometry_documentation) (done)
- [implement SIMBIO forward solver](/development/project/simbio_plan) (done)
- [replicate functionality of MNE software](/development/project/replicate_functionality_of_mne_software) (done)
- [Creating a head-model for source-reconstruction of MEG data](/development/project/headmodel_tutorial) (done)
- [Implement a robust algorithm for constructing triangulated EEG-BEM head models](/development/project/bemmodel) (done, wont fix)
- [How is the segmentation defined?](/faq/how_is_the_segmentation_defined) (done, made faq)
- [How to change the MRI orientation, the voxel size or the field-of-view?](/faq/how_change_mri_orientation_size_fov) (done, made faq)
- [Creating a volume conduction model of the head for source-reconstruction of EEG data](/development/project/headmodel_tutorial_eeg) (done)
- [ensure that the compat directories are NOT called by FieldTrip itself](/development/project/compat) (done)
- [infrastructure for testing](/development/project/infrastructure_for_testing) (done)
- [Implement a framework for regression testing](/development/project/testing) (done)
- [modularise ft_connectivityanalysis](/development/project/modularise_ft_connectivityanalysis) (done)
- [add the spike functions from Martin](/development/project/spike) (done)
- [create a forward solver for charges in an infinite halfspace](/development/project/halfspace) (done)
- [ensure consistent trial definition](/development/project/ensure_consistent_trial_definition) (done)
- [prefix all public functions with ft](/development/project/prefix) (done)
- [provide an interface to the OpenMEEG software for BEM modelling](/development/project/openmeeg) (done)
- [Implement online data processing and classification for BCI](/development/project/bci) (done)
- [Switch from SPM2 to SPM8](/development/project/switch_from_spm2_to_spm8) (done)
- [switch from CVS to SVN for the code version and release management](/development/svn) (done)
- [add stripped spm2 and other toolboxes as external dependencies](/development/project/external_dependencies) (done)
- [Implement a function which computes an mvar-model based on the input data](/development/project/mvaranalysis) (done).
- [Implement a function which computes a variety of bivariate coupling measures from the input data](/development/project/couplinganalysis) (done).
- [handling of continuous data](/development/project/continuous) (done)
- [Implement function that checks consistency of cfgs](/development/project/checkconfig) (done)
- [Restructure the directory layout](/development/project/directorylayout) (done)
- [Implement support for CTF synthetic gradiometers](/development/project/synthetic_grad) (done)
- [integrate the new preproc module into fieldtrip](/development/project/merge_preproc) (done)
- [consistent flank detection for triggers](/development/project/trigger) (done)
- [Implement trial selection option](/development/project/trialselect) (done)
- [Implement a graphical user interface as a "wizard" for certain analysis protocols](/development/project/wizard) (done)
- [Redesign the interface to the read_fcdc_xxx functions](/development/project/read_fcdc_xxx) (done)
- [Check the consistency between the documentation and the implementations](/development/project/consistency) (done)
- [Redesign and implement a common statistical backend for various data types](/development/project/statistics) (done)
- [Reimplement the avg/cov/trial handling](/development/project/timelockanalysis) (done)
- [integration with NUTMEG](/development/project/nutmeg) (will probably never happen, no active nutmeg development anymore)
- [transform_grid](/development/project/transform_grid) (done, ft_transform_geometry)
