---
title: FieldTrip/SIMBIO integration plan
---

{% include /shared/development/warning.md %}

The goal is to integrate the SIMBIO FEM model into FieldTrip.

this involves ft_prepare_vol_sens and ft_compute_leadfield

vgrid - geometric cube meshes will be discussed in the next meeting 18th of April

## Scenarios

Here is a [list of the typical scenarios](/development/project/simbio_scenarios) for which you would like to use SIMBIO, written from the user's perspective.

## Background Materials

Here are the [background materials](/development/project/simbio_materials) for the initial integration plan.

## Steps to be taken (Cristiano)

- Make a good example script to show the FieldTrip pipeline in generating BEM models lead fields
  - this requires an anatomical MRI and location of the electrodes to be shared: use standard_BEM mri (convert to nii) and elc files
  - how to read the elc and the nii
  - how to check the coregistration and if needed fix it
  - how to make the segmentation (based on the T1)
  - Subsequently for BEM the questions would be
    - how to make the BEM meshes (based on the segmentation)
    - how to make the BEM volume conduction model (based on the meshes)
    - how to make the BEM leadfield (based on the vol model and the electrodes)
  - and for FEM the questions would be
    - how to make the FEM meshes (based on the segmentation)
    - how to make the FEM volume conduction model (based on the meshes), done by SimBio??
    - how to make the FEM leadfield (based on the vol model and the electrodes), done by SimBio
    - how to read the FEM leadfield back into MATLAB, done by read_msr.m
  - how to plot the leadfield in MATLAB (using the 3d electrode positions)
- read simbio documentation, done
- how to write the fieldtrip/matlab data structures to files that SIMBIO understands, done
- how to read the SIMBIO output files back into matlab, done
- get the simbio binaries running under Linux CentOS 64-bit, release 5.2, done
- discuss with Robert about i) testing with practical datasets ii) meshing models programs like vgrid, done
- test write functions from Felix, done
- integrate dip,elc write functions in FieldTrip, done
- prepare a FT call to Simbio (for EEG only)
- understand how to call SimBio for MEG
- unerstand how to import a volume and generate a mesh for SimBio

## Steps to be taken (Johannes/Felix/Carsten)

- Get familiar with the FieldTrip toolbox / data structures / code style.
- Program all the needed readers/writers for EEG lead field computation with a given head model, electrode configuration and source space configuration.
- Extend the pipeline in the direction of model and source space generation in such a way that the user will need to do less model generation by himself. Preliminary goal: The only input data is a labeled MRI image. Subsequent steps:

  - Write i/o functions for vista format: We need to get the MRI image into the vista format, and the volume conductor model into MATLAB again >> We have to wait for Johannes for that purpose. He already started to work on these problems: Since vgrid (and the vista library) is open source we can also rewrite it with respect to the data formats it is using. We even thought about writing a .mex function that totally replaces the need for vgrid as an external binary. Than we would not need any i/o functions anymore.
  - Integrate functions to construct a source space for a given model in vista format.
  - Integrate vgrid to produce a model in vista format from a given labeled MRI image.

- MEG will be integrated at a later stage. We would need functions that produce FEM-models of the given MEG sensors automatically. This is not trivial and will need some time, care and testing (Somebody should be paid for doing it, it is nothing that can be done besides the normal work).

## Applications

to be discussed

## External links

- https://www.mrt.uni-jena.de/simbio/index.php/Main_Page
- http://www.rheinahrcampus.de/~medsim/vgrid/index.html
- http://www.ant-neuro.com/products/asa
- http://www.sci.utah.edu/cibc/software/106-scirun.html
