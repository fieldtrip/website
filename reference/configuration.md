---
title: Index of all configuration options
---

# Index of all configuration options 

A detailed description of each function is available in the [reference documentation](/reference).

**cfg.TR** - [ft_realtime_fmriproxy](/reference/ft_realtime_fmriproxy)  
2.0

## A 

**cfg.absdiff** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or 'yes', computes absolute derivative (i.e. first derivative then rectify)

**cfg.absnoise** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
add noise with absolute level

**cfg.absnoise** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation), [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
scalar (default: 1), specifying the standard deviation of white noise superimposed on top of the simulated signals

**cfg.accuracy_green** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
distance from fiducial coordinate; green when within limits (default = 0.15 cm)

**cfg.accuracy_orange** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
orange when within limits, red when out (default = 0.3 cm)

**cfg.acquisition** - [ft_realtime_neuralynxproxy](/reference/ft_realtime_neuralynxproxy)  
string, name of computer running the Cheetah software (default = 'fcdc284')

**cfg.age** - [ft_nirs_prepare_ODtransformation](/reference/ft_nirs_prepare_ODtransformation), [ft_nirs_transform_ODs](/reference/ft_nirs_transform_ODs)  
scalar, age of the subject (necessary to automatically select the appropriate DPF, or

**cfg.align** - [ft_spike_waveform](/reference/ft_spike_waveform)  
'yes' (def). or 'no'. If 'yes', we align all waves to maximum

**cfg.align** - [ft_appendlayout](/reference/ft_appendlayout)  
string, 'center', 'left', 'right', 'top' or 'bottom' (default = 'center')

**cfg.alim** - [ft_rejectvisual](/reference/ft_rejectvisual)  
value that determines the amplitude scaling for the channel and trial display, if empty then the amplitude scaling is automatic (default = [])

**cfg.allowoverlap** - [ft_databrowser](/reference/ft_databrowser)  
'yes' or 'no', whether data that is overlapping in multiple trials is allowed (default = 'no')

**cfg.alpha** - [ft_statistics_analytic](/reference/ft_statistics_analytic), [ft_statistics_stats](/reference/ft_statistics_stats)  
number, critical value for rejecting the null-hypothesis (default = 0.05)

**cfg.alpha** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
number, critical value for rejecting the null-hypothesis per tail (default = 0.05)

**cfg.alpha** - [ft_clusterplot](/reference/ft_clusterplot)  
number, highest cluster p-value to be plotted max 0.3 (default = 0.05)

**cfg.alpha** - [ft_sliceinterp](/reference/ft_sliceinterp)  
value between 0 and 1 or 'adaptive' (default)

**cfg.alphaparam** - [ft_topoplotCC](/reference/ft_topoplotCC)  
string, parameter to be used to control the opacity (see below)

**cfg.ampl** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
nxn matrix, specifying the amplitude

**cfg.analyze** - [ft_qualitycheck](/reference/ft_qualitycheck)  
string, 'yes' or 'no' to analyze the dataset (default = 'yes')

**cfg.anaparameter** - [ft_sourceplot](/reference/ft_sourceplot)  
string, field in data with the anatomical data (default = 'anatomy' if present in data)

**cfg.anonimize** - [ft_audiovideobrowser](/reference/ft_audiovideobrowser)  
[x1 x2 y1 y2], range in pixels for placing a bar over the eyes (default = [])

**cfg.appenddim** - [ft_appendfreq](/reference/ft_appendfreq)  
string, the dimension to concatenate over (default is automatic)

**cfg.appenddim** - [ft_appendtimelock](/reference/ft_appendtimelock)  
string, the dimension to concatenate over which to append, this can be 'chan' and 'rpt' (default is automatic)

**cfg.arrowhead** - [ft_topoplotCC](/reference/ft_topoplotCC)  
string, 'none', 'stop', 'start', 'both' (default = 'none') cfg.arrowsize = scalar, size of the arrow head in figure units, i.e. the same units as the layout (default is automatically determined) cfg.arrowoffset = scalar, amount that the arrow is shifted to the side in figure units, i.e. the same units as the layout (default is automatically determined) cfg.arrowlength = scalar, amount by which the length is reduced relative to the complete line (default = 0.8)

**cfg.artfctdef.clip.amplthreshold** - [ft_artifact_clip](/reference/ft_artifact_clip)  
number, minimum amplitude difference in consecutive samples to be considered as 'clipped' (default = 0) string, percent of the amplitude range considered as 'clipped' (i.e. '1%')

**cfg.artfctdef.clip.channel** - [ft_artifact_clip](/reference/ft_artifact_clip)  
Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details

**cfg.artfctdef.clip.pretim** - [ft_artifact_clip](/reference/ft_artifact_clip)  
0.000; pre-artifact rejection-interval in seconds

**cfg.artfctdef.clip.psttim** - [ft_artifact_clip](/reference/ft_artifact_clip)  
0.000; post-artifact rejection-interval in seconds

**cfg.artfctdef.clip.timethreshold** - [ft_artifact_clip](/reference/ft_artifact_clip)  
number, minimum duration in seconds of a datasegment with consecutive identical samples to be considered as 'clipped'

**cfg.artfctdef.crittoilim** - [ft_rejectartifact](/reference/ft_rejectartifact)  
when using complete rejection, reject trial only when artifacts occur within this time window (default = whole trial). This only works with in-memory data, since trial time axes are unknown for data on disk.

**cfg.artfctdef.ecg.channel** - [ft_artifact_ecg](/reference/ft_artifact_ecg)  
Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details

**cfg.artfctdef.ecg.cutoff** - [ft_artifact_ecg](/reference/ft_artifact_ecg)  
3; peak-threshold

**cfg.artfctdef.ecg.inspect** - [ft_artifact_ecg](/reference/ft_artifact_ecg)  
Nx1 list of channels which will be shown in a QRS-locked average

**cfg.artfctdef.ecg.method** - [ft_artifact_ecg](/reference/ft_artifact_ecg)  
'zvalue'; peak-detection method

**cfg.artfctdef.ecg.pretim** - [ft_artifact_ecg](/reference/ft_artifact_ecg)  
0.05; pre-artifact rejection-interval in seconds

**cfg.artfctdef.ecg.psttim** - [ft_artifact_ecg](/reference/ft_artifact_ecg)  
0.3; post-artifact rejection-interval in seconds

**cfg.artfctdef.eog.artifact** - [ft_rejectartifact](/reference/ft_rejectartifact)  
Nx2 matrix with artifact segments, this is added to the cfg by using FT_ARTIFACT_EOG

**cfg.artfctdef.eog.artpadding** - [ft_artifact_eog](/reference/ft_artifact_eog)  
0.1

**cfg.artfctdef.eog.bpfilter** - [ft_artifact_eog](/reference/ft_artifact_eog)  
'yes'

**cfg.artfctdef.eog.bpfiltord** - [ft_artifact_eog](/reference/ft_artifact_eog)  
4

**cfg.artfctdef.eog.bpfilttype** - [ft_artifact_eog](/reference/ft_artifact_eog)  
'but'

**cfg.artfctdef.eog.bpfreq** - [ft_artifact_eog](/reference/ft_artifact_eog)  
[1 15]

**cfg.artfctdef.eog.channel** - [ft_artifact_eog](/reference/ft_artifact_eog)  
Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details

**cfg.artfctdef.eog.cutoff** - [ft_artifact_eog](/reference/ft_artifact_eog)  
z-value at which to threshold (default = 4)

**cfg.artfctdef.eog.fltpadding** - [ft_artifact_eog](/reference/ft_artifact_eog)  
0.1

**cfg.artfctdef.eog.hilbert** - [ft_artifact_eog](/reference/ft_artifact_eog)  
'yes'

**cfg.artfctdef.eog.trlpadding** - [ft_artifact_eog](/reference/ft_artifact_eog)  
0.5

**cfg.artfctdef.feedback** - [ft_rejectartifact](/reference/ft_rejectartifact)  
'yes' or 'no' (default = 'no')

**cfg.artfctdef.invert** - [ft_rejectartifact](/reference/ft_rejectartifact)  
'yes' or 'no' (default = 'no')

**cfg.artfctdef.jump.absdiff** - [ft_artifact_jump](/reference/ft_artifact_jump)  
'yes'

**cfg.artfctdef.jump.artifact** - [ft_rejectartifact](/reference/ft_rejectartifact)  
Nx2 matrix with artifact segments, this is added to the cfg by using FT_ARTIFACT_JUMP

**cfg.artfctdef.jump.artpadding** - [ft_artifact_jump](/reference/ft_artifact_jump)  
automatically determined based on the filter padding (cfg.padding)

**cfg.artfctdef.jump.channel** - [ft_artifact_jump](/reference/ft_artifact_jump)  
Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details

**cfg.artfctdef.jump.cutoff** - [ft_artifact_jump](/reference/ft_artifact_jump)  
z-value at which to threshold (default = 20)

**cfg.artfctdef.jump.medianfilter** - [ft_artifact_jump](/reference/ft_artifact_jump)  
'yes'

**cfg.artfctdef.jump.medianfiltord** - [ft_artifact_jump](/reference/ft_artifact_jump)  
9

**cfg.artfctdef.jump.trlpadding** - [ft_artifact_jump](/reference/ft_artifact_jump)  
automatically determined based on the filter padding (cfg.padding)

**cfg.artfctdef.minaccepttim** - [ft_rejectartifact](/reference/ft_rejectartifact)  
when using partial rejection, minimum length in seconds of remaining trial (default = 0.1)

**cfg.artfctdef.muscle.artifact** - [ft_rejectartifact](/reference/ft_rejectartifact)  
Nx2 matrix with artifact segments, this is added to the cfg by using FT_ARTIFACT_MUSCLE

**cfg.artfctdef.muscle.artpadding** - [ft_artifact_muscle](/reference/ft_artifact_muscle)  
0.1

**cfg.artfctdef.muscle.boxcar** - [ft_artifact_muscle](/reference/ft_artifact_muscle)  
0.2

**cfg.artfctdef.muscle.bpfilter** - [ft_artifact_muscle](/reference/ft_artifact_muscle)  
'yes'

**cfg.artfctdef.muscle.bpfiltord** - [ft_artifact_muscle](/reference/ft_artifact_muscle)  
8

**cfg.artfctdef.muscle.bpfilttype** - [ft_artifact_muscle](/reference/ft_artifact_muscle)  
'but'

**cfg.artfctdef.muscle.bpfreq** - [ft_artifact_muscle](/reference/ft_artifact_muscle)  
[110 140]

**cfg.artfctdef.muscle.channel** - [ft_artifact_muscle](/reference/ft_artifact_muscle)  
Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details

**cfg.artfctdef.muscle.cutoff** - [ft_artifact_muscle](/reference/ft_artifact_muscle)  
z-value at which to threshold (default = 4)

**cfg.artfctdef.muscle.fltpadding** - [ft_artifact_muscle](/reference/ft_artifact_muscle)  
0.1

**cfg.artfctdef.muscle.hilbert** - [ft_artifact_muscle](/reference/ft_artifact_muscle)  
'yes'

**cfg.artfctdef.muscle.trlpadding** - [ft_artifact_muscle](/reference/ft_artifact_muscle)  
0.1

**cfg.artfctdef.nan.channel** - [ft_artifact_nan](/reference/ft_artifact_nan)  
Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details

**cfg.artfctdef.reject** - [ft_rejectartifact](/reference/ft_rejectartifact)  
'none', 'partial', 'complete', 'nan', or 'value' (default = 'complete')

**cfg.artfctdef.threshold.bpfilter** - [ft_artifact_threshold](/reference/ft_artifact_threshold)  
'no' or 'yes' (default = 'yes')

**cfg.artfctdef.threshold.bpfiltord** - [ft_artifact_threshold](/reference/ft_artifact_threshold)  
4

**cfg.artfctdef.threshold.bpfreq** - [ft_artifact_threshold](/reference/ft_artifact_threshold)  
[0.3 30]

**cfg.artfctdef.threshold.channel** - [ft_artifact_threshold](/reference/ft_artifact_threshold)  
cell-array with channel labels

**cfg.artfctdef.threshold.max** - [ft_artifact_threshold](/reference/ft_artifact_threshold)  
value in uV or T, default inf

**cfg.artfctdef.threshold.min** - [ft_artifact_threshold](/reference/ft_artifact_threshold)  
value in uV or T, default -inf

**cfg.artfctdef.threshold.offset** - [ft_artifact_threshold](/reference/ft_artifact_threshold)  
value in uV or T, default inf

**cfg.artfctdef.threshold.onset** - [ft_artifact_threshold](/reference/ft_artifact_threshold)  
value in uV or T, default inf

**cfg.artfctdef.threshold.range** - [ft_artifact_threshold](/reference/ft_artifact_threshold)  
value in uV or T, default inf

**cfg.artfctdef.tms.artpadding** - [ft_artifact_tms](/reference/ft_artifact_tms)  
0.01

**cfg.artfctdef.tms.channel** - [ft_artifact_tms](/reference/ft_artifact_tms)  
Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details

**cfg.artfctdef.tms.cutoff** - [ft_artifact_tms](/reference/ft_artifact_tms)  
z-value at which to threshold (default = 4)

**cfg.artfctdef.tms.derivative** - [ft_artifact_tms](/reference/ft_artifact_tms)  
'yes'

**cfg.artfctdef.tms.fltpadding** - [ft_artifact_tms](/reference/ft_artifact_tms)  
0.1

**cfg.artfctdef.tms.trlpadding** - [ft_artifact_tms](/reference/ft_artifact_tms)  
0.1

**cfg.artfctdef.value** - [ft_rejectartifact](/reference/ft_rejectartifact)  
scalar value to replace the data in the artifact segments (default = nan)

**cfg.artfctdef.visual.artifact** - [ft_rejectartifact](/reference/ft_rejectartifact)  
Nx2 matrix with artifact segments, this is added to the cfg by using FT_DATABROWSER

**cfg.artfctdef.xxx.artifact** - [ft_databrowser](/reference/ft_databrowser)  
Nx2 matrix with artifact segments see FT_ARTIFACT_xxx functions

**cfg.artfctdef.xxx.artifact** - [ft_rejectartifact](/reference/ft_rejectartifact)  
Nx2 matrix with artifact segments, this could be added by your own artifact detection function

**cfg.artfctdef.zvalue.artfctpeak** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'yes' or 'no'

**cfg.artfctdef.zvalue.artifact** - [ft_rejectartifact](/reference/ft_rejectartifact)  
Nx2 matrix with artifact segments, this is added to the cfg by using FT_ARTIFACT_ZVALUE

**cfg.artfctdef.zvalue.artpadding** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  


**cfg.artfctdef.zvalue.baselinewindow** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
[begin end] in seconds, the default is the complete trial

**cfg.artfctdef.zvalue.bpfilter** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'no' or 'yes' bandpass filter

**cfg.artfctdef.zvalue.bpfiltord** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
bandpass filter order

**cfg.artfctdef.zvalue.bpfilttype** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'

**cfg.artfctdef.zvalue.bpfreq** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
bandpass frequency range, specified as [low high] in Hz

**cfg.artfctdef.zvalue.bsfilter** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'no' or 'yes' bandstop filter for line noise removal

**cfg.artfctdef.zvalue.bsfiltord** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
bandstop filter order

**cfg.artfctdef.zvalue.bsfilttype** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'

**cfg.artfctdef.zvalue.bsfreq** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
bandstop frequency range, specified as [low high] in Hz

**cfg.artfctdef.zvalue.channel** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  


**cfg.artfctdef.zvalue.cutoff** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  


**cfg.artfctdef.zvalue.demean** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'no' or 'yes'

**cfg.artfctdef.zvalue.detrend** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'no' or 'yes'

**cfg.artfctdef.zvalue.dftfilter** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'no' or 'yes' line noise removal using discrete fourier transform

**cfg.artfctdef.zvalue.fltpadding** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  


**cfg.artfctdef.zvalue.hilbert** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'no' or 'yes'

**cfg.artfctdef.zvalue.hpfilter** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'no' or 'yes' highpass filter

**cfg.artfctdef.zvalue.hpfiltord** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
highpass filter order

**cfg.artfctdef.zvalue.hpfilttype** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'

**cfg.artfctdef.zvalue.hpfreq** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
highpass frequency in Hz

**cfg.artfctdef.zvalue.interactive** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'yes' or 'no'

**cfg.artfctdef.zvalue.lpfilter** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'no' or 'yes' lowpass filter

**cfg.artfctdef.zvalue.lpfiltord** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
lowpass filter order

**cfg.artfctdef.zvalue.lpfilttype** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
digital filter type, 'but' (default) or 'firws' or 'fir' or 'firls'

**cfg.artfctdef.zvalue.lpfreq** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
lowpass frequency in Hz

**cfg.artfctdef.zvalue.medianfilter** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'no' or 'yes' jump preserving median filter

**cfg.artfctdef.zvalue.medianfiltord** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
length of median filter

**cfg.artfctdef.zvalue.rectify** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'no' or 'yes'

**cfg.artfctdef.zvalue.trlpadding** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  


**cfg.artifact** - [ft_removetemplateartifact](/reference/ft_removetemplateartifact)  
Mx2 matrix with sample numbers of the artifact segments, e.g. obtained from FT_ARTIFACT_EOG

**cfg.asymmetry** - [ft_freqsimulation](/reference/ft_freqsimulation)  
amount of asymmetry (default = 0, which is none)

**cfg.atlas** - [ft_sourceplot](/reference/ft_sourceplot)  
string, filename of atlas to use (default = []) see FT_READ_ATLAS for ROI masking (see 'masking' below) or for orthogonal plots (see method='ortho' below)

**cfg.atlas** - [ft_volumelookup](/reference/ft_volumelookup), [ft_volumelookup](/reference/ft_volumelookup), [ft_volumelookup](/reference/ft_volumelookup)  
string, filename of atlas to use, see FT_READ_ATLAS

**cfg.audiofile** - [ft_audiovideobrowser](/reference/ft_audiovideobrowser)  
string with the filename

**cfg.audiohdr** - [ft_audiovideobrowser](/reference/ft_audiovideobrowser)  
header structure of the audio data, see FT_READ_HEADER

**cfg.avgoverchan** - [ft_spiketriggeredspectrum_stat](/reference/ft_spiketriggeredspectrum_stat)  
'weighted', 'unweighted' (default) or 'no'. This regulates averaging of fourierspectra prior to computing the statistic. - 'weighted' : we average across channels by weighting by the LFP power. This is identical to adding the raw LFP signals in time and then taking their FFT. - 'unweighted': we average across channels after normalizing for LFP power. This is identical to normalizing LFP signals for their power, averaging them, and then taking their FFT. - 'no' : no weighting is performed, statistic is computed for every LFP channel.

**cfg.avgoverchan** - [ft_freqstatistics](/reference/ft_freqstatistics), [ft_timelockstatistics](/reference/ft_timelockstatistics)  
'yes' or 'no' (default = 'no')

**cfg.avgoverfreq** - [ft_freqstatistics](/reference/ft_freqstatistics)  
'yes' or 'no' (default = 'no')

**cfg.avgoverfreq** - [ft_sourceplot](/reference/ft_sourceplot)  
string, can be 'yes' or 'no' (default = 'no')

**cfg.avgovertime** - [ft_freqstatistics](/reference/ft_freqstatistics), [ft_timelockstatistics](/reference/ft_timelockstatistics)  
'yes' or 'no' (default = 'no')

**cfg.avgovertime** - [ft_sourceplot](/reference/ft_sourceplot)  
string, can be 'yes' or 'no' (default = 'no')

**cfg.axes** - [ft_multiplotER](/reference/ft_multiplotER)  
string, 'yes' or 'no' whether to draw x- and y-axes for each graph (default = 'yes')

**cfg.axis** - [ft_sourceplot](/reference/ft_sourceplot)  
'on' or 'off' (default = 'on')

**cfg.axisfontsize** - [ft_databrowser](/reference/ft_databrowser)  
number, fontsize along the axes (default = 10)

**cfg.axisfontunits** - [ft_databrowser](/reference/ft_databrowser)  
string, can be 'normalized', 'points', 'pixels', 'inches' or 'centimeters' (default = 'points')

## B 

**cfg.backproject** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
'yes' or 'no' (default = 'yes') determines when reducerank is applied whether the lower rank leadfield is projected back onto the original linear subspace, or not.

**cfg.badchannel** - [ft_channelrepair](/reference/ft_channelrepair)  
cell-array, see FT_CHANNELSELECTION for details

**cfg.badchannel** - [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity)  
cell-array, see FT_CHANNELSELECTION for details (default = [])

**cfg.bandwidth** - [ft_connectivityanalysis](/reference/ft_connectivityanalysis)  
scalar, (default = Rayleigh frequency), needed for

**cfg.baseline** - [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotTFR](/reference/ft_singleplotTFR)  
'yes', 'no' or [time1 time2] (default = 'no'), see FT_FREQBASELINE

**cfg.baseline** - [ft_multiplotER](/reference/ft_multiplotER)  
'yes', 'no' or [time1 time2] (default = 'no'), see FT_TIMELOCKBASELINE or FT_FREQBASELINE

**cfg.baseline** - [ft_singleplotER](/reference/ft_singleplotER)  
'yes', 'no' or [time1 time2] (default = 'no'), see ft_timelockbaseline

**cfg.baseline** - [ft_movieplotER](/reference/ft_movieplotER)  
'yes','no' or [time1 time2] (default = 'no'), see FT_TIMELOCKBASELINE

**cfg.baseline** - [ft_movieplotTFR](/reference/ft_movieplotTFR), [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
'yes','no' or [time1 time2] (default = 'no'), see FT_TIMELOCKBASELINE or FT_FREQBASELINE

**cfg.baseline** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
(optional)

**cfg.baseline** - [ft_timelockbaseline](/reference/ft_timelockbaseline)  
[begin end] (default = 'no')

**cfg.baseline** - [ft_freqbaseline](/reference/ft_freqbaseline)  
[begin end] (default = 'no'), alternatively an Nfreq x 2 matrix can be specified, that provides frequency specific baseline windows.

**cfg.baseline** - [ft_timelocksimulation](/reference/ft_timelocksimulation)  
number (default = 0.3)

**cfg.baseline** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
scalar, baseline length in seconds (default = 0)

**cfg.baselinetype** - [ft_movieplotER](/reference/ft_movieplotER), [ft_singleplotER](/reference/ft_singleplotER), [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
'absolute' or 'relative' (default = 'absolute')

**cfg.baselinetype** - [ft_freqbaseline](/reference/ft_freqbaseline), [ft_movieplotTFR](/reference/ft_movieplotTFR), [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotTFR](/reference/ft_singleplotTFR)  
'absolute', 'relative', 'relchange', 'normchange', 'db' or 'zscore' (default = 'absolute')

**cfg.baselinewindow** - [ft_combineplanar](/reference/ft_combineplanar)  
[begin end]

**cfg.baselinewindow** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation), [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
[begin end] in seconds, the default is the complete trial

**cfg.baselinewindow** - [ft_preprocessing](/reference/ft_preprocessing), [ft_resampledata](/reference/ft_resampledata)  
[begin end] in seconds, the default is the complete trial (default = 'all')

**cfg.baudrate** - [ft_omri_quality](/reference/ft_omri_quality)  
serial port baudrate (default = 19200)

**cfg.bcifun** - [ft_realtime_packettimer](/reference/ft_realtime_packettimer)  
processing of the data (default = @bcifun_timer)

**cfg.bcifun** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_synchronous](/reference/ft_realtime_synchronous)  
the BCI function that is called

**cfg.begsample** - [ft_redefinetrial](/reference/ft_redefinetrial)  
single number or Nx1 vector, expressed in samples relative to the start of the input trial

**cfg.binica.annealdeg** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.annealstep** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.bias** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.blocksize** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.extended** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.filenum** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.lrate** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.maxsteps** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.momentum** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.pca** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.posact** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.sphering** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.stop** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.verbose** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.binica.weightsin** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.bins** - [ft_spike_isi](/reference/ft_spike_isi)  
ascending vector of isi bin edges.

**cfg.binsize** - [ft_spike_xcorr](/reference/ft_spike_xcorr)  
[binsize] in sec (default = 0.001 sec).

**cfg.binsize** - [ft_spike_psth](/reference/ft_spike_psth)  
[binsize] in sec or string. If 'scott', we estimate the optimal bin width using Scott's formula (1979). If 'sqrt', we take the number of bins as the square root of the number of observations. The optimal bin width is derived over all neurons; thus, this procedure works best if the input contains only one neuron at a time.

**cfg.blocksize** - [ft_realtime_topography](/reference/ft_realtime_topography)  
0.5;

**cfg.blocksize** - [ft_icabrowser](/reference/ft_icabrowser)  
blocksize of time course (default = 1 sec)

**cfg.blocksize** - [ft_databrowser](/reference/ft_databrowser)  
duration in seconds for cutting the data up

**cfg.blocksize** - [ft_realtime_modeegproxy](/reference/ft_realtime_modeegproxy)  
number, in seconds (default = 0.125)

**cfg.blocksize** - [ft_realtime_jaga16proxy](/reference/ft_realtime_jaga16proxy), [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
number, in seconds (default = 0.5)

**cfg.blocksize** - [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer), [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer), [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect), [ft_realtime_ouunpod](/reference/ft_realtime_ouunpod), [ft_realtime_powerestimate](/reference/ft_realtime_powerestimate), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer), [ft_realtime_topography](/reference/ft_realtime_topography)  
number, size of the blocks/chuncks that are processed (default = 1 second)

**cfg.blocksize** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_synchronous](/reference/ft_realtime_synchronous)  
number, size of the blocks/chuncks that are processed in seconds (default = 1)

**cfg.blocksize** - [ft_realtime_pooraudioproxy](/reference/ft_realtime_pooraudioproxy)  
size of recorded audio blocks in seconds (default=1)

**cfg.bootstrap** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes' bootstrap resampling of trials

**cfg.borderspikes** - [ft_spiketriggeredspectrum_convol](/reference/ft_spiketriggeredspectrum_convol)  
'no', or if cfg.rejectsaturation = 'yes', or if the trial length was too short for the window desired.

**cfg.box** - [ft_multiplotTFR](/reference/ft_multiplotTFR)  
'yes', 'no' (default = 'no' if maskparameter given default = 'yes') Draw a box around each graph

**cfg.box** - [ft_volumelookup](/reference/ft_volumelookup)  
Nx3 vector, size of each box in cm/mm dep on unit of input

**cfg.box** - [ft_layoutplot](/reference/ft_layoutplot)  
string, 'yes' or 'no' whether box should be plotted around electrode (default = 'yes')

**cfg.box** - [ft_multiplotER](/reference/ft_multiplotER)  
string, 'yes' or 'no' whether to draw a box around each graph (default = 'no')

**cfg.boxchannel** - [ft_prepare_layout](/reference/ft_prepare_layout)  
'all', or Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details specificies channels to use for determining channel box size (default = 'all', recommended for MEG/EEG, a selection is recommended for iEEG)

**cfg.bpfiltdev** - [ft_preprocessing](/reference/ft_preprocessing)  
bandpass max passband deviation (firws with 'kaiser' window, default 0.001 set in low-level function)

**cfg.bpfiltdf** - [ft_preprocessing](/reference/ft_preprocessing)  
bandpass transition width (firws, overrides order, default set in low-level function)

**cfg.bpfiltdir** - [ft_preprocessing](/reference/ft_preprocessing)  
filter direction, 'twopass' (default), 'onepass' or 'onepass-reverse' or 'onepass-zerophase' (default for firws) or 'onepass-minphase' (firws, non-linear!)

**cfg.bpfilter** - [ft_preprocessing](/reference/ft_preprocessing), [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
'no' or 'yes' bandpass filter (default = 'no')

**cfg.bpfilter** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation), [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
'yes' (or 'no')

**cfg.bpfilter** - [ft_realtime_topography](/reference/ft_realtime_topography)  
[15 25];

**cfg.bpfiltord** - [ft_preprocessing](/reference/ft_preprocessing)  
bandpass filter order (default set in low-level function)

**cfg.bpfilttype** - [ft_preprocessing](/reference/ft_preprocessing)  
digital filter type, 'but' or 'firws' or 'fir' or 'firls' (default = 'but')

**cfg.bpfiltwintype** - [ft_preprocessing](/reference/ft_preprocessing)  
bandpass window type, 'hann' or 'hamming' (default) or 'blackman' or 'kaiser' (firws)

**cfg.bpfreq** - [ft_realtime_topography](/reference/ft_realtime_topography)  
	 'yes'; ft_realtime_topography(cfg);

**cfg.bpfreq** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation), [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
[bplow bphigh] (default: [15 25])

**cfg.bpfreq** - [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
bandpass frequency range, specified as [low high] in Hz

**cfg.bpfreq** - [ft_preprocessing](/reference/ft_preprocessing)  
bandpass frequency range, specified as [lowFreq highFreq] in Hz

**cfg.bpfreq** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
nxnx2 matrix, specifying the lower and upper frequencies of the bands that are transmitted, rows causing column

**cfg.bpinstabilityfix** - [ft_preprocessing](/reference/ft_preprocessing)  
deal with filter instability, 'no', 'reduce', 'split' (default = 'no')

**cfg.brainsmooth** - [ft_volumesegment](/reference/ft_volumesegment)  
'no', or scalar, the FWHM of the gaussian kernel in voxels, (default = 5)

**cfg.brainthreshold** - [ft_volumesegment](/reference/ft_volumesegment)  
'no', or scalar, relative threshold value which is used to threshold the tpm in order to create a volumetric brainmask (see below), (default = 0.5)

**cfg.bsfiltdev** - [ft_preprocessing](/reference/ft_preprocessing)  
bandstop max passband deviation (firws with 'kaiser' window, default 0.001 set in low-level function)

**cfg.bsfiltdf** - [ft_preprocessing](/reference/ft_preprocessing)  
bandstop transition width (firws, overrides order, default set in low-level function)

**cfg.bsfiltdir** - [ft_preprocessing](/reference/ft_preprocessing)  
filter direction, 'twopass' (default), 'onepass' or 'onepass-reverse' or 'onepass-zerophase' (default for firws) or 'onepass-minphase' (firws, non-linear!)

**cfg.bsfilter** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or 'yes' bandstop filter (default = 'no')

**cfg.bsfiltord** - [ft_preprocessing](/reference/ft_preprocessing)  
bandstop filter order (default set in low-level function)

**cfg.bsfilttype** - [ft_preprocessing](/reference/ft_preprocessing)  
digital filter type, 'but' or 'firws' or 'fir' or 'firls' (default = 'but')

**cfg.bsfiltwintype** - [ft_preprocessing](/reference/ft_preprocessing)  
bandstop window type, 'hann' or 'hamming' (default) or 'blackman' or 'kaiser' (firws)

**cfg.bsfreq** - [ft_preprocessing](/reference/ft_preprocessing)  
bandstop frequency range, specified as [low high] in Hz (or as Nx2 matrix for notch filter)

**cfg.bsinstabilityfix** - [ft_preprocessing](/reference/ft_preprocessing)  
deal with filter instability, 'no', 'reduce', 'split' (default = 'no')

**cfg.bufferdata** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_synchronous](/reference/ft_realtime_synchronous)  
causes the realtime function to jump to the last

**cfg.bufferdata** - [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer)  
causes the realtime function to jump to the last available data

**cfg.bufferdata** - [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer)  
whether to process the 'first or 'last' data that is available (default = 'last')

**cfg.bufferdata** - [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect), [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer)  
whether to start on the 'first or 'last' data that is available (default = 'first')

**cfg.bufferdata** - [ft_realtime_fmriviewer](/reference/ft_realtime_fmriviewer), [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer), [ft_realtime_ouunpod](/reference/ft_realtime_ouunpod), [ft_realtime_powerestimate](/reference/ft_realtime_powerestimate), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder)  
whether to start on the 'first or 'last' data that is available (default = 'last')

**cfg.bufferdata** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_synchronous](/reference/ft_realtime_synchronous)  
whether to start on the 'first or 'last' data that is available when the function _starts_ (default = 'last')

**cfg.bw** - [ft_prepare_layout](/reference/ft_prepare_layout)  
'yes' or 'no', if an image is used and this option is true, the image is transformed in black and white (default = 'no', i.e. do not transform)

## C 

**cfg.calibration** - [ft_realtime_jaga16proxy](/reference/ft_realtime_jaga16proxy)  
number, in uV per bit (default = 1)

**cfg.calibration** - [ft_spikedownsample](/reference/ft_spikedownsample)  
optional scaling factor to apply to the data to convert it in uV, see below

**cfg.camlight** - [ft_sourceplot](/reference/ft_sourceplot)  
'yes' or 'no' (default = 'yes')

**cfg.casesensitive** - [ft_electroderealign](/reference/ft_electroderealign)  
'yes' or 'no', determines whether string comparisons between electrode labels are case sensitive (default = 'yes')

**cfg.center** - [ft_prepare_layout](/reference/ft_prepare_layout)  
string, center and scale the electrodes in the sphere that represents the head, can be 'yes' or 'no' (default = 'no')

**cfg.channel** - [ft_realtime_topography](/reference/ft_realtime_topography)  
'MEG';

**cfg.channel** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
'all' (default) or list of channels for which an mvar model is fitted. (Do NOT specify if cfg.channelcmb is defined)

**cfg.channel** - [ft_stratify](/reference/ft_stratify)  
'all' or list with indices ( default = 'all')

**cfg.channel** - [ft_prepare_layout](/reference/ft_prepare_layout)  
'all', or Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details

**cfg.channel** - [ft_channelnormalise](/reference/ft_channelnormalise)  
'all', or a selection of channels

**cfg.channel** - [ft_connectivityanalysis](/reference/ft_connectivityanalysis)  
Nx1 cell-array containing a list of channels which are used for the subsequent computations. This only has an effect when the input data is univariate. See FT_CHANNELSELECTION

**cfg.channel** - [ft_spiketriggeredspectrum_stat](/reference/ft_spiketriggeredspectrum_stat)  
Nx1 cell-array or numerical array with selection of channels (default = 'all'),See CHANNELSELECTION for details

**cfg.channel** - [ft_megplanar](/reference/ft_megplanar)  
Nx1 cell-array with selection of channels (default = 'MEG'), see FT_CHANNELSELECTION for details

**cfg.channel** - [ft_nonlinearassociation](/reference/ft_nonlinearassociation)  
Nx1 cell-array with selection of channels (default = 'all'), see CHANNELSELECTION for details

**cfg.channel** - [ft_denoise_dssp](/reference/ft_denoise_dssp), [ft_dipolefitting](/reference/ft_dipolefitting), [ft_dipolesimulation](/reference/ft_dipolesimulation), [ft_electroderealign](/reference/ft_electroderealign), [ft_freqanalysis](/reference/ft_freqanalysis), [ft_freqdescriptives](/reference/ft_freqdescriptives), [ft_freqgrandaverage](/reference/ft_freqgrandaverage), [ft_freqstatistics](/reference/ft_freqstatistics), [ft_globalmeanfield](/reference/ft_globalmeanfield), [ft_multiplotER](/reference/ft_multiplotER), [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_prepare_leadfield](/reference/ft_prepare_leadfield), [ft_preprocessing](/reference/ft_preprocessing), [ft_rejectvisual](/reference/ft_rejectvisual), [ft_removetemplateartifact](/reference/ft_removetemplateartifact), [ft_singleplotTFR](/reference/ft_singleplotTFR), [ft_sourceanalysis](/reference/ft_sourceanalysis), [ft_spikedownsample](/reference/ft_spikedownsample), [ft_spikesplitting](/reference/ft_spikesplitting), [ft_spiketriggeredaverage](/reference/ft_spiketriggeredaverage), [ft_spiketriggeredinterpolation](/reference/ft_spiketriggeredinterpolation), [ft_timelockanalysis](/reference/ft_timelockanalysis), [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage), [ft_timelockstatistics](/reference/ft_timelockstatistics), [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details

**cfg.channel** - [ft_nirs_prepare_ODtransformation](/reference/ft_nirs_prepare_ODtransformation), [ft_nirs_transform_ODs](/reference/ft_nirs_transform_ODs)  
Nx1 cell-array with selection of channels (default = 'nirs'), see FT_CHANNELSELECTION for more details

**cfg.channel** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
Nx1 cell-array with selection of channels (default = {'1' '2' ...})

**cfg.channel** - [ft_detect_movement](/reference/ft_detect_movement)  
Nx1 cell-array with selection of channels, see FT_CHANNELSELECTION for details, (default = 'all')

**cfg.channel** - [ft_databrowser](/reference/ft_databrowser)  
cell-array with channel labels, see FT_CHANNELSELECTION

**cfg.channel** - [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
cell-array with channel names

**cfg.channel** - [ft_realtime_jaga16proxy](/reference/ft_realtime_jaga16proxy)  
cell-array with channel names, see FT_CHANNELSELECTION

**cfg.channel** - [ft_componentanalysis](/reference/ft_componentanalysis), [ft_spikesorting](/reference/ft_spikesorting)  
cell-array with channel selection (default = 'all'), see FT_CHANNELSELECTION for details

**cfg.channel** - [ft_crossfrequencyanalysis](/reference/ft_crossfrequencyanalysis)  
cell-array with selection of channels, see FT_CHANNELSELECTION

**cfg.channel** - [ft_timelockbaseline](/reference/ft_timelockbaseline)  
cell-array, see FT_CHANNELSELECTION

**cfg.channel** - [ft_denoise_prewhiten](/reference/ft_denoise_prewhiten), [ft_realtime_asaproxy](/reference/ft_realtime_asaproxy), [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_average](/reference/ft_realtime_average), [ft_realtime_brainampproxy](/reference/ft_realtime_brainampproxy), [ft_realtime_classification](/reference/ft_realtime_classification), [ft_realtime_downsample](/reference/ft_realtime_downsample), [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy), [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect), [ft_realtime_neuralynxproxy](/reference/ft_realtime_neuralynxproxy), [ft_realtime_oddball](/reference/ft_realtime_oddball), [ft_realtime_ouunpod](/reference/ft_realtime_ouunpod), [ft_realtime_powerestimate](/reference/ft_realtime_powerestimate), [ft_realtime_selectiveaverage](/reference/ft_realtime_selectiveaverage), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer), [ft_realtime_synchronous](/reference/ft_realtime_synchronous)  
cell-array, see FT_CHANNELSELECTION (default = 'all')

**cfg.channel** - [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer)  
cell-array, see FT_CHANNELSELECTION (default = {'MEG', 'MEGREF'})

**cfg.channel** - [ft_prepare_neighbours](/reference/ft_prepare_neighbours)  
channels for which neighbours should be found

**cfg.channel** - [ft_connectivityplot](/reference/ft_connectivityplot)  
list of channels to be included for the plotting (default = 'all'), see FT_CHANNELSELECTION for details

**cfg.channel** - [ft_realtime_pooraudioproxy](/reference/ft_realtime_pooraudioproxy)  
number of channels (1 or 2, default=2)

**cfg.channel** - [ft_singleplotER](/reference/ft_singleplotER)  
nx1 cell-array with selection of channels (default = 'all') see ft_channelselection for details

**cfg.channel** - [ft_electrodermalactivity](/reference/ft_electrodermalactivity), [ft_heartrate](/reference/ft_heartrate), [ft_respiration](/reference/ft_respiration)  
selected channel for processing, see FT_CHANNELSELECTION

**cfg.channel** - [ft_denoise_pca](/reference/ft_denoise_pca)  
the channels to be denoised (default = 'MEG')

**cfg.channel** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
the channels to be denoised (default = 'all'), see FT_SELECTDATA

**cfg.channelclamped** - [ft_databrowser](/reference/ft_databrowser)  
cell-array with channel labels, that (when using the 'vertical' viewmode) will always be shown at the bottom. This is useful for showing ECG/EOG channels along with the other channels

**cfg.channelcmb** - [ft_freqanalysis](/reference/ft_freqanalysis), [ft_spike_jpsth](/reference/ft_spike_jpsth), [ft_spike_xcorr](/reference/ft_spike_xcorr)  
Mx2 cell-array with selection of channel pairs (default = {'all' 'all'}), see FT_CHANNELCOMBINATION for details

**cfg.channelcmb** - [ft_lateralizedpotential](/reference/ft_lateralizedpotential)  
Nx2 cell-array

**cfg.channelcmb** - [ft_connectivityanalysis](/reference/ft_connectivityanalysis)  
Nx2 cell-array containing the channel combinations on which to compute the connectivity. This only has an effect when the input data is univariate. See FT_CHANNELCOMBINATION

**cfg.channelcmb** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
specify channel combinations as a two-column cell-array with channels in each column between which a bivariate model will be fit (overrides cfg.channel)

**cfg.channelcmb** - [ft_spike_plot_jpsth](/reference/ft_spike_plot_jpsth)  
string or index of single channel combination to trigger on. See SPIKESTATION_FT_SUB_CHANNELCOMBINATION for details.

**cfg.channelcmb** - [ft_lateralizedpotential](/reference/ft_lateralizedpotential)  
{'Fp1' 'Fp2' 'F7' 'F8' 'F3' 'F4' 'T7' 'T8' 'C3' 'C4' 'P7' 'P8' 'P3' 'P4' 'O1' 'O2'}

**cfg.channelcolormap** - [ft_databrowser](/reference/ft_databrowser)  
COLORMAP (default = customized lines map with 15 colors)

**cfg.channelprefix** - [ft_spikedownsample](/reference/ft_spikedownsample)  
string, will be added to channel name, e.g. 'lfp' -> 'lfp_ncs001' (default = [])

**cfg.chanscale** - [ft_databrowser](/reference/ft_databrowser)  
Nx1 vector with scaling factors, one per channel specified in cfg.channel

**cfg.chantype** - [ft_preprocessing](/reference/ft_preprocessing)  
string or Nx1 cell-array with channel types to be read (only for NeuroOmega)

**cfg.chanunit** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
units for the channel data

**cfg.clim** - [ft_volumerealign](/reference/ft_volumerealign)  
[min max], scaling of the anatomy color (default is to adjust to the minimum and maximum)

**cfg.clim** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
color range of the data (default = [0 1], i.e. the full range)

**cfg.clim** - [ft_sourceplot](/reference/ft_sourceplot)  
lower and upper anatomical MRI limits (default = [0 1])

**cfg.clipVar** - [ft_omri_quality](/reference/ft_omri_quality)  
threshold to clip variation plot with as a fraction of signal magnitude (default=0.2)

**cfg.clipmax** - [ft_sliceinterp](/reference/ft_sliceinterp)  
value or 'auto' (clipping of source data)

**cfg.clipmin** - [ft_sliceinterp](/reference/ft_sliceinterp)  
value or 'auto' (clipping of source data)

**cfg.clipsym** - [ft_sliceinterp](/reference/ft_sliceinterp)  
'yes' or 'no' (default) symmetrical clipping

**cfg.closedistance** - [ft_nirs_referencechannelsubtraction](/reference/ft_nirs_referencechannelsubtraction)  
scalar, defines the maximal distance between a shallow and a short channel in cm (default = 15). NOT APPLIED CURRENTLY!

**cfg.cloudtype** - [ft_sourceplot](/reference/ft_sourceplot)  
'point' plots a single point at each sensor position 'cloud' (default) plots each a group of spherically arranged points at each sensor position 'surf' plots a single spherical surface mesh at each sensor position

**cfg.clusteralpha** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
for either parametric or nonparametric thresholding per tail (default = 0.05)

**cfg.clustercritval** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
for parametric thresholding (default is determined by the statfun)

**cfg.clusterstatistic** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
how to combine the single samples that belong to a cluster, 'maxsum', 'maxsize', 'wcm' (default = 'maxsum') option 'wcm' refers to 'weighted cluster mass', a statistic that combines cluster size and intensity; see Hayasaka & Nichols (2004) NeuroImage for details

**cfg.clustertail** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
-1, 1 or 0 (default = 0)

**cfg.clusterthreshold** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
method for single-sample threshold, 'parametric', 'nonparametric_individual', 'nonparametric_common' (default = 'parametric')

**cfg.cmapneurons** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster)  
'auto' (default), or nUnits-by-3 matrix. Controls coloring of spikes and psth/density data if multiple cells are present.

**cfg.cohmethod** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'regular', 'lambda1', 'canonical'

**cfg.coilaccuracy** - [ft_preprocessing](/reference/ft_preprocessing)  
can be empty or a number (0, 1 or 2) to specify the accuracy (default = [])

**cfg.coilfreq** - [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer)  
single number in Hz or list of numbers

**cfg.coilfreq** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
single number in Hz or list of numbers (default = [293, 307, 314, 321, 328])

**cfg.colmax** - [ft_sliceinterp](/reference/ft_sliceinterp)  
source value mapped to the highest color (default = 'auto')

**cfg.colmin** - [ft_sliceinterp](/reference/ft_sliceinterp)  
source value mapped to the lowest color (default = 'auto')

**cfg.colorbar** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
'yes' 'no' (default) 'North' inside plot box near top 'South' inside bottom 'East' inside right 'West' inside left 'NorthOutside' outside plot box near top 'SouthOutside' outside bottom 'EastOutside' outside right 'WestOutside' outside left

**cfg.colorbar** - [ft_spike_plot_jpsth](/reference/ft_spike_plot_jpsth)  
'yes' (default) or 'no'

**cfg.colorbar** - [ft_sourceplot](/reference/ft_sourceplot)  
'yes' or 'no' (default = 'yes')

**cfg.colorbar** - [ft_movieplotER](/reference/ft_movieplotER), [ft_movieplotTFR](/reference/ft_movieplotTFR), [ft_multiplotTFR](/reference/ft_multiplotTFR)  
'yes', 'no' (default = 'no')

**cfg.colorbar** - [ft_singleplotTFR](/reference/ft_singleplotTFR)  
'yes', 'no' (default = 'yes')

**cfg.colorgrad** - [ft_sourceplot](/reference/ft_sourceplot)  
'white' or a scalar (e.g. 1), degree to which color of points in cloud changes from its center

**cfg.colorgroups** - [ft_databrowser](/reference/ft_databrowser)  
'sequential' 'allblack' 'labelcharx' (x = xth character in label), 'chantype' or vector with length(data/hdr.label) defining groups (default = 'sequential')

**cfg.colormap** - [ft_spike_plot_isireturn](/reference/ft_spike_plot_isireturn)  
N-by-3 colormap (see COLORMAP). Default = hot(256);

**cfg.colormap** - [ft_spike_plot_jpsth](/reference/ft_spike_plot_jpsth)  
N-by-3 colormap (see COLORMAP). or 'auto' (default,hot(256))

**cfg.colormap** - [ft_icabrowser](/reference/ft_icabrowser), [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotTFR](/reference/ft_singleplotTFR), [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
any sized colormap, see COLORMAP

**cfg.colormap** - [ft_sliceinterp](/reference/ft_sliceinterp)  
colormap for source overlay (default is jet(128))

**cfg.colorparam** - [ft_topoplotCC](/reference/ft_topoplotCC)  
string, parameter to be used to control the line color

**cfg.columns** - [ft_prepare_layout](/reference/ft_prepare_layout)  
number of columns (default is automatic)

**cfg.comment** - [ft_topoplotER](/reference/ft_topoplotER)  
'no', 'auto' or 'xlim' (default = 'auto') 'auto': date, xparam and zparam limits are printed 'xlim': only xparam limits are printed

**cfg.comment** - [ft_topoplotTFR](/reference/ft_topoplotTFR)  
'no', 'auto' or 'xlim' (default = 'auto') 'auto': date, xparam, yparam and parameter limits are printed 'xlim': only xparam limits are printed 'ylim': only yparam limits are printed

**cfg.comment** - [ft_annotate](/reference/ft_annotate)  
string

**cfg.comment** - [ft_topoplotIC](/reference/ft_topoplotIC)  
string 'no' 'auto' or 'xlim' (default = 'auto') 'auto': date, xparam and zparam limits are printed 'xlim': only xparam limits are printed

**cfg.comment** - [ft_multiplotER](/reference/ft_multiplotER), [ft_multiplotTFR](/reference/ft_multiplotTFR)  
string of text (default = date + limits) Add 'comment' to graph (according to COMNT in the layout)

**cfg.commentpos** - [ft_topoplotIC](/reference/ft_topoplotIC)  
string or two numbers, position of comment (default 'leftbottom') 'lefttop' 'leftbottom' 'middletop' 'middlebottom' 'righttop' 'rightbottom' 'title' to place comment as title 'layout' to place comment as specified for COMNT in layout [x y] coordinates

**cfg.commentpos** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
string or two numbers, position of the comment (default = 'leftbottom') 'lefttop' 'leftbottom' 'middletop' 'middlebottom' 'righttop' 'rightbottom' 'title' to place comment as title 'layout' to place comment as specified for COMNT in layout [x y] coordinates

**cfg.complex** - [ft_connectivityanalysis](/reference/ft_connectivityanalysis)  
'abs' (default), 'angle', 'complex', 'imag', 'real', '-logabs', support for method 'coh', 'csd', 'plv'

**cfg.component** - [ft_dipolefitting](/reference/ft_dipolefitting)  
array with numbers (can be empty -> all)

**cfg.component** - [ft_topoplotIC](/reference/ft_topoplotIC)  
field that contains the independent component(s) to be plotted as color

**cfg.component** - [ft_rejectcomponent](/reference/ft_rejectcomponent)  
list of components to remove, e.g. [1 4 7] or see FT_CHANNELSELECTION

**cfg.compscale** - [ft_databrowser](/reference/ft_databrowser)  
string, 'global' or 'local', defines whether the colormap for the topographic scaling is applied per topography or on all visualized components (default 'global')

**cfg.conductivity** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel), [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  


**cfg.conductivity** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
a number or a vector containing the conductivities of the compartments

**cfg.conductivity** - [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity), [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity)  
conductivity of the skin (default = 0.33 S/m)

**cfg.confound** - [ft_regressconfound](/reference/ft_regressconfound)  
matrix, [Ntrials X Nconfounds], may not contain NaNs

**cfg.continuous** - [ft_artifact_clip](/reference/ft_artifact_clip), [ft_artifact_ecg](/reference/ft_artifact_ecg), [ft_artifact_eog](/reference/ft_artifact_eog), [ft_artifact_jump](/reference/ft_artifact_jump), [ft_artifact_muscle](/reference/ft_artifact_muscle), [ft_artifact_threshold](/reference/ft_artifact_threshold)  
'yes' or 'no' whether the file contains continuous data

**cfg.continuous** - [ft_artifact_tms](/reference/ft_artifact_tms), [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'yes' or 'no' whether the file contains continuous data (default = 'yes')

**cfg.continuous** - [ft_preprocessing](/reference/ft_preprocessing)  
'yes' or 'no' whether the file contains continuous data (default is determined automatic)

**cfg.continuous** - [ft_databrowser](/reference/ft_databrowser)  
'yes' or 'no', whether the data should be interpreted as continuous or trial-based

**cfg.coordsys** - [ft_volumerealign](/reference/ft_volumerealign)  
string specifying the origin and the axes of the coordinate system. Supported coordinate systems are 'ctf', '4d', 'bti', 'yokogawa', 'asa', 'itab', 'neuromag', 'acpc', and 'paxinos'. See http://tinyurl.com/ojkuhqz

**cfg.coordsys** - [ft_preprocessing](/reference/ft_preprocessing)  
string, 'head' or 'dewar' (default = 'head')

**cfg.coordsys** - [ft_meshrealign](/reference/ft_meshrealign)  
string, can be 'ctf', 'neuromag', '4d', 'bti', 'itab'

**cfg.correctMotion** - [ft_omri_pipeline](/reference/ft_omri_pipeline), [ft_omri_pipeline_nuisance](/reference/ft_omri_pipeline_nuisance)  
	 = flag indicating whether to correct motion artifacts (default = 1 = yes)

**cfg.correctSliceTime** - [ft_omri_pipeline](/reference/ft_omri_pipeline), [ft_omri_pipeline_nuisance](/reference/ft_omri_pipeline_nuisance)  
flag indicating whether to correct slice timing (default = 1 = yes)

**cfg.correctm** - [ft_statistics_analytic](/reference/ft_statistics_analytic)  
string, apply multiple-comparison correction, 'no', 'bonferroni', 'holm', 'hochberg', 'fdr' (default = 'no')

**cfg.correctm** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
string, apply multiple-comparison correction, 'no', 'max', cluster', 'bonferroni', 'holm', 'hochberg', 'fdr' (default = 'no')

**cfg.correcttail** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
string, correct p-values or alpha-values when doing a two-sided test, 'alpha','prob' or 'no' (default = 'no')

**cfg.coupling** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
nxn matrix, specifying coupling strength, rows causing column

**cfg.covariance** - [ft_timelockanalysis](/reference/ft_timelockanalysis)  
'no' or 'yes' (default = 'no')

**cfg.covariancewindow** - [ft_timelockanalysis](/reference/ft_timelockanalysis)  
[begin end] in seconds, or 'all', 'minperiod', 'maxperiod', 'prestim', 'poststim' (default = 'all')

**cfg.covmat** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
covariance matrix between the signals

**cfg.crosshair** - [ft_sourceplot](/reference/ft_sourceplot)  
'yes' or 'no' (default = 'yes')

**cfg.csp.classlabels** - [ft_componentanalysis](/reference/ft_componentanalysis)  
vector that assigns a trial to class 1 or 2.

**cfg.csp.numfilters** - [ft_componentanalysis](/reference/ft_componentanalysis)  
the number of spatial filters to use (default: 6).

**cfg.cutoff** - [ft_realtime_downsample](/reference/ft_realtime_downsample)  
double, cutoff frequency of lowpass filter (default = 0.8*Nyquist-freq.)

**cfg.cvar** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
number or list with indices, control variable(s)

## D 

**cfg.datafile** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_average](/reference/ft_realtime_average), [ft_realtime_classification](/reference/ft_realtime_classification), [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer), [ft_realtime_fmriviewer](/reference/ft_realtime_fmriviewer), [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect), [ft_realtime_oddball](/reference/ft_realtime_oddball), [ft_realtime_ouunpod](/reference/ft_realtime_ouunpod), [ft_realtime_powerestimate](/reference/ft_realtime_powerestimate), [ft_realtime_selectiveaverage](/reference/ft_realtime_selectiveaverage), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer), [ft_realtime_synchronous](/reference/ft_realtime_synchronous), [ft_realtime_topography](/reference/ft_realtime_topography)  
string

**cfg.datafile** - [ft_artifact_clip](/reference/ft_artifact_clip), [ft_artifact_ecg](/reference/ft_artifact_ecg), [ft_artifact_eog](/reference/ft_artifact_eog), [ft_artifact_jump](/reference/ft_artifact_jump), [ft_artifact_muscle](/reference/ft_artifact_muscle), [ft_artifact_threshold](/reference/ft_artifact_threshold), [ft_artifact_tms](/reference/ft_artifact_tms), [ft_artifact_zvalue](/reference/ft_artifact_zvalue), [ft_databrowser](/reference/ft_databrowser), [ft_definetrial](/reference/ft_definetrial), [ft_preprocessing](/reference/ft_preprocessing)  
string with the filename

**cfg.dataformat** - [ft_artifact_clip](/reference/ft_artifact_clip), [ft_artifact_ecg](/reference/ft_artifact_ecg), [ft_artifact_eog](/reference/ft_artifact_eog), [ft_artifact_jump](/reference/ft_artifact_jump), [ft_artifact_muscle](/reference/ft_artifact_muscle), [ft_artifact_threshold](/reference/ft_artifact_threshold), [ft_artifact_tms](/reference/ft_artifact_tms), [ft_artifact_zvalue](/reference/ft_artifact_zvalue), [ft_definetrial](/reference/ft_definetrial)  


**cfg.dataformat** - [ft_spikedetection](/reference/ft_spikedetection)  
string with the output dataset format, see FT_WRITE_FCDC_SPIKE

**cfg.dataformat** - [ft_spikedownsample](/reference/ft_spikedownsample)  
string with the output dataset format, see WRITE_DATA

**cfg.dataformat** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_average](/reference/ft_realtime_average), [ft_realtime_classification](/reference/ft_realtime_classification), [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer), [ft_realtime_fmriviewer](/reference/ft_realtime_fmriviewer), [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect), [ft_realtime_oddball](/reference/ft_realtime_oddball), [ft_realtime_ouunpod](/reference/ft_realtime_ouunpod), [ft_realtime_powerestimate](/reference/ft_realtime_powerestimate), [ft_realtime_selectiveaverage](/reference/ft_realtime_selectiveaverage), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer), [ft_realtime_synchronous](/reference/ft_realtime_synchronous), [ft_realtime_topography](/reference/ft_realtime_topography)  
string, default is determined automatic

**cfg.datahdr** - [ft_audiovideobrowser](/reference/ft_audiovideobrowser)  
header structure of the EEG/MEG data, see FT_READ_HEADER

**cfg.dataset** - [ft_realtime_topography](/reference/ft_realtime_topography)  
'PW02_ingnie_20061212_01.ds';

**cfg.dataset** - [ft_realtime_classification](/reference/ft_realtime_classification)  
'Subject01.ds';

**cfg.dataset** - [ft_qualitycheck](/reference/ft_qualitycheck)  
a string (e.g. 'dataset.ds')

**cfg.dataset** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_average](/reference/ft_realtime_average), [ft_realtime_classification](/reference/ft_realtime_classification), [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer), [ft_realtime_fmriviewer](/reference/ft_realtime_fmriviewer), [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect), [ft_realtime_oddball](/reference/ft_realtime_oddball), [ft_realtime_ouunpod](/reference/ft_realtime_ouunpod), [ft_realtime_powerestimate](/reference/ft_realtime_powerestimate), [ft_realtime_selectiveaverage](/reference/ft_realtime_selectiveaverage), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer), [ft_realtime_synchronous](/reference/ft_realtime_synchronous), [ft_realtime_topography](/reference/ft_realtime_topography)  
string

**cfg.dataset** - [ft_artifact_clip](/reference/ft_artifact_clip), [ft_artifact_ecg](/reference/ft_artifact_ecg), [ft_artifact_eog](/reference/ft_artifact_eog), [ft_artifact_jump](/reference/ft_artifact_jump), [ft_artifact_muscle](/reference/ft_artifact_muscle), [ft_artifact_threshold](/reference/ft_artifact_threshold), [ft_artifact_tms](/reference/ft_artifact_tms), [ft_artifact_zvalue](/reference/ft_artifact_zvalue), [ft_databrowser](/reference/ft_databrowser), [ft_definetrial](/reference/ft_definetrial), [ft_headmovement](/reference/ft_headmovement), [ft_preprocessing](/reference/ft_preprocessing)  
string with the filename

**cfg.dataset** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
string with the input dataset

**cfg.dataset** - [ft_spikefixdmafile](/reference/ft_spikefixdmafile), [ft_spikesplitting](/reference/ft_spikesplitting)  
string with the name of the DMA log file

**cfg.dataset** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
string, name or location of a dataset/buffer (default = 'buffer://odin:1972')

**cfg.datatype** - [ft_volumewrite](/reference/ft_volumewrite)  
'bit1', 'uint8', 'int16', 'int32', 'float' or 'double'

**cfg.debias** - [ft_spike_xcorr](/reference/ft_spike_xcorr)  
'yes' (default) or 'no'. If 'yes', we scale the cross-correlogram by M/(M-abs(lags)), where M = 2*N -1 with N the length of the data segment.

**cfg.debug** - [ft_realtime_pooraudioproxy](/reference/ft_realtime_pooraudioproxy)  
show sample time and clock time (default = 'yes')

**cfg.decimate** - [ft_realtime_jaga16proxy](/reference/ft_realtime_jaga16proxy)  
integer number (default = 1)

**cfg.decimation** - [ft_realtime_downsample](/reference/ft_realtime_downsample)  
integer, downsampling factor (default = 1, no downsampling)

**cfg.deformweight** - [ft_electroderealign](/reference/ft_electroderealign)  
number (default: 1), weight of deformation relative to shift energy cost (lower increases grid flexibility)

**cfg.degree** - [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity)  
degree of legendre polynomials (default for <=32 electrodes = 9, <=64 electrodes = 14, <=128 electrodes = 20, else = 32

**cfg.delay** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
delay vector between the signals in samples

**cfg.delay** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
matrix, [nsignal x number of unobserved signals] specifying the time shift (in samples) between the unobserved signals and the observed signals

**cfg.delay** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
nxn matrix, specifying the delay, in seconds, from one signal's spectral component to the other signal, rows causing column

**cfg.delaystep** - [ft_nonlinearassociation](/reference/ft_nonlinearassociation)  
2/cfg.fsample

**cfg.demean** - [ft_preprocessing](/reference/ft_preprocessing), [ft_resampledata](/reference/ft_resampledata)  
'no' or 'yes', whether to apply baseline correction (default = 'no')

**cfg.demean** - [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer)  
'no' or 'yes', whether to apply baseline correction (default = 'yes')

**cfg.demean** - [ft_componentanalysis](/reference/ft_componentanalysis), [ft_rejectcomponent](/reference/ft_rejectcomponent)  
'no' or 'yes', whether to demean the input data (default = 'yes')

**cfg.demean** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
'yes' (default) or 'no' explicit removal of DC-offset

**cfg.demean** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation), [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
'yes' (or 'no')

**cfg.demean** - [ft_combineplanar](/reference/ft_combineplanar)  
'yes' or 'no' (default = 'no')

**cfg.demean** - [ft_channelnormalise](/reference/ft_channelnormalise)  
'yes' or 'no' (or boolean value) (default = 'yes')

**cfg.demean** - [ft_realtime_topography](/reference/ft_realtime_topography)  
'yes';

**cfg.demeandata** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
string, 'yes' or 'no', whether or not to make dependent variable zero mean prior to the regression (default = 'no')

**cfg.demeanrefdata** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
string, 'yes' or 'no', whether or not to make reference data zero mean prior to the regression (default = 'no')

**cfg.density** - [ft_spike_plot_isireturn](/reference/ft_spike_plot_isireturn)  
'yes' or 'no', if 'yes', we will use color shading on top of the individual datapoints to indicate the density.

**cfg.derivative** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or 'yes', computes the first order derivative of the data (default = 'no')

**cfg.design** - [ft_freqstatistics](/reference/ft_freqstatistics)  
Nxnumobservations: design matrix (for examples/advice, please see the Fieldtrip wiki, especially cluster-permutation tutorial and the 'walkthrough' design-matrix section)

**cfg.detrend** - [ft_resampledata](/reference/ft_resampledata)  
'no' or 'yes', detrend the data prior to resampling (no default specified, see below)

**cfg.detrend** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or 'yes', remove linear trend from the data (done per trial) (default = 'no')

**cfg.dewar** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
filename or mesh, description of the dewar shape (default is automatic)

**cfg.dftbandwidth** - [ft_preprocessing](/reference/ft_preprocessing)  
bandwidth of line noise frequencies, applies to spectrum interpolation, in Hz (default = [1 2 3])

**cfg.dftfilter** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or 'yes' line noise removal using discrete fourier transform (default = 'no')

**cfg.dftfreq** - [ft_preprocessing](/reference/ft_preprocessing)  
line noise frequencies in Hz for DFT filter (default = [50 100 150])

**cfg.dftneighbourwidth** - [ft_preprocessing](/reference/ft_preprocessing)  
bandwidth of frequencies neighbouring line noise frequencies, applies to spectrum interpolation, in Hz (default = [2 2 2])

**cfg.dftreplace** - [ft_preprocessing](/reference/ft_preprocessing)  
'zero' or 'neighbour', method used to reduce line noise, 'zero' implies DFT filter, 'neighbour' implies spectrum interpolation (default = 'zero')

**cfg.dim** - [ft_volumereslice](/reference/ft_volumereslice)  
[nx ny nz], size of the volume in each direction

**cfg.dim** - [ft_sliceinterp](/reference/ft_sliceinterp)  
integer value, default is 3 (dimension to slice)

**cfg.dip.amplitude** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
per dipole

**cfg.dip.frequency** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
in Hz

**cfg.dip.mom** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
[Qx Qy Qz] (size 3xN)

**cfg.dip.phase** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
in radians

**cfg.dip.pos** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
[Rx Ry Rz] (size Nx3)

**cfg.dip.pos** - [ft_dipolefitting](/reference/ft_dipolefitting)  
initial dipole position, matrix of Ndipoles x 3

**cfg.dip.signal** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  


**cfg.dipfit.display** - [ft_dipolefitting](/reference/ft_dipolefitting)  
level of display, can be 'off', 'iter', 'notify' or 'final' (default = 'iter')

**cfg.dipfit.maxiter** - [ft_dipolefitting](/reference/ft_dipolefitting)  
maximum number of function evaluations allowed (default depends on the optimfun)

**cfg.dipfit.optimfun** - [ft_dipolefitting](/reference/ft_dipolefitting)  
function to use, can be 'fminsearch' or 'fminunc' (default is determined automatic)

**cfg.dipoleunit** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
units for dipole amplitude (default nA*m)

**cfg.direction** - [ft_appendlayout](/reference/ft_appendlayout)  
string, 'horizontal' or 'vertical' (default = 'horizontal')

**cfg.direction** - [ft_prepare_layout](/reference/ft_prepare_layout)  
string, can be any of 'LR', 'RL' (for horizontal), 'TB', 'BT' (for vertical)

**cfg.direction** - [ft_prepare_layout](/reference/ft_prepare_layout)  
string, can be any of 'LRTB', 'RLTB', 'LRBT', 'RLBT', 'TBLR', 'TBRL', 'BTLR', 'BTRL' (default = 'LRTB')

**cfg.directionality** - [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotER](/reference/ft_singleplotER), [ft_singleplotTFR](/reference/ft_singleplotTFR), [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
'', 'inflow' or 'outflow' specifies for connectivity measures whether the inflow into a node, or the outflow from a node is plotted. The (default) behavior of this option depends on the dimor of the input data (see below).

**cfg.directionality** - [ft_multiplotER](/reference/ft_multiplotER)  
'', 'inflow' or 'outflow' specifies for connectivity measures whether the inflow into a node, or the outflow from a node is plotted. The (default) behavior of this option depends on the dimord of the input data (see below).

**cfg.distance** - [ft_appendlayout](/reference/ft_appendlayout)  
number, distance between layouts (default is automatic)

**cfg.distmat** - [ft_sourceplot](/reference/ft_sourceplot)  
precomputed distance matrix (default = [])

**cfg.downsample** - [ft_sourceplot](/reference/ft_sourceplot)  
downsampling for resolution reduction, integer value (default = 1) (orig: from surface)

**cfg.downsample** - [ft_sourceinterpolate](/reference/ft_sourceinterpolate), [ft_volumedownsample](/reference/ft_volumedownsample), [ft_volumenormalise](/reference/ft_volumenormalise), [ft_volumereslice](/reference/ft_volumereslice), [ft_volumewrite](/reference/ft_volumewrite)  
integer number (default = 1, i.e. no downsampling)

**cfg.downsample** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
integer number (default = 1, i.e. no downsampling), see FT_VOLUMEDOWNSAMPLE

**cfg.downsample** - [ft_volumesegment](/reference/ft_volumesegment)  
integer, amount of downsampling before segmentation (default = 1; i.e., no downsampling)

**cfg.downscale** - [ft_spikesplitting](/reference/ft_spikesplitting)  
single number or vector (for each channel), corresponding to the number of bits removed from the LSB side (default = 0)

**cfg.dpf** - [ft_nirs_prepare_ODtransformation](/reference/ft_nirs_prepare_ODtransformation), [ft_nirs_transform_ODs](/reference/ft_nirs_transform_ODs)  
scalar, differential path length factor

**cfg.dpffile** - [ft_nirs_prepare_ODtransformation](/reference/ft_nirs_prepare_ODtransformation), [ft_nirs_transform_ODs](/reference/ft_nirs_transform_ODs)  
string, location to a lookup table for the relation between participant age and DPF

**cfg.dss.denf.function** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.dss.denf.params** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.dssp** - [ft_denoise_dssp](/reference/ft_denoise_dssp)  
structure with parameters that determine the behavior of the algorithm

**cfg.dssp.n_in** - [ft_denoise_dssp](/reference/ft_denoise_dssp)  
'all', or scalar. Number of dimensions of the subspace describing the field inside the ROI.

**cfg.dssp.n_intersect** - [ft_denoise_dssp](/reference/ft_denoise_dssp)  
scalar (default = 0.9). Number of dimensions (if value is an integer>=1), or threshold for the included eigenvalues (if value<1), determining the dimensionality of the intersection.

**cfg.dssp.n_out** - [ft_denoise_dssp](/reference/ft_denoise_dssp)  
'all', or scalar. Number of dimensions of the subspace describing the field outside the ROI.

**cfg.dssp.n_space** - [ft_denoise_dssp](/reference/ft_denoise_dssp)  
'all', or scalar. Number of dimensions for the initial spatial projection.

**cfg.dt** - [ft_spike_plot_isireturn](/reference/ft_spike_plot_isireturn)  
resolution of the 2-D histogram, or of the kernel plot in seconds. Since we have to smooth for a finite number of values, cfg.dt determines the resolution of our smooth density plot.

**cfg.duration** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
scalar, trial length in seconds (default = 4.56)

## E 

**cfg.ecgscale** - [ft_databrowser](/reference/ft_databrowser), [ft_rejectvisual](/reference/ft_rejectvisual)  
number, scaling to apply to the ECG channels prior to display

**cfg.edgecolor** - [ft_sourceplot](/reference/ft_sourceplot)  
[r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r'

**cfg.eegscale** - [ft_databrowser](/reference/ft_databrowser), [ft_rejectvisual](/reference/ft_rejectvisual)  
number, scaling to apply to the EEG channels prior to display

**cfg.elec** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  


**cfg.elec** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
(required) structure with electrode positions or filename, see FT_READ_SENS

**cfg.elec** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
struct containing previously placed electrodes (this overwrites cfg.channel)

**cfg.elec** - [ft_channelrepair](/reference/ft_channelrepair), [ft_databrowser](/reference/ft_databrowser), [ft_dipolefitting](/reference/ft_dipolefitting), [ft_dipolesimulation](/reference/ft_dipolesimulation), [ft_electroderealign](/reference/ft_electroderealign), [ft_layoutplot](/reference/ft_layoutplot), [ft_neighbourplot](/reference/ft_neighbourplot), [ft_prepare_layout](/reference/ft_prepare_layout), [ft_prepare_leadfield](/reference/ft_prepare_leadfield), [ft_prepare_neighbours](/reference/ft_prepare_neighbours), [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel), [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
structure with electrode positions or filename, see FT_READ_SENS

**cfg.emgscale** - [ft_databrowser](/reference/ft_databrowser), [ft_rejectvisual](/reference/ft_rejectvisual)  
number, scaling to apply to the EMG channels prior to display

**cfg.ems** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
'no' (default) or 'yes' explicit removal ensemble mean

**cfg.enableedit** - [ft_neighbourplot](/reference/ft_neighbourplot)  
string, 'yes' or 'no', allows you to interactively add or remove edges between vertices (default = 'no')

**cfg.endsample** - [ft_redefinetrial](/reference/ft_redefinetrial)  
single number or Nx1 vector, expressed in samples relative to the start of the input trial

**cfg.envelopewindow** - [ft_heartrate](/reference/ft_heartrate), [ft_respiration](/reference/ft_respiration)  
scalar, time in seconds

**cfg.eogscale** - [ft_databrowser](/reference/ft_databrowser), [ft_rejectvisual](/reference/ft_rejectvisual)  
number, scaling to apply to the EOG channels prior to display

**cfg.equalbinavg** - [ft_stratify](/reference/ft_stratify)  
'yes'

**cfg.errorbars** - [ft_spike_plot_psth](/reference/ft_spike_plot_psth)  
'no', 'std', 'sem' (default), 'conf95%' (requires statistic toolbox, according to student-T distribution), 'var'

**cfg.errorbars** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster)  
'no', 'std', 'sem' (default), 'conf95%','var'

**cfg.eta** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'yes' or 'no' (default = 'no')

**cfg.eventfile** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_average](/reference/ft_realtime_average), [ft_realtime_classification](/reference/ft_realtime_classification), [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer), [ft_realtime_fmriviewer](/reference/ft_realtime_fmriviewer), [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect), [ft_realtime_oddball](/reference/ft_realtime_oddball), [ft_realtime_ouunpod](/reference/ft_realtime_ouunpod), [ft_realtime_powerestimate](/reference/ft_realtime_powerestimate), [ft_realtime_selectiveaverage](/reference/ft_realtime_selectiveaverage), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer), [ft_realtime_synchronous](/reference/ft_realtime_synchronous), [ft_realtime_topography](/reference/ft_realtime_topography)  
string

**cfg.eventformat** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_average](/reference/ft_realtime_average), [ft_realtime_classification](/reference/ft_realtime_classification), [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer), [ft_realtime_fmriviewer](/reference/ft_realtime_fmriviewer), [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect), [ft_realtime_oddball](/reference/ft_realtime_oddball), [ft_realtime_ouunpod](/reference/ft_realtime_ouunpod), [ft_realtime_powerestimate](/reference/ft_realtime_powerestimate), [ft_realtime_selectiveaverage](/reference/ft_realtime_selectiveaverage), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer), [ft_realtime_synchronous](/reference/ft_realtime_synchronous), [ft_realtime_topography](/reference/ft_realtime_topography)  
string, default is determined automatic

**cfg.eventtype** - [ft_recodeevent](/reference/ft_recodeevent)  
empty, 'string' or cell-array with multiple strings

**cfg.eventvalue** - [ft_recodeevent](/reference/ft_recodeevent)  
empty or a list of event values (can be numeric or string)

**cfg.export.dataformat** - [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder)  
string describing the output file format, see FT_WRITE_DATA

**cfg.export.dataset** - [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder)  
string with the output file name

## F 

**cfg.facecolor** - [ft_sourceplot](/reference/ft_sourceplot)  
[r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of faces

**cfg.fastica.a1** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.a2** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.approach** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.dewhiteMat** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.displayInterval** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.displayMode** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.epsilon** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.finetune** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.firstEig** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.g** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.initGuess** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.interactivePCA** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.lastEig** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.maxFinetune** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.maxNumIterations** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.mu** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.numOfIC** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.only** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.pcaD** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.pcaE** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.sampleSize** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.stabilization** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.verbose** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.whiteMat** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.fastica.whiteSig** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.feedback** - [ft_megplanar](/reference/ft_megplanar)  


**cfg.feedback** - [ft_defacevolume](/reference/ft_defacevolume)  
'no' or 'yes', whether to provide graphical feedback (default = 'no')

**cfg.feedback** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'no', 'text' (default), 'textbar', 'gui'

**cfg.feedback** - [ft_spiketriggeredaverage](/reference/ft_spiketriggeredaverage), [ft_spiketriggeredinterpolation](/reference/ft_spiketriggeredinterpolation), [ft_spiketriggeredspectrum_fft](/reference/ft_spiketriggeredspectrum_fft)  
'no', 'text', 'textbar', 'gui' (default = 'no')

**cfg.feedback** - [ft_componentanalysis](/reference/ft_componentanalysis), [ft_resampledata](/reference/ft_resampledata), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no', 'text', 'textbar', 'gui' (default = 'text')

**cfg.feedback** - [ft_spikesorting](/reference/ft_spikesorting)  
'no', 'text', 'textbar', 'gui' (default = 'textbar')

**cfg.feedback** - [ft_freqanalysis_mvar](/reference/ft_freqanalysis_mvar)  
'none', or any of the methods supported by FT_PROGRESS, for providing feedback to the user in the command window.

**cfg.feedback** - [ft_electrodermalactivity](/reference/ft_electrodermalactivity), [ft_heartrate](/reference/ft_heartrate), [ft_respiration](/reference/ft_respiration)  
'yes' or 'no'

**cfg.feedback** - [ft_electroderealign](/reference/ft_electroderealign), [ft_prepare_neighbours](/reference/ft_prepare_neighbours), [ft_realtime_brainampproxy](/reference/ft_realtime_brainampproxy), [ft_realtime_jaga16proxy](/reference/ft_realtime_jaga16proxy), [ft_realtime_micromedproxy](/reference/ft_realtime_micromedproxy), [ft_realtime_modeegproxy](/reference/ft_realtime_modeegproxy)  
'yes' or 'no' (default = 'no')

**cfg.feedback** - [ft_electroderealign](/reference/ft_electroderealign)  
'yes' or 'no' (default), feedback of the iteration procedure

**cfg.feedback** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
(optional)

**cfg.feedback** - [ft_topoplotCC](/reference/ft_topoplotCC)  
string (default = 'textbar')

**cfg.feedback** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
string, 'gui', 'text', 'textbar' or 'no' (default = 'text')

**cfg.feedback** - [ft_statistics_stats](/reference/ft_statistics_stats)  
string, 'gui', 'text', 'textbar' or 'no' (default = 'textbar')

**cfg.feedback** - [ft_analysispipeline](/reference/ft_analysispipeline)  
string, 'no', 'text', 'gui' or 'yes', whether text and/or graphical feedback should be presented (default = 'yes')

**cfg.feedback** - [ft_interpolatenan](/reference/ft_interpolatenan), [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity)  
string, 'no', 'text', 'textbar', 'gui' (default = 'text')

**cfg.feedback** - [ft_spikesplitting](/reference/ft_spikesplitting)  
string, (default = 'textbar')

**cfg.feedback** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
string, can be 'yes' or 'no' for detailled feedback (default = 'yes')

**cfg.feedback** - [ft_connectivityanalysis](/reference/ft_connectivityanalysis)  
string, specifying the feedback presented to the user. Default is 'none'. See FT_PROGRESS

**cfg.fiducial** - [ft_electroderealign](/reference/ft_electroderealign)  
cell-array with the name of three fiducials used for realigning (default = {'nasion', 'lpa', 'rpa'})

**cfg.fiducial.ac** - [ft_volumerealign](/reference/ft_volumerealign)  
[i j k], position of anterior commissure

**cfg.fiducial.ini** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
1x3 vector with coordinates

**cfg.fiducial.lpa** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
1x3 vector with coordinates

**cfg.fiducial.lpa** - [ft_volumerealign](/reference/ft_volumerealign)  
[i j k], position of LPA

**cfg.fiducial.lpa** - [ft_volumewrite](/reference/ft_volumewrite)  
[x y z] position of LPA

**cfg.fiducial.lpa** - [ft_meshrealign](/reference/ft_meshrealign)  
[x y z], position of LPA

**cfg.fiducial.nas** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
1x3 vector with coordinates

**cfg.fiducial.nas** - [ft_volumerealign](/reference/ft_volumerealign)  
[i j k], position of nasion

**cfg.fiducial.nas** - [ft_volumewrite](/reference/ft_volumewrite)  
[x y z] position of nasion

**cfg.fiducial.nas** - [ft_meshrealign](/reference/ft_meshrealign)  
[x y z], position of nasion

**cfg.fiducial.pc** - [ft_volumerealign](/reference/ft_volumerealign)  
[i j k], position of posterior commissure

**cfg.fiducial.rpa** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
1x3 vector with coordinates

**cfg.fiducial.rpa** - [ft_volumerealign](/reference/ft_volumerealign)  
[i j k], position of RPA

**cfg.fiducial.rpa** - [ft_volumewrite](/reference/ft_volumewrite)  
[x y z] position of RPA

**cfg.fiducial.rpa** - [ft_meshrealign](/reference/ft_meshrealign)  
[x y z], position of RPA

**cfg.fiducial.xzpoint** - [ft_volumerealign](/reference/ft_volumerealign)  
[i j k], point on the midsagittal-plane with a positive Z-coordinate, i.e. an interhemispheric point above ac and pc

**cfg.fiducial.zpoint** - [ft_volumerealign](/reference/ft_volumerealign)  
[i j k], a point on the positive z-axis. This is an optional 'fiducial', and can be used to determine whether the input voxel coordinate axes are left-handed (i.e. flipped in one of the dimensions). If this additional point is specified, and the voxel coordinate axes are left handed, the volume is flipped to yield right handed voxel axes.

**cfg.figurename** - [ft_sourceplot](/reference/ft_sourceplot)  
string, title of the figure window

**cfg.filename** - [ft_volumewrite](/reference/ft_volumewrite)  
filename without the extension

**cfg.filename** - [ft_analysispipeline](/reference/ft_analysispipeline), [ft_sourcewrite](/reference/ft_sourcewrite)  
string, filename without the extension

**cfg.filename** - [ft_realtime_modeegproxy](/reference/ft_realtime_modeegproxy)  
string, name of the serial port (default = '/dev/tty.FireFly-B106-SPP')

**cfg.filetype** - [ft_volumewrite](/reference/ft_volumewrite)  
'analyze', 'nifti', 'nifti_img', 'analyze_spm', 'mgz', 'vmp' or 'vmr'

**cfg.filetype** - [ft_analysispipeline](/reference/ft_analysispipeline)  
string, can be 'matlab', 'html' or 'dot'

**cfg.filetype** - [ft_sourcewrite](/reference/ft_sourcewrite)  
string, can be 'nifti', 'gifti' or 'cifti' (default is automatic)

**cfg.fitind** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
(optional)

**cfg.fixedori** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'within_trials' or 'over_trials' (default = 'over_trials')

**cfg.flank.mindist** - [ft_spikedetection](/reference/ft_spikedetection)  
mininum distance in samples between detected peaks

**cfg.flank.offset** - [ft_spikedetection](/reference/ft_spikedetection)  
number of samples before peak

**cfg.flank.value** - [ft_spikedetection](/reference/ft_spikedetection)  
positive or negative threshold

**cfg.flank.ztransform** - [ft_spikedetection](/reference/ft_spikedetection)  
'yes' or 'no'

**cfg.flipdim** - [ft_sliceinterp](/reference/ft_sliceinterp)  
flip data along the sliced dimension, 'yes' or 'no' (default = 'no')

**cfg.foi** - [ft_topoplotCC](/reference/ft_topoplotCC)  
the frequency of interest which is to be plotted (default is the first frequency bin)

**cfg.foi** - [ft_freqanalysis](/reference/ft_freqanalysis)  
vector 1 x numfoi, frequencies of interest

**cfg.foi** - [ft_freqanalysis](/reference/ft_freqanalysis), [ft_freqanalysis](/reference/ft_freqanalysis)  
vector 1 x numfoi, frequencies of interest OR

**cfg.foi** - [ft_freqanalysis_mvar](/reference/ft_freqanalysis_mvar)  
vector with the frequencies at which the spectral quantities are estimated (in Hz). Default: 0:1:Nyquist

**cfg.foilim** - [ft_freqinterpolate](/reference/ft_freqinterpolate)  
Nx2 matrix with begin and end of each interval to be interpolated (default = [49 51; 99 101; 149 151])

**cfg.foilim** - [ft_realtime_powerestimate](/reference/ft_realtime_powerestimate)  
[Flow Fhigh] (default = [0 120])

**cfg.foilim** - [ft_realtime_ouunpod](/reference/ft_realtime_ouunpod)  
[Flow Fhigh] (default = [1 45])

**cfg.foilim** - [ft_freqanalysis](/reference/ft_freqanalysis), [ft_freqanalysis](/reference/ft_freqanalysis)  
[begin end], frequency band of interest

**cfg.foilim** - [ft_spiketriggeredspectrum_fft](/reference/ft_spiketriggeredspectrum_fft)  
[begin end], frequency band of interest (default = [0 150])

**cfg.foilim** - [ft_freqanalysis](/reference/ft_freqanalysis)  
[begin end], frequency band of interest OR

**cfg.foilim** - [ft_freqgrandaverage](/reference/ft_freqgrandaverage)  
[fmin fmax] or 'all', to specify a subset of frequencies (default = 'all')

**cfg.fontsize** - [ft_multiplotER](/reference/ft_multiplotER)  
font size of comment and labels (default = 8)

**cfg.fontsize** - [ft_multiplotTFR](/reference/ft_multiplotTFR)  
font size of comment and labels (if present) (default = 8)

**cfg.fontsize** - [ft_singleplotER](/reference/ft_singleplotER), [ft_singleplotTFR](/reference/ft_singleplotTFR)  
font size of title (default = 8)

**cfg.fontsize** - [ft_databrowser](/reference/ft_databrowser)  
number, fontsize inside the figure (default = 0.03)

**cfg.fontunits** - [ft_databrowser](/reference/ft_databrowser)  
string, can be 'normalized', 'points', 'pixels', 'inches' or 'centimeters' (default = 'normalized')

**cfg.fontweight** - [ft_multiplotTFR](/reference/ft_multiplotTFR)  
font weight of comment and labels (if present)

**cfg.format** - [ft_spikesplitting](/reference/ft_spikesplitting)  
'int16' or 'int32' (default = 'int32')

**cfg.framesfile** - [ft_movieplotTFR](/reference/ft_movieplotTFR)  
[] (optional), no file saved, or 'string', filename of saved frames.mat (default = []);

**cfg.framesfile** - [ft_movieplotER](/reference/ft_movieplotER)  
[], no file saved, or 'string', filename of saved frames.mat (default = []);

**cfg.framespersec** - [ft_movieplotER](/reference/ft_movieplotER), [ft_movieplotTFR](/reference/ft_movieplotTFR)  
number, frames per second (default = 5)

**cfg.freqhigh** - [ft_crossfrequencyanalysis](/reference/ft_crossfrequencyanalysis)  
scalar or vector, selection of frequencies for the high frequency data

**cfg.freqlow** - [ft_crossfrequencyanalysis](/reference/ft_crossfrequencyanalysis)  
scalar or vector, selection of frequencies for the low frequency data

**cfg.frequency** - [ft_freqstatistics](/reference/ft_freqstatistics)  
[begin end], can be 'all' (default = 'all')

**cfg.frequency** - [ft_freqdescriptives](/reference/ft_freqdescriptives)  
[fmin fmax] or 'all', to specify a subset of frequencies (default = 'all')

**cfg.frequency** - [ft_sourceplot](/reference/ft_sourceplot)  
scalar or string, can be 'all', or [beg end], specify frequency range in Hz

**cfg.frequency** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
single number (in Hz)

**cfg.fsample** - [ft_nonlinearassociation](/reference/ft_nonlinearassociation)  
1200

**cfg.fsample** - [ft_spikedensity](/reference/ft_spikedensity)  
additional user input that can be used when input is a SPIKE structure, in that case a continuous representation is created using cfg.fsample (default = 1000)

**cfg.fsample** - [ft_realtime_pooraudioproxy](/reference/ft_realtime_pooraudioproxy)  
audio sampling frequency in Hz (default = 44100)

**cfg.fsample** - [ft_spikedownsample](/reference/ft_spikedownsample)  
desired sampling frequency in Hz (default = 1000)

**cfg.fsample** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
in Hz

**cfg.fsample** - [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
sampling frequency

**cfg.fsample** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
sampling frequency in Hz

**cfg.fsample** - [ft_spike_waveform](/reference/ft_spike_waveform)  
sampling frequency of waveform time-axis. Obligatory field.

**cfg.fsample** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
scalar, sampling frequency in Hz (default = 512)

**cfg.fsample** - [ft_freqsimulation](/reference/ft_freqsimulation)  
simulated sample frequency

**cfg.fsample** - [ft_timelocksimulation](/reference/ft_timelocksimulation)  
simulated sample frequency (default = 1000)

**cfg.fshome** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
'/path/to/freesurfer dir'; cortex_hull = ft_prepare_mesh(cfg);

**cfg.fshome** - [ft_electroderealign](/reference/ft_electroderealign)  
string, path to freesurfer

**cfg.fsl.costfun** - [ft_volumerealign](/reference/ft_volumerealign)  
string, specifying the cost-function used for coregistration

**cfg.fsl.dof** - [ft_volumerealign](/reference/ft_volumerealign)  
scalar, specifying the number of parameters for the affine transformation. 6 (rigid body), 7 (global rescale), 9 (traditional) or 12.

**cfg.fsl.interpmethod** - [ft_volumerealign](/reference/ft_volumerealign)  
string, specifying the interpolation method, can be 'trilinear', 'nearestneighbour', or 'sinc'

**cfg.fsl.path** - [ft_volumerealign](/reference/ft_volumerealign)  
string, specifying the path to fsl

**cfg.fsl.reslice** - [ft_volumerealign](/reference/ft_volumerealign)  
string, specifying whether the output image will be resliced conform the target image (default = 'yes')

**cfg.funcolorlim** - [ft_sourceplot](/reference/ft_sourceplot)  
color range of the functional data (default = 'auto') [min max] 'maxabs', from -max(abs(funparameter)) to +max(abs(funparameter)) 'zeromax', from 0 to max(funparameter) 'minzero', from min(funparameter) to 0 'auto', if funparameter values are all positive: 'zeromax', all negative: 'minzero', both possitive and negative: 'maxabs'

**cfg.funcolormap** - [ft_sourceplot](/reference/ft_sourceplot)  
colormap for functional data, see COLORMAP (default = 'auto') 'auto', depends structure funparameter, or on funcolorlim - funparameter: only positive values, or funcolorlim:'zeromax' -> 'hot' - funparameter: only negative values, or funcolorlim:'minzero' -> 'cool' - funparameter: both pos and neg values, or funcolorlim:'maxabs' -> 'default' - funcolorlim: [min max] if min & max pos-> 'hot', neg-> 'cool', both-> 'default'

**cfg.funparameter** - [ft_sliceinterp](/reference/ft_sliceinterp)  
string with the functional parameter of interest (default = 'source')

**cfg.funparameter** - [ft_sourceplot](/reference/ft_sourceplot)  
string, field in data with the functional parameter of interest (default = [])

**cfg.funparameter** - [ft_sourcemovie](/reference/ft_sourcemovie)  
string, functional parameter that is color coded (default = 'avg.pow')

## G 

**cfg.gaussvar** - [ft_spike_plot_isireturn](/reference/ft_spike_plot_isireturn), [ft_spike_plot_jpsth](/reference/ft_spike_plot_jpsth)  
variance (default = 1/16 of window length in sec).

**cfg.grad** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel), [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  


**cfg.grad** - [ft_channelrepair](/reference/ft_channelrepair), [ft_databrowser](/reference/ft_databrowser), [ft_dipolefitting](/reference/ft_dipolefitting), [ft_dipolesimulation](/reference/ft_dipolesimulation), [ft_layoutplot](/reference/ft_layoutplot), [ft_neighbourplot](/reference/ft_neighbourplot), [ft_prepare_layout](/reference/ft_prepare_layout), [ft_prepare_leadfield](/reference/ft_prepare_leadfield), [ft_prepare_neighbours](/reference/ft_prepare_neighbours), [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
structure with gradiometer definition or filename, see FT_READ_SENS

**cfg.gradient** - [ft_denoise_synthetic](/reference/ft_denoise_synthetic)  
'none', 'G1BR', 'G2BR' or 'G3BR' specifies the gradiometer type to which the data should be changed

**cfg.gradscale** - [ft_multiplotER](/reference/ft_multiplotER), [ft_multiplotTFR](/reference/ft_multiplotTFR)  
number, scaling to apply to the MEG gradiometer channels prior to display

**cfg.gradscale** - [ft_databrowser](/reference/ft_databrowser), [ft_rejectvisual](/reference/ft_rejectvisual)  
number, scaling to apply to the MEG gradiometer channels prior to display (in addition to the cfg.megscale factor)

**cfg.graphcolor** - [ft_multiplotER](/reference/ft_multiplotER)  
color(s) used for plotting the dataset(s) (default = 'brgkywrgbkywrgbkywrgbkyw') alternatively, colors can be specified as Nx3 matrix of RGB values

**cfg.graphcolor** - [ft_singleplotER](/reference/ft_singleplotER)  
color(s) used for plotting the dataset(s) (default = 'brgkywrgbkywrgbkywrgbkyw') alternatively, colors can be specified as nx3 matrix of rgb values

**cfg.grid.corner1** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
1x3 position of the upper left corner point

**cfg.grid.corner2** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
1x3 position of the upper right corner point

**cfg.grid.corner3** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
1x3 position of the lower left corner point

**cfg.grid.corner4** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
1x3 position of the lower right corner point

**cfg.gridscale** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
scaling grid size (default = 67) determines resolution of figure

**cfg.gridsearch** - [ft_dipolefitting](/reference/ft_dipolefitting)  
'yes' or 'no', perform global search for initial guess for the dipole parameters (default = 'yes')

**cfg.gwidth** - [ft_freqanalysis](/reference/ft_freqanalysis), [ft_freqanalysis](/reference/ft_freqanalysis)  
determines the length of the used wavelets in standard deviations of the implicit Gaussian kernel and should be choosen >= 3; (default = 3)

## H 

**cfg.hdr** - [ft_spike_maketrials](/reference/ft_spike_maketrials)  
struct, should be specified if cfg.trlunit = 'samples'. This should be specified as cfg.hdr = data.hdr where data.hdr contains the subfields data.hdr.Fs (sampling frequency of the LFP), data.hdr.FirstTimeStamp, and data.hdr.TimeStampPerSecond.

**cfg.headerfile** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_average](/reference/ft_realtime_average), [ft_realtime_classification](/reference/ft_realtime_classification), [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer), [ft_realtime_fmriviewer](/reference/ft_realtime_fmriviewer), [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect), [ft_realtime_oddball](/reference/ft_realtime_oddball), [ft_realtime_ouunpod](/reference/ft_realtime_ouunpod), [ft_realtime_powerestimate](/reference/ft_realtime_powerestimate), [ft_realtime_selectiveaverage](/reference/ft_realtime_selectiveaverage), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer), [ft_realtime_synchronous](/reference/ft_realtime_synchronous), [ft_realtime_topography](/reference/ft_realtime_topography)  
string

**cfg.headerfile** - [ft_artifact_clip](/reference/ft_artifact_clip), [ft_artifact_ecg](/reference/ft_artifact_ecg), [ft_artifact_eog](/reference/ft_artifact_eog), [ft_artifact_jump](/reference/ft_artifact_jump), [ft_artifact_muscle](/reference/ft_artifact_muscle), [ft_artifact_threshold](/reference/ft_artifact_threshold), [ft_artifact_tms](/reference/ft_artifact_tms), [ft_artifact_zvalue](/reference/ft_artifact_zvalue), [ft_databrowser](/reference/ft_databrowser), [ft_definetrial](/reference/ft_definetrial), [ft_preprocessing](/reference/ft_preprocessing)  
string with the filename

**cfg.headerformat** - [ft_artifact_clip](/reference/ft_artifact_clip), [ft_artifact_ecg](/reference/ft_artifact_ecg), [ft_artifact_eog](/reference/ft_artifact_eog), [ft_artifact_jump](/reference/ft_artifact_jump), [ft_artifact_muscle](/reference/ft_artifact_muscle), [ft_artifact_threshold](/reference/ft_artifact_threshold), [ft_artifact_tms](/reference/ft_artifact_tms), [ft_artifact_zvalue](/reference/ft_artifact_zvalue), [ft_definetrial](/reference/ft_definetrial)  


**cfg.headerformat** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_average](/reference/ft_realtime_average), [ft_realtime_classification](/reference/ft_realtime_classification), [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer), [ft_realtime_fmriviewer](/reference/ft_realtime_fmriviewer), [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect), [ft_realtime_oddball](/reference/ft_realtime_oddball), [ft_realtime_ouunpod](/reference/ft_realtime_ouunpod), [ft_realtime_powerestimate](/reference/ft_realtime_powerestimate), [ft_realtime_selectiveaverage](/reference/ft_realtime_selectiveaverage), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer), [ft_realtime_synchronous](/reference/ft_realtime_synchronous), [ft_realtime_topography](/reference/ft_realtime_topography)  
string, default is determined automatic

**cfg.headmodel** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
(required) string, filename of precomputed FEM leadfield

**cfg.headmodel** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
structure with volume conduction model or filename, see FT_PREPARE_HEADMODEL

**cfg.headmodel** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_dipolesimulation](/reference/ft_dipolesimulation), [ft_megplanar](/reference/ft_megplanar), [ft_prepare_leadfield](/reference/ft_prepare_leadfield), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
structure with volume conduction model, see FT_PREPARE_HEADMODEL

**cfg.headmodel** - [ft_megrealign](/reference/ft_megrealign)  
structure, see FT_PREPARE_HEADMODEL

**cfg.headmovement** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
string, name or location of the .pos file created by MaxFilter which describes the location of the head relative to the dewar

**cfg.headshape** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
'/path/to/surf/lh.pial';

**cfg.headshape** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
a filename containing headshape, a Nx3 matrix with surface points, or a structure with a single or multiple boundaries

**cfg.headshape** - [ft_electroderealign](/reference/ft_electroderealign), [ft_electroderealign](/reference/ft_electroderealign), [ft_megplanar](/reference/ft_megplanar), [ft_megrealign](/reference/ft_megrealign)  
a filename containing headshape, a structure containing a single triangulated boundary, or a Nx3 matrix with surface points

**cfg.headshape** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
a filename for the headshape, a structure containing a single surface, or a Nx3 matrix with headshape surface points (default = [])

**cfg.headshape** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
filename or mesh, description of the head shape recorded with the Structure Sensor

**cfg.headshape** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
sting, filename containing the pial surface computed by freesurfer recon-all

**cfg.headshape** - [ft_electroderealign](/reference/ft_electroderealign)  
string, filename containing subject headshape (e.g. <path to freesurfer/surf/lh.pial>)

**cfg.headshape** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
string, should be a *.fif file

**cfg.headshape** - [ft_prepare_layout](/reference/ft_prepare_layout)  
surface mesh (e.g. pial, head, etc) to be used for generating an outline, see FT_READ_HEADSHAPE for details

**cfg.headshape.headshape** - [ft_volumerealign](/reference/ft_volumerealign)  
string pointing to a file describing a headshape or a FieldTrip-structure describing a headshape, see FT_READ_HEADSHAPE

**cfg.headshape.icp** - [ft_volumerealign](/reference/ft_volumerealign)  
'yes' or 'no', use automatic realignment based on the icp-algorithm. If both 'interactive' and 'icp' are executed, the icp step follows the interactive realignment step (default = 'yes')

**cfg.headshape.interactive** - [ft_volumerealign](/reference/ft_volumerealign)  
'yes' or 'no', use interactive realignment to align headshape with scalp surface (default = 'yes')

**cfg.headshape.scalpsmooth** - [ft_volumerealign](/reference/ft_volumerealign)  
scalar, smoothing parameter for the scalp extraction (default = 2)

**cfg.headshape.scalpthreshold** - [ft_volumerealign](/reference/ft_volumerealign)  
scalar, threshold parameter for the scalp extraction (default = 0.1)

**cfg.height** - [ft_prepare_layout](/reference/ft_prepare_layout)  
scalar (default is automatic)

**cfg.highlight** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
'off', 'on', 'labels', 'numbers'

**cfg.highlight** - [ft_topoplotIC](/reference/ft_topoplotIC)  
'on', 'labels', 'numbers', 'off'

**cfg.highlightchannel** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
Nx1 cell-array with selection of channels, or vector containing channel indices see FT_CHANNELSELECTION

**cfg.highlightcolor** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
highlight marker color (default = [0 0 0] (black))

**cfg.highlightcolorneg** - [ft_clusterplot](/reference/ft_clusterplot)  
color of highlight marker for negative clusters (default = [0 0 0])

**cfg.highlightcolorpos** - [ft_clusterplot](/reference/ft_clusterplot)  
color of highlight marker for positive clusters (default = [0 0 0])

**cfg.highlightfontsize** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
highlight marker size (default = 8)

**cfg.highlightseries** - [ft_clusterplot](/reference/ft_clusterplot)  
1x5 cell-array, highlight option series with 'on', 'labels' or 'numbers' (default {'on', 'on', 'on', 'on', 'on'} for p < [0.01 0.05 0.1 0.2 0.3]

**cfg.highlightsize** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
highlight marker size (default = 6)

**cfg.highlightsizeseries** - [ft_clusterplot](/reference/ft_clusterplot)  
1x5 vector, highlight marker size series (default [6 6 6 6 6] for p < [0.01 0.05 0.1 0.2 0.3])

**cfg.highlightsymbol** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
highlight marker symbol (default = 'o')

**cfg.highlightsymbolseries** - [ft_clusterplot](/reference/ft_clusterplot)  
1x5 vector, highlight marker symbol series (default ['*', 'x', '+', 'o', '.'] for p < [0.01 0.05 0.1 0.2 0.3]

**cfg.hilbert** - [ft_preprocessing](/reference/ft_preprocessing)  
'no', 'abs', 'complex', 'real', 'imag', 'absreal', 'absimag' or 'angle' (default = 'no')

**cfg.host** - [ft_realtime_brainampproxy](/reference/ft_realtime_brainampproxy)  
string, name of computer running the recorder software (default = 'eeg002')

**cfg.hotkeys** - [ft_singleplotER](/reference/ft_singleplotER)  
enables hotkeys (leftarrow/rightarrow/uparrow/downarrow/m) for dynamic zoom and translation (ctrl+) of the axes

**cfg.hotkeys** - [ft_singleplotTFR](/reference/ft_singleplotTFR)  
enables hotkeys (leftarrow/rightarrow/uparrow/downarrow/pageup/pagedown/m) for dynamic zoom and translation (ctrl+) of the axes and color limits

**cfg.hotkeys** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
enables hotkeys (pageup/pagedown/m) for dynamic zoom and translation (ctrl+) of the color limits

**cfg.hotkeys** - [ft_multiplotTFR](/reference/ft_multiplotTFR)  
enables hotkeys (up/down arrows) for dynamic colorbar adjustment

**cfg.hpfiltdev** - [ft_preprocessing](/reference/ft_preprocessing)  
highpass max passband deviation (firws with 'kaiser' window, default 0.001 set in low-level function)

**cfg.hpfiltdf** - [ft_preprocessing](/reference/ft_preprocessing)  
highpass transition width (firws, overrides order, default set in low-level function)

**cfg.hpfiltdir** - [ft_preprocessing](/reference/ft_preprocessing)  
filter direction, 'twopass' (default), 'onepass' or 'onepass-reverse' or 'onepass-zerophase' (default for firws) or 'onepass-minphase' (firws, non-linear!)

**cfg.hpfilter** - [ft_preprocessing](/reference/ft_preprocessing), [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
'no' or 'yes' highpass filter (default = 'no')

**cfg.hpfiltord** - [ft_preprocessing](/reference/ft_preprocessing)  
highpass filter order (default set in low-level function)

**cfg.hpfilttype** - [ft_preprocessing](/reference/ft_preprocessing)  
digital filter type, 'but' or 'firws' or 'fir' or 'firls' (default = 'but')

**cfg.hpfiltwintype** - [ft_preprocessing](/reference/ft_preprocessing)  
highpass window type, 'hann' or 'hamming' (default) or 'blackman' or 'kaiser' (firws)

**cfg.hpfreq** - [ft_preprocessing](/reference/ft_preprocessing), [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
highpass frequency in Hz

**cfg.hpinstabilityfix** - [ft_preprocessing](/reference/ft_preprocessing)  
deal with filter instability, 'no', 'reduce', 'split' (default = 'no')

## I 

**cfg.icasso.Niter** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.icasso.mode** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.image** - [ft_prepare_layout](/reference/ft_prepare_layout)  
filename, use an image to construct a layout (e.g. useful for ECoG grids)

**cfg.image** - [ft_layoutplot](/reference/ft_layoutplot)  
filename, use an image to construct a layout (e.g. usefull for ECoG grids)

**cfg.implicitref** - [ft_preprocessing](/reference/ft_preprocessing)  
'label' or empty, add the implicit EEG reference as zeros (default = [])

**cfg.implicitref** - [ft_prepare_montage](/reference/ft_prepare_montage)  
string with the label of the implicit reference, or empty (default = [])

**cfg.individual.elec** - [ft_interactiverealign](/reference/ft_interactiverealign)  
structure

**cfg.individual.grad** - [ft_interactiverealign](/reference/ft_interactiverealign)  
structure

**cfg.individual.headmodel** - [ft_interactiverealign](/reference/ft_interactiverealign)  
structure, see FT_PREPARE_HEADMODEL

**cfg.individual.headmodelstyle** - [ft_interactiverealign](/reference/ft_interactiverealign)  
'vertex', 'edge', 'surface' or 'both' (default = 'edge')

**cfg.individual.headshape** - [ft_interactiverealign](/reference/ft_interactiverealign)  
structure, see FT_READ_HEADSHAPE

**cfg.individual.headshapestyle** - [ft_interactiverealign](/reference/ft_interactiverealign)  
'vertex', 'edge', 'surface' or 'both' (default = 'vertex')

**cfg.individual.mri** - [ft_interactiverealign](/reference/ft_interactiverealign)  
structure, see FT_READ_MRI

**cfg.input** - [ft_omri_pipeline](/reference/ft_omri_pipeline), [ft_omri_pipeline_nuisance](/reference/ft_omri_pipeline_nuisance)  
FieldTrip buffer containing raw scans (default 'buffer://localhost:1972')

**cfg.input** - [ft_omri_quality](/reference/ft_omri_quality)  
FieldTrip buffer containing raw scans (default='buffer://localhost:1972')

**cfg.input** - [ft_realtime_dicomproxy](/reference/ft_realtime_dicomproxy)  
string or cell-array of strings (see below)

**cfg.inputcoord** - [ft_volumelookup](/reference/ft_volumelookup), [ft_volumelookup](/reference/ft_volumelookup), [ft_volumelookup](/reference/ft_volumelookup)  
'mni' or 'tal', coordinate system of the mri/source/stat

**cfg.inputfile** - [ft_analysispipeline](/reference/ft_analysispipeline), [ft_annotate](/reference/ft_annotate), [ft_anonymizedata](/reference/ft_anonymizedata), [ft_appenddata](/reference/ft_appenddata), [ft_appendfreq](/reference/ft_appendfreq), [ft_artifact_clip](/reference/ft_artifact_clip), [ft_artifact_ecg](/reference/ft_artifact_ecg), [ft_artifact_eog](/reference/ft_artifact_eog), [ft_artifact_jump](/reference/ft_artifact_jump), [ft_artifact_muscle](/reference/ft_artifact_muscle), [ft_artifact_nan](/reference/ft_artifact_nan), [ft_artifact_threshold](/reference/ft_artifact_threshold), [ft_artifact_tms](/reference/ft_artifact_tms), [ft_channelnormalise](/reference/ft_channelnormalise), [ft_channelrepair](/reference/ft_channelrepair), [ft_clusterplot](/reference/ft_clusterplot), [ft_combineplanar](/reference/ft_combineplanar), [ft_componentanalysis](/reference/ft_componentanalysis), [ft_connectivityanalysis](/reference/ft_connectivityanalysis), [ft_denoise_synthetic](/reference/ft_denoise_synthetic), [ft_detect_movement](/reference/ft_detect_movement), [ft_dipolefitting](/reference/ft_dipolefitting), [ft_examplefunction](/reference/ft_examplefunction), [ft_freqanalysis](/reference/ft_freqanalysis), [ft_freqanalysis_mvar](/reference/ft_freqanalysis_mvar), [ft_freqdescriptives](/reference/ft_freqdescriptives), [ft_freqgrandaverage](/reference/ft_freqgrandaverage), [ft_freqinterpolate](/reference/ft_freqinterpolate), [ft_freqstatistics](/reference/ft_freqstatistics), [ft_globalmeanfield](/reference/ft_globalmeanfield), [ft_interpolatenan](/reference/ft_interpolatenan), [ft_lateralizedpotential](/reference/ft_lateralizedpotential), [ft_layoutplot](/reference/ft_layoutplot), [ft_math](/reference/ft_math), [ft_megplanar](/reference/ft_megplanar), [ft_megrealign](/reference/ft_megrealign), [ft_meshrealign](/reference/ft_meshrealign), [ft_movieplotER](/reference/ft_movieplotER), [ft_movieplotTFR](/reference/ft_movieplotTFR), [ft_multiplotER](/reference/ft_multiplotER), [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_mvaranalysis](/reference/ft_mvaranalysis), [ft_networkanalysis](/reference/ft_networkanalysis), [ft_nirs_prepare_ODtransformation](/reference/ft_nirs_prepare_ODtransformation), [ft_nirs_referencechannelsubtraction](/reference/ft_nirs_referencechannelsubtraction), [ft_nirs_scalpcouplingindex](/reference/ft_nirs_scalpcouplingindex), [ft_nirs_transform_ODs](/reference/ft_nirs_transform_ODs), [ft_prepare_leadfield](/reference/ft_prepare_leadfield), [ft_prepare_mesh](/reference/ft_prepare_mesh), [ft_preprocessing](/reference/ft_preprocessing), [ft_redefinetrial](/reference/ft_redefinetrial), [ft_regressconfound](/reference/ft_regressconfound), [ft_rejectartifact](/reference/ft_rejectartifact), [ft_rejectcomponent](/reference/ft_rejectcomponent), [ft_rejectvisual](/reference/ft_rejectvisual), [ft_removetemplateartifact](/reference/ft_removetemplateartifact), [ft_resampledata](/reference/ft_resampledata), [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity), [ft_singleplotER](/reference/ft_singleplotER), [ft_sourceanalysis](/reference/ft_sourceanalysis), [ft_sourcedescriptives](/reference/ft_sourcedescriptives), [ft_sourcegrandaverage](/reference/ft_sourcegrandaverage), [ft_sourceinterpolate](/reference/ft_sourceinterpolate), [ft_sourcemovie](/reference/ft_sourcemovie), [ft_sourceplot](/reference/ft_sourceplot), [ft_sourcewrite](/reference/ft_sourcewrite), [ft_timelockanalysis](/reference/ft_timelockanalysis), [ft_timelockbaseline](/reference/ft_timelockbaseline), [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage), [ft_timelockstatistics](/reference/ft_timelockstatistics), [ft_topoplotCC](/reference/ft_topoplotCC), [ft_topoplotTFR](/reference/ft_topoplotTFR), [ft_topoplotTFR](/reference/ft_topoplotTFR), [ft_volumedownsample](/reference/ft_volumedownsample), [ft_volumenormalise](/reference/ft_volumenormalise), [ft_volumerealign](/reference/ft_volumerealign), [ft_volumereslice](/reference/ft_volumereslice), [ft_volumesegment](/reference/ft_volumesegment), [ft_volumewrite](/reference/ft_volumewrite)  
...

**cfg.interactive** - [ft_movieplotTFR](/reference/ft_movieplotTFR)  
'no' or 'yes', make it interactive

**cfg.interactive** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster)  
'yes' (default) or 'no'. If 'yes', zooming and panning operate via callbacks.

**cfg.interactive** - [ft_spikedetection](/reference/ft_spikedetection)  
'yes' or 'no'

**cfg.interactive** - [ft_audiovideobrowser](/reference/ft_audiovideobrowser)  
'yes' or 'no' (default = 'yes')

**cfg.interactive** - [ft_sliceinterp](/reference/ft_sliceinterp)  
'yes' or 'no' (default), interactive coordinates and source values

**cfg.interactive** - [ft_multiplotER](/reference/ft_multiplotER)  
'yes' or 'no', make the plot interactive (default = 'yes') In a interactive plot you can select areas and produce a new interactive plot when a selected area is clicked. Multiple areas can be selected by holding down the SHIFT key.

**cfg.interactive** - [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotTFR](/reference/ft_singleplotTFR), [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
Interactive plot 'yes' or 'no' (default = 'yes') In a interactive plot you can select areas and produce a new interactive plot when a selected area is clicked. Multiple areas can be selected by holding down the SHIFT key.

**cfg.interactive** - [ft_singleplotER](/reference/ft_singleplotER)  
interactive plot 'yes' or 'no' (default = 'yes') in a interactive plot you can select areas and produce a new interactive plot when a selected area is clicked. multiple areas can be selected by holding down the shift key.

**cfg.interplimits** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
limits for interpolation (default = 'head') 'electrodes' to furthest electrode 'head' to edge of head

**cfg.interpmethod** - [ft_sourceinterpolate](/reference/ft_sourceinterpolate)  
string, can be 'nearest', 'linear', 'cubic', 'spline', 'sphere_avg' or 'smudge' (default = 'linear for interpolating two 3D volumes, 'nearest' for all other cases)

**cfg.interpolate** - [ft_spike_waveform](/reference/ft_spike_waveform)  
double integer (default = 1). Increaes the density of samples by a factor cfg.interpolate

**cfg.interpolate** - [ft_spike_plot_isireturn](/reference/ft_spike_plot_isireturn), [ft_spike_plot_jpsth](/reference/ft_spike_plot_jpsth)  
integer (default = 1), we perform interpolating with extra number of spacings determined by cfg.interpolate. For example cfg.interpolate = 5 means 5 times more dense axis.

**cfg.interpolatenan** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
string 'yes', 'no' (default = 'yes') interpolate over channels containing NaNs

**cfg.interpolation** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
'linear','cubic','nearest','v4' (default = 'v4') see GRIDDATA

**cfg.interptoi** - [ft_spiketriggeredinterpolation](/reference/ft_spiketriggeredinterpolation)  
value, time in seconds used for interpolation, which must be larger than timwin (default = 0.2)

**cfg.inwardshift** - [ft_megrealign](/reference/ft_megrealign)  


**cfg.inwardshift** - [ft_megplanar](/reference/ft_megplanar)  
depth of the source layer relative to the head model surface (default = 2.5 cm, which is appropriate for a skin-based head model)

**cfg.inwardshift** - [ft_megrealign](/reference/ft_megrealign)  
depth of the source layer relative to the headshape surface or volume conduction model (no default supplied, see below)

**cfg.inwardshift** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
number, how much should the innermost surface be moved inward to constrain sources to be considered inside the source compartment (default = 0)

**cfg.isodistance** - [ft_electroderealign](/reference/ft_electroderealign)  
'yes', 'no' (default) or number, to enforce isotropic inter-electrode distances (pairmethod 'label' only)

**cfg.isolatedsource** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
(optional)

**cfg.iti** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
scalar, inter-trial interval in seconds (default = 1)

**cfg.ivar** - [ft_statistics_analytic](/reference/ft_statistics_analytic), [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
number or list with indices, independent variable(s)

## J 

**cfg.jackknife** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
'no' (default) or 'yes' specifies whether the coefficients are estimated for all leave-one-out sets of trials

**cfg.jackknife** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes' jackknife resampling of trials

**cfg.jackknife** - [ft_freqdescriptives](/reference/ft_freqdescriptives)  
'yes' or 'no', estimate standard error by means of the jack-knife (default = 'no')

**cfg.jumptoeof** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_synchronous](/reference/ft_realtime_synchronous)  
causes the realtime function to jump to the end

**cfg.jumptoeof** - [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer)  
causes the realtime function to jump to the end when the

**cfg.jumptoeof** - [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
jump to end of file at initialization (default = 'no')

**cfg.jumptoeof** - [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer), [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect), [ft_realtime_signalrecorder](/reference/ft_realtime_signalrecorder), [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer)  
whether to skip to the end of the stream/file at startup (default = 'yes')

**cfg.jumptoeof** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_synchronous](/reference/ft_realtime_synchronous)  
whether to start on the 'first or 'last' data that is available when the function _starts_ (default = 'last')

## K 

**cfg.kappa** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
number or empty for automatic default

**cfg.kappa** - [ft_denoise_prewhiten](/reference/ft_denoise_prewhiten)  
scalar, truncation parameter for the inverse

**cfg.keepbrain** - [ft_defacevolume](/reference/ft_defacevolume)  
'no' or 'yes', segment and retain the brain (default = 'no')

**cfg.keepchannel** - [ft_electroderealign](/reference/ft_electroderealign)  
string, 'yes' or 'no' (default = 'no')

**cfg.keepchannel** - [ft_rejectvisual](/reference/ft_rejectvisual)  
string, determines how to deal with channels that are not selected, can be 'no' completely remove deselected channels from the data (default) 'yes' keep deselected channels in the output data 'nan' fill the channels that are deselected with NaNs 'repair' repair the deselected channels using FT_CHANNELREPAIR

**cfg.keepcsd** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes'

**cfg.keepcsd** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'yes' or 'no' (default = 'no')

**cfg.keepfield** - [ft_anonymizedata](/reference/ft_anonymizedata)  
cell-array with strings, fields to keep (default = {})

**cfg.keepfilter** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes'

**cfg.keepindividual** - [ft_sourcegrandaverage](/reference/ft_sourcegrandaverage)  
'no' or 'yes'

**cfg.keepindividual** - [ft_freqgrandaverage](/reference/ft_freqgrandaverage), [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)  
'yes' or 'no' (default = 'no')

**cfg.keepinside** - [ft_volumedownsample](/reference/ft_volumedownsample)  
'yes' or 'no', keep the inside/outside labeling (default = 'yes')

**cfg.keepleadfield** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes'

**cfg.keepmom** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes'

**cfg.keepmom** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'yes' or 'no' (default = 'yes')

**cfg.keepnoisecsd** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'yes' or 'no' (default = 'no')

**cfg.keepnoisemom** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'yes' or 'no' (default = 'yes')

**cfg.keepnumeric** - [ft_anonymizedata](/reference/ft_anonymizedata)  
'yes' or 'no', keep numeric fields (default = 'yes')

**cfg.keepremoved** - [ft_analysispipeline](/reference/ft_analysispipeline)  
'yes' or 'no', determines whether removed fields are completely removed, or only replaced by a short textual description (default = 'no')

**cfg.keepsampleinfo** - [ft_appenddata](/reference/ft_appenddata), [ft_appendtimelock](/reference/ft_appendtimelock)  
'yes', 'no', 'ifmakessense' (default = 'ifmakessense')

**cfg.keeptapers** - [ft_freqanalysis](/reference/ft_freqanalysis)  
'yes' or 'no', return individual tapers or average (default = 'no')

**cfg.keeptrial** - [ft_rejectvisual](/reference/ft_rejectvisual)  
string, determines how to deal with trials that are not selected, can be 'no' completely remove deselected trials from the data (default) 'yes' keep deselected trials in the output data 'nan' fill the trials that are deselected with NaNs

**cfg.keeptrials** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
'no' (default) or 'yes' specifies whether the coefficients are estimated for each trial separately, or on the concatenated data

**cfg.keeptrials** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes'

**cfg.keeptrials** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'yes' or 'no' (default = 'no')

**cfg.keeptrials** - [ft_spike_jpsth](/reference/ft_spike_jpsth), [ft_spike_psth](/reference/ft_spike_psth), [ft_spike_xcorr](/reference/ft_spike_xcorr)  
'yes' or 'no' (default)

**cfg.keeptrials** - [ft_spike_rate](/reference/ft_spike_rate)  
'yes' or 'no' (default).

**cfg.keeptrials** - [ft_spikedensity](/reference/ft_spikedensity)  
'yes' or 'no' (default). If 'yes', we store the trials in a matrix in the output SDF as well

**cfg.keeptrials** - [ft_freqdescriptives](/reference/ft_freqdescriptives)  
'yes' or 'no', estimate single trial power (useful for fourier data) (default = 'no')

**cfg.keeptrials** - [ft_nonlinearassociation](/reference/ft_nonlinearassociation)  
'yes' or 'no', process the individual trials or the concatenated data (default = 'no')

**cfg.keeptrials** - [ft_freqanalysis](/reference/ft_freqanalysis), [ft_spiketriggeredaverage](/reference/ft_spiketriggeredaverage), [ft_timelockanalysis](/reference/ft_timelockanalysis)  
'yes' or 'no', return individual trials or average (default = 'no')

**cfg.keeptrials** - [ft_crossfrequencyanalysis](/reference/ft_crossfrequencyanalysis)  
string, can be 'yes' or 'no'

**cfg.keepvalue** - [ft_anonymizedata](/reference/ft_anonymizedata)  
cell-array with strings, values to keep (default = {})

**cfg.kmeans** - [ft_spikesorting](/reference/ft_spikesorting)  
substructure with additional low-level options for this method

**cfg.kurtosis** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'yes' or 'no' (default = 'no')

## L 

**cfg.lambda** - [ft_omri_quality](/reference/ft_omri_quality)  
forgetting factor for the variaton plot (default=0.9)

**cfg.lambda** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
number or empty for automatic default

**cfg.lambda** - [ft_channelrepair](/reference/ft_channelrepair)  
regularisation parameter (default = 1e-5, not for method 'distance')

**cfg.lambda** - [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity)  
regularization parameter (default = 1e-05)

**cfg.lambda** - [ft_denoise_prewhiten](/reference/ft_denoise_prewhiten)  
scalar, or string, regularization parameter for the inverse

**cfg.latency** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
[b1 e1; b2 e2; ...]

**cfg.latency** - [ft_spiketriggeredspectrum_stat](/reference/ft_spiketriggeredspectrum_stat)  
[beg end] in sec, or 'maxperiod', 'poststim' or 'prestim'. This determines the start and end of analysis window.

**cfg.latency** - [ft_spike_rate](/reference/ft_spike_rate)  
[begin end] in seconds 'maxperiod' (default) 'minperiod', i.e., the minimal period all trials share 'prestim' (all t<=0) 'poststim' (all t>=0).

**cfg.latency** - [ft_spike_select](/reference/ft_spike_select)  
[begin end] in seconds 'maxperiod' (default), i.e., maximum period available 'minperiod', i.e., the minimal period all trials share 'prestim' (all t<=0) 'poststim' (all t>=0).

**cfg.latency** - [ft_spike_psth](/reference/ft_spike_psth)  
[begin end] in seconds 'maxperiod' (default), i.e., maximum period available 'minperiod', i.e., the minimal period all trials share, 'prestim' (all t<=0) 'poststim' (all t>=0).

**cfg.latency** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_freqstatistics](/reference/ft_freqstatistics), [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage), [ft_timelockstatistics](/reference/ft_timelockstatistics)  
[begin end] in seconds or 'all' (default = 'all')

**cfg.latency** - [ft_spike_plot_jpsth](/reference/ft_spike_plot_jpsth)  
[begin end] in seconds or 'max' (default), 'prestim' or 'poststim';

**cfg.latency** - [ft_spike_isi](/reference/ft_spike_isi)  
[begin end] in seconds, 'max' (default), 'min', 'prestim'(t<=0), or 'poststim' (t>=0). If 'max', we use all available latencies. If 'min', we use only the time window contained by all trials. If 'prestim' or 'poststim', we use time to or from 0, respectively.

**cfg.latency** - [ft_spike_xcorr](/reference/ft_spike_xcorr)  
[begin end] in seconds, 'max' (default), 'min', 'prestim'(t<=0), or 'poststim' (t>=0).%

**cfg.latency** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster)  
[begin end] in seconds, 'maxperiod' (default), 'minperiod', 'prestim' (all t<=0), or 'poststim' (all t>=0).

**cfg.latency** - [ft_spikedensity](/reference/ft_spikedensity)  
[begin end] in seconds, 'maxperiod' (default), 'minperiod', 'prestim'(t>=0), or 'poststim' (t>=0).

**cfg.latency** - [ft_spike_jpsth](/reference/ft_spike_jpsth)  
[begin end] in seconds, 'maxperiod' (default), 'prestim'(t<=0), or 'poststim' (t>=0)

**cfg.latency** - [ft_spike_plot_psth](/reference/ft_spike_plot_psth)  
[begin end] in seconds, 'maxperiod' (default), 'prestim'(t<=0), or 'poststim' (t>=0).

**cfg.latency** - [ft_rejectvisual](/reference/ft_rejectvisual), [ft_timelockanalysis](/reference/ft_timelockanalysis)  
[begin end] in seconds, or 'all', 'minperiod', 'maxperiod', 'prestim', 'poststim' (default = 'all')

**cfg.latency** - [ft_spikesplitting](/reference/ft_spikesplitting)  
[begin end], (default = 'all')

**cfg.latency** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
[begin end], default is [0 inf]

**cfg.latency** - [ft_freqdescriptives](/reference/ft_freqdescriptives)  
[tmin tmax] or 'all', to specify a subset of latencies (default = 'all')

**cfg.latency** - [ft_sourceplot](/reference/ft_sourceplot)  
scalar or string, can be 'all', 'prestim', 'poststim', or [beg end], specify time range in seconds

**cfg.latency** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
single number in seconds, for time-frequency analysis

**cfg.layout** - [ft_realtime_topography](/reference/ft_realtime_topography)  
'CTF151.lay';

**cfg.layout** - [ft_prepare_layout](/reference/ft_prepare_layout)  
'butterfly' will give you a layout with all channels on top of each other

**cfg.layout** - [ft_prepare_layout](/reference/ft_prepare_layout)  
'circular' will distribute the channels on a circle

**cfg.layout** - [ft_prepare_layout](/reference/ft_prepare_layout)  
'horizontal' will give you a 1xN ordered layout

**cfg.layout** - [ft_layoutplot](/reference/ft_layoutplot)  
'ordered'

**cfg.layout** - [ft_prepare_layout](/reference/ft_prepare_layout)  
'ordered' will give you a NxN ordered layout

**cfg.layout** - [ft_prepare_layout](/reference/ft_prepare_layout)  
'vertical' will give you a Nx1 ordered layout

**cfg.layout** - [ft_prepare_layout](/reference/ft_prepare_layout)  
filename containg the input layout (*.mat or *.lay file), this can also be a layout structure, which is simply returned as-is (see below for details)

**cfg.layout** - [ft_layoutplot](/reference/ft_layoutplot)  
filename containg the layout

**cfg.layout** - [ft_databrowser](/reference/ft_databrowser), [ft_icabrowser](/reference/ft_icabrowser), [ft_neighbourplot](/reference/ft_neighbourplot), [ft_prepare_neighbours](/reference/ft_prepare_neighbours)  
filename of the layout, see FT_PREPARE_LAYOUT

**cfg.layout** - [ft_realtime_topography](/reference/ft_realtime_topography), [ft_topoplotCC](/reference/ft_topoplotCC)  
specification of the layout, see FT_PREPARE_LAYOUT

**cfg.layout** - [ft_movieplotER](/reference/ft_movieplotER), [ft_movieplotTFR](/reference/ft_movieplotTFR), [ft_topoplotIC](/reference/ft_topoplotIC)  
specification of the layout, see below

**cfg.layout** - [ft_multiplotER](/reference/ft_multiplotER), [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
specify the channel layout for plotting using one of the supported ways (see below).

**cfg.length** - [ft_redefinetrial](/reference/ft_redefinetrial)  
single number (in unit of time, typically seconds) of the required snippets

**cfg.level1.condition** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
scalar, or vector of length L1 (default = 1)

**cfg.level1.gain** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
scalar, or vector of length L1 (default = 1)

**cfg.level2.condition** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
scalar, or vector of length L2 (default = 1)

**cfg.level2.gain** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
scalar, or vector of length L2 (default = 1)

**cfg.level3.condition** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
scalar, or vector of length L3 (default = 1)

**cfg.level3.gain** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
scalar, or vector of length L3 (default = 1)

**cfg.limittext** - [ft_multiplotER](/reference/ft_multiplotER), [ft_multiplotTFR](/reference/ft_multiplotTFR)  
add user-defined text instead of cfg.comment, (default = cfg.comment)

**cfg.linefreq** - [ft_qualitycheck](/reference/ft_qualitycheck)  
scalar, frequency of power line (default = 50)

**cfg.linestyle** - [ft_multiplotER](/reference/ft_multiplotER), [ft_singleplotER](/reference/ft_singleplotER)  
linestyle/marker type, see options of the PLOT function (default = '-') can be a single style for all datasets, or a cell-array containing one style for each dataset

**cfg.linewidth** - [ft_multiplotER](/reference/ft_multiplotER), [ft_singleplotER](/reference/ft_singleplotER)  
linewidth in points (default = 0.5)

**cfg.linewidth** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster)  
number indicating the width of the lines (default = 1);

**cfg.linewidth** - [ft_databrowser](/reference/ft_databrowser)  
number, width of plotted lines (default = 0.5)

**cfg.location** - [ft_sourceplot](/reference/ft_sourceplot)  
location of cut, (default = 'auto') 'auto', 'center' if only anatomy, 'max' if functional data 'min' and 'max' position of min/max funparameter 'center' of the brain [x y z], coordinates in voxels or head, see cfg.locationcoordinates

**cfg.locationcoordinates** - [ft_sourceplot](/reference/ft_sourceplot)  
coordinate system used in cfg.location, 'head' or 'voxel' (default = 'head') 'head', headcoordinates as mm or cm 'voxel', voxelcoordinates as indices

**cfg.lpfiltdev** - [ft_preprocessing](/reference/ft_preprocessing)  
lowpass max passband deviation (firws with 'kaiser' window, default 0.001 set in low-level function)

**cfg.lpfiltdf** - [ft_preprocessing](/reference/ft_preprocessing)  
lowpass transition width (firws, overrides order, default set in low-level function)

**cfg.lpfiltdir** - [ft_preprocessing](/reference/ft_preprocessing)  
filter direction, 'twopass' (default), 'onepass' or 'onepass-reverse' or 'onepass-zerophase' (default for firws) or 'onepass-minphase' (firws, non-linear!)

**cfg.lpfilter** - [ft_preprocessing](/reference/ft_preprocessing), [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
'no' or 'yes' lowpass filter (default = 'no')

**cfg.lpfiltord** - [ft_preprocessing](/reference/ft_preprocessing)  
lowpass filter order (default set in low-level function)

**cfg.lpfilttype** - [ft_preprocessing](/reference/ft_preprocessing)  
digital filter type, 'but' or 'firws' or 'fir' or 'firls' (default = 'but')

**cfg.lpfiltwintype** - [ft_preprocessing](/reference/ft_preprocessing)  
lowpass window type, 'hann' or 'hamming' (default) or 'blackman' or 'kaiser' (firws)

**cfg.lpfreq** - [ft_preprocessing](/reference/ft_preprocessing), [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
lowpass frequency in Hz

**cfg.lpinstabilityfix** - [ft_preprocessing](/reference/ft_preprocessing)  
deal with filter instability, 'no', 'reduce', 'split' (default = 'no')

## M 

**cfg.magradius** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
number representing the radius for the cfg.magtype based search (default = 3)

**cfg.magscale** - [ft_multiplotER](/reference/ft_multiplotER), [ft_multiplotTFR](/reference/ft_multiplotTFR)  
number, scaling to apply to the MEG magnetometer channels prior to display

**cfg.magscale** - [ft_databrowser](/reference/ft_databrowser), [ft_rejectvisual](/reference/ft_rejectvisual)  
number, scaling to apply to the MEG magnetometer channels prior to display (in addition to the cfg.megscale factor)

**cfg.magtype** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
string representing the 'magnet' type used for placing the electrodes 'peakweighted' place electrodes at weighted peak intensity voxel (default) 'troughweighted' place electrodes at weighted trough intensity voxel 'peak' place electrodes at peak intensity voxel (default) 'trough' place electrodes at trough intensity voxel 'weighted' place electrodes at center-of-mass

**cfg.markcorner** - [ft_volumewrite](/reference/ft_volumewrite)  
'yes' or 'no', mark the first corner of the volume

**cfg.marker** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
'on', 'labels', 'numbers', 'off'

**cfg.marker** - [ft_sliceinterp](/reference/ft_sliceinterp)  
[Nx3] array defining N marker positions to display

**cfg.markercolor** - [ft_sliceinterp](/reference/ft_sliceinterp)  
[1x3] marker color in RGB (default = [1 1 1], i.e. white)

**cfg.markercolor** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
channel marker color (default = [0 0 0] (black))

**cfg.markerfontsize** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
font size of channel labels (default = 8 pt)

**cfg.markersize** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
channel marker size (default = 2)

**cfg.markersize** - [ft_sliceinterp](/reference/ft_sliceinterp)  
radius of markers (default = 5);

**cfg.markersymbol** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
channel marker symbol (default = 'o')

**cfg.markfiducial** - [ft_volumewrite](/reference/ft_volumewrite)  
'yes' or 'no', mark the fiducials

**cfg.markorigin** - [ft_volumewrite](/reference/ft_volumewrite)  
'yes' or 'no', mark the origin

**cfg.mask** - [ft_layoutplot](/reference/ft_layoutplot)  
string, 'yes' or 'no' whether the mask should be plotted (default = 'yes')

**cfg.mask** - [ft_prepare_layout](/reference/ft_prepare_layout)  
string, how to create the mask, can be 'circle', 'square', 'convex', 'headshape', 'mri' or 'no' (default is automatic)

**cfg.maskclipmax** - [ft_sliceinterp](/reference/ft_sliceinterp)  
value or 'auto' (clipping of mask data)

**cfg.maskclipmin** - [ft_sliceinterp](/reference/ft_sliceinterp)  
value or 'auto' (clipping of mask data)

**cfg.maskclipsym** - [ft_sliceinterp](/reference/ft_sliceinterp)  
'yes' or 'no' (default) symmetrical clipping

**cfg.maskcolmin** - [ft_sliceinterp](/reference/ft_sliceinterp)  
mask value mapped to the highest opacity, i.e. non-transparent (default = 'auto')

**cfg.maskcolmin** - [ft_sliceinterp](/reference/ft_sliceinterp)  
mask value mapped to the lowest opacity, i.e. completely transparent (default ='auto')

**cfg.maskfacealpha** - [ft_multiplotER](/reference/ft_multiplotER), [ft_singleplotER](/reference/ft_singleplotER)  
mask transparency value between 0 and 1

**cfg.maskmap** - [ft_sliceinterp](/reference/ft_sliceinterp)  
opacitymap for source overlay (default is linspace(0,1,128))

**cfg.masknans** - [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotTFR](/reference/ft_singleplotTFR)  
'yes' or 'no' (default = 'yes')

**cfg.maskparameter** - [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotTFR](/reference/ft_singleplotTFR)  
field in the data to be used for masking of data, can be logical (e.g. significant data points) or numerical (e.g. t-values). (not possible for mean over multiple channels, or when input contains multiple subjects or trials)

**cfg.maskparameter** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
field in the data to be used for masking of data. It should have alues between 0 and 1, where 0 corresponds to transparent.

**cfg.maskparameter** - [ft_multiplotER](/reference/ft_multiplotER)  
field in the first dataset to be used for marking significant data

**cfg.maskparameter** - [ft_singleplotER](/reference/ft_singleplotER)  
field in the first dataset to be used for masking of data (not possible for mean over multiple channels, or when input contains multiple subjects or trials)

**cfg.maskparameter** - [ft_sliceinterp](/reference/ft_sliceinterp)  
parameter used as opacity mask (default = 'none')

**cfg.maskparameter** - [ft_sourceplot](/reference/ft_sourceplot)  
string, field in the data to be used for opacity masking of fun data (default = []) If values are between 0 and 1, zero is fully transparant and one is fully opaque. If values in the field are not between 0 and 1 they will be scaled depending on the values of cfg.opacitymap and cfg.opacitylim (see below) You can use masking in several ways, f.i. - use outcome of statistics to show only the significant values and mask the insignificant NB see also cfg.opacitymap and cfg.opacitylim below - use the functional data itself as mask, the highest value (and/or lowest when negative) will be opaque and the value closest to zero transparent - Make your own field in the data with values between 0 and 1 to control opacity directly

**cfg.maskparameter** - [ft_volumelookup](/reference/ft_volumelookup)  
string, field in volume to be looked up, data in field should be logical

**cfg.maskparameter** - [ft_sourcemovie](/reference/ft_sourcemovie)  
string, functional parameter that is used for opacity (default = [])

**cfg.maskstyle** - [ft_sourceplot](/reference/ft_sourceplot)  
'opacity', or 'colormix'. If 'opacity', low-level graphics opacity masking is applied, if 'colormix', the color data is explicitly expressed as a single RGB value, incorporating the opacitymask. Yields faster and more robust rendering in general.

**cfg.maskstyle** - [ft_multiplotER](/reference/ft_multiplotER), [ft_singleplotER](/reference/ft_singleplotER)  
style used for masking of data, 'box', 'thickness' or 'saturation' (default = 'box')

**cfg.maskstyle** - [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotTFR](/reference/ft_singleplotTFR)  
style used to masking, 'opacity', 'saturation', or 'outline' (default = 'opacity') 'outline' can only be used with a logical cfg.maskparameter use 'saturation' or 'outline' when saving to vector-format (like *.eps) to avoid all sorts of image-problems

**cfg.match** - [ft_recodeevent](/reference/ft_recodeevent)  
'exact' or 'nearest'

**cfg.matfile** - [ft_qualitycheck](/reference/ft_qualitycheck)  
string, filename (e.g. 'previousoutput.mat'), preferably in combination with analyze = 'no'

**cfg.maxAbs** - [ft_omri_quality](/reference/ft_omri_quality)  
threshold (mm) for absolute motion before 'A' is sent to serial port, default = Inf

**cfg.maxRel** - [ft_omri_quality](/reference/ft_omri_quality)  
threshold (mm) for relative motion before 'B' is sent to serial port, default = Inf

**cfg.maxblocksize** - [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
number, in seconds (default = 1)

**cfg.maxdelay** - [ft_nonlinearassociation](/reference/ft_nonlinearassociation)  
32/cfg.fsample

**cfg.maxiter** - [ft_electroderealign](/reference/ft_electroderealign)  
number (default: 50), maximum number of optimization iterations

**cfg.maxlag** - [ft_spike_xcorr](/reference/ft_spike_xcorr)  
number in seconds, indicating the maximum lag for the cross-correlation function in sec (default = 0.1 sec).

**cfg.maxqueryrange** - [ft_volumelookup](/reference/ft_volumelookup), [ft_volumelookup](/reference/ft_volumelookup)  
number, should be odd and >= to minqueryrange (default = 1)

**cfg.maxradius** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
(optional)

**cfg.medianfilter** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or 'yes' jump preserving median filter (default = 'no')

**cfg.medianfiltord** - [ft_preprocessing](/reference/ft_preprocessing)  
length of median filter (default = 9)

**cfg.medianwindow** - [ft_electrodermalactivity](/reference/ft_electrodermalactivity)  
scalar, length of window for median filter in seconds (default = 8)

**cfg.megscale** - [ft_databrowser](/reference/ft_databrowser), [ft_rejectvisual](/reference/ft_rejectvisual)  
number, scaling to apply to the MEG channels prior to display

**cfg.memory** - [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
'low' or 'high', whether to be memory or computationally efficient, respectively (default = 'high')

**cfg.method** - [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)  
'across' (default) or 'within', see below.

**cfg.method** - [ft_defacevolume](/reference/ft_defacevolume)  
'box', 'spm' (default = 'box')

**cfg.method** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
'cortexhull';

**cfg.method** - [ft_artifact_tms](/reference/ft_artifact_tms)  
'detect' or 'marker', see below.

**cfg.method** - [ft_prepare_neighbours](/reference/ft_prepare_neighbours)  
'distance', 'triangulation' or 'template'

**cfg.method** - [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity)  
'finite' for finite-difference method or 'spline' for spherical spline method 'hjorth' for Hjorth approximation method

**cfg.method** - [ft_electroderealign](/reference/ft_electroderealign), [ft_electroderealign](/reference/ft_electroderealign)  
'headshape'

**cfg.method** - [ft_stratify](/reference/ft_stratify)  
'histogram' 'splithilo' 'splitlohi' 'splitlolo' 'splithihi' 'equatespike'

**cfg.method** - [ft_spike_jpsth](/reference/ft_spike_jpsth)  
'jpsth' or 'shiftpredictor'. If 'jpsth', we output the normal stat. If 'shiftpredictor', we compute the jpsth after shuffling subsequent trials.

**cfg.method** - [ft_spikesorting](/reference/ft_spikesorting)  
'kmeans', 'ward'

**cfg.method** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'lcmv' linear constrained minimum variance beamformer 'sam' synthetic aperture magnetometry 'dics' dynamic imaging of coherent sources 'pcc' partial cannonical correlation/coherence 'mne' minimum norm estimation 'rv' scan residual variance with single dipole 'music' multiple signal classification 'sloreta' standardized low-resolution electromagnetic tomography 'eloreta' exact low-resolution electromagnetic tomography

**cfg.method** - [ft_spiketriggeredspectrum](/reference/ft_spiketriggeredspectrum)  
'mtmfft' or 'mtmconvol' (see below)

**cfg.method** - [ft_freqinterpolate](/reference/ft_freqinterpolate)  
'nan', 'linear' (default = 'nan')

**cfg.method** - [ft_channelnormalise](/reference/ft_channelnormalise)  
'perchannel', or 'acrosschannel', computes the standard deviation per channel, or across all channels. The latter method leads to the same scaling across channels and preserves topographical distributions

**cfg.method** - [ft_componentanalysis](/reference/ft_componentanalysis)  
'runica', 'fastica', 'binica', 'pca', 'svd', 'jader', 'varimax', 'dss', 'cca', 'sobi', 'white' or 'csp' (default = 'runica')

**cfg.method** - [ft_sourceplot](/reference/ft_sourceplot)  
'slice', plots the data on a number of slices in the same plane 'ortho', plots the data on three orthogonal slices 'surface', plots the data on a 3D brain surface 'glassbrain', plots a max-projection through the brain 'vertex', plots the grid points or vertices scaled according to the functional value 'cloud', plot the data as clouds, spheres, or points scaled according to the functional value

**cfg.method** - [ft_statistics_stats](/reference/ft_statistics_stats)  
'stats'

**cfg.method** - [ft_combineplanar](/reference/ft_combineplanar)  
'sum', 'svd', 'abssvd', or 'complex' (default = 'sum')

**cfg.method** - [ft_preprocessing](/reference/ft_preprocessing)  
'trial' or 'channel', read data per trial or per channel (default = 'trial')

**cfg.method** - [ft_headmovement](/reference/ft_headmovement)  
'updatesens' (default), 'cluster', 'avgoverrpt', 'pertrial_cluster', 'pertrial'

**cfg.method** - [ft_channelrepair](/reference/ft_channelrepair)  
'weighted', 'average', 'spline', 'slap' or 'nan' (default = 'weighted')

**cfg.method** - [ft_spike_xcorr](/reference/ft_spike_xcorr)  
'xcorr' or 'shiftpredictor'. If 'shiftpredictor' we do not compute the normal cross-correlation but shuffle the subsequent trials. If two channels are independent, then the shift predictor should give the same correlogram as the raw correlogram calculated from the same trials. Typically, the shift predictor is subtracted from the correlogram.

**cfg.method** - [ft_freqsimulation](/reference/ft_freqsimulation)  
The methods are explained in more detail below, but they can be 'superimposed' simply add the contribution of the different frequencies 'broadband' create a single broadband signal component 'phalow_amphigh' phase of low freq correlated with amplitude of high freq 'amplow_amphigh' amplitude of low freq correlated with amplithude of high freq 'phalow_freqhigh' phase of low freq correlated with frequency of high signal 'asymmetric' single signal component with asymmetric positive/negative deflections

**cfg.method** - [ft_sourcestatistics](/reference/ft_sourcestatistics)  
different methods for calculating the probability of the null-hypothesis, 'montecarlo' uses a non-parametric randomization test to get a Monte-Carlo estimate of the probability, 'analytic' uses a parametric test that results in analytic probability, 'stats' (soon deprecated) uses a parametric test from the MATLAB statistics toolbox,

**cfg.method** - [ft_freqstatistics](/reference/ft_freqstatistics), [ft_timelockstatistics](/reference/ft_timelockstatistics)  
different methods for calculating the significance probability and/or critical value 'montecarlo' get Monte-Carlo estimates of the significance probabilities and/or critical values from the permutation distribution, 'analytic' get significance probabilities and/or critical values from the analytic reference distribution (typically, the sampling distribution under the null hypothesis), 'stats' use a parametric test from the MATLAB statistics toolbox, 'crossvalidate' use crossvalidation to compute predictive performance

**cfg.method** - [ft_freqanalysis](/reference/ft_freqanalysis)  
different methods of calculating the spectra 'mtmfft', analyses an entire spectrum for the entire data length, implements multitaper frequency transformation 'mtmconvol', implements multitaper time-frequency transformation based on multiplication in the frequency domain. 'wavelet', implements wavelet time frequency transformation (using Morlet wavelets) based on multiplication in the frequency domain. 'tfr', implements wavelet time frequency transformation (using Morlet wavelets) based on convolution in the time domain. 'mvar', does a fourier transform on the coefficients of an estimated multivariate autoregressive model, obtained with FT_MVARANALYSIS. In this case, the output will contain a spectral transfer matrix, the cross-spectral density matrix, and the covariance matrix of the innovatio noise.

**cfg.method** - [ft_resampledata](/reference/ft_resampledata)  
interpolation method, see INTERP1 (default = 'pchip')

**cfg.method** - [ft_spike_rate_orituning](/reference/ft_spike_rate_orituning)  
model to apply, implemented are 'orientation' and 'direction'

**cfg.method** - [ft_spikedownsample](/reference/ft_spikedownsample)  
resampling method, can be 'resample', 'decimate' or 'downsample'

**cfg.method** - [ft_volumerealign](/reference/ft_volumerealign)  
string representing the method for aligning 'interactive' use the GUI to specify the fiducials 'fiducial' use pre-specified fiducials 'headshape' match the MRI surface to a headshape 'spm' match to template anatomical MRI 'fsl' match to template anatomical MRI

**cfg.method** - [ft_electroderealign](/reference/ft_electroderealign)  
string representing the method for aligning or placing the electrodes 'interactive' realign manually using a graphical user interface 'fiducial' realign using three fiducials (e.g. NAS, LPA and RPA) 'template' realign the electrodes to match a template set 'headshape' realign the electrodes to fit the head surface 'project' projects electrodes onto the head surface 'moveinward' moves electrodes inward along their normals

**cfg.method** - [ft_detect_movement](/reference/ft_detect_movement)  
string representing the method for movement detection 'velocity2D' detects microsaccades using the 2D velocity 'clustering' use unsupervised clustering method to detect microsaccades

**cfg.method** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
string representing the method for placing the electrodes 'volume' interactively locate electrodes on three orthogonal slices of a volumetric MRI or CT scan 'headshape' interactively locate electrodes on a head surface '1020' automatically locate electrodes on a head surface according to the 10-20 system 'shaft' automatically locate electrodes along a linear sEEG shaft 'grid' automatically locate electrodes on a MxN ECoG grid

**cfg.method** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
string that specifies the forward solution, see below

**cfg.method** - [ft_spikedetection](/reference/ft_spikedetection)  
string with the method to use, can be 'all', 'zthresh', 'ztrig', 'flank'

**cfg.method** - [ft_volumereslice](/reference/ft_volumereslice)  
string, 'flip', 'nearest', 'linear', 'cubic' or 'spline' (default = 'linear')

**cfg.method** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
string, 'mlr', 'cca', 'pls', 'svd', option specifying the criterion for the regression (default = 'mlr')

**cfg.method** - [ft_nirs_referencechannelsubtraction](/reference/ft_nirs_referencechannelsubtraction)  
string, 'regstat2', 'QR' or 'OLS' (default = 'QR')

**cfg.method** - [ft_spiketriggeredinterpolation](/reference/ft_spiketriggeredinterpolation)  
string, The interpolation method can be 'nan', 'cubic', 'linear', 'nearest', spline', 'pchip' (default = 'nan'). See INTERP1 for more details.

**cfg.method** - [ft_connectivityanalysis](/reference/ft_connectivityanalysis)  
string, can be 'amplcorr', amplitude correlation, support for freq and source data 'coh', coherence, support for freq, freqmvar and source data. For partial coherence also specify cfg.partchannel, see below. For imaginary part of coherency or coherency also specify cfg.complex, see below. 'csd', cross-spectral density matrix, can also calculate partial csds - if cfg.partchannel is specified, support for freq and freqmvar data 'dtf', directed transfer function, support for freq and freqmvar data 'granger', granger causality, support for freq and freqmvar data 'pdc', partial directed coherence, support for freq and freqmvar data 'plv', phase-locking value, support for freq and freqmvar data 'powcorr', power correlation, support for freq and source data 'powcorr_ortho', power correlation with single trial orthogonalisation, support for source data 'ppc' pairwise phase consistency 'psi', phaseslope index, support for freq and freqmvar data 'wpli', weighted phase lag index (signed one, still have to take absolute value to get indication of strength of interaction. Note: measure has positive bias. Use wpli_debiased to avoid this. 'wpli_debiased' debiased weighted phase lag index (estimates squared wpli) 'wppc' weighted pairwise phase consistency 'corr' Pearson correlation, support for timelock or raw data

**cfg.method** - [ft_crossfrequencyanalysis](/reference/ft_crossfrequencyanalysis)  
string, can be 'coh' - coherence 'plv' - phase locking value 'mvl' - mean vector length 'mi' - modulation index

**cfg.method** - [ft_meshrealign](/reference/ft_meshrealign)  
string, can be 'interactive' or fiducial' (default = 'interactive')

**cfg.method** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
string, can be 'interactive', 'projectmesh', 'iso2mesh', 'isosurface', 'headshape', 'hexahedral', 'tetrahedral','cortexhull', 'fittemplate'

**cfg.method** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
string, can be 'linear_mix', 'mvnrnd', 'ar', 'ar_reverse' (see below)

**cfg.method** - [ft_rejectvisual](/reference/ft_rejectvisual)  
string, describes how the data should be shown, this can be 'summary' show a single number for each channel and trial (default) 'channel' show the data per channel, all trials at once 'trial' show the data per trial, all channels at once

**cfg.method** - [ft_globalmeanfield](/reference/ft_globalmeanfield)  
string, determines whether the amplitude or power should be calculated (see below, default is 'amplitude', can be 'power')

**cfg.method** - [ft_interpolatenan](/reference/ft_interpolatenan)  
string, interpolation method, see HELP INTERP1 (default = 'linear')

**cfg.method** - [ft_sourceparcellate](/reference/ft_sourceparcellate)  
string, method to combine the values, see below (default = 'mean')

**cfg.method** - [ft_networkanalysis](/reference/ft_networkanalysis)  
string, specifying the graph measure that will be computed. See below for the list of supported measures.

**cfg.method** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
the name of the toolbox containing the function for the actual computation of the ar-coefficients this can be 'biosig' (default) or 'bsmart' you should have a copy of the specified toolbox in order to use mvaranalysis (both can be downloaded directly).

**cfg.metric** - [ft_rejectvisual](/reference/ft_rejectvisual)  
string, describes the metric that should be computed in summary mode for each channel in each trial, can be 'var' variance within each channel (default) 'min' minimum value in each channel 'max' maximum value each channel 'maxabs' maximum absolute value in each channel 'range' range from min to max in each channel 'kurtosis' kurtosis, i.e. measure of peakedness of the amplitude distribution 'zvalue' mean and std computed over all time and trials, per channel

**cfg.minblocksize** - [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
number, in seconds (default = 0)

**cfg.minlength** - [ft_redefinetrial](/reference/ft_redefinetrial)  
length in seconds, can be 'maxperlen' (default = [])

**cfg.minqueryrange** - [ft_volumelookup](/reference/ft_volumelookup), [ft_volumelookup](/reference/ft_volumelookup)  
number, should be odd and <= to maxqueryrange (default = 1)

**cfg.minspace** - [ft_sourceplot](/reference/ft_sourceplot)  
scalar, minimum spacing between slices if nslices>1 (default = 1)

**cfg.missingchannel** - [ft_channelrepair](/reference/ft_channelrepair)  
cell-array, see FT_CHANNELSELECTION for details

**cfg.mix** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
matrix, [nsignal x number of unobserved signals] specifying the mixing from the unobserved signals to the observed signals, or = matrix, [nsignal x number of unobserved signals x number of samples] specifying the mixing from the unobserved signals to the observed signals which changes as a function of time within the trial = cell-arry, [1 x ntrials] with each cell a matrix as specified above, when a trial-specific mixing is required

**cfg.model** - [ft_dipolefitting](/reference/ft_dipolefitting)  
'moving' or 'regional'

**cfg.montage** - [ft_layoutplot](/reference/ft_layoutplot), [ft_prepare_layout](/reference/ft_prepare_layout)  
'no' or a montage structure (default = 'no')

**cfg.montage** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or a montage structure, see FT_APPLY_MONTAGE (default = 'no')

**cfg.moveinward** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
number, move dipoles inward to ensure a certain distance to the innermost surface of the source compartment (default = 0)

**cfg.moveinward** - [ft_electroderealign](/reference/ft_electroderealign)  
number, the distance that the electrode should be moved inward (negative numbers result in an outward move)

**cfg.moviefreq** - [ft_movieplotTFR](/reference/ft_movieplotTFR)  
number, movie frames are all time points at the fixed frequency moviefreq (default = []);

**cfg.movietime** - [ft_movieplotTFR](/reference/ft_movieplotTFR)  
number, movie frames are all frequencies at the fixed time movietime (default = []);

**cfg.mri** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
can be filename, MRI structure or segmented MRI structure

**cfg.mri** - [ft_prepare_layout](/reference/ft_prepare_layout)  
segmented anatomical MRI to be used for generating an outline, see FT_READ_MRI and FT_VOLUMESEGMENT for details

**cfg.mri** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
structure with anatomical MRI model or filename, see FT_READ_MRI

**cfg.mva** - [ft_statistics_crossvalidate](/reference/ft_statistics_crossvalidate)  
a multivariate analysis (default = {dml.standardizer dml.svm})

**cfg.mvarmethod** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
scalar (only required when cfg.method = 'biosig'). default is 2, relates to the algorithm used for the computation of the AR-coefficients by mvar.m

**cfg.mvpa** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
structure that contains detailed options for the MVPA procedure. See https://github.com/treder/MVPA-Light for more details.

**cfg.mvpa.balance** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
string, for imbalanced data that does not have the same number of instances in each class 'oversample' oversamples the minority classes 'undersample' undersamples the minority classes such that all classes have the same number of instances. Note that undersampling is at the level of the repeats, whereas we oversampling occurs within each training set (for an explanation see mv_balance_classes). You can also give an integer number for undersampling. The samples will be reduced to this number. Note that concurrent over/undersampling (oversampling of the smaller class, undersampling of the larger class) is not supported at the moment

**cfg.mvpa.classifier** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
'lda' Regularised linear discriminant analysis (LDA) (for two classes) 'multiclass_lda' LDA for more than two classes 'logreg' Logistic regression 'svm' Support Vector Machine (SVM) 'ensemble' Ensemble of classifiers. Any of the other classifiers can be used as a learner. 'kernel_fda' Kernel Fisher Discriminant Analysis

**cfg.mvpa.cv** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
string, cross-validation type, either 'kfold', 'leaveout' or 'holdout'. If 'none', no cross-validation is used and the classifier is tested on the training set. (default 'kfold')

**cfg.mvpa.feedback** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
'yes' or 'no', whether or not to print feedback on the console (default 'yes')

**cfg.mvpa.k** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
number of folds in k-fold cross-validation (default 5)

**cfg.mvpa.metric** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
string, performance metric. Possible metrics: accuracy auc tval dval confusion precision recall f1 See https://github.com/treder/MVPA-Light for an overview of all classifiers and metrics.

**cfg.mvpa.normalise** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
string, normalises the data across samples, for each time point and each feature separately, using 'zscore' or 'demean' (default 'zscore'). Set to 'none' or [] to avoid normalisation.

**cfg.mvpa.p** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
if cfg.cv is 'holdout', p is the fraction of test samples (default 0.1)

**cfg.mvpa.param** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
struct, structure with hyperparameters for the classifier (see HYPERPARAMETERS below)

**cfg.mvpa.repeat** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
number of times the cross-validation is repeated with new randomly assigned folds (default 5)

**cfg.mvpa.replace** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
bool, if balance is set to 'oversample' or 'undersample', replace determines whether data is drawn with replacement (default 1)

**cfg.mvpa.stratify** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
if 1, the class proportions are approximately preserved in each test fold (default 1)

**cfg.mychan** - [ft_databrowser](/reference/ft_databrowser)  
Nx1 cell-array with selection of channels

**cfg.mychanscale** - [ft_databrowser](/reference/ft_databrowser)  
number, scaling to apply to the channels specified in cfg.mychan

## N 

**cfg.n1.ampl** - [ft_freqsimulation](/reference/ft_freqsimulation)  
root-mean-square amplitude of wide-band signal prior to filtering

**cfg.n1.bpfreq** - [ft_freqsimulation](/reference/ft_freqsimulation)  
[Flow Fhigh]

**cfg.n2.ampl** - [ft_freqsimulation](/reference/ft_freqsimulation)  
root-mean-square amplitude of wide-band signal prior to filtering

**cfg.n2.bpfreq** - [ft_freqsimulation](/reference/ft_freqsimulation)  
[Flow Fhigh]

**cfg.name** - [ft_volumenormalise](/reference/ft_volumenormalise), [ft_volumesegment](/reference/ft_volumesegment)  
string for output filename

**cfg.nbits** - [ft_realtime_pooraudioproxy](/reference/ft_realtime_pooraudioproxy)  
recording depth in bits (default = 16)

**cfg.nearestto** - [ft_recodeevent](/reference/ft_recodeevent)  
'trialzero' compare with time t=0 for each trial (default) 'trialbegin' compare with the begin of each trial 'trialend' compare with the end of each trial

**cfg.neighbourdist** - [ft_prepare_neighbours](/reference/ft_prepare_neighbours)  
number, maximum distance between neighbouring sensors (only for 'distance')

**cfg.neighbours** - [ft_freqstatistics](/reference/ft_freqstatistics), [ft_megplanar](/reference/ft_megplanar), [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity), [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
neighbourhood structure, see FT_PREPARE_NEIGHBOURS

**cfg.neighbours** - [ft_neighbourplot](/reference/ft_neighbourplot)  
neighbourhood structure, see FT_PREPARE_NEIGHBOURS (optional)

**cfg.neighbours** - [ft_channelrepair](/reference/ft_channelrepair)  
neighbourhood structure, see also FT_PREPARE_NEIGHBOURS

**cfg.neighbours** - [ft_rejectvisual](/reference/ft_rejectvisual)  
neighbourhood structure, see also FT_PREPARE_NEIGHBOURS (required for repairing channels)

**cfg.nfold** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
scalar, indicating the number of test folds to use in a cross-validation scheme

**cfg.nfolds** - [ft_statistics_crossvalidate](/reference/ft_statistics_crossvalidate)  
number of cross-validation folds (default = 5)

**cfg.noise.ampl** - [ft_freqsimulation](/reference/ft_freqsimulation)  
amplitude of noise

**cfg.noise.ampl** - [ft_timelocksimulation](/reference/ft_timelocksimulation)  
number (default = 0.1)

**cfg.noisecov** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
matrix, [nsignal x nsignal] specifying the covariance matrix of the innovation process

**cfg.nonlinear** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
'no' (or 'yes'), use non-linear normalization

**cfg.nonlinear** - [ft_volumenormalise](/reference/ft_volumenormalise)  
'yes' (default) or 'no', estimates a nonlinear transformation in addition to the linear affine registration. If a reasonably accurate normalisation is sufficient, a purely linearly transformed image allows for 'reverse-normalisation', which might come in handy when for example a region of interest is defined on the normalised group-average.

**cfg.nonlinear** - [ft_dipolefitting](/reference/ft_dipolefitting)  
'yes' or 'no', perform nonlinear search for optimal dipole parameters (default = 'yes')

**cfg.normalization** - [ft_spike_jpsth](/reference/ft_spike_jpsth)  
'no' (default), or 'yes'. If requested, the joint psth is normalized as in van Aertsen et al. (1989).

**cfg.normalize** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes' (default = 'no')

**cfg.normalize** - [ft_spike_waveform](/reference/ft_spike_waveform)  
'yes' (default) or 'no': normalizes all waveforms to have peak-to-through amp of 2

**cfg.normalize** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
'yes' or 'no' (default = 'no')

**cfg.normalize** - [ft_regressconfound](/reference/ft_regressconfound)  
string, 'yes' or 'no', normalization to make the confounds orthogonal (default = 'yes')

**cfg.normalizeparam** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
depth normalization parameter (default = 0.5)

**cfg.normalizevar** - [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)  
'N' or 'N-1' (default = 'N-1')

**cfg.npackets** - [ft_realtime_packettimer](/reference/ft_realtime_packettimer)  
the number of packets shown in one plot (default=1000) after reaching the end

**cfg.nr_bins** - [ft_nonlinearassociation](/reference/ft_nonlinearassociation)  
7

**cfg.nsignal** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
scalar, number of signals

**cfg.nslices** - [ft_sliceinterp](/reference/ft_sliceinterp)  
integer value, default is 20

**cfg.nslices** - [ft_sourceplot](/reference/ft_sourceplot)  
number of slices, (default = 20)

**cfg.nslices** - [ft_sourceplot](/reference/ft_sourceplot)  
scalar, number of slices to plot if 'slicepos' = 'auto (default = 1)

**cfg.ntrials** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
integer N, number of trials (default = 320)

**cfg.ntrials** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
number of trials

**cfg.ntrials** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
scalar, number of trials

**cfg.numDummy** - [ft_omri_pipeline](/reference/ft_omri_pipeline)  
how many scans to ignore initially (default 0)

**cfg.numDummy** - [ft_omri_pipeline_nuisance](/reference/ft_omri_pipeline_nuisance)  
how many scans to ignore initially (default 4)

**cfg.numDummy** - [ft_omri_quality](/reference/ft_omri_quality)  
how many scans to ignore initially (default=0)

**cfg.numRegr** - [ft_omri_pipeline_nuisance](/reference/ft_omri_pipeline_nuisance)  
number of nuisance regressors (1=constant term, 2=const+linear,5=const,linear+translation)

**cfg.numbin** - [ft_stratify](/reference/ft_stratify)  
10

**cfg.numbootstrap** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
number of bootstrap replications (e.g. number of original trials)

**cfg.numchans** - [ft_spikefixdmafile](/reference/ft_spikefixdmafile)  
number of channels (default = 256)

**cfg.numclusters** - [ft_headmovement](/reference/ft_headmovement)  
number of segments with constant headposition in which to split the data (default = 10). This argument is used in some of the methods only (see below), and is used in a kmeans clustering scheme.

**cfg.numcomponent** - [ft_componentanalysis](/reference/ft_componentanalysis)  
'all' or number (default = 'all')

**cfg.numdipoles** - [ft_dipolefitting](/reference/ft_dipolefitting)  
number, default is 1

**cfg.numiter** - [ft_stratify](/reference/ft_stratify)  
2000

**cfg.numpermutation** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
number, e.g. 500 or 'all'

**cfg.numrandomization** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
number of randomizations, can be 'all'

**cfg.numrandomization** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
number, e.g. 500

**cfg.numtrl** - [ft_freqsimulation](/reference/ft_freqsimulation)  
number of simulated trials

**cfg.numtrl** - [ft_timelocksimulation](/reference/ft_timelocksimulation)  
number of simulated trials (default = 10)

**cfg.numvertices** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
[800, 1600, 2400]; bnd = ft_prepare_mesh(cfg, segmentation);

**cfg.numvertices** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
numeric vector, should have same number of elements as cfg.tissue

## O 

**cfg.offset** - [ft_nonlinearassociation](/reference/ft_nonlinearassociation)  
0

**cfg.offset** - [ft_realtime_synchronous](/reference/ft_realtime_synchronous)  
offset relative to the trigger (default = 0)

**cfg.offset** - [ft_redefinetrial](/reference/ft_redefinetrial)  
single number or Nx1 vector, expressed in samples relative to current t=0

**cfg.opacitylim** - [ft_sourceplot](/reference/ft_sourceplot)  
range of mask values to which opacitymap is scaled (default = 'auto') [min max] 'maxabs', from -max(abs(maskparameter)) to +max(abs(maskparameter)) 'zeromax', from 0 to max(abs(maskparameter)) 'minzero', from min(abs(maskparameter)) to 0 'auto', if maskparameter values are all positive: 'zeromax', all negative: 'minzero', both positive and negative: 'maxabs'

**cfg.opacitymap** - [ft_sourceplot](/reference/ft_sourceplot)  
opacitymap for mask data, see ALPHAMAP (default = 'auto') 'auto', depends structure maskparameter, or on opacitylim - maskparameter: only positive values, or opacitylim:'zeromax' -> 'rampup' - maskparameter: only negative values, or opacitylim:'minzero' -> 'rampdown' - maskparameter: both pos and neg values, or opacitylim:'maxabs' -> 'vdown' - opacitylim: [min max] if min & max pos-> 'rampup', neg-> 'rampdown', both-> 'vdown' - NB. to use p-values use 'rampdown' to get lowest p-values opaque and highest transparent

**cfg.openmeeg.batchsize** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
scalar (default 100e3), number of dipoles for which the leadfield is computed in a single call to the low-level code. Trades off memory efficiency for speed.

**cfg.openmeeg.dsm** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
'no'/'yes', reuse existing DSM if provided

**cfg.openmeeg.keepdsm** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
'no'/'yes', option to retain DSM (no by default)

**cfg.openmeeg.nonadaptive** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
'no'/'yes'

**cfg.operation** - [ft_math](/reference/ft_math)  
string, can be 'add', 'subtract', 'divide', 'multiply', 'log10', 'abs'

**cfg.operation** - [ft_math](/reference/ft_math)  
string, for example '(x1-x2)/(x1+x2)' or 'x1/6'

**cfg.option1** - [ft_examplefunction](/reference/ft_examplefunction)  
value, explain the value here (default = something)

**cfg.option2** - [ft_examplefunction](/reference/ft_examplefunction)  
value, describe the value here and if needed continue here to allow automatic parsing of the help

**cfg.option3** - [ft_examplefunction](/reference/ft_examplefunction)  
value, explain it here (default is automatic)

**cfg.opto** - [ft_prepare_layout](/reference/ft_prepare_layout)  
sstructure with optode definition or filename, see FT_READ_SENS

**cfg.opto** - [ft_neighbourplot](/reference/ft_neighbourplot)  
structure with gradiometer definition or filename, see FT_READ_SENS

**cfg.opto** - [ft_layoutplot](/reference/ft_layoutplot)  
structure with optode definition or filename, see FT_READ_SENS

**cfg.opto** - [ft_channelrepair](/reference/ft_channelrepair)  
structure with optode definition, see FT_READ_SENS

**cfg.opts** - [ft_volumesegment](/reference/ft_volumesegment)  
struct, containing spm-version specific options. See the code and/or the SPM-documentation for more detail.

**cfg.opts** - [ft_volumebiascorrect](/reference/ft_volumebiascorrect)  
struct, containing spmversion specific options. See the code below and the SPM-documentation for more information.

**cfg.order** - [ft_nonlinearassociation](/reference/ft_nonlinearassociation)  
'Hxy'

**cfg.order** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel), [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
(optional)

**cfg.order** - [ft_realtime_downsample](/reference/ft_realtime_downsample)  
interger, order of butterworth lowpass filter (default = 4)

**cfg.order** - [ft_channelrepair](/reference/ft_channelrepair)  
order of the polynomial interpolation (default = 4, not for method 'distance')

**cfg.order** - [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity)  
order of the splines (default = 4)

**cfg.order** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
scalar, order of the autoregressive model (default=10)

**cfg.ori** - [ft_sourceplot](/reference/ft_sourceplot)  
'x', 'y', or 'z', specifies the orthogonal plane which will be plotted (default = 'y')

**cfg.ostream** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous), [ft_realtime_synchronous](/reference/ft_realtime_synchronous)  
the output stream that is used to send a command via write_event (default = []

**cfg.outline** - [ft_prepare_layout](/reference/ft_prepare_layout)  
string, how to create the outline, can be 'circle', 'square', 'convex', 'headshape', 'mri' or 'no' (default is automatic)

**cfg.output** - [ft_recodeevent](/reference/ft_recodeevent)  
'event' the event itself 'eventvalue' the value of the event 'eventnumber' the number of the event 'samplenumber' the sample at which the event is located 'samplefromoffset' number of samples from t=0 (c.f. response time) 'samplefrombegin' number of samples from the begin of the trial 'samplefromend' number of samples from the end of the trial

**cfg.output** - [ft_freqanalysis](/reference/ft_freqanalysis)  
'pow' return the power-spectra 'powandcsd' return the power and the cross-spectra 'fourier' return the complex Fourier-spectra

**cfg.output** - [ft_regressconfound](/reference/ft_regressconfound)  
'residual' (default), 'beta', or 'model'. If 'residual' is specified, the output is a data structure containing the residuals after regressing out the in cfg.reject listed confounds. If 'beta' or 'model' is specified, the output is a data structure containing the regression weights or the model, respectively.

**cfg.output** - [ft_volumelookup](/reference/ft_volumelookup)  
'single' always outputs one label; if several POI are provided, they are considered together as describing a ROI (default) 'multiple' outputs one label per POI (e.g., choose to get labels for different electrodes)

**cfg.output** - [ft_volumesegment](/reference/ft_volumesegment)  
'skullstrip'; segmented = ft_volumesegment(cfg, mri) will generate a skull-stripped anatomy based on a brainmask generated from the probabilistic tissue maps. The skull-stripped anatomy is stored in the field segmented.anatomy.

**cfg.output** - [ft_prepare_layout](/reference/ft_prepare_layout)  
filename (ending in .mat or .lay) to which the layout will be written (default = [])

**cfg.output** - [ft_layoutplot](/reference/ft_layoutplot)  
filename to which the layout will be written (default = [])

**cfg.output** - [ft_volumesegment](/reference/ft_volumesegment)  
string or cell-array of strings, see below (default = 'tpm')

**cfg.output** - [ft_spikefixdmafile](/reference/ft_spikefixdmafile)  
string with the name of the DMA log file, (default is determined automatic)

**cfg.output** - [ft_spikesplitting](/reference/ft_spikesplitting)  
string with the name of the splitted DMA dataset directory, (default is determined automatic)

**cfg.output** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
string with the output dataset (default is determined automatic)

**cfg.output** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
string, 'model' or 'residual' (defaul = 'model'), specifies what is outputed in .trial field in <dataout>

**cfg.output** - [ft_omri_pipeline](/reference/ft_omri_pipeline), [ft_omri_pipeline_nuisance](/reference/ft_omri_pipeline_nuisance)  
where to write processed scans to (default 'buffer://localhost:1973')

**cfg.output** - [ft_freqsimulation](/reference/ft_freqsimulation)  
which channels should be in the output data, can be 'mixed' or 'all' (default = 'all')

**cfg.output** - [ft_volumesegment](/reference/ft_volumesegment)  
{'brain' 'scalp' 'skull'}; segmented = ft_volumesegment(cfg, mri) will produce a volume with 3 binary masks, representing the brain surface, scalp surface, and skull which do not overlap.

**cfg.output** - [ft_volumesegment](/reference/ft_volumesegment)  
{'brain'}; segment_brain = ft_volumesegment(cfg, segment_tpm);

**cfg.output** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
{'scalp', 'skull', 'brain'}; segmentation = ft_volumesegment(cfg, mri);

**cfg.output** - [ft_volumesegment](/reference/ft_volumesegment)  
{'scalp'}; segmented = ft_volumesegment(cfg, mri) will produce a volume with a binary mask (based on the anatomy), representing the border of the scalp surface (i.e., everything inside the surface is also included). Such representation of the scalp is produced faster, because it doesn't require to create the tissue probabilty maps before creating the mask.

**cfg.output** - [ft_volumesegment](/reference/ft_volumesegment)  
{'tpm'}; segment_tpm = ft_volumesegment(cfg, mri);

**cfg.outputfile** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel), [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
(required) string, filename prefix for the output files

**cfg.outputfile** - [ft_annotate](/reference/ft_annotate), [ft_anonymizedata](/reference/ft_anonymizedata), [ft_appenddata](/reference/ft_appenddata), [ft_appendfreq](/reference/ft_appendfreq), [ft_channelnormalise](/reference/ft_channelnormalise), [ft_channelrepair](/reference/ft_channelrepair), [ft_combineplanar](/reference/ft_combineplanar), [ft_componentanalysis](/reference/ft_componentanalysis), [ft_connectivityanalysis](/reference/ft_connectivityanalysis), [ft_denoise_synthetic](/reference/ft_denoise_synthetic), [ft_detect_movement](/reference/ft_detect_movement), [ft_dipolefitting](/reference/ft_dipolefitting), [ft_examplefunction](/reference/ft_examplefunction), [ft_freqanalysis](/reference/ft_freqanalysis), [ft_freqanalysis_mvar](/reference/ft_freqanalysis_mvar), [ft_freqdescriptives](/reference/ft_freqdescriptives), [ft_freqgrandaverage](/reference/ft_freqgrandaverage), [ft_freqinterpolate](/reference/ft_freqinterpolate), [ft_freqstatistics](/reference/ft_freqstatistics), [ft_globalmeanfield](/reference/ft_globalmeanfield), [ft_interpolatenan](/reference/ft_interpolatenan), [ft_lateralizedpotential](/reference/ft_lateralizedpotential), [ft_math](/reference/ft_math), [ft_megplanar](/reference/ft_megplanar), [ft_megrealign](/reference/ft_megrealign), [ft_meshrealign](/reference/ft_meshrealign), [ft_mvaranalysis](/reference/ft_mvaranalysis), [ft_nirs_referencechannelsubtraction](/reference/ft_nirs_referencechannelsubtraction), [ft_nirs_scalpcouplingindex](/reference/ft_nirs_scalpcouplingindex), [ft_prepare_mesh](/reference/ft_prepare_mesh), [ft_preprocessing](/reference/ft_preprocessing), [ft_redefinetrial](/reference/ft_redefinetrial), [ft_regressconfound](/reference/ft_regressconfound), [ft_rejectcomponent](/reference/ft_rejectcomponent), [ft_rejectvisual](/reference/ft_rejectvisual), [ft_removetemplateartifact](/reference/ft_removetemplateartifact), [ft_resampledata](/reference/ft_resampledata), [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity), [ft_sourceanalysis](/reference/ft_sourceanalysis), [ft_sourcedescriptives](/reference/ft_sourcedescriptives), [ft_sourcegrandaverage](/reference/ft_sourcegrandaverage), [ft_sourceinterpolate](/reference/ft_sourceinterpolate), [ft_timelockanalysis](/reference/ft_timelockanalysis), [ft_timelockbaseline](/reference/ft_timelockbaseline), [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage), [ft_timelockstatistics](/reference/ft_timelockstatistics), [ft_volumedownsample](/reference/ft_volumedownsample), [ft_volumenormalise](/reference/ft_volumenormalise), [ft_volumerealign](/reference/ft_volumerealign), [ft_volumereslice](/reference/ft_volumereslice), [ft_volumesegment](/reference/ft_volumesegment)  
...

**cfg.outputfile** - [ft_icabrowser](/reference/ft_icabrowser)  
MAT file which contains indices of all components to reject

**cfg.outputunit** - [ft_spike_psth](/reference/ft_spike_psth)  
'rate' (default) or 'spikecount' or 'proportion'. If 'rate', we convert the output per trial to firing rates (spikes/sec). If 'spikecount', we count the number spikes per trial. If 'proportion', we normalize the area under the PSTH to 1.

**cfg.outputunit** - [ft_spike_rate](/reference/ft_spike_rate)  
'rate' (default) or 'spikecount'. If 'rate', we convert the output per trial to firing rates (spikes/sec). If 'spikecount', we count the number spikes per trial.

**cfg.outputunit** - [ft_spikedensity](/reference/ft_spikedensity)  
'rate' (default) or 'spikecount'. This determines the physical unit of our spikedensityfunction, either in firing rate or in spikecount.

**cfg.outputunit** - [ft_spike_isi](/reference/ft_spike_isi)  
'spikecount' (default) or 'proportion' (sum of all bins = 1).

**cfg.outputunit** - [ft_spike_xcorr](/reference/ft_spike_xcorr)  
- 'proportion' (value in each bin indicates proportion of occurence) - 'center' (values are scaled to center value which is set to 1) - 'raw' (default) unnormalized crosscorrelogram.

**cfg.overlap** - [ft_realtime_topography](/reference/ft_realtime_topography)  
0.25;

**cfg.overlap** - [ft_realtime_topography](/reference/ft_realtime_topography)  
number, amojunt of overlap between chunks (default = 0 seconds)

**cfg.overlap** - [ft_realtime_asynchronous](/reference/ft_realtime_asynchronous)  
overlap between blocks in seconds (default = 0)

**cfg.overlap** - [ft_redefinetrial](/reference/ft_redefinetrial)  
single number (between 0 and 1 (exclusive)) specifying the fraction of overlap between snippets (0 = no overlap)

**cfg.overlap** - [ft_prepare_layout](/reference/ft_prepare_layout)  
string, how to deal with overlapping channels when the layout is constructed from a sensor configuration structure. This can be 'shift' - shift the positions in 2D space to remove the overlap (default) 'keep' - do not shift, retain the overlap 'no' - throw an error when overlap is present

## P 

**cfg.pad** - [ft_freqanalysis](/reference/ft_freqanalysis)  
number, 'nextpow2', or 'maxperlen' (default), length in seconds to which the data can be padded out. The padding will determine your spectral resolution. If you want to compare spectra from data pieces of different lengths, you should use the same cfg.pad for both, in order to spectrally interpolate them to the same spectral resolution. The new option 'nextpow2' rounds the maximum trial length up to the next power of 2. By using that amount of padding, the FFT can be computed more efficiently in case 'maxperlen' has a large prime factor sum.

**cfg.padding** - [ft_preprocessing](/reference/ft_preprocessing)  
length (in seconds) to which the trials are padded for filtering (default = 0)

**cfg.padtype** - [ft_freqanalysis](/reference/ft_freqanalysis)  
string, type of padding (default 'zero', see ft_preproc_padding)

**cfg.padtype** - [ft_preprocessing](/reference/ft_preprocessing)  
string, type of padding (default: 'data' padding or 'mirror', depending on feasibility)

**cfg.pairmethod** - [ft_electroderealign](/reference/ft_electroderealign)  
'pos' (default) or 'label', the method for electrode pairing on which the deformation energy is based

**cfg.pairtrials** - [ft_stratify](/reference/ft_stratify)  
'spikesort', 'linkage' or 'no' (default = 'spikesort')

**cfg.param** - [ft_spike_isi](/reference/ft_spike_isi)  
string, one of 'gamfit' : returns [shape scale] for gamma distribution fit 'coeffvar' : coefficient of variation (sd / mean) 'lv' : Shinomoto's Local Variation measure (2009)

**cfg.parameter** - [ft_volumerealign](/reference/ft_volumerealign)  
'anatomy' the parameter which is used for the visualization

**cfg.parameter** - [ft_sourceparcellate](/reference/ft_sourceparcellate)  
cell-array with strings, fields that should be parcellated (default = 'all')

**cfg.parameter** - [ft_volumenormalise](/reference/ft_volumenormalise)  
cell-array with the functional data to be normalised (default = 'all')

**cfg.parameter** - [ft_timelockbaseline](/reference/ft_timelockbaseline)  
field for which to apply baseline normalization, or cell-array of strings to specify multiple fields to normalize (default = 'avg')

**cfg.parameter** - [ft_freqbaseline](/reference/ft_freqbaseline)  
field for which to apply baseline normalization, or cell-array of strings to specify multiple fields to normalize (default = 'powspctrm')

**cfg.parameter** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
field that contains the data to be plotted as color, for example 'avg', 'powspctrm' or 'cohspctrm' (default is automatic)

**cfg.parameter** - [ft_singleplotER](/reference/ft_singleplotER)  
field to be plotted on y-axis (default depends on data.dimord) 'avg', 'powspctrm' or 'cohspctrm'

**cfg.parameter** - [ft_multiplotER](/reference/ft_multiplotER)  
field to be plotted on y-axis, for example 'avg', 'powspctrm' or 'cohspctrm' (default is automatic)

**cfg.parameter** - [ft_singleplotTFR](/reference/ft_singleplotTFR)  
field to be plotted on z-axis, e.g. 'powspcrtrm' (default depends on data.dimord)

**cfg.parameter** - [ft_multiplotTFR](/reference/ft_multiplotTFR)  
field to be represented as color (default depends on data.dimord) 'powspctrm' or 'cohspctrm'

**cfg.parameter** - [ft_freqstatistics](/reference/ft_freqstatistics)  
string (default = 'powspctrm')

**cfg.parameter** - [ft_timelockstatistics](/reference/ft_timelockstatistics)  
string (default = 'trial' or 'avg')

**cfg.parameter** - [ft_sourceinterpolate](/reference/ft_sourceinterpolate)  
string (or cell-array) of the parameter(s) to be interpolated

**cfg.parameter** - [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)  
string or cell-array indicating which parameter to average. default is set to 'avg', if it is present in the data.

**cfg.parameter** - [ft_freqgrandaverage](/reference/ft_freqgrandaverage)  
string or cell-array of strings indicating which parameter(s) to average. default is set to 'powspctrm', if it is present in the data.

**cfg.parameter** - [ft_networkanalysis](/reference/ft_networkanalysis)  
string specifying the bivariate parameter in the data for which the graph measure will be computed.

**cfg.parameter** - [ft_volumedownsample](/reference/ft_volumedownsample)  
string, data field to downsample (default = 'all')

**cfg.parameter** - [ft_volumewrite](/reference/ft_volumewrite)  
string, describing the functional data to be processed, e.g. 'pow', 'coh', 'nai' or 'anatomy'

**cfg.parameter** - [ft_sourcegrandaverage](/reference/ft_sourcegrandaverage), [ft_sourcestatistics](/reference/ft_sourcestatistics)  
string, describing the functional data to be processed, e.g. 'pow', 'nai' or 'coh'

**cfg.parameter** - [ft_math](/reference/ft_math)  
string, field from the input data on which the operation is performed, e.g. 'pow' or 'avg'

**cfg.parameter** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
string, field in data (default = 'anatomy' if present in data)

**cfg.parameter** - [ft_sourcewrite](/reference/ft_sourcewrite)  
string, functional parameter to be written to file

**cfg.parameter** - [ft_movieplotER](/reference/ft_movieplotER), [ft_movieplotTFR](/reference/ft_movieplotTFR)  
string, parameter that is color coded (default = 'avg')

**cfg.parameter** - [ft_connectivityplot](/reference/ft_connectivityplot)  
string, the functional parameter to be plotted (default = 'cohspctrm')

**cfg.parameter** - [ft_appendfreq](/reference/ft_appendfreq)  
string, the name of the field to concatenate

**cfg.params** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
matrix, [nsignal x nsignal x number of lags] specifying the autoregressive coefficient parameters. A non-zero element at cfg.params(i,j,k) means a directional influence from signal j onto signal i (at lag k).

**cfg.parcellation** - [ft_sourceparcellate](/reference/ft_sourceparcellate)  
string, fieldname that contains the desired parcellation

**cfg.partchannel** - [ft_connectivityanalysis](/reference/ft_connectivityanalysis)  
cell-array containing a list of channels that need to be partialized out, support for method 'coh', 'csd', 'plv'

**cfg.path** - [ft_icabrowser](/reference/ft_icabrowser)  
where pdfs will be saves (default = pwd)

**cfg.peakseparation** - [ft_heartrate](/reference/ft_heartrate), [ft_respiration](/reference/ft_respiration)  
scalar, time in seconds

**cfg.perchannel** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
string, 'yes' or 'no', or logical, whether or not to perform estimation of beta weights separately per channel

**cfg.performance** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
string, 'Pearson' or 'r-squared' (default = 'Pearson'), indicating what performance metric is outputed in .weights(k).performance field of <dataout> for the k-th fold

**cfg.permutation** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes'

**cfg.pertrial** - [ft_denoise_pca](/reference/ft_denoise_pca)  
'no' (default) or 'yes'. Regress out the references on a per trial basis

**cfg.planarmethod** - [ft_megplanar](/reference/ft_megplanar)  
string, can be 'sincos', 'orig', 'fitplane', 'sourceproject' (default = 'sincos')

**cfg.ploteventlabels** - [ft_databrowser](/reference/ft_databrowser)  
'type=value', 'colorvalue' (default = 'type=value');

**cfg.plotevents** - [ft_databrowser](/reference/ft_databrowser)  
'no' or 'yes', whether to plot event markers. (default is 'yes')

**cfg.plotfiltresp** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or 'yes', plot filter responses (firws, default = 'no')

**cfg.plotfit** - [ft_spike_plot_isi](/reference/ft_spike_plot_isi)  
'yes' (default) or 'no'. This requires that when calling FT_SPIKESTATION_ISI, cfg.gammafit = 'yes'.

**cfg.plotlabels** - [ft_databrowser](/reference/ft_databrowser)  
'yes', 'no' or 'some', whether to plot channel labels in vertical viewmode. The option 'some' plots one label for every ten channels, which is useful if there are many channels. (default = 'yes')

**cfg.plotselection** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster)  
'yes' or 'no' (default). If yes plot Y axis only for selection in cfg.trials

**cfg.plotunit** - [ft_qualitycheck](/reference/ft_qualitycheck)  
scalar, the length of time to be plotted in one panel (default = 3600)

**cfg.point** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  


**cfg.polhemus** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
filename or mesh, description of the head shape recorded with the Polhemus (default is automatic)

**cfg.polyorder** - [ft_preprocessing](/reference/ft_preprocessing)  
polynome order for poly trend removal (default = 2; note that all lower-order trends will also be removed when using cfg.polyremoval)

**cfg.polyremoval** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or 'yes', remove higher order trend from the data (done per trial) (default = 'no')

**cfg.polyremoval** - [ft_freqanalysis](/reference/ft_freqanalysis)  
number (default = 0), specifying the order of the polynome which is fitted and subtracted from the time domain data prior to the spectral analysis. For example, a value of 1 corresponds to a linear trend. The default is a mean subtraction, thus a value of 0. If no removal is requested, specify -1. see FT_PREPROC_POLYREMOVAL for details

**cfg.port** - [ft_realtime_brainampproxy](/reference/ft_realtime_brainampproxy)  
number, TCP port to connect to (default = 51244)

**cfg.port** - [ft_realtime_jaga16proxy](/reference/ft_realtime_jaga16proxy)  
number, UDP port to listen on (default = 55000)

**cfg.position** - [ft_databrowser](/reference/ft_databrowser)  
location and size of the figure, specified as a vector of the form [left bottom width height].

**cfg.poststim** - [ft_artifact_tms](/reference/ft_artifact_tms)  
scalar, time in seconds post onset of detected even to mark as artifactual (default = 0.010 seconds)

**cfg.postwindow** - [ft_interpolatenan](/reference/ft_interpolatenan)  
value, length of data after interpolation window, in seconds (default = 1)

**cfg.powmethod** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'regular', 'lambda1', 'trace', 'none'

**cfg.powscale** - [ft_icabrowser](/reference/ft_icabrowser)  
scaling of y axis in power plot, 'lin' or 'log10', (default = 'log10')

**cfg.precision** - [ft_preprocessing](/reference/ft_preprocessing)  
'single' or 'double' (default = 'double')

**cfg.precision** - [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
numeric representation, can be double, single, int32, int16 (default = 'double')

**cfg.precision** - [ft_sourcewrite](/reference/ft_sourcewrite)  
string, can be 'single', 'double', etc.

**cfg.prefix** - [ft_icabrowser](/reference/ft_icabrowser)  
prefix of the pdf files (default = 'ICA')

**cfg.preproc.baselinewindow** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
[begin end] in seconds, the default is the complete trial

**cfg.preproc.baselinewindow** - [ft_databrowser](/reference/ft_databrowser)  
[begin end] in seconds, the default is the complete trial (default = 'all')

**cfg.preproc.boxcar** - [ft_rejectvisual](/reference/ft_rejectvisual)  
0.2

**cfg.preproc.bpfiltdir** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
filter direction, 'twopass' (default) or 'onepass'

**cfg.preproc.bpfilter** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
'no' or 'yes' bandpass filter

**cfg.preproc.bpfilter** - [ft_rejectvisual](/reference/ft_rejectvisual), [ft_rejectvisual](/reference/ft_rejectvisual)  
'yes'

**cfg.preproc.bpfilter** - [ft_heartrate](/reference/ft_heartrate)  
'yes' or 'no'

**cfg.preproc.bpfilter** - [ft_respiration](/reference/ft_respiration)  
'yes' or 'no' (default = 'yes')

**cfg.preproc.bpfiltord** - [ft_rejectvisual](/reference/ft_rejectvisual)  
4

**cfg.preproc.bpfiltord** - [ft_rejectvisual](/reference/ft_rejectvisual)  
8

**cfg.preproc.bpfiltord** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
bandpass filter order

**cfg.preproc.bpfilttype** - [ft_rejectvisual](/reference/ft_rejectvisual), [ft_rejectvisual](/reference/ft_rejectvisual)  
'but'

**cfg.preproc.bpfilttype** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
digital filter type, 'but' (default) or 'fir'

**cfg.preproc.bpfreq** - [ft_rejectvisual](/reference/ft_rejectvisual)  
[1 15]

**cfg.preproc.bpfreq** - [ft_rejectvisual](/reference/ft_rejectvisual)  
[110 140]

**cfg.preproc.bpfreq** - [ft_heartrate](/reference/ft_heartrate), [ft_respiration](/reference/ft_respiration)  
[low high], filter frequency in Hz

**cfg.preproc.bpfreq** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
bandpass frequency range, specified as [low high] in Hz

**cfg.preproc.demean** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
'no' or 'yes'

**cfg.preproc.demean** - [ft_databrowser](/reference/ft_databrowser)  
'no' or 'yes', whether to apply baseline correction (default = 'no')

**cfg.preproc.detrend** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
'no' or 'yes'

**cfg.preproc.detrend** - [ft_databrowser](/reference/ft_databrowser)  
'no' or 'yes', remove linear trend from the data (done per trial) (default = 'no')

**cfg.preproc.dftfilter** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
'no' or 'yes' line noise removal using discrete fourier transform

**cfg.preproc.hilbert** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
'no' or 'yes'

**cfg.preproc.hpfiltdir** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
filter direction, 'twopass' (default) or 'onepass'

**cfg.preproc.hpfilter** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
'no' or 'yes' highpass filter

**cfg.preproc.hpfiltord** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
highpass filter order

**cfg.preproc.hpfilttype** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
digital filter type, 'but' (default) or 'fir'

**cfg.preproc.hpfreq** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
highpass frequency in Hz

**cfg.preproc.lnfilter** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
'no' or 'yes' line noise removal using notch filter

**cfg.preproc.lnfiltord** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
line noise notch filter order

**cfg.preproc.lnfreq** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
line noise frequency in Hz, default 50Hz

**cfg.preproc.lpfiltdir** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
filter direction, 'twopass' (default) or 'onepass'

**cfg.preproc.lpfilter** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
'no' or 'yes' lowpass filter

**cfg.preproc.lpfilter** - [ft_databrowser](/reference/ft_databrowser)  
'no' or 'yes' lowpass filter (default = 'no')

**cfg.preproc.lpfiltord** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
lowpass filter order

**cfg.preproc.lpfilttype** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
digital filter type, 'but' (default) or 'fir'

**cfg.preproc.lpfreq** - [ft_databrowser](/reference/ft_databrowser), [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
lowpass frequency in Hz

**cfg.preproc.medianfilter** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
'no' or 'yes' jump preserving median filter

**cfg.preproc.medianfiltord** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
length of median filter

**cfg.preproc.rectify** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
'no' or 'yes'

**cfg.preproc.rectify** - [ft_rejectvisual](/reference/ft_rejectvisual), [ft_rejectvisual](/reference/ft_rejectvisual)  
'yes'

**cfg.prestim** - [ft_artifact_tms](/reference/ft_artifact_tms)  
scalar, time in seconds prior to onset of detected event to mark as artifactual (default = 0.005 seconds)

**cfg.prewindow** - [ft_interpolatenan](/reference/ft_interpolatenan)  
value, length of data prior to interpolation window, in seconds (default = 1)

**cfg.projcomb** - [ft_sourceplot](/reference/ft_sourceplot)  
'mean', 'max', method to combine the different projections

**cfg.projection** - [ft_prepare_layout](/reference/ft_prepare_layout)  
string, 2D projection method can be 'stereographic', 'orthographic', 'polar' or 'gnomic' (default = 'polar') When 'orthographic', cfg.viewpoint can be used to indicate to specificy projection (keep empty for legacy projection)

**cfg.projection** - [ft_layoutplot](/reference/ft_layoutplot)  
string, 2D projection method can be 'stereographic', 'ortographic', 'polar', 'gnomic' or 'inverse' (default = 'orthographic')

**cfg.projectmom** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'yes' or 'no' (default = 'no')

**cfg.projectnoise** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes'

**cfg.projmethod** - [ft_sourceplot](/reference/ft_sourceplot)  
projection method, how functional volume data is projected onto surface 'nearest', 'project', 'sphere_avg', 'sphere_weighteddistance'

**cfg.projthresh** - [ft_sourceplot](/reference/ft_sourceplot)  
implements thresholding on the surface level for example, 0.7 means 70% of maximum

**cfg.projvec** - [ft_sourceplot](/reference/ft_sourceplot)  
vector (in mm) to allow different projections that are combined with the method specified in cfg.projcomb

**cfg.projweight** - [ft_sourceplot](/reference/ft_sourceplot)  
vector of weights for the different projections (default = 1)

**cfg.pruneratio** - [ft_megplanar](/reference/ft_megplanar)  
for singular values, default is 1e-3

**cfg.pseudovalue** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes' pseudovalue resampling of trials

**cfg.psth** - [ft_spike_plot_jpsth](/reference/ft_spike_plot_jpsth)  
'yes' (default) or 'no'. Plot PSTH with JPSTH if 'yes';

## Q 

**cfg.querymethod** - [ft_volumelookup](/reference/ft_volumelookup)  
'sphere' searches voxels around the ROI in a sphere (default) = 'cube' searches voxels around the ROI in a cube

**cfg.queryrange** - [ft_sourceplot](/reference/ft_sourceplot)  
number, in atlas voxels (default 3)

## R 

**cfg.radius** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
(optional)

**cfg.radius** - [ft_sourceplot](/reference/ft_sourceplot)  
scalar, maximum radius of cloud (default = 4)

**cfg.randomization** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes'

**cfg.randomseed** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation), [ft_dipolesimulation](/reference/ft_dipolesimulation), [ft_freqsimulation](/reference/ft_freqsimulation)  
'yes' or a number or vector with the seed value (default = 'yes')

**cfg.randomseed** - [ft_componentanalysis](/reference/ft_componentanalysis)  
comp.cfg.callinfo.randomseed (from previous call)

**cfg.randomseed** - [ft_componentanalysis](/reference/ft_componentanalysis)  
integer seed value of user's choice

**cfg.randomseed** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
string, 'yes', 'no' or a number (default = 'yes')

**cfg.rawtrial** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no' or 'yes' construct filter from single trials, apply to single trials. Note that you also may want to set cfg.keeptrials='yes' to keep all trial information, especially if using in combination with sourcemodel.filter

**cfg.readevent** - [ft_realtime_signalviewer](/reference/ft_realtime_signalviewer)  
whether or not to copy events (default = 'no')

**cfg.readevent** - [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
whether or not to copy events (default = 'no'; event type can also be specified; e.g., 'UPPT002')

**cfg.rectify** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or 'yes' (default = 'no')

**cfg.reducerank** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_prepare_leadfield](/reference/ft_prepare_leadfield), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
'no', or number (default = 3 for EEG, 2 for MEG)

**cfg.refchan** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
reference channel label (for coherence)

**cfg.refchan** - [ft_realtime_coillocalizer](/reference/ft_realtime_coillocalizer)  
single string or cell-array with strings

**cfg.refchannel** - [ft_prepare_montage](/reference/ft_prepare_montage), [ft_preprocessing](/reference/ft_preprocessing)  
cell-array with new EEG reference channel(s), this can be 'all' for a common average reference

**cfg.refchannel** - [ft_multiplotER](/reference/ft_multiplotER), [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotER](/reference/ft_singleplotER), [ft_singleplotTFR](/reference/ft_singleplotTFR), [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
name of reference channel for visualising connectivity, can be 'gui'

**cfg.refchannel** - [ft_denoise_pca](/reference/ft_denoise_pca)  
the channels used as reference signal (default = 'MEGREF')

**cfg.refchannel** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
the channels used as reference signal (default = 'MEGREF'), see FT_SELECTDATA

**cfg.refdip** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
reference dipole location (for coherence)

**cfg.reflags** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
integer array, specifying temporal lags (in msec) by which to shift refchannel with respect to data channels

**cfg.refmethod** - [ft_prepare_montage](/reference/ft_prepare_montage)  
'avg', 'bioloar', 'comp' (default = 'avg')

**cfg.refmethod** - [ft_preprocessing](/reference/ft_preprocessing)  
'avg', 'median', or 'bipolar' for bipolar derivation of sequential channels (default = 'avg')

**cfg.rejcomp** - [ft_icabrowser](/reference/ft_icabrowser)  
list of components which shall be initially marked for rejection, e.g. [1 4 7]

**cfg.reject** - [ft_regressconfound](/reference/ft_regressconfound)  
vector, [1 X Nconfounds], listing the confounds that are to be rejected (default = 'all')

**cfg.rejectonpeak** - [ft_spike_waveform](/reference/ft_spike_waveform)  
'yes' (default) or 'no': takes away waveforms with too late peak, and no rising AP towards peak of other waveforms

**cfg.rellim** - [ft_realtime_packettimer](/reference/ft_realtime_packettimer)  
y limits of subplot 1 (default = [-100 100])

**cfg.relnoise** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
add noise with level relative to simulated signal

**cfg.remove** - [ft_analysispipeline](/reference/ft_analysispipeline)  
cell-array with strings, determines which objects will be removed from the configuration prior to writing it to file. For readibility of the script, you may want to remove the large objectssuch as event structure, trial definition, source positions

**cfg.removefield** - [ft_anonymizedata](/reference/ft_anonymizedata)  
cell-array with strings, fields to remove (default = {})

**cfg.removemean** - [ft_timelockanalysis](/reference/ft_timelockanalysis)  
'no' or 'yes' for covariance computation (default = 'yes')

**cfg.removemean** - [ft_connectivityanalysis](/reference/ft_connectivityanalysis)  
'yes' (default), or 'no', support for method 'powcorr' and 'amplcorr'.

**cfg.removevalue** - [ft_anonymizedata](/reference/ft_anonymizedata)  
cell-array with strings, values to remove (default = {})

**cfg.renderer** - [ft_sourceplot](/reference/ft_sourceplot)  
'painters', 'zbuffer', ' opengl' or 'none' (default = 'opengl') note that when using opacity the OpenGL renderer is required.

**cfg.renderer** - [ft_multiplotER](/reference/ft_multiplotER), [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotER](/reference/ft_singleplotER), [ft_singleplotTFR](/reference/ft_singleplotTFR)  
'painters', 'zbuffer', ' opengl' or 'none' (default = [])

**cfg.renderer** - [ft_databrowser](/reference/ft_databrowser)  
string, 'opengl', 'zbuffer', 'painters', see MATLAB Figure Properties. If this function crashes, you should try 'painters'.

**cfg.reproducescript** - [ft_reproducescript](/reference/ft_reproducescript)  
string, directory with the script and intermediate data

**cfg.reref** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or 'yes' (default = 'no')

**cfg.resample** - [ft_sliceinterp](/reference/ft_sliceinterp)  
integer value, default is 1 (for resolution reduction)

**cfg.resample** - [ft_statistics_crossvalidate](/reference/ft_statistics_crossvalidate)  
true/false; upsample less occurring classes during training and downsample often occurring classes during testing (default = false)

**cfg.resamplefs** - [ft_resampledata](/reference/ft_resampledata)  
frequency at which the data will be resampled (default = 256 Hz)

**cfg.resolution** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
number (e.g. 1 cm) for automatic grid generation

**cfg.resolution** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
number (e.g. 6) of the resolution of the template MNI grid, defined in mm

**cfg.resolution** - [ft_volumereslice](/reference/ft_volumereslice)  
number, in physical units

**cfg.resolutionmatrix** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'yes' or 'no' (default = 'no')

**cfg.roi** - [ft_volumelookup](/reference/ft_volumelookup), [ft_volumelookup](/reference/ft_volumelookup)  
Nx3 vector, coordinates of the POI

**cfg.roi** - [ft_sourceplot](/reference/ft_sourceplot)  
string or cell of strings, region(s) of interest from anatomical atlas (see cfg.atlas above) everything is masked except for ROI

**cfg.roi** - [ft_volumelookup](/reference/ft_volumelookup)  
string or cell-array of strings, ROI from anatomical atlas

**cfg.rotate** - [ft_sliceinterp](/reference/ft_sliceinterp)  
number of ccw 90 deg slice rotations (default = 0)

**cfg.rotate** - [ft_layoutplot](/reference/ft_layoutplot), [ft_prepare_layout](/reference/ft_prepare_layout)  
number, rotation around the z-axis in degrees (default = [], which means automatic)

**cfg.round2nearestvoxel** - [ft_volumelookup](/reference/ft_volumelookup)  
'yes' or 'no' (default = 'no'), voxel closest to point of interest is calculated and box/sphere is centered around coordinates of that voxel

**cfg.round2nearestvoxel** - [ft_volumelookup](/reference/ft_volumelookup)  
'yes' or 'no', voxel closest to POI is calculated (default = 'yes')

**cfg.rows** - [ft_prepare_layout](/reference/ft_prepare_layout)  
number of rows (default is automatic)

**cfg.runica.anneal** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.annealdeg** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.bias** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.block** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.extended** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.interput** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.logfile** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.lrate** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.maxsteps** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.momentum** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.pca** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.posact** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.specgram** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.sphering** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.stop** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.verbose** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.runica.weights** - [ft_componentanalysis](/reference/ft_componentanalysis)  


## S 

**cfg.s1.ampl** - [ft_freqsimulation](/reference/ft_freqsimulation)  
amplitude of signal 1

**cfg.s1.ampl** - [ft_timelocksimulation](/reference/ft_timelocksimulation)  
number (default = 1.0)

**cfg.s1.freq** - [ft_freqsimulation](/reference/ft_freqsimulation)  
frequency of signal 1

**cfg.s1.numcycli** - [ft_timelocksimulation](/reference/ft_timelocksimulation)  
number (default = 1)

**cfg.s1.phase** - [ft_freqsimulation](/reference/ft_freqsimulation)  
phase (in rad) relative to cosine of signal 1 (default depends on method) = number or 'random'

**cfg.s2.ampl** - [ft_freqsimulation](/reference/ft_freqsimulation)  
amplitude of signal 2

**cfg.s2.ampl** - [ft_timelocksimulation](/reference/ft_timelocksimulation)  
number (default = 0.7)

**cfg.s2.freq** - [ft_freqsimulation](/reference/ft_freqsimulation)  
frequency of signal 2

**cfg.s2.numcycli** - [ft_timelocksimulation](/reference/ft_timelocksimulation)  
number (default = 2)

**cfg.s2.phase** - [ft_freqsimulation](/reference/ft_freqsimulation)  
phase (in rad) relative to cosine of signal 1 (default depends on method) = number or 'random'

**cfg.s3.ampl** - [ft_freqsimulation](/reference/ft_freqsimulation)  
amplitude of signal 3

**cfg.s3.ampl** - [ft_timelocksimulation](/reference/ft_timelocksimulation)  
number (default = 0.2)

**cfg.s3.freq** - [ft_freqsimulation](/reference/ft_freqsimulation)  
frequency of signal 3

**cfg.s3.numcycli** - [ft_timelocksimulation](/reference/ft_timelocksimulation)  
number (default = 4)

**cfg.s3.phase** - [ft_freqsimulation](/reference/ft_freqsimulation)  
phase (in rad) relative to cosine of signal 1 (default depends on method) = number or 'random'

**cfg.s4.ampl** - [ft_freqsimulation](/reference/ft_freqsimulation)  
amplitude of signal 4

**cfg.s4.freq** - [ft_freqsimulation](/reference/ft_freqsimulation)  
frequency of signal 4

**cfg.s4.phase** - [ft_freqsimulation](/reference/ft_freqsimulation)  
phase (in rad) relative to cosine of signal 1 (default depends on method) = number or 'random'

**cfg.samperframe** - [ft_movieplotER](/reference/ft_movieplotER), [ft_movieplotTFR](/reference/ft_movieplotTFR)  
number, samples per fram (default = 1)

**cfg.sampleindex** - [ft_resampledata](/reference/ft_resampledata)  
'no' or 'yes', add a channel with the original sample indices (default = 'no')

**cfg.saveaspng** - [ft_clusterplot](/reference/ft_clusterplot)  
string, filename of the output figures (default = 'no')

**cfg.savemat** - [ft_qualitycheck](/reference/ft_qualitycheck)  
string, 'yes' or 'no' to save the analysis (default = 'yes')

**cfg.saveplot** - [ft_realtime_packettimer](/reference/ft_realtime_packettimer)  
if path is specified, first plot is saved (default=[]);

**cfg.saveplot** - [ft_qualitycheck](/reference/ft_qualitycheck)  
string, 'yes' or 'no' to save the visualization (default = 'yes')

**cfg.scalar** - [ft_math](/reference/ft_math)  
scalar value to be used in the operation

**cfg.scale** - [ft_defacemesh](/reference/ft_defacemesh), [ft_defacevolume](/reference/ft_defacevolume)  
initial size of the box along each dimension (default is automatic)

**cfg.scale** - [ft_channelnormalise](/reference/ft_channelnormalise)  
scalar value used for scaling (default = 1)

**cfg.scaling** - [ft_volumewrite](/reference/ft_volumewrite)  
'yes' or 'no'

**cfg.scalpsmooth** - [ft_volumesegment](/reference/ft_volumesegment)  
'no', or scalar, the FWHM of the gaussian kernel in voxels, (default = 5)

**cfg.scalpthreshold** - [ft_volumesegment](/reference/ft_volumesegment)  
'no', or scalar, relative threshold value which is used to threshold the anatomical data in order to create a volumetric scalpmask (see below), (default = 0.1)

**cfg.scatter** - [ft_spike_plot_isireturn](/reference/ft_spike_plot_isireturn)  
'yes' (default) or 'no'. If 'yes', we plot the individual values.

**cfg.searchlight** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
'yes' or 'no', performs searchlight analysis (default 'no'). More information see below

**cfg.searchrange** - [ft_recodeevent](/reference/ft_recodeevent)  
'anywhere' search anywhere for the event, (default) 'insidetrial' only search inside 'outsidetrial' only search outside 'beforetrial' only search before the trial 'aftertrial' only search after the trial 'beforezero' only search before time t=0 of each trial 'afterzero' only search after time t=0 of each trial

**cfg.selcfg** - [ft_databrowser](/reference/ft_databrowser)  
configuration options for function in cfg.selfun

**cfg.seldat** - [ft_databrowser](/reference/ft_databrowser)  
'selected' or 'all', specifies whether only the currently selected or all channels will be passed to the selfun (default = 'selected')

**cfg.selectfeature** - [ft_databrowser](/reference/ft_databrowser)  
string, name of feature to be selected/added (default = 'visual')

**cfg.selection** - [ft_defacemesh](/reference/ft_defacemesh), [ft_defacevolume](/reference/ft_defacevolume)  
which voxels to keep, can be 'inside' or 'outside' (default = 'outside')

**cfg.selectmode** - [ft_databrowser](/reference/ft_databrowser)  
'markartifact', 'markpeakevent', 'marktroughevent' (default = 'markartifact')

**cfg.selfun** - [ft_databrowser](/reference/ft_databrowser)  
string, name of function that is evaluated using the right-click context menu. The selected data and cfg.selcfg are passed on to this function.

**cfg.serial** - [ft_omri_quality](/reference/ft_omri_quality)  
serial port (default = /dev/ttyS0), set [] to disable motion reporting

**cfg.shading** - [ft_topoplotIC](/reference/ft_topoplotIC)  
'flat' 'interp' (default = 'flat')

**cfg.shading** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
'flat' or 'interp' (default = 'flat')

**cfg.shaft.along** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
1x3 or Nx3 positions along the shaft

**cfg.shaft.distance** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
scalar, distance between electrodes

**cfg.shaft.tip** - [ft_electrodeplacement](/reference/ft_electrodeplacement)  
1x3 position of the electrode at the tip of the shaft

**cfg.shortdistance** - [ft_nirs_referencechannelsubtraction](/reference/ft_nirs_referencechannelsubtraction)  
scalar, below which distance a channel is regarded as short in cm (default = 1.5)

**cfg.showRawVariation** - [ft_omri_quality](/reference/ft_omri_quality)  
1 to show variation in raw scans (default), 0 to show var. in processed scans

**cfg.showcallinfo** - [ft_icabrowser](/reference/ft_icabrowser)  
show call info, 'yes' or 'no' (default: 'no')

**cfg.showcomment** - [ft_multiplotER](/reference/ft_multiplotER)  
'yes' or 'no' (default = 'yes')

**cfg.showcomment** - [ft_multiplotTFR](/reference/ft_multiplotTFR)  
'yes', 'no' (default = 'yes')

**cfg.showinfo** - [ft_analysispipeline](/reference/ft_analysispipeline)  
string or cell-array of strings, information to display in the gui boxes, can be any combination of 'functionname', 'revision', 'matlabversion', 'computername', 'username', 'calltime', 'timeused', 'memused', 'workingdir', 'scriptpath' (default = 'functionname', only display function name). Can also be 'all', show all pipeline. Please note that if you want to show a lot of information, this will require a lot of screen real estate.

**cfg.showlabels** - [ft_multiplotER](/reference/ft_multiplotER)  
'yes' or 'no' (default = 'no')

**cfg.showlabels** - [ft_multiplotTFR](/reference/ft_multiplotTFR)  
'yes', 'no' (default = 'no')

**cfg.showoutline** - [ft_multiplotER](/reference/ft_multiplotER)  
'yes' or 'no' (default = 'no')

**cfg.showoutline** - [ft_multiplotTFR](/reference/ft_multiplotTFR)  
'yes', 'no' (default = 'no')

**cfg.showscale** - [ft_multiplotER](/reference/ft_multiplotER)  
'yes' or 'no' (default = 'yes')

**cfg.showscale** - [ft_multiplotTFR](/reference/ft_multiplotTFR)  
'yes', 'no' (default = 'yes')

**cfg.singleshell.batchsize** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
scalar or 'all' (default 1), number of dipoles for which the leadfield is computed in a single call to the low-level code. Trades off memory efficiency for speed.

**cfg.skipcomnt** - [ft_prepare_layout](/reference/ft_prepare_layout)  
'yes' or 'no', whether the comment should be included in the layout or not (default = 'no')

**cfg.skipscale** - [ft_prepare_layout](/reference/ft_prepare_layout)  
'yes' or 'no', whether the scale should be included in the layout or not (default = 'no')

**cfg.skullsmooth** - [ft_volumesegment](/reference/ft_volumesegment)  
'no', or scalar, the FWHM of the gaussian kernel in voxels, (default = 5) this parameter is only used when the segmentation contains 6 tisuse types, including 'bone'

**cfg.skullthreshold** - [ft_volumesegment](/reference/ft_volumesegment)  
'no', or scalar, relative threshold value which is used to threshold the anatomical data in order to create a volumetric scalpmask (see below), (default = 0.5). this parameter is only used when the segmetnation contains 6 tissue types, including 'bone',

**cfg.slice** - [ft_sourceplot](/reference/ft_sourceplot)  
requires 'anatomical' as input (default = 'none') '2d', plots 2D slices through the cloud with an outline of the mesh '3d', draws an outline around the mesh at a particular slice

**cfg.slicedim** - [ft_sourceplot](/reference/ft_sourceplot)  
dimension to slice 1 (x-axis) 2(y-axis) 3(z-axis) (default = 3)

**cfg.slicepos** - [ft_sourceplot](/reference/ft_sourceplot)  
'auto' or Nx1 vector specifying the position of the slice plane along the orientation axis (default = 'auto': chooses slice(s) with the most data)

**cfg.slicerange** - [ft_sourceplot](/reference/ft_sourceplot)  
range of slices in data, (default = 'auto') 'auto', full range of data [min max], coordinates of first and last slice in voxels

**cfg.smooth** - [ft_defacevolume](/reference/ft_defacevolume), [ft_volumedownsample](/reference/ft_volumedownsample)  
'no' or the FWHM of the gaussian kernel in voxels (default = 'no')

**cfg.smooth** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
5, smoothing in voxels

**cfg.smoothFWHM** - [ft_omri_pipeline](/reference/ft_omri_pipeline)  
kernel width in mm (Full Width Half Maximum) for smoothing (default = 0 => no smoothing)

**cfg.smoothFWHM** - [ft_omri_pipeline_nuisance](/reference/ft_omri_pipeline_nuisance)  
kernel width in mm (Full Width Half Maximum) for smoothing (default = 8)

**cfg.snapshot** - [ft_volumerealign](/reference/ft_volumerealign)  
'no' ('yes'), making a snapshot of the image once a fiducial or landmark location is selected. The optional second output argument to the function will contain the handles to these figures.

**cfg.snapshotfile** - [ft_volumerealign](/reference/ft_volumerealign)  
'ft_volumerealign_snapshot' or string, the root of the filename for the snapshots, including the path. If no path is given the files are saved to the pwd. The consecutive figures will be numbered and saved as png-file.

**cfg.sobi.n_sources** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.sobi.p_correlations** - [ft_componentanalysis](/reference/ft_componentanalysis)  


**cfg.source.datafile** - [ft_realtime_downsample](/reference/ft_realtime_downsample), [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
string

**cfg.source.dataformat** - [ft_realtime_downsample](/reference/ft_realtime_downsample), [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
string, default is determined automatic

**cfg.source.dataset** - [ft_realtime_downsample](/reference/ft_realtime_downsample), [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
string

**cfg.source.eventfile** - [ft_realtime_downsample](/reference/ft_realtime_downsample), [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
string

**cfg.source.eventformat** - [ft_realtime_downsample](/reference/ft_realtime_downsample), [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
string, default is determined automatic

**cfg.source.headerfile** - [ft_realtime_downsample](/reference/ft_realtime_downsample), [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
string

**cfg.source.headerformat** - [ft_realtime_downsample](/reference/ft_realtime_downsample), [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
string, default is determined automatic

**cfg.sourcemodel** - [ft_denoise_dssp](/reference/ft_denoise_dssp)  
structure, source model with precomputed leadfields, see FT_PREPARE_LEADFIELD

**cfg.sourcemodel.dim** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
[Nx Ny Nz] vector with dimensions in case of 3-D grid (optional)

**cfg.sourcemodel.dim** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
[Nx Ny Nz] vector with dimensions in case of 3-D sourcemodel (optional)

**cfg.sourcemodel.dim** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
[Nx Ny Nz] vector with dimensions in case of 3D grid (optional)

**cfg.sourcemodel.filter** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel), [ft_sourceanalysis](/reference/ft_sourceanalysis)  


**cfg.sourcemodel.inside** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
N*1 vector with boolean value whether grid point is inside brain (optional)

**cfg.sourcemodel.inside** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
N*1 vector with boolean value whether position is inside brain (optional)

**cfg.sourcemodel.inside** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
N*1 vector with boolean value whether sourcemodel point is inside brain (optional)

**cfg.sourcemodel.lbex** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  


**cfg.sourcemodel.leadfield** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel), [ft_sourceanalysis](/reference/ft_sourceanalysis)  


**cfg.sourcemodel.pos** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_prepare_leadfield](/reference/ft_prepare_leadfield), [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
N*3 matrix with position of each source

**cfg.sourcemodel.pos** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
N*3 matrix with the vertex positions of the cortical sheet

**cfg.sourcemodel.resolution** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
number (e.g. 1 cm) for automatic sourcemodel generation

**cfg.sourcemodel.subspace** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  


**cfg.sourcemodel.tri** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
M*3 matrix that describes the triangles connecting the vertices

**cfg.sourcemodel.unit** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
string, can be 'mm', 'cm', 'm' (default is automatic)

**cfg.sourcemodel.xgrid** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
vector (e.g. -20:1:20) or 'auto' (default = 'auto')

**cfg.sourcemodel.ygrid** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
vector (e.g. -20:1:20) or 'auto' (default = 'auto')

**cfg.sourcemodel.zgrid** - [ft_prepare_leadfield](/reference/ft_prepare_leadfield)  
vector (e.g. 0:1:20) or 'auto' (default = 'auto')

**cfg.spacemax** - [ft_sliceinterp](/reference/ft_sliceinterp)  
'auto' (default) or integer (last slice position)

**cfg.spacemin** - [ft_sliceinterp](/reference/ft_sliceinterp)  
'auto' (default) or integer (first slice position)

**cfg.speed** - [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
relative speed at which data is written (default = 1)

**cfg.speed** - [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy)  
relative speed at which data is written (default = inf)

**cfg.speedup** - [ft_realtime_dicomproxy](/reference/ft_realtime_dicomproxy)  
optional speedup parameter

**cfg.sphere** - [ft_volumelookup](/reference/ft_volumelookup)  
radius of each sphere in cm/mm dep on unit of input

**cfg.spheremesh** - [ft_megplanar](/reference/ft_megplanar), [ft_megrealign](/reference/ft_megrealign)  
number of dipoles in the source layer (default = 642)

**cfg.sphereradius** - [ft_sourceplot](/reference/ft_sourceplot)  
maximum distance from each voxel to the surface to be included in the sphere projection methods, expressed in mm

**cfg.spherify** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
'yes' or 'no', scale the source model so that it fits inside a sperical volume conduction model (default = 'no')

**cfg.spikechannel** - [ft_spike_select](/reference/ft_spike_select), [ft_spike_waveform](/reference/ft_spike_waveform)  
See FT_CHANNELSELECTION for details.

**cfg.spikechannel** - [ft_spike_psth](/reference/ft_spike_psth)  
See FT_CHANNELSELECTION for details. cfg.trials is vector of indices (e.g., 1:2:10) logical selection of trials (e.g., [1010101010]) 'all' (default), selects all trials

**cfg.spikechannel** - [ft_spikedensity](/reference/ft_spikedensity)  
cell-array ,see FT_CHANNELSELECTION for details

**cfg.spikechannel** - [ft_spiketriggeredspectrum_stat](/reference/ft_spiketriggeredspectrum_stat)  
label of ONE unit, according to FT_CHANNELSELECTION

**cfg.spikechannel** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster), [ft_spike_rate](/reference/ft_spike_rate)  
see FT_CHANNELSELECTION for details

**cfg.spikechannel** - [ft_spike_plot_isireturn](/reference/ft_spike_plot_isireturn), [ft_spike_plot_psth](/reference/ft_spike_plot_psth)  
string or index of single spike channel to trigger on (default = 1) Only one spikechannel can be plotted at a time.

**cfg.spikechannel** - [ft_spike_isi](/reference/ft_spike_isi)  
string or index of spike channels to trigger on (default = 'all') See FT_CHANNELSELECTION for details.

**cfg.spikechannel** - [ft_spike_plot_isi](/reference/ft_spike_plot_isi)  
string or index or logical array to to select 1 spike channel. (default = 1).

**cfg.spikechannel** - [ft_spiketriggeredaverage](/reference/ft_spiketriggeredaverage), [ft_spiketriggeredinterpolation](/reference/ft_spiketriggeredinterpolation)  
string, name of single spike channel to trigger on

**cfg.spikechannel** - [ft_spiketriggeredspectrum_fft](/reference/ft_spiketriggeredspectrum_fft)  
string, name of spike channels to trigger on cfg.channel = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details

**cfg.spikelength** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster)  
number >0 and <=1 indicating the length of the spike. If cfg.spikelength = 1, then no space will be left between subsequent rows representing trials (row-unit is 1).

**cfg.spikesel** - [ft_spiketriggeredspectrum_stat](/reference/ft_spiketriggeredspectrum_stat)  
'all' (default) or numerical or logical selection of spikes.

**cfg.split** - [ft_denoise_prewhiten](/reference/ft_denoise_prewhiten)  
cell-array of channel types between which covariance is split, it can also be 'all' or 'no'

**cfg.spm.cost_fun** - [ft_volumerealign](/reference/ft_volumerealign)  
cost function string: 'mi' - Mutual Information (default) 'nmi' - Normalised Mutual Information 'ecc' - Entropy Correlation Coefficient 'ncc' - Normalised Cross Correlation

**cfg.spm.fwhm** - [ft_volumerealign](/reference/ft_volumerealign)  
smoothing to apply to 256x256 joint histogram, default: [7 7]

**cfg.spm.params** - [ft_volumerealign](/reference/ft_volumerealign)  
starting estimates (6 elements), default: [0 0 0 0 0 0]

**cfg.spm.regtype** - [ft_volumerealign](/reference/ft_volumerealign)  
'subj', 'rigid'

**cfg.spm.sep** - [ft_volumerealign](/reference/ft_volumerealign)  
optimisation sampling steps (mm), default: [4 2]

**cfg.spm.smoref** - [ft_volumerealign](/reference/ft_volumerealign)  
scalar value

**cfg.spm.smosrc** - [ft_volumerealign](/reference/ft_volumerealign)  
scalar value

**cfg.spm.tol** - [ft_volumerealign](/reference/ft_volumerealign)  
tolerences for accuracy of each param, default: [0.02 0.02 0.02 0.001 0.001 0.001]

**cfg.spmmethod** - [ft_volumesegment](/reference/ft_volumesegment)  
string, 'old', 'new', 'mars' (default = 'old'). This pertains to the algorithm used when cfg.spmversion='spm12', see below.

**cfg.spmversion** - [ft_volumesegment](/reference/ft_volumesegment)  
string, 'spm2', 'spm8', 'spm12' (default = 'spm12')

**cfg.spmversion** - [ft_prepare_mesh](/reference/ft_prepare_mesh), [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel), [ft_volumedownsample](/reference/ft_volumedownsample), [ft_volumenormalise](/reference/ft_volumenormalise), [ft_volumerealign](/reference/ft_volumerealign)  
string, 'spm2', 'spm8', 'spm12' (default = 'spm8')

**cfg.spmversion** - [ft_volumebiascorrect](/reference/ft_volumebiascorrect)  
string, 'spm8', 'spm12' (default = 'spm8')

**cfg.standardisedata** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
string, 'yes' or 'no', whether or not to standardise dependent variable prior to the regression (default = 'no')

**cfg.standardiserefdata** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
string, 'yes' or 'no', whether or not to standardise reference data prior to the regression (default = 'no')

**cfg.statistic** - [ft_statistics_analytic](/reference/ft_statistics_analytic), [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
'indepsamplesT' independent samples T-statistic, 'indepsamplesF' independent samples F-statistic, 'indepsamplesregrT' independent samples regression coefficient T-statistic, 'indepsamplesZcoh' independent samples Z-statistic for coherence, 'depsamplesT' dependent samples T-statistic, 'depsamplesFmultivariate' dependent samples F-statistic MANOVA, 'depsamplesregrT' dependent samples regression coefficient T-statistic, 'actvsblT' activation versus baseline T-statistic.

**cfg.statistic** - [ft_statistics_stats](/reference/ft_statistics_stats)  
'ttest' test against a mean of zero 'ttest2' compare the mean in two conditions 'paired-ttest' 'anova1' 'kruskalwallis' 'signtest' 'signrank' 'pearson' 'kendall' 'spearman'

**cfg.statistic** - [ft_statistics_crossvalidate](/reference/ft_statistics_crossvalidate)  
a cell-array of statistics to report (default = {'accuracy' 'binomial'})

**cfg.statistic** - [ft_statistics_analytic](/reference/ft_statistics_analytic)  
string, statistic to compute for each sample or voxel (see below)

**cfg.stimuli** - [ft_spike_rate_orituning](/reference/ft_spike_rate_orituning)  
should be an 1 x nConditions array of orientations or directions in radians varargin{i} corresponds to cfg.stimuli(i)

**cfg.stimulus1.isi** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
in seconds, i.e. for 10Hz you would specify 0.1 seconds as the interstimulus interval (default = 0.1176)

**cfg.stimulus1.isijitter** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
in seconds, max jitter relative to the previous stimulus (default = 0)

**cfg.stimulus1.kernelduration** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
in seconds (default = isi)

**cfg.stimulus1.kernelshape** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
'sine'

**cfg.stimulus1.mode** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
'periodic', 'transient' or 'off' (default = 'periodic')

**cfg.stimulus1.number** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
does not apply for periodic stimuli

**cfg.stimulus1.onset** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
in seconds, first stimulus relative to the start of the trial (default = 0)

**cfg.stimulus1.onsetjitter** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
in seconds, max jitter that is added to the onset (default = 0)

**cfg.stimulus2.condition** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
1xM vector with condition codes for each transient within a trial (default = [1 1 2 2])

**cfg.stimulus2.condition** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
does not apply for periodic stimuli

**cfg.stimulus2.gain** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
1xM vector with gain for each condition for each transient within a trial(default = [1 1 1 1])

**cfg.stimulus2.gain** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
does not apply for periodic stimuli

**cfg.stimulus2.isi** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
in seconds as the interstimulus interval (default = 0.7)

**cfg.stimulus2.isijitter** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
in seconds, max jitter relative to the previous stimulus ((default = 0.2)

**cfg.stimulus2.kernelduration** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
in seconds (default = 0.75*isi)

**cfg.stimulus2.kernelshape** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
'hanning'

**cfg.stimulus2.mode** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
'periodic', 'transient' or 'off' (default = 'transient')

**cfg.stimulus2.number** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
scalar M, how many transients are to be presented per trial (default = 4)

**cfg.stimulus2.onset** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
in seconds, first stimulus relative to the start of the trial (default = 0.7)

**cfg.stimulus2.onsetjitter** - [ft_steadystatesimulation](/reference/ft_steadystatesimulation)  
in seconds, max jitter that is added to the onset (default = 0.2)

**cfg.style** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotIC](/reference/ft_topoplotIC), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
plot style (default = 'both') 'straight' colormap only 'contour' contour lines only 'both' (default) both colormap and contour lines 'fill' constant color between lines 'blank' only the head shape

**cfg.submethod** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
(optional)

**cfg.subplotsize** - [ft_clusterplot](/reference/ft_clusterplot)  
layout of subplots ([h w], default [3 5])

**cfg.supchan** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
suppressed channel label(s)

**cfg.supdip** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
suppressed dipole location(s)

**cfg.supmethod** - [ft_sourcedescriptives](/reference/ft_sourcedescriptives)  
'chan_dip', 'chan', 'dip', 'none' (default)

**cfg.surfdownsample** - [ft_sourceplot](/reference/ft_sourceplot)  
number (default = 1, i.e. no downsampling)

**cfg.surffile** - [ft_sourceplot](/reference/ft_sourceplot)  
string, file that contains the surface (default = 'surface_white_both.mat') 'surface_white_both.mat' contains a triangulation that corresponds with the SPM anatomical template in MNI coordinates

**cfg.surfinflated** - [ft_sourceplot](/reference/ft_sourceplot)  
string, file that contains the inflated surface (default = []) may require specifying a point-matching (uninflated) surffile

**cfg.symmetry** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
'x', 'y' or 'z' symmetry for two dipoles, can be empty (default = [])

## T 

**cfg.t_ftimwin** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
the width of the sliding window on which the coefficients are estimated

**cfg.tail** - [ft_statistics_analytic](/reference/ft_statistics_analytic), [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo), [ft_statistics_stats](/reference/ft_statistics_stats)  
number, -1, 1 or 0 (default = 0)

**cfg.taper** - [ft_freqanalysis](/reference/ft_freqanalysis)  
'dpss', 'hanning' or many others, see WINDOW (default = 'dpss') For cfg.output='powandcsd', you should specify the channel combinations between which to compute the cross-spectra as cfg.channelcmb. Otherwise you should specify only the channels in cfg.channel.

**cfg.taper** - [ft_spiketriggeredspectrum_fft](/reference/ft_spiketriggeredspectrum_fft)  
'dpss', 'hanning' or many others, see WINDOW (default = 'hanning')

**cfg.tapsmofrq** - [ft_freqanalysis](/reference/ft_freqanalysis)  
number, the amount of spectral smoothing through multi-tapering. Note that 4 Hz smoothing means plus-minus 4 Hz, i.e. a 8 Hz smoothing box.

**cfg.tapsmofrq** - [ft_spiketriggeredspectrum_fft](/reference/ft_spiketriggeredspectrum_fft)  
number, the amount of spectral smoothing through multi-tapering. Note that 4 Hz smoothing means plus-minus 4 Hz, i.e. a 8 Hz smoothing box. Note: multitapering rotates phases (no problem for consistency)

**cfg.tapsmofrq** - [ft_freqanalysis](/reference/ft_freqanalysis)  
vector 1 x numfoi, the amount of spectral smoothing through multi-tapering. Note that 4 Hz smoothing means plus-minus 4 Hz, i.e. a 8 Hz smoothing box. cfg.foi = vector 1 x numfoi, frequencies of interest cfg.taper = 'dpss', 'hanning' or many others, see WINDOW (default = 'dpss') For cfg.output='powandcsd', you should specify the channel combinations between which to compute the cross-spectra as cfg.channelcmb. Otherwise you should specify only the channels in cfg.channel. cfg.t_ftimwin = vector 1 x numfoi, length of time window (in seconds) cfg.toi = vector 1 x numtoi, the times on which the analysis windows should be centered (in seconds), or a string such as '50%' or 'all' (default). Both string options use all timepoints available in the data, but 'all' centers a spectral estimate on each sample, whereas the percentage specifies the degree of overlap between the shortest time windows from cfg.t_ftimwin.

**cfg.tapsmofrq** - [ft_spiketriggeredspectrum_convol](/reference/ft_spiketriggeredspectrum_convol)  
vector 1 x numfoi, the amount of spectral smoothing through multi-tapering. Note that 4 Hz smoothing means plus-minus 4 Hz, i.e. a 8 Hz smoothing box. cfg.foi = vector 1 x numfoi, frequencies of interest cfg.taper = 'dpss', 'hanning' or many others, see WINDOW (default = 'hanning') cfg.t_ftimwin = vector 1 x numfoi, length of time window (in seconds) cfg.taperopt = parameter that goes in WINDOW function (only applies to windows like KAISER). cfg.spikechannel = cell-array with selection of channels (default = 'all') see FT_CHANNELSELECTION for details cfg.channel = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details cfg.borderspikes = 'yes' (default) or 'no'. If 'yes', we process the spikes falling at the border using an LFP that is not centered on the spike. If 'no', we output NaNs for spikes around which we could not center an LFP segment. cfg.rejectsaturation= 'yes' (default) or 'no'. If 'yes', we set EEG segments where the maximum or minimum voltage range is reached with zero derivative (i.e., saturated signal) to NaN, effectively setting all spikes phases that use these parts of the EEG to NaN. An EEG that saturates always returns the same phase at all frequencies and should be ignored.

**cfg.target** - [ft_nirs_transform_ODs](/reference/ft_nirs_transform_ODs)  
Mx1 cell-array, can be 'O2Hb' (oxygenated hemo- globin), 'HHb' de-oxygenated hemoglobin') or 'tHb' (total hemoglobin), or a combination of those (default: {'O2Hb', 'HHb'})

**cfg.target** - [ft_electroderealign](/reference/ft_electroderealign)  
list of electrode sets that will be averaged

**cfg.target** - [ft_electroderealign](/reference/ft_electroderealign)  
single electrode set that serves as standard

**cfg.target.datafile** - [ft_realtime_asaproxy](/reference/ft_realtime_asaproxy), [ft_realtime_brainampproxy](/reference/ft_realtime_brainampproxy), [ft_realtime_ctfproxy](/reference/ft_realtime_ctfproxy), [ft_realtime_dicomproxy](/reference/ft_realtime_dicomproxy), [ft_realtime_downsample](/reference/ft_realtime_downsample), [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy), [ft_realtime_fmriproxy](/reference/ft_realtime_fmriproxy), [ft_realtime_jaga16proxy](/reference/ft_realtime_jaga16proxy), [ft_realtime_micromedproxy](/reference/ft_realtime_micromedproxy), [ft_realtime_modeegproxy](/reference/ft_realtime_modeegproxy), [ft_realtime_neuralynxproxy](/reference/ft_realtime_neuralynxproxy), [ft_realtime_pooraudioproxy](/reference/ft_realtime_pooraudioproxy), [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
string, target destination for the data (default = 'buffer://localhost:1972')

**cfg.target.dataformat** - [ft_realtime_asaproxy](/reference/ft_realtime_asaproxy), [ft_realtime_brainampproxy](/reference/ft_realtime_brainampproxy), [ft_realtime_ctfproxy](/reference/ft_realtime_ctfproxy), [ft_realtime_downsample](/reference/ft_realtime_downsample), [ft_realtime_fileproxy](/reference/ft_realtime_fileproxy), [ft_realtime_jaga16proxy](/reference/ft_realtime_jaga16proxy), [ft_realtime_micromedproxy](/reference/ft_realtime_micromedproxy), [ft_realtime_modeegproxy](/reference/ft_realtime_modeegproxy), [ft_realtime_neuralynxproxy](/reference/ft_realtime_neuralynxproxy), [ft_realtime_pooraudioproxy](/reference/ft_realtime_pooraudioproxy), [ft_realtime_signalproxy](/reference/ft_realtime_signalproxy)  
string, default is determined automatic

**cfg.target.eventfile** - [ft_realtime_brainampproxy](/reference/ft_realtime_brainampproxy), [ft_realtime_micromedproxy](/reference/ft_realtime_micromedproxy)  
string, target destination for the events (default = 'buffer://localhost:1972')

**cfg.target.eventformat** - [ft_realtime_brainampproxy](/reference/ft_realtime_brainampproxy), [ft_realtime_micromedproxy](/reference/ft_realtime_micromedproxy)  
string, default is determined automatic

**cfg.target.label** - [ft_electroderealign](/reference/ft_electroderealign)  
{'NAS', 'LPA', 'RPA'}

**cfg.target.pos** - [ft_electroderealign](/reference/ft_electroderealign)  
[0 -90 0] % location of the right ear

**cfg.target.pos** - [ft_electroderealign](/reference/ft_electroderealign)  
[0 90 0] % location of the left ear

**cfg.target.pos** - [ft_electroderealign](/reference/ft_electroderealign)  
[110 0 0] % location of the nose

**cfg.template** - [ft_megrealign](/reference/ft_megrealign)  


**cfg.template** - [ft_megrealign](/reference/ft_megrealign)  
datasets that are averaged into the standard

**cfg.template** - [ft_volumesegment](/reference/ft_volumesegment)  
filename of the template anatomical MRI (default = '/spm2/templates/T1.mnc' or '/spm8/templates/T1.nii')

**cfg.template** - [ft_prepare_neighbours](/reference/ft_prepare_neighbours)  
name of the template file, e.g. CTF275_neighb.mat

**cfg.template** - [ft_megrealign](/reference/ft_megrealign)  
single dataset that serves as template

**cfg.template** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
specification of a template grid (grid structure), or a filename of a template grid (defined in MNI space), either cfg.resolution or cfg.template needs to be defined. If both are defined cfg.template prevails

**cfg.template** - [ft_volumenormalise](/reference/ft_volumenormalise)  
string, filename of the template anatomical MRI (default = 'T1.mnc' for spm2 or 'T1.nii' for spm8)

**cfg.template** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
string, name of a template dataset for between-session repositioning (default = [])

**cfg.template.axes** - [ft_interactiverealign](/reference/ft_interactiverealign)  
string, 'yes' or 'no (default = 'no')

**cfg.template.elec** - [ft_interactiverealign](/reference/ft_interactiverealign)  
structure

**cfg.template.grad** - [ft_interactiverealign](/reference/ft_interactiverealign)  
structure

**cfg.template.headmodel** - [ft_interactiverealign](/reference/ft_interactiverealign)  
structure, see FT_PREPARE_HEADMODEL

**cfg.template.headmodelstyle** - [ft_interactiverealign](/reference/ft_interactiverealign)  
'vertex', 'edge', 'surface' or 'both' (default = 'edge')

**cfg.template.headshape** - [ft_interactiverealign](/reference/ft_interactiverealign)  
structure, see FT_READ_HEADSHAPE

**cfg.template.headshapestyle** - [ft_interactiverealign](/reference/ft_interactiverealign)  
'vertex', 'edge', 'surface' or 'both' (default = 'vertex')

**cfg.template.mri** - [ft_interactiverealign](/reference/ft_interactiverealign)  
structure, see FT_READ_MRI

**cfg.testtrials** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
cell-array or string, trial indices to be used as test folds in a cross-validation scheme (numel(cfg.testrials == number of folds))

**cfg.threshold** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
0.1, relative to the maximum value in the segmentation

**cfg.threshold** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
integer array, ([1 by 2] or [1 by numel(cfg.channel) + numel(cfg.reflags)]), regularization or shrinkage ('lambda') parameter to be loaded on the diagonal of the penalty term (if cfg.method == 'mlrridge' or 'mlrqridge')

**cfg.threshold** - [ft_heartrate](/reference/ft_heartrate)  
scalar, between 0 and 1 (default = 0.4)

**cfg.threshold** - [ft_nirs_scalpcouplingindex](/reference/ft_nirs_scalpcouplingindex)  
scalar, the correlation value which has to be exceeded to be labelled a 'good' channel (default 0.75)

**cfg.threshold** - [ft_realtime_heartbeatdetect](/reference/ft_realtime_heartbeatdetect)  
value, after normalization (default = 3)

**cfg.tight** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
'yes' or 'no' (default is automatic)

**cfg.time** - [ft_resampledata](/reference/ft_resampledata)  
cell-array with one time axis per trial (i.e. from another dataset)

**cfg.time** - [ft_freqsimulation](/reference/ft_freqsimulation)  
cell-array with one time axis per trial, which are for example obtained from an existing dataset

**cfg.timestampdefinition** - [ft_spikedetection](/reference/ft_spikedetection), [ft_spikedownsample](/reference/ft_spikedownsample)  
'orig' or 'sample'

**cfg.timestampspersecond** - [ft_spike_maketrials](/reference/ft_spike_maketrials)  
number of timestaps per second (for Neuralynx, 1000000 for example). This can be computed for example from the LFP hdr (cfg.timestampspersecond = data.hdr.Fs*data.hdr.TimeStampPerSecond) or is a priori known.

**cfg.timextime** - [ft_statistics_mvpa](/reference/ft_statistics_mvpa)  
'yes' or 'no', performs time x time generalisation. In other words, the classifier is trained at each time point and tested at every time point. The result is a time x time matrix of classification performance. (default 'no') Note that searchlight and timextime cannot be run simultaneously (at least one option needs to be set to 'no').

**cfg.timwin** - [ft_nonlinearassociation](/reference/ft_nonlinearassociation)  
0.2

**cfg.timwin** - [ft_spiketriggeredinterpolation](/reference/ft_spiketriggeredinterpolation)  
[begin end], duration of LFP segment around each spike (default = [-0.005 0.005]) to be removed

**cfg.timwin** - [ft_spiketriggeredaverage](/reference/ft_spiketriggeredaverage), [ft_spiketriggeredspectrum_fft](/reference/ft_spiketriggeredspectrum_fft)  
[begin end], time around each spike (default = [-0.1 0.1])

**cfg.timwin** - [ft_spiketriggeredspectrum_stat](/reference/ft_spiketriggeredspectrum_stat)  
double or 'all' (default) - double: indicates we compute statistic with a sliding window of cfg.timwin, i.e. time-resolved analysis. - 'all': we compute statistic over all time-points, i.e. in non-time resolved fashion.

**cfg.tissue** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  


**cfg.tissue** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
a string or integer, to be used in combination with a 'seg' for the second intput. If 'brain', 'skull', and 'scalp' are fields present in 'seg', then cfg.tissue need not be specified, as these are defaults, depending on cfg.method. Otherwise, cfg.tissue should refer to which field(s) of seg should be used.

**cfg.tissue** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
cell-array with tissue types or numeric vector with integer values

**cfg.tissue** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel), [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
see above; in combination with 'seg' input

**cfg.tissue** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel), [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
see above; in combination with 'seg' input; default options are 'brain' or 'scalp'

**cfg.tissue** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  
see above; in combination with 'seg' input; default options are 'brain' or 'scalp'; must be only 1 value

**cfg.tissue** - [ft_prepare_mesh](/reference/ft_prepare_mesh)  
{'scalp', 'skull', 'brain'};

**cfg.tissueval** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  


**cfg.title** - [ft_sliceinterp](/reference/ft_sliceinterp)  
optional title (default is '')

**cfg.title** - [ft_topoplotIC](/reference/ft_topoplotIC)  
string or 'auto' or 'off', specify a figure title, or use 'component N' (auto) as the title

**cfg.title** - [ft_singleplotER](/reference/ft_singleplotER), [ft_singleplotTFR](/reference/ft_singleplotTFR)  
string, title of plot

**cfg.title** - [ft_sourceplot](/reference/ft_sourceplot)  
string, title of the plot

**cfg.toi** - [ft_nonlinearassociation](/reference/ft_nonlinearassociation)  
[]

**cfg.toi** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
[t1 t2 ... tx] the time points at which the windows are centered

**cfg.toi** - [ft_freqanalysis](/reference/ft_freqanalysis)  
vector 1 x numtoi, the times on which the analysis windows should be centered (in seconds)

**cfg.toilim** - [ft_freqgrandaverage](/reference/ft_freqgrandaverage)  
[tmin tmax] or 'all', to specify a subset of latencies (default = 'all')

**cfg.toilim** - [ft_redefinetrial](/reference/ft_redefinetrial)  
[tmin tmax] to specify a latency window in seconds, can be Nx2 vector

**cfg.tol** - [ft_sourceanalysis](/reference/ft_sourceanalysis)  
number or empty for automatic default

**cfg.tolerance** - [ft_appendfreq](/reference/ft_appendfreq)  
scalar, tolerance to determine how different the frequency and/or time axes are allowed to still be considered compatible (default = 1e-5)

**cfg.tolerance** - [ft_appendtimelock](/reference/ft_appendtimelock)  
scalar, tolerance to determine how different the time axes are allowed to still be considered compatible (default = 1e-5)

**cfg.topolabel** - [ft_componentanalysis](/reference/ft_componentanalysis)  
Nx1 cell-array with the channel labels

**cfg.topplotfunc** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster)  
'bar' (default) or 'line'.

**cfg.topplotsize** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster)  
number ranging from 0 to 1, indicating the proportion of the rasterplot that the top plot will take (e.g., with 0.7 the top plot will be 70% of the rasterplot in size). Default = 0.5.

**cfg.tpm** - [ft_volumesegment](/reference/ft_volumesegment)  
cell-array containing the filenames of the tissue probability maps

**cfg.transform** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  


**cfg.translate** - [ft_defacemesh](/reference/ft_defacemesh), [ft_defacevolume](/reference/ft_defacevolume)  
initial position of the center of the box (default = [0 0 0])

**cfg.translate** - [ft_defacemesh](/reference/ft_defacemesh), [ft_defacevolume](/reference/ft_defacevolume)  
initial rotation of the box (default = [0 0 0])

**cfg.trialborders** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster)  
'yes' or 'no'. If 'yes', borders of trials are plotted

**cfg.trialdef** - [ft_definetrial](/reference/ft_definetrial)  
structure with details of trial definition, see below

**cfg.trialdef.eventtype** - [ft_trialfun_artinis](/reference/ft_trialfun_artinis)  
'?'

**cfg.trialdef.eventtype** - [ft_trialfun_artinis](/reference/ft_trialfun_artinis)  
'gui'

**cfg.trialdef.eventtype** - [ft_artifact_tms](/reference/ft_artifact_tms), [ft_definetrial](/reference/ft_definetrial), [ft_trialfun_artinis](/reference/ft_trialfun_artinis)  
'string'

**cfg.trialdef.eventvalue** - [ft_artifact_tms](/reference/ft_artifact_tms), [ft_definetrial](/reference/ft_definetrial), [ft_trialfun_artinis](/reference/ft_trialfun_artinis)  
number, string or list with numbers or strings

**cfg.trialdef.oxyproj** - [ft_trialfun_artinis](/reference/ft_trialfun_artinis)  
'string', indicating an oxyproj-file, in which information about the events for this oxy3-file are stored

**cfg.trialdef.poststim** - [ft_trialfun_artinis](/reference/ft_trialfun_artinis)  
latency in seconds (optional)

**cfg.trialdef.poststim** - [ft_definetrial](/reference/ft_definetrial)  
number, latency in seconds (optional)

**cfg.trialdef.prestim** - [ft_trialfun_artinis](/reference/ft_trialfun_artinis)  
latency in seconds (optional)

**cfg.trialdef.prestim** - [ft_definetrial](/reference/ft_definetrial)  
number, latency in seconds (optional)

**cfg.trialdef.triallength** - [ft_definetrial](/reference/ft_definetrial)  
duration in seconds (can also be 1 or Inf) cfg.trialdef.ntrials = number of trials (can also be 1 or Inf)

**cfg.trialdef.triallength** - [ft_trialfun_artinis](/reference/ft_trialfun_artinis)  
duration in seconds (can be Inf) cfg.trialdef.ntrials = number of trials

**cfg.trialfun** - [ft_realtime_classification](/reference/ft_realtime_classification)  
'trialfun_Subject01'; ft_realtime_classification(cfg);

**cfg.trialfun** - [ft_artifact_tms](/reference/ft_artifact_tms)  
function name, see below (default = 'ft_trialfun_general')

**cfg.trialfun** - [ft_definetrial](/reference/ft_definetrial)  
string with function name, see below (default = 'ft_trialfun_general')

**cfg.trialfun** - [ft_realtime_average](/reference/ft_realtime_average), [ft_realtime_classification](/reference/ft_realtime_classification), [ft_realtime_oddball](/reference/ft_realtime_oddball), [ft_realtime_selectiveaverage](/reference/ft_realtime_selectiveaverage)  
string with the trial function

**cfg.triallength** - [ft_connectivitysimulation](/reference/ft_connectivitysimulation)  
in seconds

**cfg.triallength** - [ft_dipolesimulation](/reference/ft_dipolesimulation)  
time in seconds

**cfg.trials** - [ft_spike_jpsth](/reference/ft_spike_jpsth)  
'all' (default) or numerical or logical array of to be selected trials.

**cfg.trials** - [ft_channelnormalise](/reference/ft_channelnormalise), [ft_channelrepair](/reference/ft_channelrepair), [ft_componentanalysis](/reference/ft_componentanalysis), [ft_denoise_dssp](/reference/ft_denoise_dssp), [ft_denoise_synthetic](/reference/ft_denoise_synthetic), [ft_detect_movement](/reference/ft_detect_movement), [ft_freqanalysis](/reference/ft_freqanalysis), [ft_freqdescriptives](/reference/ft_freqdescriptives), [ft_megplanar](/reference/ft_megplanar), [ft_multiplotER](/reference/ft_multiplotER), [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_nonlinearassociation](/reference/ft_nonlinearassociation), [ft_preprocessing](/reference/ft_preprocessing), [ft_redefinetrial](/reference/ft_redefinetrial), [ft_rejectvisual](/reference/ft_rejectvisual), [ft_resampledata](/reference/ft_resampledata), [ft_scalpcurrentdensity](/reference/ft_scalpcurrentdensity), [ft_singleplotTFR](/reference/ft_singleplotTFR), [ft_timelockanalysis](/reference/ft_timelockanalysis), [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
'all' or a selection given as a 1xN vector (default = 'all')

**cfg.trials** - [ft_singleplotER](/reference/ft_singleplotER)  
'all' or a selection given as a 1xn vector (default = 'all')

**cfg.trials** - [ft_connectivityanalysis](/reference/ft_connectivityanalysis)  
Nx1 vector specifying which trials to include for the computation. This only has an effect when the input data contains repetitions.

**cfg.trials** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
integer array, trials to be used in regression, see FT_SELECTDATA

**cfg.trials** - [ft_denoise_pca](/reference/ft_denoise_pca)  
list of trials that are used (default = 'all')

**cfg.trials** - [ft_spike_psth](/reference/ft_spike_psth), [ft_spikedensity](/reference/ft_spikedensity)  
numeric or logical selection of trials (default = 'all')

**cfg.trials** - [ft_spike_plot_raster](/reference/ft_spike_plot_raster)  
numeric or logical selection of trials (default = 'all').

**cfg.trials** - [ft_spike_isi](/reference/ft_spike_isi), [ft_spike_xcorr](/reference/ft_spike_xcorr)  
numeric selection of trials (default = 'all')

**cfg.trials** - [ft_spike_select](/reference/ft_spike_select)  
vector of indices (e.g., 1:2:10) logical selection of trials (e.g., [1010101010]) 'all' (default), selects all trials

**cfg.trials** - [ft_spike_rate](/reference/ft_spike_rate)  
vector of indices (e.g., 1:2:10) logical selection of trials (e.g., [1010101010]) 'all' (default), selects all trials% cfg.trials

**cfg.trials** - [ft_spiketriggeredspectrum_stat](/reference/ft_spiketriggeredspectrum_stat)  
vector of indices (e.g., 1:2:10), logical selection of trials (e.g., [1010101010]), or 'all' (default)

**cfg.trigger** - [ft_realtime_synchronous](/reference/ft_realtime_synchronous)  
the trigger values that should be processed (default = 'all')

**cfg.trl** - [ft_preprocessing](/reference/ft_preprocessing), [ft_redefinetrial](/reference/ft_redefinetrial)  
Nx3 matrix with the trial definition, see FT_DEFINETRIAL

**cfg.trl** - [ft_audiovideobrowser](/reference/ft_audiovideobrowser)  
Nx3 matrix, see FT_DEFINETRIAL

**cfg.trl** - [ft_headmovement](/reference/ft_headmovement)  
empty (default), or Nx3 matrix with the trial definition, can be empty.see FT_DEFINETRIAL. If defined empty, the whole recording is used

**cfg.trl** - [ft_spike_maketrials](/reference/ft_spike_maketrials)  
is an nTrials-by-M matrix, with at least 3 columns: Every row contains start (col 1), end (col 2) and offset of the event trigger in the trial in timestamp or sample units (cfg.trlunit). For example, an offset of -1000 means that the trigger (t = 0 sec) occurred 1000 timestamps or samples after the trial start. If more columns are added than 3, these are used to construct the spike.trialinfo field having information about the trial. Note that values in cfg.trl get inaccurate above 2^53 (in that case it is better to use the original uint64 representation)

**cfg.trl** - [ft_databrowser](/reference/ft_databrowser)  
structure that defines the data segments of interest, only applicable for trial-based data

**cfg.trl** - [ft_artifact_threshold](/reference/ft_artifact_threshold), [ft_artifact_tms](/reference/ft_artifact_tms)  
structure that defines the data segments of interest, see FT_DEFINETRIAL

**cfg.trl** - [ft_artifact_ecg](/reference/ft_artifact_ecg), [ft_artifact_eog](/reference/ft_artifact_eog), [ft_artifact_jump](/reference/ft_artifact_jump), [ft_artifact_muscle](/reference/ft_artifact_muscle), [ft_artifact_zvalue](/reference/ft_artifact_zvalue)  
structure that defines the data segments of interest. See FT_DEFINETRIAL

**cfg.trllen** - [ft_freqsimulation](/reference/ft_freqsimulation)  
length of simulated trials in seconds

**cfg.trllen** - [ft_timelocksimulation](/reference/ft_timelocksimulation)  
length of simulated trials in seconds (default = 1)

**cfg.trlunit** - [ft_spike_maketrials](/reference/ft_spike_maketrials)  
'timestamps' (default) or 'samples'. If 'samples', cfg.trl should be specified in samples, and cfg.hdr = data.hdr should be specified. This option can be used to reuse a cfg.trl that was used for preprocessing LFP data. If 'timestamps', cfg.timestampspersecond should be specified, but cfg.hdr should not.

**cfg.truncate** - [ft_denoise_pca](/reference/ft_denoise_pca)  
optional truncation of the singular value spectrum (default = 'no')

## U 

**cfg.unit** - [ft_prepare_headmodel](/reference/ft_prepare_headmodel)  


**cfg.unmixing** - [ft_componentanalysis](/reference/ft_componentanalysis)  
NxN unmixing matrix

**cfg.updatesens** - [ft_combineplanar](/reference/ft_combineplanar), [ft_componentanalysis](/reference/ft_componentanalysis), [ft_denoise_pca](/reference/ft_denoise_pca), [ft_rejectcomponent](/reference/ft_rejectcomponent)  
'no' or 'yes' (default = 'yes')

**cfg.updatesens** - [ft_denoise_tsr](/reference/ft_denoise_tsr)  
string, 'yes' or 'no' (default = 'yes')

**cfg.usefftfilt** - [ft_preprocessing](/reference/ft_preprocessing)  
'no' or 'yes', use fftfilt instead of filter (firws, default = 'no')

**cfg.uvar** - [ft_statistics_analytic](/reference/ft_statistics_analytic), [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
number or list with indices, unit variable(s)

## V 

**cfg.variance** - [ft_freqdescriptives](/reference/ft_freqdescriptives)  
'yes' or 'no', estimate standard error in the standard way (default = 'no')

**cfg.vartriallen** - [ft_spike_psth](/reference/ft_spike_psth)  
'yes' (default) Accept variable trial lengths and use all available trials and the samples in every trial. Missing values will be ignored in the computation of the average and the variance and stored as NaNs in the output psth.trial. 'no' Only select those trials that fully cover the window as specified by cfg.latency and discard those trials that do not.

**cfg.vartriallen** - [ft_spikedensity](/reference/ft_spikedensity)  
'yes' (default) or 'no'. 'yes' - accept variable trial lengths and use all available trials and the samples in every trial. Missing values will be ignored in the computation of the average and the variance. 'no' - only select those trials that fully cover the window as specified by cfg.latency.

**cfg.vartriallen** - [ft_spike_rate](/reference/ft_spike_rate)  
'yes' (default) or 'no'. If 'yes' - accept variable trial lengths and use all available trials and the samples in every trial. If 'no' - only select those trials that fully cover the window as specified by cfg.latency and discard those trials that do not.

**cfg.vartriallen** - [ft_spike_xcorr](/reference/ft_spike_xcorr)  
'yes' (default) or 'no'. If 'yes' - accept variable trial lengths and use all available trials and the samples in every trial. If 'no' - only select those trials that fully cover the window as specified by cfg.latency and discard those trials that do not. if cfg.method = 'yes', then cfg.vartriallen should be 'no' (otherwise, fewer coincidences will occur because of non-overlapping windows)

**cfg.velocity2D.kernel** - [ft_detect_movement](/reference/ft_detect_movement)  
vector 1 x nsamples, kernel to compute velocity (default = [1 1 0 -1 -1].*(data.fsample/6); cfg.velocity2D.demean = 'no' or 'yes', whether to apply centering correction (default = 'yes') cfg.velocity2D.mindur = minimum microsaccade durantion in samples (default = 3); cfg.velocity2D.velthres = threshold for velocity outlier detection (default = 6);

**cfg.verbose** - [ft_nirs_referencechannelsubtraction](/reference/ft_nirs_referencechannelsubtraction)  
boolean, whether text output is desired (default = false)

**cfg.verbose** - [ft_neighbourplot](/reference/ft_neighbourplot)  
string, 'yes' or 'no', whether the function will print feedback text in the command window

**cfg.vertexcolor** - [ft_sourceplot](/reference/ft_sourceplot)  
[r g b] values or string, for example 'brain', 'cortex', 'skin', 'black', 'red', 'r', or an Nx3 or Nx1 array where N is the number of vertices

**cfg.verticalpadding** - [ft_databrowser](/reference/ft_databrowser)  
number or 'auto', padding to be added to top and bottom of plot to avoid channels largely dissappearing when viewmode = 'vertical'/'component' (default = 'auto'). The padding is expressed as a proportion of the total height added to the top and bottom. The setting 'auto' determines the padding depending on the number of channels that are being plotted.

**cfg.videofile** - [ft_audiovideobrowser](/reference/ft_audiovideobrowser)  
string with the filename

**cfg.videohdr** - [ft_audiovideobrowser](/reference/ft_audiovideobrowser)  
header structure of the video data, see FT_READ_HEADER

**cfg.viewmode** - [ft_volumerealign](/reference/ft_volumerealign)  
'ortho' or 'surface', visualize the anatomical MRI as three slices or visualize the extracted head surface (default = 'ortho')

**cfg.viewmode** - [ft_databrowser](/reference/ft_databrowser)  
string, 'butterfly', 'vertical', 'component' for visualizing ICA/PCA components (default is 'butterfly')

**cfg.viewpoint** - [ft_prepare_layout](/reference/ft_prepare_layout)  
string indicating the view point that is used for orthographic projection of 3-D sensor positions to the 2-D plane. The possible viewpoints are 'left' - left sagittal view, L=anterior, R=posterior, top=top, bottom=bottom 'right' - right sagittal view, L=posterior, R=anterior, top=top, bottom=bottom 'topleft' - view from the top top, L=anterior, R=posterior, top=top, bottom=bottom 'topright' - view from the top right, L=posterior, R=anterior, top=top, bottom=bottom 'inferior' - inferior axial view, L=R, R=L, top=anterior, bottom=posterior 'superior' - superior axial view, L=L, R=R, top=anterior, bottom=posterior 'anterior' - anterior coronal view, L=R, R=L, top=top, bottom=bottom 'posterior' - posterior coronal view, L=L, R=R, top=top, bottom=bottom 'auto' - automatic guess of the most optimal of the above tip: use cfg.viewpoint = 'auto' per iEEG electrode grid/strip/depth for more accurate results tip: to obtain an overview of all iEEG electrodes, choose superior/inferior, use cfg.headshape/mri, and plot using FT_LAYOUTPLOT with cfg.box/mask = 'no'

**cfg.viewresult** - [ft_volumerealign](/reference/ft_volumerealign)  
string, 'yes' or 'no', whether or not to visualize aligned volume(s) after realignment (default = 'no')

**cfg.visible** - [ft_clusterplot](/reference/ft_clusterplot)  
string, 'on' or 'off' whether figure will be visible (default = 'on')

**cfg.visible** - [ft_neighbourplot](/reference/ft_neighbourplot), [ft_sourceplot](/reference/ft_sourceplot)  
string, 'on' or 'off', whether figure will be visible (default = 'on')

**cfg.visible** - [ft_layoutplot](/reference/ft_layoutplot)  
string, 'yes' or 'no' whether figure will be visible (default = 'yes')

**cfg.visualize** - [ft_qualitycheck](/reference/ft_qualitycheck)  
string, 'yes' or 'no' to visualize the analysis (default = 'yes')

**cfg.vmpversion** - [ft_volumewrite](/reference/ft_volumewrite)  
1 or 2 (default) version of the vmp-format to use

**cfg.voxels** - [ft_realtime_fmriproxy](/reference/ft_realtime_fmriproxy)  
[64 64 32]

## W 

**cfg.ward** - [ft_spikesorting](/reference/ft_spikesorting)  
substructure with additional low-level options for this method

**cfg.ward.distance** - [ft_spikesorting](/reference/ft_spikesorting)  
'L1', 'L2', 'correlation', 'cosine'

**cfg.warp** - [ft_electroderealign](/reference/ft_electroderealign)  
'dykstra2012', or 'hermes2010'

**cfg.warp** - [ft_electroderealign](/reference/ft_electroderealign)  
'fsaverage'

**cfg.warp** - [ft_electroderealign](/reference/ft_electroderealign)  
string describing the spatial transformation for the template and headshape methods 'rigidbody' apply a rigid-body warp (default) 'globalrescale' apply a rigid-body warp with global rescaling 'traditional' apply a rigid-body warp with individual axes rescaling 'nonlin1' apply a 1st order non-linear warp 'nonlin2' apply a 2nd order non-linear warp 'nonlin3' apply a 3rd order non-linear warp 'nonlin4' apply a 4th order non-linear warp 'nonlin5' apply a 5th order non-linear warp 'dykstra2012' back-project ECoG onto the cortex using energy minimzation 'hermes2010' back-project ECoG onto the cortex along the local norm vector 'fsaverage' surface-based realignment with FreeSurfer fsaverage brain (left->left or right->right) 'fsaverage_sym' surface-based realignment with FreeSurfer fsaverage_sym left hemisphere (left->left or right->left) 'fsinflated' surface-based realignment with FreeSurfer individual subject inflated brain (left->left or right->right)

**cfg.warpmni** - [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)  
'yes'

**cfg.whichEcho** - [ft_omri_pipeline_nuisance](/reference/ft_omri_pipeline_nuisance)  
which echo to process for multi-echo sequences (default = 1)

**cfg.whitebg** - [ft_sliceinterp](/reference/ft_sliceinterp)  
'yes' or 'no' (default = 'yes')

**cfg.width** - [ft_freqanalysis](/reference/ft_freqanalysis), [ft_freqanalysis](/reference/ft_freqanalysis)  
'width', or number of cycles, of the wavelet (default = 7)

**cfg.width** - [ft_prepare_layout](/reference/ft_prepare_layout)  
scalar (default is automatic)

**cfg.widthparam** - [ft_topoplotCC](/reference/ft_topoplotCC)  
string, parameter to be used to control the line width (see below)

**cfg.window** - [ft_spike_plot_isireturn](/reference/ft_spike_plot_isireturn)  
'no', 'gausswin' or 'boxcar' 'gausswin' is N-by-N multivariate gaussian, where the diagonal of the covariance matrix is set by cfg.gaussvar. 'boxcar' is N-by-N rectangular window.

**cfg.window** - [ft_spike_plot_jpsth](/reference/ft_spike_plot_jpsth)  
'string' or N-by-N matrix 'no': apply no smoothing ' gausswin' use a Gaussian smooth function ' boxcar' use a box-car to smooth

**cfg.winfunc** - [ft_spikedensity](/reference/ft_spikedensity)  
(a) string or function handle, type of window to convolve with (def = 'gauss'). - 'gauss' (default) - 'alphawin', given by win = x*exp(-x/timeconstant) - For standard window functions in the signal processing toolbox see WINDOW. (b) vector of length nSamples, used directly as window

**cfg.winfuncopt** - [ft_spikedensity](/reference/ft_spikedensity)  
options that go with cfg.winfunc For cfg.winfunc = 'alpha': the timeconstant in seconds (default = 0.005s) For cfg.winfunc = 'gauss': the standard deviation in seconds (default = 1/4 of window duration in seconds) For cfg.winfunc = 'wname' with 'wname' any standard window function see window opts in that function and add as cell-array If cfg.winfunctopt = [], default opts are taken.

**cfg.winlen** - [ft_spike_plot_jpsth](/reference/ft_spike_plot_jpsth)  
window length in seconds (default = 5*binwidth). length of our window is 2*round*(cfg.winlen/binwidth) where binwidth is the binwidth of the jpsth (jpsth.time(2)-jpsth.time(1)).

**cfg.winlen** - [ft_spike_plot_isireturn](/reference/ft_spike_plot_isireturn)  
window length in seconds (default = 5*cfg.dt). The total length of our window is 2*round*(cfg.winlen/cfg.dt) +1;

**cfg.winstepsize** - [ft_spiketriggeredspectrum_stat](/reference/ft_spiketriggeredspectrum_stat)  
double, stepsize of sliding window in seconds. For example if cfg.winstepsize = 0.1, we compute stat every other 100 ms.

**cfg.write** - [ft_volumenormalise](/reference/ft_volumenormalise)  
'no' (default) or 'yes', writes the segmented volumes to SPM2 compatible analyze-file, with the suffix _anatomy for the anatomical MRI volume _param for each of the functional volumes

**cfg.write** - [ft_volumesegment](/reference/ft_volumesegment)  
'no' or 'yes' (default = 'no'), writes the probabilistic tissue maps to SPM compatible analyze (spm2), or nifti (spm8/spm12) files, with the suffix (spm2) _seg1, for the gray matter segmentation _seg2, for the white matter segmentation _seg3, for the csf segmentation or with the prefix (spm8, and spm12 with spmmethod='old') c1, for the gray matter segmentation c2, for the white matter segmentation c3, for the csf segmentation when using spm12 with spmmethod='new' there'll be 3 additional tissue types c4, for the bone segmentation c5, for the soft tissue segmentation c6, for the air segmentation when using spm12 with spmmethod='mars' the tpms will be postprocessed with the mars toolbox, yielding smoother% segmentations in general.

**cfg.wvar** - [ft_statistics_analytic](/reference/ft_statistics_analytic)  
number or list with indices, within-block variable(s)

**cfg.wvar** - [ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)  
number or list with indices, within-cell variable(s)

## X 

**cfg.xgrid** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
vector (e.g. -20:1:20) or 'auto' (default = 'auto')

**cfg.xlim** - [ft_movieplotER](/reference/ft_movieplotER), [ft_multiplotER](/reference/ft_multiplotER), [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotER](/reference/ft_singleplotER), [ft_singleplotTFR](/reference/ft_singleplotTFR)  
'maxmin' or [xmin xmax] (default = 'maxmin')

**cfg.xlim** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
[min max], range in cm to plot (default = [-15 15])

**cfg.xlim** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
limit for 1st dimension in data (e.g., time), can be 'maxmin' or [xmin xmax] (default = 'maxmin')

**cfg.xlim** - [ft_connectivityplot](/reference/ft_connectivityplot)  
selection boundaries over first dimension in data (e.g., freq) 'maxmin' or [xmin xmax] (default = 'maxmin')

**cfg.xlim** - [ft_movieplotTFR](/reference/ft_movieplotTFR)  
selection boundaries over first dimension in data (e.g., time) 'maxmin' or [xmin xmax] (default = 'maxmin')

**cfg.xrange** - [ft_volumereslice](/reference/ft_volumereslice)  
[min max], in physical units

## Y 

**cfg.ygrid** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
vector (e.g. -20:1:20) or 'auto' (default = 'auto')

**cfg.ylim** - [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotTFR](/reference/ft_singleplotTFR)  
'maxmin' or [ymin ymax] (default = 'maxmin')

**cfg.ylim** - [ft_multiplotER](/reference/ft_multiplotER), [ft_singleplotER](/reference/ft_singleplotER)  
'maxmin', 'maxabs', 'zeromax', 'minzero', or [ymin ymax] (default = 'maxmin')

**cfg.ylim** - [ft_spike_plot_isi](/reference/ft_spike_plot_isi)  
[min max] or 'auto' (default) If 'auto', we plot from 0 to 110% of maximum plotted value);

**cfg.ylim** - [ft_spike_plot_psth](/reference/ft_spike_plot_psth)  
[min max] or 'auto' (default) If 'standard', we plot from 0 to 110% of maximum plotted value);

**cfg.ylim** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
[min max], range in cm to plot (default = [-15 15])

**cfg.ylim** - [ft_topoplotTFR](/reference/ft_topoplotTFR)  
limit for 2nd dimension in data (e.g., freq), can be 'maxmin' or [ymin ymax] (default = 'maxmin')

**cfg.ylim** - [ft_movieplotTFR](/reference/ft_movieplotTFR)  
selection boundaries over second dimension in data (e.g., freq) 'maxmin' or [xmin xmax] (default = 'maxmin')

**cfg.ylim** - [ft_connectivityplot](/reference/ft_connectivityplot)  
selection boundaries over second dimension in data (i.e. ,time, if present), 'maxmin', or [ymin ymax] (default = 'maxmin')

**cfg.ylim** - [ft_databrowser](/reference/ft_databrowser)  
vertical scaling, can be 'maxmin', 'maxabs' or [ymin ymax] (default = 'maxabs')

**cfg.yrange** - [ft_volumereslice](/reference/ft_volumereslice)  
[min max], in physical units

## Z 

**cfg.zgrid** - [ft_dipolefitting](/reference/ft_dipolefitting), [ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel), [ft_sourceanalysis](/reference/ft_sourceanalysis)  
vector (e.g. 0:1:20) or 'auto' (default = 'auto')

**cfg.zlim** - [ft_realtime_headlocalizer](/reference/ft_realtime_headlocalizer)  
[min max], range in cm to plot (default is automatic)

**cfg.zlim** - [ft_databrowser](/reference/ft_databrowser)  
color scaling to apply to component topographies, 'minmax', 'maxabs' (default = 'maxmin')

**cfg.zlim** - [ft_topoplotER](/reference/ft_topoplotER), [ft_topoplotTFR](/reference/ft_topoplotTFR)  
limits for color dimension, 'maxmin', 'maxabs', 'zeromax', 'minzero', or [zmin zmax] (default = 'maxmin')

**cfg.zlim** - [ft_icabrowser](/reference/ft_icabrowser)  
plotting limits for color dimension of topoplot, 'maxmin', 'maxabs', 'zeromax', 'minzero', or [zmin zmax] (default = 'maxmin')

**cfg.zlim** - [ft_connectivityplot](/reference/ft_connectivityplot)  
plotting limits for color dimension, 'maxmin', 'maxabs' or [zmin zmax] (default = 'maxmin')

**cfg.zlim** - [ft_movieplotER](/reference/ft_movieplotER), [ft_movieplotTFR](/reference/ft_movieplotTFR), [ft_multiplotTFR](/reference/ft_multiplotTFR), [ft_singleplotTFR](/reference/ft_singleplotTFR), [ft_topoplotIC](/reference/ft_topoplotIC)  
plotting limits for color dimension, 'maxmin', 'maxabs', 'zeromax', 'minzero', or [zmin zmax] (default = 'maxmin')

**cfg.zrange** - [ft_volumereslice](/reference/ft_volumereslice)  
[min max], in physical units

**cfg.zscore** - [ft_mvaranalysis](/reference/ft_mvaranalysis)  
'no' (default) or 'yes' specifies whether the channel data are z-transformed prior to the model fit. This may be necessary if the magnitude of the signals is very different e.g. when fitting a model to combined MEG/EMG data

**cfg.zscore** - [ft_denoise_pca](/reference/ft_denoise_pca)  
standardise reference data prior to PCA (default = 'no')

**cfg.zthresh.mindist** - [ft_spikedetection](/reference/ft_spikedetection)  
mininum distance in samples between detected peaks

**cfg.zthresh.neg** - [ft_spikedetection](/reference/ft_spikedetection)  
negative threshold, e.g. -3

**cfg.zthresh.offset** - [ft_spikedetection](/reference/ft_spikedetection)  
number of samples before peak (default = 16)

**cfg.zthresh.pos** - [ft_spikedetection](/reference/ft_spikedetection)  
positive threshold, e.g. 3

