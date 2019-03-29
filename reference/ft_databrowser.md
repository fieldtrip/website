---
title: ft_databrowser
---
```
 FT_DATABROWSER can be used for visual inspection of data. Artifacts that were
 detected by artifact functions (see FT_ARTIFACT_xxx functions where xxx is the type
 of artifact) are marked. Additionally data pieces can be marked and unmarked as
 artifact by manual selection. The output cfg contains the updated specification of
 the artifacts.

 Use as
   cfg = ft_databrowser(cfg)
   cfg = ft_databrowser(cfg, data)
 If you only specify the configuration structure, it should contain the name of the
 dataset on your hard disk (see below). If you specify input data, it should be a
 data structure as obtained from FT_PREPROCESSING or from FT_COMPONENTANALYSIS.

 If you want to browse data that is on disk, you have to specify
   cfg.dataset                 = string with the filename
 Instead of specifying the dataset, you can also explicitely specify the name of the
 file containing the header information and the name of the file containing the
 data, using
   cfg.datafile                = string with the filename
   cfg.headerfile              = string with the filename

 The following configuration options are supported:
   cfg.ylim                    = vertical scaling, can be 'maxmin', 'maxabs' or [ymin ymax] (default = 'maxabs')
   cfg.zlim                    = color scaling to apply to component topographies, 'minmax', 'maxabs' (default = 'maxmin')
   cfg.blocksize               = duration in seconds for cutting the data up
   cfg.trl                     = structure that defines the data segments of interest, only applicable for trial-based data
   cfg.continuous              = 'yes' or 'no', whether the data should be interpreted as continuous or trial-based
   cfg.allowoverlap            = 'yes' or 'no', whether data that is overlapping in multiple trials is allowed (default = 'no')
   cfg.channel                 = cell-array with channel labels, see FT_CHANNELSELECTION
   cfg.channelclamped          = cell-array with channel labels, that (when using the 'vertical' viewmode) will always be shown at the bottom. This is useful for showing ECG/EOG channels along with the other channels
   cfg.plotlabels              = 'yes', 'no' or 'some', whether to plot channel labels in vertical viewmode. The option 'some' plots one label for every ten channels, which is useful if there are many channels. (default = 'yes')
   cfg.ploteventlabels         = 'type=value', 'colorvalue' (default = 'type=value');
   cfg.plotevents              = 'no' or 'yes', whether to plot event markers. (default is 'yes')
   cfg.viewmode                = string, 'butterfly', 'vertical', 'component' for visualizing ICA/PCA components (default is 'butterfly')
   cfg.artfctdef.xxx.artifact  = Nx2 matrix with artifact segments see FT_ARTIFACT_xxx functions
   cfg.selectfeature           = string, name of feature to be selected/added (default = 'visual')
   cfg.selectmode              = 'markartifact', 'markpeakevent', 'marktroughevent' (default = 'markartifact')
   cfg.colorgroups             = 'sequential' 'allblack' 'labelcharx' (x = xth character in label), 'chantype' or vector with length(data/hdr.label) defining groups (default = 'sequential')
   cfg.channelcolormap         = COLORMAP (default = customized lines map with 15 colors)
   cfg.verticalpadding         = number or 'auto', padding to be added to top and bottom of plot to avoid channels largely dissappearing when viewmode = 'vertical'/'component'  (default = 'auto'). The padding is expressed as a proportion of the total height added to the top and bottom. The setting 'auto' determines the padding depending on the number of channels that are being plotted.
   cfg.selfun                  = string, name of function that is evaluated using the right-click context menu. The selected data and cfg.selcfg are passed on to this function.
   cfg.selcfg                  = configuration options for function in cfg.selfun
   cfg.seldat                  = 'selected' or 'all', specifies whether only the currently selected or all channels will be passed to the selfun (default = 'selected')
   cfg.renderer                = string, 'opengl', 'zbuffer', 'painters', see MATLAB Figure Properties. If this function crashes, you should try 'painters'.
   cfg.position                = location and size of the figure, specified as a vector of the form [left bottom width height].

 The following options for the scaling of the EEG, EOG, ECG, EMG and MEG channels is
 optional and can be used to bring the absolute numbers of the different channel
 types in the same range (e.g. fT and uV). The channel types are determined from the
 input data using FT_CHANNELSELECTION.
   cfg.eegscale                = number, scaling to apply to the EEG channels prior to display
   cfg.eogscale                = number, scaling to apply to the EOG channels prior to display
   cfg.ecgscale                = number, scaling to apply to the ECG channels prior to display
   cfg.emgscale                = number, scaling to apply to the EMG channels prior to display
   cfg.megscale                = number, scaling to apply to the MEG channels prior to display
   cfg.gradscale               = number, scaling to apply to the MEG gradiometer channels prior to display (in addition to the cfg.megscale factor)
   cfg.magscale                = number, scaling to apply to the MEG magnetometer channels prior to display (in addition to the cfg.megscale factor)
   cfg.mychanscale             = number, scaling to apply to the channels specified in cfg.mychan
   cfg.mychan                  = Nx1 cell-array with selection of channels
   cfg.chanscale               = Nx1 vector with scaling factors, one per channel specified in cfg.channel
   cfg.compscale               = string, 'global' or 'local', defines whether the colormap for the topographic scaling is applied per topography or on all visualized components (default 'global')

 You can specify preprocessing options that are to be applied to the  data prior to
 display. Most options from FT_PREPROCESSING are supported. They should be specified
 in the sub-structure cfg.preproc like these examples
   cfg.preproc.lpfilter        = 'no' or 'yes'  lowpass filter (default = 'no')
   cfg.preproc.lpfreq          = lowpass  frequency in Hz
   cfg.preproc.demean          = 'no' or 'yes', whether to apply baseline correction (default = 'no')
   cfg.preproc.detrend         = 'no' or 'yes', remove linear trend from the data (done per trial) (default = 'no')
   cfg.preproc.baselinewindow  = [begin end] in seconds, the default is the complete trial (default = 'all')

 In case of component viewmode, a layout is required. If no layout is specified, an
 attempt is made to construct one from the sensor definition that is present in the
 data or specified in the configuration.
   cfg.layout                  = filename of the layout, see FT_PREPARE_LAYOUT
   cfg.elec                    = structure with electrode positions or filename, see FT_READ_SENS
   cfg.grad                    = structure with gradiometer definition or filename, see FT_READ_SENS

 The default font size might be too small or too large, depending on the number of
 channels. You can use the following options to change the size of text inside the
 figure and along the axes.
   cfg.fontsize                = number, fontsize inside the figure (default = 0.03)
   cfg.fontunits               = string, can be 'normalized', 'points', 'pixels', 'inches' or 'centimeters' (default = 'normalized')
   cfg.axisfontsize            = number, fontsize along the axes (default = 10)
   cfg.axisfontunits           = string, can be 'normalized', 'points', 'pixels', 'inches' or 'centimeters' (default = 'points')
   cfg.linewidth               = number, width of plotted lines (default = 0.5)

 When visually selection data, a right-click will bring up a context-menu containing
 functions to be executed on the selected data. You can use your own function using
 cfg.selfun and cfg.selcfg. You can use multiple functions by giving the names/cfgs
 as a cell-array.

 In butterfly and vertical mode, you can use the "identify" button to reveal the name of a
 channel. Please be aware that it searches only vertically. This means that it will
 return the channel with the amplitude closest to the point you have clicked at the
 specific time point. This might be counterintuitive at first.

 The "cfg.artfctdef" structure in the output cfg is comparable to the configuration
 used by the artifact detection functions like FT_ARTIFACT_ZVALUE and in
 FT_REJECTARTIFACT. It contains for each artifact type an Nx2 matrix in which the
 first column corresponds to the begin samples of an artifact period, the second
 column contains the end samples of the artifact periods.

 Note for debugging: in case the databrowser crashes, use delete(gcf) to kill the
 figure.

 See also FT_PREPROCESSING, FT_REJECTARTIFACT, FT_ARTIFACT_EOG, FT_ARTIFACT_MUSCLE,
 FT_ARTIFACT_JUMP, FT_ARTIFACT_MANUAL, FT_ARTIFACT_THRESHOLD, FT_ARTIFACT_CLIP,
 FT_ARTIFACT_ECG, FT_COMPONENTANALYSIS
```
