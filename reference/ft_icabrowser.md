---
title: ft_icabrowser
layout: default
tags: 
---
```
 ICA component viewer and GUI

 loads in comp structure from FieldTrip ft_componentanalysis
 presents a GUI interface showin the power spectrum, variance over time
 and the topography of the components, as well as the possibility to save
 a PDF, view the timecourse and toggle components to be rejected vs kept.
 when done, will create a file with the components to be rejected

 CONFIGURATION NEEDED:
 cfg.path         where pdfs will be saves
 cfg.prefix       prefix of the pdf files
 cfg.layout       layout of the topo view

 OPTIONAL CONFIGURATION:
 cfg.colormap      colormap for topo
 cfg.inputfile
 cfg.outputfile    will contain indices of all components to reject

 original written by Thomas Pfeffer
 adapted by Jonathan Daume and Anne Urai
 University Medical Center Hamburg-Eppendorf, 2015
```
