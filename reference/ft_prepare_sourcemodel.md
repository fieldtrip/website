---
title: ft_prepare_sourcemodel
---
```
 FT_PREPARE_SOURCEMODEL constructs a source model, for example a 3D grid or a
 cortical sheet. The source model that can be used for source reconstruction,
 beamformer scanning, linear estimation and MEG interpolation.

 Use as
   sourcemodel = ft_prepare_sourcemodel(cfg)
 where the details of the configuration structure determine how the source
 model will be constructed.

 A source model can be constructed based on
   - regular 3D grid with explicit specification
   - regular 3D grid with specification of the resolution
   - regular 3D grid, based on segmented MRI, restricted to gray matter
   - regular 3D grid, based on a warped template grid, based on the MNI brain
   - surface mesh based on the brain surface from the volume conduction model
   - surface mesh based on the head surface from an external file
   - cortical sheet that was created in MNE or Freesurfer
   - using user-supplied source positions, which can be regular or irregular
 The approach that will be used depends on the configuration options that
 you specify.

 Configuration options for generating a regular 3D grid
   cfg.xgrid      = vector (e.g. -20:1:20) or 'auto' (default = 'auto')
   cfg.ygrid      = vector (e.g. -20:1:20) or 'auto' (default = 'auto')
   cfg.zgrid      = vector (e.g.   0:1:20) or 'auto' (default = 'auto')
   cfg.resolution = number (e.g. 1 cm) for automatic grid generation

 Configuration options for predefined source positions
   cfg.sourcemodel.pos        = N*3 matrix with position of each source
   cfg.sourcemodel.inside     = N*1 vector with boolean value whether position is inside brain (optional)
   cfg.sourcemodel.dim        = [Nx Ny Nz] vector with dimensions in case of 3D grid (optional)
 The following fields are not used in this function, but will be copied along to the output
   cfg.sourcemodel.leadfield
   cfg.sourcemodel.filter
   cfg.sourcemodel.subspace
   cfg.sourcemodel.lbex

 Configuration options for a warped MNI grid
   cfg.mri        = structure with anatomical MRI model or filename, see FT_READ_MRI
   cfg.warpmni    = 'yes'
   cfg.resolution = number (e.g. 6) of the resolution of the
                                template MNI grid, defined in mm
   cfg.template   = specification of a template grid (grid structure), or a
                                filename of a template grid (defined in MNI space),
                                either cfg.resolution or cfg.template needs
                                to be defined. If both are defined cfg.template prevails
   cfg.nonlinear  = 'no' (or 'yes'), use non-linear normalization

 Configuration options for cortex segmentation, i.e. for placing dipoles in grey matter
   cfg.mri           = can be filename, MRI structure or segmented MRI structure
   cfg.threshold     = 0.1, relative to the maximum value in the segmentation
   cfg.smooth        = 5, smoothing in voxels

 Configuration options for reading a cortical sheet from file
   cfg.headshape     = string, should be a *.fif file

 The EEG or MEG sensor positions can be present in the data or can be specified as
   cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS
   cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS

 The headmodel or volume conduction model can be specified as
   cfg.headmodel     = structure with volume conduction model or filename, see FT_PREPARE_HEADMODEL

 Other configuration options
   cfg.sourcemodel.unit    = string, can be 'mm', 'cm', 'm' (default is automatic)
   cfg.tight   = 'yes' or 'no' (default is automatic)
   cfg.inwardshift  = number, how much should the innermost surface be moved inward to constrain
                      sources to be considered inside the source compartment (default = 0)
   cfg.moveinward   = number, move dipoles inward to ensure a certain distance to the innermost
                      surface of the source compartment (default = 0)
   cfg.spherify     = 'yes' or 'no', scale the source model so that it fits inside a sperical
                      volume conduction model (default = 'no')
   cfg.symmetry     = 'x', 'y' or 'z' symmetry for two dipoles, can be empty (default = [])
   cfg.headshape    = a filename for the headshape, a structure containing a single surface,
                      or a Nx3 matrix with headshape surface points (default = [])
   cfg.spmversion   = string, 'spm2', 'spm8', 'spm12' (default = 'spm8')

 See also FT_PREPARE_LEADFIELD, FT_PREPARE_HEADMODEL, FT_SOURCEANALYSIS,
 FT_DIPOLEFITTING, FT_MEGREALIGN
```
