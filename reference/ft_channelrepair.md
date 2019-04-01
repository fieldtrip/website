---
title: ft_channelrepair
---
```
 FT_CHANNELREPAIR repairs bad or missing channels in the data by replacing them with the
 plain average of of all neighbours, by a weighted average of all neighbours, by an
 interpolation based on a surface Laplacian, or by spherical spline interpolating (see
 Perrin et al., 1989).

 Use as
   [interp] = ft_channelrepair(cfg, data)

 The configuration must contain
   cfg.method         = 'weighted', 'average', 'spline', 'slap' or 'nan' (default = 'weighted')
   cfg.badchannel     = cell-array, see FT_CHANNELSELECTION for details
   cfg.missingchannel = cell-array, see FT_CHANNELSELECTION for details
   cfg.neighbours     = neighbourhood structure, see also FT_PREPARE_NEIGHBOURS
   cfg.trials         = 'all' or a selection given as a 1xN vector (default = 'all')
   cfg.lambda         = regularisation parameter (default = 1e-5, not for method 'distance')
   cfg.order          = order of the polynomial interpolation (default = 4, not for method 'distance')

 The weighted neighbour approach cannot be used reliably to repair multiple bad channels
 that lie next to each other.

 If you want to reconstruct channels that are absent in your data, those channels may
 also be missing from the sensor definition (grad, elec or opto) and determining the
 neighbours is non-trivial. In that case you must use a complete sensor definition from
 another dataset or from a template.

 The EEG, MEG or NIRS sensor positions can be present in the data or can be specified as
   cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS
   cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS
   cfg.opto          = structure with optode definition, see FT_READ_SENS

 This function only interpolates data over space, not over time. If you want to
 interpolate using temporal information, e.g. using a segment of data before and
 after the nan-marked artifact, you should use FT_INTERPOLATENAN.

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a *.mat
 file on disk and/or the output data will be written to a *.mat file. These mat
 files should contain only a single variable, corresponding with the
 input/output structure.

 See also FT_MEGREALIGN, FT_MEGPLANAR, FT_PREPARE_NEIGHBOURS, FT_INTERPOLATENAN
```
