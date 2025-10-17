---
title: Multimodal faces dataset
tags: [practicalmeeg2025, mmfaces]
---

The dataset that we analyze in these tutorials is part of a dataset recorded by Rik Hanson and colleagues. During the PracticalMEEG hands-on sessions we will mainly work with the MEG data of a single representative subject, for the group statistics we will work with source-level processed data from all subjects.

## Downloading the original data

The original data is ~84 GB and can be found on <https://openneuro.org> and {% include badge doi="10.18112/openneuro.ds000117.v1.0.5" %}.

To download the original data, we recommend to use the Amazon AWS command line utility
like this:

    aws s3 sync --no-sign-request s3://openneuro.org/ds000117 ds000117-orig/

or using DataLad like this

    datalad install -r https://github.com/OpenNeuroDatasets/ds000117.git

## Details on the multimodal faces dataset

{% include /shared/tutorial/mmfaces.md %}
