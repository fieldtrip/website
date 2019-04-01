---
title: ft_read_headshape
---
```
 FT_READ_HEADSHAPE reads the fiducials and/or the measured headshape from a variety
 of files (like CTF and Polhemus). The headshape and fiducials can for example be
 used for coregistration.

 Use as
   [shape] = ft_read_headshape(filename, ...)
 or
   [shape] = ft_read_headshape({filename1, filename2}, ...)

 If you specify the filename as a cell-array, the following situations are supported:
  - a two-element cell-array with the file names for the left and
    right hemisphere, e.g. FreeSurfer's {'lh.orig' 'rh.orig'}, or
    Caret's {'X.L.Y.Z.surf.gii' 'X.R.Y.Z.surf.gii'}
  - a two-element cell-array points to files that represent
    the coordinates and topology in separate files, e.g.
    Caret's {'X.L.Y.Z.coord.gii' 'A.L.B.C.topo.gii'};
 By default all information from the two files will be concatenated (i.e. assumed to
 be the shape of left and right hemispeheres). The option 'concatenate' can be set
 to 'no' to prevent them from being concatenated in a single structure.

 Additional options should be specified in key-value pairs and can include
   'format'      = string, see below
   'coordsys'    = string, e.g. 'head' or 'dewar' (only supported for CTF)
   'unit'        = string, e.g. 'mm' (default is the native units of the file)
   'concatenate' = 'no' or 'yes' (default = 'yes')
   'image'       = path to .jpg file
   'surface'     = specific surface to be read (only for caret spec files)

 Supported input file formats include
   'matlab'       containing FieldTrip or BrainStorm headshapes or cortical meshes
   'stl'          STereoLithography file format, for use with CAD and/or generic 3D mesh editing programs
   'vtk'          Visualization ToolKit file format, for use with Paraview
   'mne_*'        MNE surface description in ASCII format ('mne_tri') or MNE source grid in ascii format, described as 3D points ('mne_pos')
   'obj'          Wavefront .obj file obtained with the structure.io
   'off'
   'ply'
   'itab_asc'
   'ctf_*'
   '4d_*'
   'neuromag_*'
   'yokogawa_*'
   'polhemus_*'
   'freesurfer_*'
   'mne_source'
   'spmeeg_mat'
   'netmeg'
   'vista'
   'tet'
   'tetgen_ele'
   'gifti'
   'caret_surf'
   'caret_coord'
   'caret_topo'
   'caret_spec'
   'brainvisa_mesh'
   'brainsuite_dfs'

 See also FT_READ_HEADMODEL, FT_READ_SENS, FT_READ_ATLAS, FT_WRITE_HEADSHAPE
```
