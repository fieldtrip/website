---
title: ft_connectivity_laggedcoherence
---
```
 FT_CONNECTIVITY_LAGGEDCOHERENCE performs time-resolved coherence analysis of
 oscillatory activity only, both within and between recording sites. This implements
 the method described in Fransen, Anne M. M, Van Ede, Freek, Maris, Eric (2015)
 Identifying oscillations on the basis of rhythmicity. NeuroImage 118: 256-267.

 Use as
   lcoh = ft_connectivityanalysis(cfg, freq)
 with cfg.method='laggedcoherence' or as
    lcoh = ft_connectivity_laggedcoherence(cfg, freq)

 The input data should be organised in a structure as obtained from FT_FREQANALYSIS
 and should contain the fields 'fourierspctrm' and 'time'. The timepoints must be
 chosen such that the desired cfg.lag/cfg.foi (lag in s) is an integer multiple of
 the time resolution in freqout.

 This function must be called separately for each frequency of interest. To analyse
 multiple frequencies, you can use a for-loop like this:
   cfg_F             = [];
   cfg_F.method      = 'wavelet';
   cfg_F.output      = 'fourier';
   cfg_F.width       = 3;
   cfg_F.keeptrials  = 'yes';
   cfg_LC            = [];
   cfg_LC.lag        = cfg_F.width;
   cfg_LC.method     = 'laggedcoherence';
   foi               = 1:1:100;
   fs                = data.fsample;
   for counter = 1:length(foi);
       cfg_F.foi     = foi(counter);
       cfg_LC.foi    = foi(counter);
       width         = cfg_F.width/cfg_F.foi;
       cfg_F.toi     = data.time{1}(1) + ceil(fs*width/2)/fs : ...   %from:
         cfg_LC.lag/cfg_F.foi : ...                      %in steps of size:
         data.time{1}(end) - ceil(fs*width/2)/fs;                      %to:
       freqout       = ft_freqanalysis(cfg_F,data);
       lcoh(counter) = ft_connectivityanalysis(cfg_LC,freqout);
   end

 The configuration structure cfg should contain:
   cfg.foi          =  frequency of interest (default=freqout.freq(1))
   cfg.lag          =  the number of periods between the onset of the time window
                       used for phase estimate 1 and the onset of the time window
                       for phase estimate 2 (the default cfg.lag is set to match the
                       time resolution in freqout). We recommend users to choose
                       cfg.lag such that it is larger or equal to the width of the
                       wavelet used for each Fourier transform in ft_freqanalysis
   cfg.output       =  'lcoh', or 'csd' (default='lcoh'). When the output
                       is set to 'csd', one can specify the channel combinations
                       between which to compute the lagged cross-spectra in
                       cfg.channelcmb

 To calculate lagged coherence values from the cross-spectra, do:
    abs(lcoh.laggedcrsspctrm)./sqrt(lcoh.powspctrm1.*lcoh.powspctrm2)
 where lcoh.powspctrm1 denotes power in the channels of the first
 column of cfg.channelcmb, and lcoh.powspctrm2 does the same for the
 channels in the second column of cfg.channelcmb. Note that the power
 is calculated for the same time windows that are used for calculating
 the lagged cross-spectra.

 Optional settings:
   cfg.timeresolved = 'yes' or 'no' (default='no'). If set to yes, lagged
                      coherence is calculated separately for each pair of timepoints
                      that is separated by cfg.lag
   cfg.nlags        = the lags in lcoh are the set of (1:1:nlags)*lag
                      (default = 1). Note that if cfg.timeresolved=='yes', then
                      cfg.nlags must be set to 1.
   cfg.channel      = Nx1 cell-array with selection of channels
                      (default = 'all'), see FT_CHANNELSELECTION for details
   cfg.channelcmb   = Mx2 cell-array with channel pairs, (default={'all','all'}),
                      see FT_CHANNELCOMBINATION for details
   cfg.autocmb      = 'yes' or 'no' (default='no'). Adds all auto-
                      combinations of cfg.channel to cfg.channelcmb
   cfg.trialsets    = cell-array with per cell the set of trials over
                      which lcoh is calculated. Each cell must contain 'all' or a
                      1xN vector of trial indices. Default={'all'}. Note that this
                      differs from the required format of cfg.trials in e.g.
                      ft_connectivityanalysis.

 See also FT_CONNECTIVITYANALYSIS
```
