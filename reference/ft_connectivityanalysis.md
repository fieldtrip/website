---
title: ft_connectivityanalysis
---
```
 FT_CONNECTIVITYANALYSIS computes various measures of connectivity between
 MEG/EEG channels or between source-level signals.

 Use as
   stat = ft_connectivityanalysis(cfg, data)
   stat = ft_connectivityanalysis(cfg, timelock)
   stat = ft_connectivityanalysis(cfg, freq)
   stat = ft_connectivityanalysis(cfg, source)
 where the first input argument is a configuration structure (see below)
 and the second argument is the output of FT_PREPROCESSING,
 FT_TIMELOCKANLAYSIS, FT_FREQANALYSIS, FT_MVARANALYSIS or FT_SOURCEANALYSIS.

 The different connectivity metrics are supported only for specific
 datatypes (see below).

 The configuration structure has to contain
   cfg.method  =  string, can be
     'amplcorr',  amplitude correlation, support for freq and source data
     'coh',       coherence, support for freq, freqmvar and source data.
                  For partial coherence also specify cfg.partchannel, see below.
                  For imaginary part of coherency or coherency also specify
                  cfg.complex, see below.
     'csd',       cross-spectral density matrix, can also calculate partial
                  csds - if cfg.partchannel is specified, support for freq
                  and freqmvar data
     'dtf',       directed transfer function, support for freq and
                  freqmvar data
     'granger',   granger causality, support for freq and freqmvar data
     'pdc',       partial directed coherence, support for freq and
                  freqmvar data
     'plv',       phase-locking value, support for freq and freqmvar data
     'powcorr',   power correlation, support for freq and source data
     'powcorr_ortho', power correlation with single trial
                  orthogonalisation, support for source data
     'ppc'        pairwise phase consistency
     'psi',       phaseslope index, support for freq and freqmvar data
     'wpli',      weighted phase lag index (signed one,
                  still have to take absolute value to get indication of
                  strength of interaction. Note: measure has positive
                  bias. Use wpli_debiased to avoid this.
     'wpli_debiased'  debiased weighted phase lag index
                  (estimates squared wpli)
     'wppc'       weighted pairwise phase consistency
     'corr'       Pearson correlation, support for timelock or raw data

 Additional configuration options are
   cfg.channel    = Nx1 cell-array containing a list of channels which are
     used for the subsequent computations. This only has an effect when
     the input data is univariate. See FT_CHANNELSELECTION
   cfg.channelcmb = Nx2 cell-array containing the channel combinations on
     which to compute the connectivity. This only has an effect when the
     input data is univariate. See FT_CHANNELCOMBINATION
   cfg.trials     = Nx1 vector specifying which trials to include for the
     computation. This only has an effect when the input data contains
     repetitions.
   cfg.feedback   = string, specifying the feedback presented to the user.
     Default is 'none'. See FT_PROGRESS

 For specific methods the configuration can also contain
   cfg.partchannel = cell-array containing a list of channels that need to
     be partialized out, support for method 'coh', 'csd', 'plv'
   cfg.complex     = 'abs' (default), 'angle', 'complex', 'imag', 'real',
     '-logabs', support for method 'coh', 'csd', 'plv'
   cfg.removemean  = 'yes' (default), or 'no', support for method
     'powcorr' and 'amplcorr'.
   cfg.bandwidth   = scalar, (default = Rayleigh frequency), needed for
			'psi', half-bandwidth of the integration across frequencies (in Hz)

 To facilitate data-handling and distributed computing you can use
   cfg.inputfile   =  ...
   cfg.outputfile  =  ...
 If you specify one of these (or both) the input data will be read from a *.mat
 file on disk and/or the output data will be written to a *.mat file. These mat
 files should contain only a single variable, corresponding with the
 input/output structure.

 See also FT_PREPROCESSING, FT_TIMELOCKANALYSIS, FT_FREQANALYSIS,
 FT_MVARANALYSIS, FT_SOURCEANALYSIS, FT_NETWORKANALYSIS.

 For the implemented methods, see also FT_CONNECTIVITY_CORR,
 FT_CONNECTIVITY_GRANGER, FT_CONNECTIVITY_PPC, FT_CONNECTIVITY_WPLI,
 FT_CONNECTIVITY_PDC, FT_CONNECTIVITY_DTF, FT_CONNECTIVITY_PSI
```
