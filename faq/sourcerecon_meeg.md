---
title: Can I do combined EEG and MEG source reconstruction?
parent: Source reconstruction
category: faq
tags: [eeg, meg, headmodel, source]
redirect_from:
    - /faq/can_i_do_combined_eeg_and_meg_source_reconstruction/
---

# Can I do combined EEG and MEG source reconstruction?

In principle the answer is "yes". However, it is sofar only supported by the low-level code in [forwinv](/development/forwinv) and not by the high-level FieldTrip functions such as **[ft_dipolesimulation](/reference/ft_dipolesimulation)**, **[ft_dipolefitting](/reference/ft_dipolefitting)** and **[ft_sourceanalysis](/reference/ft_sourceanalysis)**.

[Here](/example/combined_eeg_and_meg_source_reconstruction) is an example that demonstrates combined forward computations. Inverse source reconstructions using the low-level code should work similar, i.e. by combining the EEG and MEG sensor definitions and volume conduction models into a cell-array.

The same approach can also be used for combined EEG and iEEG, or combined MEG and iEEG, or any other data fusion. Furthermore, note that the combination of volume conduction models can contain more realistically and accurate forward models than the spherical models used in the example.
