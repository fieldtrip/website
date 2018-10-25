---
title: Introduction
layout: default
---

## Introduction

In this tutorial we will explore different measures of connectivity, using simulated data and using source-level MEG data. You will learn how to compute various connectivity measures and how these measures can be interpreted. Furthermore, a number of interpretational problems will be addressed.

Since this tutorial focusses on connectivity measures in the frequency domain, we expect that you understand the basics of frequency domain analysis, because this is not covered by this tutorial. 

Note that this tutorial does not cover all possible pitfalls associated with the analysis of connectivity and the interpretational difficulties. Although the computation of connectivity measures might be easy using FieldTrip, the interpretation of the outcomes of those measures in terms of brain networks and activity remains challenging and should be exercised with caution.

## Background

The brain is organized in functional units, which at the smallest level consists of neurons, and at higher levels consists of larger neuronal populations. Functional localization studies consider the brain to be organized in specialized neuronal modules corresponding to specific areas in the brain. These functionally specialized brain areas (e.g. visual cortex area V1, V2, V4, MT, ...) have to pass information back and forth along anatomical connections. The identification of these functional connections and determining their functional relevance comprises connectivity analysis and can be done using the **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)** and associated functions.

The nomenclature for connectivity analysis can be adopted from [graph theory](http://en.wikipedia.org/wiki/Graph_theory), in which brain areas correspond to nodes or vertices and the connections between the nodes is given by edges. One of the fundamental challenges in the analysis of brain networks from MEG and EEG data lies not only in identifying the "edges", i.e. the functional connections, but also the "nodes". The remainder of this tutorial will only explain the methods to characterize the edges, but will not go into detail into identifying the nodes. The [tutorial:beamformer](/tutorial/beamformer) and [corticomuscular coherence](/tutorial/coherence) tutorial provide more pointers to localizing the nodes.

Many measures of connectivity exist, and they can be broadly divided into measures of functional connectivity (denoting statistical dependencies between measured signals, without information about causality/directionality), and measures of effective connectivity, which describe directional interactions. 

After the identification of the network nodes and the characterization of the edges between the nodes, it is possible to analyze and describe certain network features in more detail. This network analysis is also not covered in this tutorial, although FieldTrip provides some functionality in this direction (see **[ft_networkanalysis](/reference/ft_networkanalysis)** to get started).

## Procedure

This tutorial consists of three part

*  Simulated data with directed connections. In this part we are going to simulate some data and use these data to compute various connectivity metrics. As a generative model of the data we will use a multivariate autoregressive model and we will use **[ft_connectivitysimulation](/reference/ft_connectivitysimulation)** for this. Subsequently, we will estimate the multivariate autoregressive model and the spectral transfer function, and the cross-spectral density matrix using the functions **[ft_mvaranalysis](/reference/ft_mvaranalysis)** and **[ft_freqanalysis](/reference/ft_freqanalysis)**. In the next step we will compute and inspect various measures of connectivity with  **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)** and **[ft_connectivityplot](/reference/ft_connectivityplot)**.

*  Simulated data with common pick-up and different noise levels. In this part we are going to simulate some data consisting of an instantaneous mixture of 3 'sources', creating a situation of common pick up. We will explore the effect of this common pick up on the consequent estimates of connectivity, and we will investigate the effect of different mixings on these estimates. 

*  Connectivity between MEG virtual channel and EMG. In this part we are going to reconstruct MEG virtual channel data and estimate connectivity between this virtual channel and EMG. The data used for this part are the same as in the [Analysis of corticomuscular coherence](/tutorial/coherence) tutorial.

## Simulated data with directed connections

We will first simulate some data with a known connectivity structure built in. This way we know what to expect in terms of connectivity. To simulate data we use **[ft_connectivitysimulation](/reference/ft_connectivitysimulation)**. We will use an order 2 multivariate autoregressive model. The necessary ingredients are a set of NxN coefficient matrices, one matrix for each time lag. These coefficients need to be stored in the cfg.param field. Next to the coefficients we have to specify the NxN covariance matrix of the innovation noise. This matrix needs to be stored in the cfg.noisecov field.
The model we are going to use to simulate the data is as follow

x(t) = 0.8*x(t-1) - 0.5*x(t-2)

y(t) = 0.9*y(t-1) + 0.5*z(t-1) - 0.8*y(t-2)

z(t) = 0.5*z(t-1) + 0.4*x(t-1) - 0.2*z(t-2)

	
	cfg             = [];
	cfg.ntrials     = 500;
	cfg.triallength = 1;
	cfg.fsample     = 200;
	cfg.nsignal     = 3;
	cfg.method      = 'ar';
	
	cfg.params(:,:,1) = [ 0.8    0    0 ; 
	                        0  0.9  0.5 ;
	                      0.4    0  0.5];
	                      
	cfg.params(:,:,2) = [-0.5    0    0 ; 
	                        0 -0.8    0 ; 
	                        0    0 -0.2];
	                        
	cfg.noisecov      = [ 0.3    0    0 ;
	                        0    1    0 ;
	                        0    0  0.2];
	
	data              = ft_connectivitysimulation(cfg);
	

The simulated data consists of 3 channels in 500 trials. You can easily visualize the data for example in the first trial using

    figure
    plot(data.time{1}, data.trial{1}) 
    legend(data.label)
    xlabel('time (s)')

![image](/media/tutorial/connectivity/data.png@400)

or browse through the complete data using

    cfg = [];
    cfg.viewmode = 'vertical';  % you can also specify 'butterfly' 
    ft_databrowser(cfg, data);

![image](/media/tutorial/connectivity/databrowser.png@400)

### Computation of the multivariate autoregressive model

To be able to compute spectrally resolved [Granger causality](http://en.wikipedia.org/wiki/Granger_causality), or other frequency-domain directional measures of connectivity, we have to fit an autoregressive model to the data. This is done using the **[ft_mvaranalysis](/reference/ft_mvaranalysis)** function. 

For the actual computation of the autoregressive coefficients FieldTrip makes use of an implementation from third party toolboxes. At present **[ft_mvaranalysis](/reference/ft_mvaranalysis)** supports the [biosig](http://biosig.sourceforge.net/) and [bsmart](http://www.brain-smart.org) toolboxes for these computations. 

In this tutorial we will use the bsmart toolbox. The relevant functions have been included in the FieldTrip release in the fieldtrip/external/bsmart directory.

	
	cfg         = [];
	cfg.order   = 5;
	cfg.toolbox = 'bsmart';
	mdata       = ft_mvaranalysis(cfg, data);
	
	mdata = 
	         dimord: 'chan_chan_lag'
	          label: {3x1 cell}
	         coeffs: [3x3x5 double]
	       noisecov: [3x3 double]
	            dof: 500
	    fsampleorig: 200
	            cfg: [1x1 struct]
	            

The resulting variable **mdata** contains a description of the data in terms of a multivariate autoregressive model. For each time-lag up to the model order (which is 5 in this case), a 3x3 matrix of coefficients is outputted. The noisecov-field contains covariance matrix of the model's residuals.

#### Exercise 1

<div class="exercise">
Compare the parameters specified for the simulation with the estimated coefficients and discuss.
</div>

### Computation of the spectral transfer function

From the autoregressive coefficients it is now possible to compute the spectral transfer matrix, for which we use **[ft_freqanalysis](/reference/ft_freqanalysis)**.

`<codeb>`
cfg        = [];
cfg.method = 'mvar';
mfreq      = ft_freqanalysis(cfg, mdata);

mfreq = 
        label: {3x1 cell}
         freq: [1x101 double]
       dimord: 'chan_chan_freq'
     transfer: [3x3x101 double]
     noisecov: [3x3 double]
    crsspctrm: [3x3x101 double]
          dof: 500
          cfg: [1x1 struct]
          
`</code>`

The resulting **mfreq** data structure contains the pairwise transfer function between the 3 channels for 101 frequencies. 

It is also possible to compute the spectral transfer function using non-parametric spectral factorization of the cross-spectral density matrix. For this, we need a Fourier decomposition of the data. This is done in the following section.

### Non-parametric computation of the cross-spectral density matrix

Some connectivity metrics can be computed from a non-parametric spectral estimate (i.e. after the application of the FFT-algorithm and conjugate multiplication to get cross-spectral densities), such as coherence, phase-locking value and phase slope index. The following part computes the fourier-representation of the data using **[ft_freqanalysis](/reference/ft_freqanalysis)**. It is not necessary to compute the cross-spectral density at this stage, because the function used in the next step, **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)**, contains functionality to compute the cross-spectral density from the fourier coefficients.

	
	cfg           = [];
	cfg.method    = 'mtmfft';
	cfg.taper     = 'dpss';
	cfg.output    = 'fourier';
	cfg.tapsmofrq = 2;
	freq          = ft_freqanalysis(cfg, data);
	
	freq = 
	            label: {3x1 cell}
	           dimord: 'rpttap_chan_freq'
	             freq: [1x101 double]
	    fourierspctrm: [1500x3x101 double]
	        cumsumcnt: [500x1 double]
	        cumtapcnt: [500x1 double]
	              cfg: [1x1 struct]
	

The resulting **freq** structure contains the spectral estimate for 3 tapers in each of the 500 trials (hence 1500 estimates), for each of the 3 channels and for 101 frequencies.

### Computation and inspection of the connectivity measures

The actual computation of the connectivity metric is done by **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)**. This function is transparent to the type of input data, i.e. provided the input data allows the requested metric to be computed, the metric will be calculated. Here, we provide an example for the computation and visualization of the coherence coefficient.

	
	cfg           = [];
	cfg.method    = 'coh';
	coh           = ft_connectivityanalysis(cfg, freq);
	cohm          = ft_connectivityanalysis(cfg, mfreq);
	

Subsequently, the data can be visualized using **[ft_connectivityplot](/reference/ft_connectivityplot)**.

	
	cfg           = [];
	cfg.parameter = 'cohspctrm';
	cfg.zlim      = [0 1];
	ft_connectivityplot(cfg, coh, cohm);

![image](/media/tutorial/connectivity/connectivityplot.png@400)

The coherence measure is a symmetric measure, which means that it does not provide information regarding the direction of information flow between any pair of signals. In order to analyze directionality in interactions, measures based on the concept of granger causality can be computed. These measures are based on an estimate of the spectral transfer matrix, which can be computed in a straightforward way from the multivariate autoregressive model fitted to the data.

	
	cfg           = [];
	cfg.method    = 'granger';
	granger       = ft_connectivityanalysis(cfg, mfreq);
	
	cfg           = [];
	cfg.parameter = 'grangerspctrm';
	cfg.zlim      = [0 1];
	ft_connectivityplot(cfg, granger);
	

![image](/media/tutorial/connectivity/grangerplot1.png@400)

Instead of plotting it with **[ft_connectivityplot](/reference/ft_connectivityplot)**, you can use the following low-level Matlab plotting code which gives a better understanding of the numerical representation of the results.

	
	figure
	for row=1:3
	for col=1:3
	  subplot(3,3,(row-1)*3+col);
	  plot(granger.freq, squeeze(granger.grangerspctrm(row,col,:)))
	  ylim([0 1])
	end
	end

![image](/media/tutorial/connectivity/grangerplot2.png@400)

#### Exercise 2

<div class="exercise">
Discuss the differences between the granger causality spectra, and the coherence spectra.
</div>

#### Exercise 3

<div class="exercise">
Compute the following connectivity measures from the **mfreq** data, and visualize and discuss the results: partial directed coherence (pdc), directed transfer function (dtf), phase slope index (psi)
</div>

## Simulated data with common pick-up and different noise levels

FIXME this is under progress

When working with electrophysiological data (EEG/MEG/LFP) the signals that are picked up by the individual channels invariably consist of instantaneous mixtures of the underlying source signals. This mixing can severely affect the outcome of connectivity analysis, and thus affects the interpretation. We will demonstrate this by simulating data in 2 channels, where each of the channels consists of a weighted combination of temporally white noise unique to each of the channels, and a common input of a band-limited signal (filtered between 15 and 25 Hz). We will compute connectivity between these channels, and show that the common input can give rise to spurious estimates of connectivity.  

	
	
	% create some instantaneously mixed data
	
	% define some variables locally
	nTrials  = 100;
	nSamples = 1000;
	fsample  = 1000;
	
	% mixing matrix
	mixing   = [0.8 0.2 0;
	              0 0.2 0.8];
	
	data       = [];
	data.trial = cell(1,nTrials);
	data.time  = cell(1,nTrials);
	for k = 1:nTrials
	  dat = randn(3, nSamples);
	  dat(2,:) = ft_preproc_bandpassfilter(dat(2,:), 1000, [15 25]);
	  dat = 0.2.*(dat-repmat(mean(dat,2),[1 nSamples]))./repmat(std(dat,[],2),[1 nSamples]);
	  data.trial{k} = mixing * dat;
	  data.time{k}  = (0:nSamples-1)./fsample;
	end
	data.label = {'chan1' 'chan2'}';
	
	figure;plot(dat'+repmat([0 1 2],[nSamples 1]));
	title('original ''sources''');
	
	figure;plot((mixing*dat)'+repmat([0 1],[nSamples 1])); 
	axis([0 1000 -1 2]);
	set(findobj(gcf,'color',[0 0.5 0]), 'color', [1 0 0]);
	title('mixed ''sources''');

![image](/media/tutorial/connectivity/mixingmixed.png@300)
![image](/media/tutorial/connectivity/mixingunmixed.png@300)

	
	
	% do spectral analysis
	cfg = [];
	cfg.method    = 'mtmfft';
	cfg.output    = 'fourier';
	cfg.foilim    = [0 200];
	cfg.tapsmofrq = 5;
	freq          = ft_freqanalysis(cfg, data);
	fd            = ft_freqdescriptives(cfg, freq);
	
	figure;plot(fd.freq, fd.powspctrm);
	set(findobj(gcf,'color',[0 0.5 0]), 'color', [1 0 0]);
	title('powerpectrum');
	

![image](/media/tutorial/connectivity/mixingpowerspectrum.png@300)

	
	
	% compute connectivity
	cfg = [];
	cfg.method = 'granger';
	g = ft_connectivityanalysis(cfg, freq);
	cfg.method = 'coh';
	c = ft_connectivityanalysis(cfg, freq);
	

	
	
	% visualize the results
	cfg = [];
	cfg.parameter = 'grangerspctrm';
	figure;ft_connectivityplot(cfg, g);
	cfg.parameter = 'cohspctrm';
	figure;ft_connectivityplot(cfg, c);
	

![image](/media/tutorial/connectivity/mixinggranger.png@300)
![image](/media/tutorial/connectivity/mixingcoherence.png@300)

#### Exercise 4

<div class="exercise">
Simulate new data using the following mixing matrix: 

	
	
	[0.9 0.1 0;0 0.2 0.8] 
	

and recompute the connectivity measures. Discuss what you see.

</div>

#### Exercise 5

<div class="exercise">
Play a bit with the parameters in the mixing matrix and see what is the effect on the estimated connectivity.
</div>

#### Exercise 6

<div class="exercise">
Simulate new data where the 2 mixed signals are created from 4 underlying sources, and where two of these sources are common input to both signals, and where these two sources are temporally shifted copies of one another.

Hint: the mixing matrix could look like thi

	
	[a b c 0; 0 d e f];

and the trials could be created like thi

	
	for k = 1:nTrials
	  dat = randn(4, nSamples+10);
	  dat(2,:) = ft_preproc_bandpassfilter(dat(2,:), 1000, [15 25]);
	  dat(3,1:(nSamples)) = dat(2,11:(nSamples+10)); 
	  dat = dat(:,1:1000);
	  dat = 0.2.*(dat-repmat(mean(dat,2),[1 nSamples]))./repmat(std(dat,[],2),[1 nSamples]);
	  data.trial{k} = mixing * dat;
	  data.time{k}  = (0:nSamples-1)./fsample;
	end

Compute connectivity between the signals and discuss what you observe. In particular, also compute measures of directed interaction.
</div>
