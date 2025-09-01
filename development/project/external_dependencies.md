---
title: Add stripped spm2 and other toolboxes as external dependencies
---

{% include /shared/development/warning.md %}


Some FieldTrip functions use SPM2, SPM5 and EEGLAB for the actual computations. From these external toolboxes only limited functionality is used. Therefore it makes sense to copy those functions into a stripped-down version that can then be included in the release version of fieldtrip. E.g.

- fieldtrip/external/spm2 -> containing smoothing and segmentation
- fieldtrip/external/spm5 -> containing reading of nifti
- fieldtrip/external/eeglab -> containing runica

Better would be to get rid of SPM2 altogether and migrate SPM5 towards SPM8, but that requires real coding.

## Steps to take

- make inventory of external dependencies: which functions are involved
- add a copy of those functions to fieldtrip
- modify "hastoolbox" to ensure that it correctly recognizes the stripped down version
