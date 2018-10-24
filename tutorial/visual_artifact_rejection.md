---
layout: default
tags: fixme tutorial artifact meg raw preprocessing MEG-language
---


# Visual artifact rejection

## Introduction

This tutorial makes use of the preprocessed data from [Preprocessing - Trigger based trial selection](/tutorial/preprocessing). Run the script from that section in order to produce the single trial data structure, or download it from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/rejectvisual/PreprocData.mat](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/rejectvisual/PreprocData.mat). Load the data with the following command: 

    load PreprocData dataFIC

Before further analysis in any of the other tutorials, it is best to have artifact free data. Within FieldTrip you can choose to do visual/manual or automatic artifact detection and rejection. 


## Background


For a successful analysis of EEG or MEG signals, "clean" data is required. That means that you should try to reduce the amount of variance in the data due to factors that you cannot influence. One of the factors that is difficult to control are the presence of artifacts in the data. These artifact are physiological or can result from the acquisition electronics. The strongest physiological artifacts stem from eye blinks, eye movements and head movements. Muscle artifact from swallowing and neck contraction can be a problem as well. Artifacts related to the electronics are 'SQUID jumps' or spikes seen in several channels. 
To start with, it is best to avoid those artifacts during the recording. You can instruct the subject not to blink during the trial, but instead give him some well-defined time between the trials in which he is allowed to blink. But of course there will always be some artifacts in the raw data. 

While detecting artifacts by visual inspection, keep in mind that it is a subjective decision to reject certain trials and keep other trials. Which type of artifacts should be rejected depends on the analysis you would like to do on the clean data. If you would like to do a time-frequency analysis of power in the gamma band it is important to reject all trials with muscle artifacts, but for a ERF analysis it is more important to reject trials with drifts and eye artifacts. 

In visual artifact detection, the user visually inspects the data and identifies the trials or data segments and the channels that are affected and that should be removed. The visual inspection results in a list of noisy data segments and channels.

The functions that are available for visual artifact detection are

    * **[ft_rejectvisual](/reference/ft_rejectvisual)**
    * **[ft_databrowser](/reference/ft_databrowser)**

The **[ft_rejectvisual](/reference/ft_rejectvisual)** function works only for segmented data (i.e. trials) that have already been read into memory. It allows you to browse through the large amounts of data in a MATLAB figure by either showing all channels at once (per trial) or showing all trials at once (per channel) or by showing a summary of all channels and trials. Using the mouse, you can select trials and/or channels that should be removed from the data. This function directly returns the data with the noise parts removed and you don't have to call **[ft_rejectartifact](/reference/ft_rejectartifact)** or **[ft_rejectcomponent](/reference/ft_rejectcomponent)**.

The **[ft_databrowser](/reference/ft_databrowser)** function works both for continuous and segmented data and also works with the data either on disk or already read into memory. It allows you to browse through the data and to select with the mouse sections of data that contain an artifact. Those time-segments are marked. Contrary to ft_rejectvisual, the ft_databrowser function does not return the cleaned data and also does not allow you to delete bad channels (though you can switch them off from visualisation). After detecting the time-segments with the artifacts, you should call **[ft_rejectartifact](/reference/ft_rejectartifact)** to remove them from your data (when the data is already in memory) or from your trial definition (when the data is still on disk).

Noteworthy is that the **[ft_databrowser](/reference/ft_databrowser)** function can also be used to visualise the timecourse of the ICA components and thus easily allows you to identify the components corresponding to eye blinks, heart beat and line noise. Note that a proper ICA unmixing of your data requires that the atypical artifacts (e.g. electrode movement, squid jumps) are removed **prior** to calling **[ft_componentanalysis](/reference/ft_componentanalysis)**. After you have determined what the bad components are, you can call **[ft_rejectcomponent](/reference/ft_rejectcomponent)** to project the data back to the sensor level, excluding the bad components.






## Procedure

The following steps are taken to do visual artifact rejectio

   * Read the data into MATLAB using **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)**, as explained in the [previous tutorial](/tutorial/preprocessing)
   * Visual inspection of the trials and rejection of artifacts using **[ft_rejectvisual](/reference/ft_rejectvisual)** 
   * Alternatively: use **[ft_databrowser](/reference/ft_databrowser)** and mark the artifacts manually by interactively paging trial by trial



### Manual artifact rejection - display one trial at a time

The function **[ft_rejectvisual](/reference/ft_rejectvisual)** provides various ways of identifying trials contaminated with artifacts.

The configuration option cfg.method provides the possibility of browsing through the data channel by channel (cfg.method= 'channel'), trial by trial (cfg.method = 'trial') or displaying all the data at once (cfg.method = 'summary'). The field cfg.latency determines the time window of interest with respect to the trigger signals. In the example below the whole trial is inspected (i.e. cfg.latency is per default assigned to the whole trial). 

The scaling of the plots is automatically adjusted according to the maximum amplitude over all channels. The scaling can be set using cfg.alim. For EOG/EEG channels cfg.alim=5e-5 (50 micro Volt) is a useful scale and for the MEG channels cfg.alim=1e-12 (10 fT/cm).

To browse through the data trial by trial while viewing all channels writ

    cfg          = [];
    cfg.method   = 'trial';
    cfg.alim     = 1e-12; 
    dummy        = ft_rejectvisual(cfg,dataFIC);

Click through the trials using the > button to inspect each trial. 

If your dataset contains MEG and EEG channels (like this dataset), the MEG and EEG channels are scaled differently when using only cfg.alim (the EEG channels show up as big black bars on the screen). One of the reasons to record EOG, EMG or ECG is to check these channels while identifying eye, muscle and heart artifacts. The following code can be used to scale MEG and EEG channels both properl

    cfg          = [];
    cfg.method   = 'trial';
    cfg.alim     = 1e-12; 
    cfg.megscale = 1;
    cfg.eogscale = 5e-8;
    dummy        = ft_rejectvisual(cfg,dataFIC);

In trial 15 notice the slower drift observed over a larger group of sensors. This is most likely due to a head movement.

{{:tutorial:artifactdetect:untitled.jpg|}}

Trial 84 shows an artifact which is caused by the electronics. Notice the jump in sensor MLT4

{{:tutorial:artifactdetect:untitled-1.jpg?530|}}

By browsing through the trials, related artifacts become evident (trial 15, 36, 39, 42, 43, 45 ,49, 50, 81, 82 and 84). They should be marked as 'bad'. After pressing the 'quit' button the trials marked 'bad' are now removed from the data structure. 

If you would like to keep track of which trials you reject, keep in mind that the trialnumbers change when you call **[ft_rejectvisual](/reference/ft_rejectvisual)** more than once. An example: There are 87 trials in your data and first you reject trial 15, 36 and 39. Then trial number 87 becomes trial number 84. Later when you also want to reject trials 42, 43, 45 ,49, 50, 81, 82 and 84 you should be very careful and subtract 3 from all the old trial numbers. If you would like to know which trials you rejected, it is best to call rejectvisual only once.


### Manual artifact rejection - display one channel at a time


It can also be convenient to view data from one channel at a time. This can be particularly relevant for the EOG channel. To do so writ

    cfg          = [];
    cfg.method   = 'channel';
    cfg.alim     = 1e-12; 
    cfg.megscale = 1;
    cfg.eogscale = 5e-8;
    dummy        = ft_rejectvisual(cfg,dataFIC);

Click through the data using the > button.
While clicking through all the trials you see that channels MLO12 and MLP31 contain a lot of artifacts (see the figure below ). They should be marked as 'bad'. After pressing the 'quit' button the channels marked 'bad' are now removed from the data structure. 

{{:tutorial:artifactdetect:untitled-2.jpg|}}


### Manual artifact rejection - display a summary

To produce an overview of the data choose the cfg.method 'summary

    cfg          = [];
    cfg.method   = 'summary';
    cfg.alim     = 1e-12; 
    dummy        = ft_rejectvisual(cfg,dataFIC); 

This gives you a plot with the variance for each channel and trial. 

{{:tutorial:artifactdetect:channel_trialvariance.png?650|}}

You should note that there is one channel which has a very high variance. That is the EOG channel, which contains numbers in uV which are of a very different order of magnitude than all MEG channels in T. Toggling the EOG channel will also change the figure with the maximal variance per trial (second row, left) a lot. Then you only see the variance in each trial in the MEG channels.

The command window allows for toggling trials and channels on and off. The first choice could be of toggling channels off. Enter either a channel number or its name in the edit box and enter it again to toggle it back on.

Alternatively use the mouse directly to toggle (e.g.) channels off as following: drag the mouse on the top right panel, and include the rightmost dot in the selection box. In a couple of successive steps remove the 4 channels with bigger variance and press 'Quit'.

Before pressing the 'Quit' button, you can always toggle the channels/trials back on, by using the edit boxes 'Toggle trial' or 'Toggle channel'.

{{:tutorial:artifactdetect:channel_trialvariance2.png?650|}}

After quitting, the trials/channels will be rejected from the data set and the command line output appears as follow

    the input is raw data with 152 channels and 87 trials
    showing a summary of the data for all channels and trials
    computing metric [---------------------------------------------------------]
    87 trials marked as GOOD, 0 trials marked as BAD
    148 channels marked as GOOD, 4 channels marked as BAD
    no trials were removed
    the following channels were removed: MLP31, MLT33, MLT41, EOG
    the call to "ft_rejectvisual" took 20 seconds and an estimated 84 MB

This operation could be repeated for each of the metrics, by clicking on the different radio buttons 'var', 'min', 'max', etc. 

`<note>`
The summary mode in **[/reference/ft_rejectvisual](/reference/ft_rejectvisual)** has been primarily designed to visually screen for artefacts in channels of a consistent type, i.e. in this example only for the axial MEG gradiometers. 

If you have EEG data, the EOG channels have the same physical units and very similar amplitudes and therefore can be visualised simultaneously. 

If you have data from a 306-channel Neuromag system, you will have both magnetometers and planar gradiometers, which have different physical units and rather different numbers. Combining them in a single visualisation is likely to result in a biassed selection, either mainly relying on the magnetometers or the gradiometers being used to find artefacts.

You can use the following options in **[/reference/ft_rejectvisual](/reference/ft_rejectvisual)** to apply a scaling to the channels prior to visualisation: *cfg.eegscale, cfg.eogscale, cfg.ecgscale, cfg.emgscale, cfg.megscale, cfg.gradscale* and *cfg.magscale*.    

You can also call **[/reference/ft_rejectvisual](/reference/ft_rejectvisual)** multiple times, once for every type of channels in your data. If you use *cfg.keepchannel='yes'*, channels will not be removed from the data on the subsequent calls. For exampl

    cfg = [];
    cfg.method = 'summary'
    cfg.keepchannel = 'yes';
    
    cfg.channel = 'MEGMAG';
    clean1  = ft_rejectvisual(cfg, orig);
    
    cfg.channel = 'MEGGRAD';
    clean2  = ft_rejectvisual(cfg, clean1);
    
    cfg.channel = 'EEG';
    clean3  = ft_rejectvisual(cfg, clean2);
`</note>`


----

You can repeat this for the initially congruent (IC) condition. To detect all the artifacts use **[ft_rejectvisual](/reference/ft_rejectvisual)** with all 3 methods (trial, channel and summary) like in the examples above.

    clear all
    load PreprocData dataIC
   
    cfg          = [];
    cfg.method   = 'trial'; % also try cfg.method = 'channel' and cfg.method = 'summary'
    cfg.alim     = 1e-12; 
    cfg.megscale = 1;
    cfg.eogscale = 5e-8; 
    dummy        = ft_rejectvisual(cfg,dataIC);

 Trials 1, 2, 3, 4, 14, 15, 16, 17, 20, 35, 39, 40, 47, 78, 79, 80, 86 contain various artifacts, classify these as 'BAD'. Also reject the channels MLO12 and MLP31.

----
Repeat the procedure for the fully congruent condition (FC

    clear all
    load PreprocData dataFC
    
    cfg          = [];
    cfg.method   = 'trial'; % also try cfg.method = 'channel' and cfg.method = 'summary'
    cfg.alim     = 1e-12; 
    cfg.megscale = 1;
    cfg.eogscale = 5e-8; 
    dummy        = ft_rejectvisual(cfg,dataFC);

 Trials 2, 3, 4, 30, 39, 40, 41, 45, 46, 47, 51, 53, 59, 77, 85 contain various artifacts, classify these as 'BAD'. Also reject the channels MLO12 and MLP31.
### Use ft_databrowser to mark the artifacts manually

An alternative way to remove artifacts is to page through the butterfly plots of the single trials, by using the ft_databrowser function.
Call the function like


	% first select only the MEG channels
	cfg = [];
	cfg.channel = 'MEG';
	data = ft_preprocessing(cfg,dataFIC);
	% open the browser and page through the trials
	cfg=[];
	cfg.channel = 'MEG';
	artf=ft_databrowser(cfg,dataFIC);


In the image below are two figures for the same trial (trial 75). As in the left figure first drag the mouse on the artifact to create dotted lines on either side of the artifact (left image).  Then, as in the right figure click within the dotted line

{{:tutorial:fig4.png?nolink&600|}}

The resulting variable contains the fiel

artf.artfctdef.visual.artifact = [begartf endartf]

with the beginning and ending sample for all marked sections.


## Summary

Per condition, the following trials contain artifact


*  FIC: 15, 36, 39, 42, 43, 49, 50, 81, 82, 84

*  IC:  1,  2,  3,  4,  14, 15, 16, 17, 20, 35, 39, 40, 47, 78, 79, 80, 86

*  FC:  2,  3,  4,  30, 39, 40, 41, 45, 46, 47, 51, 53, 59, 77, 85 

Channels MLO12 and MLP31 are removed because of artifacts.

This tutorial was last tested with version 20120501 of FieldTrip using MATLAB 2009b on a 64-bit Linux platform.

