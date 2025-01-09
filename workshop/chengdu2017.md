---
title: Chengdu, China
parent: FieldTrip courses and workshops
category: workshop
---

# FieldTrip workshop in Chengdu, China

- By whom: Robert Oostenveld
- When: 27-29 September 2017
- Where: Room 133 (theoretical part) and Room 135 (practical part), Center for Information in Medicine, School of Life Science & Technology, University of Electronic Science & Technology of China (UESTC)
- Local Organizer: Pedro Valdés-Sosa, Vincent (Qing Wang) and Eduardo.
- Advice for the attendees: Bring a computer with a recent MATLAB version and FieldTrip.

This will be a loosely organized workshop that comprises a series of lectures and hands-on sessions. In the first workshop session Robert will give an introduction on FieldTrip and we will do a hands-on session on preprocessing EEG data. After that we will jointly decide what the next topic will be. Possible topics include basic or advanced analysis methods for EEG/MEG using FieldTrip, the use of the [BIDS standard](http://bids.neuroimaging.io) for EEG/MEG data organization and sharing, and the use of the megconnectome pipelines from the [Human Connectome Project](http://humanconnectome.org).

## Program

#### Wednesday morning

- 1h - welcome and intro lecture - [slides](/assets/pdf/workshop/chengdu2017/introduction.pdf)
- 2h - hands-on on preprocessing of [EEG](/tutorial/preprocessing_erp) data.

#### Thursday morning

- 3h - preprocessing of Cuban EEG dataset (eyes opened/closed and hyperventilation)

#### Friday morning

- 1h - forward and inverse modeling lecture - [slides](/assets/pdf/workshop/chengdu2017/forward.pdf)
- 2h - anatomical processing and lead fields for Cuban EEG dataset

Please note that the script for the Cuban EEG dataset is further down on this page.

## Getting started with the hands-on sessions

{% include markup/skyblue %}
Please read the [FieldTrip reference paper](http://www.hindawi.com/journals/cin/2011/156869/) to understand the FieldTrip toolbox design.

If you are not familiar with MATLAB or are not certain about your MATLAB skills, please go through the [MATLAB for psychologists](http://www.antoniahamilton.com/matlab.html) tutorial (which is also useful for non-psychologists).
{% include markup/end %}

For the hands-on sessions you have to start MATLAB. We will provide a recent FieldTrip copy and the hands-on data on a USB stick. Alternatively, you can get them from the download server (which will be slower).

To get going, you need to start MATLAB. Then, you need to issue the following command

    restoredefaultpath
    cd <path_to_fieldtrip>
    addpath(pwd)
    ft_defaults

{% include markup/red %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed.
{% include markup/end %}

The `restoredefaultpath` command clears your path, keeping only the official MATLAB toolboxes. The `addpath(pwd)` statement adds the present working directory, i.e. the directory containing the FieldTrip main functions. The `ft_defaults` command ensures that all required subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you need to change into the hands-on specific directory, containing the data that is necessary to run the specific hands-on session.

## Script for the Cuban EEG dataset

    %%

    cfg = [];
    cfg.dataset = 'MC0001519.set';
    data = ft_preprocessing(cfg);

    figure
    plot(data.time{1}, data.trial{1}(1,:));
    title(data.label{1})

    cfg = [];
    cfg.viewmode = 'vertical';
    cfg = ft_databrowser(cfg, data)

    %% cut the data into 1 second pieces
    cfg = [];
    cfg.length = 1; % seconds
    data_1sec = ft_redefinetrial(cfg, data);

    cfg = [];
    cfg.viewmode = 'vertical';
    ft_databrowser(cfg, data_1sec);
    % in the GUI: increase the horizontal scale a few times

    cfg = [];
    cfg.viewmode = 'vertical';
    cfg.continuous = 'yes';
    ft_databrowser(cfg, data_1sec);
    % in the GUI: increase the horizontal scale a few times

    %% select every 2nd trial
    cfg = [];
    cfg.trials = 1:2:length(data_1sec.trial);
    data_1sec_sel = ft_selectdata(cfg, data_1sec);

    cfg = [];
    cfg.viewmode = 'vertical';
    cfg.continuous = 'yes';
    ft_databrowser(cfg, data_1sec_sel);
    % in the GUI: increase the horizontal scale a few times

    %%
    cfg = [];
    cfg.dataset = 'MC0001519.set';
    cfg.trialfun = 'ft_trialfun_general';
    cfg.trialdef.eventtype = '?';
    dummy = ft_definetrial(cfg);

    event = ft_read_event('MC0001519.set');
    disp(event(1));
    disp(event(2));
    disp(event(3));
    disp(event(4));
    disp(event(end));

    cfg = [];
    cfg.dataset = 'MC0001519.set';
    cfg.trialfun = 'ft_trialfun_general';
    cfg.trialdef.prestim = 0;
    cfg.trialdef.poststim = 10;
    cfg.trialdef.eventtype = 'gui';
    cfg = ft_definetrial(cfg);
    % in the GUI: select eyes_opened

    data = ft_preprocessing(cfg);

    cfg = [];
    cfg.viewmode = 'vertical';
    cfg.continuous = 'yes';
    ft_databrowser(cfg, data);
    % in the GUI: increase the horizontal scale to 60 seconds

    %% use a custom trialfun for reading the eyes_opened segments
    cfg = [];
    cfg.dataset = 'MC0001519.set';
    cfg.trialfun = 'trialfun_opened';
    cfg = ft_definetrial(cfg);

    data = ft_preprocessing(cfg);

    cfg = [];
    cfg.viewmode = 'vertical';
    cfg.continuous = 'yes';
    ft_databrowser(cfg, data);
    % in the GUI: increase the horizontal scale to 60 seconds

    %% use a custom trialfun for reading both segments
    cfg = [];
    cfg.dataset = 'MC0001519.set';
    cfg.trialfun = 'trialfun_both';
    cfg = ft_definetrial(cfg);

    data = ft_preprocessing(cfg);

    cfg = [];
    cfg.viewmode = 'vertical';
    cfg.continuous = 'yes';
    ft_databrowser(cfg, data);
    % in the GUI: increase the horizontal scale to 60 seconds

    %% select opened and closed
    cfg = [];
    cfg.trials = find(data.trialinfo==1);
    data_opened = ft_selectdata(cfg, data);

    cfg = [];
    cfg.trials = find(data.trialinfo==2);
    data_closed = ft_selectdata(cfg, data);

    %%

    cfg = [];
    cfg.length = 1; % seconds
    data_opened_1sec = ft_redefinetrial(cfg, data_opened);

    cfg = [];
    cfg.length = 1; % seconds
    data_closed_1sec = ft_redefinetrial(cfg, data_closed);

    % EXCERCISE: use ft_redefinetrial on "data" and look at the trialinfo in
    % the output

    cfg = [];
    cfg.method = 'mtmfft';
    cfg.taper = 'hanning';
    spectrum_opened = ft_freqanalysis(cfg, data_opened_1sec);
    spectrum_closed = ft_freqanalysis(cfg, data_closed_1sec);

    %%
    figure
    cfg = [];
    cfg.layout = 'EEG1010.lay';
    cfg.xlim = [2 40];
    ft_multiplotER(cfg, spectrum_opened, spectrum_closed)

    % EXCERCIS
    % - go back and use cfg.reref and cfg.refchannel
    % - go back and use ft_rejectvisual
    % - go back and use demean=yes and/or some filtering

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    cfg = [];
    cfg.method = 'runica';
    comp = ft_componentanalysis(cfg, data);
    % this takes about 30 seconds

    cfg = [];
    cfg.layout = 'EEG1010.lay';
    cfg.viewmode = 'component';
    cfg.continuous = 'yes';
    ft_databrowser(cfg, comp)
    % in the GUI: write down the artifact components

    cfg = [];
    cfg.component = [1 2];
    data_clean = ft_rejectcomponent(cfg, comp);

    cfg = [];
    cfg.viewmode = 'vertical';
    cfg.continuous = 'yes';
    ft_databrowser(cfg, data_clean);

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    data_clean = data;

    figure
    ft_plot_sens(data_clean.elec, 'label', 'label');
    % in the FIGURE: turn the axes around, then do
    ft_plot_axes(data_clean.elec);

    edit average58.ele

    elec = [];
    elec.elecpos = [
        119    91    12
        61    91    12
        141   140    69
        39   140    69
        154   147   123
        26   147   123
        158   115   163
        22   115   163
        120    50   205
        60    50   205
        158    83    52
        22    83    52
        173    71   107
        7    71   106
        158    76   177
        22    76   177
        90   155    52
        90   177   129
        90   128   194
        117   152    58
        63   152    58
        115   130   191
        65   130   191
        125   126    32
        55   126    32
        158   102   170
        22   102   170
        167   108    91
        13   108    91
        172   104   114
        8   104   114
        171    81   143
        9    81   143
        142    93   191
        38    93   191
        90    93     5
        90   171    88
        90   145   182
        90    90   209
        90    49   211
        103   110   202
        77   110   202
        118   147   176
        62   147   176
        132   150   167
        48   150   167
        120   169   127
        60   169   127
        158   114    69
        22   114    69
        143   149    94
        37   149    94
        117   166    99
        63   166    99
        172   101   138
        8   101   138
        158    57   173
        22    57   173
        ];
    elec.label = data_clean.label;
    elec.unit = 'mm';

    figure
    ft_plot_sens(elec, 'label', 'label');
    % in the FIGURE: turn the axes around, then do
    ft_plot_axes(elec);

    %%

    tmp = load('standard_bem.mat');
    headmodel = tmp.vol;

    cfg = [];
    cfg.method = 'interactive';
    cfg.headshape = headmodel.bnd(1);
    elec_realigned = ft_electroderealign(cfg, elec);
    % In the GUI: rotate 90 degrees around x, then apply
    % In the GUI: translate [-90 90 75], then apply and close

    %%

    if false
        mri = ft_read_mri('DICOM/MR.1.3.12.2.1107.5.2.6.14077.5.0.23815012430271304');
        disp(mri.transform)
    end

    mri = ft_read_mri('FREESURFER_SURF/mri/T1.nii');
    disp(mri.transform)
    mri = ft_determine_coordsys(mri);
    % in the GUI: press r, a, s, n

    % see https://www.fieldtriptoolbox.org/tutorial/sourcemodel

    cfg = [];
    ft_sourceplot(cfg, mri);

    cfg = [];
    cfg.method = 'flip';
    mri = ft_volumereslice(cfg, mri);

    cfg = [];
    ft_sourceplot(cfg, mri);

    ft_determine_coordsys(mri);

    %%
    cfg = [];
    cfg.coordsys = 'ctf';
    mri_realigned = ft_volumerealign(cfg, mri);

    cfg = [];
    ft_sourceplot(cfg, mri_realigned);

    figure
    ft_determine_coordsys(mri, 'interactive', 'no');
    figure
    ft_determine_coordsys(mri_realigned, 'interactive', 'no');

    %%
    cfg = [];
    cfg.spmversion = 'spm12';
    cfg.output = {'scalp', 'skull', 'brain'};
    mri_seg = ft_volumesegment(cfg, mri_realigned);
    % this takes some 2.5 minutes

    save mri_seg mri_seg
    load mri_seg

    cfg = [];
    % cfg.method = 'projectmesh';
    cfg.tissue = {'scalp', 'skull', 'brain'};
    cfg.spmversion = 'spm12';
    cfg.numvertices = [500 1000 1500];
    mesh = ft_prepare_mesh(cfg, mri_seg);

    %%
    figure
    hold on
    ft_plot_mesh(mesh(1), 'edgecolor', 'none', 'facecolor', 'r');
    ft_plot_mesh(mesh(2), 'edgecolor', 'none', 'facecolor', 'b');
    ft_plot_mesh(mesh(3), 'edgecolor', 'none', 'facecolor', 'g');
    alpha 0.2
    ft_plot_axes(mesh);

    %%

    % this is a work-around for a bug in ft_electroderealig
    % it does not show the labels
    ft_plot_sens(elec, 'label', 'label');
    % note the dense triangle at the back of the head

    cfg = [];
    cfg.method = 'interactive';
    cfg.headshape = mesh(1);
    elec_realigned = ft_electroderealign(cfg, elec);
    % In the GUI: rotate 90 degrees around x, then apply
    % In the GUI: rotate -90 degrees around z, then apply
    % In the GUI: translate [-110 90 50], then apply and close

    %%

    mesh = ft_convert_units(mesh, 'm');

    cfg = [];
    cfg.tissue = {'scalp', 'skull', 'brain'};
    cfg.conductivity = [1 1/20 1];
    % cfg.method = 'bemcp';
    % headmodel_bemcp = ft_prepare_headmodel(cfg, mesh);
    % cfg.method = 'dipoli';
    % headmodel_dipoli = ft_prepare_headmodel(cfg, mesh);
    cfg.method = 'openmeeg';
    headmodel_openmeeg = ft_prepare_headmodel(cfg, mesh);

    save headmodel_openmeeg

    %%
    load headmodel_dipoli

    cfg = [];
    cfg.resolution = 10;
    cfg.unit = 'mm';
    cfg.headmodel = headmodel_dipoli;
    sourcemodel = ft_prepare_sourcemodel(cfg);

    figure
    ft_plot_mesh(sourcemodel);

    figure
    ft_plot_mesh(sourcemodel.pos(sourcemodel.inside,:));
    ft_plot_axes(sourcemodel);

    cfg = [];
    cfg.grid = sourcemodel;
    cfg.headmodel = headmodel_dipoli;
    cfg.elec = elec_realigned;
    leadfield = ft_prepare_leadfield(cfg);

    %%

    cfg = [];
    cortex_lh = ft_read_headshape('FREESURFER_SURF/surf/lh.pial');
    cortex_rh = ft_read_headshape('FREESURFER_SURF/surf/rh.pial');

    figure
    ft_plot_mesh(cortex_lh);
    ft_plot_mesh(cortex_rh);
    ft_plot_axes(cortex_lh);

    ft_plot_mesh(sourcemodel.pos(sourcemodel.inside,:));

    % This shows that the cortical sheet is currently not coregistered
    % with the headmodel and electrodes. Also the sensity (number of
    % vertices) is too high. See https://www.fieldtriptoolbox.org/tutorial/sourcemodel
    % for the preferred pipeline.
