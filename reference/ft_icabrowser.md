---
title: ft_icabrowser
---
```
 FT_ICABROWSER loads in comp structure from FieldTrip ft_componentanalysis
 and presents a GUI interface showing the power spectrum, variance over
 time and the topography of the components, as well as the possibility to
 save a PDF, view the timecourse and toggle components to be rejected vs
 kept.

 Use as
    [rej_comp] = ft_icabrowser(cfg, comp)

 where the input comp structure should be obtained from FT_COMPONENTANALYSIS.

 The configuration must contain:
   cfg.layout     = filename of the layout, see FT_PREPARE_LAYOUT

 further optional configuration parameters are
   cfg.rejcomp       = list of components which shall be initially marked for rejection, e.g. [1 4 7]
   cfg.blocksize     = blocksize of time course (default = 1 sec)
   cfg.powscale      = scaling of y axis in power plot, 'lin' or 'log10', (default = 'log10')
   cfg.zlim          = plotting limits for color dimension of topoplot, 'maxmin', 'maxabs', 'zeromax', 'minzero', or [zmin zmax] (default = 'maxmin')
   cfg.path          = where pdfs will be saves (default = pwd)
   cfg.prefix        = prefix of the pdf files (default = 'ICA')
   cfg.colormap      = any sized colormap, see COLORMAP
   cfg.outputfile    = MAT file which contains indices of all components to reject
   cfg.showcallinfo  = show call info, 'yes' or 'no' (default: 'no')

 original written by Thomas Pfeffer
 adapted by Jonathan Daume and Anne Urai
 University Medical Center Hamburg-Eppendorf, 2015

 modified by Daniel Matthes
 Max Planck Institute for Human Cognitive and Brain Sciences, 2019

 See also FT_COMPONENTANALYSIS, FT_TOPOPLOTIC, FT_PREPARE_LAYOUT
```
