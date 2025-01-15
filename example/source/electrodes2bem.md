---
title: Align EEG electrode positions to BEM headmodel
category: example
tags: [eeg, mri, source, headmodel]
redirect_from:
    - /example/align_eeg_electrode_positions_to_bem_headmodel/
    - /example/electrodes2bem/
---

# Align EEG electrode positions to BEM headmodel

## Description

To use accurate individual volume conduction models of the head (or "head models") in inverse source reconstruction of EEG data, we construct a head model from the individual MRI. Furthermore, it is necessary to express the electrode positions in the same coordinate system and units as the MRI and head model.

This script demonstrates how to transform electrode positions to the individuals MRI space using the 3 fiducial points that correspond to the anatomical landmarks 'nasion', 'preauricular left' and 'preauricular right'. In the example below the position of these three anatomical landmark locations is specified in the electrode structure as if they were normal electrodes.

Furthermore, it is necessary to provide the voxel coordinates of the same fiducial points in the MRI. Typically the MRI is aligned to MNI space, thus the resulting electrode positions are as well aligned to MNI space.

## MATLAB script

    % fit electrode coordinates to an individual MRI according to the same
    % fiducials (nasion, left & right preauricular points) in both systems

    % ensure that the electrode coordinates are in mm
    elec = ft_convert_units(elec,'mm'); % should be the same unit as MRI

    % these are expressed in the coordinate system of the electrode position capture device
    Nas = elec.chanpos(strcmp(elec.label, 'nasion'),:);
    Lpa = elec.chanpos(strcmp(elec.label, 'left'),:);
    Rpa = elec.chanpos(strcmp(elec.label, 'right'),:);

    % determine the same marker locations in voxel coordinates, e.g., [57,127,15])
    % find fiducials e.g., by using ft_sourceplot(cfg, mri) which plots a figure in which
    % you can interactively select slices of the mri
    % You can also use ft_volumerealign with cfg.interactive='yes' and obtain the fiducials from the output.cfg.fiducial

    vox_Nas = mri.nasion;  % fiducials saved in mri structure
    vox_Lpa = mri.left;
    vox_Rpa = mri.right;

    vox2head = mri.transform; % transformation matrix of individual MRI

    % transform voxel indices to MRI head coordinates
    head_Nas          = ft_warp_apply(vox2head, vox_Nas, 'homogenous'); % nasion
    head_Lpa          = ft_warp_apply(vox2head, vox_Lpa, 'homogenous'); % Left preauricular
    head_Rpa          = ft_warp_apply(vox2head, vox_Rpa, 'homogenous'); % Right preauricular

    elec_mri.chanpos = [
      head_Nas
      head_Lpa
      head_Rpa
      ];
    elec_mri.label = {'nasion', 'left', 'right'};
    elec_mri.unit  = 'mm';

    % coregister the electrodes to the MRI using fiducials
    cfg = [];
    cfg.method   = 'fiducial';
    cfg.template = elec_mri;
    cfg.elec     = elec;
    cfg.fiducial = {'nasion', 'left', 'right'};
    elec_new = ft_electroderealign(cfg);

    % interactively coregister the electrodes to the BEM head model
    % this is a visual check and refinement step
    cfg = [];
    cfg.method    = 'interactive';
    cfg.elec      = elec;
    cfg.headshape = vol.bnd(1);
    elec_new = ft_electroderealign(cfg);
