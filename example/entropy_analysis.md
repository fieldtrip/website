```markdown
---
title: Performing multi-scale entropy analysis on EEG/MEG/LFP data 
tags: [example, entropy]
---

# Background

Recently, we have developed a novel algorithm based on multi-scale entropy **[Costa et al. 2002](https://doi.org/10.1103/PhysRevLett.89.068102)** called modified multi-scale entropy (mMSE) that directly quantifies the temporal irregularity of time-domain EEG/MEG/LFP signals at longer and shorter timescales. In general, patterns of fluctuations in brain activity that tend to repeat over time are assigned lower entropy, whereas more irregular, non-repeating patterns yield higher entropy. To allow the investigation of dynamic changes in signal irregularity, we developed mMSE as a time-resolved variant, while also permitting assessment of entropy over atypically longer time scales by calculating across discontinuous, concatenated segments **[Grandy et al.](https://doi.org/10.1038/srep23073)** (see the figure below). 

{% include image src="/assets/img/example/entropy_analysis/mMSEmethod.png" %}
 
Please see our preprints **[Kloosterman et al.](https://doi.org/10.1101/834614)** and **[Kosciessa et al.](https://doi.org/10.1101/752808)** for more information, and the tutorial folder on our Github page for a step-by-step explanation of the computation of multiscale entropy within our MATLAB function.

# Download and install the mMSE toolbox

To run entropy analysis on your data, download the mMSE toolbox for FieldTrip from our GitHub page as follows:
	
	git clone https://github.com/LNDG/mMSE.git

or use the Download button on the GitHub page. The mMSE toolbox folder can be placed anywhere – it is not necessary to have it in your FieldTrip folder. However, the folder needs to be added to the path so MATLAB can find it. Furthermore, availability of the FieldTrip toolbox is required as the mMSE code relies on various FieldTrip helper functions. You can do this as follows:

	addpath /path/to/your/mMSEfolder

After this step, you can call **[ft_entropyanalysis](https://github.com/LNDG/mMSE/blob/master/ft_entropyanalysis.m)** as any other FieldTrip function.

# Run multi-scale entropy analysis on your data

**[ft_entropyanalysis](https://github.com/LNDG/mMSE/blob/master/ft_entropyanalysis.m)** takes as input preprocessed data as produced by **[ft_preprocessing](/reference/ft_preprocessing)**. A few points are important to consider when preprocessing data for entropy analysis. First, it is advisable to apply a high-pass filter to your data to remove slow drifts. This is because entropy is computed by counting how often patterns reoccur in the time-domain data. To determine patterns, the data is first discretized by defining boundaries around each data point. These boundaries are set based on the standard deviation of the time-domain-signal. Slow drifts (e.g., due to electrode motion during the recording in EEG) will increase the standard deviation, thus loosening these boundaries, which in turn will result in more pattern matches and thus lower estimations of entropy **[Kosciessa et al.](https://doi.org/10.1101/752808)**. We have previously used a standard high-pass Butterworth filter during preprocessing, with a cutoff of 0.5 Hz on the continuous data (prior to defining trials), with good results. 

Second, entropy is often computed for shorter and longer time scales. Longer time scales are accessed by increasingly coarsening the data by either averaging neighbouring data points or point skipping after low-pass filtering. Therefore, the timescales you can access depend on the sampling rate of the data. Given that entropy analysis can become computationally  intensive with the high sampling rates and high number of channels typically used in E/MEG, we recommend downsampling to make the data easier to handle. In our example, we use a sampling rate of 256 Hz.

A final point pertains to the boundaries that are set around each data point to count pattern matches (see figure above). By increasingly smoothing the time series, coarse-graining affects not only on the signal’s entropy, but also its overall variation, as reflected in the decreasing standard deviation as a function of time scale (see **[Nikulin and Brismar, 2004](https://doi.org/10.1103/PhysRevLett.92.089803)**). In the original implementation of the MSE calculation, the similarity parameter `r` was set as a proportion of the original (scale 1) time series’ standard deviation and applied to all the scales **[Costa et al. 2002](https://doi.org/10.1103/PhysRevLett.89.068102)**. Because of the decreasing variation in the time series due to coarse graining, the similarity parameter therefore becomes increasingly tolerant at longer time scales, resulting in more similar patterns and decreased entropy. This decreasing entropy can be attributed both to changes in signal complexity, but also in overall variation. To overcome this limitation, we advise recomputing the similarity parameter for each timescale, thereby normalizing MSE with respect to changes in overall time series variation at each scale. This feature can be controlled using the `cfg.recompute_r` parameter, as explained below.

To run entropy analysis on your preprocessed data, first define the configuration:

	cfg = [];
	cfg.m                 = 2; % pattern length
	cfg.r                 = 0.5; % similarity criterion 0.5
	cfg.timwin            = 0.5; % sliding window size
	cfg.toi               = -0.5:0.05:1; % set this according to your trial length
	cfg.timescales        = 1:42; %1:40; % scale list
	cfg.recompute_r       = 'perscale_toi_sp';  
	cfg.coarsegrainmethod = 'filtskip';  % pointavg or filtskip
	cfg.filtmethod        = 'lp'; % low pass filter for pointskip 
	cfg.mem_available     = 16e9; % in bytes, 8e9 default
	cfg.allowgpu          = true;

These settings define the following parameters in the computation: 
- `cfg.m` is the length of the data pattern that are being counted, consisting of `m` and `m+1` patterns. `cfg.m = 2` means that 2-element patterns are counted and compared with the number of 3-element patterns.
- `cfg.r` is the pattern similarity parameter, indicating the proportion of the signal SD that is used for discretizing the data. A value of 0.5 indicates half the SD.
- `cfg.timwin` is the length of the sliding window used for selecting segments from the data.
- `cfg.toi` is a 1 x numtoi vector indicating the times on which the analysis windows (see `cfg.timwin`) should be centered (in seconds). The parameter is identical to the `cfg.toi` parameter in **[ft_freqanalysis](/reference/ft_freqanalysis)**.
- `cfg.timescales` is a 1 x numscoi vector indicating the temporal scales for which entropy will be computed. `cfg.timescales` is defined in scale numbers, in which scale 1 is the original time scale of the input data, corresponding to the sampling rate of the input data. For scale 2, the data is coarsegrained to `data.fsample`/2, for scale 3 `data.fsample`/3, etc..
- `cfg.recompute_r` indicates in which stages of the analysis the r parameter should be recomputed. `perscale_toi_sp` means the r parameter should be recomputed for each timescale, time point and starting point. 
- `cfg.coarsegrainmethod` indicates the filtering procedure used to derive coarser (i.e., longer) time scales. It can either be `filt_skip` (default) (filter, then skip points; see **[Valencia et al. (2009)](https://doi.org/10.1109/tbme.2009.2021986)**) or `pointavg` (average groups of timepoints). 
- `cfg.filtmethod` indicates the type of filter used in the 'filt_skip' method. It can either be `lp` (default), `hp`, `bp`, or `no` for no filtering.  
- `cfg.mem_available` indicates the memory available to perform computations (default 8e9 bytes). Entropy is computed in the function using 2-dimensional time-by-time matrices, which grow exponentially in size as the number of trials increases. If the matrices exceed this size, they are chunked and processed sequentially to avoid overloading memory.
- `cfg.allowgpu` 1 (default) or 0 to indicate whether to allow computations to be run on a graphical processing unit (GPU), if available on the system. This can substantially speed up the computations. The function detects automatically both the presence of a MATLAB-compatible GPU, and the optimal chunk size depending on how much memory is available on the GPU. 

After defining the cfg structure, entropy analysis is then run simply as follows:

	[mse] = ft_entropyanalysis(cfg, data);

The `mmse` output struct has the following fields:

	label: {48×1 cell}
	fsample: [1×42 double]
	timescales: [1×42 double]
	time: [1×26 double]
	dimord: 'chan_timescales_time'
	sampen: [48×42×26 double]
	r: [48×42×26 double]  
cfg: [1×1 struct]

The `mmse` struct has been designed to be structurally comparable to a `freq` structure as obtained from **[ft_freqanalysis](/reference/ft_freqanalysis)**, with the following exceptions: `timescales` replaces the `frequency` field, indicating the timescales axis. `sampen` replaces the `powspctrm` field, containing the resulting sample entropy values. `fsample` indicates the sampling rate of the data at each coarsegraining step. `r` contains the r values computed at each channel-by-timescales-by-time location.

If, after computing mMSE, you would like to use the FieldTrip functions for plotting using e.g. **[ft_multiplotTFR](/reference/ft_multiplotTFR)** and running statistics using **[ft_freqstatistics](/reference/ft_freqstatistics)**, the easiest way is to place the mMSE output into a freq structure (see **[ft_datatype_freq](/reference/ft_datatype_freq)**) so you can just plug the mMSE values into these functions.

Please contact us if you have questions (kloosterman [at] mpib-berlin.mpg.de) or if you find bugs. You can also send us a Pull Request on the Github page.

This work was contributed by Niels Kloosterman, Julian Kosciessa, Liliana Polyanska, and Douglas Garrett within the **[Lifespan Neural Dynamics Group]( https://github.com/LNDG)**.

Please cite the following papers if you find the mMSE toolbox useful:

Kloosterman NA, Kosciessa J, Lindenberger U, Fahrenfort J, Garrett DD (2019) Boosting Brain Signal Variability Underlies Liberal Shifts in Decision Bias. Biorxiv:834614. 

Kosciessa JQ, Kloosterman NA, Garrett DD (2019) Standard multiscale entropy reflects spectral power at mismatched temporal scales: What’s signal irregularity got to do with it? Biorxiv:752808. 

Grandy TH, Garrett DD, Schmiedek F, Werkle-Bergner M (2016) On the estimation of brain signal entropy from sparse neuroimaging data. Sci Rep 6:23073. 

```

