---
title: Can I use Octave instead of MATLAB?
tags: [octave]
category: faq
redirect_from:
    - /faq/can_i_use_octave_instead_of_matlab/
    - /faq/octave/
---

From the [Octave](https://www.gnu.org/software/octave) website: _"GNU Octave is a high-level interpreted language, primarily intended for numerical computations... The Octave language is quite similar to MATLAB so that most programs are easily portable."_

There are quite some people interested in this, mainly because Octave provides a free alternative to MATLAB. FieldTrip development primarily aims at MATLAB and at the Donders we do all our analyses in MATLAB. Many of the core computations that you can do with FieldTrip can in principle also be performed using Octave. Parts of the code (e.g., the plotting functions) are written in a way that is rather MATLAB specific.

Some people have reported that Octave works fine for them, although we don't have precise details on what works and what not.

Relevant is that Octave 3.4.0 is much faster on matrix operations than previous versions and has an improved compatibility with scripts and functions that have been written for MATLAB.

On the email discussion list there is a [relevant thread](http://mailman.science.ru.nl/pipermail/fieldtrip/2010-December/003339.html) that you might find interesting.
