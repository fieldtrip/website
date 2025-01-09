---
title: How does MTMCONVOL work?
parent: Spectral analysis
category: faq
tags: [freq]
---

# How does MTMCONVOL work?

With the mtmconvol method of **[ft_freqanalysis](/reference/ft_freqanalysis)** we effectively convolve the data with a complex wavelet, but computationally it is a little bit more involved: The wavelet is constructed by time-point wise multiplying the (real) cosine and (imaginary) sine component at each frequency with the specified tapering function. When using a Gaussian taper, this results in a Morlet wavelet. The Hanning taper that we often use has the practical advantage that the temporal spread is fully confined to the specified taper length (time window of interest), whereas with a Gaussian taper (which is infinitely wide) the taper needs to be truncated. Following the construction of the taper, both the data and tapered wavelet are Fourier transformed and element-wise multiplied in the frequency domain, after which the inverse Fourier transform is computed. By virtue of the [Convolution theorem](https://en.wikipedia.org/wiki/Convolution_theorem), this effectively results in a convolution of the complex wavelet with the data, but is computationally more efficient in case multiple tapers are employed (as the data only needs to be Fourier transformed once).

The same approach can also be used with multiple tapers, such as the DPSS sequence. This results in robust [multitaper](https://en.wikipedia.org/wiki/Multitaper) spectral estimates of power as a function of time, smoothed over a well-controlled frequency range.

Since the implemented method can be used either with a single taper of choice or with multiple tapers, we have dubbed it "mtmconvol" (multi-taper-method convolution), similar to "mtmfft" (multi-taper method fast Fourier transform).
