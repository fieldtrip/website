---
title: Developing the documentation of the source reconstruction methods
---

{% include /shared/development/warning.md %}

# Developing the documentation of the source reconstruction methods

## Introduction

This page contains questions that users could ask when they analyze their data with FieldTrip. If it is possible the answers are also provided. If any documentation already exist on the FieldTrip wiki website gives an answer, the answer should point to those pages. In some cases, may we just want to point to relevant literature.

## Questions and Answers

## What kind of source reconstruction methods are implemented in FieldTrip?

The [Inverse source parameter estimates from EEG/MEG data](/development/module/inverse) page describes under the second point which are the supported methods.

1.  dipole fitting
    - simultaneous optimisation of position, orientation and strength
    - symmetry constrains and/or fixed position, with free orientation and strength
2.  dipole scanning
    - dynamic imaging of coherent sources (DICS)
    - linear constrained minimum variance (LCMV)
    - partial canonical coherence (PCC)
    - multiple signal classification (MUSIC)
    - scanning for residual variance
3.  distributed source modeling
    - minimum norm estimation with and without noise regularisation (MNE)

The reference of the **[ft_sourceanalysis](/reference/ft_sourceanalysis)** function refers to the following method

    cfg.method = 'lcmv'    linear constrained minimum variance beamformer
                 'sam'     synthetic aperture magnetometry
                 'dics'    dynamic imaging of coherent sources
                 'pcc'     partial cannonical correlation/coherence
                 'mne'     minimum norm estimation
                 'loreta'  minimum norm estimation with smoothness constraint
                 'rv'      scan residual variance with single dipole
                 'music'   multiple signal classification
                 'mvl'     multivariate Laplace source localization

## What is the difference between the methods?

Here are the [References to implemented methods](/references_methods).

## What kind of source reconstruction method should I use?

- _Does it depend on the data?_ (EEG vs. MEG, oscillations vs event-related, realistic vs. non-realistic headmodel)

Event-related Field/Potential + time-course: MNE
Oscillatory activity + at certain point in time: beamforming (dics)
beamforming: lcmv - ?
(see Hesse, Jensen (2010) and Background of the MNE tutorial)

- _Does it depend on a priori hypothesis of the source involved?_ (cortical sheets vs. 3D grid)
- _Does it depend on what kind of information I am interested in?_ (e.g., changes in time or not)

## What kind of data I need for source reconstruction?

functional data, anatomical data, channel/electrode positions

## Why should I use source reconstruction?

point to introductionary literature

## How should I do source reconstruction?

depends on the specific method; available documentation in FT at the momen

### dipolefitting

- simultaneous optimisation of position, orientation and strength
- symmetry constrains and/or fixed position, with free orientation and strength

**tutorial sites:**

none.

** example scripts:**

[Compute forward simulated data and apply a dipole fit](/example/source/simulateddata_dipolefit)

[Fit a dipole to the tactile ERF after mechanical stimulation](/example/source/dipolefit_somatosensory_erf)

_Why is this fixme?_

[source reconstruction using two dipoles](/development/project/symmetric_dipoles)

_This is under construction, but it is not really clear how this exactly relates to dipole fitting._

### dipole scanning

- dynamic imaging of coherent sources (DICS)
- linear constrained minimum variance (LCMV)
- partial canonical coherence (PCC)
- multiple signal classification (MUSIC)
- scanning for residual variance

### distributed source modeling

- minimum norm estimation with and without noise regularisation (MNE)

## What kind of volume conduction models of the head are implemented in FieldTrip?

FAQ: [What kind of volume conduction models are implemented?](/faq/source/datatype_headmodel)

Reference: **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**

- The methods listed in the reference of ft_prepare_headmodel should be matched to the articles in [References to implemented methods](/references_methods).
- The references to implemented methods can be probably extended.

Method

**EEG**

- name in help of ft_prepare_headmodel: asa
- article in References to implemented methods: **none**
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: **none** but it is probably not applicable
- **reading function** (reads in a certain type of volume conduction model)

- name in help of ft_prepare_headmodel: bemcp
- article in References to implemented methods: **none**
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: **none** but the person's name who provided the code is mentioned

- name in help of ft_prepare_headmodel: dipoli
- article in References to implemented methods: yes (Oostendorp T, van Oosterom A., 1991)
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: yes

- name in help of ft_prepare_headmodel: openmeeg
- article in References to implemented methods: **none**
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: **yes**

- name in help of ft_prepare_headmodel: concentricspheres
- article in References to implemented methods: yes (Cuffin, Cohen, 1979)
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: **none**

- name in help of ft_prepare_headmodel: halfspace
- article in References to implemented methods: **none** (but is it relevant?)
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: **none** (but is it relevant?)

- name in help of ft_prepare_headmodel: infinite
- article in References to implemented methods: **none** (but is it relevant?)
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: **none** (but is it relevant?)

- name in help of ft_prepare_headmodel: multispheres
- Does this methods apply also to EEG? It says so in [Refurbishing the FORWARD module](/development/project/fwdarch) but it is **not listed as method for EEG** in the reference of ft_prepare_headmodel.
- see it under MEG methods.

- name in help of ft_prepare_headmodel: singlesphere
- article in References to implemented methods: yes (Cuffin, Cohen, 1977)
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: yes

- name in help of ft_prepare_headmodel: **none**

- name in script of ft_prepare_headmodel: **slab_monopole**
- article in References to implemented methods: **none**
- lower-level function name: **[ft_headmodel_slab](/reference/forward/ft_headmodel_slab)**
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: **none**

- name in help of ft_prepare_headmodel: simbio
- article in References to implemented methods: **none** but is probably not applicable
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: **none** but it is probably not applicable
- **reading function** (reads in a certain type of volume conduction model)

- name in help of ft_prepare_headmodel: fns
- article in References to implemented methods: **none**
- explanation in help of the lower-level function: yes

- reference in help of the lower-level function: **yes** (or at least a link provided)

**MEG**

- name in help of ft_prepare_headmodel: singlesphere
- see it under EEG methods.

- name in help of ft_prepare_headmodel: **multispheres** FIXME rather not use multisphere because it is ambiguous
- name in script of ft_prepare_headmodel: **localspheres**
- article in References to implemented methods: yes (Huang et al., 1999) but is called: **multispheres**
- lower-level function name: **[ft_headmodel_localspheres](/reference/forward/ft_headmodel_localspheres)**
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: yes

- name in help of ft_prepare_headmodel: singleshell
- article in References to implemented methods: yes (Nolte, 2003)
- explanation in help of the lower-level function: yes
- reference in help of the lower-level function: yes

- name in help of ft_prepare_headmodel: infinite
- see it under EEG methods.

- name in help of ft_prepare_headmodel: openmeeg
- Does this methods apply also to MEG? It says so in [Refurbishing the FORWARD module](/development/project/fwdarch) but it is **not listed as method for MEG** in the reference of ft_prepare_headmodel.
- see it under EEG methods.
