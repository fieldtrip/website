---
title: BIDS - the brain imaging data structure
category: example
tags: [bids, sharing]
redirect_from:
    - /example/bids/
---

# BIDS - the brain imaging data structure

The [BIDS standard](https://bids.neuroimaging.io) aims to organise and describe neuroimaging data in a uniform way to simplify data sharing through the scientific community.

FieldTrip can read data from all MEG, EEG, iEEG and MRI file formats that are supported in BIDS. Furthermore, it includes the **[data2bids](/reference/data2bids)** function to convert data to the BIDS structure. This function can convert data formats (if needed), and writes the accompanying "sidecar files" that contain metadata about channels, coordinates, events, etcetera to the .json and .tsv format.

{% include markup/yellow %}
We recommend that you convert your raw data to BIDS **prior** to implementing your analyses scripts. That will make it much easier to share the scripts, the raw and the derived data.
{% include markup/end %}

The BIDS project overview is presented on <http://bids.neuroimaging.io>. You can read the full specification on <https://bids-specification.readthedocs.io>. Please note that BIDS is not only relevant for FieldTrip, but that it also been embraced by the SPM, EEGLAB, MNE-Python and BrainStorm developers, and of course by the MRI and fMRI community, for example on <https://openneuro.org>.

The following figure gives an example of EEG data organized according to BIDS (taken from [Pernet *et al.*, 2019](https://doi.org/10.1038/s41597-019-0104-8)):

{% include image src="/assets/img/example/bids/BIDS_example.png" width="500" %}

This example shows that BIDS does not only specify the directory structure and the file names for the data (1), but also includes information about acquisition parameters (2), stimuli (3), channels (4), electrodes position (5) and coordinate system (6) in which the electrodes are expressed. Note that for EEG the electrode position and coordinate system are optional, but the other metadata is not.

{% include markup/green %}
The [EEG sedation](/workshop/madrid2019/bids_sedation) example is currently the most clean and comprehensive FieldTrip-specific demonstration of how to convert existing raw EEG data to BIDS.
{% include markup/end %}

## See also

{% include seealso tag="bids" %}
