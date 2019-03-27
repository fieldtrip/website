---
title: Preprocessing and averaging of single-channel NIRS data
tags: [tutorial, nirs, preprocessing, nirs-singlechannel]
---

# Preprocessing and averaging of single-channel NIRS data

## Introduction

This tutorial demonstrates how to analyze a functional near-infrared spectroscopy (fNIRS) dataset focussing on one single channel.
The goal is to introduce the basic fNIRS analysis features of FieldTrip on Artinis NIRS data.
You can find details on the Artinis recording and analysis software [here](http://www.fieldtriptoolbox.org/getting_started/artinis).

By the end of this tutorial, you will be able to read in fNIRS data, segment it and apply different pre-processing steps. This tutorial thus also serves as a kind of general introduction into the basic fundamentals of FieldTrip.
You will also learn how to create basic visualizations of the data such as plotting single traces or topographic mapping.
Finally, in this tutorial you will compute time-locked averages from the segmented data.

This tutorial does not show how to deal with bad channels as it only operates on single channel data. You can find more information about [how to remove bad channels](/tutorial/nirs_multichannel#remove_bad_channels) and generally how to analyise multiple channels in the [Preprocessing and averaging of multi-channel NIRS data](/tutorial/nirs_multichannel) tutorial.

## Background

NIRS is an abbreviation of Near-InfraRed Spectroscopy, which is a method to measure the level of oxygenation in the blood flowing through the tissue on which the sensors are placed. It relies on the fact that oxygenated hemoglobin has a different light absorption spectrum than de-oxygenated hemoglobin and hence it has a different color so you will. Most NIRS systems emit light of 2 wavelengths, typically around 700 and 850 nm, at every source optode and some systems use three wavelengths.

The detector optode is placed a few centimeters away from the source optode. Together, the source and detector optode make up a channel, but keep in mind that the system will always have 2 spatial locations for that one channel (most of us assume the recorded activity comes from a location mainly in the middle of the source and the detector) and 2 light wavelengths. The idea is that the light is scattered through the tissue and a small portion of the light will be detectable at the surface of the tissue by means of light detectors. The intensities of the light detected at the skin fluctuate systematically with changes in the oxygenated and de-oxygenated hemoglobin concentrations present in the tissue that lies between the source and detector optode. Due to the (more or less random) scatter, most light that arrives at the detector has only traveled through the surface of the tissue and only some small portion has traveled through an area a bit deeper below the surface. Typically, it is assumed that the light detected at the skin has traveled through a tissue volume that has a banana shape when depicted from a side-view. If the source and the detector are placed further apart, the light detected can potentially have traveled deeper through the tissue. Practically, there are limitations, because the portion of light that arrives at the detector falls off dramatically with increasing source-detector separations. When measuring changes in hemoglobin in the brain, the skull functions as an important barrier, as much light is absorbed by the bone. For that reason, scanning deeper in the brain is only feasible in young infants who still have a thin skull.

The concentration of oxy- and deoxygenated hemoglobin can not be assessed in absolute terms, which means that all measures will reflect relative changes. Hence, like EEG and MEG, a baseline period is required. This can either be time-locked to the events that are provided to the participant (trial-by-trial baselines) which implies functional NIRS (fNIRS) or measured in a somewhat longer period prior or after the recording of interest (NIRS).

The recorded and later processed fNIRS signal is comparable to fMRI in that sense that a hemodynamic response function (HRF) can be obtained, but with a higher temporal resolution. It is therefore, at least in theory, possible to measure the initial dip in the curve. In contrast to fMRI, the spatial resolution however is much poorer, and typically, we mainly record from the surface of the brain. As a result, plotting will often resemble EEG. The temporal resolution of EEG is of course much higher, but, the positive side of fNIRS is that the measured signal can only stem from the region in-between the source and detector, which need not be the case in EEG due to smearing. As such, fNIRS is a promising method for measuring brain activity in populations that cannot be tested in an fMRI scanner (think of young infants or people with cochlear implants who would otherwise display larger artifacts in regions that might be of critical interest), and/or for tasks that require more movements than the scanner would allow. Do keep in mind though that blood pressure can change with your task and thereby affects the measured signal as well.

## The dataset used in this tutorial

In this dataset the motor cortex was probed using an Oxymon MK III system of Artinis Medical Systems. The system was placed over the motor cortex, and subsequently the subject was asked to perform finger tapping. Alongside the recordings from the brain, we recorded when the participant was doing what in a so-called event channel. In that channel, an 'A' was recorded at the moment the participant started with the motor task, and a 'B' was recorded whenever the participant stopped tapping. This motor task was repeated for a total of 12 times and all data was saved, including the event channel, in an .oxy3 file.

The data used in this tutorial is available from our FTP server; please download [motor_cortex.oxy3](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/nirs_singlechannel/motor_cortex.oxy3) and [optodetemplates.xml](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/nirs_singlechannel/optodetemplates.xml). For the XML file please right-click and save-as.

## Procedure

Analyses can be conducted in many different ways and in different orders, depending on the data and on the experimental design. We will first introduce you to a standard order of analysis steps, which you can subsequently try out step-by-step in this tutorial.

The following order of steps provide a good standard approach for analysing fNIRS data (see Fig 1 for an overview:

- read data & trim off non-experimental time windows
- remove bad channels (not covered in this tutorial, because we focus on one channel only)
- remove artifacts within channels; segments of data within channels that will be excluded from the analysis, e.g. motion artifacts
- transform optical densities to changes in oxyhemoglobin (oxyHb) and deoxyhemoglobin (deoxyHb) concentration
- separate functional from systemic responses (signal conditioning); this step in itself is necessary, people choose one or more of the steps below
  - filter; i.e. temporal processing
  - subtract reference channel; i.e. spatial processing
  - anti-correlate oxyHb/deoxyHb-traces per channel
- define epochs; in some experiments, this step could be taken earlier (e.g. if you have a long recording with a very short piece of relevant data)
- average over conditions and visualize the data

{% include image src="/assets/img/tutorial/nirs_singlechannel/nirs_tut1_fig1.png" width="400" %}

_Figure: Overview of fNIRS analysis procedure._

### Getting Started

The dataset that we would like to analyze is called 'motor_cortex.oxy3'. First, we need to point FieldTrip to this file. Note that FieldTrip does not feature a graphical-user interface, but instead requires you to script your way to the end goal. To let MATLAB know that we want to use FieldTrip and it's file locations, add the FieldTrip folder to your path ([without subfolders](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path)) and then execute the **[ft_defaults](/reference/ft_defaults)** function by typin

    ft_defaults

In general, FieldTrip is keeping all input arguments to a function stored together in a local variable called 'configuration' or 'cfg'. Although MATLAB variables could take any name, for convenience we will keep on using the name 'cfg' for this. FieldTrip functions are designed to each represent one step in your analysis pipeline. One (crucial) step in your analysis pipeline is to read in and preprocess the data. For this, we will make use of the FieldTrip function **[ft_preprocessing](/reference/ft_preprocessing)**. You can check out the help of the preprocessing function by typing:

    help ft_preprocessing

It might also be helpful to check out the code to obtain an understanding of what the function is about.
As FieldTrip is an open source toolbox, you can always have a look at the code details by typing

    edit ft_preprocessing

{% include markup/info %}
If this is your first time using FieldTrip you might also want to have a look at the [introduction to the toolbox and MATLAB tutorial](/tutorial/introduction).
{% include markup/end %}

### Read & trim data

For now, however, let's take a moment and read the help only and neglect the code.
So, it seems that **[ft_preprocessing](/reference/ft_preprocessing)** would like to see our filename in the variable cfg.dataset. So, let us give FieldTrip this information. Best is to open up the editor and put all lines of code in there. It is also good practice to initialize the cfg-variable each time you want to start a new step in your processing pipelin

    cfg = [];
    cfg.dataset = 'motor_cortex.oxy3';

Normally you would specify the full path, including the drive (for instance: C:\). This makes sure that your code will execute independent from your current MATLAB location. It is good practice to keep your original raw data, your processed data and your scripts in three separate locations. In this case we will work with the data in the present working directory.

Let us try to execute **[ft_preprocessing](/reference/ft_preprocessing)** now as was specified in the hel

    [data] = ft_preprocessing(cfg);

When working with .oxy3-files, the optode template containing the layout of the optodes needs to be loaded. If MATLAB cannot find the template file on your path, it will pop up a graphical user interface dialogue asking you to locate the xml file. By default this file is located in C:\Program Files (x86)\Artinis Medical Systems BV\Oxysoft 3.0.103. The file to select is “optodetemplates.xml”. However, given that FieldTrip often will search for this function, it is best to copy this function to the same folder as where your MATLAB analysis script and/or your fNIRS are data stored. For information on how to choose the optimal template for your experiments, please see https://www.artinis.com/blogpost-all/2017/6/27/how-do-i-choose-the-correct-fibers-and-template-for-my-oxymon.

FieldTrip is finished when you see something like this on the scree

    >> the call to "ft_preprocessing" took 9 seconds

{% include markup/info %}
There are more options to specify when reading in your data, such as cfg.padding, cfg.padtype and cfg.continuous. Those options have default values or are determined automatically, so we ignore them here but you can find all of them in the help documentation.

Through the option cfg.trl you can specify which trials should be read in. For now we will read in all trials, but we will make a selection later on.
{% include markup/end %}

Let us take a look at what just happened. If you observed your workspace closely, you will have noticed that a new variable was added called 'data'. This is the same name that we put just in front of **[ft_preprocessing](/reference/ft_preprocessing)**. Had you written [something], then the variable 'something' would have been added to your workspace.
If preprocessing was done as described, the data will have the following field

    data =
           hdr: [1×1 struct]
         label: {48×1 cell}
          time: {[1×4462 double]}
         trial: {[48×4462 double]}
       fsample: 5
    sampleinfo: [1 4462]
          opto: [1×1 struct]
           cfg: [1×1 struct]

Let us go through these one-by-one. The field 'hdr' contain all top-level information about your data, like for example the original sample rate, the number of channels etc. So all information that was potentially available at the time you read in the dataset. The field 'label' lists the name of all channels that you decided to read in. Note that you have told **[ft_preprocessing](/reference/ft_preprocessing)** to just read-in, by default, all channels as you haven't specified a subset. As you can see, there are 48 labels, and as the measurement consisted of 2 wavelengths per channel, this represents 24 channels. You also read in a set of ADC-channels, these will be ignored for now (these contain the triggers of the oxymon file, hence, this is NIRS acquisition hardware specific). The next field is called 'time' and represents the time axis of the dataset. The field 'trial' contains the data of all your channels. It is called 'trial' because usually, data is separated into different trials. To start off, we however have now read in all available data. The field 'fsample' describes the current sample rate of the data in the 'trial'-field. The field 'sampleinfo' describes the sample numbers of each trial with respect to the original measurement. The field 'opto' contains all high-level information about the composition of the channels and optodes, such as what wavelengths were used, the position of the optodes, what optodes formed which channels, etc. Finally, the field 'cfg' is the same cfg that we have just used, extended by some default values. This way, we can always trace back what has actually happened to our data. But more about that later.

Let us dive deeper into our data for now. For having a quick look at our data, we can use the function **[ft_databrowser](/reference/ft_databrowser)** . The databrowser is much more than a simple 'data browser', but we will utilize this functionality for our purpose at the moment. Of course, we could have a look at how to call the databrowser (help **[ft_databrowser](/reference/ft_databrowser)**), but a good guess is always to use FieldTrip functions as ft_functionname(cfg, data). We can keep the cfg empty to start with, and then see if this works. We add 'ylim = 'maxmin'' to the configuration to adjust the y-axis such that the lowest values in the graph are determining the lowest point on the y-axis, and the largest values in the graph determine the highest point on the y-axis.

    cfg = [];
    cfg.ylim = 'maxmin'
    ft_databrowser(cfg, data);

{% include image src="/assets/img/tutorial/nirs_singlechannel/nirs_tut1_fig1_ft_databrowser_readin.png" width="400" %}

_Figure: Databrowser read-in._

Using **[ft_databrowser](/reference/ft_databrowser)**, you can also cut out pieces of your data that you do not need. For instance, if you have started the recording while putting the optodes in place, you will probably have a chunk of data at the start of the recording that you don’t need and which contains very high (not brain-related) values that rapidly fluctuate. It is useful to cut these pieces out (trimming). In the tutorial dataset, this is not needed, but see here for an [illustration of how trimming works within ft_databrowser](/tutorial/visual_artifact_rejection#use_ft_databrowser_to_mark_the_artifacts_manually).

Additionally, we'll from here select just one channel, to reduce the complexity for those new to fNIRS analyses.

    cfg = [];
    cfg.ylim = 'maxmin'
    cfg.channel = {'Rx4b-Tx5 [860nm]', 'Rx4b-Tx5 [764nm]'};
    ft_databrowser(cfg, data);

{% include image src="/assets/img/tutorial/nirs_singlechannel/nirs_tut1_fig3_databrowser_one_chan.png" width="400" %}

_Figure: Databrowser with one channel selected._

#### Exercise 1

{% include markup/info %}
Take a moment to familiarize yourself with the user-interface. Change the horizontal and vertical scales until you can see the heartbeat signal in the selected channels. Tip: A time slice of something between 10 to 20 seconds is optimal. Picking up the heartbeat in the NIRS measurement is a sign of good data quality, if the heartbeat cannot be detected in the data, contact with the skin must have been poor.
{% include markup/end %}

### Remove artifacts

There are several ways to remove aspects of the data that are not of interest. That is, fNIRS data not only represents changes in oxyhemoglobin and deoxyhemoglobin concentrations, but contains, amongst others, also other physiological signals, random noise and variations stemming from the measurement environment. One prominent issue is motion artifacts, which are produced by temporary changes in the contact between optode and skin, often caused by movements of the head. Typically, one finds these motion artifacts in all channels simultaneously, but it could also be that just one channel or a few channels were affected, for instance if the participant moves the mouth. Short, unexpected peaks in the data are considered to stem from motion. You can detect and remove these artifacts for instance through \*_[ft_artifact_zvalue](/reference/ft_artifact_zvalue)_

You can specify a z-value cut-off like this:

    cfg = [];
    cfg.channel = {'Rx4b-Tx5 [860nm]', 'Rx4b-Tx5 [764nm]'};
    cfg.artfctdef.zvalue.channel = {'Rx4b-Tx5 [860nm]', 'Rx4b-Tx5 [764nm]'};
    cfg.artfctdef.zvalue.cutoff = 3.5;
    [cfg, artifact] = ft_artifact_zvalue(cfg, data);

You will see that FieldTrip identified 8 artifacts through this procedure. These are not yet removed, you would call **[ft_rejectartifact](/reference/ft_rejectartifact)**.

#### Exercise 2

{% include markup/info %}
Play around with the cut-off z-value. You can do this by running the artifact rejection in interactive mode by adding cfg.artfctdef.zvalue.interactive = 'yes'; before you run [cfg, artifact] = ft_artifact_zvalue(cfg, data);.
In the interactive mode, you can change the threshold to see which parts of the data would be rejected, the rejected bits are marked in red.

What is the optimal threshold to get rid off short lived peaks?
{% include markup/end %}

### Transform to changes in oxyHB/deoxyHB

You might have noticed that you were looking at OD values (OD stands for optical density and directly relates to the light intensity that fell on the optodes) rather than at oxygenated and deoxygenated hemoglobin concentrations, because the channel labels mention the wavelengths. We can transform our data to concentrations using **[ft_nirs_transform_ODs](/reference/ft_nirs_transform_ODs)**. One of the choices you can make when using **[ft_nirs_transform_ODs](/reference/ft_nirs_transform_ODs)** is the dpf (differential path length factor), which can differ depending on the age of the participant and the tissue type under investigation (i.e. when analysing changes in blood oxygenation in muscles

    cfg = [];
    cfg.dpf = 5.9;
    cfg.channel = {'Rx4b-Tx5 [860nm]', 'Rx4b-Tx5 [764nm]'};
    data_conc = ft_nirs_transform_ODs(cfg, data);

#### Exercise 3

{% include markup/info %}
Check out the data again! As expected, the selected channel, in which you were able to see a clear heartbeat in the raw signal, also shows a clean signal once transformed to oxy- and deoxyHb values, right?
{% include markup/end %}

### Separate functional from systemic responses

Apart from motion artifacts, which appear as spikes in the data, fNIRS measurements also contain systemic responses, which, for functional NIRS, we want to filter out of our data. There are multiple ways of extracting the functional response (the fNIRS response) out of the data, but for now, we take a simple but relatively effective approach, namely by applying a bandpass filter. A bandpass filter eliminates data above and below a user-defined threshold frequency. We will filter our data in the frequency range of most
interest for the hemodynamic response. That is activation below 0.1 Hz. Additionally we high-pass filter above 0.01 Hz to eliminate slow drifts.

    cfg = [];
    cfg.bpfilter = 'yes';
    cfg.bpfreq = [0.01 0.1];
    data_filtered = ft_preprocessing(cfg, data_conc);

### Define epochs of interest

Because we are interested to find whether the brain responds specifically to the events that took place during the experiment, we want to focus our analyses on the timewindows in which the events took place (these timewindows are often called epochs or trials). More specifically, we want to investigate whether there is increase in oxygenation in the channel of interest timelocked to the experimental event. In the current dataset, the events are fingertaps of the participant. To be able to analyze these specific event-related responses, we have not only recorded the NIRS signal, but also when which event happened, stored in a so-called trigger channel. The triggers indicate when what happened in the experiment.

Earlier, we have read in all epochs by not specifying cfg.trl during our previous call to **[ft_preprocessing](/reference/ft_preprocessing)**. In the help documentation cfg.trl points to **[ft_definetrial](/reference/ft_definetrial)**, which we will now use to define our trials. So let us have a look at the functio

    help ft_definetrial

Let us assume for now that we have no clue about the triggers in the data. We will thus now utilize a more-or-less hidden functionality to retrieve this information.

    cfg = [];
    cfg.dataset = 'motor_cortex.oxy3';
    cfg.channel = {'Rx4b-Tx5 [860nm]', 'Rx4b-Tx5 [764nm]'};
    cfg.trialdef = [];
    cfg.trialdef.eventtype = '?';

The question mark indicates that we are not sure about the event triggers, and the function **[ft_trialfun_general](/reference/ft_trialfun_general)** will thus output all events that are found in the dataset. Now, we can call **[ft_definetrial](/reference/ft_definetrial)**

    ft_definetrial(cfg);

In the command window, you will see that 24 events were found, and two types of events were used, namely event 'A' and event 'B'. In case you recorded your files with the Artinis Oxymon system, and you
did not add events during the measurement, you can include them here, see FAQ.

Furthermore, note that we do not define the output variable [cfg] now, as we are not interested in the output. The variable 'cfg' will thus stay unchanged. We want to have a look at epochs/trials starting 10 second pre-stimulus (before event ‘A’) and ending 35 seconds after ‘A’ (post-stimulus). So we can now define our trials and subsequently use this to call **[ft_preprocessing](/reference/ft_preprocessing)**:

    cfg.trialdef.eventtype  = 'event';
    cfg.trialdef.eventvalue = 'A';
    cfg.trialdef.prestim    = 10;
    cfg.trialdef.poststim   = 35;
    cfg = ft_definetrial(cfg);
    data_epoch = ft_redefinetrial(cfg,data_filtered);

Note that we left out the brackets around the output variable as we have a single output variable here. Great, we have 12 trials now! Check them out using the databrowser, but let us use some settings to make the plots look neate

    cfg = [];
    cfg.ylim = [-1 1];
    cfg.viewmode = 'vertical';
    ft_databrowser(cfg, data_epoch);

{% include image src="/assets/img/tutorial/nirs_singlechannel/nirs_tut1_fig3_ft_define_trial_v2.png" width="400" %}

_Figure: Databrowser for 12 trials._

So we pulled our data out of the measurement. The data looks crisps and clear.

#### Exercise 4

{% include markup/info %}
All signal values seem to be around the same values. Why could that be?
{% include markup/end %}

#### Exercise 5

{% include markup/info %}
You might want to perform an additional preprocessing step now. What steps do you consider useful? Check out the options in **[ft_preprocessing](/reference/ft_preprocessing)**!
{% include markup/end %}

### Timelockanalysis

We would like to compute the average of our data and have a look at the average response. We can use **[ft_timelockanalysis](/reference/ft_timelockanalysis)** for computing the average and the various available plotting function for plotting.

    cfg = [];
    data_timelock = ft_timelockanalysis(cfg, data_epoch);

The output is the data structure data_timelock with the following field

    data_timelock =
       avg: [2×225 double]
       var: [2×225 double]
      time: [1×225 double]
       dof: [2×225 double]
     label: {2×1 cell}
    dimord: 'chan_time'
      opto: [1×1 struct]
       cfg: [1×1 struct]

The most important field is data.timelock.avg, containing the average over all trials for each channel.

Below we plotted the averaged O2Hb and HHb traces from A-10 seconds to A+35 seconds. To follow fNIRS convention, O2Hb is coloured red and HHb is coloured blue.

    time = data_timelock.time;
    O2Hb = data_timelock.avg(1,:);
    HHb  = data_timelock.avg(2,:);
    figure;
    plot(time,O2Hb,'r'); hold on;
    plot(time,HHb,'b');
    legend('O2Hb','HHb'); ylabel('\DeltaHb (\muM)'); xlabel('time (s)');

{% include image src="/assets/img/tutorial/nirs_singlechannel/nirs_tut1_fig4_ft_average_hem_respons.png" width="400" %}

_Figure: Averaged O2Hb and HHb traces. This figure closely resembles the text-book fNIRS model of cortical activation, which describes an increase in oxygen demand from the tissue instigating an increase in O2Hb due to neuro-vascular coupling as depicted by Scholkmann et al. in figure 5 of their 2014 review article (http://www.sciencedirect.com/science/article/pii/S1053811913004941)._

## Summary and conclusion

We explained the pre-processing steps for a single channel in an fNIRS dataset using FieldTrip. If you would like to read further on how to pre-process an fNIRS dataset with multiple channels, you can continue with the [fNIRS multi-channel tutorial](/tutorial/nirs_multichannel). When you have more questions about the topic of any tutorial, do not forget to check the [frequently asked questions](/faq) and the [example scripts](/example).

See also the other documentation that relates to fNIRS:

{% include seealso tag1="nirs" %}
