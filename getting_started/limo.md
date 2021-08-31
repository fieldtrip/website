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

The inputs of LIMO statistical analyses are preprocessed and segmented data (EEG or source signal) that are stored as `.mat` (FieldTrip data) or `.set` (EEGLAB data) files. Following BIDS standard, those data are known as derivatives data.

The outputs of LIMO are generated at each levels:
1. First level analysis derives subject specific parameter estimates (`n_channels x n_timeframes x n_variables` matrix) for any effects as well as contrast estimates (`n_channels x n_timeframes x n_stat_variables` matrix). 
2. Second level analysis results of a `n_channels x n_timeframes x n_stat_variables` matrix corresponding to the group analysis.

The following figure gives an example of inputs/outputs within the whole BIDS structure:

![BIDS derivatives example](/assets/img/getting_started/limo/BIDS_derivatives_example.png)
{% include image src="/assets/img/getting_started/limo/BIDS_derivatives_example.png" width="300" %}


## How does LIMO EEG use FieldTrip?

LIMO EEG integrates FieldTrip functions to deal with FieldTrip data structures. As the statistical analyses require specific information, **[ft_datatype](https://www.fieldtriptoolbox.org/reference/ft_datatype/)** function allows the algorithm to define the structure and extract required field. Then, LIMO functions convert them to the appropriate format. The following figure illustrates this process:
![LIMO uses FieldTrip](/assets/img/getting_started/limo/LIMO_uses_FieldTrip.png)
{% include image src="/assets/img/getting_started/limo/LIMO_uses_FieldTrip.png" width="300" %}


After having estimated the betas with 1st level analysis, LIMO continues with the 2nd level (group level) analysis.

### Global framework

Processing data through FieldTrip functions and performing statistical analyses on the proceesed data is made easy by the compatibility of LIMO EEG to FieldTrip data structures. The users can directly design a model with FieldTrip data as input (following BIDS standard). The whole pipeline, in BIDS format, could be described as follow:

![LIMO pipeline description](/assets/img/getting_started/limo/block_schematic_pipeline.png)
{% include image src="/assets/img/getting_started/limo/block_schematic_pipeline.png" width="300" %}

The following example is related to the EEG dataset of [Wakeman & Henson (2015)](https://www.nature.com/articles/sdata20151) acquired through visual stimulation with 3 face categories (famous, unknown and scrambled) and 1 covariate (the time between the first and the second presentation of a same face). The statistical analysis aims to identify spatio-temporal regions of significant effect of the face type on the Event-Related Potential (ERP) as well as the effect of the time between 2 presentations of the same face. Categories have been coded as integer values: 1(famous), 2(unknown), 3(scrambled). The Covariates are continuous values.

1. **Model Design**

The first step is to design the model corresponding to the study. This design consists of different steps:

- The required paths and some additional informations have to be defined
```
PATH_TO_ROOT = bids_root_folder; %location of main folder (raw data)
PATH_TO_DERIV = bids_derivatives_folder; %location of processed signal

% define the case (sensor or source level analysis)
SOURCE_ANALYSIS = false; %set to true if you analyse source data

% define the task to analyse
task_name = 'faceStudy';

% trial start and end
trial_start = -200; %starting time of the trial in ms
trial_end = 500; %ending time of the trial in ms
```

- We define the contrast we want to study
```
contrast.mat = [1 -0.5 -0.5]; %contrast between famous (the first value) and other categories (the sum of the 2nd and 3rd value)
```

- The split of the covariates (regressors) has to be defined. Here we want to create 1 column of covariates by regressor (to analyse the influence on each condition)
```
regress_cat = { 1 , 1;   
                2 , 2;
                3 , 3};  %correspondance between covariate and categories. Here, we create 1 column of covariate by category.

% Note: the following syntax has to be respected for the mapping (/!\ don't use the value 0 /!\):
% {first_regressor_merging, corresponding_value ;
%  second_regressor_merging, corresponding_value;
%  nth_regressor_merging, corresponding_value    }
```

- We select the desired covariates (regressors) to study (in case there are several covariates). Here there is only  1 covariate
```
my_trialinfo = 'trialinfo.mat'; %information about trials for each subject, as defined by FT_DEFINETRIAL and FT_PREPROCESSING
selected_regressors = 4; %selection from trialinfo.Properties.VariableNames (here, the first 3 columns correspond to the categories and the 4th one is the covariate)
```

- Create the model (this operation calls raw data of each subject and designs the required matrices... it could take 1 or 2 minutes)
```
model = create_model(PATH_TO_DERIV,PATH_TO_SOURCE,SOURCE_ANALYSIS,task_name,my_trialinfo,trial_start,trial_end,selected_regressors,regress_cat);
```

2. **First level analysis**

The beta and contrast estimates are computed subject by subject through a parallel computing pipeline.

As we want both the betas (ERP model) and contrast (conditional difference) to be computed and stored as "derivatives 2" (cf. pipeline figure), we do the following
```
cd(PATH_TO_DERIV)
option = 'both'; %'model specification', 'contrast only' or 'both'
```

Now that everything is properly defined, we can run the computation (Almost all your CPU cores will be requested for this task, it's time to grab a coffee...)
```
[LIMO_files, procstatus] = limo_batch(option,model,contrast); %writes beta and contrast estimates to disk in derivatives 2 folder
```

3. **Second level analysis**

The group-level analysis will run as a parallel computing pipeline on contrast estimates (in this example).

We first need an estimates of the channel locations representing all the subjects. Here we consider the channel-by-channel average position
```
 expected_chanlocs = limo_avg_expected_chanlocs(PATH_TO_DERIV, model.defaults);
```

We then select the targeted first-level estimates (here the first contrast, corresponding to face type comparison) and the name of the corresponding statistical test we want to perform
```
my_con = 'con_1'
cd('derivatives/eeg') %path to 1st level analysis output
LIMOfiles = fullfile(pwd,sprintf('%s_files_GLM_OLS_Time_Channels.txt',my_con));
if ~exist(['derivatives/t_test_' my_con],'dir')
    mkdir(['derivatives/t_test_' my_con])
end
cd(['derivatives/t_test_' my_con])
```

Finally, we run the second level analysis mentioning the desired statistical test to perform, the desired number of bootstrap repetitions and if a threshold free cluster enhancement ([Pernel *et al.*, 2015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4510917/)) has to be computed. Another parallel computing pipeline will start, it should last less time than the first-level analysis.
```
stat_test = 'one sample t-test'; %desired statistical test
nboot = 1000; %number of boostrap repetition
tfce = 1; %set to 0 if the threshold free enhancement algorithm does not have to be run

LIMOPath = limo_random_select(stat_test,expected_chanlocs,'LIMOfiles',... 
    LIMOfiles,'analysis_type','Full scalp analysis',...
    'type','Channels','nboot',nboot,'tfce',tfce,'skip design check','yes');
```

Then, results can be plot by calling `limo_results` function. By selecting "clustering" as MC correction and the generated "one_sample_ttest_parameter_1.mat" through "image all", you obtain the regions of significant difference between the categories as shown by this figure:
![LIMO T-test](/assets/img/getting_started/limo/example_results.png)
{% include image src="/assets/img/getting_started/limo/example_results.png" width="300" %}