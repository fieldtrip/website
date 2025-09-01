---
title: What are the differences between the old and the new implementation of 'mtmftt' in ft_freqanalysis?
category: faq
tags: [freq, mtmfft]
redirect_from:
    - /faq/what_are_the_differences_between_the_old_and_the_new_implementation_of_mtmfft_in_ft_freqanalysis/
    - /faq/what_are_the_differences_between_the_old_and_the_new_implementation_of_mtmfft_in_ft_freqanalyis/
    - /faq/freqanalysis_mtmfft_new/
---

Several things have changed in the new implementation of frequency analysis by the new low-level module 'specest'.

- All 'mtmfft' output is now phase-shifted such that any angle from any fourier-coefficient is from the perspective of the oscillation in the data being at its peak at time = 0
- 'mtmfft' can now take a cfg.foi input-vector as well, instead of the usual cfg.foilim (backwards compatible)
- In many cases the new implementation will run significantly faster. No increase in memory requirement has been seen so far.
