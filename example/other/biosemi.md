---
title: Example analysis pipeline for Biosemi data
parent: Various other examples
grand_parent: Examples
category: example
tags: [eeg, dataformat, biosemi, bdf]
redirect_from:
    - /example/biosemi/
---

# Example analysis pipeline for Biosemi data

The following is an example analysis pipeline that was used for the FieldTrip workshop at [CUNY, New York](http://www.cuny.edu) by Stephen and Saskia in 2011.

{% include markup/red %}
Biosemi BDF data should always be off-line referenced to one of the electrodes that is present in the data. The raw data in the file is relative to the CMS and still contains relatively much artifactual and line-noise. See also the [Biosemi website](https://www.biosemi.com/faq/cms&drl.htm).
{% include markup/end %}

### Modify layout file

    % load biosemi160 into q (which has sensor locations in polar coordinates
    % add fiducials then save

    % cfg=[];
    % cfg.layout='biosemi160.lay';
    % q=ft_prepare_layout(cfg);

    zeroline = 92/40*50;

    q{161,1} = 'nasion';
    q{161,2} = zeroline; %ten percent under FPz
    q{161,3} = q{104,3};

    q{162,1} = 'inion';
    q{162,2} = zeroline; %ten percent under Oz
    q{162,3} = q{23,3};

    q{163,1} = 'left';
    q{163,2} = -zeroline; %ten percent under T7
    q{163,3} = q{137,3};

    q{164,1} = 'right';
    q{164,2} = zeroline; %ten percent under T8
    q{164,3} = q{64,3};

    save('LayoutNY_fiducials',q);

    % construct 3D electrode positions

    load LayoutNY_fiducials.mat

    ph = cell2mat(q(:,2));
    th = cell2mat(q(:,3));

    x = sin(ph*pi/180) .* cos(th*pi/180);
    y = sin(ph*pi/180) .* sin(th*pi/180);
    z = cos(ph*pi/180);

    plot3(x, y, z, '.');
    elec.label = q(:,1);
    elec.pnt = [x y z];

    % scale to get into mm
    elec.pnt = 100*elec.pnt;

    vol = ft_read_headmodel('headmodel/standard_bem.mat');

    % realign electrodes to headmodel
    cfg = [];
    cfg.method = 'interactive';
    cfg.elec = elec;
    cfg.headshape = vol.bnd(1); %1 = skin
    elec = ft_electroderealign(cfg);

    %save new electrodes
    save elec160.mat elec

### Preprocessing

    clear all

    cond = {'Pitch20', 'Pitch40', 'Timbre490', 'Timbre510'};

    for c = 1:4 % loop over the 4 conditions
      for block = 1:4 % loop over the 4 blocks within each condition

        % create the trial definition
        cfg=[];
        cfg.filename              = ['data/RON_', cond{c}, '_Block', num2str(block), '_Sub03.bdf'];
        cfg.trialfun              = 'trialfunNY';
        cfg.trialdef.eventtype    = 'STATUS';
        cfg.trialdef.eventvalue   = [121 122 103 104 111 112]; % stimulus triggers (standard before (2), deviant (2), standard after(2))
        cfg.trialdef.eventcorrect = [1   2   1   2   1   2  ]; % correct response triggers
        cfg.trialdef.prestim      = 0.2; % latency in seconds
        cfg.trialdef.poststim     = 1;   % latency in seconds

        cfg = ft_definetrial(cfg);

        % remember condition and block
        trl = cfg.trl;
        trl(:,6) = c;
        trl(:,8) = block;

        % define the relevant trials
        for i=1:length(trl)
          if ismember(trl(i,4), [121 122])
            trl(i,7) = 1; % standard before
          elseif ismember(trl(i,4), [103 104])
            trl(i,7) = 2; % deviant
          elseif ismember(trl(i,4), [111 112])
            trl(i,7) = 3; % standard after
          end
        end

        % read and preprocess the data using the trial definition
        cfg=[];
        cfg.dataset       = ['data/RON_', cond{c}, '_Block', num2str(block), '_Sub03.bdf'];
        cfg.trl           = trl;
        cfg.reref         = 'yes';
        cfg.refchannel    = 'EXG5';

        data = ft_preprocessing(cfg);

        % save the data to disk
        save(['analysis/prepro/data_', cond{c}, '_block', num2str(block)], 'data')
      end
    end

### Artifact rejection

    clear all
    cond = {'Pitch20' 'Pitch40', 'Timbre490', 'Timbre510'};

    % concatenate all trials/blocks
    ipart=1;
    for icond = 1:4
      for iblock = 1:4
        disp(['Loading analysis/prepro/data_', cond{icond}, '_block', num2str(iblock)]);
        load(['analysis/prepro/data_', cond{icond}, '_block', num2str(iblock)], 'data');
        datapart(ipart) = data;
        ipart=ipart+1;
      end
    end

    cfg=[];
    data = ft_appenddata(cfg, datapart(1), datapart(2),datapart(3),datapart(4),datapart(5),datapart(6),datapart(7),datapart(8),datapart(9),datapart(10),datapart(11),datapart(12),datapart(13),datapart(14),datapart(15),datapart(16));
    clear datapart*

    % detect eog artifacts using ICA
    cfg=[];
    cfg.method  = 'runica';
    cfg.channel = 1:160; % EEG channels only
    datacomp = ft_componentanalysis(cfg, data);
    save('analysis/ica/datacomp', 'datacomp')

    % plot the components to detect the artifacts
    figure
    k=1; f=1;
    for icomp=1:length(datacomp.topo)
      if k>20
        k=1;
        figure
      end
      cfg=[];
      cfg.layout = 'biosemi160.lay';
      cfg.xlim   = [icomp icomp];

      subplot(4,5,k);
      ft_topoplotER(cfg, datacomp);
      title(icomp);

      k = k+1;
    end

    % remove components that reflect eog artifacts
    cfg=[];
    cfg.component = [12 49]; % note the exact numbers will vary per run
    data = ft_rejectcomponent(cfg, datacomp);
    save('analysis/data_clean', 'data')

    %% manual artifact rejection

    % remove the mean
    cfg=[];
    cfg.demean = 'yes';
    data = ft_preprocessing(cfg, data);

    % shuffle the trials for non-biased artifact rejection
    shuffle = randperm(length(data.trial));
    datashuff = data;
    for i=1:length(data.trial)
      datashuff.trial{i} = data.trial{shuffle(i)};
      datashuff.time{i}  = data.time{shuffle(i)};
      datashuff.trialinfo(i,:) = data.trialinfo(shuffle(i),:);
    end

    % browse for artifact rejection
    cfg = [];
    cfg.channel = 'EEG';
    cfg.continuous = 'no';
    cfg = ft_databrowser(cfg, data);
    data = ft_rejectartifact(cfg,data);

    % visual artifact rejection in summary mode
    cfg = [];
    cfg.method = 'summary';
    data = ft_rejectvisual(cfg, data);

    % the following trials were removed: 43, 87, 174, 261, 307, 333, 343, 398, 557, 583, 593, 606, 666, 670, 674, 741, 742, 743, 744, 745, 899
    % the following channels were removed: A7, A13, A14, A25, A26, A27, A28, B8, B9, B12, B19, B32, D1, D21, D23, D25, D26, D31, D32, E1, E17, E21, E32

    save('analysis/data_clean', 'data')

### Timelock Analysis

    clear all

    cond = {'Pitch20' 'Pitch40', 'Timbre490', 'Timbre510'};

    load('analysis/data_clean', 'data')

    for icond = 1:4 % loop over the 4 conditions
      for istim = 1:3 % loop over standard-before, deviant, standard-after

        % compute timelocked averages for each condition
        cfg=[];
        cfg.lpfilter   = 'yes';
        cfg.lpfreq     = 40;
        cfg.trials   = find(data.trialinfo(:,3) == icond & data.trialinfo(:,4) == istim);
        timelock{icond,istim} = ft_timelockanalysis(cfg, data);

        % baseline correct
        cfg=[];
        cfg.baseline = [-0.2 0];
        timelock{icond,istim} = ft_timelockbaseline(cfg, timelock{icond,istim});
      end
    end

    save('analysis/timelock/timelock_all','timelock');

    % plot the ERPs over all sensors
    figure
    for i = 1:4
      subplot(2,2,i);
      ft_singleplotER([],timelock{i,1},timelock{i,2},timelock{i,3});
      title(cond{i});
      if i==1
        legend('standard-before', 'deviant', 'standard-after', 'Location', 'NorthWest')
      end
    end
    print(gcf, '-dpng', 'figures/fig1_ERP')

    % plot ERP in interactive mode, only for standard-before
    cfg = [];
    cfg.layout      = 'biosemi160lay.mat';
    cfg.interactive = 'yes';
    figure; ft_multiplotER(cfg,timelock{1,1});

    % compute the contrasts
    for icond = 1:4
      % standard before vs deviant
      stb_vs_dev{icond} = timelock{1,1};
      stb_vs_dev{icond}.avg = timelock{icond,2}.avg - timelock{icond,1}.avg;

      % standard before vs standard after
      stb_vs_sta{icond} = timelock{1,1};
      stb_vs_sta{icond}.avg = timelock{icond,3}.avg - timelock{icond,1 }.avg;

    end

    % plot the contrasts
    figure
    for icond = 1:4
      cfg=[];
      cfg.xlim        = [0.5 7];
      cfg.zlim        = 'maxabs';
      cfg.interactive = 'yes';
      cfg.layout      = 'biosemi160lay.mat';
      cfg.colorbar    = 'yes';

      subplot(2,2,icond);
      ft_topoplotER(cfg, stb_vs_dev{icond});
    end
    print(gcf, '-dpng', 'figures/fig2_ERP')

    figure
    for icond = 1:4
      cfg=[];
      cfg.xlim        = [0.5 7];
      cfg.zlim        = 'maxabs';
      cfg.interactive = 'yes';
      cfg.layout      = 'biosemi160lay.mat';
      cfg.colorbar    = 'yes';

      subplot(2,2,icond);
      ft_topoplotER(cfg, stb_vs_sta{icond});
    end
    print(gcf, '-dpng', 'figures/fig3_ERP')

    %% now collapse

    % compute averages for pitch and timbre
    for istim = 1:3
      cfg=[];
      cfg.lpfilter   = 'yes';
      cfg.lpfreq     = 40;
      cfg.keeptrials = 'yes';
      cfg.trials     = find((data.trialinfo(:,3) == 1 | data.trialinfo(:,3) == 2 ) & data.trialinfo(:,4) == istim);
      timelock_pitch{istim}  = ft_timelockanalysis(cfg, data);

      cfg.trials     = find((data.trialinfo(:,3) == 3 | data.trialinfo(:,3) == 4 ) & data.trialinfo(:,4) == istim);
      timelock_timbre{istim} = ft_timelockanalysis(cfg, data);

      cfg=[];
      cfg.baseline   = [-0.2 0];
      timelock_pitch{istim}  = ft_timelockbaseline(cfg, timelock_pitch{istim});
      timelock_timbre{istim} = ft_timelockbaseline(cfg, timelock_timbre{istim});
    end
    save('analysis/timelock/timelock_avg','timelock_*');

    % plot contrasts
    figure
    subplot(1,2,1);
    ft_singleplotER([],timelock_pitch{1},timelock_pitch{2},timelock_pitch{3});
    title('Pitch');

    subplot(1,2,2);
    ft_singleplotER([],timelock_timbre{1},timelock_timbre{2},timelock_timbre{3});
    title('Timbre');

    print(gcf, '-dpng', 'figures/fig4_ERP')

### Statistics

    cfg               = [];
    cfg.layout        = 'biosemi160lay.mat'; %in meters
    %cfg.layout       = 'elec160.mat'; %in mm
    cfg.neighbourdist = .1;
    cfg.neighbours    = ft_prepare_neighbours(cfg,timelock_pitch{1});

    cfg.latency       = [0 1];
    cfg.parameter     = 'trial';
    cfg.method        = 'montecarlo';
    cfg.design        = [1:size(timelock_pitch{2}.trial,1) 1:size(timelock_pitch{1}.trial,1);
      ones(1,size(timelock_pitch{2}.trial,1)), ones(1,size(timelock_pitch{1}.trial,1))*2];

    cfg.numrandomization = 1000;
    cfg.correctm      = 'cluster';
    cfg.correcttail   = 'prob';
    cfg.ivar          = 2;
    cfg.uvar          = 1;

    cfg.statistic     = 'indepsamplesT';

    stat = ft_timelockstatistics(cfg, timelock_pitch{2}, timelock_pitch{1});

    save('analysis/timelock/stat','stat');

    %% plot

    % cfg=[];
    % cfg.layout = 'biosemi160lay.mat';
    % ft_clusterplot(cfg, stat)

    % find relevant clusters
    ipos = find([stat.posclusters.prob]<=0.05);
    ineg = find([stat.negclusters.prob]<=0.05);

    % loop over all sig positive clusters
    for i=ipos

      cfg=[];
      cfg.highlight = 'on';
      cfg.zparam    = 'stat';
      cfg.layout    = 'biosemi160lay.mat';
      cfg.style     = 'straight';
      cfg.gridscale = 500;

      % find the significant time range for this cluster
      tmp=[];
      for t = 1:length(stat.time)
        if ~isempty(find(any(stat.posclusterslabelmat(:,t)==ipos)))
          tmp = [tmp t];
        end
      end
      cfg.xlim      = [stat.time(tmp(1)) stat.time(tmp(end))];

      % find the channels belonging to this cluster
      cfg.highlightchannel = [];
      for c = 1:length(stat.label)
        if ~isempty(find(any(stat.posclusterslabelmat(c,:)==ipos)))
          cfg.highlightchannel = [cfg.highlightchannel c];
        end
      end

      figure
      ft_topoplotER(cfg, stat);
      title('positive cluster')
      print(gcf, '-dpng', ['figures/fig5_STAT_pos', num2str(i)])
    end

    % loop over all sig negative clusters
    for i=ineg

      cfg=[];
      cfg.highlight = 'on';
      cfg.zparam    = 'stat';
      cfg.layout    = 'biosemi160lay.mat';
      cfg.style     = 'straight';
      cfg.gridscale = 500;

      % find the significant time range for this cluster
      tmp=[];
      for t = 1:length(stat.time)
        if ~isempty(find(any(stat.negclusterslabelmat(:,t)==ineg)))
          tmp = [tmp t];
        end
      end
      cfg.xlim      = [stat.time(tmp(1)) stat.time(tmp(end))];

      % find the channels belonging to this cluster
      cfg.highlightchannel = [];
      for c = 1:length(stat.label)
        if ~isempty(find(any(stat.negclusterslabelmat(c,:)==ineg)))
          cfg.highlightchannel = [cfg.highlightchannel c];
        end
      end

      figure
      ft_topoplotER(cfg, stat);
      title('negative cluster')
      print(gcf, '-dpng', ['figures/fig6_STAT_neg', num2str(i)])
    end

    load analysis/timelock/timelock_all.mat
    load headmodel/standard_mri.mat

    elec = ft_read_sens('elec160.mat');
    vol  = ft_read_headmodel('headmodel/standard_bem.mat');

    figure, ft_plot_headmodel(vol)

    % prepare data
    cfg = [];
    cfg.demean = 'yes';
    cfg.baselinewindow = [-inf 0];
    cfg.reref = 'yes';
    cfg.refchannel = 'all'; % thereby averaging systematic leadfield error over sensors
    for icond = 1 : 4
        for istim = 1 : 3
            timelock{icond,istim} = ft_preprocessing(cfg, timelock{icond,istim});
        end
    end

    % do some averages
    before = timelock{1,1};
    before.trial{1} = (timelock{1,1}.trial{1} + timelock{2,1}.trial{1} + timelock{3,1}.trial{1} + timelock{4,1}.trial{1} ) ./ 4;
    deviant = timelock{1,1};
    deviant.trial{1} = (timelock{1,2}.trial{1} + timelock{2,2}.trial{1} + timelock{3,2}.trial{1} + timelock{4,2}.trial{1} ) ./ 4;
    after = timelock{1,1};
    after.trial{1} = (timelock{1,3}.trial{1} + timelock{2,3}.trial{1} + timelock{3,3}.trial{1} + timelock{4,3}.trial{1} ) ./ 4;

    % plot ERPs
    cfg = [];
    cfg.layout = 'biosemi160lay.mat';
    cfg.interactive = 'yes';
    figure; ft_multiplotER(cfg, before, deviant, after);
    legend;

    % dipole fitting
    cfg = [];
    cfg.headmodel = vol;
    cfg.elec = elec;
    cfg.model = 'regional';
    cfg.numdipoles = 2;
    cfg.latency = [0.080 0.1]; %n100
    cfg.gridsearch = 'yes';
    cfg.resolution = 20; % mm
    cfg.nonlinear = 'yes';
    cfg.symmetry = 'x';
    source = ft_dipolefitting(cfg, before);

    % topoplot ERP
    cfg = [];
    cfg.layout = 'biosemi160lay.mat';
    cfg.zparam = 'Vdata';
    figure; ft_topoplotER(cfg, source);

    % topoplot dipole model
    cfg.zparam = 'Vmodel';
    figure; ft_topoplotER(cfg, source);

    % topoplot difference data with model
    source.Vdifference = source.Vdata ./ source.Vmodel;
    cfg.zparam = 'Vdifference';
    cfg.zlim = [0 2];
    figure; ft_topoplotER(cfg, source);

    % plot first dipole position on mni
    cfg = [];
    cfg.method = 'ortho';
    cfg.location = source.dip.pos(1,:);
    figure; ft_sourceplot(cfg, mri);

    % plot second dipole position on mni
    cfg.location = source.dip.pos(2,:);
    figure; ft_sourceplot(cfg, mri);

    % use dipole positions to extract time course of whole trial
    cfg = source.cfg;
    cfg.dip.pos = source.dip.pos;
    cfg.gridsearch = 'no';
    cfg.nonlinear = 'no';
    cfg.latency = [-inf inf];
    cfg.headmodel = vol;
    cfg.elec = elec;
    source2 = ft_dipolefitting(cfg, before);

    % plot time courses of both dipoles
    figure; hold;
    plot(source2.time, source2.dip.mom(1:3,:), '-')
    plot(source2.time, source2.dip.mom(4:6,:), ':')

    % use Singular Value Decomposition to extract component from all
    % three orientations of first dipole. u = identity matrix, s = scaling, v =
    % signal strength
    [u1, s1, v1] = svd(source2.dip.mom(1:3,:));
    [u2, s2, v2] = svd(source2.dip.mom(4:6,:));
    figure; hold;
    plot(source2.time, v1(:,1));
    plot(source2.time, v2(:,1),':');

    % use Pythagoras to make one dimensional dipole from three orientations
    figure; hold;
    plot(source2.time, sqrt(sum(source2.dip.mom(1:3,:).^2)));
    plot(source2.time, sqrt(sum(source2.dip.mom(4:6,:).^2)),':');
