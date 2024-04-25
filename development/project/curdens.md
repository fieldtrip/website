---
title: How to create a volumetric current density
---

{% include /shared/development/warning.md %}

# How to create a volumetric current density

{% include markup/blue %}
Upon reviewing this page on the website, it seems to me that this project is not going to happen. Although the FieldTrip code base might be used (in combination with other code), the released code will not be extended to specifically facilitate this.
{% include markup/end %}

## Introduction

What is the tutorial about

This is relevant for TMS tDCS ....

## Background

What is TMS/tDCS

Why we need current densities

Overview about the methods which are used

## Procedure

A set of logical steps describing the pipeline, in MATLAB, FieldTrip code or also from somewhere else (e.g., FreeSurfer)

Examples with code/command lines instructions

**@Cristiano**

- segment inner skull from CT
- segment the outer brain from the MRI
- project the electrodes from CT onto inner skull (CT space)
- superimpose two surfaces (electrodes are expressed in brain coordinates afterwards)
  This is done in SPM by coregistration of the CT to MRI images.
  This automatically gives the transfer matrix from CT to MRI coordinates (and hence you also have the electrodes expressed in MRI coordinates)

- check the surface does not contain self intersections
- mesh the brain triangulation with Tetgen
- assign conductivity to nodes -> elements

**@Arno**

- convert mesh pnt and tri into a structure readable by Tetgen (.poly and .nodes)
- run Tetgen
- collect result (.node, .ele, (maybe .faces))

**@All**

- write wfmesh/elec/parameters/cond on disk
- run SimBio solver

Alternatively (interactive)

- write .mat files : elec/wfmesh/cond
- write a SciRun schematic
- run SciRun
- collect solution and save it in a .mat file

**@Robert**

- discuss next steps

### Questions

Is the output of SimBio/SciRun the stiffness matrix (profiles of current in the head)?
(input: current, output: spatial current density)

## Summary

General conclusions

## Suggested readings

Other FT documentation pages
