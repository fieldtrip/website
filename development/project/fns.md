---
title: Provide an interface to the FNS software for FDM modelling
---

{% include /shared/development/warning.md %}

# Provide an interface to the FNS software for FDM modelling

The Finite Difference Neuroelectromagnetic Modeling Software (FNS) is a toolbox developed by Hung Dang (Please send your comments and suggestions to hungptit@gmail.com) and has the interesting feature of building forward models based on volumetric features of the volume conductor.

## Goals

Integrate the forward model part of FNS in FieldTrip.

Q: What about the inverse modelling?

A: All inverse methods in FieldTrip are independent from the forward model, i.e. there is a function that computes a leadfield and another function that uses it together with the data to make an estimate of the source. This allows the complete collection of inverse methods to be used either for MEG, MEG and ECoG data.

## Features

1. FNS computes the forward solution starting from segmented volumes (does not require necessarily meshes as input, but uses FSL (if installed) to segment them)
2. The output of FNS is a volumetric image representing the voltage in all points of the space
3. FNS on a Linux machine requires MATLAB and [Bioelectromagnetism MATLAB toolbox](http://eeg.sourceforge.net/) (for time series visualization?)
4. To run FNS forward solver a user need to have 1 GByte of memory available

## How it works

First create and store the system matrix in output file data.h

    # Example of Linux shell command
    elecsfwd --img smri-seghead --electrodes electrodes.h5 --data data.h5 --contable  ../../data/conductivity/contable.csv --TOL 1e-8'

The smri-seghead file is the name of a analyze format file (.hdr, .img) which contains the segmentations with the assigned tissue values (e.g., gray matter = 1, white matter =2, or single sphere = 1).

electrodes.h5 contains the electrodes matrix with a row for each electrode and 4 columns (X,Y,Z positions of the electrode in voxel space) and label.

contable.csv is a comma separated file which assigns a conductivity value for each tissue type present in the analyze file.

## Steps to be taken

1. create the necessary interfaces (meshes, conductivities, sensors structures)
2. create a wrapper to run the binaries
3. The call to elecsfwd should be modified as follow

- input arguments --img segfile and --electrodes elecs disappear, they are substituted by two other arguments called --dim and --3dmesh
- the input argument --3dmesh contains the coordinates of the voxels' centers (all and only voxels belonging to the head) and an additional columns with the tissue label of each voxel. The resulting matrix V has dimensions [N (head voxels) X 4]
- the input argument dim contains the dimensions of the MRI (e.g., 256X256X256] in order to be able to build the box around the head
- output argument --data datafile now contains only a matrix M of dimensions [skinXbrain voxels], no additional fields
- provide Hung with 2 files: one segmented labeled MRI, one text file with the output voxels, containing the positions of the solutions in voxels coordinates

## Steps to be taken (Cristiano)

1. Understand how to initialize all the elements used by elecsfwd function to calculate the leadfield
   in particular:

- smri-seghead: the segmentation mesh file format (can it be a .mat file?)
- electrodes.h5: the electrodes positions file (in head coordinates?)
  - how do we read/plot elecs if we have h5 file?
- data.h5: time courses of the electrodes (?), no output
  - how do we read/interpret its content? (contains lf?)
  - how to determine if h5 file is elecs or lf...?
- contable.csv: conductivity table (do not understande really the organization of this)
- tolerance: of what?
- what is the format h5? done

2. Understand how to retrieve them (from disk? in memory?) done
3. Discuss the integration of MKL no commercial libraries in the frame of GPL license of Linux (and Windows), try without any intel libraries, try libraries of octave (is modular)
4. Ask for a more handy download scheme from FNS site (ftp link to zip file). Done. I have uploaded the archived here http://hhvn.nmsu.edu/uploads/fns/fns.tar.bz2
5. The makefile shows dependency from FDM folder, using the default compiler (gcc) (see make.inc), never tested for other compilers than Intel probably
6. libguide.so is not available as seems to be again an intel thingie
7. Ask for references papers (Hung Dang and Kwong Ng) -> done
8. New statically linked binaries work with libc 2.7 onwards (my system is not compatible), document the feature and test it on a higher system -> done ( new bins available linked with old libraries )
9. Ask for a downgrade of GPL licensing from "3 or higher" to "2 or higher" (more code compatible with FieldTrip license). Done -> Hung: I have changed from 3.0 to 2.0 version.

## Steps to be taken (Hung)

1. Update load the test data for FNS. Done

2. Clean update FNS code

   - Rename all FNS routine prefix to 'fns\_'

3. Update notes about the beamforming algorithms

   - Will upload papers and posters

4. Take the electrode rereferencing out of the main binary. Done

   - FNS does not do any referencing.
   - User need to specify the reference technique and FieldTrip will handle this.

5. System matrix has to be extracted from data.h5 output as previously calculated from 'elecs_fwd'.

   - Create a MATLAB function with as input argument the tissue type and as output the correspondent system matrix. Done with the C version. Working on the MATLAB version now.

6. Add usage and other information to all binaries. Updating.

7. Redesign FNS

   - Forward solver will have

     - Inputs

       - The segmented volume image
       - Fitted electrode grid locations (in MRI coordinate)
       - Dipole locations

     - Output
       - All computed forward solvers
       - Some other information to extract the lead field matrices including model sizes, voxel sizes (optional), mapping vector (internal usage only it will be used only when user want to reduce the memory).

8. Current version

- Compute all forward solutions and save to a file.
  - This routine could be threaded using OpenMP, however, the required memory may growing substantially then just disable it for now.
  - Will add a better parallelism technique later for the next release.
- Either C or MATLAB routine could be used to compute the lead field matrix (NELECx3\*NDIPOLE matrix) of a given set of dipoles (3xNDIPOLE matrix)
- Need to do referencing before using the lead field matrix

## External links

1. Wiki page http://hunghienvn.nmsu.edu/wiki/index.php/FNS
2. FNS source code http://hunghienvn.nmsu.edu/uploads/fns/
3. FNS test data: http://hunghienvn.nmsu.edu/uploads/others/testdata/
