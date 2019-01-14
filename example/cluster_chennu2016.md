---
# Overview of the tutorial

In this example script we are going to learn how the normalization of the **Power Spectral Density (PSD)** affects the statistics strength and sensitivity. To archive that we will use the **cluster-based nonparametric permutation test** to:

1. Compute a **Multivariate ANOVA**  to test the effect of the
(drug) intervention on the entire EEG spectrum.

2. Compute **within** -participant contrasts

3. Compute **between** -participant contrasts

4. Compute a **2x2 interaction**

5. Compute a **correlation** between a variable and the EEG
spectrum

Set-up paths and define important variables

    if ispc;
      wrkpath = 'C:\Users\diegolozano\Dropbox\wc_chennu\Chennu2016BIDS\';
      addpath(fullfile(wrkpath,'code','pipelines'));
    else
      wrkpath = '/home/dlozano/Dropbox/wc_chennu/Chennu2016BIDS/';
      addpath(fullfile(wrkpath,'code','pipelines'));
    end

    occipital_ROI = {'E50','T5','E59','E60','Pz','E65','E66','E67','O1','E71','E72','Oz','E76','E77','O2','E84','E85','E90','E91','T6','E101','E51','E97'};
    frontal_ROI   = {'E3','E4','E5','E6','E7','Fp2','E10','Fz','E12','E13','E15','E16','E18','E19','E20','Fp1','E23','F3','E27','E28','E29','E30','E105','E106','E111','E112','E117','E118','E123','F4'};

    exp_cond = {...
      '*task-rest_run-1_eeg_freq.mat';...% baseline
      '*task-rest_run-2_eeg_freq.mat';...% mild sedation
      '*task-rest_run-3_eeg_freq.mat';...% moderate sedation
      '*task-rest_run-4_eeg_freq.mat'};  % recovery
    cfg_neigh = load(fullfile(wrkpath,'code','neighbours','cfg_neighbours.mat'));
    folder_dir = dir(fullfile(wrkpath,'derivatives_v2_freq','sub*'));

    % create dummy variables to fill participants and sedative conditions
    [base_sedation,mild_sedation,mode_sedation,reco_sedation]=deal(cell(size(folder_dir,1),1));

    % here we'll add covariates to take into account during stats such as drug concentration, reaction time, correct responses
    cov_labels = {'drug concentration' 'reaction time' 'correct responses'};
    covariates = zeros(size(folder_dir,1),size(exp_cond,1),size(cov_labels,2));

    for subj = 1:size(folder_dir,1);
      dtsv = dir(fullfile(wrkpath,'raw_bids',folder_dir(subj,1).name,'*.tsv'));
      tsv_table = readtable(fullfile(dtsv.folder,dtsv.name), 'FileType', 'text', 'Delimiter', '\t',...
        'ReadVariableNames',1,'ReadRowNames',1,'Format','%s%s%s%f%f%f');

      covariates(subj,:,:)=tsv_table{:,3:5};
      clear tsv_table;
      for f = 1:size(exp_cond,1);
        dmat = dir(fullfile(wrkpath,'derivatives_v2_freq',folder_dir(subj,1).name,'freq',exp_cond{f,1}));
        if     f==1;
          base_sedation{subj,1} = load(fullfile(dmat.folder,dmat.name));
        elseif f==2;
          mild_sedation{subj,1} = load(fullfile(dmat.folder,dmat.name));
        elseif f==3;
          mode_sedation{subj,1} = load(fullfile(dmat.folder,dmat.name));
        elseif f==4;
          reco_sedation{subj,1} = load(fullfile(dmat.folder,dmat.name));
        end
      end
    end

    % here we arrange the data of each condition in a 3D matrix consisting of subj_chan_freq
    cfg = [];
    cfg.keepindividual = 'yes';
    base_sedation = ft_freqgrandaverage(cfg,base_sedation{:});
    mild_sedation = ft_freqgrandaverage(cfg,mild_sedation{:});
    mode_sedation = ft_freqgrandaverage(cfg,mode_sedation{:});
    reco_sedation = ft_freqgrandaverage(cfg,reco_sedation{:});

    % get the numerical indices to compute averages later
    sel_oROI = match_str(base_sedation.label,occipital_ROI);
    sel_fROI = match_str(base_sedation.label,frontal_ROI);

    elec = prepare_elec_chennu2016(base_sedation.label);


# Normalization of the Power Spectral Density (PSD)

**1. Normalize the PSD relative to the mean taken over freq_norm during the SAME sedative state**

     - Pros: you become sensitive to power difference within each sedative
state

     - Cons: denominator is different across sedative states which
difficult the interpretation of results. Are differences in PSD
because the numerator or the denominator?
    ~~~~
    freq_oi   = [8 12]; % frequency range to display averages
    freq_norm = [0.7 40]; % frequency range used to normalize the spectrum
    foi      = nearest(base_sedation.freq,freq_oi);
    foi_norm = nearest(base_sedation.freq,freq_norm);

    base_sedation.powspctrm_w = bsxfun(@rdivide, base_sedation.powspctrm, mean(base_sedation.powspctrm(:,:,foi_norm(1):foi_norm(2)),3));
    mild_sedation.powspctrm_w = bsxfun(@rdivide, mild_sedation.powspctrm, mean(mild_sedation.powspctrm(:,:,foi_norm(1):foi_norm(2)),3));
    mode_sedation.powspctrm_w = bsxfun(@rdivide, mode_sedation.powspctrm, mean(mode_sedation.powspctrm(:,:,foi_norm(1):foi_norm(2)),3));
    reco_sedation.powspctrm_w = bsxfun(@rdivide, reco_sedation.powspctrm, mean(reco_sedation.powspctrm(:,:,foi_norm(1):foi_norm(2)),3));'
    ~~~~

**2. Normalize the PSD to the mean taken over freq_norm during BASELINE sedative state**

     - Pros: the **demonimator** is the same for all sessions which facilitates comparisons

     - Cons: if baseline is biased, all our estimates will be biased

~~~~
    common_denominator = mean(base_sedation.powspctrm(:,:,foi_norm(1):foi_norm(2)),3);
    base_sedation.powspctrm_b = bsxfun(@rdivide, base_sedation.powspctrm, common_denominator); %repmat(mean(base_sedation.powspctrm,3),1,1,90);
    mild_sedation.powspctrm_b = bsxfun(@rdivide, mild_sedation.powspctrm, common_denominator);
    mode_sedation.powspctrm_b = bsxfun(@rdivide, mode_sedation.powspctrm, common_denominator);
    reco_sedation.powspctrm_b = bsxfun(@rdivide, reco_sedation.powspctrm, common_denominator);

    % To simplify the results, let's collapse the data using the ROIs and frequency ranges defined in the paper
    cfg = [];
    cfg.channel     = frontal_ROI;
    cfg.avgoverchan = 'yes';
    cfg.foi         = freq_oi;
    cfg.avgoverfreq = 'yes';
    cfg.parameter   = {'powspctrm','powspctrm_w','powspctrm_b'};
    base_sedation_fROI = ft_selectdata(cfg,base_sedation);
    mild_sedation_fROI = ft_selectdata(cfg,mild_sedation);
    mode_sedation_fROI = ft_selectdata(cfg,mode_sedation);
    reco_sedation_fROI = ft_selectdata(cfg,reco_sedation);

    cfg.channel     = occipital_ROI;
    base_sedation_oROI = ft_selectdata(cfg,base_sedation);
    mild_sedation_oROI = ft_selectdata(cfg,mild_sedation);
    mode_sedation_oROI = ft_selectdata(cfg,mode_sedation);
    reco_sedation_oROI = ft_selectdata(cfg,reco_sedation);

    % collect the data to plot it using plotSpread
    data_raw_fROI    = {base_sedation_fROI.powspctrm...
                        mild_sedation_fROI.powspctrm...
                        mode_sedation_fROI.powspctrm...
                        reco_sedation_fROI.powspctrm};
    data_raw_oROI    = {base_sedation_oROI.powspctrm...
                        mild_sedation_oROI.powspctrm...
                        mode_sedation_oROI.powspctrm...
                        reco_sedation_oROI.powspctrm};

    data_within_fROI = {base_sedation_fROI.powspctrm_w...
                        mild_sedation_fROI.powspctrm_w...
                        mode_sedation_fROI.powspctrm_w...
                        reco_sedation_fROI.powspctrm_w};
    data_within_oROI = {base_sedation_oROI.powspctrm_w...
                        mild_sedation_oROI.powspctrm_w...
                        mode_sedation_oROI.powspctrm_w...
                        reco_sedation_oROI.powspctrm_w};

    data_between_fROI ={base_sedation_fROI.powspctrm_b...
                        mild_sedation_fROI.powspctrm_b...
                        mode_sedation_fROI.powspctrm_b...
                        reco_sedation_fROI.powspctrm_b};
    data_between_oROI ={base_sedation_oROI.powspctrm_b...
                        mild_sedation_oROI.powspctrm_b...
                        mode_sedation_oROI.powspctrm_b...
                        reco_sedation_oROI.powspctrm_b};

    figure('Position',[30 197 1281 420]);
    subplot(231);
    plotSpread(data_raw_fROI,[],[],{'baseline','mild','moderate','recovery'});ylabel('abs. power (V^2)');
    title('raw PSD Front');
    subplot(232);
    h2 = plotSpread(data_within_fROI,[],[],{'baseline','mild','moderate','recovery'});ylabel('rel. power');
    title('within PSD Front');
    set(h2{1},'LineWidth',1,'Marker', '.','Color','r','MarkerFaceColor','r')
    subplot(233);
    h3 = plotSpread(data_between_fROI,[],[],{'baseline','mild','moderate','recovery'});ylabel('rel. power');
    title('between PSD Front');
    set(h3{1},'LineWidth',1,'Marker', '.','Color','k','MarkerFaceColor','k')

    subplot(234);
    plotSpread(data_raw_oROI,[],[],{'baseline','mild','moderate','recovery'});ylabel('abs. power (V^2)');
    title('raw PSD Occip');
    subplot(235);
    h5 = plotSpread(data_within_oROI,[],[],{'baseline','mild','moderate','recovery'});ylabel('rel. power');
    title('within PSD Occip');
    set(h5{1},'LineWidth',1,'Marker', '.','Color','r','MarkerFaceColor','r')
    subplot(236);
    h6 = plotSpread(data_between_oROI,[],[],{'baseline','mild','moderate','recovery'});ylabel('rel. power');
    title('between PSD Occip');
    set(h6{1},'LineWidth',1,'Marker', '.','Color','k','MarkerFaceColor','k')

    {% include markup/warning %}
    **QUESTION 1**:
    why in the between session normalization all participants are clustered around value 1?
    Lead: if you plot the alpha power as a function of the total spectrum power, what type of relationship do you see?
    {% include markup/end %}

    % let's make topoplots and the PSD for each ROI for each sedative condition (similar to Fig 5A in Chennu et al.,)
    cfg = [];
    cfg.elec             = elec;
    cfg.parameter        = 'powspctrm_b'; % you can test any of the subfields: powspctrm, powspctrm_w, powspctrm_b
    cfg.xlim             = [8 15]; % frequency range to make the topoplot
    cfg.highlight        = 'on';
    % here the figure cosmetics
    cfg.highlightchannel = {frontal_ROI occipital_ROI};
    cfg.highlightsymbol  = {'o','*'};
    cfg.highlightcolor   = [0 0 0];
    cfg.highlightsize    = 6;
    cfg.markersymbol     = '.';
    cfg.comment          = 'no';
    cfg.colormap         = 'jet';

    figure('position',[680 240 1039 420]);
    subplot(241);ft_topoplotER(cfg,base_sedation);colorbar;title('baseline');
    subplot(242);ft_topoplotER(cfg,mild_sedation);colorbar;title('mild');
    subplot(243);ft_topoplotER(cfg,mode_sedation);colorbar;title('moderate');
    subplot(244);ft_topoplotER(cfg,reco_sedation);colorbar;title('recovery');

    subplot(245);loglog(base_sedation.freq,...
      [squeeze(mean(mean(base_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
       squeeze(mean(mean(base_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    legend('Front ROI','Occip ROI','Location','southwest');
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('baseline');

    subplot(246);loglog(mild_sedation.freq,...
      [squeeze(mean(mean(mild_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
       squeeze(mean(mean(mild_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('mild');

    subplot(247);loglog(mode_sedation.freq,...
      [squeeze(mean(mean(mode_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
       squeeze(mean(mean(mode_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('moderate');

    subplot(248);loglog(reco_sedation.freq,...
      [squeeze(mean(mean(reco_sedation.(cfg.parameter)(:,sel_fROI,:),2),1))...
       squeeze(mean(mean(reco_sedation.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('recovery');
~~~~

<div class="note"></div>   
**QUESTION 2**: There's a participant in the dataset with an extreme power value: Can you find it?

~~~~
figure; plot(base_sedation.freq,...
    [squeeze(base_sedation.powspctrm_b(participant_outlier,outlier_chans,:))...
    squeeze(mild_sedation.powspctrm_b(participant_outlier,outlier_chans,:))...
    squeeze(mode_sedation.powspctrm_b(participant_outlier,outlier_chans,:))...
    squeeze(reco_sedation.powspctrm_b(subj,outlier_chans,:))]);
    participants = [1:20];
    participants(participant_outlier) = [];

    cfg = [];
    cfg.trials    = participants;% cfg.trials will select the 'subj' dimension
    cfg.parameter = {'powspctrm','powspctrm_w','powspctrm_b'};
    base_sedation_out = ft_selectdata(cfg,base_sedation);
    mild_sedation_out = ft_selectdata(cfg,mild_sedation);
    mode_sedation_out = ft_selectdata(cfg,mode_sedation);
    reco_sedation_out = ft_selectdata(cfg,reco_sedation);
~~~~

# CONTRAST 1: main effect of drug

    foi_contrast = [0.5 30];

    cfg = [];
    cfg.channel          = 'all';
    cfg.frequency        = foi_contrast;
    cfg.avgovergfreq     = 'no';
    cfg.parameter        = 'powspctrm_b';
    cfg.method           = 'ft_statistics_montecarlo';
    cfg.statistic        = 'ft_statfun_depsamplesFmultivariate';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';%'maxsum', 'maxsize', 'wcm'
    cfg.clusterthreshold = 'nonparametric_common';
    cfg.minnbchan        = 2;
    cfg.tail             = 1; % For a F-statistic, it only make sense to calculate the right tail
    cfg.clustertail      = cfg.tail;
    cfg.alpha            = 0.05;
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 500;
    cfg.neighbours       = cfg_neigh.neighbours;

    % outlier included
    subj = size(folder_dir,1);
    design = zeros(2,4*subj);
    design(1,1:subj)          = 1;
    design(1,subj+1:2*subj)   = 2;
    design(1,subj*2+1:3*subj) = 3;
    design(1,subj*3+1:4*subj) = 4;
    design(2,:) = repmat(1:subj,1,4);

    cfg.design = design;
    cfg.ivar   = 1;
    cfg.uvar   = 2;
    stat1a = ft_freqstatistics(cfg, base_sedation,mild_sedation,mode_sedation,reco_sedation);

    % outlier excluded
    subj = size(participants,2);
    design = zeros(2,4*subj);
    design(1,1:subj)          = 1;
    design(1,subj+1:2*subj)   = 2;
    design(1,subj*2+1:3*subj) = 3;
    design(1,subj*3+1:4*subj) = 4;
    design(2,:)               = repmat(1:subj,1,4);
    cfg.design = design;

    stat1b = ft_freqstatistics(cfg, base_sedation_out,mild_sedation_out,mode_sedation_out,reco_sedation_out);

    % run averages
    cfg = [];
    cfg.foilim     = foi_contrast;
    cfg.avgoverrpt = 'yes';
    cfg.parameter  = {'powspctrm','powspctrm_w','powspctrm_b'};
    base_sedation_avg = ft_selectdata(cfg,base_sedation);
    mild_sedation_avg = ft_selectdata(cfg,mild_sedation);
    mode_sedation_avg = ft_selectdata(cfg,mode_sedation);
    reco_sedation_avg = ft_selectdata(cfg,reco_sedation);
    base_sedation_out_avg = ft_selectdata(cfg,base_sedation_out);
    mild_sedation_out_avg = ft_selectdata(cfg,mild_sedation_out);
    mode_sedation_out_avg = ft_selectdata(cfg,mode_sedation_out);
    reco_sedation_out_avg = ft_selectdata(cfg,reco_sedation_out);

    base_sedation_avg.mask = stat1a.mask;
    mild_sedation_avg.mask = stat1a.mask;
    mode_sedation_avg.mask = stat1a.mask;
    reco_sedation_avg.mask = stat1a.mask;
    base_sedation_out_avg.mask = stat1b.mask;
    mild_sedation_out_avg.mask = stat1b.mask;
    mode_sedation_out_avg.mask = stat1b.mask;
    reco_sedation_out_avg.mask = stat1b.mask;

    cfg = [];
    cfg.zlim        = [0 90];
    cfg.elec          = elec;
    cfg.colorbar      = 'no';
    cfg.maskparameter = 'mask';  % use the thresholded probability to mask the data
    cfg.maskstyle     = 'box';
    cfg.parameter     = 'powspctrm_b';
    cfg.maskfacealpha = 0.1;
    figure;ft_multiplotER(cfg,base_sedation_avg,mild_sedation_avg,mode_sedation_avg,reco_sedation_avg)
    figure;ft_multiplotER(cfg,base_sedation_out_avg,mild_sedation_out_avg,mode_sedation_out_avg,reco_sedation_out_avg)


# CONTRAST 2: within-participant BASELINE vs MODERATE sedation comparison

    cfg = [];
    cfg.channel          = 'all';
    cfg.frequency        = foi_contrast;
    cfg.parameter        = 'powspctrm_w';
    cfg.method           = 'ft_statistics_montecarlo';
    cfg.statistic        = 'ft_statfun_depsamplesT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.clusterthreshold = 'nonparametric_common';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = cfg.tail;
    cfg.alpha            = 0.05;
    cfg.correcttail      = 'alpha';
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 500;
    cfg.neighbours       = cfg_neigh.neighbours;

    subj = size(folder_dir,1);
    design = zeros(2,2*subj);
    design(1,1:subj)        = 1;
    design(1,subj+1:2*subj) = 2;
    design(2,1:subj)        = 1:subj;
    design(2,subj+1:2*subj) = 1:subj;

    cfg.design = design;
    cfg.ivar     = 1;
    cfg.uvar     = 2;
    stat2 = ft_freqstatistics(cfg, base_sedation, mode_sedation);

    % get the 1st positive and negative cluster
    sigposmask = (stat2.posclusterslabelmat==1) & stat2.mask;
    signegmask = (stat2.negclusterslabelmat==1) & stat2.mask;

    % choose the cluster you want to see: POSITIVE or NEGATIVE
    base_sedation_avg.mask = signegmask;
    mode_sedation_avg.mask = signegmask;

    cfg = [];
    cfg.elec          = elec;
    cfg.colorbar      = 'no';
    cfg.maskparameter = 'mask';  % use the thresholded probability to mask the data
    cfg.maskstyle     = 'box';
    cfg.parameter     = 'powspctrm_w';
    cfg.maskfacealpha = 0.5;
    figure;ft_multiplotER(cfg,base_sedation_avg,mode_sedation_avg);



# CONTRAST 3: between-participants RESPONSIVE vs DROWSY comparison
first we compute the hit rate of each participant and condition knowing
that the number of correct responses in that task is 40. See point 5) in
https://www.repository.cam.ac.uk/handle/1810/252736

    hit_rate = (covariates(:,:,3)./40).*100;

Chennu et al 2016 made a proper behavioral analysis to detect the drowsy
group. Here we just used to select arbitrarily 70% threshold to match Figure 1B

    drowsy_group = find(hit_rate(:,3)<70);
    respon_group = setxor(1:size(folder_dir,1),drowsy_group);

    figure;
    plot(hit_rate(respon_group,:)','-^b','MarkerFaceColor','b');
    hold on;
    plot(hit_rate(drowsy_group,:)','marker','^','color',[0 0.5 0],'MarkerFaceColor',[0 0.5 0])
    hold off;
    ylabel('Perceptual hit rate (%)');
    set(gca,'XTickLabel',{'baseline','','mild','','moderate','','recovery'});

    % copy the datasets and select the relevant subgroups
    [base_sedation_respon base_sedation_drowsy]=deal(base_sedation);
    [mild_sedation_respon mild_sedation_drowsy]=deal(mild_sedation);
    [mode_sedation_respon mode_sedation_drowsy]=deal(mode_sedation);
    [reco_sedation_respon reco_sedation_drowsy]=deal(reco_sedation);

    cfg = [];
    cfg.trials = respon_group; % cfg.trials will select the 'subj' dimension
    cfg.parameter   = {'powspctrm','powspctrm_w','powspctrm_b'};
    base_sedation_respon = ft_selectdata(cfg,base_sedation_respon);
    mild_sedation_respon = ft_selectdata(cfg,mild_sedation_respon);
    mode_sedation_respon = ft_selectdata(cfg,mode_sedation_respon);
    reco_sedation_respon = ft_selectdata(cfg,reco_sedation_respon);

    cfg.trials = drowsy_group;
    base_sedation_drowsy = ft_selectdata(cfg,base_sedation_drowsy);
    mild_sedation_drowsy = ft_selectdata(cfg,mild_sedation_drowsy);
    mode_sedation_drowsy = ft_selectdata(cfg,mode_sedation_drowsy);
    reco_sedation_drowsy = ft_selectdata(cfg,reco_sedation_drowsy);
    cfg = [];
    cfg.channel          = 'all';
    cfg.frequency        = foi_contrast;
    cfg.avgovergfreq     = 'no';
    cfg.parameter        = 'powspctrm_w';
    cfg.method           = 'ft_statistics_montecarlo';
    cfg.statistic        = 'ft_statfun_indepsamplesT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.clusterthreshold = 'nonparametric_common';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = cfg.tail;
    cfg.alpha            = 0.05;
    cfg.correcttail      = 'alpha';
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 500;
    cfg.neighbours       = cfg_neigh.neighbours;

    design = zeros(1,size(respon_group,1) + size(drowsy_group,1));
    design(1,1:size(respon_group,1)) = 1;
    design(1,(size(respon_group,1)+1):(size(respon_group,1)+size(drowsy_group,1))) = 2;

    cfg.design = design;
    cfg.ivar   = 1;

    stat3 = ft_freqstatistics(cfg, mode_sedation_respon,mode_sedation_drowsy);

    cfg = [];
    cfg.alpha  = stat3.cfg.alpha;
    cfg.parameter = 'stat';
    cfg.zlim   = [-3 3];
    cfg.elec = elec;
    ft_clusterplot(cfg, stat3);


    cfg = [];
    cfg.elec = elec;
    cfg.zlim = [1.5 3];
    cfg.xlim = [8 15];
    cfg.parameter = 'powspctrm_w';
    cfg.markersymbol = '.';
    cfg.comment = 'no';
    cfg.colormap = 'jet';
    cfg.colorbar = 'no';

    figure('position',[680 240 1039 420]);
    subplot(241);ft_topoplotER(cfg,base_sedation_respon);colorbar;title('base Responsive');
    subplot(242);ft_topoplotER(cfg,mild_sedation_respon);colorbar;title('mild Responsive');
    subplot(243);ft_topoplotER(cfg,mode_sedation_respon);colorbar;title('mode Responsive');
    subplot(244);ft_topoplotER(cfg,reco_sedation_respon);colorbar;title('reco Responsive');

    subplot(245);ft_topoplotER(cfg,base_sedation_drowsy);colorbar;title('base Drowsy');
    subplot(246);ft_topoplotER(cfg,mild_sedation_drowsy);colorbar;title('mild Drowsy');
    subplot(247);ft_topoplotER(cfg,mode_sedation_drowsy);colorbar;title('mode Drowsy');
    subplot(248);ft_topoplotER(cfg,reco_sedation_drowsy);colorbar;title('reco Drowsy');

PSDs for each group separately as a function of sedative state

    figure('position',[680 240 1039 420]);
    subplot(241);loglog(base_sedation_respon.freq,...
      [squeeze(mean(mean(base_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
       squeeze(mean(mean(base_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    legend('Front ROI resp','Front ROI drow','Location','southwest');
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('baseline');

    subplot(242);loglog(mild_sedation_respon.freq,...
      [squeeze(mean(mean(mild_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
       squeeze(mean(mean(mild_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('mild');

    subplot(243);loglog(mode_sedation_respon.freq,...
      [squeeze(mean(mean(mode_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
       squeeze(mean(mean(mode_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('moderate');

    subplot(244);loglog(reco_sedation_respon.freq,...
      [squeeze(mean(mean(reco_sedation_respon.(cfg.parameter)(:,sel_fROI,:),2),1))...
       squeeze(mean(mean(reco_sedation_drowsy.(cfg.parameter)(:,sel_fROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    title('recover');

    % PSDs from occipital ROI
    subplot(245);loglog(base_sedation_respon.freq,...
      [squeeze(mean(mean(base_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
       squeeze(mean(mean(base_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);
    legend('Occip ROI resp','Occip ROI drow','Location','southwest');

    subplot(246);loglog(mild_sedation_respon.freq,...
      [squeeze(mean(mean(mild_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
       squeeze(mean(mean(mild_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);

    subplot(247);loglog(mode_sedation_respon.freq,...
      [squeeze(mean(mean(mode_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
       squeeze(mean(mean(mode_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);

    subplot(248);loglog(reco_sedation_respon.freq,...
      [squeeze(mean(mean(reco_sedation_respon.(cfg.parameter)(:,sel_oROI,:),2),1))...
       squeeze(mean(mean(reco_sedation_drowsy.(cfg.parameter)(:,sel_oROI,:),2),1))]);
    xlim([0.5 45]);grid on;hold on;plot([10,10],[10^-3 10^2],'--k')
    ylim([10^-3 10^2]);
    xlabel('Frequency (Hz)');
    ylabel(cfg.parameter);


# CONTRAST 4: 2x2 INTERACTION between SEDATION (baseline vs moderate) and GROUP (responsive vs drowsy)

Now we compute the within-participant contrast: baseline vs moderate sedative state for each participant in each group

    cfg = [];
    cfg.parameter = {'powspctrm','powspctrm_w','powspctrm_b'};
    cfg.operation = 'subtract';
    sedation_respon_d = ft_math(cfg,base_sedation_respon,mode_sedation_respon);
    sedation_drowsy_d = ft_math(cfg,base_sedation_drowsy,mode_sedation_drowsy);

Finally we compute the interaction:

    cfg = [];
    cfg.channel          = 'all';
    cfg.frequency        = foi_contrast;
    cfg.avgovergfreq     = 'no';
    cfg.parameter        = 'powspctrm_w';
    cfg.method           = 'ft_statistics_montecarlo';
    cfg.statistic        = 'ft_statfun_indepsamplesT';
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsum';
    cfg.clusterthreshold = 'nonparametric_common';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = cfg.tail;
    cfg.alpha            = 0.05;
    cfg.correcttail      = 'alpha';
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 1000;
    cfg.neighbours       = cfg_neigh.neighbours;

    design = zeros(1,size(respon_group,1) + size(drowsy_group,1));
    design(1,1:size(respon_group,1)) = 1;
    design(1,(size(respon_group,1)+1):(size(respon_group,1)+size(drowsy_group,1))) = 2;

    cfg.design = design;
    cfg.ivar   = 1;

    stat4 = ft_freqstatistics(cfg, sedation_respon_d, sedation_drowsy_d);

    cfg = [];
    cfg.alpha  = stat4.cfg.alpha;
    cfg.parameter = 'stat';
    cfg.zlim   = [-4 4];
    cfg.elec = elec;
    figure('position',[680 245 874 730]);
    ft_clusterplot(cfg, stat4);


# CONTRAST 5: correlation between a covariate (drug dosage) and brain activity

    cfg = [];
    cfg.channel          = 'all';
    cfg.frequency        = [8 30]; % let's test alpha and low beta bands
    cfg.avgoverfreq      = 'no';
    cfg.avgoverchan      = 'no';
    cfg.parameter        = 'powspctrm_b';
    cfg.method           = 'ft_statistics_montecarlo';
    cfg.statistic        = 'ft_statfun_correlationT';
    cfg.type             = 'spearman'; % type of the correlation (see help corr to know other types)
    cfg.correctm         = 'cluster';
    cfg.clusteralpha     = 0.05;
    cfg.clusterstatistic = 'maxsize';
    cfg.clusterthreshold = 'nonparametric_individual';
    cfg.minnbchan        = 2;
    cfg.tail             = 0;
    cfg.clustertail      = 0;
    cfg.alpha            = 0.05;
    cfg.correcttail      = 'alpha';
    cfg.computeprob      = 'yes';
    cfg.numrandomization = 1000;
    cfg.neighbours       = cfg_neigh.neighbours;

    subj = size(mode_sedation.powspctrm,1);
    design = zeros(1,subj);

    % {'drug concentration' 'reaction time' 'correct responses'};
    design(1,:) = covariates(:,3,1)./1000;
    cfg.design = design;
    cfg.ivar     = 1;

    stat5 = ft_freqstatistics(cfg,mode_sedation);

    cfg = [];
    cfg.alpha  = stat5.cfg.alpha;
    cfg.parameter = 'stat';
    cfg.zlim   = [-3 3];
    cfg.elec = elec;
    ft_clusterplot(cfg,stat5);

Now select the significant sensors and frequencies and  plot the interaction

    % get the 1st positive and negative cluster
    signegmask = (stat4.negclusterslabelmat==1) & stat4.mask;
    % pool all channels and frequencies that in the cluster
    chanoineg = match_str(stat4.label,stat4.label(sum(signegmask,2) > 0));
    foilimneg = stat4.freq(sum(signegmask,1) > 0);
    foilim = [min(foilimneg) max(foilimneg)];

    % choose the cluster you want to see
    base_sedation_avg.mask = signegmask;
    mode_sedation_avg.mask = signegmask;

    cfg = [];
    cfg.foilim      = foilim;
    cfg.avgoverfreq = 'yes';
    cfg.channel     = chanoineg;
    cfg.avgoverchan = 'yes';
    cfg.parameter   = {'powspctrm','powspctrm_w','powspctrm_b'};
    b_r = ft_selectdata(cfg,base_sedation_respon);
    m_r = ft_selectdata(cfg,mode_sedation_respon);
    b_d = ft_selectdata(cfg,base_sedation_drowsy);
    m_d = ft_selectdata(cfg,mode_sedation_drowsy);

    % compute confidence intervals:
    parameter = 'powspctrm_w';%make sure this 'parameter' is the same as the one you used in cfg.parameter in ft_freqstatistics
    ci_b_r = bootci(1000,{@mean b_r.(parameter)},'alpha',0.05);
    ci_m_r = bootci(1000,{@mean,m_r.(parameter)},'alpha',0.05);
    ci_b_d = bootci(1000,{@mean,b_d.(parameter)},'alpha',0.05);
    ci_m_d = bootci(1000,{@mean,m_d.(parameter)},'alpha',0.05);

    % compute means
    x_b_r = mean(b_r.(parameter),1);
    x_m_r = mean(m_r.(parameter),1);
    x_b_d = mean(b_d.(parameter),1);
    x_m_d = mean(m_d.(parameter),1);

    % and the standard error of the mean
    sem_b_r = sem(b_r.(parameter),1);
    sem_m_r = sem(m_r.(parameter),1);
    sem_b_d = sem(b_d.(parameter),1);
    sem_m_d = sem(m_d.(parameter),1);


    figure('position',[145   246   818   420]);
    subplot(121);errorbar([1 2],[x_b_r,x_m_r]',[ci_b_r(1),ci_m_r(1)],[ci_b_r(2),ci_m_r(2)],'-rs');
    ylabel(parameter);
    hold all
    subplot(121);errorbar([1 2],[x_b_d x_m_d]',[ci_b_r(1),ci_m_r(1)],[ci_b_r(1),ci_m_r(1)],'-bs');
    ylabel(parameter);
    xlim([0 3]);
    ylim([-0.5 1.5]);
    title('interaction with 95% C.I.')
    set(gca,'XTickLabel',{'','','baseline','','moderate','',''});
    legend('Responsive','Drowsy','Location','northwest');

    subplot(122);errorbar([1 2],[x_b_r,x_m_r]',[sem_b_r,sem_m_r(1)],'-rs');
    ylabel(parameter);
    hold all
    subplot(122);errorbar([1 2],[x_b_d x_m_d]',[sem_b_r,sem_m_r],'-bs');
    ylabel(parameter);
    xlim([0 3]);
    ylim([-0.5 1.5]);
    title('interaction with SEM')
    set(gca,'XTickLabel',{'','','baseline','','moderate','',''});


# HOMEWORK:
INTERACTION between GROUP (RESPONSIVE vs DROWSY) and ROI (Frontal vs Occipital)

Here the fists steps. Prepare the data

    cfg = [];
    cfg.channel     = frontal_ROI;
    cfg.avgoverchan = 'yes';
    cfg.parameter   = {'powspctrm','powspctrm_w','powspctrm_b'};

select FRONTAL ROI in RESPONSIVE group

    base_sedation_respon_fROI = ft_selectdata(cfg,base_sedation_respon);
    mild_sedation_respon_fROI = ft_selectdata(cfg,mild_sedation_respon);
    mode_sedation_respon_fROI = ft_selectdata(cfg,mode_sedation_respon);
    reco_sedation_respon_fROI = ft_selectdata(cfg,reco_sedation_respon);

select FRONTAL ROI in DROWSY group

    base_sedation_drowsy_fROI = ft_selectdata(cfg,base_sedation_drowsy);
    mild_sedation_drowsy_fROI = ft_selectdata(cfg,mild_sedation_drowsy);
    mode_sedation_drowsy_fROI = ft_selectdata(cfg,mode_sedation_drowsy);
    reco_sedation_drowsy_fROI = ft_selectdata(cfg,reco_sedation_drowsy);

    cfg.channel     = occipital_ROI;

select OCCIPITAL ROI in RESPONSIVE group

    % here we just delete the channel names to avoid  problems using ft_math below
    base_sedation_respon_oROI = ft_selectdata(cfg,base_sedation_respon);base_sedation_respon_oROI.label=base_sedation_respon_fROI.label;
    mild_sedation_respon_oROI = ft_selectdata(cfg,mild_sedation_respon);mild_sedation_respon_oROI.label=base_sedation_respon_fROI.label;
    mode_sedation_respon_oROI = ft_selectdata(cfg,mode_sedation_respon);mode_sedation_respon_oROI.label=base_sedation_respon_fROI.label;
    reco_sedation_respon_oROI = ft_selectdata(cfg,reco_sedation_respon);reco_sedation_respon_oROI.label=base_sedation_respon_fROI.label;


select frontal ROI in DROWSY group

    base_sedation_drowsy_oROI = ft_selectdata(cfg,base_sedation_drowsy);base_sedation_drowsy_oROI.label=base_sedation_respon_fROI.label;
    mild_sedation_drowsy_oROI = ft_selectdata(cfg,mild_sedation_drowsy);mild_sedation_drowsy_oROI.label=base_sedation_respon_fROI.label;
    mode_sedation_drowsy_oROI = ft_selectdata(cfg,mode_sedation_drowsy);mode_sedation_drowsy_oROI.label=base_sedation_respon_fROI.label;
    reco_sedation_drowsy_oROI = ft_selectdata(cfg,reco_sedation_drowsy);reco_sedation_drowsy_oROI.label=base_sedation_respon_fROI.label;


Now we compute the within-participant contrast: frontral vs occipital ROI for each participant in each group

    cfg = [];
    cfg.parameter = {'powspctrm','powspctrm_w','powspctrm_b'};
    cfg.operation = 'subtract';

ROI contrast in RESPONSIVE group

    base_sedation_respon_dROI = ft_math(cfg,base_sedation_respon_fROI,base_sedation_respon_oROI);
    mild_sedation_respon_dROI = ft_math(cfg,mild_sedation_respon_fROI,mild_sedation_respon_oROI);
    mode_sedation_respon_dROI = ft_math(cfg,mode_sedation_respon_fROI,mode_sedation_respon_oROI);
    reco_sedation_respon_dROI = ft_math(cfg,reco_sedation_respon_fROI,reco_sedation_respon_oROI);

ROI contrast in DROWSY group

    base_sedation_drowsy_dROI = ft_math(cfg,base_sedation_drowsy_fROI,base_sedation_drowsy_oROI);
    mild_sedation_drowsy_dROI = ft_math(cfg,mild_sedation_drowsy_fROI,mild_sedation_drowsy_oROI);
    mode_sedation_drowsy_dROI = ft_math(cfg,mode_sedation_drowsy_fROI,mode_sedation_drowsy_oROI);
    reco_sedation_drowsy_dROI = ft_math(cfg,reco_sedation_drowsy_fROI,reco_sedation_drowsy_oROI);

From here on it's your duty...

# Extra POINT:
Does the INTERACTION correlate with any of the covariates?
