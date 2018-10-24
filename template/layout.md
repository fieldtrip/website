---
layout: default
---

{{tag>template layout}}

# Template 2D layouts for plotting

Electrode positions in the layouts are represented as points in 2-D Carthesian space, i.e. with an X and Y position for each electrode. Furthermore, each electrode has a label. In the [layout tutorial](/tutorial/layout) you can find more details on how to create and use them. The file format for layout files specified as ascii *.lay files is explained [here](/faq/what_is_the_format_of_the_layout_file_which_is_used_for_plotting).

You can use the following snippet of code to get a quick overview of the template layout sets.

	
	dirlist  = dir('template/layout/*');
	filename = {dirlist(~[dirlist.isdir]).name}'
	for i=1:length(filename)
	  cfg = [];
	  cfg.layout = filename{i};
	  layout = ft_prepare_layout(cfg);
	
	  figure
	  ft_plot_lay(layout);
	  h = title(filename{i});
	  set(h, 'Interpreter', 'none');
	  
	  [p, f, x] = fileparts(filename{i});
	  print([lower(f) '.png'], '-dpng');
	end

## EASY CAP

The following series of template layouts is for the electrode caps from [EASY CAP](http://www.easycap.de). They are sorted based on their electrode montages. FieldTrip provides .mat files (since r5201 - feb 2012) that are based on the bitmap images obtained from the easycap website and shown below. The layout structure stored in those .mat files contains fields that describe the position (.pos), the width (.width), and the height (.height), and the naming (.label) of the electrodes. Furthermore, it contains fields that describe the topographic interpolation boundaries (.mask) and the outlines of the 'head' (.outline).  

###  10%-Arrangements

The following template layout sets are provide

*  easycapM25.mat

*  easycapM3.mat

*  easycapM22.mat

*  easycapM23.mat

*  easycapM24.mat

*  easycapM11.mat

*  easycapM1.mat

*  easycapM15.mat

####  easycapM25 - International 10/20-System (used in EC20) 

{{:template:easycapm25.png?direct&200x200|}}
{{:template:easycapm25.mat.png?direct&200x200|}}

#### easycapM3 - Extended 10/20-System with 30 Channels

![image](/media/template/easycapm3.png@200)
{{:template:easycapm3.mat.png?direct&200x200|}}

#### easycapM22 - Small Equidistant 29-Channel-Arrangment (used in Braincap32)

![image](/media/template/easycapm22.png@200)
{{:template:easycapm22.mat.png?direct&200x200|}}

#### easycapM23 - Large Equidistant 32-Channel-Arrangement

![image](/media/template/easycapm23.png@200)
{{:template:easycapm23.mat.png?direct&200x200|}}

#### easycapM24 - Large Equidistant 34-Channel-Arrangement (used in EC40)

![image](/media/template/easycapm24.png@200)
{{:template:easycapm24.mat.png?direct&200x200|}}

#### easycapM11 - 61-Channel-Arrangement ("10%-System") (used in BrainCap64)

![image](/media/template/easycapm11.png@200)
{{:template:easycapm11.mat.png?direct&200x200|}}

#### easycapM1 - 74-Channel-Arrangement (used in EC80)

![image](/media/template/easycapm1.png@200)
{{:template:easycapm1.mat.png?direct&200x200|}}

#### easycapM15 - 128-Channel-Arrangement

![image](/media/template/easycapm15.png@200)
{{:template:easycapm15.mat.png?direct&200x200|}}
### Triangulated Equidistant Arrangements

The following template layout sets are provide

*  easycapM7.mat

*  easycapM10.mat

*  easycapM16.mat

*  easycapM14.mat

#### easycapM7 - Spherical 32-Channel-Arrangement

{{:template:easycapm7.png?direct&200|}}
{{:template:easycapm7.mat.png?direct&200x200|}}

#### easycapM10 - Equidistant 61-Channel-Arrangement

![image](/media/template/easycapm10.png@200)
{{:template:easycapm10.mat.png?direct&200x200|}}

#### easycapM16 - Equidistant 88-Channel-Arrangement

![image](/media/template/easycapm16.png@200)
{{:template:easycapm16.mat.png?direct&200x200|}}

#### easycapM14 - Spherical 124-Channel-Arrangement

{{:template:easycapm14.png?direct&200|}}
{{:template:easycapm14.mat.png?direct&200x200|}}

### Miscellaneous Arrangements

The following template layout sets are provide

*  easycapM20.mat

*  easycapM17.mat

*  easycapM19.mat

#### easycapM20 - BESA 32-Channel-Arrangement for Epilepsy Diagnostics

![image](/media/template/easycapm20.png@200)
{{:template:easycapm20.mat.png?direct&200x200|}}

#### easycapM17 - 29-Channel-Arrangement for Language Research

![image](/media/template/easycapm17.png@200)
{{:template:easycapm17.mat.png?direct&200x200|}}

## actiCAP

The following template layouts are for electrode caps from [actiCAP](http://www.brainproducts.com). FieldTrip provides .mat files (since r6121 - june 2012) that are based on the bitmap images shown below. Note that these layouts were created for the DCCN and the MPI specifically and may differ from other actiCAP layouts. For a standard actiCap layout, see: acticap-64ch-standard2.mat.

#### dccn_customized_acticap64.mat

This is a custom 64-Channel-Arrangement for the DCCN. The 32 channels from the 1st amplifier are located central, the 32 channels from the 2nd amplifier are along the rim.

{{:template:dccn_customized_acticap64.png?direct&250|}}
{{:template:dccn_customized_acticap64.mat.png?direct&200x200|}}

#### mpi_customized_acticap64.mat

This is a custom 64-Channel-Arrangement for the MPI. Note that the electrode positions are the same as for the DCCN customized version, but that the channel order is different. The MPI version has the 32 channels from the 1st amplifier on the right and the 32 channels from the 2nd amplifier on the left.

![image](/media/template/mpi_customized_acticap64.png@200)
![image](/media/template/mpi_customized_acticap64.mat.png@200)

#### acticap-64ch-standard2.mat

This is the standard 64-channel-Arrangement from [Brain Products](http://www.brainproducts.com/files/public/downloads/actiCAP-64-channel-Standard-2_1201.pdf). It is based on the same coordinates as the easycap electrode caps. This particular layout was created using the [easycapM1 layout](http://www.fieldtriptoolbox.org/_media/template/easycapm1.png) and then removing eight electrodes (FPz, Iz, F9, F10, P9, P10, O9, O10) which are not present in the cap. Furthermore, two eletrodes (AFz, FCz) were renamed to their purpose of being Ground(Gnd) and Reference(Ref) electrode.

{{:template:acticap-64-channel-standard-2_original.jpg?direct&200 |actiCAP-64-channel-Standard-2 Brain Products}}
{{:template:acticap-64-channel-standard-2_fieldtrip.jpg?direct&200 |actiCAP-64-channel-Standard-2 FieldTrip}}




## NeuroScan Quick-cap

The following template layout set is for an electrode cap from [NeuroScan](http://www.neuroscan.com). The origin and construction is described on http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=679. The QuikCap_NSL_128 layout has been provided by Andre Cravo.  


*  {{:template:quickcap64.mat.png?linkonly|quickcap64.mat}} (since june 2012 - r6055)

*  {{:template:quikcap_nsl_128.mat.png?linkonly|QuikCap_NSL_128.mat}} (since nov 2012 - r6915)

## BioSemi cap

The following template layouts are for an electrode cap from [BioSemi](http://www.biosemi.com).  


*  {{:template:biosemi16.lay.png?linkonly|biosemi16.lay}}

*  ![image](/media/template/biosemi32.lay.png)

*  ![image](/media/template/biosemi64.lay.png)

*  ![image](/media/template/biosemi128.lay.png)

*  ![image](/media/template/biosemi160.lay.png)

*  ![image](/media/template/biosemi256.lay.png)
## Standard 10-XX cap

The following template layouts are for an electrode cap based on a standard 10-XX montage. 


*  ![image](/media/template/EEG1005.lay.png)

*  ![image](/media/template/EEG1010.lay.png)

*  ![image](/media/template/EEG1020.lay.png)

*  ![image](/media/template/elec1005.lay.png)

*  ![image](/media/template/elec1010.lay.png)

*  ![image](/media/template/elec1020.lay.png)
## 4D/BTI array

The following template layouts are for a sensor array of the 4D/BTI MEG system. 


*  ![image](/media/template/4D148.lay.png)

*  ![image](/media/template/4D248.lay.png)

*  {{:template:4D248_helmet.png?linkonly|4D248_helmet.mat}} - realistic display of temporal sensors

## CTF array

The following template layouts are for a sensor array of the CTF MEG system. 


*  ![image](/media/template/CTF151.lay.png)

*  {{:template:CTF151_helmet.png?linkonly|CTF151_helmet.mat}} - realistic display of temporal sensors

*  ![image](/media/template/CTF275.lay.png)

*  {{:template:CTF275_helmet.png?linkonly|CTF275_helmet.mat}} - realistic display of temporal sensors
 
## Neuromag array

The following template layouts are for a sensor array of the Neuromag MEG system. The major difference between the neuromag306 and the NM306 layouts is the labelling of the sensors (e.g. 'MEG1431' and '1431' respectively). In a similar vein, NM122.lay and NM122_combined.lay contain the lengthier labels (e.g. 'MEG 008'), whereas NM122all.lay has the shorter labels ('008').


*  ![image](/media/template/neuromag306all.lay.png)

*  {{:template:neuromag306cmb.lay.png?linkonly|neuromag306cmb.lay}} - includes the combined planar gradiometers

*  {{:template:neuromag306mag.lay.png?linkonly|neuromag306mag.lay}} - includes only the magnetometers

*  {{:template:neuromag306planar.lay.png?linkonly|neuromag306planar.lay}} - includes only the planar gradiometers

*  ![image](/media/template/NM122.lay.png)

*  ![image](/media/template/NM122all.lay.png)

*  {{:template:NM122combined.lay.png?linkonly|NM122combined.lay}} - includes the combined planar gradiometers

*  ![image](/media/template/NM306all.lay.png)

*  {{:template:NM306mag.lay.png?linkonly|NM306mag.lay}} - includes only the magnetometers

*  {{:template:NM306planar.lay.png?linkonly|NM306planar.lay}} - includes only the planar gradiometers 
## Yokogawa array

The following template layouts are for a sensor array of the Yokogawa MEG system. The labels in these layouts, except for the old variant, are prefixed to indicate the gradiometer type ('PG*' - planar gradiometer, 'AG*' - axial gradiometer). 

*  ![image](/media/template/yokogawa440.lay.png)

*  ![image](/media/template/yokogawa440_old.lay.png)

*  {{:template:yokogawa440ag.lay.png?linkonly|yokogawa440ag.lay}} - includes only the axial gradiometers

*  ![image](/media/template/yokogawa440all.lay.png)

*  {{:template:yokogawa440pg.lay.png?linkonly|yokogawa440pg.lay}}  - includes only the planar gradiometers
