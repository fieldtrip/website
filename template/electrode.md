---
layout: default
tags: template
---

# Table of contents
{:.no_toc}

* this is a markdown unordered list which will be replaced with the ToC, excluding the "Contents header" from above
{:toc}

# Template 3-D electrode sets

Electrodes are represented as points in 3-D Carthesian space, i.e. with an X, Y and Z position for each electrode. Furthermore, each electrode has a label. There is a frequently asked question about [how the electrode structure is described](/faq/how_are_electrodes_magnetometers_or_gradiometers_described).

You can use the following snippet of code to get a quick overview of the template electrode sets.


	dirlist  = dir('template/electrode/*');
	filename = {dirlist(~[dirlist.isdir]).name}'
	for i=1:length(filename)
	  elec = ft_read_sens(filename{i});
	  figure
	  ft_plot_sens(elec);
	  title(filename{i});
	  grid on
	  rotate3d
	end

### The 10-20, 10-10 and 10-5 system for electrode placement

The following template electrode sets describe the 10-20 EEG electrodes and were constructed by Robert Oostenveld as part of the study described in *Robert Oostenveld and Peter Praamstra. **The five percent electrode system for high-resolution EEG and ERP measurements.** Clin Neurophysiol. 2001 Apr;112(4):713-9.* More details on the electrode positioning and the different naming schemes can be found in the paper (link to [pubmed](http://www.ncbi.nlm.nih.gov/pubmed/11275545), [sciencedirect](http://www.sciencedirect.com/science/article/pii/S1388245700005277)) and on Robert's [personal blog](http://robertoostenveld.nl/?p=5).

The electrodes are stored in an ASA .elc file  which can be read with **[ft_read_sens](/reference/ft_read_sens)**. The electrode positions are represented in mm in the MNI coordinate system and are aligned with the scalp model which is detailed in [this publication](http://www.ncbi.nlm.nih.gov/pubmed/12842715).     

*  standard_1005.elc

*  standard_1020.elc

*  standard_alphabetic.elc

*  standard_postfixed.elc

*  standard_prefixed.elc

*  standard_primed.elc

### The EGI geodesic sensor net

The following template electrode sets are for the [EGI](http://www.egi.com) geodesic sensor net and were downloaded from the EGI [ftp server](ftp://www.egi.com).

*  GSN-HydroCel-128.sfp

*  GSN-HydroCel-129.sfp

*  GSN-HydroCel-256.sfp

*  GSN-HydroCel-257.sfp

*  GSN-HydroCel-32.sfp

*  GSN-HydroCel-64_1.0.sfp

*  GSN-HydroCel-65_1.0.sfp

### Easycap electrode arrangements

The following template electrode sets are for the [Easycap](http://www.easycap.de/easycap/e/products/products.htm) electrode arrangements and were downloaded from the Easycap [download page](http://www.easycap.de/easycap/e/downloads/electrode_sites_coordinates.htm).

*  easycap-M1.sfp (Full 10%-System)

*  easycap-M10.sfp (Equidistant 61-Channel-Arrangement)
