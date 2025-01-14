---
title: Getting started with SPM
category: getting_started
tags: [spm]
redirect_from:
    - /getting_started/spm/
---

# Getting started with SPM

Statistical Parametric Mapping (SPM) is a software package designed for the analysis of brain imaging data sequences. FieldTrip and SPM are both implemented in MATLAB and the projects work closely together and share code. If you use FieldTrip, chances are that you use SPM code (possibly without knowing it), and vice versa.

## Background

[SPM12](http://www.fil.ion.ucl.ac.uk/spm/software/spm8b/) is the latest version of [SPM software](http://www.fil.ion.ucl.ac.uk/spm/) developed by the Methods Group at the Wellcome Trust Centre for Neuroimaging, Institute of Neurology, University College London, UK and collaborators. SPM12 implements several advanced methods for M/EEG analysis:

- Statistical analysis at both scalp and source level and also analysis of time-frequency images using the General Linear Model (GLM) with thresholding based on Random Field Theory (RFT).

- Bayesian 3D imaging source reconstruction methods including Multiple Sparse Priors (MSP) and MSP with group constraints.

- Variational Bayesian dipole fitting, which makes it possible to fit and compare different dipole models for a particular scalp topography. Although dipole fitting is implemented in several packages including FieldTrip, comparison of different dipole models and optimal selection of the number of dipoles based on model evidence is only available in SPM.

- Dynamic Causal Modelling (DCM)- a spatiotemporal network model to estimate effective connectivity in a network of sources. It is an easy to use, but nevertheless very sophisticated tool which makes it possible to model brain's electrical activity with biologically plausible neuronal models, make inferences about physiologically meaningful parameters and compare different models for the same data. DCM is presently available for evoked responses (ERP), steady state responses (a.k.a. power spectra and cross-spectral densities) and induced responses (a.k.a. event-related spectral perturbations, a.k.a. time-frequency images).

The developers of SPM have a formal collaboration with the developers of FieldTrip on many analysis issues. For example, SPM and FieldTrip share routines for converting data to MATLAB, forward modeling for M/EEG source reconstruction and the SPM12 distribution contains a version of FieldTrip so that you can combine FieldTrip and SPM functions in your custom scripts. SPM and FieldTrip complement each other well as SPM is geared toward very specific analysis tools whereas FieldTrip is a more general repository of different methods that can be put together in flexible ways to perform a variety of analyses.

[Reference paper](https://www.hindawi.com/journals/cin/2011/852961/), [courses](https://www.fil.ion.ucl.ac.uk/spm/course/video/) and [tutorials](https://jsheunis.github.io/2018-06-28-spm12-matlab-scripting-tutorial-1/) are also available


## How does FieldTrip use SPM?

As SPM's core expertise is mainly oriented to volumetric data processing (MRI, fMRI), FieldTrip integrates SPM functionalities to deal with two main operations:

1. Creation of the geometries needed for accurate forward modelling (e.g., _spm_create_vol_, _spm_segment_)
2. Spatial normalization of volumetric images for efficient group statistics at the source level (e.g., _spm_normalise_, _spm_deformations_)

The following figure shows main FieldTrip functions using SPM:

{% include image src="/assets/img/getting_started/spm/FieldTrip_uses_SPM.png" width="500" %}


## How does SPM use FieldTrip?

SPM integrates some FieldTrip functions to perform operations on M/EEG data such as reading, format checking, plotting, preprocessing or frequency analysis. Specifically, SPM needs FieldTrip to create forward models (_ft_compute_leadfield_, _ft_prepare_vol_sens_). The following figure illustrates some SPM functions that call FieldTrip:

{% include image src="/assets/img/getting_started/spm/SPM_uses_FieldTrip.png" width="500" %}


## Complementary use of both toolboxes

You can also take advantage of both SPM and FieldTrip toolboxes to run a wider range of analyses on an experiment. To convert data from SPM object to FieldTrip structure, you can use `spm2fieldtrip` and `fieldtrip2spm` functions as shown in this example:

    ft_hastoolbox('spm8',1);
    D = spm_eeg_load(spm_filename);
    data = spm2fieldtrip(D);

Let's have a look at the specific tools available within each of them:

- FieldTrip offers highly customisable analyses through scripting, while SPM allows non-proficient MATLAB users to run their analyses through GUI tools. The graphical interface is simply called through `spm xxxx` where the xxxx corresponds to the data type to be analysed (e.g., `spm eeg`).

- Statistical analysis in FieldTrip can be performed using either parametric (i.e. estimating p-values based on known distributions of the test-statistic (e.g., a T- or F-statistic) under some null hypothesis), or non-parametric (i.e. estimating p-values based on randomization techniques and Montecarlo sampling) (cf. [demo](/workshop/meg-uk-2015/fieldtrip-stats-demo)). FieldTrip supports various traditional test-statistics (such as T-statistics or F-statistics, but the user also has the opportunity to design his/her own custom test-statistic by means of a statfun. On the other hand, SPM uses general linear model (GLM), computing p-values based on parametric statistics (T- or F-tests) based on specific contrasts, typically following a 2-level approach: 1st level = subject-by-subject regression (cf. [tutorial](https://www.youtube.com/watch?v=KdB9F8cf0L0&list=PLx_IWc-RN82uKTWzgho2ARVGan8TNlb9d&index=12)); 2nd level = group analysis, computing contrasts at the group level of estimated model parameters (cf. [tutorial](https://www.youtube.com/watch?v=_7jzkV7oUXg&list=PLx_IWc-RN82uKTWzgho2ARVGan8TNlb9d&index=13)). An example of SPM sensor-level stats can be found [here](/workshop/meg-uk-2015/spm_stats). On top of that, the way both toolboxes deal with the multiple comparison problem is also different. FieldTrip implements a clustering method, while SPM exploits the random field theory ([RFT](https://www.fil.ion.ucl.ac.uk/spm/doc/books/hbf2/pdfs/Ch14.pdf)).

- FieldTrip's source reconstruction tool includes multiple methods such as [dipole fitting](/workshop/natmeg2014/dipolefitting/), linear constrained minimum variance beamformer ([LCMV](/tutorial/beamformer_lcmv/)), dynamic imaging of coherent sources ([DICS](/tutorial/beamformer/)), minimum norm estimation ([MNE](/tutorial/minimumnormestimate)), etc. as described in [ft_sourceanalysis](/reference/ft_sourceanalysis), while SPM focuses on [Bayesian 3D imaging source reconstruction](/workshop/meg-uk-2015/spm_source) or variational Bayesian dipole fitting using `spm_eeg_dipole_waveforms`.

- Connectivity analysis can be done using various methods. FieldTrip leaves the user the opportunity to choose between various methods (coherence, correlation, cross-spectral density, phase-locking value, Granger causality), as described in [ft_connectivityanalysis](/reference/ft_connectivityanalysis) (cf. [demo](/workshop/meg-uk-2015/fieldtrip-connectivity-demo)), while SPM focuses on dynamic causal modelling (DCM) offering a very sophisticated analysis as shown in [this example](/workshop/meg-uk-2015/dcm_tutorial).

- Spectral analysis provided by FieldTrip offers several ways to estimate the spectrum of the signal, including fast Fourier transform using multitapers, wavelet convolution, and Fourier transformation of multivariate autoregressive model parameters as described in [ft_freqanalysis](/reference/ft_freqanalysis) (cf. [demo](/workshop/oslo2019/timefrequency)). SPM mainly uses FieldTrip functions `ft_specest_xxxx` to run spectral analysis except for Morlet wavelet transform that is computed through the `spm_eeg_morlet` function.

In summary, FieldTrip leaves more freedom to the user with highly customizable tools, while SPM tools are very specific to achieve maximum efficiency. This complementarity is illustrated in the following figure:

{% include image src="/assets/img/getting_started/spm/FieldTrip_SPM_complement.png" width="500" %}


## Practical issues

To prevent function name clashes, up to [SPM version r4010](https://github.com/spm/spm8/releases/tag/r4010) from July 2010 SPM8 called its FieldTrip functions via intermediate or 'wrapper' functions whose name always started with `ft_`. Prior to renaming FieldTrip functions according to the same convention this had the advantage that even if there was a different FieldTrip version in MATLAB path from the one used by SPM, SPM only used its own version and incompatibilities could be avoided. From SPM r4010 onward the version of FieldTrip that is distributed with SPM is a 'light' version with the same layout and function names as the standalone FieldTrip but without the `compat` folders, large template files and without some less frequently toolboxes (e.g., classification and real time).

FieldTrip data structures can be converted to SPM EEG files using the _spm_eeg_ft2spm_ function.

SPM12 M/EEG data, once loaded with the function _spm_eeg_load_, can can be converted to FieldTrip format using the method `ftraw` (with the syntax `D.ftraw` or `ftraw(D)`) for the raw struct format or `fttimelock` (with the syntax `D.fttimelock` or `fttimelock(D)`) for the timelock struct format. Additional arguments can be supplied to these functions to select only part of the data, e.g.

    raw = ftraw(D, D.indchannel('Cz'), D.indsample(-0.1):D.indsample(0.2), D.indtrial('oddball'));

Since the SPM12 M/EEG format as well as its predecessors SPM8/SPM5 format are supported by the [fileio toolbox](/development/module/fileio), it is possible to preprocess SPM M/EEG data in FieldTrip the usual way without the need for SPM to be installed. An SPM M/EEG dataset consists of two files with extensions `.mat` and `.dat`. The name of the `.mat` file should be specified as `cfg.dataset` in ft_preprocessing for the SPM format to be recognized.

The shared infrastructure for head modeling makes it possible to use a head model coregistered with sensors using SPM12 for FieldTrip methods such as beamforming and obtain results with SPM and FieldTrip in the same coordinate system. This facilitates comparison and validation of results obtained with SPM using FieldTrip and _vice versa_.
