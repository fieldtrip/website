---
title: Mouse EEG - channel and source analysis
---

{% include markup/danger %}
This page is a draft tutorial that is not yet finished.
{% include markup/end %}

# Mouse EEG - channel and source analysis

## Introduction

This tutorial describes the processing of mouse EEG data. It deals with preprocessing, computing ERPs, time-frequency analysis, and visualization of channel-level data. Furtermore, it deals with reading and processing anatomical data, the coregistration with EEg electrodes, and the construction of a volume conduction model and source model. Finally, the EEG data is source reconstructed.

The method to record the mouse EEG as used in this tutorial is explained in this [video tutorial](http://www.jove.com/video/2562/high-density-eeg-recordings-freely-moving-mice-using-polyimide-based), which also points to information on optical stimulation of the mouse brain through an optical fiber. To learn how to process EEG data in more general, we suggest you check the tutorial on [Preprocessing of EEG data and computing ERPs](/tutorial/preprocessing_erp).

## Background

The purpose of the study was to use EEG combined with optogenetic stimulation (so called opto-EEG) for studying sensorimotor integration. Sensorimotor integration is a neurological process dealing with somatosensation inputs into motor outputs in an effective way. Numerous studies have shown the direct signal pathways within somatosensor-motor circuits, however little is known how the tactile sensations with different stimulation frequency are processed from somatosensory to motor cortex in order to react appropriately to different types of stimulation.

Transgenic mice were used for the study (Thy1-ChR2-EYFP, B6 mice, 12 weeks; body weight 27 g, male[http://jaxmice.jax.org/strain/007615.html](http://jaxmice.jax.org/strain/007615.html)). For implantation of electrodes on the skull and sensory thalamus (VPM; 1.82 mm posterior, 1.5 mm lateral and 3.7 mm ventral to bregma), mice were anesthetized (ketamine/xylazine cocktail, 120 and 6 mg/kg, respectively) and then positioned in a stereotaxic apparatus.

For optogenetic stimulation, we used a semiconductor laser (USA & BCL-040-445; 445 nm wavelength and 40 mW/mm2 maximum output power; CrystaLaser LLC., Reno, NV, USA) that was gated using a pulse generator (575 digital delay, Berkeley Nucleonics Corp., Berkeley, CA, USA). Blue light from the laser was guided to the brain using an optic fiber with clad/core diameters of 125 mm and 3.4 mm, respectively (P1-405A-FC-5; Thorlabs Inc., Newton, NJ, USA). The light intensity from the tip of optical fiber was approximately 2 mW/mm2 measured by integrating sphere coupled to spectrometer (BLUE-Wave-VIS2/IC2/IRRAD-CAL, Stellar-Net Inc., Tampa, FL, USA). Various pulse trains with a 20 ms pulse width were delivered in four different cortical regions (somatosensory cortices, primary motor cortex, and sensory thalamus marked as S1, S2, M1, and VPM in below figure, respectively).

{% include image src="/assets/img/tutorial/mouse_eeg/figure1.png" width="500" %}

We mimicked peripheral sensation by direct optogenetic stimulation of S1, S2, M1 and sensory thalamus and concurrently recorded the frequency dependent responses (1, 10, 20, 30, 40 and 50 Hz) with a depth electrode in the region of the optode (i.e. S1, S2, M1 and thalamus). Furthermore, we recorded EEG on the surface of the skull using a high-density micro electrode array. We allocated two electrodes in the most anterior region as the reference and ground electrodes. The signals from the brain were recorded both by high-density micro electrode array (EEG = 38 channels, plus ground and reference, so 40 electrodeds) and as the local field potential (single channel). The EEG and LFP were acquired with an analog amplifier (Synamp, Neuroscan, USA) with a sampling frequency of 2000 Hz.

### The dataset used in this tutorial

The data for this tutorial can be downloaded from our [download server](https://download.fieldtriptoolbox.org/tutorial/mouse_eeg/).

## Procedure

The procedure consists of the following steps:

- define trials
- preprocessing
- checking for artifacts
- rereferencing
- time-locked averaging
- making a channel layout, deal with animal size
- visualizing ERPs
- time-frequency analysis
- visualizing TFRs
- read the anatomical MRI data
- coregister it
- read the atlas data
- coregister it
- make segmentation of tissue inside skull
- make mesh of brain-skull boundary
- inflate segmentation using imdilate
- make mesh of skull-skin boundary
- make BEM volume conduction model
- make source model
- align electrodes with BEM model, deal with animal size
- do source reconstruction
- visualize source reconstruction
- look up source reconstruction results in atlas

## Preprocessing

### Define trials

Using **[ft_definetrial](/reference/ft_definetrial)** and **[ft_preprocessing](/reference/ft_preprocessing)** we define, read and preprocess the data segmentsof interest. Trials are specified by their begin and end sample in the data file and each trial has an offset that defines where the relative t=0 point (usually the point of the optogenetic stimulus-trigger) is for that trial.

We start with a visual inspection of the data.

    cfg = [];
    cfg.dataset = 'S1s_10Hz.cnt';
    cfg.viewmode = 'vertical';
    cfg.blocksize = 30; % show 30 seconds per page
    cfg = ft_databrowser(cfg);

The dataset used here does not include digital trigger information. To record the timing of stimulation, an analog input channel 'HL1' was used to record TTL triggers. We use a customized function and the `cfg.trialfun='mousetrialfun'` option to define the segments. The trial function results in a `cfg.trl` Nx3 array that ccontains the begin- and endsample, and the trigger offset of each trial relative to the beginning of the raw data on disk.

    function trl = mousetrialfun(cfg)

    % this function requires the following fields to be specified
    % cfg.dataset
    % cfg.trialdef.threshold
    % cfg.trialdef.prestim
    % cfg.trialdef.poststim

    hdr = ft_read_header(cfg.dataset);
    trigchan = find(strcmp(hdr.label, 'HL1'));
    trigger_data = ft_read_data(cfg.dataset, 'chanindx', trigchan); % read trigger data
    trigger_data = -trigger_data; % flip sign
    trigger_data = trigger_data - median(trigger_data); % shift

    if isfield(cfg, 'trialdef') && isfield(cfg.trialdef, 'threshold')
      trigger_threshold = cfg.trialdef.threshold;
    else
      trigger_threshold = 0.5*max(trigger_data);
    end

    % give some feedback
    figure
    plot(trigger_data, 'b')
    hold on
    plot(trigger_threshold*ones(size(trigger_data)), 'g')

    stim_duration = cfg.trialdef.prestim  * hdr.Fs; % number of samples
    rest_duration = cfg.trialdef.poststim * hdr.Fs; % number of samples

    % extracts, trigger timing ------------------------------------------------
    data1 = find(abs(trigger_data) > trigger_threshold);      % exceed threshold
    data2 = find(data1-[0,data1(1,1:end-1)] > rest_duration); % exceed 'rest_duration'
    idx = data1(data2);
    clear data1 data2

    trigger_event(1,:) = idx;
    clear idx

    % give some additional feedback
    plot(trigger_event(1,:), trigger_threshold, 'rx')

    % extracts, trigger contents ----------------------------------------------
    for tr = 1:size(trigger_event,2)
      temp_data = abs(trigger_data(trigger_event(1,tr):trigger_event(1,tr)+stim_duration-1));
      idx = find_cross(temp_data, trigger_threshold, 'down'); clear temp_data
      trigger_event(2,tr) = size(find(idx == 1),2) / (stim_duration / hdr.Fs);
    end

    trl       = [trigger_event(1, :) - stim_duration+1; trigger_event(1, :) + rest_duration]';
    trl(:, 3) = zeros(size(trl, 1), 1);

    function idx = find_cross(data, thr, type)
    % find peaks.
    % data = 1 by n vector.
    % thr = the crossing point.
    % type = 'both', 'up', 'down'.
    % default type: 'both'.

    if size(data,1) > 1
      data = data.';
      if size(data,2) > 1
        error('data must be vector form')
      end
    end

    % up crossing
    tidx1 = zeros(1,size(data,2)-1);
    tidx2 = zeros(1,size(data,2)-1);
    idx1 = zeros(1,size(data,2)-1);
    tidx1(data(1,1:end-1) <= thr) = 1;
    tidx2(data(1,2:end) > thr) = 1;
    idx1(tidx1 + tidx2 == 2) = 1; clear tidx1 tidx2

    % down crossing
    tidx1 = zeros(1,size(data,2)-1);
    tidx2 = zeros(1,size(data,2)-1);
    idx2 = zeros(1,size(data,2)-1);
    tidx1(data(1,1:end-1) >= thr) = 1;
    tidx2(data(1,2:end) < thr) = 1;
    idx2(tidx1 + tidx2 == 2) = 1; clear tidx1 tidx2

    % both
    idx0 = zeros(1,size(data,2)-1);
    idx0(idx1 + idx2 > 0) = 1;

    if nargin == 2
      idx = idx0;
    elseif nargin == 3
      if strcmpi(type,'both')
        idx = idx0;
      elseif strcmpi(type,'up')
        idx = idx1;
      elseif strcmpi(type,'down')
        idx = idx2;
      end
    end

Using this trial function, we can call **[ft_definetrial](/reference/ft_definetrial)** to find the trials or segments of interest.

    cfg = [];
    cfg.dataset  = 'S1s_10Hz.cnt';
    cfg.trialfun = 'mousetrialfun'; % see above
    cfg.trialdef.threshold = 2e6;
    cfg.trialdef.prestim    = 1; % in seconds
    cfg.trialdef.poststim   = 2; % in seconds
    cfg = ft_definetrial(cfg);

You will see that the trial function produces a figure, which can be used to check whether the threshold was at the appropriate level and whether the stimulation onsets are properly detected.

FIXME insert figure (1 data loading)

The segments of interest are specified by their begin- and endsample and by the offset that specifies the timing relative to the data segment. The offset is 2000, indicating that sample 2000 in every trial is considered as time t=0.

    >> cfg.trl

    ans =
        7447       13446       -2000
       17447       23446       -2000
       27447       33446       -2000
       37447       43446       -2000
       47447       53446       -2000
       57447       63446       -2000
       67447       73446       -2000
       ...

### Reading and filtering

After the segments of interest have been specified as `cfg.trl`, we read them from disk into memory. At this step we also specify other preprocessing options such as the filter settings.

    cfg.channel   = 'all';
    cfg.baseline  = [-0.30, -0.05];
    cfg.demean    = 'yes';
    cfg.bsfilter  = 'yes';
    cfg.bsfreq    = [59 61]
    cfg.lpfilter  = 'yes';
    cfg.lpfreq    = 100;
    data          = ft_preprocessing(cfg);

The output of ft_preprocessing is a structure which has the following fields:

    data =
               hdr: [1x1 struct]
             label: {39x1 cell}
              time: {1x88 cell}
             trial: {1x88 cell}
           fsample: 2000
        sampleinfo: [88x2 double]
               cfg: [1x1 struct]

In `data.sampleinfo` you can find the begin and endsample of each trial: these are copied over from the 1st and 2nd column of `cfg.trl`. The offset in the 3rd column has been used to make an individual time axis `data.time` for each trial.

We can plot all channels for a single trial using standard MATLAB code:

    figure
    plot(data.time{1}, data.trial{1});
    legend(data.label);
    grid on

FIXME insert figure (2 single trial plot )

### Checking for artifacts

Using **[ft_databrowser](/reference/ft_databrowser)** we can do a quick visual inspection of the data in each trials and check for artefacts.

    cfg = [];
    cfg.viewmode = 'butterfly';
    cfg = ft_databrowser(cfg, data);

FIXME insert figure (3 datatrial browser)

The 41th channel with label 'HL1' contains the analog TTL trigger, which is of much larger amplitude than all other channels. We can exclude it in the GUI by clicking the "channel" button and removing it or by using the following code:

    cfg = [];
    cfg.viewmode = 'vertical';
    cfg.channel = {'all', '-HL1'};
    cfg = ft_databrowser(cfg, data);

Some channels show a much lower noise level than others (e.g., AF8). This might be due to differences in the electrode-skull impedance.

FIXME insert figure (4 check the impedance and report it here)

### Rereferencing

During acquisition the two most frontal electrodes in the grid were used as the ground and reference. These two electrodes are placed just anterior of the Fp1 and the Fp2 electrode. We rereference the data to a common average over all electrodes.

    cfg            = [];
    cfg.reref      = 'yes';
    cfg.channel    = {'all', '-VPM', '-Sync', '-HL1'};  % we don't want to re-reference these
    cfg.refchannel = {'FP1';'FP2';...
                      'AF3';'AF4';'AF7';'AF8';...
                      'F1';'F2';'F5';'F6';...
                      'FC1';'FC2';'FC5';'FC6';...
                      'C1';'C2';'C3';'C4';'C5';'C6';...
                      'CP1';'CP2';'CP3';'CP4';'CP5';'CP6';...
                      'P1';'P2';'P3';'P4';'P5';'P6';...
                      'PO3';'PO4';'PO7';'PO8';...
                      'O1';'O2'};
    data_reref = ft_preprocessing(cfg, data);

We have now lost the LFP, since that should not be rereferenced to the common average reference. We can get it back from the original data and append it to the rereferenced EEG data.

    cfg = [];
    cfg.channel = 'VPM';
    data_vmp = ft_selectdata(cfg, data);

    cfg = [];
    data_reref = ft_appenddata(cfg, data_reref, data_vmp);

You can compare the original and re-referenced data using ft_databrowser.
 
    cfg            = [];
    cfg.viewmode   = 'vertical';
    cfg            = ft_databrowser(cfg, data_reref);

FIXME insert figure (5 datatrial browser)

### Making a channel layout for plotting

For 2D plotting of the channel data, FieldTrip makes use of so-called [layouts](/tutorial/layout). These layouts specify the location and size of each channel, and can include an outline (for example of the mouse head) and a mask to restrict the topographic interpolation for topoplots.

To make a customized layout for the EEG array we start with a figure that indicates the electrode arrangement. This example photo is taken from Lee et al. (2011) Journal of Visualized Experiments ([video](http://www.jove.com/video/2562/high-density-eeg-recordings-freely-moving-mice-using-polyimide-based), [pdf](http://www.jove.com/pdf/2562/jove-protocol-2562-high-density-eeg-recordings-freely-moving-mice-using-polyimide-based).

{% include image src="/assets/img/tutorial/mouse_eeg/figure2.png" width="400" %}

You can specify `cfg.image` in **[ft_prepare_layout](/reference/ft_prepare_layout)** and subsequently click on the location of each electrode. After specifying each electrode location, you'll be asked to specify the outlines of the head (i.e. the circle around the head, the eyes, the nose and ears (dash lines) and optionally some lines representing other important landmarks: bold lines, bregma, and lambda) and to specify the mask for the topographic interpolation (green dash line).

Find the bregma and lambda points on the skull, and record them with the stereotaxic ruler. The bregma and lambda points are located in the same anterio-posterior axis.

The anterio-posterior axis of high-density electrode array (HD-array) matches the line between bregma and lambda points. The bregma point (0, 0) should be located at the middle of the 4th layer of the anterior of HD-array because we follow the Paxinos coordinate system. We implemented a mouse layout on fixed length (4.2 mm) between bregma and lambda.

    cfg         = [];
    cfg.image   = 'mouse_skull_with_HDEEG.png';
    layout      = ft_prepare_layout(cfg);

After creating the layout, you should manually assign the correct name of the channel labels in the `layout.label` cell-array. The channel order in `layout.label` should correspond to the sequence in which you clicked the electrodes. You can use **[ft_plot_layout](/reference/plotting/ft_plot_layout)** for a visual inspection of the layout. You will see that a placeholder have been added for the comment and the scale.

FIXME insert figure (6 layout plot)

If you think that some outlines (nose, eyes, head, whiskers and ears) are not necessary, you can pass without assigning any outline. Next step is zero point calibration for the bregma point. If you, however, use customized layout for single subject, you don't need to carry out next step.

Coinsidering the mouse anatomy, the bregma point is located in the middle of the 4th layer of the anterior of the EEG array that it should be set (0, 0) because we follow the Paxinos coordinate system. To calibrate layout position, we just subtract the value of bregma on the layout that we constructed in the previous step.

    bregma = [382, 280];
    layout.pos = layout.pos - repmat(bregma, size(layout.pos, 1), 1);
    for i=1:numel(layout.outline)
      layout.outline{i} = layout.outline{i} - repmat(bregma, size(layout.outline{1, i}, 1), 1);
    end
    for i=1:numel(layout.mask)
      layout.mask{i} = layout.mask{i} - repmat(bregma, size(layout.mask{1, i}, 1), 1);
    end

We plot it to confirm the calibration.

    figure
    ft_plot_layout(layout)
    axis on
    grid on

FIXME insert figure (7 layout plot)

If you are satisfied with the result, you should save it to a MATLAB file. However, in the case of this specific tutorial you probably don't want to overwrite the mat file that you have downloaded, but rather want to read that from disk and inspect it with **[ft_plot_layout](/reference/plotting/ft_plot_layout)**.

    if false
      save mouse_layout.mat layout
    else
      load mouse_layout.mat
    end

### Deal with differences in animal size

The polyimide film from which the high-density EEG array is made is not strechable. Each mouse, however, has a different head size depending on its strain, age, weight and sex. To deal with the different sizes, we use the distance between bregma and lambda and a reference scale of 4.2 mm. If you have a smaller mouse, and consequently a relatively wider spaced EEG array for that specific mouse, you can scale the layout to accommodate this. The approach here to deal with differences in the mouse brain size is very comparable to the one adopted in the Talairach-Tournoux anatomical atlas of the human brain.

For example for a mouse with a bregma-lambda distance of 3.8, you can do the following.

    layout42 = layout; % this is the reference
    layout38 = layout; % make a copy, this will be updated

    ratio = 4.2/3.8; % the electrodes span a relatively larger part of the head on the smaller-sized animal

    layout38.pos = layout42.pos * ratio;
    for i=1:numel(layout38.outline)
      layout38.outline{i} = layout42.outline{i} * ratio;
    end
    for i=1:numel(layout38.mask)
      layout38.mask{i} = layout42.mask{i} * ratio;
    end

Again, to confirm your calibration:

    figure
    ft_plot_layout(layout38)
    axis on
    grid on

{% include image src="/assets/img/tutorial/mouse_eeg/figure3.png" width="400" %}

For the human EEG it is convenient to make use of a single [template](/template/layout) for the channel positions. Human EEG caps come in different sizes, for example ranging from 52 to 60 cm head circumference in 2cm steps, and those caps also are slightly strechable. The range of human EEG caps can therefore accommodate approximately a 15% difference in head circumference. For the mouse, the electrode grids are however fixed, whereas the head sizes still differ.

For example, let's think about a case of targetting CA1 hippocampus which is (AP, ML, DV) = (-2, 1.5, -2) with respect to the bregma according to the mouse atlas. Each individual mouse has different brain size. What we do is to measure the length between bregma to lambda, and if the length is 3.9 mm, we multiply the target distance by `4.2/3.9 = 1.077`. Hence the stereotaxic target for CA1 would be (AP, ML, DV) = (-2.15, 1.62, -2.15). Since the accuracy of the stereotaxic is 0.1 mm, the actual target becomes be (-2.1, 1.6, -2.1).

Note that some mouse research groups rescale only anterior posterior (AP) and according to them the target coordinate would be -2.1, 1.5, -2.

In the mouse we can use histology as a a secondary confirmation procedure after recordings. The anatomical structure of mouse brain due not vary dramatically if the weight and/or the length between bregma and lambda are in the similar range, in a sense of a few hundreds micrometer. For example, any structure with a dimension ranging larger than a couple of hundreds micrometer, we seldom fail to hit this structure. However, when we aim for a structure with a sharp shape with dimension smaller than a couple of hundreds micrometer, we half fail to hit that structure. But if this structure is on the cortex or near, we seldom fail.

## Channel level analysis - ERPs

The ERP time-locked to stimulus onset is computed by averaging the data over all trials.

    cfg = [];
    timelock = ft_timelockanalysis(cfg, data_reref);

We can again plot it with a standard MATLAB command.

    figure
    plot(timelock.time, timelock.avg);
    legend(timelock.label);

FIXME insert figure (8 timelock plot)

Looking at the figure legend, you can see that channel VPM shows a particularly large response to the stimulation. This makes sense, as it corresponds to the depth electrode that is inserted along with the optode, i.e. it records from the stimulated site.

Rather than plotting all ERPs on top of each other, we can also plot them according to the channel layout. For that we use the function **[ft_multiplotER](/reference/ft_multiplotER)**.

    cfg             = [];
    cfg.layout      = 'mouse_layout.mat';  % from file
    cfg.showoutline = 'yes';
    cfg.interactive = 'no';  % or 'yes'
    ft_multiplotER(cfg, timelock);

FIXME insert figure (9 timelock plot)

When you specify `cfg.interactive = 'no'` you can use the MATLAB zoom buttons. With `cfg.interactive = 'yes'` the zoom buttonsd don't work properly, but you can make a selection of channels and click in the selection, which causes them to be averaged and displayed in a single plot. In the single plot, you can again make a selection of time, which is subsequently averaged (for all channels) and shown as the interpolated topographic distribution of the potential.

FIXME insert figure (singleplot)

FIXME insert figure (topoplot)

## Channel level analysis - TFRs

This section describes how to calculate time-frequency representations using Hanning window.

    % power spectrogram
    cfg                   = [];
    cfg.output            = 'pow';
    cfg.method            = 'mtmconvol';
    cfg.taper             = 'hanning';
    cfg.foi               = 4:4:100;                         % frequencies of interest
    cfg.t_ftimwin         = ones(length(cfg.foi),1)*0.250;   % 250 ms window
    cfg.toi               = -1:0.01:3.0;                     % from -1 to 3 seconds in steps of 0.01
    freq                  = ft_freqanalysis(cfg, data_reref);

The output of **[ft_freqanalysis](/reference/ft_freqanalysis)** is a structure which has the following fields:

    freq =
        powspctrm: [39x25x401 double]
           dimord: 'chan_freq_time'
            label: {39x1 cell}
             freq: [4 8 12 16 20 24 ... 96 100]
             time: [-1 -0.9900 -0.9800 -0.9700 ... 2.9900 3.0000]
              cfg: [1x1 struct]

The field `freq.powspctrm` contains the power for each of the 39 channels, for each of the 401 timepoints, and for each of the 25 frequencies (from 4 to 100 in 4Hz steps).

The results of the time-frequency analysis can be plotted with **[ft_multiplotTFR](/reference/ft_multiplotTFR)** and **[ft_singleplotTFR](/reference/ft_singleplotTFR)**. To visualize the power changes due to stimulation and to compare the power over frequencies, we perform a normalization with respect to the baseline. By specifying `cfg.baselinetype = 'relchange'` we compute the relative change, which is the power minus the average power in the baseline, divided the average power in the baseline.

    % visualization of all EEG channels
    cfg                   = [] ;
    cfg.xlim              = [-1 2];
    cfg.ylim              = [4 100];
    cfg.zlim              = [-1.0 1.0];
    cfg.colorbar          = 'yes';
    cfg.layout            = 'mouse_layout.mat'; % see above
    cfg.showoutline       = 'yes';
    cfg.baseline          = [-0.5 0];
    cfg.baselinetype      = 'relchange' ;
    ft_multiplotTFR(cfg, freq);

FIXME insert figure (10 ft_multiplotTFR)
FIXME insert figure (11 ft_topoplotTFR)

Again with `cfg.interactive = 'yes'`, which is the default, you can select one or multiple channels, click on them and get an average TFR over those channels,. In that average you can make a time and frequency selection, click in it, and get a spatial topopgraphy of the relative power over all channels in that fime-frequency range.

If you did not construct a layout, you can visualize the TFRs sequentially over all channels. An advantage of this is that in contrast to the previous figure, channel VMP is now also plotted. There is no location for that channel in the layout contained in the `mouse_layout.mat` file.

    % visualization of all EEG channels, not topographically arranged
    cfg                   = [] ;
    cfg.xlim              = [-1 2];
    cfg.ylim              = [4 100];
    cfg.zlim              = [-1.0 1.0];
    cfg.colorbar          = 'yes';
    cfg.layout            = 'ordered'; % see FT_PREPARE_LAYOUT
    cfg.showlabels        = 'yes';
    cfg.baseline          = [-0.5 0];
    cfg.baselinetype      = 'relchange' ;
    ft_multiplotTFR(cfg, freq);

FIXME insert figure (12 ft_multiplotTFR with ordered)

You can also explicitly visualize a TFR  for a specific channel.

    % single channel visualization
    cfg                   = [] ;
    cfg.channel           = 'VMP'; % you can also specify multiple, it will then average
    cfg.xlim              = [-1 2];
    cfg.ylim              = [4 100];
    cfg.zlim              = [-1.0 1.0];
    cfg.colorbar          = 'yes';
    cfg.baseline          = [-0.2 0];
    cfg.baselinetype      = 'relchange' ;
    ft_singleplotTFR(cfg, freq);
    xlabel('time (s)')
    ylabel('frequency (Hz)')

FIXME insert figure (13 ft_singleplotTFR with order)

## Anatomical processing and construction of the volume conduction model

### Reading and coregistring the anatomical data

The anatomical MRI is originally obtained from <http://brainatlas.mbi.ufl.edu>, but is also available from our [download server](https://download.fieldtriptoolbox.org/tutorial/mouse_eeg/).

    mri = ft_read_mri('Num1_MinDef_M_Normal_age12_num10.hdr')

    figure
    ft_determine_coordsys(mri, 'interactive', 'no')

FIXME insert figure (13 ft_determine_coordsys)

This gives a figure that shows the origin as a white sphere, the x-axis in red, the y-axis in green and the z-axis in blue (remember RGB). We notice that the origin is not at Bregma, nor at the interaural point. This is inconsistent with the desired [coordinate system](/faq/coordsys#details_on_the_paxinos-franklin_mouse_coordinate_system), hence we have to realign the anatomical MRI.

#### Coregistration using high-level graphical function

We can use the **[ft_volumerealign](/reference/ft_volumerealign)** function to coregister the anatomical MRI to the desired coordinate system. There are multiple coordinate systems in which the anatomy of the brain and head can be described, but here we want to use the Paxinos-Franklin cordite system which uses Bregma and Lambda as anatomical landmarks (or fiducials).

    cfg = [];
    cfg.coordsys  = 'paxinos';
    mri_realigned = ft_volumerealign(cfg, mri);

FIXME insert figure (14 ft_volumerealign)

The anatomical MRI is displayed in three orthogonal plots. You have to visually identify the anatomical landmark location and press "b" for bregma, "l" for lambda and "z" for a midsagittal point. Using "f" you can toggle the landmarks or fiducials on and off. Once you are happy with their placement, you press "q" and the realigned mri is returned:

    mri_realigned =
                  dim: [256 256 512]
              anatomy: [256x256x512 double]
                  hdr: [1x1 struct]
            transform: [4x4 double]
                 unit: 'cm'
                  cfg: [1x1 struct]
        transformorig: [4x4 double]
             coordsys: 'paxinos'

We can check the coordinate axes once more with

    figure
    ft_determine_coordsys(mri_realigned, 'interactive', 'no')

FIXME insert figure (15 ft_determine_coordsys)

### Manual coregistration using low-level functions

Using

    cfg = [];
    ft_sourceplot(cfg, mri)

and by clicking in the figure, we can determine the location of three landmarks, expressed in the coordinate system and the units of the original anatomical MRI

    bregma      = [0 -5.0 2.5];
    lambda      = [0 -5.0 2.0];
    midsagittal = [0.2 -0.7 -2.0];

The **[ft_headcoordinates](/reference/utilities/ft_headcoordinates)** function provides the homogenous transformation matrix to rotate and translate the MRI into the Paxinos coordinate system.

    head2paxinos = ft_headcoordinates(bregma, lambda, midsagittal, 'paxinos')

    head2paxinos =

        0.9994    0.0225    0.0256   -0.0009
        0.0225   -0.9997    0.0006   -4.4011
        0.0256   -0.0000   -0.9997    3.8987
             0         0         0    1.0000

We can apply this [homogenous transformation matrix](/faq/homogenous) to the MRI with

    vox2head    = mri.transform;
    vox2paxinos = head2paxinos * vox2head;

    mri_realigned           = mri;         % copy the original MRI
    mri_realigned.transform = vox2paxinos; % update the homogenous transformation matrix

It is useful to also explicitly specify the coordinate system in the anatomical MRI. It is used in **[ft_sourceplot](/reference/ft_sourceplot)** and various other functions to check whether various geometrical objects are expressed in the same coordinate system.

    mri_realigned.coordsys = 'paxinos';

#### Correcting the units of the anatomical MRI

Finally, we notice that the units are off by a factor 10x. Upon reading FieldTrip estimates the geometrical units and it expects that the object (the anatomical MRI in this case) that it reads corresponds to the size of a human head, whereas the mouse MRI is much smaller.

In the figure of **[ft_determine_coordsys](/reference/utilities/ft_determine_coordsys)**, the sphere at the origin, and the distance between each thick line segment is by default 1 cm, and the axes are 15 cm long, as that is appropriate for judging the human anatomy.

The units can be fixed by

    mri_realigned.unit = 'mm';

After coregistration of the MRI with the Paxinos coordinate system, it is [convenient to reslice it](/faq/why_does_my_anatomical_mri_show_upside-down_when_plotting_it_with_ft_sourceplot), i.e., to interpolate the greyscale values on a 3-D grid that is nicely aligned with the cardinal axes.

    cfg = [];
    cfg.xrange = [-6 6];
    cfg.yrange = [-8 1];
    cfg.zrange = [-7 10];
    cfg.resolution = 0.0470;
    mri_resliced = ft_volumereslice(cfg, mri_realigned)

    figure
    ft_sourceplot(cfg, mri_resliced)

FIXME insert figure (16 ft_sourceplot)

### Reading and coregistring the anatomical atlas

On <http://brainatlas.mbi.ufl.edu> (and our download server) there is also an anatomically labeled version of the same brain available. We can use this as anatomical atlas.

    atlas = ft_read_atlas('Num1_MinDef_M_Normal_age12_num10Atlas.hdr')

Since the original anatomical and labeled MRI are expressed in the same coordinate system, we can apply the same transformation to the atlas. Again, we also fix the units and specify the coordinate system.
    
    atlas_realigned           = atlas;
    atlas_realigned.transform = mri_realigned.transform;
    atlas_realigned.unit      = mri_realigned.unit;
    atlas_realigned.coordsys  = mri_realigned.coordsys;

We can visualise the atlas in the same way as the anatomical MRI.

    cfg = [];
    ft_sourceplot(cfg, atlas);

FIXME insert figure (17 ft_sourceplot)

You can see (by clicking around) that it contains integer values. Each area with the same integer value is a single region.

The MRI file does not include the labels of the different tissue types. We can fix this and manually assign the labels from this [paper](http://www.sciencedirect.com/science/article/pii/S0306452205007633#).

      % rename "anatomy" into "tissue"
      atlas_realigned.tissue = atlas_realigned.anatomy;
      atlas_realigned = rmfield(atlas_realigned, 'anatomy');

      % add a "tissuelabel" cell-array with the names
      atlas_realigned.tissuelabel = {'Hippocampus', 'External_capsule', 'Caudate_putamen', ...
        'Ant_commissure', 'Globus_pallidus', 'Internal_Capsule', 'Thalamus', ...
        'Cerebellum', 'Superior_colliculi', 'Ventricles', 'Hypothalamus', ...
        'Inferior_colliculi', 'Central_grey', 'Neocortex', 'Amygdala', ...
        'Olfactoryt_bulb', 'Brain_stem', 'Rest_of_Midbrain', ...
        'BasalForebrain_septum', 'Fimbria'};

With the correct labels, we can use **[ft_sourceplot](/reference/ft_sourceplot)** to plot the anatomy and to show the corresponding atlas label by clicking on a location in the brain.

    cfg = [];
    cfg.atlas = atlas_realigned;
    ft_sourceplot(cfg, mri_resliced)

FIXME insert figure (18 ft_sourceplot with atlas label)

It is also possible to explore only the atlas itself, using the anatomical labels in the atlas. For that it is again convenient to reslice the atlas so that the voxels are aligned with the canonical axes. Note that we do **not** want to interpolate th evalues, since a voxel that happens to be in between tissue 1 and 2 cannot be assumed to correspond to tissue label 2.

    cfg = [];
    cfg.xrange = [-6 6];
    cfg.yrange = [-8 1];
    cfg.zrange = [-7 10];
    cfg.resolution = 0.0470;
    cfg.method = 'nearest'; % take the nearest value, do not interpolate
    atlas_resliced = ft_volumereslice(cfg, atlas_realigned)

    cfg = [];
    cfg.atlas = atlas_resliced;
    cfg.funparameter = 'tissue';
    cfg.funcolormap = 'lines';
    ft_sourceplot(cfg, atlas_resliced)

FIXME insert figure (19 ft_sourceplot with atlas label and color)

### Make segmentation of the brain and skull

We start with a histogram of the grey-scale values

    hist(mri_resliced.anatomy(:), 100)
    axis(1.0e+06 * [-0.0011    0.0170   -0.8100    1.5900]); % ugh!

Make a binary image of the brain

    mri_resliced.brain = mri_resliced.anatomy>6000;

    se = strel_bol(9);
    mri_resliced.skull = imdilate(mri_resliced.brain, se);

    combined = mri_resliced.skull + mri_resliced.brain;
    imagesc(combined(:,:,256))

The skull shows up with integer value 1 and the brain (which is fully enclosed in the skull) shows up with integer value 2.

FIXME insert figure (20 image segmentation)

### Make mesh of the brain-skull and skull-skin boundary

This part describes how to make the volume conduction model for the source localization. In the previous section we performed a segmentation to extract the brain and skull. Since we use an in-vitro MRI without skull, a virtual skull was made from the brain surface by image dilation. To construct the surfaces of the boundaries, we use the **[ft_prepare_mesh](/reference/ft_prepare_mesh)** to get the triangulated meshes for skull and brain.

    cfg             = [];
    cfg.tissue      = {'skull', 'brain'};
    cfg.numvertices = [1500, 1500];
    mesh            = ft_prepare_mesh(cfg, mri_resliced);

FIXME insert figure (21 ft_prepare_mesh plot)

We've been set limited number of vertices in **[ft_prepare_mesh](/reference/ft_prepare_mesh)**.
Because [OpenMEEG](http://www-sop.inria.fr/athena/software/OpenMEEG/) could not support to bigger volume above around 1500 vertices.

### Make BEM volume conduction model

After making up volume objects, we perform the **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** for assigning the electrical property of volumes. From the literature in human study, the brain conductivity ranges from 0.12-0.48/Ω.m [ref 1-3], and the human skull from 0.006-0.015/Ω.m [ref 4,5] or even higher as 0.032-0.080/Ω.m [ref 5]. According to another studies for the conductivity ratio between skull and brain, they reported numerical value with large variation the ranges from 25 to 80 times [ref 6]. It is hard to specify the brain-to-skull conductivity ratio from these values with such large variations. In this step, we just assign conductivities applying to 80 times ratio between skull and brain.

1.  Nicholson, Paul W. "Specific impedance of cerebral white matter." Experimental neurology 13.4 (1965): 386-401.
2.  Gonçalves, Sónia I., et al. "In vivo measurement of the brain and skull resistivities using an EIT-based method and realistic models for the head." Biomedical Engineering, IEEE Transactions on 50.6 (2003): 754-767.
3.  Oostendorp, Thom F., Jean Delbeke, and Dick F. Stegeman. "The conductivity of the human skull: results of in vivo and in vitro measurements." Biomedical Engineering, IEEE Transactions on 47.11 (2000): 1487-1492.
4.  Hoekema, R., et al. "Measurement of the conductivity of skull, temporarily removed during epilepsy surgery." Brain topography 16.1 (2003): 29-38.
5.  Rush, S., and Daniel A. D. "Current distribution in the brain from surface electrodes." Anesthesia & Analgesia 47.6 (1968): 717-723.
6.  Lai, Y., et al. "Estimation of in vivo human brain-to-skull conductivity ratio from simultaneous extra-and intra-cranial electrical potential recordings." Clinical neurophysiology 116.2 (2005): 456-465.

[OpenMEEG](http://www-sop.inria.fr/athena/software/OpenMEEG/) is an external package that solves the forward problem. It implements a Boundary Element Method (BEM) and provides accurate solutions when dealing with realistic head models. As we mentioned above in the segmentation section, we are computing the BEM for two layers (brain and skull).

    bnd_in.bnd = bnd;
    bnd_in.conductivity = [0.33/80, 0.33];
    cfg = [];
    cfg.tissue = {'skull', 'brain'};
    cfg.method = 'openmeeg';
    vol = ft_prepare_headmodel(cfg, bnd_in);

    vol =

                 bnd: [1x2 struct]
                cond: [0.0041 0.3300]
        skin_surface: 1
              source: 2
                 mat: [5996x5996 double]
                type: 'openmeeg'
                unit: 'cm'
                 cfg: [1x1 struct]

## Specification of electrodes

Now that we have the volume conduction model, we need to specify where the electrodes are relative to the head model. The electrode positions consist of real distances of each electrode to the middle of the 4th layer (bregma point).

    loc = [
      -1.461  3.457  0.437357631
      1.461  3.457  0.437357631
      -1.461  2.396  0.328018223
      1.461  2.396  0.328018223
      -2.147  2.396  0.482915718
      2.147  2.396  0.482915718
      -1.461  1.131  0.23690205
      1.461  1.131  0.23690205
      -2.396  1.131  0.501138952
      2.396  1.131  0.501138952
      -1.71  0  0.264236902
      1.71  0  0.264236902
      -3.243  0  0.738041002
      3.243  0  0.738041002
      -1.559  -0.989  0.118451025
      1.559  -0.989  0.118451025
      -2.512  -0.989  0.291571754
      2.512  -0.989  0.291571754
      -3.51  -0.989  0.765375854
      3.51  -0.989  0.765375854
      -1.666  -2.254  0.027334852
      1.666  -2.254  0.027334852
      -2.673  -2.254  0.118451025
      2.673  -2.254  0.118451025
      -3.67  -2.254  0.61047836
      3.67  -2.254  0.61047836
      -1.684  -3.332  0.018223235
      1.684  -3.332  0.018223235
      -2.949  -3.332  0.346241458
      2.949  -3.332  0.346241458
      -4.009  -3.332  0.84738041
      4.009  -3.332  0.84738041
      -1.675  -4.695  0.291571754
      1.675  -4.695  0.291571754
      -2.619  -4.695  0.464692483
      2.619  -4.695  0.464692483
      -1.764  -5.702  0.4738041
      1.764  -5.702  0.4738041
    ];

To confirm the alignment between the headmodel and electrode positions, we make a 3D figure using the following code.

    ft_plot_mesh(mesh, 'facecolor', 'skin', 'edgecolor', 'b');
    hold on
    alpha 0.5
    camlight
    plot3(loc(:, 1), loc(:, 2), loc(:, 3), '*g');
    hold off

FIXME insert figure (22 plot_mesh with electrode)

You see that the figure is not what you would expect. The electrode positions are not expressed in the correct coordinates. We can fix this manually.

We use the ft_headcoordinates function with the input variables bregma_middle, lambda_middle, and bregma_ventral.

- The bregma_middle indicates the bregma point [0, 0, 0].
- The lambda_middle indicates the lambda point [0, y, 0] aligned with anterio-parietal axis.
- The bregma_ventral indicates a location inside the brain compared to the electrode array.

          bregma_middle  = mean(loc(11:12, :));
          lambda_middle  = mean(loc([27 28 33 34], :));
          bregma_ventral = bregma_middle + [0 0 1];

          elec2head = ft_headcoordinates(bregma_middle, lambda_middle, bregma_ventral, 'paxinos');

Subsequently, we can apply the transformation matrix to the electrode position. We first organize the electrode positions in a MATLAB structure, in line with the FieldTrip [description of electrodes](/faq/how_are_electrodes_magnetometers_or_gradiometers_described).

    elec.elecpos  = loc;
    elec.label = {
        'FP1';'FP2';
        'AF3';'AF4';'AF7';'AF8';...
        'F1';'F2';'F5';'F6';
        'FC1';'FC2';'FC5';'FC6';...
        'C1';'C2';'C3';'C4';'C5';'C6';
        'CP1';'CP2';'CP3';'CP4';'CP5';'CP6';...
        'P1';'P2';'P3';'P4';'P5';'P6';
        'PO3';'PO4';'PO7';'PO8';
        'O1';'O2'
      };
    
    % apply the transformation
    elec = ft_transform_geometry(elec2head, elec);
    
    % remember the coordinate system that we assigned
    elec.coordsys = 'paxinos';

We check the result of co-registration between the headmodel and electrodes in a 3D figure.

    figure
    ft_plot_mesh(mesh, 'facecolor', 'skin', 'edgecolor', 'b');
    hold on
    ft_plot_sens(elec);
    hold off
    axis on
    grid

FIXME insert figure (23 plot_mesh with electrode)

After the co-registration there are still some small gaps between the electrode positions and the skull surface. When computing the BEM solutions, FieldTrip will automaticall project the 3D electrode positions orthogonally onto the skull surfacey.

### Deal with differences in animal size

Compared to human EEG, in the mouse EEG recordings the electrode grid does not scale along with the size of the animal. Consequently, the position of the electrodes relative to the brain depends on the head size. This affects the topographic plotting of channel level data, the comparison (group stats) of channel-level data from multiple animals, and the electrode positions and volume conduction model used for source reconstruction.

The principled solution to this is that the experimentally measured lambda-bregma distance (or some other measure of head size) is used to scale the background image in the channel layout and to scale the volume conduction model of the head.

The more pragmatic solution that we use here is to inverse-scale the electrodes and keep the head size constant. Effectively the result is the same, but it is easier to manage. Furthermore, it makes the source-level results directly comparable over animals.

### Make the leadfields

The final procedure of the forward problem is to generate the leadfield matrices that representing the linear relation between the dipole positoins in the sourcemodel and the predicted measurements on the electrodes. Sometimes this is also referred to as the gain matrix.


With **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)** we place a grid of dipoles in the head model.

    cfg            = [];
    cfg.elec       = ft_convert_units(elec, 'mm');
    cfg.headmodel  = ft_convert_units(headmodel, 'mm');
    cfg.xgrid      = -6:0.25:6;
    cfg.ygrid      = -8:0.25:1;
    cfg.zgrid      = -7:0.25:10;
    cfg.unit       = 'mm';
    sourcemodel    = ft_prepare_sourcemodel(cfg);


With **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)** we can get the matrices with respect to aligned electrode position and BEM meshes.

    cfg                 = [];
    cfg.sourcemodel     = sourcemodel;
    cfg.elec            = ft_convert_units(elec, 'mm');
    cfg.headmodel       = ft_convert_units(headmodel, 'mm');
    cfg.reducerank      = 3;
    cfg.normalize       = 'yes';
    cfg.channel         = sens.label;
    leadfield           = ft_prepare_leadfield(cfg);

    leadfield =

            xgrid: [1x40 double]
            ygrid: [1x29 double]
            zgrid: [1x59 double]
              dim: [40 29 59]
              pos: [68440x3 double]
        leadfield: {68440x1 cell}
           inside: [68440x1 logical]
             unit: 'mm'
              cfg: [1x1 struct]

## Calculating the cross spectral density matrix

The [beamforming technique](/tutorial/beamformer) for EEG and MEG source reconstruction is based on a spatial filter. The [DICS spatial filter](http://www.pnas.org/content/98/2/694.short) is derived from the cross-spectral density matrix, which is the frequency-domain counterpart of the covariance matrix. This matrix contains the cross-spectral densities for all channel combinations and is computed from the Fourier transformed data of the single trials. It is given as output by **[ft_freqanalysis](/reference/ft_freqanalysis)** when `cfg.output = 'powandcsd'`.

Before computing the cross-spectral density matrix, we make subselections of the data in the pre-stimulus and post-stimulus intervals. We will use these later to make a contrast between the two conditions.

    % make selections in the data
    cfg          = [];
    cfg.toilim   = [-0.6 -0.1];
    cfg.channel  = {'all', '-VPM'};
    dataPre      = ft_preprocessing(cfg, data_reref);
    
    cfg          = [];
    cfg.toilim   = [0.1 0.6];
    cfg.channel  = {'all', '-VPM'};
    dataPost     = ft_redefinetrial(cfg, data_reref);

    cfg          = [];
    dataAll      = ft_appenddata(cfg, dataPre, dataPost);

The frequency of interest is 10 Hz and we use multitapering with a smoothing window of +/-4 Hz:

    % compute the cross-spectral density
    cfg           = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'powandcsd';
    cfg.tapsmofrq = 4;
    cfg.foilim    = [10 10];
    freqPre       = ft_freqanalysis(cfg, dataPre);

    cfg           = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'powandcsd';
    cfg.tapsmofrq = 4;
    cfg.foilim    = [10 10];
    freqPost      = ft_freqanalysis(cfg, dataPost);

    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'powandcsd';
    cfg.tapsmofrq = 4;
    cfg.foilim    = [10 10];
    freqAll       = ft_freqanalysis(cfg, dataAll);

## Source reconstruction

Using the covariance matrices and the leadfield matrices a spatial filtering is calculated and estimated the dipole intensity for each grid point. By applying the filter to the Fourier transformed data we can then estimate the power for neural activity by optogenetic stimuli (10 Hz). This results in a power estimate for each grid point. To get normalized index for the neural activity we have to do the spatial filtering both pre-stimulus and post-stimulus.

    cfg                   = [];
    cfg.elec              = ft_convert_units(elec, 'mm');
    cfg.method            = 'dics';
    cfg.frequency         = 10;
    cfg.grid              = leadfield;
    cfg.headmodel         = headmodel;
    cfg.channel           = elec.label;
    cfg.dics.projectnoise = 'yes';
    cfg.dics.lambda       = '5%';
    cfg.dics.keepfilter   = 'yes';
    cfg.dics.realfilter   = 'yes';
    sourceAll             = ft_sourceanalysis(cfg, freqAll);

    % use the common filter approach to make a clean statistical contrast
    cfg.sourcemodel.filter  = sourceAll.avg.filter;
    sourcePre             = ft_sourceanalysis(cfg, freqPre);
    sourcePost            = ft_sourceanalysis(cfg, freqPost);

To calculate neural activity index is the same like below equation. The function **[ft_sourceinterpolate](/reference/ft_sourceinterpolate)** interpolates the source reconstructed activity or a statistical distribution onto the voxels or vertices of an anatomical description of the brain (MRI with atlas).

    sourceDiff          = sourcePost;
    sourceDiff.avg.pow  = (sourcePost.avg.pow - sourcePre.avg.pow) ./ sourcePre.avg.pow;

    cfg                 = [];
    cfg.downsample      = 2;
    cfg.parameter       = 'avg.pow';
    sourceDiffInt       = ft_sourceinterpolate(cfg, sourceDiff , mri_resliced);

### Visualize source reconstruction

    cfg               = [];
    cfg.atlas         = atlas;
    cfg.method        = 'ortho'; % 'slice'
    cfg.funparameter  = 'avg.pow';
    cfg.maskparameter = cfg.funparameter;
    cfg.funcolorlim   = [0.0 1.2];
    cfg.opacitylim    = [0.0 1.2];
    cfg.opacitymap    = 'rampup';
    ft_sourceplot(cfg, sourceDiffInt);

FIXME insert figure (24 source localization by DICS -ortho view)

## Suggested further reading

- video that describes the high-density mouse EEG array: <http://www.jove.com/video/2562/high-density-eeg-recordings-freely-moving-mice-using-polyimide-based>
- PLoS ONE (2013) paper about the mouse EEG source reconstruction: <http://www.ncbi.nlm.nih.gov/pubmed/24244506>
- comparable monkey ECoG: <http://www.ncbi.nlm.nih.gov/pubmed/19436080>
- comparable rat ECoG part 1: <http://www.ncbi.nlm.nih.gov/pubmed/24820913>
- comparable rat ECoG part 2: <http://www.ncbi.nlm.nih.gov/pubmed/24814253>
