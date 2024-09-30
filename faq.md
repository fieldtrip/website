---
title: Frequently Asked Questions
category: faq
---

# Frequently Asked Questions

On this page you can find answers to a variety of FieldTrip and MATLAB related questions.

We invite you to [add your own](/contribute) example scripts or frequently asked questions on the website. Also tutorials can be added. Every time you explain somebody something about FieldTrip, please consider whether you could use the website for this, so others can learn from it as well.

See also the [tutorials](/tutorial) and [example scripts](/example).

## Reading and preprocessing data

- [How can I use the databrowser?](/faq/databrowser)
- [How can I inspect the electrode impedances of my data?](/faq/how_can_i_inspect_the_electrode_impedances_of_my_data)
- [Should I rereference my EEG data prior to, or after ICA?](/faq/ica_rereference)
- [I used to work with trl-matrices that have more than 3 columns. Why is this not supported anymore?](/faq/trialinfo_trl)
- [Why should I set continuous to yes for CTF data?](/faq/continuous)

### Specific data formats

- [How can I read EGI mff data without the JVM?](/faq/how_can_i_read_egi_mff_data_without_the_jvm)
- [How can I read all channels from an EDF file that contains multiple sampling rates?](/faq/how_can_i_read_all_channels_from_an_edf_file_that_contains_multiple_sampling_rates)
- [How does the CTF higher-order gradiometer work?](/faq/how_does_the_ctf_higher-order_gradiometer_work)
- [How can I extend the reading functions with a new dataformat?](/faq/how_can_i_extend_the_reading_functions_with_a_new_dataformat)
- [I have problems reading in neuroscan .cnt files. How can I fix this?](/faq/i_have_problems_reading_in_neuroscan_.cnt_files._how_can_i_fix_this)
- [Why are the fileio functions stateless, does the fseek not make them very slow?](/faq/fileio_stateless)
- [How can I import my own dataformat?](/faq/how_can_i_import_my_own_dataformat)
- [How can I deal with a discontinuous Neuralynx recording?](/faq/discontinuous_neuralynx)
- [How can I fix a corrupt CTF meg4 data file?](/faq/ctf_fixmeg4)
- [How can I fix a corrupt CTF res4 header file?](/faq/ctf_fixres4)
- [How can I read corrupted (unsaved) CTF data?](/faq/how_can_i_read_corrupted_unsaved_ctf_data)
- [I am having problems reading the CTF .hc headcoordinates file](/faq/ctf_fixhc)

### Data handling

- [Reading is slow, can I write my raw data to a more efficient file format?](/faq/writedata_matbin)
- [What dataformats are supported?](/faq/dataformat)
- [How can I append the files of two separate recordings?](/faq/append_files)
- [How can I convert one dataformat into another?](/faq/convert_dataformat)
- [How can I merge two datasets that were acquired simultaneously with different amplifiers?](/faq/how_can_i_merge_two_datasets_that_were_acquired_simultaneously_with_different_amplifiers)
- [How can I preprocess a dataset that is too large to fit into memory?](/faq/how_can_i_preprocess_a_dataset_that_is_too_large_to_fit_into_memory)
- [How can I rename channels in my data structure?](/faq?rename_channels)

### Trials, triggers and events

- [How can I check or decipher the sequence of triggers in my data?](/faq/triggers)
- [How can I find out what eventvalues and eventtypes there are in my data?](/faq/how_can_i_find_out_what_eventvalues_and_eventtypes_there_are_in_my_data)
- [How can I process continuous data without triggers?](/faq/how_can_i_process_continuous_data_without_triggers)
- [How can I transform trigger values from bits to decimal representation with a trialfun?](/faq/how_can_i_transform_trigger_values_from_bits_to_decimal_representation_with_a_trialfun)
- [Is it possible to keep track of trial-specific information in my FieldTrip analysis pipeline?](/faq/trialinfo)

### Artifacts

- [What kind of filters can I apply to my data?](/faq/preproc_filtertypes)
- [Do I need to resample my data, and if so, how is this to be done?](/faq/resampling_lowpassfilter)
- [I used ICA on my MEG data from before 2012 and now FieldTrip crashes, why is that?](/faq/ica_crash)
- [Why does my ICA output contain complex numbers?](/faq/ica_complexvalues)
- [How can I consistently represent artifacts in my data?](/faq/artifact_representation)
- [How can I interpret the different types of padding that I find when dealing with artifacts?](/faq/artifact_padding)
- [How does the filter padding in preprocessing work?](/faq/how_does_the_filter_padding_in_preprocessing_work)
- [Why is there a residual 50Hz line-noise component after applying a DFT filter?](/faq/why_is_there_a_residual_50hz_line-noise_component_after_applying_a_dft_filter)

## Spectral analysis

- [How can I compute inter-trial coherence?](/faq/itc)
- [How can I do time-frequency analysis on continuous data?](/faq/tfr_continuous)
- [How does mtmconvol work?](/faq/mtmconvol)
- [How to interpret the sign of the phase slope index?](/faq/how_to_interpret_the_sign_of_the_phase_slope_index)
- [In what way can frequency domain data be represented in FieldTrip?](/faq/datatype_freq)
- [What convention is used to define absolute phase in 'mtmconvol', 'wavelet' and 'mtmfft'](/faq/freqanalysis_phasedefinition)
- [What does "padding not sufficient for requested frequency resolution" mean?](/faq/freqanalysis_paddinginsufficient)
- [What is the difference between coherence and coherency?](/faq/coherence_coherency)
- [Why am I not getting exact integer frequencies?](/faq/freqanalysis_foinoninteger)
- [Why does my TFR contain NaNs?](/faq/tfr_nans)
- [Why does my TFR look strange (part I, demeaning)?](/faq/tfr_strangedemean)
- [Why does my TFR look strange (part II, detrending)?](/faq/tfr_strangedetrend)
- [Why is the largest peak in the spectrum at the frequency which is 1/segment length?](/faq/why_largest_peak_spectrum)
- [Why does my output.freq not match my cfg.foi when using 'mtmconvol' in ft_freqanalyis?](/faq/freqanalysis_foimismatchmtmconvol)
- [Why does my output.freq not match my cfg.foi when using 'mtmfft' in ft_freqanalyis?](/faq/freqanalysis_foimismatchmtmfft)
- [Why does my output.freq not match my cfg.foi when using 'wavelet' (formerly 'wltconvol') in ft_freqanalyis?](/faq/freqanalysis_foimismatchwavelet)
- [Does it make sense to subtract the ERP prior to time frequency analysis, to distinguish evoked from induced power?](/faq/evoked_vs_induced)

## Source reconstruction

- [Can I do combined EEG and MEG source reconstruction?](/faq/sourcerecon_meeg)
- [Can I restrict the source reconstruction to the grey matter?](/faq/sourcerecon_greymatter)
- [How are electrodes, magnetometers or gradiometers described?](/faq/sensors_definition)
- [How are the LPA and RPA points defined?](/faq/anat_landmarks)
- [How are the different head and MRI coordinate systems defined?](/faq/coordsys)
- [How can I check whether the grid that I have is aligned to the segmented volume and to the sensor gradiometer?](/faq/sourcrecon_checkalignment)
- [How can I convert an anatomical mri from DICOM into CTF format?](/faq/anat_dicom2ctf)
- [How can I determine the anatomical label of a source or electrode?](/faq/how_can_i_determine_the_anatomical_label_of_a_source)
- [How can I fine-tune my BEM volume conduction model?](/faq/how_can_i_fine-tune_my_bem_volume_conduction_model)
- [How can I map source locations onto an anatomical label in an atlas?](/faq/how_can_i_map_source_locations_between_two_different_representations)
- [How can I visualize the different geometrical objects that are needed for forward and inverse computations?](/faq/how_can_i_visualize_the_different_geometrical_objects_that_are_needed_for_forward_and_inverse_computations)
- [How do I install the OpenMEEG binaries?](/faq/how_do_i_install_the_openmeeg_binaries)
- [How do homogenous coordinate transformation matrices work?](/faq/homogenous)
- [How is anatomical, functional or statistical "volume data" described?](/faq/how_is_anatomical_functional_or_statistical_volume_data_described)
- [How should I specify the fiducials?](/faq/fiducial)
- [How to change the MRI orientation, the voxel size or the field-of-view?](/faq/how_change_mri_orientation_size_fov)
- [How to coregister an anatomical MRI with the gradiometer or electrode positions?](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions)
- [Is it good or bad to have dipole locations outside of the brain for which the source reconstruction is computed?](/faq/sourcerecon_outside)
- [Is it important to have accurate measurements of electrode locations for EEG source reconstruction?](/faq/sensors_accuracy)
- [My MRI is upside down, is this a problem?](/faq/anat_upsidedown)
- [Should I use a Polhemus or a Structure Sensor to record electrode positions?](/faq/structuresensor)
- [What is the conductivity of the brain, CSF, skull and skin tissue?](/faq/conductvitiy_defaults)
- [What is the difference between the ACPC, MNI, SPM and TAL coordinate systems?](/faq/acpc)
- [What material is used for the flexible MEG headcasts?](/faq/headcast)
- [What kind of volume conduction models are implemented?](/faq/datatype_headmodel)
- [Where can I find the dipoli command-line executable?](/faq/dipoli_filelocation)
- [Where is the anterior commissure?](/faq/anterior_commissure)
- [Why is there a rim around the brain for which the source reconstruction is not computed?](/faq/why_is_there_a_rim_around_the_brain_for_which_the_source_reconstruction_is_not_computed)
- [Why is the source model deformed or incorrectly aligned after warping template?](/faq/why_is_the_source_model_deformed_or_incorrectly_aligned_after_warping_template)
- [Why should I use an average reference for EEG source reconstruction?](/faq/why_should_i_use_an_average_reference_for_eeg_source_reconstruction)
- [Why does my EEG headmodel look funny?](/faq/headmodel_meshingproblem)

## Statistical analysis

- [How NOT to interpret results from a cluster-based permutation test?](/faq/clusterstats_interpretation)
- [How can I define neighbouring sensors?](/faq/sensors_neighbours)
- [How can I determine the onset of an effect?](/faq/how_can_i_determine_the_onset_of_an_effect)
- [How can I test an interaction effect using cluster-based permutation tests?](/faq/clusterstats_interaction)
- [Should I use t or F values for cluster-based permutation tests?](/faq/clusterstats_teststatistic)
- [How can I test for correlations between neuronal data and quantitative stimulus and behavioural variables?](/faq/how_can_i_test_for_correlations_between_neuronal_data_and_quantitative_stimulus_and_behavioural_variables)
- [How can I test whether a behavioral measure is phasic?](/faq/how_can_i_test_whether_a_behavioral_measure_is_phasic)
- [How can I use the ivar, uvar, wvar and cvar options to precisely control the permutations?](/faq/clusterstats_iuwcvar)
- [How does ft_prepare_neighbours work?](/faq/how_does_ft_prepare_neighbours_work)
- [What is the idea behind statistical inference at the second-level?](/faq/statistics_secondlevel)
- [Why are there multiple neighbour templates for the NeuroMag306 system?](/faq/neighbours_neuromag)
- [Why should I use the cfg.correcttail option when using statistics_montecarlo?](/faq/clusterstats_correcttail)

## Plotting and visualization

- [How can I play back EEG/MEG and synchronous audio or video?](/faq/audiovideo)
- [How can I visualize a 'localspheres' volume conductor model?](/faq/how_can_i_visualize_a_localspheres_volume_conductor_model)
- [How do I construct a layout file for the plotting functions?](/faq/layout_creation)
- [I am getting strange artifacts in figures that use opacity](/faq/opacityrendering)
- [I am having problems printing figures that use opacity](/faq/i_am_having_problems_printing_figures_that_use_opacity)
- [What are the different Neuromag and Yokogawa layouts good for?](/faq/layout_magandgrad)
- [What is a good way to save images for later processing in other software?](/faq/figure_export)
- [What is the format of the layout file, which is used for plotting?](/faq/layout_fileformat)
- [What is the plotting convention for anatomical MRIs?](/faq/anat_plottingconvention)
- [Why does my anatomical MRI show upside-down when plotting it with ft_sourceplot?](/faq/anat_upsidedownplotting)
- [Which colormaps are supported?](/faq/colormap)

## Experimental questions

- [How can I change the head localization in a CTF dataset?](/faq/ctf_changeheadloc)
- [How can I monitor a subject's head position during a MEG session?](/faq/how_can_i_monitor_a_subject_s_head_position_during_a_meg_session)
- [How can I test the serial port connection between two computers?](/faq/how_can_i_test_the_serial_port_connection_between_two_computers)
- [How can I use my MacBook Pro for stimulus presentation in the MEG lab?](/faq/how_can_i_use_my_macbook_pro_for_stimulus_presentation_in_the_meg_lab)
- [How can I visualize the Neuromag head position indicator coils?](/faq/how_can_i_visualize_the_neuromag_head_position_indicator_coils)

## Realtime data streaming and analysis

- [Does the FieldTrip realtime buffer only work with MATLAB?](/faq/fieldtripbuffer)
- [How fast is the FieldTrip buffer for realtime data streaming?](/faq/how_fast_is_the_fieldtrip_buffer_for_realtime_data_streaming)
- [How should I get started with the FieldTrip realtime buffer?](/faq/how_should_i_get_started_with_the_fieldtrip_realtime_buffer)

## Distributed computing

- [What are the different approaches I can take for distributed computing?](/faq/distributed_computing)

### Distributed computing with the MATLAB distributed computing toolbox

- [How to get started with the MATLAB distributed computing toolbox?](/faq/how_to_get_started_with_the_matlab_distributed_computing_toolbox)

### Distributed computing with fieldtrip/qsub on a HPC cluster

- [How to compile MATLAB code into stand-alone executables?](/faq/how_to_compile_matlab_code_into_stand-alone_executables)
- [How to get started with distributed computing using qsub?](/faq/how_to_get_started_with_distributed_computing_using_qsub)

## MATLAB questions

- [Installation and setting up the path](/faq/installation)
- [Can I prevent "external" toolboxes from being added to my MATLAB path?](/faq/toolboxes_legacyvsexternal)
- [Can I use FieldTrip without MATLAB license?](/faq/compiled)
- [Can I use Octave instead of MATLAB?](/faq/octave)
- [How can I compile the mex files and command-line programs?](/faq/compile)
- [How can I compile the mex files on 64-bit Windows?](/faq/compile_windows)
- [How can I compile the mex files on macOS?](/faq/compile_osx)
- [How many lines of code does FieldTrip consist of?](/faq/how_many_lines_of_code_does_fieldtrip_consist_of)
- [How to select the correct SPM toolbox?](/faq/how_to_select_the_correct_spm_toolbox)
- [MATLAB complains about a missing or invalid MEX file, what should I do?](/faq/matlab_mexinvalid)
- [MATLAB complains that mexmaci64 cannot be opened because the developer cannot be verified](/faq/mex_osx)
- [MATLAB does not see the functions in the "private" directory](/faq/matlab_privatefunctions)
- [MATLAB version 7.3 (2006b)_crashes_when_I_try_to_do_...](/faq/matlab_crash73)
- [The databrowser crashes and destroys the whole MATLAB session, how can I resolve this?](/faq/databrowser_crash)
- [What are the MATLAB requirements for using FieldTrip?](/faq/requirements)
- [What is the relation between "events" (such as_triggers) and "trials"?](/faq/eventsversustrials)
- [Which external toolboxes are used by FieldTrip?](/faq/external)
- [Why are so many of the interesting functions in the private directories?](/faq/privatefunctions_why)

## Code and development questions

- [How are the various data structures defined?](/faq/datatype)
- [How can I debug my analysis script if a FieldTrip function gives an error?](/faq/matlab_debugging)
- [How can I keep track of the changes to the code?](/faq/how_can_i_keep_track_of_the_changes_to_the_code)
- [What does a typical call to a FieldTrip function look like?](/faq/fieldtrip_functioncall)
- [Why is FieldTrip maintained in SVN and not in git?](/faq/svnversusgit)

## Organizational questions

- [Can I get an offline version of the website documentation?](/faq/documentation_offline)
- [Can I use the FieldTrip logo on my poster?](/faq/fieldtriplogo)
- [How many people are subscribed to the email discussion list?](/faq/emaillist_subscribers)
- [How should I refer to FieldTrip in my publication?](/faq/how_should_i_refer_to_fieldtrip_in_my_publication)
- [How should I send example data to the developers?](/faq/how_should_i_send_example_data_to_the_developers)
- [How to ask good questions to the community?](/faq/how_to_ask_good_questions_to_the_community)
- [I am having problems downloading](/faq/download_ftpproblem)
- [I am working at the Donders, should I also download FieldTrip?](/faq/download_donders)
- [Which version of FieldTrip should I download?](/faq/fieldtrip_downloadversion)
- [Why am I not allowed to post to the discussion list?](/faq/emaillist_nopost)
- [Why am I not receiving emails from the discussion list?](/faq/emaillist_noreceive)
- [Why am I receiving warnings about too many bouncing emails?](/faq/emaillist_bounces)
- [Why is FieldTrip developed separately from EEGLAB?](/faq/fieldtrip_eeglab)
- [Why is my message rejected from the email discussion list?](/faq/emaillist_rejected)

## Various other questions

- [Are the FieldTrip lectures available on video?](/faq/video)
- [Can I map different electrode position layouts?](/faq/capmapping)
- [Can I organize my own FieldTrip workshop?](/faq/workshop)
- [How can I anonymize DICOM files?](/faq/anonymization_dicom)
- [How can I anonymize a CTF dataset?](/faq/anonymization_ctf)
- [How can I anonymize a brainvisino dataset?](/faq/anonymization_vrainvision)
- [How can I anonymize data processed in FieldTrip?](/faq/anonymization_fieldtripdata)
- [How can I anonymize or deidentify an anatomical MRI?](/faq/anonymization_anatomical)
- [How can I convert an anatomical MRI from DICOM into CTF format?](/faq/how_can_i_convert_an_anatomical_mri_from_dicom_into_ctf_format)
- [How can I share my MEG data?](/faq/data_sharing)
- [How do I prevent FieldTrip from printing the time and memory after each function call?](/faq/how_do_i_prevent_fieldtrip_from_printing_the_time_and_memory_after_each_function_call)
- [How should I prepare for the upcoming FieldTrip workshop?](/faq/how_should_i_prepare_for_the_upcoming_fieldtrip_workshop)
- [How should I specify the coordinate systems in a BIDS dataset?](/faq/bids_coordsystem)
- [What are the units of the data and of the derived results?](/faq/units)
- [Which datasets are used in the documentation and where are they used?](/faq/datasets)
- [What usage information is FieldTrip tracking?](/faq/tracking)
- [Where can I find open access MEG/EEG data?](/faq/open_data)
- [Which methodological details should I report in an EEG/MEG manuscript?](/faq/checklist)
