---
title: Inverse source parameter estimates from EEG/MEG data
tags: [development, inverse]
redirect_from:
  - /development/inverse/
---

# Inverse source parameter estimates from EEG/MEG data

FieldTrip has a consistent set of low-level functions for source reconstruction, i.e. estimating the location, strength and other parameters of the sources in the brain that underly the observed EEG and MEG data. The usual mathematical description of the sources is the equivalent current dipole, which is why in the subsequent documentation you will often see _source_ and _dipole_ used exchangeably.

The objective of supplying these low-level functions as a separate module/toolbox are to

1.  facilitate the reuse of these functions in other open source projects (e.g., EEGLAB, SPM)
2.  facilitate the implementation and support for new inverse methods, esp. for external users/contributors
3.  facilitate the implementation of advanced features

The low-level functions are combined in the [forward](/development/module/forward) and the [inverse](/development/module/inverse) toolboxes, which are released together with FieldTrip but can also be downloaded [here](https://download.fieldtriptoolbox.org/modules) as separate toolboxes. In the past these functions were combined in one toolbox.

Please note that if you are an end-user interested in analyzing experimental EEG/MEG data, you will probably will want to use the high-level FieldTrip functions. The functions such as **[ft_preprocessing](/reference/ft_preprocessing)**, **[ft_timelockanalysis](/reference/ft_timelockanalysis)** and **[ft_sourceanalysis](/reference/ft_sourceanalysis)** provide a user-friendly interface that take care of all relevant analysis steps and the data bookkeeping.

## Module layout

The [forward](/development/module/forward) module contains the methods to compute the solution to the volume conduction problem, i.e. "What is the potential or field distribution given a known source?".

The [inverse](/development/module/inverse) module contains the methods to estimate the source parameters, i.e. to answer the question "What are the unknown source parameter estimates, given the observed EEG or MEG field distribution?".

It contains high-level functions that are publicly available for experienced end-user. The functionality of these functions within these modules depend on low-level functions which are not available to the end-user and combined in a private directory.

## Supported methods for inverse estimation of the source parameters

The inverse methods for computing a source reconstruction can be divided into three categories: **dipole fitting** (using an overdetermined model with a few sources), **scanning** (using a metric that can be computed independently on each point of a source model) and **distributed source modelling** (using an underdetermined distributed source model). The following source reconstruction methods are implemented

### Dipole fitting

- simultaneous optimisation of position, orientation and strength
- symmetry constrains and/or fixed position, with free orientation and strength

### Scanning

- dynamic imaging of coherent sources (DICS)
- linear constrained minimum variance (LCMV)
- partial canonical coherence (PCC)
- multiple signal classification (MUSIC)
- scanning for residual variance
- scanning using sLORETA

### Distributed source modeling

- minimum norm estimation with and without noise regularisation (MNE)
- minimum norm estimation using eLORETA
- minimum norm estimation using Harmony

## Definition of the function-calls (API)

The functions for the inverse computation of the source activity, i.e. for computing the source reconstruction are

    estimate = ft_inverse_dics(sourcemodel, sens, headmodel, dat, C, ...)
    estimate = ft_inverse_dipolefit(sourcemodel, sens, headmodel, dat, ...)
    estimate = ft_inverse_eloreta(sourcemodel, sens, headmodel, dat, C, ...)
    estimate = ft_inverse_harmony(sourcemodel, sens, headmodel, dat, ...)
    estimate = ft_inverse_lcmv(sourcemodel, sens, headmodel, dat, C, ...)
    estimate = ft_inverse_mne(sourcemodel, sens, headmodel, dat, ...)
    estimate = ft_inverse_music(sourcemodel, sens, headmodel, dat, ...)
    estimate = ft_inverse_pcc(sourcemodel, sens, headmodel, dat, C, ...)
    estimate = ft_inverse_rv(sourcemodel, sens, headmodel, dat, ...)
    estimate = ft_inverse_sam(sourcemodel, sens, headmodel, dat, C, ...)
    estimate = ft_inverse_sloreta(sourcemodel, sens, headmodel, dat, C, ...)

The input structure "sourcemodel" contains the source model used for the reconstruction, or the initial dipole positions for fitting.

The input structure "sens" contains the electrode positions or the gradiometer positions and orientations.

The input structure "headmodel" contains the geometry and conductivity of the volume conductor model.

Most functions have additional optional input arguments that are specified as key-value pairs.

## Related documentation

The literature references to the implemented methods are given [here](/references_to_implemented_methods).

### See also these tutorials

{% include seealso category="tutorial" tag1="source" %}

### See also these frequently asked questions

{% include seealso category="faq" tag1="source" %}

### See also these examples

{% include seealso category="example" tag1="source" %}
