---
title: BIDS - the brain imaging data structure
tags: [bids, sharing]
---

# BIDS - the brain imaging data structure

FieldTrip can read data from all MEG, EEG, iEEG and MRI file formats that are supported in BIDS. Furthermore, it includes the **[data2bids](/reference/data2bids)** function to convert data to the BIDS structure. This function can convert data formats (if needed), and writes the accompanying "sidecar files" that contain metadata about channels, coordinates, events, etcetera to the .json and .tsv format.

## See also

{% include seealso tag="bids" %}
