---
title: Integration with SPM8
---

{% include /shared/development/warning.md %}


    1) support of arbitrary EEG montages (elec.tra)
    2) scaling of electrophysiological data
    3) common coregistration function for FT and SPM
    4) use FT filtering and artifact detection in SPM
    5) use FT spectral analysis for SPM's TF and DCM-IR
    6) dipole fitting weighted with noise covariance
    7) support of continuous head localization in MEG

## Renaming functions and including FieldTrip and spm8 in each others repositories

Public FieldTrip functions (i.e. those used by end-users) will be renamed to ft_xxx. The code in fieldtrip/external/xxx will not be affected. The code in fieldtrip/fileio, plotting, forwinv, preproc and future modules (i.e. stand-alone toolboxes that are nevertheless integral part of fieldtrip) will follow the same naming scheme (so read_header will become ft_read_header). The code in the classification module probably won't change. Also some other sections probably won't change (uint64, config, statfun). The motivation behind it is that potentially confusing functions (preprocessing, read_data) are renamed and that functions which are explicit
ly shared among toolboxes will be renamed.
