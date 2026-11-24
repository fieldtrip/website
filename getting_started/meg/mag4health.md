---
title: Getting started with MAG4Health OPM data
tags: [dataformat, meg, opm, mag4health]
category: getting_started
redirect_from:
    - /getting_started/mag4health/
---

[MAG4Health](https://www.mag4health.com) is a company based in France that develops optically pumped magnetometer (OPM)-based MEG systems using helium-4 quantum sensors. Their technology builds on room-temperature magnetometers originally developed for space applications and offers an alternative to conventional SQUID-based MEG systems, without the need for cryogenic cooling. The wearable OPM-MEG technology is designed to accommodate different head sizes and allow greater freedom of movement during recordings, with applications in both clinical and fundamental neuroscience research.

MAG4Health stores the data in the Neuromag fif format, which makes it directly accessible in FieldTrip and other MEG software.

Channels are named according to the sensor position, with the starting letter L and R for left and right, and Z for central sensors. The second letter codes for the approximate position over the brain lobe as F, C, T, P, O, similar to the naming scheme of the EEG [10-20 system](https://en.wikipedia.org/wiki/10–20_system_(EEG)).

Although the MAG4Health OPMs use a single laser, allowing the two orthogonal directions to be recorded with low noise, it also records the third (more noisy) direction. The radial direction is indicated by channels ending in `_r`, the first tangential direction is `_t` and the 2nd more noisy direction is `_t2`.
