---
layout: default
---

{{tag>faq eeg meg headmodel source}}

# Can I do combined EEG and MEG source reconstruction?

In principle the answer is "yes". However, it is sofar only supported by the low-level code in [:development:forwinv](/development/forwinv) and not by the high-level FieldTrip functions such as **[ft_dipolesimulation](/reference/ft_dipolesimulation)**, **[ft_dipolefitting](/reference/ft_dipolefitting)** and **[ft_sourceanalysis](/reference/ft_sourceanalysis)**.

[Here](/example/combined_eeg_and_meg_source_reconstruction) is an example that demonstrates how forward computations can be done. Inverse source reconstructions using the low-level code should work similar, i.e. by combining the eeg and meg sensor definitions and volume conduction models into a cell array. 

Note that the same approach can also be used for combined EEG and invasive EEG, or combined MEG and invasive EEG, or any other data fusion. Furthermore note that the combination of volume conduction models can  contain more realistically and accurate forward models than those used below.  


