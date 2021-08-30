---
title: Getting started with LIMO EEG
tags: [statistics, GLM, limo, eeg]
---

# Getting started with LIMO EEG

## Background

**[LIMO EEG](https://github.com/LIMO-EEG-Toolbox/limo_tools/wiki)** is a free open source and open development toolbox for the statistical analysis of EEG data ([Pernet *et al.*, 2011](https://doi.org/10.1155/2011/831409)). The main goal of the toolbox is the analysis and formal testing for experimental effects at all electrodes/sensors and
all time points of EEG recordings, as well as in source space. LIMO EEG offers a large range of statistical features:
- Tests (including many popular designs): linear regressions, ANOVAs, ANCOVAs.
- Methods: mass univariate general linear analysis, spatiotemporal clustering and bootstrapping for multiple comparison correction
- Hierarchical general linear model (GLM):
	1. within-subject variance (single trial analyses)
	2. between-subject variance

The following figure illustrates the hierarchical analysis:
![LIMO hierarchical analysis](/assets/img/getting_started/limo/herarchical_analysis.png)
{% include image src="/assets/img/getting_started/limo/herarchical_analysis.png" width="300" %}


The toolbox is implemented in Matlab and requires the Matlab statistical toolbox.

LIMO EEG was initially designed as a plug-in of EEGLAB, but latest updates of the toolbox make it compatible with FieldTrip **[raw](https://www.fieldtriptoolbox.org/reference/ft_datatype_raw/)** and **[source](https://www.fieldtriptoolbox.org/reference/ft_datatype_source/)** data. For other data types, the statistical analyses can be performed independently.

Although the toolbox is primarily designed for EEG data, LIMO EEG can process MEG data.

## Data format

As LIMO EEG directly reads and writes data from/to disk, the recommended way to design the dataset is through **[Brain Imaging Data Structure (BIDS) standard](https://bids.neuroimaging.io/index.html)**. This standard aims to organise and describe neuroimaging data in a uniform way to simplify data sharing through the scientific community. An example of BIDS EEG dataset can be found [here](https://www.fieldtriptoolbox.org/example/bids/).

The inputs of LIMO statistical analyses are preprocessed and segmented data (EEG or source signal). Following BIDS standard, those data are stored as derivatives data. 

** !!!!!** LIMO reads BIDS ** DERIVATIVES ** ! => ....

Organising a dataset following BIDS standard can be done through [data2bids](https://github.com/fieldtrip/fieldtrip/blob/release/data2bids.m) function. We also designed a simplified function to reorganise a dataset through the [create_bids](https://github.com/LucaLaFisca/LIMO-for-FieldTrip/blob/main/utils/create_bids.m) function.

** ADD LINKS TO https://www.fieldtriptoolbox.org/example/bids/, https://www.fieldtriptoolbox.org/example/bids_eeg/ instead of GitHub page**
** MOVE THE FIGURE TO BIDS EXAMPLE DOC  => https://www.fieldtriptoolbox.org/example/bids/   so, add an overview of BIDS and what FT can do with it (read and create BIDS data)**


## How does FieldTrip use LIMO EEG?

Currently, there is no FieldTrip function that directly calls LIMO tools. Does not fit the way ft_statistics works... memory vs disk...

However, a "statfun" could be created to perform specific statistical analyses with LIMO. The following figure shows how it could be implemented:
![FieldTrip uses LIMO](/assets/img/getting_started/limo/FieldTrip_uses_LIMO.png)
{% include image src="/assets/img/getting_started/limo/FieldTrip_uses_LIMO.png" width="300" %}

## How does LIMO EEG use FieldTrip?

** CHANGE THE FIGURE TO KEEP ANALOGY BETWEEN EEGLAB AND FIELDTRIP **
LIMO EEG integrates FieldTrip functions to deal with FieldTrip data structures. As the statistical analyses require specific information, **[ft_datatype](https://www.fieldtriptoolbox.org/reference/ft_datatype/)** function allows the algorithm to define the structure and extract required field. Then, LIMO functions convert them to the appropriate format. The following figure illustrates this process:
![LIMO uses FieldTrip](/assets/img/getting_started/limo/LIMO_uses_FieldTrip.png)
{% include image src="/assets/img/getting_started/limo/LIMO_uses_FieldTrip.png" width="300" %}

** example framework **

Processing data through FieldTrip functions and performing statistical analyses on the proceesed data is made easy by the compatibility of LIMO EEG to FieldTrip data structures. The users can directly design a model with FieldTrip data as input (following BIDS standard). The following code gives an example of how to perform a statistical analysis on a dataset containing 2 categories and 4 covariates:

** CHANGE THE STUDY TO FACE PAPER (https://github.com/fieldtrip/fieldtrip/blob/release/data2bids.m) AND EXPLAIN WHAT ARE THE CATEGORIES AND WHAT IS THE COVARIATE (TIME FROM 1ST PRESENTATION) **

** ADD trialinfo screenshot to explain the dataset (cat, cov, ...) **

** ADD information about specific subfunctions so that it can be understood by spm, ft and EEGLAB users (e.g. expectations about computation time)**

```
% define the required paths
PATH_TO_ROOT = bids_root_folder;
PATH_TO_DERIV = bids_derivatives_folder; %location of processed signal (estimated parameters will be stored there after regression)
PATH_TO_SOURCE = bids_source_data_folder; %in case of source data analysis

% define the case
SOURCE_ANALYSIS = false; %set to true if you analyse source data

% define the task to analyse
task_name = 'semanticPriming';

% design the desired contrasts & regressor combination
%%% contrast syntax %%%
% [first_factor_combination_vector ;
%  second_factor_combination_vector;
%  nth_factor_combination_vector    ]
%%% regressor syntax %%%
% {first_regressor_merging, corresponding_value ;
%  second_regressor_merging, corresponding_value;
%  nth_regressor_merging, corresponding_value    }

contrast.mat = [1 -1 0]; %contrast between the 2 categories
regress_cat = { 1 , 1;   
                2 , 2};  %correspondance between regressors and categories

% select the desired regressors
my_trialinfo = 'trialinfo.mat'; %information about trials for each subject, as defined by FT_DEFINETRIAL and FT_PREPROCESSING
selected_regressors = 3:6; %selection from trialinfo.Properties.VariableNames
trial_start = -200; %starting time of the trial in ms
trial_end = 500; %ending time of the trial in ms

% define rejected categories
%%% /!\/!\/!\/!\/!\ %%%
%%% WE NEED A CATEGORY TO REJECT TO FIX NaN ISSUES %%%
%%% BE SURE YOU DIDN'T ALLOCATE THIS LABEL TO A USEFUL CATEGORY %%%
reject_cat = 0; %we do not use the 0 category in our study (only there for experimental purpose)

% create the model
model = create_model(PATH_TO_DERIV,PATH_TO_SOURCE,SOURCE_ANALYSIS,task_name,my_trialinfo,trial_start,trial_end,selected_regressors,regress_cat,reject_cat);

% run the first level analysis (GLM regression)
cd(PATH_TO_ROOT)
option = 'both'; %'model specification', 'contrast only' or 'both'
[LIMO_files, procstatus] = limo_batch(option,model,contrast); %writes beta and contrast estimates to disk in derivatives folder

% perform T-test on the contrast estimates
expected_chanlocs = limo_avg_expected_chanlocs(PATH_TO_DERIV, model.defaults);

my_con = 'con_1'
LIMOfiles = fullfile(pwd,sprintf('%s_files_GLM_OLS_Time_Channels.txt',my_con));
if ~exist(['t_test_' my_con],'dir')
    mkdir(['t_test_' my_con])
end
cd(['t_test_' my_con])
LIMOPath = limo_random_select('one sample t-test',expected_chanlocs,'LIMOfiles',... 
    LIMOfiles,'analysis_type','Full scalp analysis',...
    'type','Channels','nboot',1000,'tfce',1,'skip design check','yes');
```

Then, results can be plot by calling `limo_results` function. By selecting "clustering" as MC correction and the generated "one_sample_ttest_parameter_1.mat" through "image all", you obtain the regions of significant difference between the categories as shown by this figure:
![LIMO T-test](/assets/img/getting_started/limo/ttest_example.jpg)
{% include image src="/assets/img/getting_started/limo/ttest_example.jpg" width="300" %}


## References
[1] Cyril R. Pernet, Nicolas Chauveau, Carl Gaspar, Guillaume A. Rousselet, "LIMO EEG: A Toolbox for Hierarchical LInear MOdeling of ElectroEncephaloGraphic Data", Computational Intelligence and Neuroscience, vol. 2011, Article ID 831409, 11 pages, 2011. https://doi.org/10.1155/2011/831409

[2] Pernet, C.R., Appelhoff, S., Gorgolewski, K.J. et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Sci Data 6, 103 (2019). https://doi.org/10.1038/s41597-019-0104-8