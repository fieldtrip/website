---
title: 01 July 2020 - Cleaned up the inverse module
categories: [news]
---

### 01 July 2020

In FieldTrip release [20200701](https://github.com/fieldtrip/fieldtrip/releases/tag/20200701) the low-level functions in `fieldtrip/inverse` have been renamed to `ft_inverse_xxx` and their input and output arguments have been cleaned up. This addresses a long-standing [plan](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=208) for improving the [inverse modeling API](/development/module/inverse). Except for the renaming of the low-level functions (which you won't notice if you call them through the high-level `ft_sourceanalysis` and `ft_dipolefitting`) there are no functional changes.
