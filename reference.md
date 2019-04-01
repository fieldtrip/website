---
title: Reference documentation
tags: [cfg, timelock, freq, source, headmodel, statistics, plot]
---

# Reference documentation

The reference documentation is provided here for your convenience. In the first part of this page the most important FieldTrip functions are listed by category. In the second part of this page you will find an alphabetical list of all FieldTrip functions.

A complete overview with all configuration options is available in the [configuration index](/reference/configuration).

If you are looking for the papers that describe the algorithms implemented in FieldTrip, please look at the [references to implemented methods](/references_to_implemented_methods).

This reference documentation is automatically generated from the MATLAB code every day. Therefore you should not edit these pages manually, since your changes would be overwritten automatically. If you want to suggest corrections to the documentation, please send them by email to the mailing list or to one of the main developers (see [contact](/contact)).

Note that this reference documentation is identical to the help text that is displayed in MATLAB when you type "help functionname".

## Description of the data structures

- [ft_datatype_raw](/reference/ft_datatype_raw)
- [ft_datatype_timelock](/reference/ft_datatype_timelock)
- [ft_datatype_freq](/reference/ft_datatype_freq)
- [ft_datatype_comp](/reference/ft_datatype_comp)
- [ft_datatype_source](/reference/ft_datatype_source)
- [ft_datatype_volume](/reference/ft_datatype_volume)
- [ft_datatype_dip](/reference/ft_datatype_dip)
- [ft_datatype_mvar](/reference/ft_datatype_mvar)
- [ft_datatype_parcellation](/reference/ft_datatype_parcellation)
- [ft_datatype_segmentation](/reference/ft_datatype_segmentation)
- [ft_datatype_spike](/reference/ft_datatype_spike)
- [ft_datatype_sens](/reference/ft_datatype_sens)
- [ft_datatype_headmodel](/reference/ft_datatype_headmodel)

## Preprocessing, reading and converting data

- [ft_definetrial](/reference/ft_definetrial)
- [ft_artifact_eog](/reference/ft_artifact_eog)
- [ft_artifact_jump](/reference/ft_artifact_jump)
- [ft_artifact_muscle](/reference/ft_artifact_muscle)
- [ft_rejectartifact](/reference/ft_rejectartifact)
- [ft_rejectvisual](/reference/ft_rejectvisual)
- [ft_preprocessing](/reference/ft_preprocessing)
- [ft_appenddata](/reference/ft_appenddata)
- [ft_resampledata](/reference/ft_resampledata)
- [ft_channelrepair](/reference/ft_channelrepair)
- [ft_recodeevent](/reference/ft_recodeevent)
- [ft_redefinetrial](/reference/ft_redefinetrial)

## Event-Related Fields or Potentials

- [ft_timelockanalysis](/reference/ft_timelockanalysis)
- [ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)
- [ft_timelockstatistics](/reference/ft_timelockstatistics)
- [ft_singleplotER](/reference/ft_singleplotER)
- [ft_topoplotER](/reference/ft_topoplotER)
- [ft_multiplotER](/reference/ft_multiplotER)

## Frequency and Time-Frequency analysis

- [ft_freqanalysis](/reference/ft_freqanalysis)
- [ft_freqbaseline](/reference/ft_freqbaseline)
- [ft_freqgrandaverage](/reference/ft_freqgrandaverage)
- [ft_freqdescriptives](/reference/ft_freqdescriptives)
- [ft_freqstatistics](/reference/ft_freqstatistics)
- [ft_singleplotTFR](/reference/ft_singleplotTFR)
- [ft_topoplotTFR](/reference/ft_topoplotTFR)
- [ft_multiplotTFR](/reference/ft_multiplotTFR)

## Source analysis

- [ft_dipolefitting](/reference/ft_dipolefitting)
- [ft_dipolesimulation](/reference/ft_dipolesimulation)
- [ft_sourceanalysis](/reference/ft_sourceanalysis)
- [ft_sourcegrandaverage](/reference/ft_sourcegrandaverage)
- [ft_sourcedescriptives](/reference/ft_sourcedescriptives)
- [ft_sourcestatistics](/reference/ft_sourcestatistics)
- [ft_sourceparcellate](/reference/ft_sourceparcellate)
- [ft_sourceplot](/reference/ft_sourceplot)
- [ft_sourceinterpolate](/reference/ft_sourceinterpolate)
- [ft_prepare_leadfield](/reference/ft_prepare_leadfield)
- [ft_volumelookup](/reference/ft_volumelookup)
- [ft_volumenormalise](/reference/ft_volumenormalise)
- [ft_volumesegment](/reference/ft_volumesegment)

## Statistical analysis

- [ft_timelockstatistics](/reference/ft_timelockstatistics)
- [ft_freqstatistics](/reference/ft_freqstatistics)
- [ft_sourcestatistics](/reference/ft_sourcestatistics)
- [ft_statfun_actvsblT](/reference/ft_statfun_actvsblT)
- [ft_statfun_depsamplesFunivariate](/reference/ft_statfun_depsamplesFunivariate)
- [ft_statfun_depsamplesFmultivariate](/reference/ft_statfun_depsamplesFmultivariate)
- [ft_statfun_depsamplesT](/reference/ft_statfun_depsamplesT)
- [ft_statfun_depsamplesregrT](/reference/ft_statfun_depsamplesregrT)
- [ft_statfun_diff](/reference/ft_statfun_diff)
- [ft_statfun_diff_itc](/reference/ft_statfun_diff_itc)
- [ft_statfun_indepsamplesF](/reference/ft_statfun_indepsamplesF)
- [ft_statfun_indepsamplesT](/reference/ft_statfun_indepsamplesT)
- [ft_statfun_indepsamplesZcoh](/reference/ft_statfun_indepsamplesZcoh)
- [ft_statfun_indepsamplesregrT](/reference/ft_statfun_indepsamplesregrT)
- [ft_statfun_mean](/reference/ft_statfun_mean)
- [ft_statfun_pooledT](/reference/ft_statfun_pooledT)
- [ft_statfun_roc](/reference/ft_statfun_roc)

## Plotting and display of data

- [ft_clusterplot](/reference/ft_clusterplot)
- [ft_layoutplot](/reference/ft_layoutplot)
- [ft_movieplotER](/reference/ft_movieplotER)
- [ft_movieplotTFR](/reference/ft_movieplotTFR)
- [ft_multiplotCC](/reference/ft_multiplotCC)
- [ft_multiplotER](/reference/ft_multiplotER)
- [ft_multiplotTFR](/reference/ft_multiplotTFR)
- [ft_mvaranalysis](/reference/ft_mvaranalysis)
- [ft_neighbourplot](/reference/ft_neighbourplot)
- [ft_prepare_layout](/reference/ft_prepare_layout)
- [ft_singleplotER](/reference/ft_singleplotER)
- [ft_singleplotTFR](/reference/ft_singleplotTFR)
- [ft_sourceplot](/reference/ft_sourceplot)
- [ft_topoplotER](/reference/ft_topoplotER)
- [ft_topoplotIC](/reference/ft_topoplotIC)
- [ft_topoplotTFR](/reference/ft_topoplotTFR)

## Low-level functions ...

### ... from the preproc module

- [ft_preproc_bandpassfilter](/reference/ft_preproc_bandpassfilter)
- [ft_preproc_bandstopfilter](/reference/ft_preproc_bandstopfilter)
- [ft_preproc_baselinecorrect](/reference/ft_preproc_baselinecorrect)
- [ft_preproc_denoise](/reference/ft_preproc_denoise)
- [ft_preproc_derivative](/reference/ft_preproc_derivative)
- [ft_preproc_detrend](/reference/ft_preproc_detrend)
- [ft_preproc_dftfilter](/reference/ft_preproc_dftfilter)
- [ft_preproc_highpassfilter](/reference/ft_preproc_highpassfilter)
- [ft_preproc_hilbert](/reference/ft_preproc_hilbert)
- [ft_preproc_lowpassfilter](/reference/ft_preproc_lowpassfilter)
- [ft_preproc_medianfilter](/reference/ft_preproc_medianfilter)
- [ft_preproc_rectify](/reference/ft_preproc_rectify)
- [ft_preproc_rereference](/reference/ft_preproc_rereference)
- [ft_preproc_standardize](/reference/ft_preproc_standardize)

### ... from the fileio module

- [ft_chantype](/reference/ft_chantype)
- [ft_filetype](/reference/ft_filetype)
- [ft_filter_event](/reference/ft_filter_event)
- [ft_flush_data](/reference/ft_flush_data)
- [ft_flush_event](/reference/ft_flush_event)
- [ft_flush_header](/reference/ft_flush_header)
- [ft_read_data](/reference/ft_read_data)
- [ft_read_event](/reference/ft_read_event)
- [ft_read_header](/reference/ft_read_header)
- [ft_read_headshape](/reference/ft_read_headshape)
- [ft_read_mri](/reference/ft_read_mri)
- [ft_read_sens](/reference/ft_read_sens)
- [ft_read_spike](/reference/ft_read_spike)
- [ft_read_vol](/reference/ft_read_vol)
- [ft_write_data](/reference/ft_write_data)
- [ft_write_event](/reference/ft_write_event)

### ... from the plotting module

- [ft_plot_axes](/reference/ft_plot_axes)
- [ft_plot_box](/reference/ft_plot_box)
- [ft_plot_cloud](/reference/ft_plot_cloud)
- [ft_plot_crosshair](/reference/ft_plot_crosshair)
- [ft_plot_dipole](/reference/ft_plot_dipole)
- [ft_plot_headshape](/reference/ft_plot_headshape)
- [ft_plot_layout](/reference/ft_plot_layout)
- [ft_plot_line](/reference/ft_plot_line)
- [ft_plot_matrix](/reference/ft_plot_matrix)
- [ft_plot_mesh](/reference/ft_plot_mesh)
- [ft_plot_montage](/reference/ft_plot_montage)
- [ft_plot_ortho](/reference/ft_plot_ortho)
- [ft_plot_patch](/reference/ft_plot_patch)
- [ft_plot_sens](/reference/ft_plot_sens)
- [ft_plot_slice](/reference/ft_plot_slice)
- [ft_plot_text](/reference/ft_plot_text)
- [ft_plot_topo](/reference/ft_plot_topo)
- [ft_plot_topo3d](/reference/ft_plot_topo3d)
- [ft_plot_vector](/reference/ft_plot_vector)
- [ft_plot_vol](/reference/ft_plot_vol)

### ... from the forward module

- [ft_compute_leadfield](/reference/ft_compute_leadfield)
- [ft_convert_units](/reference/ft_convert_units)
- [ft_estimate_units](/reference/ft_estimate_units)
- [ft_senstype](/reference/ft_senstype)
- [ft_voltype](/reference/ft_voltype)
- [ft_prepare_vol_sens](/reference/ft_prepare_vol_sens)
- [ft_headmodel_asa](/reference/ft_headmodel_asa)
- [ft_headmodel_bemcp](/reference/ft_headmodel_bemcp)
- [ft_headmodel_concentricspheres](/reference/ft_headmodel_concentricspheres)
- [ft_headmodel_dipoli](/reference/ft_headmodel_dipoli)
- [ft_headmodel_halfspace](/reference/ft_headmodel_halfspace)
- [ft_headmodel_infinite](/reference/ft_headmodel_infinite)
- [ft_headmodel_localspheres](/reference/ft_headmodel_localspheres)
- [ft_headmodel_openmeeg](/reference/ft_headmodel_openmeeg)
- [ft_headmodel_singleshell](/reference/ft_headmodel_singleshell)
- [ft_headmodel_singlesphere](/reference/ft_headmodel_singlesphere)
- [ft_senslabel](/reference/ft_senslabel)
- [ft_transform_headshape](/reference/ft_transform_headshape)
- [ft_transform_sens](/reference/ft_transform_sens)
- [ft_transform_vol](/reference/ft_transform_vol)
- [ft_apply_montage](/reference/ft_apply_montage)
- [ft_inside_vol](/reference/ft_inside_vol)
- [ft_sourcedepth](/reference/ft_sourcedepth)

### ... from the specest module

- [ft_specest_mtmconvol](/reference/ft_specest_mtmconvol)
- [ft_specest_mtmfft](/reference/ft_specest_mtmfft)
- [ft_specest_wavelet](/reference/ft_specest_wavelet)
- [ft_specest_mtmconvol](/reference/ft_specest_mtmconvol)
- [ft_specest_hilbert](/reference/ft_specest_hilbert)

### ... for distributed computing on a Torque or SGE cluster

- [qsubcellfun](/reference/qsubcellfun)
- [qsubfeval](/reference/qsubfeval)
- [qsubget](/reference/qsubget)
- [qsublist](/reference/qsublist)

### ... for distributed computing on a multi-core computer

- [enginecellfun](/reference/enginecellfun)
- [engineexec](/reference/engineexec)
- [enginefeval](/reference/enginefeval)
- [engineget](/reference/engineget)
- [enginepool](/reference/enginepool)

### ... for distributed computing using peer-to-peer

- [peercellfun](/reference/peercellfun)
- [peerfeval](/reference/peerfeval)
- [peerget](/reference/peerget)
- [peermaster](/reference/peermaster)
- [peerslave](/reference/peerslave)
- [peerzombie](/reference/peerzombie)
- [peerinfo](/reference/peerinfo)
- [peerlist](/reference/peerlist)
- [peerreset](/reference/peerreset)
