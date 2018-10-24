---
layout: default
tags: example statistics
---


# Computing and using estimates of effect size

The following code demonstrates how you can compute and plot the effect size. 

	
	% find the interesting segments of data
	cfg = [];
	cfg.dataset                 = 'Subject01.ds';
	cfg.trialdef.eventtype      = 'backpanel trigger';
	cfg.trialdef.prestim        = 1;
	cfg.trialdef.poststim       = 2;
	cfg.trialdef.eventvalue     = [3 5 9];
	% 3 = FIC
	% 5 = FC
	% 9 = IC
	cfg = ft_definetrial(cfg);
	
	% preprocess the data
	cfg.channel         = {'MEG', '-MLP31', '-MLO12'};
	cfg.demean          = 'yes';
	cfg.baselinewindow  = [-0.2 0];
	% cfg.lpfilter      = 'yes';
	% cfg.lpfreq        = 35;
	data = ft_preprocessing(cfg);
	
	%%
	
	cfg = [];
	cfg.keeptrials = 'yes';
	cfg.trials = (data.trialinfo==3);
	timelock_FIC = ft_timelockanalysis(cfg, data);
	cfg.trials = (data.trialinfo==5);
	timelock_FC = ft_timelockanalysis(cfg, data);
	cfg.trials = (data.trialinfo==9);
	timelock_IC = ft_timelockanalysis(cfg, data);
	
	%%
	
	cfg = [];
	cfg.parameter = 'trial';
	cfg.method = 'analytic';
	cfg.statistic = 'indepsamplesT';
	cfg.design = [1*ones(1,size(timelock_FC.trial,1)) 2*ones(1,size(timelock_FIC.trial,1))];
	cfg.ivar = 1;
	stat_FCvsFIC = ft_timelockstatistics(cfg, timelock_FC, timelock_FIC);
	
	%%
	
	cfg = [];
	cfg.layout = 'CTF151_helmet';
	cfg.parameter = 'stat';
	ft_multiplotER(cfg, stat_FCvsFIC);
	
	%%
	
	% MLF32 shows a large positive p-value that peaks around 600ms
	chansel = match_str(timelock_FC.label, 'MLF32');
	timesel = nearest(timelock_FC.time, 0.6);
	
	%%
	
	x1 = timelock_FC.trial(:, chansel, timesel)*1e12;
	x2 = timelock_FIC.trial(:, chansel, timesel)*1e12;
	
	x1 = mean(mean(x1,3),2);
	x2 = mean(mean(x2,3),2);
	
	n1 = length(x1);
	n2 = length(x2);
	
	if n1==n2
	  % this fails if x1 and x2 are of different length
	  figure
	  hist([x1 x2], 50); legend({'FC', 'FIC'})
	end
	
	pooled_sd = sqrt( ((n1-1)*std(x1)^2 + (n2-1)*std(x2)^2) / (n1+n2-1) );
	cohensd = (mean(x1)-mean(x2)) / pooled_sd
	
	% see https://en.wikipedia.org/wiki/Effect_size#Cohen.27s_d
	
	% Very small  0.01
	% Small       0.20
	% Medium      0.50
	% Large       0.80
	% Very large  1.20
	% Huge        2.00
	


It is interesting to see how the effect size increases by taking the average over more channels and time points.

	
	
	%%
	
	chansel = match_str(timelock_FC.label, {'MLF22', 'MLF23', 'MLF32', 'MLF33', 'MLF42', 'MLF43', 'MLF52'});
	timesel = nearest(timelock_FC.time, 0.496607) : nearest(timelock_FC.time, 0.765893);
	
	% now repeat the computation of Cohen's d above



Proper preprocessing of the data also increases the effect size.

	
	%%
	
	cfg = [];
	cfg.method = 'summary';
	data = ft_rejectvisual(cfg, data);
	
	% now repeat the computation of Cohen's d above
	% this requires the following code for plotting
	
	edges = linspace(-0.4, 0.4, 30);
	h1 = histcounts(x1,edges);
	h2 = histcounts(x2,edges);
	bar(edges(1:end-1),[h1; h2]'); legend({'FC', 'FIC'})

