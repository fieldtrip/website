---
title: Apply non-parametric statistics with clustering on TFRs of power that were computed with BESA
parent: Statistical analysis
grand_parent: Examples
category: example
tags: [statistics, freq, cluster]
redirect_from:
    - /example/apply_clusterrandanalysis_on_tfrs_of_power_that_were_computed_with_besa/
    - /example/stats_besa/
---

# Apply non-parametric statistics with clustering on TFRs of power that were computed with BESA

    % this is the list of BESA data files in one condition
    filename_ld = {
      'AM_LD_ERA.tfc'
      'CGi_LD_ERA.tfc'
      'DK_LD_ERA.tfc'
      'ES_LD_ERA.tfc'
      'HK_LD_ERA.tfc'
      'JS_LD_ERA.tfc'
      'LJ_LD_ERA.tfc'
      'LPO_LD_ERA.tfc'
      'PP_LD_ERA.tfc'
      'SH_LD_ERA.tfc'
      };

    % this is the list of BESA data files in the other condition
    filename_sd = {
      'AM_SD_ERA.tfc'
      'CGi_SD_ERA.tfc'
      'DK_SD_ERA.tfc'
      'ES_SD_ERA.tfc'
      'HK_SD_ERA.tfc'
      'JS_SD_ERA.tfc'
      'LJ_SD_ERA.tfc'
      'LPO_SD_ERA.tfc'
      'PP_SD_ERA.tfc'
      'SH_SD_ERA.tfc'
      };

    nsubj = length(filename_ld);

    % collect all single subject data in a convenient cell-array
    for i=1:nsubj
      ld{i} = besa2fieldtrip(filename_ld{i});
      sd{i} = besa2fieldtrip(filename_sd{i});
    end

    % this is needed for the channel labels in the data from Peter Praamstra
    % MATLAB is case sensitive and we want the channel and electrode names to match
    for i=1:nsubj
      for j=1:length(ld{i}.label)
        if ld{i}.label{j}(end)=='H'
          ld{i}.label{j}(end)='h';
        end
      end
      for j=1:length(sd{i}.label)
        if sd{i}.label{j}(end)=='H'
          sd{i}.label{j}(end)='h';
        end
      end
    end

    % load a set of electrodes (these are on a unit sphere)
    % note, this will be different for your own data
    load('elec128.mat');
    % scale the electrodes to a realistic head size (in cm)
    elec.pnt = 10*elec.pnt;

    % compute the grand average for both conditions
    cfg = [];
    ldavg = ft_freqgrandaverage(cfg, ld{:});
    sdavg = ft_freqgrandaverage(cfg, sd{:});

    % make a dummy structure with the difference between ld and sd
    avgdif = ldavg;
    avgdif.powspctrm = ldavg.powspctrm - sdavg.powspctrm;

    % make some figures
    cfg = [];
    cfg.layout = elec;
    figure; ft_multiplotTFR(cfg, sdavg);
    figure; ft_multiplotTFR(cfg, ldavg);
    figure; ft_multiplotTFR(cfg, avgdif);

    % perform the statistical test using randomization and a clustering approach
    % using the ft_freqstatistics function
    cfg = [];
    cfg.elec             = elec;
    cfg.neighbourdist    = 4;
    cfg.latency          = 'all';
    cfg.frequency        = 'all';
    cfg.channel          = 'EEG1010' % see FT_CHANNELSELECTION
    cfg.avgovertime      = 'no';
    cfg.avgoverfreq      = 'no';
    cfg.avgoverchan      = 'no';
    cfg.statistic        = 'ft_statfun_depsamplesT';
    cfg.numrandomization = 200;
    cfg.correctm         = 'cluster';
    cfg.method           = 'montecarlo';
    cfg.design           = [
      1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10     % subject number
      1 1 1 1 1 1 1 1 1 1  2 2 2 2 2 2 2 2 2 2  ];  % condition number
    cfg.uvar = 1;                                   % "subject" is unit of observation
    cfg.ivar = 2;                                   % "condition" is the independent variable
    stat = ft_freqstatistics(cfg, ld{:}, sd{:});
