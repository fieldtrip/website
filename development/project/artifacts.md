---
title: Improve artifact handling
---

{% include /shared/development/warning.md %}


With the initial focus in development on MEG data, we have mostly relied on not having (many) bad channels, and on rejecting segments based on unwanted data (e.g., physiological or behavioural artifacts, such as eye blinks) rather than recording hardware instabilities (such as electrodes moving). We typically reject affected segments from further analyses, and can also exclude channels, or if needed (e.g., for grand-averaged ERPs) to interpolate channels. This is documented [here](/tutorial/preproc/artifacts).

However, now that we are processing more EEG and NIRS data, also from patients and infants, we more frequently have to deal with “sparse artifacts”, i.e. the situation that we want to reject a piece of data from a single channel, but not the channel as a whole, nor the segment as a whole.  Hence we want to extend on the strategy that we already have, which is to use NaNs for artifacts. Besides rejecting segments and channels as a whole, this allows to flag a bad piece of data in a single channel by filling it with nans. The ft_rejectvisual GUI needs to be extended, the representation of these artifacts needs to be checked (it is already partially implemented), and compatibility in downstream functions and in representations on disk (e.g., with data2bids) needs to be improved.

## MATLAB for Neurosciece summer projects

Improving the artifact handling has been listed as part of the MATLAB for Neurosciece summer projects [#1](https://github.com/fieldtrip/fieldtrip/issues?q=is%3Aissue+project%3Afieldtrip/fieldtrip/3) and [#2](https://github.com/fieldtrip/fieldtrip/issues?q=is%3Aissue+project%3Afieldtrip/fieldtrip/4), but it is not so likely that this project will receive attention in the summer of 2021.
