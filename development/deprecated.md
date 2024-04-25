---
title: Deprecated functions and options
---

{% include /shared/development/warning.md %}

# Deprecated functions and options

{% include markup/skyblue %}
Definition of **[deprecation](https://en.wikipedia.org/wiki/Deprecated)**
(_From Wikipedia, the free encyclopedia_)

In computer software standards and documentation, deprecation is the gradual phasing-out of a software or programming language feature.

A feature or method marked as deprecated is one which is considered obsolete, and whose use is discouraged. The feature still works in the current version of the software, although it may raise error messages as warnings. These serve to alert the user to the fact that the feature may be removed in future releases.
{% include markup/end %}

## Introduction

FieldTrip is developed in a continuous fashion, i.e. there are no fixed or scheduled releases; instead the code is continuously being extended and improved. Usually the changes to FieldTrip result in more functionality. Sometimes it is also necessary to remove a function or some functionality in FieldTrip. The reasons for it can be that it is replaced by a better function, that the name has changed for consistency with other FieldTrip functions, or that the implementation was buggy and too difficult to fix.

Typically we will try to keep FieldTrip backward compatible whenever we replace a function or an option with something else. However, it is not possible to maintain backward compatibility forever. That is why specific functionality is _deprecated_. This page tries to give an overview of deprecated functions and/or functionality.

The [code development guidelines](/development/guideline/code?&#document_deprecated_source_code) explain how you (as developer) should deal with deprecating functions, options or other pieces of functionality.

## Overview of deprecated functions

December 2022:

- the `peer` and `engine` module have been removed, see <https://github.com/fieldtrip/fieldtrip/issues/2153>

November 2022:

- the config object and the `cfg.trackconfig` functionality has been removed, see <https://github.com/fieldtrip/fieldtrip/issues/2127>

February 2015:

- **ft_analysisprotocol** (ft_analysispipeline has replaced this function; see <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=2852>)

July 2013:

- **ft_freqcomparison** (ft_math can do the same and more; see <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=2222>)

October 2011: the following functions were already deprecated and I moved them from the main directory to fieldtrip/compat.

- **ft_sourcewrite** (has been replaced by ft_volumewrite)
- **ft_databrowser_old**
- **ft_componentbrowser_old**

September 2011: the following function should really not be used any more. Since I am updating some of the other ft_artifact_xxx functions, I decided to put this out of the way (i.e. moved it to compat).

- **ft_artifact_manual**

October 2010: the following functions will be substituted by a single implementation of **[ft_artifact_zvalue](/reference/ft_artifact_zvalue)**, which accomplishes the same results of the deprecated function with different cfg settings ([see HERE](/tutorial/artifacts)).

- **ft_artifact_eog**
- **ft_artifact_jump**
- **ft_artifact_muscle**

January 2010: Because of switching to the new low-level plotting functions in the plotting toolbox topoplot.m has become deprecated. Nearly all of its functionality is now in topoplotER/TFR.

- **topoplot.m**

May 2009: The read_fcdc/write_fcdc functions have all been replaced over the course of the last years by new functions in the fileio module. The new functions have a cleaner interface and should therefore be used preferably.

- **read_fcdc_header.m**
- **read_fcdc_data.m**
- **read_fcdc_event.m**
- **read_fcdc_mri.m**
- **read_fcdc_elec.m**
- **write_fcdc_data.m**
- **read_fcdc_spike.m**
- **write_fcdc_spike.m**

April 2007: The following functions have been excluded from the 0.9.8 release version

- **downsamplevolume.m**
- **normalisevolume.m**
- **segmentvolume.m**
- **artifact_eog_old.m**
- **artifact_jump_old.m**
- **artifact_muscle_old.m**
- **sourceplot_old.m**
- **electrodenormalize.m**
- **meginterpolate.m**
- **precompute_leadfield.m**

January 2006: The XXXvolume functions have all been renamed to volumeXXX to make their names more consistent and to make it easier to find the FieldTrip functions that operate on volume data.

- **downsamplevolume.m** has been renamed to volumedownsample
- **normalisevolume.m** has been renamed to volumenormalise
- **segmentvolume.m** has been renamed to volumesegment

January 2006: Some of the artifact detection functions have been completely rewritten. Although the new functions should have the same behavior, the exact same result cannot be guaranteed. To allow people to use the old implementations, they are still available:

- **artifact_eog_old.m** is the old implementation of artifact_eog
- **artifact_jump_old.m** is the old implementation of artifact_jump
- **artifact_muscle_old.m** is the old implementation of artifact_muscle

September 2005: The trial functions in the list below all predate the generic event handling that has been implemented using read_fcdc_event. These trial functions are file-format specific, and therefore deprecated.

The idea underlying the new implementation for trialfuns is to separate the "hardware knowledge" for getting trigger information out of the file (in _read_fcdc_event.m_) from the "experiment knowledge" in determining the sequence of trigger events that is interesting (in the trialfun). There is one general trial function _trialfun_general.m_ that can be used for selecting a segment around a trigger. A more elaborate explanation and example code is given [here](/example/making_your_own_trialfun_for_conditional_trial_definition).

- **trialfun_brainvision.m**
- **trialfun_ctf_continuous.m**
- **trialfun_ctf_epoched.m**
- **trialfun_eeprobe_avr.m**
- **trialfun_eeprobe_cnt.m**
- **trialfun_neuromag.m**
- **trialfun_neuroscan_cnt.m**
- **trialfun_neuroscan_eeg.m**

Some miscellaneous functions that are deprecated are:

- **electrodenormalize.m** has been replaced by electroderealign
- **meginterpolate.m** has been replaced by the individual functions megrealign, megplanar and megrepair
- **precompute_leadfield.m** has been replaced by prepare_leadfield
- **rejecttrial.m** has been replaced by rejectvisual
- **statistics_random.m** has been replaced by statistics_montecarlo

## Overview of deprecated cfg options

June 2013: functionality moved from ft_sourcedescriptives to ft_math.

- **cfg.transform** (deprecated)

January 2010: Several old options from topoplot.m (deprecated) have been renamed/deprecated and are now supported in topoplotER/TFR.

- **cfg.electrodes** (renamed into: cfg.marker)
- **cfg.emarker** (renamed into: cfg.markersymbol)
- **cfg.ecolor** (renamed into: cfg.markercolor)
- **cfg.emarkersize** (renamed into: cfg.markersize)
- **cfg.efontsize** (renamed into: cfg.markerfontsize)
- **cfg.hlmarker** (renamed into: cfg.highlightsymbol)
- **cfg.hlcolor** (renamed into: cfg.highlightcolor)
- **cfg.hlmarkersize** (renamed into: cfg.highlightsize)
- **cfg.maplimits** (renamed into: cfg.zlim)
- **cfg.grid_scale** (renamed into: cfg.gridscale)
- **cfg.interpolate** (renamed into: cfg.interpolation)
- **cfg.numcontour** (renamed into: cfg.contournum)
- **cfg.electrod** (renamed into: cfg.marker)
- **cfg.electcolor** (renamed into: cfg.markercolor)
- **cfg.emsize** (renamed into: cfg.markersize)
- **cfg.efsize** (renamed into: cfg.markerfontsize)
- **cfg.headlimits** (renamed into: cfg.interplimits)
- **cfg.hllinewidth** (deprecated)
- **cfg.headcolor** (deprecated)
- **cfg.hcolor** (deprecated)
- **cfg.hlinewidth** (deprecated)
- **cfg.contcolor** (deprecated)
- **cfg.outline** (deprecated)
- **cfg.highlightfacecolor** (deprecated)
- **cfg.showlabels** (deprecated)
- **cfg.hllinewidth** (deprecated)

July 2008

- **cfg.tightgrid** (in prepare_dipole_grid)

February 2007

- **cfg.plot3d** (in megrealign) has been replaced by cfg.feedback
- **cfg.plot3d** (in electroderealign) has been merged with cfg.feedback

Older

- **cfg.sgn** (in freqanalysis and some artifact functions) has been replaced by cfg.label for consistency with other functions
- **cfg.sgncomb** has been replaced by cfg.labelcmb for consistency with cfg.label
- **cfg.rejectmuscle** (preprocessing and rejectartifact) has been replaced by cfg.artfctdef.muscle
- **cfg.rejectjump** (preprocessing and rejectartifact) has been replaced by cfg.artfctdef.jump
- **cfg.rejecteog** (preprocessing and rejectartifact) has been replaced by cfg.artfctdef.eog
