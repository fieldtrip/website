---
title: 27 November 2020 - Bug in ft_sourceanalysis with the DICS method
category: news
tweet: Attention fieldtrippers! Sadly, we found a bug in FieldTrip starting from release 20200701. It concerns ft_sourceanalysis with the DICS method. See https://www.fieldtriptoolbox.org/#27-november-2020 for more information.
---

### 27 November 2020

Regretfully we identified a bug in FieldTrip releases starting from release [20200701](https://github.com/fieldtrip/fieldtrip/releases/tag/20200701) onward, which might have affected your results.

Specifically, if you have been using `ft_sourceanalysis` with DICS as a method, **and** if the order of the channels of the input data structure was not alphabetical, the results are incorrect. This is caused by an accidental alphabetical reordering of the channels in the cross-spectral density matrix, which was not reflected by a similar reordering in the leadfields. We are grateful to Alexandra Steina to help us identify and resolve it. See [issue #1587](https://github.com/fieldtrip/fieldtrip/issues/1587) on GitHub for more information. 

Are you affected? If you used a FieldTrip version between **20200701** and **20201126**, and you used `ft_sourceanalysis` with method DICS, and your channels are _not_ in alphabetical order, then you are likely affected. For CTF MEG data the channels are usually in alphabetical order. Neuromag/Elekta MEG data, and MEG data from other systems often have the channels _not_ in alphabetical order. The same holds for EEG data, so your results are likely affected if you are working with EEG data, or non-CTF MEG data.

To resolve the problem, please update to the latest **20201126** release version from the [download server](https://download.fieldtriptoolbox.org/) or from the [GitHub release page](https://github.com/fieldtrip/fieldtrip/releases), recompute your source estimates, and your downstream results.
