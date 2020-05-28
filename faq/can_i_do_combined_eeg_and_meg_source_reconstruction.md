---
title: Can I do combined EEG and MEG source reconstruction?
tags: [faq, eeg, meg, headmodel, source]
---

# Can I do combined EEG and MEG source reconstruction?

In principle the answer is "yes". However, it is sofar only supported by the low-level code in [forwinv](/development/forwinv) and not by the high-level FieldTrip functions such as **[ft_dipolesimulation](https://github.com/fieldtrip/fieldtrip/blob/release/ft_dipolesimulation.m)**, **[ft_dipolefitting](https://github.com/fieldtrip/fieldtrip/blob/release/ft_dipolefitting.m)** and **[ft_sourceanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_sourceanalysis.m)**.

[Here](/example/combined_eeg_and_meg_source_reconstruction) is an example that demonstrates combined forward computations. Inverse source reconstructions using the low-level code should work similar, i.e. by combining the EEG and MEG sensor definitions and volume conduction models into a cell-array.

The same approach can also be used for combined EEG and iEEG, or combined MEG and iEEG, or any other data fusion. Furthermore, note that the combination of volume conduction models can contain more realistically and accurate forward models than the spherical models used in the example.
