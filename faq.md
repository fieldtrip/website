---
title: Frequently asked questions
category: faq
---

# Frequently asked questions

On this page you can find answers to a variety of FieldTrip and MATLAB related questions.

We invite you to [add your own](/development/contribute) example scripts or frequently asked questions on the website. Also tutorials can be added. Every time you explain somebody something about FieldTrip, please consider whether you could use the website for this, so others can learn from it as well.

See also the [tutorials](/tutorial) and [example scripts](/example).

## Reading and preprocessing data

- [How can I use the databrowser?](/faq/preproc/databrowser)
- [How can I inspect the electrode impedances of my data?](/faq/preproc/impedancecheck)
- [Should I rereference my EEG data prior to, or after ICA?](/faq/preproc/ica_rereference)
- [I used to work with trl-matrices that have more than 3 columns. Why is this not supported anymore?](/faq/preproc/trialinfo_trl)
- [Why should I set continuous to yes for CTF data?](/faq/preproc/continuous)
- [Why should I start with rereferencing for BioSemi EEG data?](/faq/preproc/biosemi_reference)

### Specific data formats

- [How can I read EGI mff data without the JVM?](/faq/preproc/dataformat/egi_nojvm)
- [How can I read all channels from an EDF file that contains multiple sampling rates?](/faq/preproc/dataformat/edf2fieldtrip)
- [How does the CTF higher-order gradiometer work?](/faq/preproc/dataformat/ctf_syntheticgradient)
- [How can I extend the reading functions with a new dataformat?](/faq/preproc/dataformat/fileio_dataformat)
- [I have problems reading in NeuroScan .cnt files. How can I fix this?](/faq/preproc/dataformat/neuroscan)
- [Why are the fileio functions stateless, does the fseek not make them very slow?](/faq/preproc/dataformat/fileio_stateless)
- [How can I import my own dataformat?](/faq/preproc/dataformat/dataformat_own)
- [How can I deal with a discontinuous Neuralynx recording?](/faq/preproc/dataformat/discontinuous_neuralynx)
- [How can I fix a corrupt CTF meg4 data file?](/faq/preproc/dataformat/ctf_fixmeg4)
- [How can I fix a corrupt CTF res4 header file?](/faq/preproc/dataformat/ctf_fixres4)
- [How can I read corrupted (unsaved) CTF data?](/faq/preproc/dataformat/ctf_readcorrupted)
- [I am having problems reading the CTF .hc headcoordinates file](/faq/preproc/dataformat/ctf_fixhc)

### Data handling

- [Reading is slow, can I write my raw data to a more efficient file format?](/faq/preproc/datahandling/writedata_matbin)
- [What dataformats are supported?](/faq/preproc/datahandling/dataformat)
- [How can I append the files of two separate recordings?](/faq/preproc/datahandling/append_files)
- [How can I convert one dataformat into another?](/faq/preproc/datahandling/convert_dataformat)
- [How can I merge two datasets that were acquired simultaneously with different amplifiers?](/faq/preproc/datahandling/mergedata)
- [How can I preprocess a dataset that is too large to fit into memory?](/faq/preproc/datahandling/preproc_downsample)
- [How can I rename channels in my data structure?](/faq/preproc/datahandling/rename_channels)

### Trials, triggers and events

- [How can I check or decipher the sequence of triggers in my data?](/faq/preproc/events/triggers)
- [How can I find out what eventvalues and eventtypes there are in my data?](/faq/preproc/events/inspect_events)
- [How can I process continuous data without triggers?](/faq/preproc/events/preproc_continuous)
- [How can I transform trigger values from bits to decimal representation with a trialfun?](/faq/preproc/events/trialfun_bit2decimal)
- [Is it possible to keep track of trial-specific information in my FieldTrip analysis pipeline?](/faq/preproc/events/trialinfo)

### Artifacts

- [What kind of filters can I apply to my data?](/faq/preproc/artifact/preproc_filtertypes)
- [Do I need to resample my data, and if so, how is this to be done?](/faq/preproc/artifact/resampling_lowpassfilter)
- [I used ICA on my MEG data from before 2012 and now FieldTrip crashes, why is that?](/faq/preproc/artifact/ica_crash)
- [Why does my ICA output contain complex numbers?](/faq/preproc/artifact/ica_complexvalues)
- [How can I consistently represent artifacts in my data?](/faq/preproc/artifact/artifact_representation)
- [How can I interpret the different types of padding that I find when dealing with artifacts?](/faq/preproc/artifact/artifact_padding)
- [How does the filter padding in preprocessing work?](/faq/preproc/artifact/preproc_padding)
- [Why is there a residual 50Hz line-noise component after applying a DFT filter?](/faq/preproc/artifact/dftfilter_residual)
- [Why does my ICA eyeblink component look strange?](/faq/preproc/artifact/ica_eyeblink_topo)

## Spectral analysis

- [How can I compute inter-trial coherence?](/faq/spectral/itc)
- [How can I do time-frequency analysis on continuous data?](/faq/spectral/tfr_continuous)
- [How does mtmconvol work?](/faq/spectral/mtmconvol)
- [How to interpret the sign of the phase slope index?](/faq/spectral/phaseslopeindex)
- [In what way can frequency domain data be represented in FieldTrip?](/faq/spectral/datatype_freq)
- [What convention is used to define absolute phase in 'mtmconvol', 'wavelet' and 'mtmfft'](/faq/spectral/freqanalysis_phasedefinition)
- [What does "padding not sufficient for requested frequency resolution" mean?](/faq/spectral/freqanalysis_paddinginsufficient)
- [What is the difference between coherence and coherency?](/faq/spectral/coherence_coherency)
- [Why am I not getting exact integer frequencies?](/faq/spectral/freqanalysis_foinoninteger)
- [Why does my TFR contain NaNs?](/faq/spectral/tfr_nans)
- [Why does my TFR look strange (part I, demeaning)?](/faq/spectral/tfr_strangedemean)
- [Why does my TFR look strange (part II, detrending)?](/faq/spectral/tfr_strangedetrend)
- [Why is the largest peak in the spectrum at the frequency which is 1/segment length?](/faq/spectral/why_largest_peak_spectrum)
- [Why does my output.freq not match my cfg.foi when using 'mtmconvol' in ft_freqanalysis?](/faq/spectral/freqanalysis_foimismatchmtmconvol)
- [Why does my output.freq not match my cfg.foi when using 'mtmfft' in ft_freqanalysis?](/faq/spectral/freqanalysis_foimismatchmtmfft)
- [Why does my output.freq not match my cfg.foi when using 'wavelet' (formerly 'wltconvol') in ft_freqanalysis?](/faq/spectral/freqanalysis_foimismatchwavelet)
- [Does it make sense to subtract the ERP prior to time frequency analysis, to distinguish evoked from induced power?](/faq/spectral/evoked_vs_induced)

## Source reconstruction

- [Can I do combined EEG and MEG source reconstruction?](/faq/source/sourcerecon_meeg)
- [Can I restrict the source reconstruction to the grey matter?](/faq/source/sourcerecon_greymatter)
- [How are electrodes, magnetometers or gradiometers described?](/faq/source/sensors_definition)
- [How are the LPA and RPA points defined?](/faq/source/anat_landmarks)
- [How are the different head and MRI coordinate systems defined?](/faq/source/coordsys)
- [How can I check whether the grid that I have is aligned to the segmented volume and to the sensor gradiometer?](/faq/source/sourcerecon_checkalignment)
- [How can I convert an anatomical mri from DICOM into CTF format?](/faq/source/anat_dicom2ctf)
- [How can I determine the anatomical label of a source or electrode?](/faq/source/label_lookup)
- [How can I fine-tune my BEM volume conduction model?](/faq/source/bem_finetune)
- [How can I map source locations onto an anatomical label in an atlas?](/faq/source/sourcerecon_atlas)
- [How can I visualize the different geometrical objects that are needed for forward and inverse computations?](/faq/source/inspect_geometries)
- [How do I install the OpenMEEG binaries?](/faq/source/openmeeg)
- [How do homogenous coordinate transformation matrices work?](/faq/source/homogenous)
- [How is anatomical, functional or statistical "volume data" described?](/faq/source/datatype_volume)
- [How should I specify the fiducials?](/faq/source/fiducial)
- [How to change the MRI orientation, the voxel size or the field-of-view?](/faq/source/anat_reslice)
- [How to coregister an anatomical MRI with the gradiometer or electrode positions?](/faq/source/anat_coreg)
- [Is it good or bad to have dipole locations outside of the brain for which the source reconstruction is computed?](/faq/source/sourcerecon_outside)
- [Is it important to have accurate measurements of electrode locations for EEG source reconstruction?](/faq/source/sensors_accuracy)
- [My MRI is upside down, is this a problem?](/faq/source/anat_upsidedown)
- [Should I use a Polhemus or a Structure Sensor to record electrode positions?](/faq/source/structuresensor)
- [What is the conductivity of the brain, CSF, skull and skin tissue?](/faq/source/conductivity_defaults)
- [What is the difference between the ACPC, MNI, SPM and TAL coordinate systems?](/faq/source/acpc)
- [What material is used for the flexible MEG headcasts?](/faq/source/headcast)
- [What kind of volume conduction models are implemented?](/faq/source/datatype_headmodel)
- [Where can I find the dipoli command-line executable?](/faq/source/dipoli_filelocation)
- [Where is the anterior commissure?](/faq/source/anterior_commissure)
- [Why is there a rim around the brain for which the source reconstruction is not computed?](/faq/source/sourcerecon_rim)
- [Why is the source model deformed or incorrectly aligned after warping template?](/faq/source/sourcemodel_deformation)
- [Why should I use an average reference for EEG source reconstruction?](/faq/source/sourcerecon_avgref)
- [Why does my EEG headmodel look funny?](/faq/source/headmodel_meshingproblem)

## Statistical analysis

- [How NOT to interpret results from a cluster-based permutation test?](/faq/stats/clusterstats_interpretation)
- [How can I define neighbouring sensors?](/faq/stats/sensors_neighbours)
- [How can I determine the onset of an effect?](/faq/stats/effectonset)
- [How can I test an interaction effect using cluster-based permutation tests?](/faq/stats/clusterstats_interaction)
- [Should I use t or F values for cluster-based permutation tests?](/faq/stats/clusterstats_teststatistic)
- [How can I test for correlations between neuronal data and quantitative stimulus and behavioural variables?](/faq/stats/behavior_signalcorrelation)
- [How can I test whether a behavioral measure is phasic?](/faq/stats/behavior_cosinefit)
- [How can I use the ivar, uvar, wvar and cvar options to precisely control the permutations?](/faq/stats/clusterstats_iuwcvar)
- [How does ft_prepare_neighbours work?](/faq/stats/neighbours_prepare)
- [What is the idea behind statistical inference at the second-level?](/faq/stats/statistics_secondlevel)
- [Why are there multiple neighbour templates for the NeuroMag306 system?](/faq/stats/neighbours_neuromag)
- [Why should I use the cfg.correcttail option when using statistics_montecarlo?](/faq/stats/clusterstats_correcttail)

## Plotting and visualization

- [How can I play back EEG/MEG and synchronous audio or video?](/faq/plotting/audiovideo)
- [How can I visualize a 'localspheres' volume conductor model?](/faq/plotting/headmodel_localspheres)
- [How do I construct a layout file for the plotting functions?](/faq/plotting/layout_creation)
- [I am getting strange artifacts in figures that use opacity](/faq/plotting/opacityrendering)
- [I am having problems printing figures that use opacity](/faq/plotting/figure_opacity)
- [What are the different Neuromag and Yokogawa layouts good for?](/faq/plotting/layout_magandgrad)
- [What is a good way to save images for later processing in other software?](/faq/plotting/figure_export)
- [What is the format of the layout file, which is used for plotting?](/faq/plotting/layout_fileformat)
- [What is the plotting convention for anatomical MRIs?](/faq/plotting/anat_plottingconvention)
- [Why does my anatomical MRI show upside-down when plotting it with ft_sourceplot?](/faq/plotting/anat_upsidedownplotting)
- [Which colormaps are supported?](/faq/plotting/colormap)

## Experimental questions

- [How can I change the head localization in a CTF dataset?](/faq/experiment/ctf_changeheadloc)
- [How can I monitor a subject's head position during a MEG session?](/faq/experiment/headlocalizer)
- [How can I test the serial port connection between two computers?](/faq/experiment/serialport)
- [How can I use my MacBook Pro for stimulus presentation in the MEG lab?](/faq/experiment/psychtoolbox_macbook)
- [How can I visualize the Neuromag head position indicator coils?](/faq/experiment/neuromag_hpi)

## Realtime data streaming and analysis

- [Does the FieldTrip realtime buffer only work with MATLAB?](/faq/realtime/fieldtripbuffer)
- [How fast is the FieldTrip buffer for realtime data streaming?](/faq/realtime/fieldtripbuffer_speed)
- [How should I get started with the FieldTrip realtime buffer?](/faq/realtime/fieldtripbuffer_gettingstarted)

## Distributed computing

- [What are the different approaches I can take for distributed computing?](/faq/distcomp/distributed_computing)

### Distributed computing with the MATLAB distributed computing toolbox

- [How to get started with the MATLAB distributed computing toolbox?](/faq/distcomp/distributed_matlab)

### Distributed computing with fieldtrip/qsub on a HPC cluster

- [How to compile MATLAB code into stand-alone executables?](/faq/distcomp/matlab_compile)
- [How to get started with distributed computing using qsub?](/faq/distcomp/distributed_qsub)

## MATLAB questions

- [Installation and setting up the path](/faq/matlab/installation)
- [Can I prevent "external" toolboxes from being added to my MATLAB path?](/faq/matlab/toolboxes_legacyvsexternal)
- [Can I use FieldTrip without MATLAB license?](/faq/matlab/compiled)
- [Can I use Octave instead of MATLAB?](/faq/matlab/octave)
- [How can I compile the mex files and command-line programs?](/faq/matlab/compile)
- [How can I compile the mex files on 64-bit Windows?](/faq/matlab/compile_windows)
- [How can I compile the mex files on macOS?](/faq/matlab/compile_osx)
- [How many lines of code does FieldTrip consist of?](/faq/matlab/fieldtrip_codelines)
- [How to select the correct SPM toolbox?](/faq/matlab/spmversion)
- [MATLAB complains about a missing or invalid MEX file, what should I do?](/faq/matlab/matlab_mexinvalid)
- [MATLAB complains that mexmaci64 cannot be opened because the developer cannot be verified](/faq/matlab/mex_osx)
- [MATLAB does not see the functions in the "private" directory](/faq/matlab/matlab_privatefunctions)
- [MATLAB version 7.3 (2006b)_crashes_when_I_try_to_do_...](/faq/matlab/matlab_crash73)
- [The databrowser crashes and destroys the whole MATLAB session, how can I resolve this?](/faq/matlab/databrowser_crash)
- [What are the MATLAB requirements for using FieldTrip?](/faq/matlab/requirements)
- [What is the relation between "events" (such as_triggers) and "trials"?](/faq/matlab/eventsversustrials)
- [Which external toolboxes are used by FieldTrip?](/faq/matlab/external)
- [Why are so many of the interesting functions in the private directories?](/faq/matlab/privatefunctions_why)

## Code and development questions

- [How are the various data structures defined?](/faq/development/datatype)
- [How can I debug my analysis script if a FieldTrip function gives an error?](/faq/development/matlab_debugging)
- [How can I keep track of the changes to the code?](/faq/development/trackchanges)
- [What does a typical call to a FieldTrip function look like?](/faq/development/fieldtrip_functioncall)
- [Why is FieldTrip maintained in SVN and not in git?](/faq/development/svnversusgit)

## Organizational questions

- [Can I get an offline version of the website documentation?](/faq/organization/documentation_offline)
- [Can I use the FieldTrip logo on my poster?](/faq/organization/fieldtriplogo)
- [How many people are subscribed to the email discussion list?](/faq/organization/emaillist_subscribers)
- [How should I refer to FieldTrip in my publication?](/faq/organization/fieldtrip_reference)
- [How should I send example data to the developers?](/faq/organization/datasharing)
- [How to ask good questions to the community?](/faq/organization/emaillist_howtoask)
- [I am having problems downloading](/faq/organization/download_ftpproblem)
- [I am working at the Donders, should I also download FieldTrip?](/faq/organization/download_donders)
- [Which version of FieldTrip should I download?](/faq/organization/fieldtrip_downloadversion)
- [Why am I not allowed to post to the discussion list?](/faq/organization/emaillist_nopost)
- [Why am I not receiving emails from the discussion list?](/faq/organization/emaillist_noreceive)
- [Why am I receiving warnings about too many bouncing emails?](/faq/organization/emaillist_bounces)
- [Why is FieldTrip developed separately from EEGLAB?](/faq/organization/fieldtrip_eeglab)
- [Why is my message rejected from the email discussion list?](/faq/organization/emaillist_rejected)

## Various other questions

- [Are the FieldTrip lectures available on video?](/faq/other/video)
- [Can I map different electrode position layouts?](/faq/other/capmapping)
- [Can I organize my own FieldTrip workshop?](/faq/other/workshop)
- [How can I anonymize DICOM files?](/faq/other/anonymization_dicom)
- [How can I anonymize a CTF dataset?](/faq/other/anonymization_ctf)
- [How can I anonymize a BrainVision dataset?](/faq/other/anonymization_brainvision)
- [How can I anonymize data processed in FieldTrip?](/faq/other/anonymization_fieldtripdata)
- [How can I anonymize or deidentify an anatomical MRI?](/faq/other/anonymization_anatomical)
- [How can I convert an anatomical MRI from DICOM into CTF format?](/faq/other/anat_dicom2ctf)
- [How can I share my MEG data?](/faq/other/data_sharing)
- [How do I prevent FieldTrip from printing the time and memory after each function call?](/faq/other/showcallinfo)
- [How should I prepare for the upcoming FieldTrip workshop?](/faq/other/workshop_preparation)
- [How should I specify the coordinate systems in a BIDS dataset?](/faq/other/bids_coordsystem)
- [What are the units of the data and of the derived results?](/faq/other/units)
- [Which datasets are used in the documentation and where are they used?](/faq/other/datasets)
- [What usage information is FieldTrip tracking?](/faq/other/tracking)
- [Where can I find open access MEG/EEG data?](/faq/other/open_data)
- [Which methodological details should I report in an EEG/MEG manuscript?](/faq/other/checklist)
