---
title: Why should I set cfg.continuous = 'yes' when preprocessing CTF trial-based data?
tags: [faq, ctf, preprocessing, continuous]
authors: [Konstantinos Tsilimparis, Robert Oostenveld]
---

# Why should I set cfg.continuous = 'yes' when preprocessing CTF trial-based data?

The CTF acquisition software by default writes data to disk in blocks. The length of these blocks can be configured, and at the DCCN this is set to 10 seconds. So the continuous recording is actually pseudo-continuous and consists of blocks of 10 seconds, where block N is followed smoothly without gaps by block N+1. However, the CTF acquisition software can also be configured to only write a block of data to disk upon a trigger. This results in "epoched" data, where only the data corresponding to the trial is written to disk and the data in the inter trial intervals is not. In this case there is a gap between block N and block N+1. If you were to read the epoched data as if it were continuously, you won't see the gaps as such along the time axis, but you will see jumps in the data as the signal may have drifted from block N to block N+1. 

FieldTrip does not distinguish between the CTF files that are written as blocks in continuous mode, without gaps, and CTF files that are written as epochs with gaps between the blocks. The low-level reading functions by default will give an error when you try to read data that extends over a boundary between two blocks, but the `cfg.continuous` option in **[ft_preprocessing](/reference/ft_preprocessing)** allows you to override that.

The "Subject01.ds" CTF dataset that is used in some tutorials is epoched and has gaps between the trials. If you were to read that as continuous, you would see discontinuities in the MEG channels. If you were to apply the automatic artifact detection functions on that as continuous data, many trials would be detected as an artifact as they start/end with a discontinuous jump in some of the channels. Hence when reading that data the `cfg.continuous` option should be set to `"no"` (which is the default).

Many other CTF datasets are recorded as pseudocontinuous without gaps between the blocks and for those you do want to set the `cfg.continuous` option to `"yes"`. 

To check whether your data is epoched or pseudocontinuous, please have a look at the `SCLK01` channel.

Note that besides **[ft_preprocessing](/reference/ft_preprocessing)**, other functions that read data from disk also have the `cfg.continuous` option, such as  **[ft_databrowser](/reference/ft_databrowser)** and the automatic artifact detection functions.
