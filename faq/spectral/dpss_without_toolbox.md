---
title: Why do I get an error about dpss, and what can I do without the Signal Processing Toolbox?
tags: [freq, matlab, octave]
category: faq
---

FieldTrip's multitaper spectral estimation (**[ft_freqanalysis](/reference/ft_freqanalysis)** with `cfg.method = 'mtmfft'` or `'mtmconvol'` and the default `cfg.taper = 'dpss'`) uses Slepian tapers computed by the `dpss` function of the MATLAB Signal Processing Toolbox. Without that toolbox, or under GNU Octave, the analysis stops with a message such as

    Undefined function 'dpss' for input arguments of type 'double'.

or, under Octave,

    error: 'dpss' undefined

You have three options.

## Use a taper that does not need the toolbox

Set `cfg.taper = 'hanning'`. FieldTrip ships its own `hanning` in `external/signal`, so this works everywhere. It gives a single-taper estimate: there is no spectral smoothing across frequencies, so `cfg.tapsmofrq` is not used. This is the usual choice for low-frequency activity, and the tutorials that use multitapers for high-frequency (gamma) activity can be run with `'hanning'` at the cost of a noisier high-frequency estimate.

## Use sine tapers

Set `cfg.taper = 'sine'` and specify `cfg.tapsmofrq` as you would for `'dpss'`. Sine tapers (Riedel and Sidorenko, 1995) are an orthogonal family that approximates the Slepian sequences; FieldTrip implements them itself, so no toolbox is needed. They give the spectral smoothing of the multitaper method with slightly worse sidelobe suppression than true Slepian tapers.

## The dpss_hack (not recommended)

The directory `external/signal/dpss_hack` contains a `dpss` replacement that interpolates precomputed Slepian tapers. It was made for a workshop in 2013, is only an approximation for settings close to the precomputed ones, and it cannot be used with the `'mtmfft'` method at all, because that method also needs the taper concentrations that the hack does not return (see [issue 2614](https://github.com/fieldtrip/fieldtrip/issues/2614)). Prefer one of the two options above.

Under GNU Octave, the first two options are the ones that work; see also [Can I use Octave instead of MATLAB?](/faq/matlab/octave)
