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

The dataset used here does not include conventional digital trigger information. To record the timing of stimulation, an analog input channel 'HL1' was used to record TTL triggers. We use a customized function and the `cfg.trialfun='mousetrialfun'` option to define the segments. The trial function results in a `cfg.trl` Nx3 array that ccontains the begin- and endsample, and the trigger offset of each trial relative to the beginning of the raw data on disk.

    function trl = mousetrialfun(cfg)

    % this function requires the following fields to be specified
    % cfg.dataset
    % cfg.trialdef.threshold
    % cfg.trialdef.prestim
    % cfg.trialdef.poststim

    hdr   = ft_read_header(cfg.dataset);
    trigchan = find(strcmp(hdr.label, 'HL1'));
    trigger_data = ft_read_data(cfg.dataset, 'chanindx', trigchan);
    trigger_data = trigger_data - median(trigger_data);

    if isfield(cfg, 'trialdef') && isfield(cfg.trialdef, 'threshold')
      trigger_threshold = cfg.trialdef.threshold;
    else
      trigger_threshold = 0.5*max(trigger_data);
    end

    figure
    plot(trigger_data, 'b')
    hold on
    plot(trigger_threshold*ones(size(trigger_data)), 'r')

    trl = [];

    stim_duration = cfg.trialdef.prestim  * hdr.Fs; % number of samples
    rest_duration = cfg.trialdef.poststim * hdr.Fs; % number of samples

    % extracts, trigger timing ------------------------------------------------
    data1 = find(abs(trigger_data) > trigger_threshold); % exceed threshold
    data2 = find(data1-[0,data1(1,1:end-1)] > rest_duration); % exceed 'rest_duration'
    idx = data1(data2);
    clear data1 data2

    trigger_event(1,:) = idx;
    clear idx

    % give some feedback
    figure
    plot(trigger_event(1,:),0,'go')

    % extracts, trigger contents ----------------------------------------------
    for tr = 1:size(trigger_event,2)
      temp_data = abs(trigger_data(trigger_event(1,tr):trigger_event(1,tr)+stim_duration-1));
      idx = find_cross(temp_data, trigger_threshold, 'down'); clear temp_data
      trigger_event(2,tr) = size(find(idx == 1),2) / (stim_duration / hdr.Fs); clear idx
    end clear tr

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
    tidx1(find(data(1,1:end-1) <= thr)) = 1;
    tidx2(find(data(1,2:end) > thr)) = 1;
    idx1(find(tidx1 + tidx2 == 2)) = 1; clear tidx1 tidx2

    % down crossing
    tidx1 = zeros(1,size(data,2)-1);
    tidx2 = zeros(1,size(data,2)-1);
    idx2 = zeros(1,size(data,2)-1);
    tidx1(find(data(1,1:end-1) >= thr)) = 1;
    tidx2(find(data(1,2:end) < thr)) = 1;
    idx2(find(tidx1 + tidx2 == 2)) = 1; clear tidx1 tidx2

    % both
    idx0 = zeros(1,size(data,2)-1);
    idx0(find(idx1 + idx2 > 0)) = 1;

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
    cfg.trialdef.eventtype  = '?';
    cfg.trialdef.eventvalue = 40000;
    cfg.trialdef.prestim    = 1; % in seconds
    cfg.trialdef.poststim   = 2; % in seconds
    cfg = ft_definetrial(cfg);

You will see that the trial function produces a figure, which can be used to check whether the threshold was at the appropriate level and whether the stimulation onsets are properly detected.

FIXME insert figure (1 data loading)

The segments of interest are specified by their begin- and endsample and by the offset that specifies the timing relative to the data segment. The offset is zero here indicating that the first sample is interpreted as time t=0.

    >> cfg.trl

    ans =
            7447       13446           0
           17447       23446           0
           27447       33446           0
           37447       43446           0
           47446       53445           0
           57445       63444           0
           67445       73444           0
    ...

### preprocessing

After the segments of interest have been specified as `cfg.trl`, we read them from disk into memory. At this step we also specify other preprocessing options such as the filter settings.

    cfg.channel   = 'all';
    cfg.baseline  = [-0.30, -0.05];
    cfg.demean    = 'yes';
    cfg.bsfilter  = 'yes';
    cfg.bsfreq    = [59 61]
    cfg.lpfilter  = 'yes';
    cfg.lpfreq    = 100;
    data          = ft_preprocessing(cfg);

The output of ft_preprocessing is a structure which has the following field

    data =
               hdr: [1x1 struct]
             label: {39x1 cell}
              time: {1x88 cell}
             trial: {1x88 cell}
           fsample: 2000
        sampleinfo: [88x2 double]
               cfg: [1x1 struct]

In `data.sampleinfo` you can find the begin and endsample of each trial. The offset has been used to make an individual time axis `data.time` for each trial.

We can plot all channels for a single trial using standard MATLAB code:

    figure
    plot(data.time{1}, data.trial{1});
    legend(data.label);
    grid on

FIXME insert figure (2 single trial plot )

### Checking for artifacts

Using **[ft_databrowser](/reference/ft_databrowser)** we can do a quick visual inspection of the data in all trials and check for artefacts.

    cfg = [];
    cfg.viewmode = 'butterfly';
    cfg = ft_databrowser(cfg, data);

FIXME insert figure (3 datatrial browser)

The 41th channel with th elabel 'HL1' contains the analog TTL trigger, which is of much larger amplitude than all other channels. We can exclude it in the GUI by clicking the "channel" button or by using the following code:

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
    cfg.channel    = {'all', '-HL1'};  % we don't want to re-reference the trigger channel
    cfg.refchannel = {'FP1';'FP2';...
                      'AF3';'AF4';'AF7';'AF8';...
                      'F1';'F2';'F5';'F6';...
                      'FC1';'FC2';'FC5';'FC6';...
                      'C1';'C2';'C3';'C4';'C5';'C6';...
                      'CP1';'CP2';'CP3';'CP4';'CP5';'CP6';...
                      'P1';'P2';'P3';'P4';'P5';'P6';...
                      'PO3';'PO4';'PO7';'PO8';...
                      'O1';'O2'};
    data_car       = ft_preprocessing(cfg, data);

You can compare the original and re-referenced data using ft_databrowser.
 
    cfg            = [];
    cfg.viewmode   = 'vertical';
    cfg.channel    = {'all', '-HL1'};
    cfg            = ft_databrowser(cfg, data_car);

FIXME insert figure (5 datatrial browser)

## Channel level analysis - ERPs

### making a channel layout and deal with animal size

In order to make layout of high-density electrode array (HD-array) on mouse skull, FieldTrip support layout files ('mouse_layout.mat') that gives you exact control of the 2-D position of the sensors for topoplotting, and of the per-channel local coordinate axes for the multiplotting. The mat-file containing various variables to draw outlines of the headshape within the name “lay”.

Let us give you the information how to make customized layout for HD-array by using FieldTrip.
This figure indicates an electrode arrangement of HD-array (this example photo is taken from Lee et al. (2011) Journal of Visualized Experiments ([video](http://www.jove.com/video/2562/high-density-eeg-recordings-freely-moving-mice-using-polyimide-based), [pdf](http://www.jove.com/pdf/2562/jove-protocol-2562-high-density-eeg-recordings-freely-moving-mice-using-polyimide-based)).

{% include image src="/assets/img/tutorial/mouse_eeg/figure2.png" width="400" %}

You can specify cfg.image in ft_prepare_layout and subsequently click on the location of each electrode. After specifying each electrode location, you'll be asked to specify the outlines of the head (i.e. the circle around the head, the eyes, the nose and ears (dash lines) and optionally some lines representing other important landmarks: bold lines, bregma, and lambda) and to specify the mask for the topographic interpolation (green dash line).

Find the bregma and lambda points on the skull, and record them with the stereotaxic ruler. The bregma and lambda points are located in the same anterio-posterior axis.

The anterio-posterior axis of high-density electrode array (HD-array) matches the line between bregma and lambda points. The bregma point (0, 0) should be located at the middle of the 4th layer of the anterior of HD-array because we follow the Paxinos coordinate system. We implemented a mouse layout on fixed length (4.2 mm) of between bregma and lambda.

    cfg         = [];
    cfg.image   = 'mouse_skull_with_HDEEG.png';
    lay         = ft_prepare_layout(cfg);

After creating the layout, you should manually assign the correct name of the channel labels in the lay.label cell-array. Channel arrangement in lay.label is followed click sequence during ft_prepare_layout process. You can use ft_layoutplot for a visual inspection of the complete layout.

    cfg          = [];
    cfg.layout   = lay;
    ft_layoutplot(cfg);

FIXME insert figure (6 layout plot)

If you think that some outlines (nose, eyes, head, whiskers and ears) are not necessary, you can pass without assigning any outline. Next step is zero point calibration for the bregma point. If you, however, use customized layout for single subject, you don't need to carry out next step.

In the aspect of mouse anatomy, the bregma point is located in the middle of the 4th layer of the anterior of HD-array that it should be set (0, 0) because we follow the Paxinos coordinate system. To calibrate layout position, we just subtract the value of bregma on acquired layout from previous step.

    xy_shift         = [382, 280];
    lay.pos          = lay.pos – repmat(xy_shift, size(lay.pos, 1), 1);
    lay.mask{1, 1}   =  lay.mask{1, 1}- repmat(xy_shift, size(lay.mask{1, 1}, 1), 1);

    for i =1:1:size(lay.outline, 2)
      lay.outline{1, i}= lay.outline{1, i}- repmat(xy_shift, size(lay.outline{1, i}, 1), 1);
    end

To confirm your calibration,

    cfg = [];
    cfg.layout = lay;
    ft_layoutplot(cfg);

FIXME insert figure (7 layout plot)

If you are satisfy with the result, you can save it to a MATLAB file:

    save mouse_eeg.mat lay

HD-array is not scalable material. Each mouse, however, has different head size depending on strain, age, weight and gender. To circumvent this problem, we set to distance of bregma and lambda as the reference scale (4.2 mm). This distance could determine the level of head size with respect to individual subject. To get scalable mouse layout easily, we made a simple function ( ft_mouse_headsize_calibration ). If you use “ft_mouse_headsize_calibration” function, you can get calibrated head layout depending on the distance of bregma and lambda. The value of this function, cfg.B2Ldistance, is only affect size of outlines. This keeps the electrodes and the mask the same.
Take an example script as belo

    cfg             = [];
    cfg.layout      = 'mouse_layout.mat';    % mouse electrode layout
    cfg.B2Ldistance = 3.8;                   % unit (mm)
    [lay_new]       = ft_mouse_headsize_calibration(cfg);

To confirm your calibration,

    cfg             = [];
    cfg.layout      = lay_new;
    ft_layoutplot(cfg);

{% include image src="/assets/img/tutorial/mouse_eeg/figure3.png" width="400" %}

:!: This is discussed on <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=2602>

The current standards to deal with differences in mouse brain size are very comparable to those adopted in the Talairach-Tournoux anatomical atlas of the human brain. For human EEG it is easy to make use of a template and to compare or average subjects, since EEG recording caps scale along with the size of the human head. e.g., at the Donders we have caps in different sizes, ranging from 52 to 60 cm head circumference in 2cm steps, thereby accommodating approximately a 15% variance in head circumference.

For the mouse the electrode grids are however of fixed dimensions, but the head sizes still differ.

For example, let's think about a case of targetting CA1 hippocampus which is (AP, ML, DV) = -2, 1.5, -2 with respect to the bregma according to the mouse atlas. Each individual mouse has different brain size. What we do is to measure the length between bregma to lambda, and if the length is 4.2 mm, we multiply the target distance by 4.2/3.9 ~= 1.077. Hence the stereotaxic target for CA1 would be (AP, ML, DV) = -2.15, 1.62, -2.15.
Since the tolerance range of the stereotaxic is 0.1 mm, the actual target would be -2.1, 1.6, -2.1.
I observed that some group rescale only anterior posterior (AP). Hence according to them the target coordinate would be -2.1, 1.5, -2. Unlike human, mouse has a secondary confirmation procedure, which is called histology. Hence, we can confirm whether we hit the target or not via histological procedure after recordings.
For your information, many neuroscientists agree that this rescaling method can work as a rule of thumb but individual difference between animals cannot be neglected, emphasizing the post-hoc histological confirmation.

The anatomical structure of mouse brain due not vary dramatically if the weight and/or the length between bregma and lambda are in the similar range, in a sense of a few hundreds micrometer. For example, any structure with a dimension ranging larger than a couple of hundreds um, we seldom fail to hit this structure. However, when we aim for a structure with a sharp shape with dimension smaller than a couple of hundreds um, we half fail to hit that structure. But if this structure is on the cortex or near, we seldom fail.

### compute and visualize the ERPs

The ERP that is time locked to stimulus onset is computed by averaging the data segments over all trials.

    cfg      = [];
    timelock = ft_timelockanalysis(cfg, data);

We can plot it with standard MATLAB command

    figure
    plot(timelock.time, timelock.avg(1:40,:)); % excluding channel HL1
    legend(timelock.label(1:40));

FIXME insert figure (8 timelock plot)

Using the figure legend, we see that channel VPM shows a large response to the stimulation. This makes sense, because channel VPM corresponds to the depth electrode that is inserted along with the optode, i.e. it records from the stimulated site.

Rather than plotting all ERPs on top of each other, we can also plot them according to the channel layout.

    cfg             = [];
    cfg.layout      = 'mouse_eeg14.mat';
    cfg.showoutline = 'yes';
    figure
    ft_multiplotER(cfg, timelock);

FIXME insert figure (9 timelock plot)

You can use the zoom in and zoom out buttons of MATLAB. Furthermore, you can make a selection of channels and click in the selection, which causes them to be averaged and displayed in a single plot. In the single plot, you can make a selection of time (i.e. latency), which is subsequently averaged as an interpolated topographic distribution of the potential.

## Channel level analysis - TFRs

In this section, we will describe how to calculate time-frequency representations using Hanning window.

    %% power spectrogram
    cfg                   = [];
    cfg.output            = 'pow';
    cfg.method            = 'mtmconvol';
    cfg.taper             = 'hanning';
    cfg.foi               = 4:2:100;                         % frequency of interest
    cfg.t_ftimwin         = ones(length(cfg.foi),1).*0.25;   % 250 ms window
    cfg.toi               = -1:0.01:3.0;                     % -1:0.01:3.0;
    freq                  = ft_freqanalysis(cfg, data);

The output of **[ft_freqanalysis](/reference/ft_freqanalysis)** is a structure which has the following field

    freq =

            label: {41x1 cell}
           dimord: 'chan_freq_time'
             freq: [1x49 double]
             time: [1x401 double]
        powspctrm: [41x49x401 double]
              cfg: [1x1 struct]

The element freq.powspctrm contains the temporal response (-1 ~ 3 sec, 0.01 sec sliding) of the power for each specified frequency (4~ 100 Hz, 2 Hz step).

### visualizing TFRs

This part shows how to visualize the results of time-frequency analysis with respect to **[ft_multiplotTFR](/reference/ft_multiplotTFR)** and **[ft_singleplotTFR](/reference/ft_singleplotTFR)**.

To visualize the power changes, a normalization with respect to a baseline interval will be performed.
This method, "relchange", means (active period-baseline)/baseline. Note that the "relchange" is expressed as a ratio of subtracting, for each frequency.
If you want to visualize TFR on the head outline of mouse, "cfg.layout=mouse_layout.mat" have to be declared.

    %% visualization of all EEG channels
    cfg                   = [] ;
    cfg.xlim              = [-1 2];
    cfg.ylim              = [4 100];
    cfg.zlim              = [-1.0 1.0];
    cfg.colorbar          = 'yes';
    cfg.layout            = 'mouse_layout.mat';
    cfg.showoutline       = 'yes';
    cfg.baseline          = [-0.5 0];
    cfg.baselinetype      = 'relchange' ;
    ft_multiplotTFR(cfg, freq);

FIXME insert figure (10 ft_multiplotTFR)

Otherwise, you can visualize TFR sequentially without mouse layout.

    %% visualization of all EEG channels, not topographically arranged
    cfg                   = [] ;
    cfg.xlim              = [-1 2];
    cfg.ylim              = [4 100];
    cfg.zlim              = [-1.0 1.0];
    cfg.colorbar          = 'yes';
    cfg.layout            = 'ordered'
    cfg.showlabels        = 'yes';
    cfg.baseline          = [-0.5 0];
    cfg.baselinetype      = 'relchange' ;
    ft_multiplotTFR(cfg, freq);

FIXME insert figure (11 ft_multiplotTFR with order)

And, you can also visualize single TFR per each channel.

    %% single channel visualization
    cfg                   = [] ;
    cfg.channel           = 'C4'; % channel
    cfg.xlim              = [-1 2];
    cfg.ylim              = [4 100];
    cfg.zlim              = [-1.0 1.0];
    cfg.colorbar          = 'yes';
    cfg.baseline          = [-0.2 0];
    cfg.baselinetype      = 'relchange' ;
    ft_singleplotTFR(cfg, freq);
    xlabel('Sec'); ylabel('Hz');

FIXME insert figure (12 ft_singleplotTFR with order)

## Coregistration of anatomy and construction of volume conduction model

### Reading and coregistring the anatomical data

The anatomical MRI is obtained from http://brainatlas.mbi.ufl.edu.

    mri = ft_read_mri('Num1_MinDef_M_Normal_age12_num10.hdr')

    figure
    ft_determine_coordsys(mri, 'interactive', 'no')

FIXME insert figure (13 ft_determine_coordsys)

This gives a figure that shows the origin (white sphere), the x-, y-, and z-axes. We notice that the origin is not at Bregma, nor at the interaural point. This is inconsistent with the desired [coordinate system](/faq/coordsys#details_on_the_paxinos-franklin_mouse_coordinate_system), hence we have to realign the anatomical MRI.

#### Coregistration using high-level graphical function

We can use the **[ft_volumerealign](/reference/ft_volumerealign)** function to coregister the anatomical MRI to the desired coordinate system. There are multiple coordinate systems in which the anatomy of the brain and head can be described, but here we want to use the Paxinos-Franklin cordite system which uses Bregma and Lambda as anatomical landmarks (or fiducials).

    cfg = [];
    cfg.coordsys  = 'paxinos';
    mri_realigned = ft_volumerealign(cfg, mri);

FIXME insert figure (14 ft_volumerealign)

The anatomical MRI is displayed in three orthogonal plots. You have to visually identify the fiducials and press "b" for bregma, "l" for lambda and "z" for a midsagittal point. Using "f" you can toggle the fiducials on and off. Once you are happy with their placement, you press "q" and the realigned mri is returned

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

The **[ft_headcoordinates](/reference/utilities/ft_headcoordinates)** function provides the homogenous transformation matrix to rotate and translate the MRI into the Paxinos coordinate system

    head2paxinos = ft_headcoordinates(bregma, lambda, midsagittal, 'paxinos')

    head2paxinos =

        0.9994    0.0225    0.0256   -0.0009
        0.0225   -0.9997    0.0006   -4.4011
        0.0256   -0.0000   -0.9997    3.8987
             0         0         0    1.0000

We can apply this transformation to the MRI with

    vox2head    = mri.transform;
    vox2paxinos = head2paxinos * vox2head;

    mri_realigned2           = mri;         % copy the original MRI
    mri_realigned2.transform = vox2paxinos; % update the homogenous transformation matrix

It is useful to also explicitly specify the coordinate system in the anatomical MRI. It is used in **[ft_sourceplot](/reference/ft_sourceplot)** and various other functions to check whether various geometrical objects are expressed in the same coordinate system.

    mri_realigned2.coordsys = 'paxinos';

#### Correcting the units of the anatomical MRI

Finally, we notice is that the units are off by a factor 10x. In the figure of **[ft_determine_coordsys](/reference/utilities/ft_determine_coordsys)**, the sphere at the origin, each thick line segment is by default 1 cm, and the axes are 15 cm long, as that is appropriate for judging the human anatomy. We can also plot it with

The units can be fixed by

    mri_realigned.unit = 'mm';

After coregistration of the MRI with the Paxinos coordinate system, it is [convenient to reslice it](/faq/why_does_my_anatomical_mri_show_upside-down_when_plotting_it_with_ft_sourceplot), i.e. to interpolate the greyscale values on a 3-D grid that is nicely aligned with the cardinal axes.

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

On <http://brainatlas.mbi.ufl.edu> there is also an anatomically labeled version of the same brain available. We can use this as anatomical atlas.

    atlas = ft_read_atlas('Num1_MinDef_M_Normal_age12_num10Atlas.hdr')

Since the original anatomical and labeled MRI are expressed in the same coordinate system, we can apply the same transformation to the atlas. Again, we also fix the units and specify the coordinate system.

    atlas.transform = mri_realigned.transform;
    atlas.unit      = mri_realigned.unit;
    atlas.coordsys  = mri_realigned.coordsys;

We can visualise the atlas in the same way as the anatomical MRI.

    cfg = [];
    cfg.anaparameter = 'brick0'; % use brick0 instead of anatomy
    ft_sourceplot(cfg, atlas);

FIXME insert figure (17 ft_sourceplot)

You can see (by clicking around) that it contains integer values. Each area with the same integer value is a single region. The name of the region is specified in

    >> atlas.brick0label

    ans =

      Columns 1 through 14
        'tissue 1'    'tissue 2'    'tissue 3'    'tissue 4'    'tissue 5'    'tissue 6'    'tissue 7'    'tissue 8'    'tissue 9'    'tissue 10'    'tissue 11'    'tissue 12'    'tissue 13'    'tissue 14'

      Columns 15 through 20
        'tissue 15'    'tissue 16'    'tissue 17'    'tissue 18'    'tissue 19'    'tissue 20'

You see that the anatomical labels are not what you would expect. This is due to the anatomically labeled MRI file not specifying the correct labels. We can fix this and manually assign the labels from this [paper](http://www.sciencedirect.com/science/article/pii/S0306452205007633#).

      atlas.brick0label = {'Hippocampus', 'External_capsule', 'Caudate_putamen',...
        'Ant_commissure', 'Globus_pallidus', 'Internal_Capsule', 'Thalamus',...
        'Cerebellum', 'Superior_colliculi', 'Ventricles', 'Hypothalamus',...
        'Inferior_colliculi', 'Central_grey', 'Neocortex', 'Amygdala',...
        'Olfactoryt_bulb', 'Brain_stem', 'Rest_of_Midbrain',...
        'BasalForebrain_septum', 'Fimbria' };

With the correct labels, we can use **[ft_sourceplot](/reference/ft_sourceplot)** to plot the anatomy and to show the corresponding atlas label by clicking on a location in the brain.

    cfg = [];
    cfg.atlas = atlas;
    ft_sourceplot(cfg, mri_resliced)

FIXME insert figure (18 ft_sourceplot with atlas label)

It is also possible to explore only the atlas itself, using the anatomical labels in the atlas.

    cfg = [];
    cfg.atlas = atlas;
    cfg.funparameter = 'brick0';
    cfg.funcolormap = 'lines';
    ft_sourceplot(cfg, atlas)

FIXME insert figure (19 ft_sourceplot with atlas label and color)

### make segmentation of tissue inside skull

We start with a histogram of the grey-scale values

    hist(mri_resliced.anatomy(:), 100)
    axis(1.0e+06 * [-0.0011    0.0170   -0.8100    1.5900]); % ugh!

Make a binary image of the brain

    mri_resliced.brain = mri_resliced.anatomy>6000;

    se = strel_bol(9);
    mri_resliced.skull = imdilate(mri_resliced.brain, se);

    combined = mri_resliced.skull + mri_resliced.brain;
    imagesc(combined(:,:,256))

The skull shows up with integer value 1, the brain (which is fully enclosed in the skull) shows up with integer value 2.

FIXME insert figure (20 image segmentation)

### make mesh of brain-skull and skull-skin boundary

This part describes how to make the volume conduction model for the source localization.
In Previous section we did volume segmentation to extract brain and skull. Since we use In vitro MRI without skull, virtual skull was made by image dilation method from brain surface.
To set up mesh objects, we use the **[ft_prepare_mesh](/reference/ft_prepare_mesh)** to get the triangulated meshes for skull and brain.

    cfg             = [];
    cfg.tissue      = {'skull', 'brain'};
    cfg.numvertices = [1500, 1500];
    bnd             = ft_prepare_mesh(cfg, mri_resliced);

FIXME insert figure (21 ft_prepare_mesh plot)

We've been set limited number of vertices in **[ft_prepare_mesh](/reference/ft_prepare_mesh)**.
Because [OpenMEEG](http://www-sop.inria.fr/athena/software/OpenMEEG/) could not support to bigger volume above around 1500 vertices.

### make BEM volume conduction model

After making up volume objects, we perform the **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** for assigning the electrical property of volumes. From the literature in human study, the brain conductivity ranges from 0.12-0.48/Ω.m [1-3], and the human skull from 0.006-0.015/Ω.m [4,5] or even higher as 0.032-0.080/Ω.m [5]. According to another studies for the conductivity ratio between skull and brain, they reported numerical value with large variation the ranges from 25 to 80 times [6]. It is hard to specify the brain-to-skull conductivity ratio from these values with such large variations. In this step, we just assign conductivities applying to 80 times ratio between skull and brain.

[OpenMEEG](http://www-sop.inria.fr/athena/software/OpenMEEG/) is an external package that solves the forward problems. It implements a Boundary Element Method (BEM) and provides accurate solutions when dealing with realistic head models. As we mentioned above segmentation section, we are computing the two volume layers (skull and brain).

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

---

1.  Nicholson, Paul W. "Specific impedance of cerebral white matter." Experimental neurology 13.4 (1965): 386-401.
2.  Gonçalves, Sónia I., et al. "In vivo measurement of the brain and skull resistivities using an EIT-based method and realistic models for the head." Biomedical Engineering, IEEE Transactions on 50.6 (2003): 754-767.
3.  Oostendorp, Thom F., Jean Delbeke, and Dick F. Stegeman. "The conductivity of the human skull: results of in vivo and in vitro measurements." Biomedical Engineering, IEEE Transactions on 47.11 (2000): 1487-1492.
4.  Hoekema, R., et al. "Measurement of the conductivity of skull, temporarily removed during epilepsy surgery." Brain topography 16.1 (2003): 29-38.
5.  Rush, S., and Daniel A. D. "Current distribution in the brain from surface electrodes." Anesthesia & Analgesia 47.6 (1968): 717-723.
6.  Lai, Y., et al. "Estimation of in vivo human brain-to-skull conductivity ratio from simultaneous extra-and intra-cranial electrical potential recordings." Clinical neurophysiology 116.2 (2005): 456-465.

## Specification of electrodes

Now, we have the volume conduction model (vol) from MRI and the channel information (loc) for array electrode within different coordinate.
This channel information is real distances of each electrode from middle of 4th layer (bregma point) in high-density electrode array.

    loc = [-1.461  3.457  0.437357631
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
    1.764  -5.702  0.4738041];

If you want to confirm the alignment of between volumes and electrode, you can see the merged 3D figure using below simple code.

    ft_plot_mesh(bnd(1), 'facecolor', 'skin', 'edgecolor', 'b'); hold on;
    alpha 0.5; camlight;
    plot3(loc(:, 1), loc(:, 2), loc(:, 3), '*g'); hold off;

FIXME insert figure (22 plot_mesh with electrode)

You see that this figure is not what you would expect. This is due to the electrode position is not specifying the correct coordinate. We can fix this and manually assign the correct angle.

To coregistrate with them,

1.  use ft_headcoordinates function with input variables (bregma_middle, lambda_middle, and bregma_ventral).
    The bregma_middle indicates the bregma point [0, 0, 0].
    The lambda_middle indicates the lambda point [0, y, 0] aligned with anterio-parietal axis.
    The bregma_ventral indicates inside direction of electrode array.

          bregma_middle      = mean(loc(11:12, :));
          lambda_middle      = mean(loc([27 28 33 34], :));
          bregma_ventral     = bregma_middle + [0 0 1];

          trans              = ft_headcoordinates(bregma_middle, lambda_middle, bregma_ventral, 'paxinos');

2.  apply transformation matrix to electrode position,

We can get homogeneous transformation matrix (trans). Next, we calculate coregistered matrix by ft_transform_sens.
Input argument (loc_tmp) have to follow below format.

    loc_tmp.elecpos    = loc;
    loc_tmp.label      = {'FP1';'FP2';'AF3';'AF4';'AF7';'AF8';...
        'F1';'F2';'F5';'F6';'FC1';'FC2';'FC5';'FC6';...
        'C1';'C2';'C3';'C4';'C5';'C6';'CP1';'CP2';'CP3';'CP4';'CP5';'CP6';...
        'P1';'P2';'P3';'P4';'P5';'P6';'PO3';'PO4';'PO7';'PO8';'O1';'O2'};
    [sens]             = ft_transform_sens(trans, loc_tmp);

3.  verify co-registration
    Then, we can get registered electrode position like below figur

          sens.elecpos

          ans =

              1.4610   -0.0789   -3.4604
             -1.4610   -0.0789   -3.4604
              1.4610    0.0015   -2.3968
             -1.4610    0.0015   -2.3968
          ...

If you want to check graphical result for co-registration of between volume and electrode.

    ft_plot_mesh(bnd(1), 'facecolor', 'skin', 'edgecolor', 'b'); hold on;
    ft_plot_sens(sens); hold off;
    axis on; grid;

FIXME insert figure (23 plot_mesh with electrode)

Even after processing the co-registration, there could be have some gaps between electrode and skull surface. However, in the case of EEG in FieldTrip toolbox, the 3D electrode position is projected orthogonally onto the skull surface automatically.

### make leadfield matrix

The final procedure of the forward problem is to generate a leadfield that representing the linear relation between sourcemodel and measurements (Gain matrix).
By using **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)** we can get the matrices with respect to aligned electrode position and BEM meshes.

    cfg                 = [];
    cfg.elec            = ft_convert_units(sens, 'mm');
    cfg.headmodel       = ft_convert_units(vol, 'mm');
    cfg.reducerank      = 3;
    cfg.normalize       = 'yes';
    cfg.channel         = sens.label;
    cfg.xgrid      = -6:0.25:6;
    cfg.ygrid      = -8:0.25:1;
    cfg.zgrid      = -7:0.25:10;
    cfg.unit       = 'mm';
    leadfieldM          = ft_prepare_leadfield(cfg);

    leadfieldM =

            xgrid: [1x40 double]
            ygrid: [1x29 double]
            zgrid: [1x59 double]
              dim: [40 29 59]
              pos: [68440x3 double]
             unit: 'mm'
           inside: [1x28155 double]
          outside: [1x40285 double]
              cfg: [1x1 struct]
        leadfield: {1x68440 cell}

## Calculating the cross spectral density matrix

The beamforming technique is based on the spatial filter. [The DICS spatial filter](http://www.pnas.org/content/98/2/694.short) is derived from the frequency counterpart of the covariance matrix (the cross-spectral density matrix). This matrix contains the cross-spectral densities for all electrode combinations and is computed from the Fourier transformed data of the single trials. It is given as output when cfg.output = 'powandcsd'. The frequency of interest is 10 Hz and the smoothing window is +/-4 Hz:

Before applying cross-spectral density matrix, the redefine of time interval and the channel selection will be carry out like below.

    %% data redefine and cross frequency analysis
    cfg          = [];
    cfg.toilim   = [-0.6 -0.1];
    dataPre      = ft_redefinetrial(cfg, data_car);
    cfg          = [];
    cfg.channel  = {'all', '-VPM', '-Sync', '-HL1'};
    dataPre      = ft_preprocessing(cfg, dataPre);
    cfg          = [];
    cfg.toilim   = [0.1 0.6];
    dataPost     = ft_redefinetrial(cfg, data);
    cfg          = [];
    cfg.channel  = {'all', '-VPM', '-Sync', '-HL1'};
    dataPost     = ft_preprocessing(cfg, dataPost);

    cfg          = [];
    cfg.method   = 'mtmfft';
    cfg.output   = 'powandcsd';
    cfg.tapsmofrq= 4;
    cfg.foilim   = [10 10];
    cfg.channel  = {'all'};
    freqPre      = ft_freqanalysis(cfg, dataPre);

    cfg          = [];
    cfg.method   = 'mtmfft';
    cfg.output   = 'powandcsd';
    cfg.tapsmofrq= 4;
    cfg.foilim   = [10 10];
    cfg.channel  = {'all'};
    freqPost     = ft_freqanalysis(cfg, dataPost);

    dataAll      = ft_appenddata([], dataPre, dataPost);
    cfg = [];
    cfg.method    = 'mtmfft';
    cfg.output    = 'powandcsd';
    cfg.tapsmofrq = 4;
    cfg.foilim    = [10 10];
    freqAll       = ft_freqanalysis(cfg, dataAll);

## Source reconstruction

Using the covariance matrices and the leadfield matrices a spatial filtering is calculated and estimated the dipole intensity for each grid point. By applying the filter to the Fourier transformed data we can then estimate the power for neural activity by optogenetic stimuli (10 Hz). This results in a power estimate for each grid point. To get normalized index for the neural activity we have to do the spatial filtering both pre-stimulus and post-stimulus.

    cfg                 = [];
    cfg.elec            = ft_convert_units(sens, 'mm');
    cfg.method          = 'dics';
    cfg.frequency       = 10;
    cfg.grid            = leadfieldM;
    cfg.headmodel       = vol;
    cfg.channel         = sens.label;
    cfg.dics.projectnoise = 'yes';
    cfg.dics.lambda       = '5%';
    cfg.dics.keepfilter   = 'yes';
    cfg.dics.realfilter   = 'yes';
    sourceAll           = ft_sourceanalysis(cfg, freqAll);

    cfg.sourcemodel.filter     = sourceAll.avg.filter;
    sourcePre           = ft_sourceanalysis(cfg, freqPre );
    sourcePost          = ft_sourceanalysis(cfg, freqPost);

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

## Dealing with differences in size

Compared to human EEG, in the mouse EEG recordings the electrode grid does not scale along with the size of the animal. Consequently, the position of the electrodes relative to the brain depends on the head size. This affects the topographic plotting of channel level data, the comparison (group stats) of channel-level data from multiple animals, and the electrode positions and volume conduction model used for source reconstruction.

The principled solution to this is that the experimentally measured lambda-bregma distance (or some other measure of head size) is used to scale the background image in the channel layout and to scale the volume conduction model of the head.

An more pragmatic solution is to keep the head size the same, but rather to inverse-scale the electrodes and keep the head size constant. Effectively the result is the same, but it is easier to manage. Furthermore, it makes the source-level results directly comparable over animals.

## Links to background material

- video: http://www.jove.com/video/2562/high-density-eeg-recordings-freely-moving-mice-using-polyimide-based
- mouse EEG PLoS ONE 2013: http://www.ncbi.nlm.nih.gov/pubmed/24244506
- monkey ECoG: http://www.ncbi.nlm.nih.gov/pubmed/19436080
- rat ECoG part 1: http://www.ncbi.nlm.nih.gov/pubmed/24820913
- rat ECoG part 2: http://www.ncbi.nlm.nih.gov/pubmed/24814253
