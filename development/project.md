---
title: Project overview
layout: default
tags: [development]
---

# Project overview

This section of the website lists information aimed at developers of FieldTrip and collaborating software projects. Most of the pages here are just meant as scratchpad for sharing ideas and for keeping track of the "to do" list and therefore will be of limited use to end-users. We also use [:bugzilla](/bugzilla) to track projects.

## Open projects

*  [clean up the buffer implementation](/development/buffer_v3)
*  [Implement a common distributed computing backend](/development/distributed)
*  [describe how to create design matrix (prepare_design to be deprecated)](/development/design)
*  [document grad.tra, modifications to it, and effects on inverse](/development/tra)
*  [integration with NUTMEG](/development/nutmeg)
*  [ensure that all wiki pages exist](/development/orphans)
*  [write a tutorial on how to work with the MEGSIM data](/development/megsim)
*  [clean up tutorial documentation](/development/tutorial_documentation)
*  [development:cleanup private functions](/development/cleanup_private_functions)
*  [development:read_neuroshare](/development/read_neuroshare)
*  [CSP for classification](/development/csp)
*  [development:transform_grid](/development/transform_grid)
*  [ ensure consistency of the documentation](/development/documentation)
*  [clean up inside_vol and similar functions](/development/inside_vol)
*  [Ensure consistent units throughout fieldtrip](/development/units)
*  [Z-scores](/development/zscores)
*  [Implement support for a separation of data into a signal and noise subspace](/development/subspace)
*  [Check the correctness of the implementation of the algorithms](/development/correctness)
*  [ Document the deprecated functions and configuration options](/development/deprecated)
*  [Reimplement the avg/cov/trial handling](/development/timelockanalysis)
*  [improve interactive and non-interactive plotting of 4D bivariate data](/development/visualization)  
*  [Ensemblemethods](/development/ensemblemethods)
*  [development:Restructure and rework all visualization functions](/development/restructure_and_rework_all_visualization_functions)
*  [Checkdata and make source-structure definition consistent with other datatypes](/development/checkdata)
*  [Import and export data to and from MNE-Python](/development/integrate_with_mne)

### Projects dealing with forward and inverse modeling
*  [How to deal with forward model UNITS?](/development/fwdunits) (see [686](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=686))
*  [Source-reconstruction using two dipoles - example script under construction](/development/symmetric_dipoles) (see [1559](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=1559))
*  [Source reconstruction of event-related fields using minimum-norm estimate - tutorial under construction](/development/minimum_norm_estimate_new)
*  [Developing the documentation of the source reconstruction methods](/development/documentation_source)
*  [Example use of DSS for BCG removal](/development/dss)
*  [the rat beamformer](/development/rat)

## Closed Projects
*  [Dealing with TMS-EEG datasets](/development/eeg_tms) (done)
*  [development:move internal fcdc documentation onto the wiki](/development/move_internal_fcdc_documentation_onto_the_wiki) (done)
*  [Create a tutorial on the processing of animal data](/development/animal) (done)
*  [Support for NIRS data](/development/nirs) (done)
*  [integration with SPM8](/development/spm8) (done)
*  [integration with SPM12](/development/spm12) (done)
*  [support for loading neighbour structure from templates, constructing your own templates and faq: how to use neighbourselection in general](/development/neighbourtemplates) (done)
*  [How to create a volumetric CURRENT density](/development/curdens)  (will not be done)
*  [provide an interface to the FNS software for FDM modelling](/development/fns) (done)
*  [dealing with the GEOMETRY of the forward model](/development/fwdarch2) (done)
*  [Refurbishing the architecture of the FORWARD module](/development/fwdarch) (done)
*  [clean up the documentation on head modeling, anatomical processing, etc.](/development/geometry_documentation) (done)  
*  [implement SIMBIO forward solver](/development/simbio_plan) (done)
*  [development:replicate functionality of MNE software](/development/replicate_functionality_of_mne_software) (done)
*  [Creating a head-model for source-reconstruction of MEG data](/development/headmodel_tutorial) (done)
*  [Implement a robust algorithm for constructing triangulated EEG-BEM head models](/development/bemmodel) (done, wont fix)
*  [How is the segmentation defined?](/faq/how_is_the_segmentation_defined) (done, made faq)
*  [How to change the MRI orientation, the voxel size or the field-of-view?](/faq/how_change_mri_orientation_size_fov) (done, made faq)
*  [Creating a volume conduction model of the head for source-reconstruction of EEG data](/development/headmodel_tutorial_eeg) (done)
*  [ensure that the compat directories are NOT called by fieldtrip itself](/development/compat) (done)
*  [development:infrastructure for testing](/development/infrastructure_for_testing) (done)
*  [Implement a framework for regression testing](/development/testing) (done)
*  [development:modularise ft_connectivityanalysis](/development/modularise_ft_connectivityanalysis) (done)
*  [add the spike functions from Martin](/development/spike) (done)
*  [create a forward solver for charges in an infinite halfspace](/development/halfspace) (done)
*  [development:ensure consistent trial definition](/development/ensure_consistent_trial_definition) (done)
*  [prefix all public functions with ft](/development/prefix) (done)
*  [provide an interface to the OpenMEEG software for BEM modelling](/development/openmeeg) (done)
*  [Implement online data processing and classification for BCI](/development/bci) (done)
*  [development:Switch from SPM2 to SPM8](/development/switch_from_spm2_to_spm8) (done)
*  [switch from CVS to SVN for the code version and release management](/development/svn) (done)
*  [add stripped spm2 and other toolboxes as external dependencies](/development/external_dependencies) (done)
*  [Implement a function which computes an mvar-model based on the input data](/development/mvaranalysis) (done).
*  [Implement a function which computes a variety of bivariate coupling measures from the input data](/development/couplinganalysis) (done).
*  [handling of continuous data](/development/continuous) (done)
*  [Implement function that checks consistency of cfgs](/development/checkconfig) (done)
*  [Restructure the directory layout](/development/directorylayout) (done)
*  [Implement support for CTF synthetic gradiometers](/development/synthetic_grad) (done)
*  [integrate the new preproc module into fieldtrip](/development/merge_preproc) (done)
*  [consistent flank detection for triggers](/development/trigger) (done)
*  [Implement trial selection option](/development/trialselect) (done)
*  [Implement a graphical user interface as a "wizard" for certain analysis protocols](/development/wizard) (done)
*  [Redesign the interface to the read_fcdc_xxx functions](/development/read_fcdc_xxx) (done)
*  [Check the consistency between the documentation and the implementations](/development/consistency) (done)
*  [Redesign and implement a common statistical backend for various data types](/development/statistics) (done)
