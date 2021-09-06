---
title: Getting started with Blackrock data
tags: [dataformat, blackrock, lfp, spike]
---

# Getting started with Blackrock data

The specifications of the Blackrock file formats can be found on [the company's website](http://support.blackrockmicro.com/). Blackrock files come in 2 flavors. One file type has the extension `.nev`, and contains information about extracellularly recorded spiking activity. The other file type has as extension `.nsX`, with X any number between 1 and 9. These files contain continuously sampled data, e.g.,  local field potentials.

To read Blackrock data, you will need the NPMK toolbox. The latest version is available from <https://github.com/BlackrockMicrosystems/NPMK>.

At this moment FieldTrip does not offer a complete implementation for importing Blackrock data. We are looking for people to help with implementing it. See [bug #2964](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=2964) and [issue #1323](https://github.com/fieldtrip/fieldtrip/issues/1323).
