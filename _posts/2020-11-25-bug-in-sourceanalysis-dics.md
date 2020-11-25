---
title: 25 November 2020 - Bug in sourceanalysis DICS
categories: [news]
tweet: Attention fieldtrippers! Sadly, we found a bug in Fieldtrip releases starting from release 20200701.. This bug mainly concerns (ft_sourceanalysis) with "DICS" as a method. Please see https://github.com/fieldtrip/fieldtrip/issues/1587 for more information.
---

### 25 November, 2020

Regretfully we identified a bug in FieldTrip releases starting from release [20200701](https://github.com/fieldtrip/fieldtrip/releases/tag/20200701), which might have affected your computations.

Specifically, if you have been using `ft_sourceanalysis` with DICS as a method, **and** if the order of the channels of the input data structure was not alphabetical, the results might have been wrong. The cause of all this was an accidental reordering of the order of the channels in the data cross-spectral density matrix (according to alphabet), which was not mirrored by a similar reordering in the leadfields. We are grateful to Alexandra Steina to point us to the problem, and to help us resolve it. See [Github issue #1587](https://github.com/fieldtrip/fieldtrip/issues/1587) for more information. 

Are you affected? If you used the master branch from GitHub (which is the development version), or a release version between **20200701** and **20201126**, and if you have used `ft_sourceanalysis` for MEG with DICS, and your channels in the data are not in alphabetical order (e.g.: for the CTF MEG they are, so you are probably fine, for EEG data they are probably not, neither are they in the other MEG systems), then you are likely affected. 

To resolve the problem, please update to the latest **20201126** release version from the [FTP server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/) or from the [GitHub release page](https://github.com/fieldtrip/fieldtrip/releases) and recompute your source estimates and downstream results.
