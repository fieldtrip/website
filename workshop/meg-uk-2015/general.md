---
title: General instructions for MATLAB demo's
tags: [meg-uk-2015]
---

We have installed the demo dataset, MATLAB 2013b and a tested copy of FieldTrip and SPM12 on the lab computers.

## SPM instructions

Start MATLAB and type

    restoredefaultpath
    addpath c:\workshop\spm12
    spm eeg

    cd c:\workshop

## FieldTrip instructions

The FieldTrip demonstrations all share the same preprocessed data (i.e. .mat files), which a are gathered in the ''fieldtrip-demo'' folder. Prior to executing sections of the MATLAB demo scripts from the website, you should therefore change into that directory.

Start MATLAB and type

    restoredefaultpath
    addpath c:\workshop\fieldtrip
    ft_defaults

    cd c:\workshop\fieldtrip-demo
