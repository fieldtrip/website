---
layout: default
---

`<note warning>`
The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas. 

After making changes to the code and/or documentation, this page should remain on the wiki as a reminder of what was done and how it was done. However, there is no guarantee that this page is updated in the end to reflect the final state of the project

So chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
`</note>`

This site is for re-structuring the event-related statistics tutorial ([Parametric and non-parametric statistics on event-related fields](/tutorial/eventrelatedstatistics)).

#  Parametric and non-parametric statistics on event-related fields 

## Introduction

The goal of this tutorial is to provide a gentle introduction into the different options that are implemented for statistical analysis. Here we will use event related fields, because they are more familiar to most of the audience and easier to visualize. Below we will show how you can do some limited statistical testing using the Matlab statistics toolbox and compare that to the FieldTrip **[ft_timelockstatistics](/reference/ft_timelockstatistics)** function. Topics that will be covered are parametric statistics on a single channel and time-window, the multiple comparison problem (MCP), non-parametric randomization testing and cluster-based testing.  

In this tutorial we will use the same [dataset](/tutorial/shared/dataset) as some of the other tutorials, except that here we will not be looking at the details within a single subject, but rather at the group statistics. We will look at how to test statistically differences among conditions within-subjects. The ERF data that will be used in this tutorial was obtained using **[ft_timelockanalysis](/reference/ft_timelockanalysis)** on all 10 subjects that participated in the experiment, followed by **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)**. The data is available from ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/eventrelatedstatistics/GA_ERF_orig.mat.

The tutorial assumes that the preprocessing and steps of the timelock-analysis are already clear for the reader. If it is not the case, you can read about those steps in other tutorials. 

This tutorial does not provide detailed information about statistics on channel-level power spectra and on time-frequency representations of power (as obtained from freqanalysis) or about source-level statistics.  But you have the same options available as described below, except that you should use the **[ft_freqstatistics](/reference/ft_freqstatistics)** function. If you want to do statistics on source reconstructed activity (as obtained from **[ft_sourceanalysis](/reference/ft_sourceanalysis)**), you have the same options available as described below, except that you should use the **[ft_sourcestatistics](/reference/ft_sourcestatistics)** function.

A more thorough explanation of randomization tests and cluster-based statistics can be found in the
[Cluster-based permutation tests on event related fields](/tutorial/cluster_permutation_timelock)
and the [Cluster-based permutation tests on time-frequency data](/tutorial/cluster_permutation_freq) tutorials.

## Background

The topic of this tutorial is the statistical analysis of MEG and EEG data. In experiments, the data is usually collected in different experimental conditions, and the experimenter wants to know by means of statistical testing if there is a difference in the data observed in these conditions. In statistics, a result (for example, a difference among conditions) is statistically significant if it is unlikely to have occurred by chance according to a predetermined threshold probability, the significance level. 

An important feature of the MEG and EEG data is that it has a spatial temporal structure, i.e. the data is sampled at multiple time-points and sensors. This influences what kind of statistics is the most suitable for comparing conditions. If the experimenter is interested at a difference in the signal at a certain time-point and sensor the more wide-spread used parametric tests are also sufficient. If it can not be predicted where the differences are, many statistical comparisons are necessary that leads to the *multiple comparisons problem* (MCP). The MCP arises from the fact that the effect of interest (i.e., a difference between experimental conditions) is evaluated at an extremely large number of (channel,time)-pairs. This number is usually in the order of several thousands. Now, the MCP involves that, due to the large number of statistical comparisons (one per (channel,time)-pair), it is not possible to control the so called *family-wise error rate* (FWER) by means of the standard statistical procedures that operate at the level of single (channel,time)-pairs. The FWER is the probability under the hypothesis of no effect of falsely concluding that there is a difference between the experimental conditions at one or more (channel,time)-pairs. A solution of the MCP requires a procedure that controls the FWER at some critical alpha-level (typically, 0.05 or 0.01). The FWER is also called the *false alarm rate*.

When parametric statistics is used, one method that addresses this problem is the so-called Bonferroni correction. The idea is if the experimenter is conducting *n* number of statistical tests then each of the individual tests should be tested under a significance level that is divided by *n*. The Bonferroni correction was derived from the observation that if *n* tests are performed with an *alpha* significance level then the probability that one comes out significantly is =< *n**//alpha// (Boole's inequality). In order, to keep this probability lower, we can use an *alpha* that is divided by *n* for each test. However, the correction comes at the cost of increasing the probability of false negatives, i.e. the test does not have enough power to reveal differences among conditions.   

Contrary to the familiar parametric statistical framework, it is straightforward to solve the MCP in the nonparametric framework. Nonparametric tests offer a freedom to the experimenter which test statistics are used for compering conditions, and help to maximize the sensitivity to the expected effect. For more details see the publication by [Maris and Oostenveld (2007)](/references_to_implemented_methods#statistical_inference_by_means_of_permutation) and the [Cluster-based permutation tests on event related fields](/tutorial/cluster_permutation_timelock)
and the [Cluster-based permutation tests on time-frequency data](/tutorial/cluster_permutation_freq) tutorials.

## Procedure

To do parametric or non-parametric statistics on event-related fields in a within-subject design we will use a dataset of 10 subjects that has been already preprocessed, the planar gradient and the subject-averages of two conditions have been already computed, and the **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)** function has already combined the data from each subject to one structure for both conditions. The gray boxes of Figure 1. show those steps which have been done already. (The orange boxes in the gray boxes (except of the ft_timelockgrandaverage step) represent processing steps that are done on all trials that belong to one subject in one condition). These steps are described in the [Trigger-based trial selection](/tutorial/preprocessing) and in the [Event related averaging and planar gradient](/tutorial/eventrelatedaveraging) tutorial. How to use the **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)** function will be described in this tutorial.

We will perform the following steps to do a statistical test in FieldTrip

*  Optionally, we can visually inspect the data and look where are differences between the conditions by plotting the grand-averages and subject-averages using the **[ft_multiplotER](/reference/ft_multiploter)**, the **[ft_singleplotER](/reference/ft_singleploter)** and the Matlab plot functions

*  To do any kind of statistical testing (parametric or non-parametric, with or without multiple comparison correction) we will use the **[ft_timelockstatistics](/reference/ft_timelockstatistics)** function

*  We can plot a schematic head with the channels where the effect is significant with the **[ft_topoplotER](/reference/ft_topoploter)** function or optionally with the **[ft_clusterplot](/reference/ft_clusterplot)** function (in case cluster-based non-parametric statistics was used)

![image](/media/development/project/tutorial_stat/ft_stat_tutorial2.png)

*Figure 1. Pipeline of statistical testing. All analysis steps in the gray boxes have been done already.*

## Reading-in, preprocessing, timelockanalysis, planar gradient, and grandaveraging

We now describe how we can statistically test the difference between the event-related averages for fully incongruent (FIC) and the fully congruent (FC) sentence endings. For this analysis we use planar gradient data. For convenience we will not do the reading-in and preprocessing steps on all subjects. Instead we begin by loading the timelock structures containing the event-related averages (of the planar gradient data) of all ten subjects. The data is available from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/cluster_permutation_timelock/GA_ERF_orig.mat](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/cluster_permutation_timelock/GA_ERF_orig.mat).

	  load GA_ERF_orig;

The event-related averages for the fully incongruent and the fully congruent sentence endings are stored in GA_FIC and GA_FC. These averages were calculated using the function **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)**. In the configuration for **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)**, the option cfg.keepindividual = ‘yes’ has to be chosen. (This has been done in the example data.) If this option is not used, then only the average ERF of all subjects (the grand-average) will be calculated. The grand-average can be found in the "avg" field, the subject averages are in the field "individual".

## Parametric statistics (this will be familiar to all of you)

### A single comparison

#### Plotting the grand-average and the subject-averages
 Plot all channels with **[ft_multiplotER](/reference/ft_multiplotER)**, and channel MLT12 with **[ft_singleplotER](/reference/ft_singleplotER)**.

	load GA_ERF_orig % Grand average of planar gradient, 10 subjects

	cfg = [];
	cfg.showlabels  = 'yes';
	cfg.layout    	= 'CTF151.lay';
	figure; ft_multiplotER(cfg,GA_FC, GA_FIC)
	
	cfg = [];
	cfg.channel = 'MLT12';
	figure; ft_singleplotER(cfg,GA_FC, GA_FIC)

![image](/media/tutorial/eventrelatedstatistics/multiplot_ga_fc_fic.png@400)

![image](/media/tutorial/eventrelatedstatistics/singleplotMLT12_ga_fc_fic.png@400)

To get an idea of the data, plot the ERF of channel MLT12 for all subject

	figure; 
	for iSub = 1:10
	  subplot(3,4,iSub)
	  plot(GA_FC.time,squeeze(GA_FC.individual(iSub,52,:)))
	  hold on
	  plot(GA_FIC.time,squeeze(GA_FIC.individual(iSub,52,:)),'r')
	  title(strcat('subject ',num2str(iSub)))
	  ylim([0 1.9e-13])
	  xlim([-1 2])
	end
	subplot(3,4,11); 
	text(0.5,0.5,'FC','color','b') ;text(0.5,0.3,'FIC','color','r')
	axis off

![image](/media/tutorial/eventrelatedstatistics/plotmlt12_allsubj_fc_fic.png@400)

Between 300ms and 700ms there seems to be a difference between the FC and the FIC condition in the grand average in channel MLT12 (channel 52).

	chan = 52;
	time = [0.3 0.7];
	
	timesel_FIC = find(GA_FIC.time >= time(1) & GA_FIC.time <= time(2));
	values_FIC = mean(GA_FIC.individual(:,chan,timesel_FIC),3);
	
	timesel_FC = find(GA_FC.time >= time(1) & GA_FC.time <= time(2));
	values_FC = mean(GA_FC.individual(:,chan,timesel_FC),3);
	
	% plot to see the effect in each subject
	M = [values_FC,values_FIC];
	figure; plot(M','o-'); xlim([0.5 2.5])
	legend({'subj1', 'subj2', 'subj3', 'subj4', 'subj5', 'subj6', ...
	        'subj7', 'subj8', 'subj9', 'subj10'}, 'location','EastOutside');

![image](/media/tutorial/eventrelatedstatistics/mlt12_300to700ms_allsubj_fc_fic.png@400)

#### T-test with Matlab function

You can do a dependent samples t-test with the Matlab ttest.m function (in the Statistics toolbox) where you average over this time window and compare. This shows that the effect on the selected time and channel is significant with a t-value of -4.9999 and a p-value of 0.00073905.

	%dependent samples ttest
	FCminFIC = values_FC - values_FIC;
	[h,p,ci,stats] = ttest(FCminFIC, 0, 0.05) % H0: mean = 0, alpha 0.05

#### T-test with FieldTrip function

You can do the same thing in FieldTrip (which does not require the statistics toolbox) using the **[ft_timelockstatistics](/reference/ft_timelockstatistics)** function. This gives you the same p-value of 0.00073905

	cfg = [];
	cfg.channel     = 'MLT12';
	cfg.latency     = [0.3 0.7];
	cfg.avgovertime = 'yes';
	cfg.parameter   = 'individual';
	cfg.method      = 'analytic';
	cfg.statistic   = 'depsamplesT';
	cfg.alpha       = 0.05;
	cfg.correctm    = 'no';
	
	Nsub = 10;
	cfg.design(1,1:2*Nsub)  = [ones(1,Nsub) 2*ones(1,Nsub)];
	cfg.design(2,1:2*Nsub)  = [1:Nsub 1:Nsub];
	cfg.ivar                = 1; % the 1st row in cfg.design contains the independent variable
	cfg.uvar                = 2; % the 2nd row in cfg.design contains the subject number
	
	stat = ft_timelockstatistics(cfg,GA_FC,GA_FIC)

####  Exercise 1

`<note exercise>`
Look at the temporal evolution of the effect by changing cfg.latency and cfg.avgovertime in **[ft_timelockstatistics](/reference/ft_timelockstatistics)**. You can plot the t-value versus time, the probability versus time and the statistical mask versus time. Note that the output of the **[ft_timelockstatistics](/reference/ft_timelockstatistics)** function closely resembles the output of the **[ft_timelockanalysis](/reference/ft_timelockanalysis)** function.
`</note>` 

### Multiple comparisons

In the previous paragraph we picked a channel and time window by hand after eyeballing the effect. If you would like to test the significance of the effect in all channels you could make a loop over channels.

	%loop over channels
	time = [0.3 0.7];
	timesel_FIC = find(GA_FIC.time >= time(1) & GA_FIC.time <= time(2));
	timesel_FC = find(GA_FC.time >= time(1) & GA_FC.time <= time(2));
	clear h p
	for iChan = 1:151
	  FICminFC = mean(GA_FIC.individual(:,iChan,timesel_FIC),3) - mean(GA_FC.individual(:,iChan,timesel_FC),3);
	  [h(iChan), p(iChan)] = ttest(FICminFC, 0, 0.05 ); % test each channel separately
	end
	
	% plot uncorrected "significant" channels
	cfg = [];
	cfg.style     = 'blank';
	cfg.layout    = 'CTF151.lay';
	cfg.highlight = 'on';
	cfg.highlightchannel = find(h);
	cfg.comment   = 'no';
	figure; ft_topoplotER(cfg, GA_FC)
	title('significant without multiple comparison correction')

![image](/media/tutorial/eventrelatedstatistics/depttestmatlab_nomcc.png@200)

But since you're now performing 151 individual tests, you are not controlling the false alarm rate any more. Under the null-hypothesis and with an alpha of 5%, you have a 5% chance of making a false alarm and incorrectly conclude that the null-hypothesis should be rejected. That false alarm rate applies to each test that you perform, so the chance of making a false alarm if you do 151 subsequent tests is much larger than the desired 5%. This is the multiple comparison problem. 

To ensure that the false alarm rate is controlled at the desired alpha level over all channels, you should do a correction for multiple comparisons. The best known correction is the Bonferoni correction, which allows to control the false alarm rate if you do multiple independent tests. For a Bonferoni correction you would divide your initial alpha level (i.e. the desired upper boundary for the false alarm rate) by the number of tests that you perform. In this case with 151 channels the alpha level would become 0.05/151 which is 0.00033113. With this alpha the effect is not significant anymore on any channel. However, a Bonferoni correction is too conservative in this case; the effect on one MEG channel is highly correlated in neighboring channels. Although the Bonferoni correction achieves the desired control of the type-I error (false alarm rate), the type-II error (chance of not rejecting H0 when it in fact should be rejected) is much larger than desired.

Below you can see the means by which to implement a Bonferoni correction and find other corrections for multiple comparisons which are less conservative and hence more sensitive.

#### Bonferoni correction with Matlab function

	% with Bonferoni correction for multiple comparisons
	for iChan = 1:151
	  FICminFC = mean(GA_FIC.individual(:,iChan,timesel_FIC),3) - mean(GA_FC.individual(:,iChan,timesel_FC),3);
	  [h(iChan), p(iChan)] = ttest(FICminFC, 0, 0.05/151); % Bonferoni correction for 151 channels
	end

#### Bonferoni correction with FieldTrip function

	cfg = [];
	cfg.channel     = 'MEG'; %now all channels
	cfg.latency     = [0.3 0.7];
	cfg.avgovertime = 'yes';
	cfg.parameter   = 'individual';
	cfg.method      = 'analytic';
	cfg.statistic   = 'depsamplesT'
	cfg.alpha       = 0.05;
	cfg.correctm    = 'bonferoni';
	
	Nsub = 10;
	cfg.design(1,1:2*Nsub)  = [ones(1,Nsub) 2*ones(1,Nsub)];
	cfg.design(2,1:2*Nsub)  = [1:Nsub 1:Nsub];
	cfg.ivar                = 1; % the 1st row in cfg.design contains the independent variable
	cfg.uvar                = 2; % the 2nd row in cfg.design contains the subject number
	
	stat = ft_timelockstatistics(cfg,GA_FIC,GA_FC)

Fieldtrip also has other methods implemented for performing a multiple comparison correction, such as FDR. See the statistics_analytic function for the options to cfg.correctm when you want to do a parametric test.

##  Non-parametric statistics

### Permutation test based on t statistics

Instead of using the analytic t-distribution to calculate the appropriate p-value for your effect, you can also use a nonparametric randomization test to obtain the p-value. 

This is implemented in FieldTrip in the function statistics_montecarlo which is called by **[ft_timelockstatistics](/reference/ft_timelockstatistics)** when you set cfg.method = 'montecarlo'. An Monte-Carlo estimate of the significance probabilities and/or critical values is then calculated based on randomizing or permuting your data many times between the conditions.

	cfg = [];
	cfg.channel     = 'MEG';
	cfg.latency     = [0.3 0.7];
	cfg.avgovertime = 'yes';
	cfg.parameter   = 'individual';
	cfg.method      = 'montecarlo';
	cfg.statistic   = 'depsamplesT'
	cfg.alpha       = 0.05;
	cfg.correctm    = 'no';
	cfg.correcttail = 'prob';
	cfg.numrandomization = 1000;
	
	Nsub = 10;
	cfg.design(1,1:2*Nsub)  = [ones(1,Nsub) 2*ones(1,Nsub)];
	cfg.design(2,1:2*Nsub)  = [1:Nsub 1:Nsub];
	cfg.ivar                = 1; % the 1st row in cfg.design contains the independent variable
	cfg.uvar                = 2; % the 2nd row in cfg.design contains the subject number
	
	stat = ft_timelockstatistics(cfg,GA_FIC,GA_FC)
	
	% make the plot
	cfg = [];
	cfg.style     = 'blank';
	cfg.layout    = 'CTF151.lay';
	cfg.highlight = 'on';
	cfg.highlightchannel = find(stat.mask);
	cfg.comment   = 'no';
	figure; ft_topoplotER(cfg, GA_FC)
	title('Nonparametric: significant without multiple comparison correction')

![image](/media/tutorial/eventrelatedstatistics/depttest_nonpara_fieldtrip_nomcc.png@200)

 

Also in the non-parametric approach for testing of statistical significance different corrections for multiple comparisons such as Bonferoni, fdr, and others are implemented. See the options for cfg.correctm in statistics_montecarlo.

###  Permutation test based on cluster statistics

FieldTrip also implements a special way to correct for multiple comparisons, which makes use of the feature in the data that the effect at neighbouring timepoints and sensors is highly correlated. For more details see the cluster permutation tutorials for [ ERFs](/tutorial/cluster_permutation_timelock) and [ time frequency data](/tutorial/cluster_permutation_freq) and the publication by [Maris and Oostenveld (2007)](/references_to_implemented_methods#statistical_inference_by_means_of_permutation).

With this method for multiple comparisons the following sensors show a significant effect (p<0.05) between 0.3 and 0.7 s.

	cfg = [];
	cfg.channel     = 'MEG';
	cfg.latency     = [0.3 0.7];
	cfg.avgovertime = 'yes';
	cfg.parameter   = 'individual';
	cfg.method      = 'montecarlo';
	cfg.statistic   = 'depsamplesT'
	cfg.alpha       = 0.05;
	cfg.correctm    = 'cluster';
	cfg.correcttail = 'prob';
	cfg.grad        = GA_FC.grad; %see ft_neighbourselection
	cfg.numrandomization = 1000;
	
	Nsub = 10;
	cfg.design(1,1:2*Nsub)  = [ones(1,Nsub) 2*ones(1,Nsub)];
	cfg.design(2,1:2*Nsub)  = [1:Nsub 1:Nsub];
	cfg.ivar                = 1; % the 1st row in cfg.design contains the independent variable
	cfg.uvar                = 2; % the 2nd row in cfg.design contains the subject number
	
	stat = ft_timelockstatistics(cfg,GA_FIC,GA_FC)
	
	% make a plot
	cfg = [];
	cfg.style     = 'blank';
	cfg.layout    = 'CTF151.lay';
	cfg.highlight = 'on';
	cfg.highlightchannel = find(stat.mask);
	cfg.comment   = 'no';
	figure; ft_topoplotER(cfg, GA_FC)
	title('Nonparametric: significant with cluster multiple comparison correction')

![image](/media/tutorial/eventrelatedstatistics/depttest_nonpara_fieldtrip_cluster2.png@200)

 

So far we predefined a time window over which the effect was averaged, and tested the difference of that between conditions. You can also **not** predefine a timewindow and cluster simultaneously over neighboring channels and neighboring time points. See the example below. Now a channel-time cluster is found from 0.33 s untill 0.52 s in which p < 0.05.

	cfg = [];
	cfg.channel     = 'MEG';
	cfg.latency     = [-0.5 2];
	cfg.avgovertime = 'no';
	cfg.parameter   = 'individual';
	cfg.method      = 'montecarlo';
	cfg.statistic   = 'depsamplesT'
	cfg.alpha       = 0.05;
	cfg.correctm    = 'cluster';
	cfg.correcttail = 'prob';
	cfg.numrandomization = 1000;
	cfg.grad             = GA_FC.grad; %see ft_neighbourselection
	cfg.minnbchan        = 2; % minimal neighbouring channels
	
	Nsub = 10;
	cfg.design(1,1:2*Nsub)  = [ones(1,Nsub) 2*ones(1,Nsub)];
	cfg.design(2,1:2*Nsub)  = [1:Nsub 1:Nsub];
	cfg.ivar                = 1; % the 1st row in cfg.design contains the independent variable
	cfg.uvar                = 2; % the 2nd row in cfg.design contains the subject number
	
	stat = ft_timelockstatistics(cfg,GA_FIC,GA_FC)

**[ft_clusterplot](/reference/ft_clusterplot)** can be used to plot the effect.

	% make a plot
	cfg = [];
	cfg.highlightsymbolseries = ['*','*','.','.','.'];
	cfg.layout = 'CTF151.lay';
	cfg.contournum = 0;
	cfg.markersymbol = '.';
	cfg.alpha = 0.05;
	cfg.zlim = [-5 5];
	ft_clusterplot(cfg,stat);

![image](/media/tutorial/eventrelatedstatistics/depttest_nonpara_fieldtrip_cluster_fig1.png@400)

![image](/media/tutorial/eventrelatedstatistics/depttest_nonpara_fieldtrip_cluster_fig2.png@400)

![image](/media/tutorial/eventrelatedstatistics/depttest_nonpara_fieldtrip_cluster_fig3.png@400)

![image](/media/tutorial/eventrelatedstatistics/depttest_nonpara_fieldtrip_cluster_fig4.png@400)

## Summary and suggested further reading

This tutorial showed how to perform parametric and non-parametric statistics in FieldTrip. It was also shown how to do t-test and Bonferroni correction with Matlab functions, and how to plot the sensors that show a significant effect.

After this gentle introduction in statistics with FieldTrip, you can continue with the [Cluster-based permutation tests on event related fields](/tutorial/cluster_permutation_timelock)
and the [cluster-based permutation tests on time-frequency data](/tutorial/cluster_permutation_freq) tutorials. These give a more detailed description of non-parametric statistical testing with a cluster-based approach.

This tutorial was last tested with version 20110304 of FieldTrip by Jan-Mathijs, using Matlab 7.6 on MacOSX 10.5.8

