---
title: Where can I find the dipoli command-line executable?
layout: default
tags: [faq, headmodel, source, matlab]
---

## Where can I find the dipoli command-line executable?

The Boundary Element Method (BEM) allows for source reconstruction of EEG data with realistic head geometries. FieldTrip implements the BEM method for EEG in a general fashion in the forward "leadfield_computation" function. However, this requires that a previously prepared BEM model is passed to the "sourceanalysis" function or to the "dipolefitting" function. To construct such an EEG BEM model, you can use the "prepare_bemmodel" function, where in cfg.method you should specify dipoli or bemcp. 

Dipoli is a command line application that was developped by [Thom Oostendorp](http://www.mbfys.ru.nl/~thom). You can download the linux version version from ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/external. You should unzip it and copy it to fieldtrip/external/dipoli. Note that there is no windows version available. 
The dipoli-executable for Linux was compiled on a 32bit system. In order to run it on a 64bit system, you need to install the "ia32-libs" library (sudo apt-get install ia32-libs). On newer systems, ia32-libs are deprecated so you should enable the i386 architecture (sudo dpkg --add-architecture i386 && sudo apt-get update) and install the 32-bit libraries (sudo apt-get install libc6:i386 libstdc++6:i386).

BEMCP is a MATLAB toolbox for BEM modeling, developed by Christophe Phillips from the Universite Liege in Belgium. It is available from ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/external and should be installed under the directory fieldtrip/external/bemcp.

