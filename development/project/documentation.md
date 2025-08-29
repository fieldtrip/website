---
title: Ensure consistency of the documentation
---

{% include /shared/development/warning.md %}

# Ensure consistency of the documentation

## Tutorials

#### Preprocessing - trigger based trial selection

Done, all the code works (9 dec 2008)

### Preprocessing - manual artifact detection based on visual inspection

The code gives no errors but this tutorial has to be rewritten. The scaling options for rejectvisial changed. Now the eog / ecg channels can be scaled separately so you can reject trials based on the artifact channels. Because of these changes the data is not scaled properly and old cfg options are used.
There is also another fixme that has to be fixed. (9 dec 2008)

### Preprocessing - automatic artifact identification

### Event-related fields and the planar gradient

### Parametric and non-parametric statistics on event-related fields

### Fourier analysis of oscillatory power and coherence

### Time-frequency Analysis Using Multitapers and Wavelets

### Analysis of corticomuscular coherence

### Applying beamforming techniques in the frequency domain

In volumesegment you get 2 warnings:

- FINITE is obsolete and will be removed in future versions. Use ISFINITE instead.
- Can't get default analyze orientation - assuming flipped

The call to `sourceplot(cfg,sourceDiffIntNorm)` gives a plot with MRI but without sources. (15 dec 2008)

The structure `sourceDiffIntN` has no inside field, so it cannot be removed. Making the plot with method 'surface' afterwards gives an error 'undefind function or variable val'.

In the source statistics part there is cfg.grid=grid but grid is never defined. So there is an error there. Because of this error you cannot make sourceSTAT and therefore it is not possible to do the rest of the tutorial.

In this tutorial there are many lines with load .... (for any reason) but these files are not in the tutorial data that people download. Maybe they should be there because if a certain part doesn't work anymore they can load the results and work further. We could also include lines to save the results like in the first tutorial.

Because I didn't do source analysis myself until now I don't now the best way to solve these problems.(16 dec 2008)

### Statistics using cluster-based permutation tests

### Plotting data

### Working with animal electrophysiology data (LFPs and spikes.m)

### How to use checkconfig

## Example MATLAB scripts

### Align EEG electrode positions to BEM headmodel

### Apply clusterrandanalysis on TFRs of power that were computed with BESA

### Compute forward simulated data and apply a dipole fit

### Compute forward simulated data and apply a beamformer scan

### Correlation analysis of fMRI data

### Create BEM headmodel for EEG

### Create MNI-aligned grids in individual head coordinates

### Cross Frequency analysis in FieldTrip

### Detect the muscle activity in an EMG channel and use that as trial definition

### Determine the filter characteristics

### Effects of tapering for power estimates

### Fit a dipole to the tactile ERF after mechanical stimulation

### Getting started with reading raw EEG or MEG data

### Make leadfields using different headmodels

### Making your own trialfun for conditional trial definition

### Use independent component analysis (ICA) to remove ECG artifacts

### Use your own forward leadfield model in an inverse beamformer computation

### Writing simulated data to a CTF dataset

### Fixing a missing sensor

### Using 3rd order gradients for CTF data

### Source reconstruction using symmetric dipole pairs
