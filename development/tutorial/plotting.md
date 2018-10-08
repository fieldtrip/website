---
layout: default
---

{{tag>tutorial plot eeg meg timelock freq statistics source layout MEG-language}}

`<note warning>`
This page is under development, use with caution 
`</note>`


# Plotting data at the channel and source level

## Introduction

To visualize your experimental data you can make use of FieldTrip's specialised plotting functions, which are optimised for the FT data structures. Alternatively, you can use the  standard MATLAB functions ('plot, 'image', 'imagesc'). 

## Background

The goal of these FieldTrip plotting functions is to ease the visualization of data structures. This is accomplished by creating a substrate of low level functions (with prefixes 'ft_plot_' and 'ft_select_', e.g. **[ft_plot_matrix](/reference/ft_plot_matrix)** or **[ft_select_box](/reference/ft_select_box)**) and high level functions (e.g. **[ft_topoplotER](/reference/ft_topoplotER)** or **[ft_multiplotTFR](/reference/ft_multiplotTFR)**).
The rationale behind this divide is that the high level functions incorporate functionality of low level function whose behavior is carefully controlled. As an example, old scripts which plotted vectorial variables by means of the MATLAB function 'plot' now make use of the FieldTrip low level routine **[ft_plot_vector](/reference/ft_plot_vector)**. This allows better control of the plotting options by using a more specific style than in MATLAB's 'plot'.

Normally, as an end-user, you do not need to bother with low level functions (which are deployed in the 'plotting' folder, see [plotting project](http://fieldtrip.fcdonders.nl/development/plotting) for a preliminary documentation on low level functions), whose options are already set to accomplish an optimal visualization. Rather you can simply use the higher level plotting functions, which is demonstrated below.

## Procedure

To determine which high level functions are suitable for you depends on the type of data you have: sensor or source space data. In this tutorial we assume that you already have the data from the [event related averaging tutorial](/tutorial/eventrelatedaveraging), the [time-frequency representations of power tutorial](/tutorial/timefrequencyanalysis) and the [applying beamforming techniques in the frequency domain tutorial](/tutorial/beamformer), and we will demonstrate plotting at both the sensor and source level.


## Plotting data at the channel level

Data at the channel level has a value for each sensor (MEG) or electrode (EEG). Here are a few examples of plotting data on the channel level using different high-level fieldtrip functions.

Plotting 2D data at the sensor level using:  ft_singleplotER (top left), ft_multiplotER (top right) and ft_topoplotER (bottom left)

{{tutorial:plotting:figure5.png?250|singleplotER}}
{{tutorial:plotting:figure5era.png?250|multiplotER}}
{{tutorial:plotting:figure5.jpg?250|topoplotER}}

Plotting 3D data at the sensor level: using ft_singleplotTFR (top left), ft_multiplotTFR (top right) and ft_topoplotTFR (bottom left) 

{{tutorial:plotting:figure3.png?250|singleplotTFR}}
{{tutorial:plotting:figure2.png?250|multiplotTFR}}
{{tutorial:plotting:figure4.png?250|topoplotTFR}}

### Singleplot functions

With **[ft_singleplotER](/reference/ft_singleplotER)** you can make a plot using the [avgFC data](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/plotting/avgFC.mat) from the [ERF tutorial](/eventrelatedaveraging) by the following cod
    cfg = [];
    cfg.xlim = [-0.2 1.0];
    cfg.ylim = [-1e-13 3e-13];
    cfg.channel = 'MLC24';
    clf;
    ft_singleplotER(cfg,avgFC);

The ft_singleplotER function first selects the data to be plotted, in this case channel MLC24, from -0.2 to 1.0 seconds. Subsequently this selected data is plotted with the MATLAB PLOT.m function. You could make the same plot by the following cod
    selected_data = avgFC.avg(9,241:601); %MLC24 is the 9th channel, -0.2 to 1.0 is sample 241 to 601
    time = avgFC.time(241:601);
    figure;
    plot(time, selected_data)
    xlim([-0.2 1.0])
    ylim([-1e-13 3e-13])

{{tutorial:plotting:singleploter_avgfc.png?400|plotted by singleplotER.m}}
{{tutorial:plotting:plot_avgfc.png?400|plotted by maptlab plot.m function}}

In **[ft_singleplotTFR](/reference/ft_singleplotTFR)** the channel, time bins and frequency bins are selected and subsequently plotted with the MATLAB IMAGESC.m function. 

The FieldTrip plotting functions have a lot of build in intelligence to make the plotting of the multidimensional data easier. It is for instance possible to do baseline correction before plotting, by specifying the baseline type and time limits. In the plotting functions either the FieldTrip function **[ft_timelockbaseline](/reference/ft_timelockbaseline)** or **[ft_freqbaseline](/reference/ft_freqbaseline)** is called.
If you specify multiple channels in cfg.channel both singleplot functions will plot the mean over these channels. In the plotting functions the FieldTrip function **[ft_channelselection](/reference/ft_channelselection)** is called, which makes it straightforward to plot for instance the mean TFR (download [here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/plotting/TFRhann.mat), see [time-frequency analysis tutorial](/timefrequencyanalysis#hanning_taper_fixed_window_length))of the left central channels.

    cfg = [];
    cfg.baseline = [-0.5 -0.1]; 
    cfg.baselinetype = 'absolute'; 	
    cfg.zlim = [-1.5e-27 1.5e-27];	
    cfg.channelname   = 'MLC'; % top figure
    figure;ft_singleplotTFR(cfg, TFRhann);

    % Optional to tr
    % cfg.channelname  = 'MRC' % bottom figure
    % figure; ft_singleplotTFR(cfg,TFRhann);

{{tutorial:plotting:singleplottfr_mlc.png?350 | singleplotTFR MLC}}
{{tutorial:plotting:singleplottfr_mrc.png?350 | singleplotTFR MRC}}

#### Exercise 1

`<note exercise>`
Try to replicate [Figure 5 from the Event Related Averaging tutorial](/tutorial/eventrelatedaveraging#plotting_the_result) and [Figure 3 from the Time Frequency analysis tutorial](/tutorial/timefrequencyanalysis#plotting_the_results ) without using FieldTrip functions.
`</note>`
### Multiplot functions

The multiplot functions work similarly to the singleplot functions, again first by selecting the data and subsequently using the MATLAB functions PLOT.m and IMAGESC.m. But instead of one plot, multiple plots are made; one for each channel. These plots are arranged according to a specified layout in one pair of axes. In the subsequent figures you can see these axes that are normally set to "off".  Exemplar code for using ft_multiplotER/TFR is shown in the 'interative mode' section of this tutorial (further down).

{{:tutorial:plotting:multiploter_axison2.png?400|multiplotER axis on}}
{{:tutorial:plotting:multiplottfr_axison2.png?400|multiplotTFR axis on}}

Normally the axes of the figure are not visible, only the "axis" of each channel, but remember these are not real axes on which you can use MATLAB axis commands, the are just lines drawn by the function. Of course you can set the limits of the channel "axis" by the cfg structure (cfg.xlim, cfg.ylim). And you can see the limits in the scale in **[ft_multiplotER](/reference/ft_multiplotER)** (righ upper corner) or in the comment for **[ft_multiplotTFR](/reference/ft_multiplotTFR)** (left upper corner).

{{:tutorial:plotting:avgfic.png?400|multiplotER}}
{{:tutorial:plotting:tfrhannall.png?400|multiplotTFR}}

The layout is determined by the layout file. Read more on layout files 
[here](/tutorial/layout), and in the [frequently asked questions](/faq/what_is_the_format_of_the_layout_file_which_is_used_for_plotting).

For multiplotting planar gradient data from the Neuromag system it is especially relevant to work with layout files: the Neuromag system has two planar gradiometers (plus one axial magnetometer) at each sensor location. You do not want to plot those on top of each other. Hence the Neuromag layout files contain two (for 122 channel) or three (for 306 channel) seperate subplots for each channel location. Those two (or three) subplots hold the data for the two planar gradients (and for the magnetometer signal).

### Topoplot functions

**[Ft_topoplotER](/reference/ft_topoplotER)** and **[ft_topoplotTFR](/reference/ft_topoplotTFR)** plot the topographic distribution of 2-Dimensional or 3-Dimensional datatypes as a 2-D circular view (looking down at the top of the head). The arrangement of the channels is again specified in the layout (see above in multiplot functions). The **[ft_topoplotER](/reference/ft_topoplotER)** and **[ft_topoplotTFR](/reference/ft_topoplotTFR)** functions first again select the data to be plotted from the 2D or 3D input data and subsequently plot the selected data using low-level Fieldtrip functions. Using one value for each channel and the x and y coordinates, the values between points are interpolated and plotted. In the help of **[ft_topoplotER](/reference/ft_topoplotER)** and **[ft_topoplotTFR](/reference/ft_topoplotTFR)** you can find many cfg options. For instance by specifying the cfg.xlim as a vector the **[ft_topoplotER](/reference/ft_topoplotER)**/**[TFR](/reference/ft_topoplotTFR)** makes selections of multiple time-windows and plots them as subplots.

The data for plotting are available from ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/plotting/GA_FC.mat and ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/plotting/TFRhann.mat.

    cfg = [];                            
    cfg.xlim = [0.3 0.5];                
    cfg.zlim = [0 6e-14];                
    cfg.layout = 'CTF151.lay';            
    figure; ft_topoplotER(cfg,GA_FC); colorbar;
    
{{tutorial:plotting:tuto_topoer.png?250|topoplotER}}    

    cfg = [];
    cfg.xlim = [0.9 1.3];                
    cfg.ylim = [15 20];                  
    cfg.zlim = [-1e-27 1e-27];           
    cfg.baseline = [-0.5 -0.1];          
    cfg.baselinetype = 'absolute';
    cfg.layout = 'CTF151.lay';
    figure; ft_topoplotTFR(cfg,TFRhann);
    
{{tutorial:plotting:tuto_topotfr.png?250|topoplotTFR}}

    % for the multiple plots als
    cfg.xlim = [-0.4:0.2:1.4];
    cfg.comment = 'xlim';
    cfg.commentpos = 'title';
    figure; ft_topoplotTFR(cfg,TFRhann);

{{tutorial:plotting:tuto_topotfr_multi.png?300|topoplotTFR_xlim_vector}}

#### Exercise 2

`<note exercise>`
The most left picture made with **[ft_topoplotER](/reference/ft_topoplotER)** is planar ERF data. Planar data can not have values lower than zero. Explain why you nevertheless see values in the plot that correspond to negative values.
`</note>`
####  

In **[ft_topoplotER](/reference/ft_topoplotER)** and **[ft_topoplotTFR](/reference/ft_topoplotTFR)**, you can specify many options to fully control the appearance of the picture. Subsequently you can use the MATLAB print function to write the figure to a file. Preferred file formats are EPS for vector drawings that can be edited in Adobe Illustrator or in Canvas (using “print -depsc”) or PNG for bitmaps (using “print -dpng”).
To make the EPS-files optimally suitable for Adobe Illustrator, use the command “print -depsc -adobecs -painter”. 
Since it seems MATLAB uses the 'painter' renderer to export in Illustrator format, with this method one can export quite complex figures that otherwise would be exported as bitmaps. Note, however, that the 'painter' renderer has many limitations  compared to the z-buffer and openGL renderers. (See also MATLAB help on selecting a renderer).

Some examples of what you can d

    % options for data selection (used with any plotting function
    cfg = [];
    cfg.xlim = [0.9 1.3];
    cfg.ylim = [15 20];
    cfg.zlim = [-1e-27 1e-27];
    cfg.baseline = [-0.5 -0.1];
    cfg.baselinetype = 'absolute';
    cfg.layout = 'CTF151.lay';

Options specific for to using topoplot.m

    cfg.gridscale = 300;                  
    cfg.style = 'straight';               
    cfg.marker = 'labels';                
    figure; ft_topoplotTFR(cfg,TFRhann);
\\ 

{{tutorial:plotting:tuto_funcytopo3.png?250 |with channel labels}}                                                                            
\\ 

    cfg.gridscale = 300;                
    cfg.contournum = 10;                
    cfg.colormap = gray(10);            
    figure; ft_topoplotTFR(cfg,TFRhann);
\\ 

{{tutorial:plotting:tuto_funcytopo2.png?250 |grayscale}}
\\ 

    cfg.gridscale = 300;
    cfg.contournum = 4;
    cfg.colormap = spring(4);
    cfg.markersymbol = '.';
    cfg.markersize = 12;
    cfg.markercolor = [0 0.69 0.94];
    figure; ft_topoplotTFR(cfg,TFRhann);
\\ 

{{tutorial:plotting:tuto_funcytopo1.png?250 |you can go crazy!}}
\\ 

### Interactive mode

In a data inspection phase you can use the interactive modus to go from one plot to the other. You can for instance select a certain frequency and time range in a singleplot, to get the average over that range plotted in a topoplot. Or select a group of channels in a topoplot or a multiplot and get the average over those channels for the whole time and frequency range in a single plot.

    %interactive
    cfg = [];
    cfg.baseline = [-0.5 -0.1];
    cfg.zlim = [-3e-27 3e-27];
    cfg.baselinetype = 'absolute';
    cfg.layout = 'CTF151.lay';
    cfg.interactive = 'yes';
    figure; ft_multiplotTFR(cfg,TFRhann)

{{tutorial:plotting:interactive1.jpg?300| multiplot select channels}}
plot with ft_multiplot, and select channels of interest

{{tutorial:plotting:interactive2.jpg?300| then you get singleplot average over those channels, select time freq window}} 
selected channels are averaged and displayed as one plot (ft_singleplotTFR is called).  Then, select a section within the TFR to get a topoplot

{{tutorial:plotting:interactive3.jpg?300| then you get topoplot average over that time freq window}}


### Plotting clusters

**[Ft_clusterplot](/reference/ft_clusterplot)** plots a series of topoplots with found clusters highlighted. The output "stat" is 2D data from **[ft_timelockstatistics](/reference/ft_timelockstatistics)** or **[ft_freqstatistics](/reference/ft_freqstatistics)** with 'cluster' as cfg.correctmc. Stat should be 2D, therefore stat from **[ft_timelockstatistics](/reference/ft_timelockstatistics)** data not averaged over time, or stat from **[ft_freqstatistics](/reference/ft_freqstatistics)** averaged over frequency not averaged over time.

The function automatically finds the clusters in the data which are smaller than the pre-specified alpha (cfg.alpha) and plots a series of topoplots with the data in "stat" field (are for instance t-values) and the sensors which are part of the cluster highlighted. 

##### Timelockdata

	
	% load stat data
	load statERF
	
	% clusterplot
	cfg = [];
	cfg.zlim = [-6 6]; %Tvalues
	cfg.alpha = 0.05;
	ft_clusterplot(cfg,statERF)


\\
{{:tutorial:staterf1.png?400|}}
{{:tutorial:staterf2.png?400|}}
{{:tutorial:staterf3.png?400|}}
{{:tutorial:staterf4.png?400|}}
\\

##### Freqdata

	
	% load statistical output performed on freq data 
	% if code is of interest, please see tutorial on cluster_permutation_freq
	
	% clusterplot
	cfg = [];
	cfg.zlim = [-5 5];
	cfg.alpha = 0.05;
	ft_clusterplot(cfg,statTFR)


\\
{{:tutorial:plotting:plottingtutorial_tfrstat.jpg?400|clusterplotTFR}}
\\

### Plotting channel-level connectivity

Please see **[ft_connectivityplot](/reference/ft_connectivityplot)**, **[ft_multiplotCC](/reference/ft_multiplotCC)** and **[ft_topoplotCC](/reference/ft_topoplotCC)**.


### Plotting Independent Component Analysis (ICA) results  

To plot ICA, PCA or other decompositions that result from **[ft_componentanalysis](/reference/ft_componentanalysis)** you can use **[ft_topoplotIC](/reference/ft_topoplotIC)** for the topographies and **[ft_databrowser](/reference/ft_databrowser)** for the topographies combined with the time series.
## Plotting data at the source level

With the **[ft_sourceplot](/reference/ft_sourceplot)** function you can plot functional source reconstructed data. Data structures can be source estimates from **[ft_sourceanalysis](/reference/ft_sourceanalysis)** or **[ft_sourcegrandaverage](/reference/ft_sourcegrandaverage)** or statistical values from **[ft_sourcestatistics](/reference/ft_sourcestatistics)**. 

At the source level, there are two main ways of representing functional data: 
 1.  On a regular, 3-dimensional grid (volumetric data) 
 2.  On a surface geometry.


### Volumetric data 

Volume data is characterized by source locations spaced as a 3D grid (like voxels in an MRI)

You can visualize your data using **[ft_sourceplot](/reference/ft_sourceplot)**, which provides multiple plotting options. To specify the method of plotting, you can adjust the options in the  configuration structure (cfg) given as an input to ft_sourceplot. options for visualization are 

Example plotting methods include (1) multiple 2D slices (axial orientation as default) trhoughout the brain, (2) multiple slices in each of the three orthorgonal directions (axial, sagittal and coronal) with which you can use to click around the brain or (3) project the functional data onto a surface. The third option will be covered under 'surface data'. 

Below, we will first provide the basic code for using **[ft_sourceplot](/reference/ft_sourceplot)**. Then, we will proceed with specifying the fields in the cfg structure in order to produce the visualisation you want when calling **[ft_sourceplot](/reference/ft_sourceplot)**.

#### Source-Freq-Time data plotted as 2D slices

Here we will plot axial slices of the brain

	
	% load data
	load statsourceTFR 
	
	% specify cfg parameters
	cfg = [];
	cfg.method        = 'slice';
	cfg.funcolorlim   = 'maxabs';
	cfg.funparameter  = 'stat';
	ft_sourceplot(cfg,statsourceTFR);
	
	% note
	To play around with the number of slices, and which slice to begin plotting, check the documentation for cfg.nslices, and cfg.slicerange, respectively.


{{:tutorial:plotting:sourcestattfr_slice.png?500|}}

#### Source-Freq-Time data plotted as in 3 orthogonal orientations

For exploring your data, plotting the brain from 3 orthogonal orientations simultaneously can be helpful.  Below you can see that the parameters are similar as plotting slices, except for the method being specified.

	
	cfg = [];
	cfg.method        = 'ortho';  %changed from slice
	cfg.funcolorlim   = 'maxabs';
	cfg.funparameter  = 'stat';
	ft_sourceplot(cfg,statsourceTFR);


{{:tutorial:plotting:sourcestattfr_ortho.png?500|}}

#### Source-Freq-Time data interpolated on to an MRI

This section uses the data from Subject01 in the [:tutorial:beamformer](/tutorial/beamformer) tutorial.

	
	% load contrast data
	load sourceDiff
	
	% load MRI and interpolate functional source data to MRI
	mri = ft_read_mri('Subject01.mri');  
	mri = ft_volumereslice([], mri);
	
	cfg            = [];
	cfg.downsample = 2;
	cfg.parameter  = 'avg.pow';
	sourceDiffInt  = ft_sourceinterpolate(cfg, sourceDiff , mri);
	
	% plot multiple 2D axial slices
	cfg = [];
	cfg.method        = 'slice';
	cfg.funparameter  = 'avg.pow';
	cfg.maskparameter = cfg.funparameter;
	cfg.funcolorlim   = [0.0 1.2];
	cfg.opacitylim    = [0.0 1.2]; 
	cfg.opacitymap    = 'rampup';  
	ft_sourceplot(cfg, sourceDiffInt);
	

{{:tutorial:beamformer:figure4bf.png?500|"Figure 4"}}

####  Plotting on 3 orthogonal slices 

	
	cfg = [];
	cfg.nonlinear     = 'no';
	sourceDiffIntNorm = ft_volumenormalise(cfg, sourceDiffInt);
	
	% plot ortho
	cfg = [];
	cfg.method        = 'ortho';
	cfg.funparameter  = 'avg.pow';
	cfg.maskparameter = cfg.funparameter;
	cfg.funcolorlim   = [0.0 1.2];
	cfg.opacitylim    = [0.0 1.2]; 
	cfg.opacitymap    = 'rampup';  
	figure; ft_sourceplot(cfg, sourceDiffIntNorm);


{{:tutorial:beamformer:figure8bf.png?500|"Figure 6"}}

The three essential cfg parameters ar

*  **cfg.anaparameter** the anatomy parameter, specifying the anatomy to be plotted

*  **cfg.funparameter** the functional parameter, specifying the functional data to be plotted

*  **cfg.maskparameter** the mask parameter, specifying the parameter to be used to mask the functional data
All parameters must be interpolated onto the same grid. See **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)** and **[ft_volumenormalise](/reference/ft_volumenormalise)**.

#### the anatomy parameter

The anatomy can be read with **[ft_read_mri](/reference/ft_read_mri)**. The functional data can be interpolated onto the anatomy by **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)**. The anatomy is scaled between 0 and 1 and plotted in gray scale.

#### the functional parameter

The functional data is plotted in color optionally on top of the anatomy. The colors used can be determined by cfg.colormap (see MATLAB function COLORMAP). How the functional values are assigned to the colormap is determined by cfg.colorlim. It makes sense to plot for instance source data as functional parameter, but also statistical values (for instance T-values).

#### the masking parameter

You can control the opacity of the functional data by the mask parameter. Which values are plotted opaque and which transparent is determined by cfg.opacitymap and cfg.opacitylim (see MATLAB function ALPHA and ALPHAMAP). The opacity map determines the degree of opacity of the functional data going from opaque to transparent.  There are multiple ways to determine your opacity scale, as a user you can determine the opacity values for each and every single voxel (and as such, region of interest).  As such, the opacity limits determine how the opacity map is assigned to the values of the mask parameter.  


#### Example 1: Plotting only positive values

Your functional data has values ranging from -3 to 3. Here we plot only the positive values  (zeromax), using the scale whereby the strongest values are opaque, and the values close to zero are transparen
    cfg.maskparameter = cfg.funparameter
    cfg.colorlim      = [0 3] (or'zeromax')
    cfg.opacitymap    = 'rampup'
    cfg.opacitylim    = [0 3] (or 'zeromax')

#### Example 2: Plotting high absolute values

Suppose the functional data is the same as in example 1, but now we only wants to plot the high negative values and high positive values (use "maxabs" setting). We set these high absolute values to opaque, and the values around zero to transparen

    cfg.maskparameter = cfg.funparameter
    cfg.colorlim      = [-3 3] (or'maxabs')
    cfg.opacitymap    = 'vdown'
    cfg.opacitylim    = [-3 3] (or'maxabs')

#### Example 3: Masking voxels outside values of interest

Here, we make a field in the data with an opacity value for each voxel, and apply that as your mask. For instance if you only want to plot the values between 2 and 2.5 you can specif
    data.mask         = (data.fun>2 & data.fun<2.5)
    cfg.maskparameter = 'mask'


** Here are some figures to help understand how the data is manipulated when specifying cfg.opacitymap:**

{{tutorial:plotting:plottuto_opac_rampup2.png?280|rampup}}
{{tutorial:plotting:plottuto_opac_vdown2.png?280|vdown}}
{{tutorial:plotting:plottuto_opac_mask.png?280|own mask}}
### Plotting on a brain surface

#### Scalar data per vertex

The representation of source activity on a surface results from source estimation using a cortical sheet as the source model. The cortical sheet is represented as a triangulated surface and the activity is assigned to each of the vertices, i.e. corner points of the triangles. Besides doing the source estimation on a cortical sheet, it is also possible to interpolate the volumetric data (i.e. estimated on a regular 3-D grid) onto a cortical sheet for visualization.

Scalar data (e.g., time-averaged activity, frequency-specific power estimates, statistics, etc.) can be plotted using the **[ft_plot_mesh](/reference/ft_plot_mesh)** function. Alternatively, volumetric data can also be rendered on a surface by projecting it to a surface geometry, using **[ft_sourceplot](/reference/ft_sourceplot)**. An example of the latter is given below, where we use the same data as in the preceding section.

#### Project volumetric data to an MNI white-matter surface surface

	
	cfg = [];
	cfg.method         = 'surface';
	cfg.funparameter   = 'avg.pow';
	cfg.maskparameter  = cfg.funparameter;
	cfg.funcolorlim    = [0.0 1.2];
	cfg.funcolormap    = 'jet';
	cfg.opacitylim     = [0.0 1.2]; 
	cfg.opacitymap     = 'rampup';  
	cfg.projmethod     = 'nearest'; 
	cfg.surffile       = 'surface_white_both.mat'; %Standard MNI brain
	cfg.surfdownsample = 10;  % downsample to speed up processing
	ft_sourceplot(cfg, sourceDiffIntNorm);
	view ([90 0])             % rotate the object in the view


{{:tutorial:beamformer:bf_tut_surfacepowrelnorm_comfilt.png?500|"Figure 7"}}

However, if you want to explore higher-dimensional data (such as TFR data) on the surface, using  **[ft_sourceplot](/reference/ft_sourceplot)** directly, is currently not supported. You can, however, select a data sub-selection manually.

#### Higher dimensional data

As an example of plotting multiple-dimensional volumetric data to the surface, we will use a source-level [statistics output](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/plotting/pos_freq_time.mat), which contains time-frequency dimensions.

In the previous section, where we have projected scalar data to the surface, we've used **[ft_sourceplot](/reference/ft_sourceplot)**, which handled low-level processing automatically for us. As projecting non-scalar data to the surface is not supported by ft_sourceplot, we now have to implement these steps manually.

Let's select our data segment of interest, so we have scalar data, which we can present to ft_sourceplot.

#### Make a data selection

	
	% Select data closest to the point-of-interest
	freqSel = 70; 
	timeSel = 0.2; 
	[~, ixFreqSel] = min(abs(stat.freq - freqSel));
	[~, ixTimeSel] = min(abs(stat.time - timeSel));
	
	%Copy all relevant fields to a new structure
	statSubSel.inside   = stat.inside;
	statSubSel.outside  = stat.outside;
	statSubSel.dim      = stat.dim;
	statSubSel.pos      = stat.pos;
	
	%Actually selecting the data; One can also apply averaging here, etc.
	statSubSel.stat = stat.stat(:,ixFreqSel, ixTimeSel);
	statSubSel.time = stat.time(ixTimeSel);
	statSubSel.freq = stat.freq(ixFreqSel);


The resulting statSubSel-structure can be processed by **[ft_sourceplot](/reference/ft_sourceplot)**. 
#### Plotting data selection to surface

	
	cfg = [];
	cfg.surffile     = surffile;
	cfg.funparameter = 'stat';
	cfg.method       = 'surface';
	cfg.location     = 'center';
	ft_sourceplot(cfg, statSubSel);


### Using external tools

Although MATLAB is a very flexible development and analysis environment, it is not super-fast in visualisation. Hence external visualisation tools are sometimes more useful for exploring your data. Volumetric and surface based data can be exported to standard file formats using **[ft_sourcewrite](/reference/ft_sourcewrite)**. Subsequently, you can use external tools such as


*  [MRIcron](http://www.mccauslandcenter.sc.edu/mricro/mricron/index.html)

*  [OpenWallnut](http://www.openwalnut.org)

*  [Connectome Workbench](http://www.humanconnectome.org/software/connectome-workbench.html)


## Suggested further reading

Plotting channel-level data in a 2-dimensional representation on your flat computer screen or on paper requires that the 3-dimensional channel positions are mapped or projected onto the 2-dimensional plane. The tutorial on [specifying the channel layout for plotting](/layout) explains how this mapping is constructed.   

FAQ
{{topic>plot +faq &list}}

Example script
{{topic>plot +example &list}}

