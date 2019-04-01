---
title: ft_meshrealign
---
```
 FT_MESHREALIGN rotates, translates and optionally scales electrode positions. The
 different methods are described in detail below.

 INTERACTIVE - You can display the mesh surface together with axis coordinate
 system, and manually (using the graphical user interface) adjust the rotation,
 translation and scaling parameters.

 FIDUCIAL - The coordinate system is updated according to the definition of the
 coordinates of anatomical landmarks or fiducials that are specified in the
 configuration. If the fiducials are not specified in the configurartion, you will
 have to click them in an interactive display of the mesh surface.

 Use as
   mesh = ft_meshrealign(cfg, mesh)
 where the mesh input argument comes from FT_READ_HEADSHAPE or FT_PREPARE_MESH and
 cfg is a configuration structure that should contain

  cfg.method    = string, can be 'interactive' or fiducial' (default = 'interactive')

 The configuration can furthermore contain
   cfg.coordsys        = string, can be 'ctf', 'neuromag', '4d', 'bti', 'itab'
   cfg.fiducial.nas    = [x y z], position of nasion
   cfg.fiducial.lpa    = [x y z], position of LPA
   cfg.fiducial.rpa    = [x y z], position of RPA

 The fiducials should be expressed in the coordinates and units of the input mesh.

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a *.mat
 file on disk and/or the output data will be written to a *.mat file. These mat
 files should contain only a single variable, corresponding with the
 input/output structure.

 See also FT_READ_HEADSHAPE, FT_PREPARE_MESH, FT_ELECTRODEREALIGN, FT_VOLUMEREALIGN
```
