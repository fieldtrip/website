---
title: Project overview
tags: [development]
---

# Project overview

This section lists information aimed at developers of FieldTrip and collaborating software projects. Most of the pages here are just meant as scratchpads for sharing ideas and for keeping track of the "to do" list and therefore will be of limited use to end-users. We also use [GitHub](/development/git) to track the development of specific projects; those are typically not listed here.

## Active projects

- [Improve artifact handling](/development/project/artifacts)
- [Improve integration with other toolboxes](/development/project/integration)
- [Improve regression testing](/development/project/regression)
- [Implement a common distributed computing backend](/development/project/distributed)
- [Import and export data to and from MNE-Python](/development/project/integrate_with_mne)
- [Implemention of realistic electrode properties in forward volume conduction models](/development/project/femfuns)

## Stale projects

- [Cleanup private functions](/development/project/cleanup_private_functions)
- [Describe how to create design matrix](/development/project/design)
- [Document grad.tra, modifications to it, and effects on inverse](/development/project/tra)
- [Document the deprecated functions and configuration options](/development/deprecated)
- [Ensure consistent units throughout fieldtrip](/development/project/units)
- [Implement support for a separation of data into a signal and noise subspace](/development/project/subspace)
- [Improve interactive and non-interactive plotting of 4D bivariate data](/development/project/visualization)
- [Improve the documentation of the source reconstruction methods](/development/project/documentation_source)
- [Restructure and rework all visualization functions](/development/project/restructure_and_rework_all_visualization_functions)
- [source reconstruction using two dipoles - example script under construction](/development/project/symmetric_dipoles), see [1559](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=1559)

## Closed Projects

- [Add stripped spm2 and other toolboxes as external dependencies](/development/project/external_dependencies) (done)
- [Add support for reading data from any file format supported by neuroshare](/development/project/read_neuroshare) (will not be done, outdated)
- [Add the spike functions from Martin](/development/project/spike) (done)
- [CSP for classification](/development/project/csp) (done)
- [Check the consistency between the documentation and the implementations](/development/project/consistency) (done)
- [Check the correctness of the implementation of the algorithms](/development/project/correctness) (done)
- [Clean up inside_vol and similar functions](/development/project/inside_vol) (done, more or less)
- [Clean up the buffer implementation](/development/project/buffer_v3) (will not be done)
- [Clean up the code of sourceanalysis, sourcedescriptives, freqdescriptives using checkdata](/development/project/checkdata) (done)
- [Clean up the documentation on head modeling, anatomical processing, etc.](/development/project/geometry_documentation) (done)
- [Clean up tutorial documentation](/development/project/tutorial_documentation) (will not be done)
- [Consistent flank detection for triggers](/development/project/trigger) (done)
- [Create a forward solver for charges in an infinite halfspace](/development/project/halfspace) (done)
- [Create a headmodel for source reconstruction of MEG data](/development/project/headmodel_tutorial) (done)
- [Create a tutorial on the processing of animal data](/development/project/animal) (done)
- [Create a volume conduction model of the head for source reconstruction of EEG data](/development/project/headmodel_tutorial_eeg) (done)
- [Dealing with TMS-EEG datasets](/development/project/eeg_tms) (done)
- [Dealing with the GEOMETRY of the forward model](/development/project/fwdarch2) (done)
- [Ensemble methods](/development/project/ensemblemethods) (will not be done)
- [Ensure consistency of the documentation](/development/project/documentation) (not clear any more)
- [Ensure consistent trial definition](/development/project/ensure_consistent_trial_definition) (done)
- [Ensure that all website pages exist](/development/project/orphans) (done)
- [Ensure that the compat directories are NOT called by FieldTrip itself](/development/project/compat) (done)
- Example use of DSS for ECG removal (done and moved in place)
- [Handling of continuous data](/development/project/continuous) (done)
- [How is the segmentation defined?](/faq/how_is_the_segmentation_defined) (done, made faq)
- [How to change the MRI orientation, the voxel size or the field-of-view?](/faq/how_change_mri_orientation_size_fov) (done, made faq)
- [How to create a volumetric CURRENT density](/development/project/curdens) (will not be done)
- [How to deal with forward model UNITS?](/development/project/fwdunits), see [686](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=686) (done)
- [Implement SIMBIO forward solver](/development/project/simbio_plan) (done)
- [Implement a consistent way to spatially transform a grid or source model](/development/project/transform_grid) (done, ft_transform_geometry)
- [Implement a framework for regression testing](/development/project/testing) (done)
- [Implement a function which computes a variety of bivariate coupling measures from the input data](/development/project/couplinganalysis) (done).
- [Implement a function which computes an mvar-model based on the input data](/development/project/mvaranalysis) (done).
- [Implement a graphical user interface as a "wizard" for certain analysis protocols](/development/project/wizard) (done)
- [Implement a robust algorithm for constructing triangulated EEG-BEM head models](/development/project/bemmodel) (done, wont fix)
- [Implement function that checks consistency of cfgs](/development/project/checkconfig) (done)
- [Implement online data processing and classification for BCI](/development/project/bci) (done)
- [Implement support for CTF synthetic gradiometers](/development/project/synthetic_grad) (done)
- [Implement trial selection option](/development/project/trialselect) (done)
- [Improve parallel computing under the hood](/development/project/parallel)
- [Infrastructure for testing](/development/project/infrastructure_for_testing) (done)
- [Integrate the new preproc module into fieldtrip](/development/project/merge_preproc) (done)
- [Integration with NUTMEG](/development/project/nutmeg) (will probably never happen, no active nutmeg development anymore)
- [Integration with SPM12](/development/project/spm12) (done)
- [Integration with SPM8](/development/project/spm8) (done)
- [Modularise ft_connectivityanalysis](/development/project/modularise_ft_connectivityanalysis) (done)
- [Move internal fcdc documentation onto the website](/development/project/move_internal_fcdc_documentation_onto_the_wiki) (done)
- [Prefix all public functions with ft](/development/project/prefix) (done)
- [Provide an interface to the FNS software for FDM modelling](/development/project/fns) (done)
- [Provide an interface to the OpenMEEG software for BEM modelling](/development/project/openmeeg) (done)
- [Redesign and implement a common statistical backend for various data types](/development/project/statistics) (done)
- [Redesign the interface to the read_fcdc_xxx functions](/development/project/read_fcdc_xxx) (done)
- [Refurbishing the architecture of the FORWARD module](/development/project/fwdarch) (done)
- [Reimplement the avg/cov/trial handling](/development/project/timelockanalysis) (done)
- [Replicate functionality of MNE software](/development/project/replicate_functionality_of_mne_software) (done)
- [Restructure the directory layout](/development/project/directorylayout) (done)
- Source reconstruction of event-related fields using minimum-norm estimate - (done and moved into place)
- [Support for NIRS data](/development/project/nirs) (done)
- [Support for loading neighbour structure from templates, constructing your own templates and FAQ on how to use neighbourselection in general](/development/project/neighbourtemplates) (done)
- [Switch from CVS to SVN for the code version and release management](/development/svn) (done)
- [Switch from SPM2 to SPM8](/development/project/switch_from_spm2_to_spm8) (done)
- [The rat beamformer](/development/project/rat) (won't be further worked on)
- [What is the best way to homogenize data using z-scores](/development/project/zscores) (not clear any more)
- [Write a tutorial on how to work with the MEGSIM data](/development/project/megsim) (will not be done)
