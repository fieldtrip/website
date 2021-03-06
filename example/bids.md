---
title: BIDS - the brain imaging data structure
tags: [bids, sharing]
---

# BIDS - the brain imaging data structure

FieldTrip can read data from all MEG, EEG, iEEG and MRI file formats that are supported in BIDS. Furthermore, it includes the **[data2bids](https://github.com/fieldtrip/fieldtrip/blob/release/data2bids.m)** function to convert data to the BIDS structure. This function can convert data formats (if needed), and writes the accompanying "sidecar files" that contain metadata about channels, coordinates, events, etcetera to the .json and .tsv format.

{% include markup/warning %}
We recommend that you convert your raw data to BIDS **prior** to implementing your analyses scripts. That will make it much easier to share the scripts and derived data.
{% include markup/end %}

The BIDS project overview is presented on <http://bids.neuroimaging.io>. You can read the full specification on <https://bids-specification.readthedocs.io>. Please note that BIDS is not only relevant for FieldTrip, but that it also been embraced by the SPM, EEGLAB, MNE-Python and BrainStorm developers, and of course by the MRI and fMRI community, for example on <https://openneuro.org>.

{% include markup/success %}
The [EEG sedation](/workshop/madrid2019/bids_sedation) example is currently the most clean and comprehensive FieldTrip-specific demonstration of how to convert existing raw EEG data to BIDS.
{% include markup/end %}

## See also

{% include seealso tag="bids" %}
