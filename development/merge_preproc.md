---
title: Switch to using the preproc functions and phase out the old preprocessing code
layout: default
---

<div class="alert-danger">

The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas. 

The code development project mentioned on this page has been finished by now. Chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
</div>

# Switch to using the preproc functions and phase out the old preprocessing code

FieldTrip is being modularized to facilitate further development of the toolbox itself, and to facilitate reuse of the code in other projects (such as realtime analysis for BrainGain, or in EEGLAB or SPM8).

A "preproc" module has been made that contains all low-level functionality that is used in the fieldtrip/preprocessing function. The existing functions in fieldtrip that still use the old code have to be converted to using the new module. Subsequently, the old version of the functions should be removed from the FieldTrip release. This pertains to 

*  avgref.m

*  blc.m

*  bandpassfilter.m        

*  dftfilter.m             

*  lowpassfilter.m

*  bandstopfilter.m        

*  highpassfilter.m        

*  notchfilter.m

Also all use of other low-level code for preprocessing (e.g. detrending or median filtering) should be changed to use the respective preproc_xxx function. 

The most obvious function to start in is fieldtrip/private/preproc, but other fieldtrip functions are also affected (a.o. freqsimulation->bandpassfilter and probably the older artifact detection functions).

## To do

*  discuss the required changes to the code

*  inventorize affected functions
    * which functions will be removed
    * which functions will be modified
    * which old and unsupported functions will break (not necessarily a problem if deprecated)

*  modify the fieldtrip/private/preproc function

*  modify all other affected functions

*  remove the code that has become obsolete

## Affected functions

**avgref:**

*  dipolefitting.m

*  private/prepare_headmodel.m

*  private/preproc.m  -done-

**blc:**

*  artifact_ecg.m  -done-

*  combineplanar.m

*  componentanalysis.m -done-

*  resampledata.m -done-

*  timelockanalysis.m -done-

*  timelockbaseline.m -done-

*  private/artifact_viewer_old.m

*  private/preproc.m  -done-

**bandpassfilter:**

*  freqsimulation.m -done-

*  spikeanalysis.m

*  spikesimulation.m -done-

*  private/preproc.m  -done-

**all other filters:**

*  private/preproc.m  -done-

**detrend:**

*  componentanalysis.m -done-

*  resampledata.m -done-

*  private/preproc.m  -done-

**hilbert:**

*  spikeanalysis.m

*  private/preproc.m  -done-

## Functions that Robert should look into

**avgref:**

*  dipolefitting.m

*  private/prepare_headmodel.m

**blc:**

*  combineplanar.m

*  private/artifact_viewer_old.m

**bandpassfilter:**

*  spikeanalysis.m

**hilbert:**

*  spikeanalysis.m

## Usefull commands

    grep filter\( *.m

