---
title: Time-frequency and spectral analysis
tags: [madrid2019, tutorial, eeg, brainvision, timelock, eeg-language]
---
# Frequency analysis of task and resting state EEG

## General introduction

In this tutorial you can find information about how to analyze the
spectral content in two different EEG datasets. The datasets consist
on a **[multi-sensory object categorization task](/workshop/madrid2019/eeg_language)** and a **[resting state
experiment](/workshop/madrid2019/eeg_chennu)**. The idea behind this approach is to show
the user, in a single tutorial, how to explore the spectral dimension of
the EEG activity and to adapt the analysis pipeline to the nature of each
experimental situation to get the most of the data. Before continuing with
this tutorial read through the linked descriptions of the datasets.

First of all, we'll provide a brief introduction on important concepts
about frequency analysis and how to use the relevant FieldTrip functions.
After, the tutorial will show how to analyse the task-data (object
categorization), this tutorial will show you how to compute
Time-Frequency Representations (TFR) related to specific stimuli events.
The TFRs will be computed using different techniques such as Fast-Fourier
Transform (FFT), tapers (boxcar, Hanning, and multitapers) and Wavelets.
For the resting state dataset the tutorial will show how to cut
continuous data into shorter epochs and how to perform spectral analysis
varying the window length and using different tapers. In the two datasets
it'll be shown how to visualize the results.

## A background on spectral analysis

Oscillatory components contained in the ongoing EEG or MEG signal often
show power changes relative to experimental events. These signals are not
necessarily phase-locked to the event and will not be represented in
event related fields and potentials (Tallon-Baudry and Bertrand (1999)
Oscillatory gamma activity in humans and its role in object
representation. Trends Cogn Sci. 3(4):151-162). The goal of this section
is to compute and visualize event related changes by calculating
time-frequency representations (TFRs) of power. This will be done using
analysis based on Fourier analysis and wavelets. The Fourier analysis
will include the application of multitapers (Mitra and Pesaran (1999)
Analysis of dynamic brain imaging data. Biophys J.
76(2):691-708), (Percival and Walden, 1993 Spectral analysis for physical
applications: multitaper and conventional univariate techniques.
Cambridge, UK: Cambridge UP.) which allow a better control of time and
frequency smoothing.

Calculating time-frequency representations of power is done using a
sliding time window. This can be done according to two principles: either
the time window has a fixed length independent of frequency, or the time
window decreases in length with increased frequency. For each time window
the power is calculated. Prior to calculating the power one or more
tapers are multiplied with the data. The aim of the tapers is to reduce
spectral leakage and control the frequency smoothing.

{% include image
src="/assets/img/tutorial/timefrequencyanalysis/tfrtiles.png" width="600"
%}

*Figure: Time and frequency smoothing. (a) For a fixed length time window
the time and frequency smoothing remains fixed. (b) For time windows that
decrease with frequency, the temporal smoothing decreases and the
frequency smoothing increases.*

If you want to know more about tapers/ window functions you can have a
look at this [wikipedia
site](http://en.wikipedia.org/wiki/Window_function). Note that Hann
window is another name for Hanning window used in this tutorial. There is
also a wikipedia site about multitapers, to take a look at it click
[here](http://en.wikipedia.org/wiki/Multitaper).

## Procedure

To calculate the time-frequency analysis for the example dataset we will
perform the following steps:

   * Read the data into MATLAB using
**[ft_definetrial](/reference/ft_definetrial)** and
**[ft_preprocessing](/reference/ft_preprocessing)**
   * Compute the power values for each frequency bin and each time bin
using the function **[ft_freqanalysis](/reference/ft_freqanalysis)**
   * Visualize the results. This can be done by creating time-frequency
plots for one (**[ft_singleplotTFR](/reference/ft_singleplotTFR)**) or
several channels (**[ft_multiplotTFR](/reference/ft_multiplotTFR)**), or
by creating a topographic plot for a specified time- and frequency
interval (**[ft_topoplotTFR](/reference/ft_topoplotTFR)**).

{% include image
src="/assets/img/tutorial/timefrequencyanalysis/tfr_pipelinenew.png"
width="200" %}

*Figure: Schematic overview of the steps in time-frequency analysis*

In this tutorial, procedures of 4 types of time-frequency analysis will
be shown. You can see each of them under the titles: Time-frequency
analysis I., II. ... and so on. If you are interested in a detailed
description about how to visualize the results, look at the Visualization
part.

## Part I: EEG time-frequency on task data

### Time-frequency analysis I: Hanning taper, fixed window length

Here, we will describe how to calculate time frequency representations
using Hanning tapers. When choosing for a fixed window length procedure
the frequency resolution is defined according to the length of the time
window (delta T). The frequency resolution (delta f in figure 1) =
1/length of time window in sec (delta T in figure 1). Thus a 500 ms time
window results in a 2 Hz frequency resolution (1/0.5 sec= 2 Hz) meaning
that power can be calculated for 2 Hz, 4 Hz, 6 Hz etc.  An integer number
of cycles must fit in the time window.

**[Ft_freqanalysis](/reference/ft_freqanalysis)** requires preprocessed
data (see above), which is available from the [FTP server](ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/workshop/madrid2019/tutorial_freq/data_task.mat).

        load data_task.mat

In this tutorial we will pool all stimuli belonging to the visual and
auditory categories, forming two datasets: data_visc and data_audc. In
the following example a time window with length 500 ms is applied.

        cfg              = [];
        cfg.output       = 'pow';
        cfg.channel      = 'all';
        cfg.method       = 'mtmconvol';
        cfg.taper        = 'hanning';
        cfg.foi          = 2:2:30;                         % analysis 2 to 30 Hz in steps of 2 Hz
        cfg.t_ftimwin    = ones(length(cfg.foi),1).*0.5;   % length of time window = 0.5 sec
        cfg.toi          = -1:0.05:1;                  % time window "slides" from -0.5 to 1.5 sec in steps of 0.05 sec (50 ms)
        TFRhann_visc = ft_freqanalysis(cfg, data_visc);    % visual stimuli
        TFRhann_audc = ft_freqanalysis(cfg, data_audc);    % auditory stimuli

Regardless of the method used for calculating the TFR, the output format
is identical. It is a structure with the following element

	TFRhann_visc =

	        label: {64x1 cell}                 % Channel names
	       dimord: 'chan_freq_time'            % Dimensions contained in powspctrm, channels X frequencies X time
	         freq: [2 4 6 8 10 12 14 16 18 20 22 24 26 28 30]  % Array of frequencies of interest (the elements of freq may be different from your cfg.foi input depending on your trial length)
	         time: [1x41 double]               % Array of time points considered
	    powspctrm: [64x15x41 double]           % 3-D matrix containing the power values
	          cfg: [1x1 struct]                % Settings used in computing this frequency decomposition

The element TFRhann_visc.powspctrm contains the temporal evolution of the raw
power values for each specified frequency.

#### Visualization

This part of the tutorial shows how to visualize the results of any type
of time-frequency analysis.

To visualize the event-related power changes, a normalization with
respect to a baseline interval will be performed. There are two
possibilities for normalizing: (a) subtracting, for each frequency, the
****average absolute**** power in a baseline interval from all other power values. This
gives, for each frequency, the absolute change in power with respect to
the baseline interval. (b) expressing, for each frequency, the raw power
values as the ****relative increase**** or decrease with respect to the power in
the baseline interval. This means active period/baseline. Note that the
relative baseline is expressed as a ratio; i.e. no change is represented
by 1.

There are three ways of graphically representing the data: 1)
time-frequency plots of all channels, in a quasi-topographical layout, 2)
time-frequency plot of an individual channel (or average of several
channels), 3) topographical 2-D map of the power changes in a specified
time-frequency interval.

To plot the TFRs from all the sensors use the function
**[ft_multiplotTFR](/reference/ft_multiplotTFR)**. Settings can be
adjusted in the cfg structure. For exampl

        cfg = [];
        cfg.baseline     = [-0.5 -0.3];
        cfg.baselinetype = 'absolute';
        cfg.showlabels   = 'yes';
        cfg.layout       = 'easycapM10.mat';
        figure;ft_multiplotTFR(cfg, TFRhann_visc);

{% include image
src="/assets/img/workshop/madrid2019/tutorial_freq/fig1_multiplotTFR_absolute.png"
width="600" %}

*Figure: Time-frequency representations calculated using ft_freqanalysis.
Plotting was done with ft_multiplotTFR)*

Note that by using the options cfg.baseline and cfg.baselinetype when
calling plotting functions, baseline correction can be applied to the
data. Baseline correction can also be applied directly by calling
**[ft_freqbaseline](/reference/ft_freqbaseline)**. You can combine the
various visualisation options/functions interactively to explore your
data. Currently, this is the default ploting behavior because the
configuration option cfg.interactive='yes' is activated unless you
explicitly select cfg.interactive='no' before calling
**[ft_multiplotTFR](/reference/ft_multiplotTFR)** to deactivate it. See
also the [plotting tutorial](/tutorial/plotting) for more details.

An interesting effect seems to be present in the TFR of sensor 1. To
make a plot of a single channel use the function
**[ft_singleplotTFR](/reference/ft_singleplotTFR)**

        cfg = [];
        cfg.baseline     = [-0.5 -0.3];
        cfg.baselinetype = 'absolute';
        cfg.maskstyle    = 'saturation';
        cfg.zlim         = [0 20];
        cfg.channel      = '1';
        cfg.layout       = 'easycapM10.mat';
        figure;
        subplot(211);ft_singleplotTFR(cfg, TFRhann_visc);title('visual stim');
        subplot(212);ft_singleplotTFR(cfg, TFRhann_audc);title('auditory stim');

{% include image
src="/assets/img/workshop/madrid2019/tutorial_freq/fig2_singleTFR_absolute.png"
width="600" %}

*Figure: The time-frequency representation with respect to single sensor obtained using **[ft_singleplotTFR](/reference/ft_singleplotTFR)**.*

If you see artifacts in your figure, see [this
question](/faq/i_am_getting_strange_artifacts_in_figures_that_use_opacity).

From Figure 4 one can see that there is an increase in power around 3-8
Hz in the time interval 0.1 to 0.3 s after stimulus onset. To show the
topography of the beta increase use the function
**[ft_topoplotTFR](/reference/ft_topoplotTFR)**

        cfg = [];
        cfg.baseline     = [-0.5 -0.3];
        cfg.baselinetype = 'absolute';
        cfg.xlim         = [0.1 0.3];
        cfg.zlim         = [0 10];
        cfg.ylim         = [3 8];
        cfg.marker       = 'on';
        cfg.layout       = 'easycapM10.mat';
        figure;
        subplot(211);ft_topoplotTFR(cfg, TFRhann_visc);title('visual stim');
        subplot(212);ft_topoplotTFR(cfg, TFRhann_audc);title('auditory stim');

{% include image
src="/assets/img/workshop/madrid2019/tutorial_freq/fig3_topoTFR_absolute.png"
width="300" %}

*Figure: A topographic representation of the time-frequency
representations (3 - 8 Hz, 0.1 - 0.3 s post stimulus) obtained using
ft_topoplotTFR*

##### Exercise 1

{% include markup/info %} Plot the power with respect to a relative
baseline (hint: use cfg.zlim = [-0.7 -0.7] and use the cfg.baselinetype
option)

How are the responses different? Discuss the assumptions behind choosing
a relative or absolute baseline
{% include markup/end %}

##### Exercise 2

{% include markup/info %} Plot the TFR of sensor 1. How do you
account for the increased power at ~200 ms in the visual vs auditory contidion (hint: compare to ERPs)?
{% include markup/end %}

### Time-frequency analysis II: Hanning taper, frequency dependent window length

It is also possible to calculate the TFRs with respect to a time window
that varies with frequency. Typically the time window gets shorter with
an increase in frequency. The main advantage of this approach is that the
temporal smoothing decreases with higher frequencies; however, this is on
the expense of frequency smoothing. We will here show how to perform this
analysis with a Hanning window. The approach is very similar to wavelet
analysis. A wavelet analysis performed with a Morlet wavelet mainly
differs by applying a Gaussian shaped taper.

The analysis is best done by first selecting the numbers of cycles per
time window which will be the same for all frequencies. For instance if
the number of cycles per window is 7, the time window is 1000 ms for 7 Hz
(1/7 x 7 cycles); 700 ms for 10 Hz (1/10 x 7 cycles) and 350 ms for 20 Hz
(1/20 x 7 cycles). The frequency can be chosen arbitrarily - however; too
fine a frequency resolution is just going to increase the redundancy
rather than providing new information.

Below is the cfg for a 7 cycle time window. The calculation is only done
for one sensor (1) but it can of course be extended to all sensors.

        cfg              = [];
        cfg.output       = 'pow';
        cfg.channel      = '1';
        cfg.method       = 'mtmconvol';
        cfg.taper        = 'hanning';
        cfg.foi          = 2:1:30;
        cfg.t_ftimwin    = 7./cfg.foi;  % 7 cycles per time window
        cfg.toi          = -1:0.05:1;
        TFRhann_visc7 = ft_freqanalysis(cfg, data_visc);    % visual stimuli
        TFRhann_audc7 = ft_freqanalysis(cfg, data_audc);    % auditory stimuli

To plot the result use **[ft_singleplotTFR](/reference/ft_singleplotTFR)**

        cfg              = [];
        cfg.baseline     = [-0.5 -0.3];
        cfg.baselinetype = 'absolute';
        cfg.maskstyle    = 'saturation';
        cfg.zlim         = [0 10];
        cfg.channel      = '1';
        cfg.interactive  = 'yes';
        cfg.layout       = 'easycapM10.mat';
        figure;
        subplot(211);ft_singleplotTFR(cfg, TFRhann_visc7);title('visual stim');
        subplot(212);ft_singleplotTFR(cfg, TFRhann_audc7);title('auditory stim');

{% include image
src="/assets/img/workshop/madrid2019/tutorial_freq/fig4_singleTFR7_absolute.png" width="600" %}

*Figure: A time-frequency representation of channel 1 obtained using
ft_singleplotTFR*


If you see artifacts in your figure, see [this
FAQ](/faq/i_am_getting_strange_artifacts_in_figures_that_use_opacity).

Note the boundary effects for lower frequencies (the white time frequency
points in the plot). There is no power value calculated for these time
frequency points. The power value is assigned to the middle time point in
the time window. For example for 2 Hz the time window has a length of 3.5
sec (1/2 * 7 cycles = 3.5 sec), this does not fit in the 3 sec window
that is preprocessed and therefore there is no data point here. For 5 Hz
the window has a length of 1.4 sec (1/5 * 7 cycles = 1.4 sec). We
preprocessed data between t = -1 sec and t = 2 sec so the first power
value is assigned to t= -0.3 (since -1 + (0.5 * 1.4) = -0.3). Because of
these boundary effects it is important to apply ****[ft_freqanalysis
](/reference/ft_freqanalysis )**** to a larger time window to get all the
time frequency points for your time window of interest.

If you would like to learn more about plotting of time-frequency
representations,  please see the [#Visualization](#Visualization)
section.


##### Exercise 3

{% include markup/exercise %} Adjust the length of the time-window and
thereby degree of smoothing. Use
**[ft_singleplotTFR](/reference/ft_singleplotTFR)** to show the results.
Discuss the consequences of changing these setting.

3 cycles per time window:

        cfg              = [];
        cfg.output       = 'pow';
        cfg.channel      = '1';
        cfg.method       = 'mtmconvol';
        cfg.taper        = 'hanning';
        cfg.foi          = 2:1:30;
        cfg.t_ftimwin    = 3./cfg.foi;
        cfg.toi          = -1:0.05:1;
        TFRhann_visc3 = ft_freqanalysis(cfg, data_visc);    % visual stimuli
        TFRhann_audc3 = ft_freqanalysis(cfg, data_audc);    % auditory stimuli

5 cycles per time windo

        cfg.t_ftimwin    = 5./cfg.foi;
        TFRhann_visc5 = ft_freqanalysis(cfg, data_visc);    % visual stimuli
        TFRhann_audc5 = ft_freqanalysis(cfg, data_audc);    % auditory stimuli

10 cycles per time window:

        cfg.t_ftimwin    = 10./cfg.foi;
        TFRhann_visc10 = ft_freqanalysis(cfg, data_visc);    % visual stimuli
        TFRhann_audc10 = ft_freqanalysis(cfg, data_audc);    % auditory stimuli
{% include markup/end %}

###  Time-frequency analysis III: Multitapers

Multitapers are typically used in order to achieve better control over
the frequency smoothing. More tapers for a given time window will result
in greater smoothing. High frequency smoothing has been shown to be
particularly advantageous when dealing with electrophysiological brain
signals above 30 Hz. Oscillatory gamma activity (30-100 Hz) is quite
broad band and thus analysis of such signals benefit from multitapering.
For signals lower than 30 Hz it is recommend to use only a single taper,
e.g. a Hanning taper as shown above (beware that in the example below
multitapers are used to analyze low frequencies because there are no
effects in the gamma band in this dataset).

Time-frequency analysis based on multitapers can be performed by the
function **[ft_freqanalysis](/reference/ft_freqanalysis)**. The function
uses a sliding time window for which the power is calculated for a given
frequency. Prior to calculating the power by discrete Fourier
transformations the data are "tapered". Several orthogonal tapers might
be used for each time window. The power is calculated for each tapered
data segment and then combined. In the example below we apply a time
window which gradually becomes shorter for higher frequencies (similar to
wavelet techniques). The arguments for the chosen parameters are as
follows

 -  cfg.foi , the frequencies of interest, here from 1 Hz to 30 Hz in
steps of 2 Hz. The step size could be decreased at the expense of
computation time and redundancy.
 -  cfg.toi, the time-interval of interest. This vector determines the
center times for the time windows for which the power values should be
calculated. The setting `cfg.toi = -1:0.05:1` results in power values
from -1 to 1 s in steps of 50 ms. A finer time resolution will give
redundant information and longer computation times, but a smoother
graphical output.
 -  cfg.t_ftimwin is the length of the sliding time-window in seconds (=
tw). We have chosen `cfg.t_ftimwin = 5./cfg.foi`, i.e. 5 cycles per
time-window. When choosing this parameter it is important that a full
number of cycles fit within the time-window for a given frequency.
 -  cfg.tapsmofrq determines the width of frequency smoothing in Hz (=
fw). We have chosen `cfg.tapsmofrq = cfg.foi*0.4`, i.e. the smoothing will
increase with frequency. Specifying larger values will result in more
frequency smoothing. For less smoothing you can specify smaller values,
however, the following relation (determined by the Shannon number) must
hold (see Percival and Walden, 1993

K = 2 <nowiki> * </nowiki> tw <nowiki> * </nowiki> fw-1,  where K is required to be larger than 0.

K is the number of multitapers applied; the more tapers the greater the
smoothing.

These settings result in the following characteristics as a function of
the frequencies of interes

{% include image
src="/assets/img/workshop/madrid2019/tutorial_freq/figure1ab.png"
width="600" %}

*Figure: a) The characteristics of the TFRs settings using multitapers in
terms of time and frequency resolution of the settings applied in the
example. b) Examples of the time-frequency tiles resulting from the
settings.*

        cfg = [];
        cfg.output     = 'pow';
        cfg.channel    = 'all';
        cfg.method     = 'mtmconvol';
        cfg.foi        = 1:2:30;
        cfg.t_ftimwin  = ones(length(cfg.foi),1).*0.5;
        cfg.tapsmofrq  = 4;
        cfg.toi        = -1:0.05:1;
        TFRmult_visc = ft_freqanalysis(cfg, data_visc);    % visual stimuli
        TFRmult_audc = ft_freqanalysis(cfg, data_audc);    % auditory stimuli

Plot the result

        cfg = [];
        cfg.baseline     = [-0.5 -0.3];
        cfg.baselinetype = 'absolute';
        cfg.channel      = '1';
        cfg.showlabels   = 'yes';
        cfg.layout       = 'easycapM10.mat';
        figure;
        subplot(211);ft_singleplotTFR(cfg, TFRmult_visc);
        subplot(212);ft_singleplotTFR(cfg, TFRmult_audc);

{% include image src="/assets/img/workshop/madrid2019/tutorial_freq/fig5_singleTFRmult_absolute.png" width="600" %}

*Figure: Time-frequency representations of power calculated using multitapers.*

If you would like to learn more about plotting of time-frequency
representations, please see the [visualization](#Visualization) section.

### Time-frequency analysis IV: Morlet wavelets

An alternative to calculating TFRs with the multitaper method is to use
Morlet wavelets. The approach is equivalent to calculating TFRs with time
windows that depend on frequency using a taper with a Gaussian shape. The
commands below illustrate how to do this. One crucial parameter to set is
cfg.width. It determines the width of the wavelets in number of cycles.
Making the value smaller will increase the temporal resolution at the
expense of frequency resolution and vice versa. The spectral bandwidth at
a given frequency F is equal to F/width*2 (so, at 30 Hz and a width of 7,
the spectral bandwidth is 30/7*2 = 8.6 Hz) while the wavelet duration is
equal to width/F/pi (in this case, 7/30/pi = 0.074s = 74ms)
((Tallon-Baudry and Bertrand (1999) Oscillatory gamma activity in humans
and its role in object representation. Trends Cogn Sci. 3(4):151-162)).

Calculate TFRs using Morlet wavelet

        cfg = [];
        cfg.channel    = 'all';
        cfg.method     = 'wavelet';
        cfg.width      = 7;
        cfg.output     = 'pow';
        cfg.foi        = 1:2:30;
        cfg.toi        = -1:0.05:1;
        TFRwave_visc = ft_freqanalysis(cfg, data_visc);    % visual stimuli
        TFRwave_audc = ft_freqanalysis(cfg, data_audc);    % auditory stimuli

Plot the result

        cfg = [];
        cfg.baseline     = [-0.5 -0.3];
        cfg.baselinetype = 'absolute';
        cfg.marker       = 'on';
        cfg.layout       = 'easycapM10.mat';
        cfg.channel      = '1';
        cfg.interactive  = 'no';
        figure;
        subplot(211);ft_singleplotTFR(cfg, TFRwave_visc);title('visual stim');
        subplot(212);ft_singleplotTFR(cfg, TFRwave_audc);title('auditory stim');

{% include image src="/assets/img/workshop/madrid2019/tutorial_freq/fig6_singleTFRwave_absolute.png"
width="600" %}

*Figure: Time-frequency representations of power calculated using Morlet
wavelets.*


##### Exercise 4
{% include markup/info %}
Adjust `cfg.width` and see how the TFRs change.
{% include markup/end %}

If you would like to learn more about plotting of time-frequency
representations, please see [#Visualization](#Visualization).


## Part II: Spectral analysis on EEG resting state data

In this tutorial we will be using an EEG data set from the Chennu et al.,
dataset, specifically the baseline experimental session from participant 22. At this point of the tutorial, you should know all the tricks behind
the Time-Frequency. To analyze the resting state data, we'll focus only
in the spectral domain so we'll simplify things.


    clear all, close all, clc
    load data_rest.mat

### Effect of windown length into frequency and power estimates

We loaded the dataset of participant 22 (baseline sedation session) and
we'll use **[ft_redefinetrial](/reference/ft_redefinetrial)** to cut
these trials out of the continuous data segment. Specifically, we'll cut
the very long time series into non-overlapping trials of various lengths
(1 sec, 2 secs and 4 secs) and we will compute the ***power spectrum*** of
each single trials and we'll average them.


    cfg1 = [];
    cfg1.length  = 1;
    cfg1.overlap = 0;
    base_rpt1 = ft_redefinetrial(cfg1,base);

    cfg1.length  = 2;
    base_rpt2 = ft_redefinetrial(cfg1,base);

    cfg1.length  = 4;
    base_rpt4 = ft_redefinetrial(cfg1,base);

Now we move on to using **[ft_freqanalysis](/reference/ft_freqanalysis)**
to compute our PSD using a boxcar window

    cfg2 = [];
    cfg2.output  = 'pow';
    cfg2.channel = 'all';
    cfg2.method  = 'mtmfft';
    cfg2.taper   = 'boxcar';
    cfg2.foi     = 0.5:1:45;% 1/cfg1.length  = 1;
    base_freq1  = ft_freqanalysis(cfg2, base_rpt1);
    cfg2.foi     = 0.5:0.5:45;% 1/cfg1.length  = 2;
    base_freq2  = ft_freqanalysis(cfg2, base_rpt2);
    cfg2.foi     = 0.5:0.25:45;% 1/cfg1.length  = 4;
    base_freq4  = ft_freqanalysis(cfg2, base_rpt4);

Plotting data


    figure;
    plot(base_freq1.freq,base_freq1.powspctrm(61,:));hold all;
    plot(base_freq2.freq,base_freq2.powspctrm(61,:));hold all;
    plot(base_freq4.freq,base_freq4.powspctrm(61,:));
    legend('1 sec window','2 sec window','4 sec window');
    xlabel('Frequency (Hz)');
    ylabel('absolute power (uV^2)');

{% include image src="/assets/img/workshop/madrid2019/tutorial_freq/fig7_FFT1channel.png" width="600" %}

Note the differences in amplitude and frequency resolution for each
window length. Can you explain why the amplitude of the PSD decrease
increasing the window length? Lead: think of the stationarity assumption
in FFT

### Effect of tapers into frequency and power estimates

Finally, we're going to learn what different tapers do on this resting
state dataset. To enhance the effects of the tapers, we will use the
epochs chopped in windows of 4 seconds because is the condition with the
highest frequency resolution. So let's run again **[ft_freqanalysis](/reference/ft_freqanalysis)**
but this time using different tapers: boxcar, hanning and discrete
prolate spheroidal sequences (dpss; multitapers).


    cfg2 = [];
    cfg2.output  = 'pow';
    cfg2.channel = 'all';
    cfg2.method  = 'mtmfft';
    cfg2.taper   = 'boxcar';
    cfg2.foi     = 0.5:0.25:45;
    base_freq_b = ft_freqanalysis(cfg2, base_rpt4);

    cfg2.taper   = 'hanning';
    base_freq_h = ft_freqanalysis(cfg2, base_rpt4);

    cfg2.taper   = 'dpss';
    cfg2.tapsmofrq = 4;
    base_freq_d = ft_freqanalysis(cfg2, base_rpt4);

    figure;
    plot(base_freq_b.freq,base_freq_b.powspctrm(61,:));hold all;
    plot(base_freq_h.freq,base_freq_h.powspctrm(61,:));hold all;
    plot(base_freq_d.freq,base_freq_d.powspctrm(61,:));
    legend('4 sec boxcar','4 secs hanning','4 sec dpss');
    xlabel('Frequency (Hz)');
    ylabel('absolute power (uV^2)');


{% include image src="/assets/img/workshop/madrid2019/tutorial_freq/fig8_taper1channel.png" width="600" %}

Note the differences in amplitude and frequency resolution for each
taper, specially the dpss. Can you explain why the amplitude of the PSD
decrease that much given that in this case the non-stationarity of the
data is the same across tapers?

Finally, we will apply what we just learn to study of propofol modulated
the power spectrum.

***Question***: Which set of parameters are more sensitive to detect the
spectrum shift (increase of low beta power)?


    cfg1 = [];
    cfg1.length  = 4;
    cfg1.overlap = 0;
    mild_rpt4 = ft_redefinetrial(cfg1,mild);
    mode_rpt4 = ft_redefinetrial(cfg1,mode);
    reco_rpt4 = ft_redefinetrial(cfg1,reco);

    cfg2 = [];
    cfg2.output  = 'pow';
    cfg2.channel = 'all';
    cfg2.method  = 'mtmfft';
    cfg2.taper   = 'boxcar';
    cfg2.foi     = 0.5:0.25:45;
    mild_freq_b = ft_freqanalysis(cfg2, mild_rpt4);
    mode_freq_b = ft_freqanalysis(cfg2, mode_rpt4);
    reco_freq_b = ft_freqanalysis(cfg2, reco_rpt4);

    cfg2.taper   = 'hanning';
    mild_freq_h = ft_freqanalysis(cfg2, mild_rpt4);
    mode_freq_h = ft_freqanalysis(cfg2, mode_rpt4);
    reco_freq_h = ft_freqanalysis(cfg2, reco_rpt4);

    cfg2.taper   = 'dpss';
    cfg2.tapsmofrq = 4;
    mild_freq_d = ft_freqanalysis(cfg2, mild_rpt4);
    mode_freq_d = ft_freqanalysis(cfg2, mode_rpt4);
    reco_freq_d = ft_freqanalysis(cfg2, reco_rpt4);

    figure;ft_multiplotER([],base_freq_b,mild_freq_b,mode_freq_b,reco_freq_b)
    figure;ft_multiplotER([],base_freq_h,mild_freq_h,mode_freq_h,reco_freq_h)
    figure;ft_multiplotER([],base_freq_d,mild_freq_d,mode_freq_d,reco_freq_d)
