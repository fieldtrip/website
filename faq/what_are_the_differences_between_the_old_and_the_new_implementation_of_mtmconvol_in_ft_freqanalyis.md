---
title: What are the differences between the old and the new implementation of 'mtmconvol' in ft_freqanalyis?
category: faq
tags: [freq, mtmconvol]
---

# What are the differences between the old and the new implementation of 'mtmconvol' in ft_freqanalyis?

Several things have changed in the new implementation of frequency analysis by the new low-level module 'specest'.

- All output is now phase-shifted such that an angle of 0 of any fourier-coefficient always means a peak of an oscillation in the data, and an angle of pi/-pi will always mean the trough of an oscillation (wavelet wise angle = 0 is implemented as cosine at peak, and sine in up-going flank)
- 'mtmconvol' now uses an accurate frequency vector for building its wavelets (determined by fsample and nsample, with cfg.foi as starting point), instead of an uncorrected cfg.foi. In many cases this will cause frequencies like e.g., 4.0978 to show up in the output. This is not an _inaccuracy_, it is _more precise_ labeling of the frequency content. This means that it is _very important_ to make sure you _zero-pad datasets to an equal length_ (using cfg.padding) that you want to compare later on: the output-foi must be identical.
- In many cases, the new implementation will run significantly faster. However, in some case there might be slight increase in memory requirement.
