---
title: Reference documentation
tags: [cfg, timelock, freq, source, headmodel, statistics, plotting]
---

# Reference documentation

This page links to the reference documentation for the most important FieldTrip functions, organized by category. If you are looking for the papers that describe the algorithms implemented in FieldTrip, please look at the [references to implemented methods](/references_to_implemented_methods).

A complete overview with all configuration options is available in the [configuration index](/configuration).

Note that this reference documentation is identical to the help text that is displayed in MATLAB when you type `help functionname`.

## Description of the data structures

- [ft_datatype_raw](/reference/utilities/ft_datatype_raw)
- [ft_datatype_timelock](/reference/utilities/ft_datatype_timelock)
- [ft_datatype_freq](/reference/utilities/ft_datatype_freq)
- [ft_datatype_comp](/reference/utilities/ft_datatype_comp)
- [ft_datatype_source](/reference/utilities/ft_datatype_source)
- [ft_datatype_volume](/reference/utilities/ft_datatype_volume)
- [ft_datatype_dip](/reference/utilities/ft_datatype_dip)
- [ft_datatype_mvar](/reference/utilities/ft_datatype_mvar)
- [ft_datatype_parcellation](/reference/utilities/ft_datatype_parcellation)
- [ft_datatype_segmentation](/reference/utilities/ft_datatype_segmentation)
- [ft_datatype_spike](/reference/utilities/ft_datatype_spike)
- [ft_datatype_sens](/reference/utilities/ft_datatype_sens)
- [ft_datatype_headmodel](/reference/utilities/ft_datatype_headmodel)

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
- [ft_statfun_actvsblT](/reference/statfun/ft_statfun_actvsblT)
- [ft_statfun_depsamplesFunivariate](/reference/statfun/ft_statfun_depsamplesFunivariate)
- [ft_statfun_depsamplesFmultivariate](/reference/statfun/ft_statfun_depsamplesFmultivariate)
- [ft_statfun_depsamplesT](/reference/statfun/ft_statfun_depsamplesT)
- [ft_statfun_depsamplesregrT](/reference/statfun/ft_statfun_depsamplesregrT)
- [ft_statfun_diff](/reference/statfun/ft_statfun_diff)
- [ft_statfun_diff_itc](/reference/statfun/ft_statfun_diff_itc)
- [ft_statfun_indepsamplesF](/reference/statfun/ft_statfun_indepsamplesF)
- [ft_statfun_indepsamplesT](/reference/statfun/ft_statfun_indepsamplesT)
- [ft_statfun_indepsamplesZcoh](/reference/statfun/ft_statfun_indepsamplesZcoh)
- [ft_statfun_indepsamplesregrT](/reference/statfun/ft_statfun_indepsamplesregrT)
- [ft_statfun_mean](/reference/statfun/ft_statfun_mean)
- [ft_statfun_pooledT](/reference/statfun/ft_statfun_pooledT)
- [ft_statfun_roc](/reference/statfun/ft_statfun_roc)

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

- [ft_preproc_bandpassfilter](/reference/preproc/ft_preproc_bandpassfilter)
- [ft_preproc_bandstopfilter](/reference/preproc/ft_preproc_bandstopfilter)
- [ft_preproc_baselinecorrect](/reference/preproc/ft_preproc_baselinecorrect)
- [ft_preproc_denoise](/reference/preproc/ft_preproc_denoise)
- [ft_preproc_derivative](/reference/preproc/ft_preproc_derivative)
- [ft_preproc_detrend](/reference/preproc/ft_preproc_detrend)
- [ft_preproc_dftfilter](/reference/preproc/ft_preproc_dftfilter)
- [ft_preproc_highpassfilter](/reference/preproc/ft_preproc_highpassfilter)
- [ft_preproc_hilbert](/reference/preproc/ft_preproc_hilbert)
- [ft_preproc_lowpassfilter](/reference/preproc/ft_preproc_lowpassfilter)
- [ft_preproc_medianfilter](/reference/preproc/ft_preproc_medianfilter)
- [ft_preproc_rectify](/reference/preproc/ft_preproc_rectify)
- [ft_preproc_rereference](/reference/preproc/ft_preproc_rereference)
- [ft_preproc_standardize](/reference/preproc/ft_preproc_standardize)

### ... from the fileio module

- [ft_chantype](/reference/fileio/ft_chantype)
- [ft_filetype](/reference/fileio/ft_filetype)
- [ft_filter_event](/reference/fileio/ft_filter_event)
- [ft_flush_data](/reference/fileio/ft_flush_data)
- [ft_flush_event](/reference/fileio/ft_flush_event)
- [ft_flush_header](/reference/fileio/ft_flush_header)
- [ft_read_data](/reference/fileio/ft_read_data)
- [ft_read_event](/reference/fileio/ft_read_event)
- [ft_read_header](/reference/fileio/ft_read_header)
- [ft_read_headshape](/reference/fileio/ft_read_headshape)
- [ft_read_headmodel](/reference/fileio/ft_read_headmodel)
- [ft_read_mri](/reference/fileio/ft_read_mri)
- [ft_read_sens](/reference/fileio/ft_read_sens)
- [ft_read_spike](/reference/fileio/ft_read_spike)
- [ft_write_data](/reference/fileio/ft_write_data)
- [ft_write_event](/reference/fileio/ft_write_event)

### ... from the plotting module

- [ft_plot_axes](/reference/plotting/ft_plot_axes)
- [ft_plot_box](/reference/plotting/ft_plot_box)
- [ft_plot_cloud](/reference/plotting/ft_plot_cloud)
- [ft_plot_crosshair](/reference/plotting/ft_plot_crosshair)
- [ft_plot_dipole](/reference/plotting/ft_plot_dipole)
- [ft_plot_headshape](/reference/plotting/ft_plot_headshape)
- [ft_plot_headmodel](/reference/plotting/ft_plot_headmodel)
- [ft_plot_layout](/reference/plotting/ft_plot_layout)
- [ft_plot_line](/reference/plotting/ft_plot_line)
- [ft_plot_matrix](/reference/plotting/ft_plot_matrix)
- [ft_plot_mesh](/reference/plotting/ft_plot_mesh)
- [ft_plot_montage](/reference/plotting/ft_plot_montage)
- [ft_plot_ortho](/reference/plotting/ft_plot_ortho)
- [ft_plot_patch](/reference/plotting/ft_plot_patch)
- [ft_plot_sens](/reference/plotting/ft_plot_sens)
- [ft_plot_slice](/reference/plotting/ft_plot_slice)
- [ft_plot_text](/reference/plotting/ft_plot_text)
- [ft_plot_topo](/reference/plotting/ft_plot_topo)
- [ft_plot_topo3d](/reference/plotting/ft_plot_topo3d)
- [ft_plot_vector](/reference/plotting/ft_plot_vector)

### ... from the forward module

- [ft_estimate_units](/reference/forward/ft_estimate_units)
- [ft_convert_units](/reference/forward/ft_convert_units)
- [ft_senstype](/reference/forward/ft_senstype)
- [ft_voltype](/reference/forward/ft_voltype)
- [ft_headmodel_asa](/reference/forward/ft_headmodel_asa)
- [ft_headmodel_bemcp](/reference/forward/ft_headmodel_bemcp)
- [ft_headmodel_concentricspheres](/reference/forward/ft_headmodel_concentricspheres)
- [ft_headmodel_dipoli](/reference/forward/ft_headmodel_dipoli)
- [ft_headmodel_halfspace](/reference/forward/ft_headmodel_halfspace)
- [ft_headmodel_infinite](/reference/forward/ft_headmodel_infinite)
- [ft_headmodel_localspheres](/reference/forward/ft_headmodel_localspheres)
- [ft_headmodel_openmeeg](/reference/forward/ft_headmodel_openmeeg)
- [ft_headmodel_singleshell](/reference/forward/ft_headmodel_singleshell)
- [ft_headmodel_singlesphere](/reference/forward/ft_headmodel_singlesphere)
- [ft_prepare_vol_sens](/reference/forward/ft_prepare_vol_sens)
- [ft_compute_leadfield](/reference/forward/ft_compute_leadfield)

### ... from the specest module

- [ft_specest_mtmconvol](/reference/specest/ft_specest_mtmconvol)
- [ft_specest_mtmfft](/reference/specest/ft_specest_mtmfft)
- [ft_specest_wavelet](/reference/specest/ft_specest_wavelet)
- [ft_specest_mtmconvol](/reference/specest/ft_specest_mtmconvol)
- [ft_specest_hilbert](/reference/specest/ft_specest_hilbert)
- [ft_specest_irasa](/reference/specest/ft_specest_irasa)

### ... for distributed computing on a Torque or SGE cluster

- [qsubcellfun](/reference/qsub/qsubcellfun)
- [qsubfeval](/reference/qsub/qsubfeval)
- [qsubget](/reference/qsub/qsubget)
- [qsublist](/reference/qsub/qsublist)
