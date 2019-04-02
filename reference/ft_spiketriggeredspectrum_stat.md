---
title: ft_spiketriggeredspectrum_stat
---
```
 FT_SPIKETRIGGEREDSPECTRUM_STAT computes phase-locking statistics for spike-LFP
 phases. These contain the PPC statistics according to Vinck et al. 2010 (Neuroimage)
 and Vinck et al. 2011 (Journal of Computational Neuroscience).

 Use as:
   [stat] = ft_spiketriggeredspectrum_stat(cfg, spike)

 The input SPIKE should be a structure as obtained from the FT_SPIKETRIGGEREDSPECTRUM function.

 Configurations (cfg) 

 cfg.method  = string, indicating which statistic to compute. Can be:
     -'plv' : phase-locking value, computes the resultant length over spike
              phases. More spikes -> lower value (bias).
     -'ang' : computes the angular mean of the spike phases.
     -'ral' : computes the rayleigh p-value.
     -'ppc0': computes the pairwise-phase consistency across all available
              spike pairs (Vinck et al., 2010).
     -'ppc1': computes the pairwise-phase consistency across all available
              spike pairs with exclusion of spike pairs in the same trial.
              This avoids history effects within spike-trains to influence
              phase lock statistics.
     -'ppc2': computes the PPC across all spike pairs with exclusion of
              spike pairs in the same trial, but applies a normalization
              for every set of trials. This estimator has more variance but
              is more robust against dependencies between spike phase and
              spike count.
         
 cfg.timwin  = double or 'all' (default)
   - double: indicates we compute statistic with a
            sliding window of cfg.timwin, i.e. time-resolved analysis.
   - 'all': we compute statistic over all time-points,
            i.e. in non-time resolved fashion.

 cfg.winstepsize  = double, stepsize of sliding window in seconds. For
   example if cfg.winstepsize = 0.1, we compute stat every other 100 ms.

 cfg.channel      = Nx1 cell-array or numerical array with selection of
   channels (default = 'all'),See CHANNELSELECTION for details

 cfg.spikechannel = label of ONE unit, according to FT_CHANNELSELECTION

 cfg.spikesel     = 'all' (default) or numerical or logical selection of spikes.

 cfg.foi          = 'all' or numerical vector that specifies a subset of
   frequencies in Hz, e.g. cfg.foi = spike.freq(1:10);                                    

 cfg.latency      = [beg end] in sec, or 'maxperiod',  'poststim' or
  'prestim'.  This determines the start and end of analysis window.

 cfg.avgoverchan  = 'weighted', 'unweighted' (default) or 'no'.
                  This regulates averaging of fourierspectra prior to
                  computing the statistic.
  - 'weighted'  : we average across channels by weighting by the LFP power.
                  This is identical to adding the raw LFP signals in time 
                  and then taking their FFT.
  - 'unweighted': we average across channels after normalizing for LFP power. 
                  This is identical to normalizing LFP signals for 
                  their power, averaging them, and then taking their FFT.
  - 'no'        : no weighting is performed, statistic is computed for
                  every LFP channel.
 cfg.trials       = vector of indices (e.g., 1:2:10),
                    logical selection of trials (e.g., [1010101010]), or
                   'all' (default)

 Main outputs:
   stat.nspikes                    =  nChancmb-by-nFreqs-nTimepoints number
                                      of spikes used to compute stat
   stat.dimord                     = 'chan_freq_time'
   stat.labelcmb                   =  nChancmbs cell-array with spike vs
                                      LFP labels
   stat.(cfg.method)               =  nChancmb-by-nFreqs-nTimepoints  statistic
   stat.freq                       =  1xnFreqs array of frequencies
   stat.nspikes                    =  number of spikes used to compute

 The output stat structure can be plotted using ft_singleplotTFR or ft_multiplotTFR.
```
