---
title: What does "padding not sufficient for requested frequency resolution" mean?
category: faq
tags: [freq]
---

# What does "padding not sufficient for requested frequency resolution" mean?

This means the frequency resolution in your cfg.foi cannot be attained by the current padding in cfg.pad. There are two solutions to this problem:

1.  change your cfg.foi
2.  change your cfg.pad

In order to do either of these, it is important to understand what the frequency resolution of your data is, and you can 'manipulate' it. The frequency resolution of any signal to be analyzed depends on the Rayleigh frequency of the data. The Rayleigh is equal to 1/T, with T being the time (in seconds) of the trial that you are analyzing. Using the Rayleigh frequency you can determine what frequencies can be estimated, namely: 0:Rayhleigh:Fsample/2 (Fsample/2 being the Nyquist frequency). So, if the length of your trial is 2.350s and you sample your data at 1000 Hz, the frequencies you can estimate are 0:(1/2.35):500. I.e. [0 0.4255 0.8511 1.2766 .... 499.1489 499.5745 500].

Usually, this is undesirable because it is difficult to work with, and can change across trials if you have variable trial lengths. This last problem is solved by padding each trial out with zeros so they are all of equal length. This changes the frequencies you can estimate from your data by artificially creating longer T's (and thus changing the Rayleigh frequency). Importantly though, this does not (!) change the intrinsic frequency resolution of your data. The same trick can be used to solve the first problem. All you need to do is make sure you pad your data out to an integer number of seconds.

An easy way to specify an appropriate integer seconds that is sure to fit the length of your maximum trial is to do

    cfg.pad = ceil(max(cellfun(@numel, data.time)/data.fsample));
