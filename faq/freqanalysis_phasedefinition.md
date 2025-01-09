---
title: What convention is used to define absolute phase in 'mtmconvol', 'wavelet' and 'mtmfft'?
parent: Spectral analysis
category: faq
tags: [freq, mtmconvol, wavelet, mtmfft, phase]
redirect_from:
    - /faq/what_convention_is_used_to_define_absolute_phase_in_mtmconvol_wavelet_and_mtmfft/
---

# What convention is used to define absolute phase in 'mtmconvol', 'wavelet' and 'mtmfft'?

- In **mtmconvol** and **wavelet** an angle of 0 of any fourier-coefficient means a peak of an oscillation in the data, and an angle of pi/-pi will always mean the trough of an oscillation (wavelet wise angle = 0 is implemented as cosine at peak, and sine in up-going flank)

- In **mtmfft** each Fourier-coefficient is phase-shifted such that the angle is from the perspective of the oscillation in the data being at its peak at time = 0. This means that when computing Fourier-coefficients, the (possibly variable) onset of each trial is taken into account.
