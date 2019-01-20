---
title: Getting started with EEG data, quality checks and ERPs
tags: [madrid2019, eeg-language]
---

# Getting started with EEG data, quality checks and ERPs

## Introduction

In FieldTrip the preprocessing of data refers to the reading of the data,
segmenting the data around interesting events such as triggers, temporal
filtering, artifact rejection and optionally rereferencing. The
**[ft_preprocessing](/reference/ft_preprocessing)** function takes care of all these steps, i.e., it reads
the data and applies the preprocessing options.

There are largely two alternative approaches for preprocessing, which
especially differ in the amount of memory required. The first approach is
to read all data from the file into memory, apply filters, and
subsequently cut the data into interesting segments. The second approach
is to first identify the interesting segments, read those segments from
the data file and apply the filters to those segments only. The remainder
of this tutorial explains the second approach, as that is the most
appropriate for large data sets such as the EEG data used in this tutorial.

Preprocessing involves several steps including identifying individual
trials from the dataset, filtering and artifact rejections. This tutorial
covers how to identify trials using the trigger signal. Defining data
segments of interest can be done according to a specified trigger channel
or according to your own criteria when you write your own trial function.

## Procedure

In this tutorial the following steps will be taken:

- Read the data into MATLAB using **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)**
- Extract bipolar EOG channels with **[ft_preprocessing](/reference/ft_preprocessing)** and get rid of reference channels with **[ft_selectdata](/reference/ft_selectdata)**. Combine EOG and data channels with **[ft_appenddata](/reference/ft_appenddata)**.
- Visual artifact rejection with **[ft_databrowser](/reference/ft_databrowser)** and **[ft_rejectvisual](/reference/ft_rejectvisual)**.
- Computing trial averages with **[ft_timelockanalysis](/reference/ft_timelockanalysis)**.
- Plotting ERPs with **[ft_topoplotER](/reference/ft_topoplotER)**

## Preprocessing

You can download the single-subject task dataset [here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/workshop/madrid2019/tutorial_erp/) from our FTP server.

### Reading trials
Let us first look at the different trigger codes present in the dataset

    cfg = [];
    cfg.dataset             = 'single_subject_task/raw/subj2.vhdr';
    cfg.trialdef.eventtype = '?';
    dummy                   = ft_definetrial(cfg);

This will display the event types and values on screen.
The trigger codes S112, S122, S132, S142 (animals) S152, S162, S172, S182 (tools) correspond to the presented visual stimuli.
The trigger codes S113, S123, S133, S143 (animals) S153, S163, S173, S183 (tools) correspond to the presented auditory stimuli.
These are the triggers we will select for now

    trigVIS = {'S112', 'S122', 'S132', 'S142', 'S152', 'S162', 'S172', 'S182'};
    trigAUD = {'S113', 'S123', 'S133','S143' , 'S153', 'S163', 'S173', 'S183'};

    cfg = [];
    cfg.dataset             = 'single_subject_task/raw/subj2.vhdr';
    cfg.trialdef.eventtype  = 'Stimulus';
    cfg.trialdef.eventvalue = [trigVIS trigAUD];
    cfg.trialdef.prestim    = 0.5;
    cfg.trialdef.poststim   = 0.8;
    cfg                     = ft_definetrial(cfg);

After the call to **[ft_definetrial](/reference/ft_definetrial)**, the configuration structure cfg now not
only stores the dataset name, but also contains a field cfg.trl with the
definition of the segments of data that will be used for further
processing and analysis. Each row in the trl-matrix represents a single
epoch-of-interest, and the trl-matrix has at least 3 columns. The first
column defines (in samples) the beginpoint of each epoch with respect to
how the data are stored in the raw datafile. The second column defines
the endpoint of each epoch, and the third column specifies the offset of
the first sample within each epoch with respect to timepoint 0 within that epoch.

We will now read in the trials defined in the cfg structure. For
preprocessing this EEG data set, the choice of the reference has to be
considered. During acquisition the reference channel of the EEG amplifier
was attached to the left mastoid. We would like to analyze this data with
a linked-mastoid reference (also known as an average-mastoid reference).

    cfg.reref       = 'yes';
    cfg.channel     = 'all';
    cfg.implicitref = 'M1';         % the implicit (non-recorded) reference channel is added to the data representation
    cfg.refchannel  = {'M1', '53'}; % the average of these channels is used as the new reference, note that channel '53' corresponds to the right mastoid (M2)

Filtering options

    cfg.lpfilter        = 'yes';
    cfg.lpfreq          = 100;
    cfg.demean          = 'yes';
    cfg.baselinewindow  = [-inf 0];
    data                = ft_preprocessing(cfg);

For consistency we will rename the channel with the name 53 located at the right mastoid to M2

    chanindx = find(strcmp(data.label, '53'));
    data.label{chanindx} = 'M2';

### Extracting EOG channel

We now continue with re-referencing to extract the bipolar EOG signal from the data.
For the vertical EOG we will use channel 50 and channel 64.
For the horizontal EOG we will compute the potential difference between
channels 51 and 60.

{% include markup/success %}
Some acquisition systems, such as Biosemi, allow for direct bipolar
recording of EOG. The re-referencing step to obtain the EOG is therefore
not required when working with Biosemi or other bipolar data.
{% include markup/end %}

{% include image src="/assets/img/tutorial/preprocessing_erp/example_eog.png" width="200" %}

EOGV channel

    cfg              = [];
    cfg.channel      = {'50' '64'};
    cfg.reref        = 'yes';
    cfg.implicitref  = []; % this is the default, we mention it here to be explicit
    cfg.refchannel   = {'50'};
    eogv             = ft_preprocessing(cfg, data);


only keep one channel, and rename to eogv

    cfg              = [];
    cfg.channel      = '64';
    eogv             = ft_selectdata(cfg, eogv);
    eogv.label       = {'eogv'};

EOGH channel

    cfg              = [];
    cfg.channel      = {'51' '60'};
    cfg.reref        = 'yes';
    cfg.implicitref  = [];
    cfg.refchannel   = {'51'};
    eogh             = ft_preprocessing(cfg, data);

only keep one channel, and rename to eogh

    cfg              = [];
    cfg.channel      = '60';
    eogh             = ft_selectdata(cfg, eogh);
    eogh.label       = {'eogh'};

We now discard these extra channels that were used as EOG from the data
and add the bipolar-referenced EOGv and EOGh channels that we have just
created.

only keep all non-EOG channels

    cfg         = [];
    cfg.channel = setdiff(1:60, [50, 51, 60, 64]);% you can use either strings or numbers as selection
    data        = ft_selectdata(cfg, data);

append the EOGH and EOGV channel to the 60 selected EEG channels

    cfg  = [];
    data = ft_appenddata(cfg, data, eogv, eogh);

FieldTrip data structures are intended to be "lightweight", in the sense
that the internal Matlab arrays can be transparently accessed. Have a look
at the data as you read it into memory

	>> data

	data =

		hdr: [1x1 struct]
	      label: {1x65 cell}
	       time: {1x400 cell}
	      trial: {1x400 cell}
 	    fsample: 500
 	 sampleinfo: [400x2 double]
  	  trialinfo: [400x1 double]
		cfg: [1x1 struct]

and note that, if you wanted to, you could plot a single trial with default Matlab function

    plot(data.time{1}, data.trial{1});

{% include image src="/assets/img/workshop/madrid2019/tutorial_erp/tsk_plottrl.png" width="800" %}

However, a better way to quickly visualize and scroll through your data
is to use **[ft_databrowser](/reference/ft_databrowser)**. There you can also easily mark artifacts.

## Visual artifacts detection

While detecting artifacts by visual inspection, keep in mind that it is a
subjective decision to reject certain trials and keep other trial. Which
type of artifacts should be rejected depends on the analysis you would
like to do on the clean data. If you would like to do a time-frequency
analysis of power in the gamma band it is important to reject all trials
with muscle artifacts, but for a ERF analysis it is more important to
reject trials with drifts and eye artifacts.

For us to get a first impression of our data quality we will use
**[ft_databrowser](/reference/ft_databrowser)** to look at our individual trials. **[Ft_databrowser](/reference/ft_databrowser)** is a
great general option if you want to quickly browse your data as it takes
both continuous and segmented data as inputs. With **[ft_databrowser](/reference/ft_databrowser)** you can
display all channels at the same time to inspect  non-systematic artifacts such as
blinks or cap movement.

    cfg = [];
    cfg.viewmode = 'vertical';
    artfct       = ft_databrowser(cfg,data)

{% include image src="/assets/img/workshop/madrid2019/tutorial_erp/tsk_databrowser.png" width="800" %}


{% include markup/info %}
Exercise 1: Skip through a couple of data segments and see if you can
already spot some artifacts. Use the buttons to mark an artifact. Are
there any bad channels in this dataset?
{% include markup/end %}

As you might have noticed it is easy to mark segments with **[ft_databrowser](/reference/ft_databrowser)**
but it is not possible to mark channels as bad and looking at each trial
individually is not always very efficient.

### Display one trial at a time

Another option for visual artifact detection is **[ft_rejectvisual](/reference/ft_rejectvisual)**. Wit this
function you can visually inspects previously segmented
data and identify the trials or the channels that are affected and that
should be removed. The visual inspection results in a list of noisy data
segments and channels. **[Ft_rejectvisual](/reference/ft_rejectvisual)** allows you to browse through the
large amounts of data in a MATLAB figure by either showing all channels
at once (per trial) or showing all trials at once (per channel) or by
showing a summary of all channels and trials, which we will do now.

We will first call **[ft_rejectvisual](/reference/ft_rejectvisual)** with all channels at once, which
corresponds more or less to using **[ft_databrowser](/reference/ft_databrowser)**, but now we can mark bad
channels and reject them from further processing.

    cfg          = [];
    cfg.method   = 'trial';
    data_clean     = ft_rejectvisual(cfg,data);

Click through the trials using the > button to inspect each trial.

{% include image src="/assets/img/workshop/madrid2019/tutorial_erp/tsk_rejecttrl.png" width="400" %}

{% include markup/info %}
Exercise 2: Can you spot which channels are noisier than others? Using
the mouse, you can select channels that should be removed from the data.
{% include markup/end %}

**[Ft_rejectvisual](/reference/ft_rejectvisual)** directly returns the data with the noise parts removed
and you don't have to call **[ft_rejectartifact](/reference/ft_rejectartifact)** or **[ft_rejectcomponent](/reference/ft_rejectcomponent)**.
We could continue working with the cleaned data, but for now we will
simply save the bad channel name and continue our data inspection.

    bad_chan = setdiff(data.label,data_clean.label);

### Display one channel at a time
Next we will call **[ft_rejectvisual](/reference/ft_rejectvisual)** to display all trials for this channel,
this is helpful in order to identify whether the channel is noisy in
general, becomes bad at a certain time during the experiment or only has
some glitches. We will also inspect the eog channels, as they will help
us identify eye blinks.

    cfg          = [];
    cfg.method   = 'channel';
    cfg.channel  = [bad_chan,'eogv','eogh'];
    data_clean   = ft_rejectvisual(cfg,data);

    blinks       = ismember(data.sampleinfo(:,1),setdiff(data. sampleinfo(:,1),data_clean.sampleinfo(:,1)));

### Display a summary
Finally we will call **[ft_rejectvisual](/reference/ft_rejectvisual)** one more time in 'summary' mode. This
option is best to identify trials or channels that are noisy overall

    cfg          = [];
    cfg.method   = 'summary';
    cfg.channel  = 'all';
    cfg.trials   = ~blinks;
    data_clean   = ft_rejectvisual(cfg,data);

{% include image src="/assets/img/workshop/madrid2019/tutorial_erp/tsk_rejectsummary.png" width="700" %}

{% include markup/info %}
Exercise 3: Which channels show the most variance and why is that?
{% include markup/end %}

{% include markup/danger %}
If you would like to keep track of which trials you reject, keep in mind
that the trialnumbers change when you call **[ft_rejectvisual](/reference/ft_rejectvisual)** more than once
or with the option cfg.trials. If you would like to know which trials you
rejected, it is best to call rejectvisual only once.
{% include markup/end %}

### Inspect cleaned data
Now that we have identified artifacts using different visual inspection
approaches, we will use **[ft_databrowser](/reference/ft_databrowser)** again to inspect the data with
bad trials marked as such For this we first compare the sample info with the
original data structure.

    bad_trl = data.sampleinfo(ismember(data.sampleinfo(:,1),setdiff(data.sampleinfo(:,1)...
    	,data_clean.sampleinfo(:,1))),:);

    cfg = [];
    cfg.viewmode = 'vertical';
    cfg.artfctdef.visual.artifact = bad_trl;
    artif = ft_databrowser(cfg,data);

In case the cleaning with **[ft_rejectvisual](/reference/ft_rejectvisual)** was not sufficient yet, you can
continue to mark trials or data segments as artifacts within
**[ft_databrowser](/reference/ft_databrowser)**. The artifact definition will be saved in the output and
you can then reject those artifacts using **[ft_rejectartifact](/reference/ft_rejectartifact)**. You will see
an example of this in the [resting-state cleaning EEG tutorial](/workshop/madrid2019/tutorial_cleaning)

## Computing and plotting the ERP's

### Channel layout
For topoplotting and sometimes for analysis it is necessary to know how
the electrodes were positioned on the scalp. In contrast to the sensor
arrangement from a given MEG manufacturer, the topographical arrangement
of the channels in EEG is not fixed. Different acquisition systems are
designed for different electrode montages, and the number and position of
electrodes can be adjusted depending on the experimental goal. In the
current experiment, so-called 64-electrodes equidistant montage (ActiCap,
BrainVision) was used.

The channel positions are not stored in the EEG dataset. You have to use
a layout file; this is a .mat file that contains the 2-D positions of the
channels. FieldTrip provides a number of default layouts for BrainVision
EEG caps in the fieldtrip/template/layout directory. It is also possible
to create custom layouts (see **[ft_prepare_layout](/reference/ft_prepare_layout)** and the [layout tutorial](/tutorial/layout)).

    cfg        = [];
    cfg.layout = 'easycapM10.mat';
    ft_layoutplot(cfg)

### Trial-average

We will now compute the ERP's for two conditions: auditory and visual stimulus presentation.
For each trial, the condition information is kept with the data structure in data.trialinfo.

use **[ft_timelockanalysis](/reference/ft_timelockanalysis)** to compute the ERPs

    cfg = [];
    cfg.trials = ismember(data_clean.trialinfo,[112, 122, 132, 142]);
    dataVIS = ft_timelockanalysis(cfg, data_clean);

    cfg = [];
    cfg.trials = ismember(data_clean.trialinfo,[113, 123, 133, 143]);
    dataAUD = ft_timelockanalysis(cfg, data_clean);

{% include markup/info %}
Exercise 4: Inspect the resulting data structure after
**[ft_timelockanalysis](/reference/ft_timelockanalysis)**. Which fields have been added and what information do
they contain?
{% include markup/end %}

We will now use **[ft_topoplotER](/reference/ft_topoplotER)** to plot both conditions at the same time.
By setting the option interactive = 'yes' you can interact with the
figure by selecting certain electrodes / time points and going back and
forth between topoplot- and time representation of the data.

    cfg = [];
    cfg.layout      = 'easycapM10.mat';
    cfg.interactive = 'yes';
    cfg.baseline    =[-0.2 0];
    ft_topoplotER(cfg, dataAUD, dataVIS)

{% include image src="/assets/img/workshop/madrid2019/tutorial_erp/tsk_topoVIS.png" width="200" %} {% include image src="/assets/img/workshop/madrid2019/tutorial_erp/tsk_topoAUD.png" width="200" %}

{% include image src="/assets/img/workshop/madrid2019/tutorial_erp/tsk_avgtime.png" width="400" %}

{% include markup/info %}
Exercise 5: Select the time window where the conditions differ the most,
do the topographies look as you would expect?
{% include markup/end %}

## Next steps

After computing your ERPs FieldTrip offers many more functions to
continue analysing your data. You can use **[ft_math](/reference/ft_math)** to compute difference
waves, **[ft_timelockstatistics](reference/ft_timelockstatistics)** to run statistics on your ERP effect, compute group
level averages with **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)**
or explore different ways of visualizing, i.e. **[ft_multiplotER](/reference/ft_multiplotER)** etc.

{% include markup/info %}
The following code allows you to look at the ERP difference waves.

    cfg = [];
    cfg.operation = 'subtract';
    cfg.parameter = 'avg';
    difference = ft_math(cfg, dataAUD, dataVIS);

note that the following appears to do the same

    difference     = dataAUD;                   % copy one of the structures
    difference.avg = dataAUD.avg - dataVIS.avg;   % compute the difference ERP

however that will not keep provenance information, whereas ft_math will
{% include markup/end %}

## See also

FAQs:
{% include seealso tag1="faq" tag3="preprocessing" %}
{% include seealso tag1="faq" tag3="timelock" %}

Examples:

{% include seealso tag1="example" tag3="preprocessing" %}
{% include seealso tag1="example" tag3="timelock" %}
