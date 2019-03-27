---
title: Inverse source parameter estimates from EEG/MEG data
---

{% include /shared/development/warning.md %}

# Inverse source parameter estimates from EEG/MEG data

FieldTrip has a consistent set of low-level functions for source reconstruction, i.e. estimating the location, strength and other parameters of the sources in the brain that underly the observed EEG and MEG data. The usual mathematical description of the sources is the equivalent current dipole, which is why in the subsequent documentation you will often see _source_ and _dipole_ used exchangeably.

The objective of supplying these low-level functions as a separate module/toolbox are to

1.  facilitate the reuse of these functions in other open source projects (e.g. EEGLAB, SPM)
2.  facilitate the implementation and support for new inverse methods, esp. for external users/contributors
3.  facilitate the implementation of advanced features

The low-level functions are combined in the [development:forward](/development/module/forward) and the [development:inverse](/development/module/inverse) toolboxes, which are released together with FieldTrip but can also be downloaded [here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/modules/) as separate toolboxes. In the past these functions were combined in one toolbox.

Please note that if you are an end-user interested in analyzing experimental EEG/MEG data, you will probably will want to use the high-level FieldTrip functions. The functions such as **[ft_preprocessing](/reference/ft_preprocessing)**, **[ft_timelockanalysis](/reference/ft_timelockanalysis)** and **[ft_sourceanalysis](/reference/ft_sourceanalysis)** provide a user-friendly interface that take care of all relevant analysis steps and the data bookkeeping.

## Module layout

The [development:forward](/development/module/forward) module contains the methods to compute the solution to the volume conduction problem, i.e. "What is the potential or field distribution given a known source?".

The [development:inverse](/development/module/inverse) module contains the methods to estimate the source parameters, i.e. to answer the question "What are the unknown source parameters, given the observed EEG or MEG field distribution?".

It contains high-level functions that are publicly available for experienced end-user. The functionality of these functions within these modules depend on low-level functions which are not available to the end-user and combined in a private directory.

## Supported methods for inverse estimation of the source parameters

The inverse methods for computing a source reconstruction can be divided into three categories: **dipole fitting** (using an overdetermined model with a few sources), **dipole scaning** (using a metric that can be computed independently on each point of a grid) and **distributed source modelling** (using an underdetermined distributed source model). The following source reconstruction methods are implemented

- dipole fitting

  - simultaneous optimisation of position, orientation and strength
  - symmetry constrains and/or fixed position, with free orientation and strength

- dipole scanning

  - dynamic imaging of coherent sources (DICS)
  - linear constrained minimum variance (LCMV)
  - partial canonical coherence (PCC)
  - multiple signal classification (MUSIC)
  - scanning for residual variance

- distributed source modeling
  - minimum norm estimation with and without noise regularisation (MNE)

## Definition of the function-calls (API)

The functions for the inverse computation of the source activity, i.e. for computing the source reconstruction are
[dipout] = dipole_fit(dip, sens, vol, dat, ...)
[dipout] = beamformer_dics(dip, sens, vol, dat, cov, ...)
[dipout] = beamformer_lcmv(dip, sens, vol, dat, cov, ...)
[dipout] = beamformer_pcc(dip, sens, vol, dat, cov, ...)
[dipout] = music(dip, sens, vol, dat, ...)
[dipout] = minimumnormestimate(dip, sens, vol, dat, ...)
[dipout] = residualvariance(dip, sens, vol, dat, ...)

The input array "pos" contains the dipole position (1x3 or Nx3).

The input structure "dip" contains the initial dipole model or dipole grid that is used for source reconstruction.

The input structure "sens" contains the electrode positions or the gradiometer positions and orientations.

The input structure "vol" contains the geometry and conductivity of the volume conductor model.

Most functions have additional optional input arguments that are specified as key-value pairs.

FIXME We are currently redesigning the interface to these functions, therefore the documentation is a bit sparse at the moment.

## Related documentation

The literature references to the implemented methods are given [here](/references_to_implemented_methods).

Frequently asked questions about forward and inverse modeling:

{% include seealso tag1="faq" tag2="source" %}

Example material for forward and inverse modeling:

{% include seealso tag1="example" tag2="source" %}

Tutorial material for forward and inverse modeling:

{% include seealso tag1="tutorial" tag2="source" %}
