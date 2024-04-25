---
title: Analysis of corticomuscular coherence
tags: [tutorial, coherence, meg, emg, plotting, source, connectivity, meg-visuomotor151]
---

# Analysis of corticomuscular coherence

## Introduction

In this tutorial we will analyze cortico-muscular coherence, which reflects functional connectivity between primary motor cortex and a contralateral effector muscle during isometric contraction.

The dataset used in this example has been recorded in an experiment in which the subject had to lift her hand and exert a constant force against a lever. The force was monitored by strain gauges on the lever. The subject performed two blocks of 20 trials in which either the left or the right wrist was extended for about 10 seconds. A trial started as soon as the subject managed to get his force output within a specified range from 1 to 2 N. If the force was not kept constant during the course of a trial, the trial was terminated prematurely.

The bipolar EMG signal was recorded from the right extensor carpi radialis longus muscle in the lower arm. MEG signals were recorded with a 151 sensor CTF Omega System (Port Coquitlam, Canada). In addition, the EOG was recorded to later discard trials contaminated by eye movements and blinks. The ongoing MEG and EOG signals were lowpass filtered at 300 Hz, digitized at 1200 Hz and stored for off-line analysis. To measure the head position with respect to the sensors, three coils were placed at anatomical landmarks of the head (nasion, left and right ear canal). While the subjects were seated under the MEG helmet, the positions of the coils were determined before and after the experiment by measuring the magnetic signals produced by currents passed through the coils. Magnetic resonance images (MRIs) were obtained from a 1.5 T Siemens system. During the MRI scan, ear molds containing small containers filled with vitamin E marked the same landmarks. This allows us, together with the anatomical landmarks, to align source estimates of the MEG with the MRI.

## Background

To study the oscillatory synchrony between two signals, one can compute the coherence. This is computed in the frequency domain by normalizing the magnitude of the summed cross-spectral density between two signals by their respective power. For each frequency bin the coherence value is a number between 0 and 1. The coherence values reflect the consistency of the phase difference between the two signals at a given frequency. In this session we will explore the concept of coherence by investigating a dataset from an experiment in which the subject was required to maintain an isometric contraction of a forearm muscle. The coherence between the MEG signals and the acquired EMG will be estimated. First we will explore the coherence between the EMG signal and all MEG channels. Secondly, we will investigate how the coherence estimate is influenced by the number of trials, and by the degree of spectral smoothing using multitaper spectral analysis. Even though the example in this session covers cortico-muscular coherence, coherence between sensors can be calculated in exactly the same way.

## Procedure

To compute the coherence between the MEG and EMG signals for the example dataset we will perform the following step

- Read the data into MATLAB using **[ft_preprocessing](/reference/ft_preprocessing)**
- Compute the power spectra and cross-spectral densities using the function **[ft_freqanalysis](/reference/ft_freqanalysis)** and subsequently compute the coherence using **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)**
- Visualize the results using **[ft_singleplotER](/reference/ft_singleplotER)**, **[ft_multiplotER](/reference/ft_multiplotER)**, and **[ft_topoplotER](/reference/ft_topoplotER)**
- Subsequently it is possible to localise the neuronal sources coherent with the EMG, using **[ft_sourceanalysis](/reference/ft_sourceanalysis)**

## Preprocessing

We will calculate the coherence between the MEG and the EMG when the subject extended her LEFT wrist, while keeping the right forearm muscle relaxed. The first step is to read the data. In this section we will apply automatic artifact rejection. Preprocessing requires the original [SubjectCMC.zip](https://download.fieldtriptoolbox.org/tutorial/SubjectCMC.zip) MEG dataset.

The epochs of interest have to be defined according to a custom-written function called trialfun_left.m. Note that this function is not part of the FieldTrip toolbox: see [appendix 2](/tutorial/coherence#appendix_2trialfun_left), or download it [here](https://download.fieldtriptoolbox.org/tutorial/coherence/trialfun_left.m). This function uses the information provided by the triggers which were recorded simultaneously with the data. In this experiment each trigger corresponds with the start or the end of a contraction. The epochs which correspond to a contraction of the left forearm muscle are selected. Subsequently these 10-second pieces are cut into ten 1-second epochs.

    % find the interesting epochs of data
    cfg = [];
    cfg.trialfun                  = 'trialfun_left';
    cfg.dataset                   = 'SubjectCMC.ds';
    cfg = ft_definetrial(cfg);

    % detect EOG artifacts in the MEG data
    cfg.continuous                = 'yes';
    cfg.artfctdef.eog.padding     = 0;
    cfg.artfctdef.eog.bpfilter    = 'no';
    cfg.artfctdef.eog.detrend     = 'yes';
    cfg.artfctdef.eog.hilbert     = 'no';
    cfg.artfctdef.eog.rectify     = 'yes';
    cfg.artfctdef.eog.cutoff      = 2.5;
    cfg.artfctdef.eog.interactive = 'no';
    cfg = ft_artifact_eog(cfg);

    % detect jump artifacts in the MEG data
    cfg.artfctdef.jump.interactive = 'no';
    cfg.padding                    = 5;
    cfg = ft_artifact_jump(cfg);

    % detect muscle artifacts in the MEG data
    cfg.artfctdef.muscle.cutoff      = 8;
    cfg.artfctdef.muscle.interactive = 'no';
    cfg = ft_artifact_muscle(cfg);

    % reject the epochs that contain artifacts
    cfg.artfctdef.reject          = 'complete';
    cfg = ft_rejectartifact(cfg);

    % preprocess the MEG data
    cfg.demean                    = 'yes';
    cfg.dftfilter                 = 'yes';
    cfg.channel                   = {'MEG'};
    cfg.continuous                = 'yes';
    meg = ft_preprocessing(cfg);

Next, read the left and right EMG data. Note that the settings are different for the EMG and MEG data. Most importantly, the EMG data are highpass filtered and rectified. This is a standard procedure when calculating cortico-muscle coherence.

    cfg              = [];
    cfg.dataset      = meg.cfg.dataset;
    cfg.trl          = meg.cfg.trl;
    cfg.continuous   = 'yes';
    cfg.demean       = 'yes';
    cfg.dftfilter    = 'yes';
    cfg.channel      = {'EMGlft' 'EMGrgt'};
    cfg.hpfilter     = 'yes';
    cfg.hpfreq       = 10;
    cfg.rectify      = 'yes';
    emg = ft_preprocessing(cfg);

Finally, combine the EMG and MEG trials to a common data structure:

    data = ft_appenddata([], meg, emg);

Note, that due to the artifact rejection, this procedure is very slow and we typically would want to perform this step only once. Therefore you can save the preprocessed data:

    save data data

The preprocessed data (data.mat)](https://download.fieldtriptoolbox.org/tutorial/coherence/data.mat) can also be downloaded. This allows you to skip the preprocessing above and continue loading the data like this:

    load data

To get a feel for the data, plot a trial from a sensor overlying the left motor-cortex (MRC21) and the left and right EMG-signals, by selecting the first trial from the data:

    figure
    subplot(2,1,1);
    plot(data.time{1},data.trial{1}(77,:));
    axis tight;
    legend(data.label(77));

    subplot(2,1,2);
    plot(data.time{1},data.trial{1}(152:153,:));
    axis tight;
    legend(data.label(152:153));

{% include image src="/assets/img/tutorial/coherence/figure1.png" width="400" %}

_Figure: An example of the raw MEG data from sensor MLC21 (upper frame) and the EMG data (lower frame). The signals are from the output of **[ft_preprocessing](/reference/ft_preprocessing)** and plotted using the MATLAB plot function. Note that the signal strength of the left EMG is bigger than that of the right EMG._

#### Exercise 1

{% include markup/skyblue %}
Explore the MEG and EMG in figure 1, e.g., by zooming in. How are the signals different from one another?
{% include markup/end %}

## Computing the coherence

Using **[ft_freqanalysis](/reference/ft_freqanalysis)**, the characteristics in the frequency domain will be computed. This step requires the preprocessed MEG and EMG data (see above or download [here](https://download.fieldtriptoolbox.org/tutorial/coherence/data.mat)). Load the data with:

    load data

After the computation of the frequency domain representation **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)** will be used to compute the coherence. There are essentially two ways of achieving the same coherence, and these will be explained below. The main difference is the way in which the frequency domain representation is computed. You can also check out [the different ways of representing frequency domain data](/faq/in_what_way_can_frequency_domain_data_be_represented_in_fieldtrip)

##### Method 1

In this 'method' we will use **[ft_freqanalysis](/reference/ft_freqanalysis)** for the computation of the fourier spectra, which is the 'bare' frequency domain representation of the signal, where both amplitude and phase information of the oscillations are represented in a complex number for each frequency.

First, a configuration structure (cfg) must be defined. The FFT-algorithm will be used to compute the Fourier representation of each signal. To optimize the estimation, spectral smoothing using 'multitapers' will be applied. In this context, the degree of 'smoothing' (as defined in the parameter cfg.tapsmofrq) is critical. We will return to this parameter later.

    cfg            = [];
    cfg.output     = 'fourier';
    cfg.method     = 'mtmfft';
    cfg.foilim     = [5 100];
    cfg.tapsmofrq  = 5;
    cfg.keeptrials = 'yes';
    cfg.channel    = {'MEG' 'EMGlft' 'EMGrgt'};
    freqfourier    = ft_freqanalysis(cfg, data);

##### Method 2

In this 'method' we will use **[ft_freqanalysis](/reference/ft_freqanalysis)** for the computation of the cross- and power spectra, which are mathematically constructed from the multiplication of a complex-valued fourier spectrum with the complex conjugate of another fourier spectrum. If the two fourier spectra are derived from the same channel, the cross spectrum is called the auto spectrum, and this is exactly the same as the power spectrum. Rather than in method 1 (see above), where the phase in the fourier spectra represented the _phase_ of the oscillation, the phase in the cross spectra represent the _phase difference_ between the oscillations of a specific channel pair. For this reason, we need to specify in the cfg between which pairs we want to compute the cross spectra.

    cfg            = [];
    cfg.output     = 'powandcsd';
    cfg.method     = 'mtmfft';
    cfg.foilim     = [5 100];
    cfg.tapsmofrq  = 5;
    cfg.keeptrials = 'yes';
    cfg.channel    = {'MEG' 'EMGlft' 'EMGrgt'};
    cfg.channelcmb = {'MEG' 'EMGlft'; 'MEG' 'EMGrgt'};
    freq           = ft_freqanalysis(cfg, data);

To calculate the coherence between the EMG and the MEG signals from the fourier spectra, or from the power- and cross spectra use the following function. This function does not care whether the input data contains fourier spectra, or power/cross spectra.

    cfg            = [];
    cfg.method     = 'coh';
    cfg.channelcmb = {'MEG' 'EMG'};
    fd             = ft_connectivityanalysis(cfg, freq);
    fdfourier      = ft_connectivityanalysis(cfg, freqfourier);

The field fd.cohspctrm/fdfourier.cohspctrm now contains the coherence for all MEG sensors with respect to the EMG signals.

## Displaying the coherence

Visualize the coherence between the EMG and all the MEG sensor

    cfg                  = [];
    cfg.parameter        = 'cohspctrm';
    cfg.xlim             = [5 80];
    cfg.refchannel       = 'EMGlft';
    cfg.layout           = 'CTF151_helmet.mat';
    cfg.showlabels       = 'yes';
    figure; ft_multiplotER(cfg, fd)

{% include image src="/assets/img/tutorial/coherence/figure2.png" width="400" %}

_Figure: The coherence between the left EMG and all the MEG sensors calculated using ft_freqanalysis and ft_connectivityanalysis. Plotting was done with ft_multiplotER._

Plot the coherence for sensor MRC21 (using the same settings as in **[ft_multiplotER](/reference/ft_multiplotER)**

    cfg.channel = 'MRC21';
    figure; ft_singleplotER(cfg, fd);

{% include image src="/assets/img/tutorial/coherence/figure3.png" width="400" %}

_Figure: The coherence spectrum between the EMG and sensor MRC21._

### Exercise 2

{% include markup/skyblue %}
a) What determines the frequency resolution of the spectrum, as displayed in figure 3? How can it be increased or decreased? Answer the same question for smoothing.

b) Plot a topographical distribution of the coherence in the beta band. The variable cfg.xlim defines the edges of the frequency band.

    cfg                  = [];
    cfg.parameter        = 'cohspctrm';
    cfg.xlim             = [15 20];
    cfg.zlim             = [0 0.1];
    cfg.refchannel       = 'EMGlft';
    cfg.layout           = 'CTF151_helmet.mat';
    figure; ft_topoplotER(cfg, fd)

{% include image src="/assets/img/tutorial/coherence/figure4.png" width="400" %}

_Figure: A topographic representation of the coherence between the left EMG and the sensors. The plot was created with ft_topoplotER._
{% include markup/end %}

### Exercise 3

{% include markup/skyblue %}
Explain the pattern of activation in Figure 4.

Plot the topographic representation for other frequencies that might be of interest.
{% include markup/end %}

### Exercise 4

{% include markup/skyblue %}
Explore the consequence of changing the smoothing in the frequency domain. Do this by recomputing the cortico-muscular coherence between the EMG signal and MEG sensor MRC21 for different degrees of smoothing. Compute the powerspectra and the cross-spectra, and the corresponding coherence using different degrees of smoothing.

a) 2 Hz smoothing (cfg.tapsmofrq = 2 Hz)

    cfg            = [];
    cfg.output     = 'powandcsd';
    cfg.method     = 'mtmfft';
    cfg.foilim     = [5 100];
    cfg.tapsmofrq  = 2;
    cfg.keeptrials = 'yes';
    cfg.channel    = {'MEG' 'EMGlft'};
    cfg.channelcmb = {'MEG' 'EMGlft'};
    freq2          = ft_freqanalysis(cfg,data);

    cfg            = [];
    cfg.method     = 'coh';
    cfg.channelcmb = {'MEG' 'EMG'};
    fd2            = ft_connectivityanalysis(cfg,freq2);

Plot the results of the 5 and 2Hz smoothing:

    cfg               = [];
    cfg.parameter     = 'cohspctrm';
    cfg.refchannel    = 'EMGlft';
    cfg.xlim          = [5 80];
    cfg.channel       = 'MRC21';
    figure; ft_singleplotER(cfg, fd, fd2);

b) 10 Hz smoothing (e.g., cfg.tapsmofrq = 10 Hz)

    cfg            = [];
    cfg.output     = 'powandcsd';
    cfg.method     = 'mtmfft';
    cfg.foilim     = [5 100];
    cfg.keeptrials = 'yes';
    cfg.channel    = {'MEG' 'EMGlft'};
    cfg.channelcmb = {'MEG' 'EMGlft'};
    cfg.tapsmofrq = 10;
    freq10        = ft_freqanalysis(cfg,data);

    cfg            = [];
    cfg.method     = 'coh';
    cfg.channelcmb = {'MEG' 'EMG'};
    fd10          = ft_connectivityanalysis(cfg,freq10);

Plot the results of the 5, 2, and 10 Hz smoothing

    cfg               = [];
    cfg.parameter     = 'cohspctrm';
    cfg.xlim          = [5 80];
    cfg.ylim          = [0 0.2];
    cfg.refchannel    = 'EMGlft';
    cfg.channel       = 'MRC21';
    figure; ft_singleplotER(cfg, fd, fd2, fd10);

Which degree of smoothing do you consider optimal in the calculations above?
{% include markup/end %}

### Exercise 5

{% include markup/skyblue %}
Another question pertains to how the estimate of coherence is affected by the number of trials. We will compare the cortico-muscular coherence at two MEG sensors for different amount of data.

Create the following configuration, and compute the coherence.

    cfg            = [];
    cfg.output     = 'powandcsd';
    cfg.method     = 'mtmfft';
    cfg.foilim     = [5 100];
    cfg.tapsmofrq  = 5;
    cfg.keeptrials = 'yes';
    cfg.channel    = {'MEG' 'EMGlft'};
    cfg.channelcmb = {'MEG' 'EMGlft'};
    cfg.trials     = 1:50;
    freq50         = ft_freqanalysis(cfg,data);

    cfg            = [];
    cfg.method     = 'coh';
    cfg.channelcmb = {'MEG' 'EMG'};
    fd50           = ft_connectivityanalysis(cfg,freq50);

Plot the result

    cfg                  = [];
    cfg.parameter        = 'cohspctrm';
    cfg.xlim             = [5 100];
    cfg.ylim             = [0 0.2];
    cfg.refchannel       = 'EMGlft';
    cfg.channel          = 'MRC21';
    figure; ft_singleplotER(cfg, fd, fd50);

Compare the results with figure 3. Pay special attention to the noise bias.
{% include markup/end %}

## Summary and further reading

This tutorial demonstrated how to compute one specific measure of connectivity. Using **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)** you can also compute other undirected and directed connectivity measures, such as Granger causality. This is explained in more detail in the [connectivity tutorial](/tutorial/connectivity).

FAQ
{% include seealso tag1="faq" tag2="connectivity" %}
{% include seealso tag1="faq" tag2="coherence"    %}

Example script
{% include seealso tag1="example" tag2="connectivity" %}
{% include seealso tag1="example" tag2="coherence"    %}

## Appendix 1: Localisation of neuronal sources coherent with the EMG using beamformers

In order to localise the neuronal sources which are coherent with the EMG, we can apply beamformers to the data. For a more extensive background in beamforming, in particular beamforming with frequency-domain data, please consult the beamformer tutorial. In this example, we are going to use an algorithm, known as DICS, to estimate the activity of the neuronal sources and to subsequently estimate the coherence with the EMG. In order to achieve this, we first need an estimate of the cross-spectral density between all MEG-channel combinations, and between the MEG-channels and the EMG, at a frequency of interest. This requires the preprocessed data, see above, or download [here](https://download.fieldtriptoolbox.org/tutorial/coherence/data.mat). Load with:

    load data

Compute the cross-spectral density matrix for 18 Hz

    cfg            = [];
    cfg.method     = 'mtmfft';
    cfg.output     = 'powandcsd';
    cfg.foilim     = [18 18];
    cfg.tapsmofrq  = 5;
    cfg.keeptrials = 'yes';
    cfg.channelcmb = {'MEG' 'MEG';'MEG' 'EMGlft'};
    freq           = ft_freqanalysis(cfg, data);

Once we computed this, we can use **[ft_sourceanalysis](/reference/ft_sourceanalysis)** using the following configuration. This step requires the subject's headmodel, which is included in the [SubjectCMC.zip](https://download.fieldtriptoolbox.org/tutorial/SubjectCMC.zip) dataset.

    cfg                 = [];
    cfg.method          = 'dics';
    cfg.refchan         = 'EMGlft';
    cfg.frequency       = 18;
    cfg.hdmfile         = 'SubjectCMC.hdm';
    cfg.inwardshift     = 1;
    cfg.resolution = 1;
    cfg.unit       = 'cm';
    source              = ft_sourceanalysis(cfg, freq);

The resulting source-structure is a volumetric reconstruction which is specified in head-coordinates. In order to be able to visualise the result with respect to the subject's MRI, we have to interpolate the functional data to the anatomical MRI. For this, we need the subject's MRI, which is included in the [SubjectCMC.zip](https://download.fieldtriptoolbox.org/tutorial/SubjectCMC.zip) dataset. After reading the anatomical MRI, we reslice it along the axes of the head coordinate system for improved visualization.

    mri = ft_read_mri('SubjectCMC.mri');

    cfg = [];
    mri = ft_volumereslice(cfg, mri);

Next, we can proceed with the interpolation.

    cfg            = [];
    cfg.parameter  = 'coh';
    cfg.downsample = 2;
    interp         = ft_sourceinterpolate(cfg, source, mri);

There are various ways to visualise the volumetric interpolated data. The most straightforward way is using **[ft_sourceplot](/reference/ft_sourceplot)**.

    cfg              = [];
    cfg.method       = 'ortho';
    cfg.interactive  = 'yes';
    cfg.funparameter = 'coh';
    figure; ft_sourceplot(cfg, interp);

{% include image src="/assets/img/tutorial/coherence/figure5.png" %}

_Figure: The neuronal source showing maximum coherence with the left EMG at 18 Hz. The plot was created with **[ft_sourceplot](/reference/ft_sourceplot)**._

## Appendix 2: trialfun_left

The trial function used to extract the trials:

    function trl = trialfun_left(cfg)

    % read in the triggers and create a trial-matrix
    % consisting of 1-second data segments, in which
    % left ECR-muscle is active.

    event = ft_read_event(cfg.dataset);
    trig  = [event(find(strcmp('backpanel trigger', {event.type}))).value];
    indx  = [event(find(strcmp('backpanel trigger', {event.type}))).sample];

    %left-condition
    sel = [find(trig==1028):find(trig==1029)];

    trig = trig(sel);
    indx = indx(sel);

    trl = [];
    for j = 1:length(trig)-1
    trg1 = trig(j);
    trg2 = trig(j+1);
    if trg1<=100 & trg2==2080
      trlok      = [[indx(j)+1:1200:indx(j+1)-1200]' [indx(j)+1200:1200:indx(j+1)]'];
      trlok(:,3) = [0:-1200:-1200*(size(trlok,1)-1)]';
      trl        = [trl; trlok];
    end
    end
