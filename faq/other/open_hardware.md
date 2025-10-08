---
title: Where can I find open hardware for MEG and EEG?
tags: [hardware, sharing]
category: faq
---

{% include markup/yellow %}
Feel free to hit the **edit** button at the bottom of this page to add links to other open hardware resources.
{% include markup/end %}

MEG and EEG labs are typically organized around equipment from commercial companies. However, there are also bits and pieces in the labs that are not commercially available (yet) and that are designed and built by the researchers themselves or their technical support groups. Especially with the development of MEG using more flexible OPM sensors there are now a lot of custom helmets and mounts being developed. Various labs share details of hardware for MEG or EEG equipment, allowing others to reuse or build on their developments. This page aims to collect pointers to open hardware for MEG and EEG.

## Cryogenic MEG headcasts

At the Donders we are using 3D printing for [flexible head-casts](https://github.com/Donders-Institute/meg_headcast) to restrict head movement and to achieve high spatial precision MEG with our CTF system. This strategy was initially developed at Aston University and the FIL by Gareth Barnes (see [this paper](https://doi.org/10.1016/j.jneumeth.2016.11.009)), and Gareth shared details with us which we used to develop the procedure that we now use at the Donders.

## Nulling coils for OPMs

The [bfieldtools](https://bfieldtools.github.io) package is Open-source Python software for magnetic field modeling, that can be used to design the wiring pattern of field nulling coils for OPM setups.

Mainak Jas has shared a [paper](https://doi.org/10.3390/s25092759) with corresponding [code and design details](https://github.com/opm-martinos/opm_coils) on Github for the design and construction of biplanar nulling coil using printed-circuit boards (PCBs).

QuSpin has documented in a [Google doc](https://docs.google.com/document/d/1e3LUfdOmUhHHBT-lbirucRoW1TdrYyMxdaS1W-6WDjA/edit?tab=t.0) a simple procedure for installing residual field nulling coils in along the walls of an MSR. This can be used with their [coil driver](https://quspin.com/low-noise-coil-driver/), but you can also make your own low-noise coil driver.

## MEG phantoms

Tim Bardouille has shared [instructions](https://github.com/tbardouille/MEG_biosignal_phantom) to construct a dry phantom for MEG. It is resembles the Neuromag/Elekta/MEGIN phantom, is based on a PCB, and results in magnetic fields that can be fitted as a equivalent current dipole in a spherical volume conductor.

## EEG phantoms

David Hairston and Alfred Yu have shared the [instructions](https://osf.io/qrka2/) for fabricating a phantom for EEG and similar electrophysiology recordings.

## MRI hardware

Although this FieldTrip website is not the most logical place to search for or to document open MRI software and hardware, we do want to point out the review paper on [Open-source magnetic resonance imaging](https://doi.org/10.1002/nbm.5052) by Lukas Winter and colleagues. It provides links to open software and hardware resources, for example the [Open Source Imaging Initiative](https://gitlab.com/osii).
