---
layout: default
tags: [faq, freq, mtmconvol]
---

## Why does my output.freq not match my cfg.foi when using 'mtmconvol' in ft_freqanalyis?

Conceptually, a time frequency analysis is a time domain convolution of a signal with a set of wavelets, each of these being designed to capture some feature in the data. The 'mtmconvol'-method uses sine/cosine waves, tapered with multitapers, which are designed to capture band-limited oscillations in the data. When doing a spectral decomposition, the goal typically is to assign the fluctuations in the signal to distinct frequency bands. Importantly, the (implicitly) required behavior of the spectral transformation is, that the power estimated at X Hz truly comes from signal fluctuations at X Hz., and not from signal fluctuations at Y Hz. (and Z Hz etc). This is the issue of spectral leakage, and a few signal processing tricks are needed to optimally control for this.
In the context of wavelet analysis in FieldTrip and in order to minimize detrimental effects of (unpredictable spectral leakage), you need to keep 2 things in min

*  The length of the wavelet at frequency X should fit an integer number of cycles of the wavelet's frequency. If this is not the case, the wavelet becomes sensitive to other frequencies in the data as well, thus making the wavelet less specific to the wished-for frequency, and vulnerable to spectral leakage.

*  The total length of the data (your trials) should yield a frequency resolution that captures the frequencies of your spectral decomposition (your cfg.foi). This is because in its implementation FieldTrip uses the trick "convolution in the time domain is equivalent to multiplication in the frequency domain". In other words, rather than convolving the time domain signal with the wavelets of different frequencies, the fourier representation data is multiplied with the fourier representation of the wavelets (and the inverse fourier transform is computed to get to the time domain representation again). If there is a mismatch between the frequencies specified in cfg.foi, and the inherent frequency resolution of the data (given by the length T, i.e. the frequency resolution is 1/T), some implicit spectral interpolation is done, which is particularly vulnerable to spectral leakage effects.

So, to make a long story short: in order to protect the user against him/herself the new implementation in the specest-module checks for potential discrepancies, and corrects the cfg.foi, if needed. Therefore, if you wish for particular frequencies in your TFR, you need to think twic

*  Do the cfg.t_ftimwins yield an integer number of cycles for each requested frequency?

*  Is the length of my data such, that the frequency resolution 1/T can capture all cfg.foi? This means, in other words, that (cfg.foi * T) should be integer numbers. 

Hint: The length of the data can be influenced with the cfg.pad parameter.
