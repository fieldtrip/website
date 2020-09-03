---
title: Reference documentation
tags: [cfg, timelock, freq, source, headmodel, statistics, plotting]
---

# Reference documentation

The reference documentation is provided here for your convenience. This page lists the most important FieldTrip functions by category.

A complete overview with all configuration options is available in the [configuration index](https://github.com/fieldtrip/fieldtrip/blob/release/configuration).

If you are looking for the papers that describe the algorithms implemented in FieldTrip, please look at the [references to implemented methods](/references_to_implemented_methods).

Note that this reference documentation is identical to the help text that is displayed in MATLAB when you type "help functionname".

## Description of the data structures

- [ft_datatype_raw](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_raw.m)
- [ft_datatype_timelock](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_timelock.m)
- [ft_datatype_freq](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_freq.m)
- [ft_datatype_comp](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_comp.m)
- [ft_datatype_source](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_source.m)
- [ft_datatype_volume](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_volume.m)
- [ft_datatype_dip](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_dip.m)
- [ft_datatype_mvar](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_mvar.m)
- [ft_datatype_parcellation](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_parcellation.m)
- [ft_datatype_segmentation](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_segmentation.m)
- [ft_datatype_spike](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_spike.m)
- [ft_datatype_sens](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_sens.m)
- [ft_datatype_headmodel](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_datatype_headmodel.m)

## Preprocessing, reading and converting data

- [ft_definetrial](https://github.com/fieldtrip/fieldtrip/blob/release/ft_definetrial.m)
- [ft_artifact_eog](https://github.com/fieldtrip/fieldtrip/blob/release/ft_artifact_eog.m)
- [ft_artifact_jump](https://github.com/fieldtrip/fieldtrip/blob/release/ft_artifact_jump.m)
- [ft_artifact_muscle](https://github.com/fieldtrip/fieldtrip/blob/release/ft_artifact_muscle.m)
- [ft_rejectartifact](https://github.com/fieldtrip/fieldtrip/blob/release/ft_rejectartifact.m)
- [ft_rejectvisual](https://github.com/fieldtrip/fieldtrip/blob/release/ft_rejectvisual.m)
- [ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)
- [ft_appenddata](https://github.com/fieldtrip/fieldtrip/blob/release/ft_appenddata.m)
- [ft_resampledata](https://github.com/fieldtrip/fieldtrip/blob/release/ft_resampledata.m)
- [ft_channelrepair](https://github.com/fieldtrip/fieldtrip/blob/release/ft_channelrepair.m)
- [ft_recodeevent](https://github.com/fieldtrip/fieldtrip/blob/release/ft_recodeevent.m)
- [ft_redefinetrial](https://github.com/fieldtrip/fieldtrip/blob/release/ft_redefinetrial.m)

## Event-Related Fields or Potentials

- [ft_timelockanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_timelockanalysis.m)
- [ft_timelockgrandaverage](https://github.com/fieldtrip/fieldtrip/blob/release/ft_timelockgrandaverage.m)
- [ft_timelockstatistics](https://github.com/fieldtrip/fieldtrip/blob/release/ft_timelockstatistics.m)
- [ft_singleplotER](https://github.com/fieldtrip/fieldtrip/blob/release/ft_singleplotER.m)
- [ft_topoplotER](https://github.com/fieldtrip/fieldtrip/blob/release/ft_topoplotER.m)
- [ft_multiplotER](https://github.com/fieldtrip/fieldtrip/blob/release/ft_multiplotER.m)

## Frequency and Time-Frequency analysis

- [ft_freqanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_freqanalysis.m)
- [ft_freqbaseline](https://github.com/fieldtrip/fieldtrip/blob/release/ft_freqbaseline.m)
- [ft_freqgrandaverage](https://github.com/fieldtrip/fieldtrip/blob/release/ft_freqgrandaverage.m)
- [ft_freqdescriptives](https://github.com/fieldtrip/fieldtrip/blob/release/ft_freqdescriptives.m)
- [ft_freqstatistics](https://github.com/fieldtrip/fieldtrip/blob/release/ft_freqstatistics.m)
- [ft_singleplotTFR](https://github.com/fieldtrip/fieldtrip/blob/release/ft_singleplotTFR.m)
- [ft_topoplotTFR](https://github.com/fieldtrip/fieldtrip/blob/release/ft_topoplotTFR.m)
- [ft_multiplotTFR](https://github.com/fieldtrip/fieldtrip/blob/release/ft_multiplotTFR.m)

## Source analysis

- [ft_dipolefitting](https://github.com/fieldtrip/fieldtrip/blob/release/ft_dipolefitting.m)
- [ft_dipolesimulation](https://github.com/fieldtrip/fieldtrip/blob/release/ft_dipolesimulation.m)
- [ft_sourceanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_sourceanalysis.m)
- [ft_sourcegrandaverage](https://github.com/fieldtrip/fieldtrip/blob/release/ft_sourcegrandaverage.m)
- [ft_sourcedescriptives](https://github.com/fieldtrip/fieldtrip/blob/release/ft_sourcedescriptives.m)
- [ft_sourcestatistics](https://github.com/fieldtrip/fieldtrip/blob/release/ft_sourcestatistics.m)
- [ft_sourceparcellate](https://github.com/fieldtrip/fieldtrip/blob/release/ft_sourceparcellate.m)
- [ft_sourceplot](https://github.com/fieldtrip/fieldtrip/blob/release/ft_sourceplot.m)
- [ft_sourceinterpolate](https://github.com/fieldtrip/fieldtrip/blob/release/ft_sourceinterpolate.m)
- [ft_prepare_leadfield](https://github.com/fieldtrip/fieldtrip/blob/release/ft_prepare_leadfield.m)
- [ft_volumelookup](https://github.com/fieldtrip/fieldtrip/blob/release/ft_volumelookup.m)
- [ft_volumenormalise](https://github.com/fieldtrip/fieldtrip/blob/release/ft_volumenormalise.m)
- [ft_volumesegment](https://github.com/fieldtrip/fieldtrip/blob/release/ft_volumesegment.m)

## Statistical analysis

- [ft_timelockstatistics](https://github.com/fieldtrip/fieldtrip/blob/release/ft_timelockstatistics.m)
- [ft_freqstatistics](https://github.com/fieldtrip/fieldtrip/blob/release/ft_freqstatistics.m)
- [ft_sourcestatistics](https://github.com/fieldtrip/fieldtrip/blob/release/ft_sourcestatistics.m)
- [ft_statfun_actvsblT](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_actvsblT.m)
- [ft_statfun_depsamplesFunivariate](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_depsamplesFunivariate.m)
- [ft_statfun_depsamplesFmultivariate](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_depsamplesFmultivariate.m)
- [ft_statfun_depsamplesT](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_depsamplesT.m)
- [ft_statfun_depsamplesregrT](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_depsamplesregrT.m)
- [ft_statfun_diff](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_diff.m)
- [ft_statfun_diff_itc](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_diff_itc.m)
- [ft_statfun_indepsamplesF](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_indepsamplesF.m)
- [ft_statfun_indepsamplesT](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_indepsamplesT.m)
- [ft_statfun_indepsamplesZcoh](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_indepsamplesZcoh.m)
- [ft_statfun_indepsamplesregrT](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_indepsamplesregrT.m)
- [ft_statfun_mean](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_mean.m)
- [ft_statfun_pooledT](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_pooledT.m)
- [ft_statfun_roc](https://github.com/fieldtrip/fieldtrip/blob/release/statfun/ft_statfun_roc.m)

## Plotting and display of data

- [ft_clusterplot](https://github.com/fieldtrip/fieldtrip/blob/release/ft_clusterplot.m)
- [ft_layoutplot](https://github.com/fieldtrip/fieldtrip/blob/release/ft_layoutplot.m)
- [ft_movieplotER](https://github.com/fieldtrip/fieldtrip/blob/release/ft_movieplotER.m)
- [ft_movieplotTFR](https://github.com/fieldtrip/fieldtrip/blob/release/ft_movieplotTFR.m)
- [ft_multiplotCC](https://github.com/fieldtrip/fieldtrip/blob/release/ft_multiplotCC.m)
- [ft_multiplotER](https://github.com/fieldtrip/fieldtrip/blob/release/ft_multiplotER.m)
- [ft_multiplotTFR](https://github.com/fieldtrip/fieldtrip/blob/release/ft_multiplotTFR.m)
- [ft_mvaranalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_mvaranalysis.m)
- [ft_neighbourplot](https://github.com/fieldtrip/fieldtrip/blob/release/ft_neighbourplot.m)
- [ft_prepare_layout](https://github.com/fieldtrip/fieldtrip/blob/release/ft_prepare_layout.m)
- [ft_singleplotER](https://github.com/fieldtrip/fieldtrip/blob/release/ft_singleplotER.m)
- [ft_singleplotTFR](https://github.com/fieldtrip/fieldtrip/blob/release/ft_singleplotTFR.m)
- [ft_sourceplot](https://github.com/fieldtrip/fieldtrip/blob/release/ft_sourceplot.m)
- [ft_topoplotER](https://github.com/fieldtrip/fieldtrip/blob/release/ft_topoplotER.m)
- [ft_topoplotIC](https://github.com/fieldtrip/fieldtrip/blob/release/ft_topoplotIC.m)
- [ft_topoplotTFR](https://github.com/fieldtrip/fieldtrip/blob/release/ft_topoplotTFR.m)

## Low-level functions ...

### ... from the preproc module

- [ft_preproc_bandpassfilter](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_bandpassfilter.m)
- [ft_preproc_bandstopfilter](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_bandstopfilter.m)
- [ft_preproc_baselinecorrect](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_baselinecorrect.m)
- [ft_preproc_denoise](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_denoise.m)
- [ft_preproc_derivative](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_derivative.m)
- [ft_preproc_detrend](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_detrend.m)
- [ft_preproc_dftfilter](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_dftfilter.m)
- [ft_preproc_highpassfilter](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_highpassfilter.m)
- [ft_preproc_hilbert](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_hilbert.m)
- [ft_preproc_lowpassfilter](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_lowpassfilter.m)
- [ft_preproc_medianfilter](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_medianfilter.m)
- [ft_preproc_rectify](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_rectify.m)
- [ft_preproc_rereference](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_rereference.m)
- [ft_preproc_standardize](https://github.com/fieldtrip/fieldtrip/blob/release/preproc/ft_preproc_standardize.m)

### ... from the fileio module

- [ft_chantype](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_chantype.m)
- [ft_filetype](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_filetype.m)
- [ft_filter_event](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_filter_event.m)
- [ft_flush_data](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_flush_data.m)
- [ft_flush_event](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_flush_event.m)
- [ft_flush_header](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_flush_header.m)
- [ft_read_data](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_data.m)
- [ft_read_event](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_event.m)
- [ft_read_header](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_header.m)
- [ft_read_headshape](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_headshape.m)
- [ft_read_headmodel](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_headmodel.m)
- [ft_read_mri](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_mri.m)
- [ft_read_sens](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_sens.m)
- [ft_read_spike](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_read_spike.m)
- [ft_write_data](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_write_data.m)
- [ft_write_event](https://github.com/fieldtrip/fieldtrip/blob/release/fileio/ft_write_event.m)

### ... from the plotting module

- [ft_plot_axes](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_axes.m)
- [ft_plot_box](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_box.m)
- [ft_plot_cloud](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_cloud.m)
- [ft_plot_crosshair](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_crosshair.m)
- [ft_plot_dipole](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_dipole.m)
- [ft_plot_headshape](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_headshape.m)
- [ft_plot_headmodel](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_headmodel.m)
- [ft_plot_layout](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_layout.m)
- [ft_plot_line](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_line.m)
- [ft_plot_matrix](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_matrix.m)
- [ft_plot_mesh](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_mesh.m)
- [ft_plot_montage](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_montage.m)
- [ft_plot_ortho](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_ortho.m)
- [ft_plot_patch](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_patch.m)
- [ft_plot_sens](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_sens.m)
- [ft_plot_slice](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_slice.m)
- [ft_plot_text](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_text.m)
- [ft_plot_topo](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_topo.m)
- [ft_plot_topo3d](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_topo3d.m)
- [ft_plot_vector](https://github.com/fieldtrip/fieldtrip/blob/release/plotting/ft_plot_vector.m)

### ... from the forward module

- [ft_estimate_units](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_estimate_units.m)
- [ft_convert_units](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_convert_units.m)
- [ft_senstype](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_senstype.m)
- [ft_voltype](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_voltype.m)
- [ft_headmodel_asa](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_headmodel_asa.m)
- [ft_headmodel_bemcp](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_headmodel_bemcp.m)
- [ft_headmodel_concentricspheres](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_headmodel_concentricspheres.m)
- [ft_headmodel_dipoli](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_headmodel_dipoli.m)
- [ft_headmodel_halfspace](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_headmodel_halfspace.m)
- [ft_headmodel_infinite](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_headmodel_infinite.m)
- [ft_headmodel_localspheres](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_headmodel_localspheres.m)
- [ft_headmodel_openmeeg](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_headmodel_openmeeg.m)
- [ft_headmodel_singleshell](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_headmodel_singleshell.m)
- [ft_headmodel_singlesphere](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_headmodel_singlesphere.m)
- [ft_prepare_vol_sens](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_prepare_vol_sens.m)
- [ft_compute_leadfield](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_compute_leadfield.m)

### ... from the specest module

- [ft_specest_mtmconvol](https://github.com/fieldtrip/fieldtrip/blob/release/specest/ft_specest_mtmconvol.m)
- [ft_specest_mtmfft](https://github.com/fieldtrip/fieldtrip/blob/release/specest/ft_specest_mtmfft.m)
- [ft_specest_wavelet](https://github.com/fieldtrip/fieldtrip/blob/release/specest/ft_specest_wavelet.m)
- [ft_specest_mtmconvol](https://github.com/fieldtrip/fieldtrip/blob/release/specest/ft_specest_mtmconvol.m)
- [ft_specest_hilbert](https://github.com/fieldtrip/fieldtrip/blob/release/specest/ft_specest_hilbert.m)

### ... for distributed computing on a Torque or SGE cluster

- [qsubcellfun](https://github.com/fieldtrip/fieldtrip/blob/release/qsub/qsubcellfun.m)
- [qsubfeval](https://github.com/fieldtrip/fieldtrip/blob/release/qsub/qsubfeval.m)
- [qsubget](https://github.com/fieldtrip/fieldtrip/blob/release/qsub/qsubget.m)
- [qsublist](https://github.com/fieldtrip/fieldtrip/blob/release/qsub/qsublist.m)

### ... for distributed computing on a multi-core computer

- [enginecellfun](https://github.com/fieldtrip/fieldtrip/blob/release/engine/enginecellfun.m)
- [engineexec](https://github.com/fieldtrip/fieldtrip/blob/release/engine/engineexec.m)
- [enginefeval](https://github.com/fieldtrip/fieldtrip/blob/release/engine/enginefeval.m)
- [engineget](https://github.com/fieldtrip/fieldtrip/blob/release/engine/engineget.m)
- [enginepool](https://github.com/fieldtrip/fieldtrip/blob/release/engine/enginepool.m)

### ... for distributed computing using peer-to-peer

- [peercellfun](https://github.com/fieldtrip/fieldtrip/blob/release/peer/peer/peercellfun.m)
- [peerfeval](https://github.com/fieldtrip/fieldtrip/blob/release/peer/peer/peerfeval.m)
- [peerget](https://github.com/fieldtrip/fieldtrip/blob/release/peer/peer/peerget.m)
- [peercontroller](https://github.com/fieldtrip/fieldtrip/blob/release/peer/peer/peercontroller.m)
- [peerworker](https://github.com/fieldtrip/fieldtrip/blob/release/peer/peer/peerworker.m)
- [peerzombie](https://github.com/fieldtrip/fieldtrip/blob/release/peer/peer/peerzombie.m)
- [peerinfo](https://github.com/fieldtrip/fieldtrip/blob/release/peer/peer/peerinfo.m)
- [peerlist](https://github.com/fieldtrip/fieldtrip/blob/release/peer/peer/peerlist.m)
- [peerreset](https://github.com/fieldtrip/fieldtrip/blob/release/peer/peer/peerreset.m)
