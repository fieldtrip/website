---
layout: default
---

##  FT_CONNECTIVITYANALYSIS

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_connectivityanalysis".

`<html>``<pre>`
    `<a href=/reference/ft_connectivityanalysis>``<font color=green>`FT_CONNECTIVITYANALYSIS`</font>``</a>` computes various measures of connectivity between
    MEG/EEG channels or between source-level signals.
 
    Use as
    stat = ft_connectivityanalysis(cfg, data)
    stat = ft_connectivityanalysis(cfg, timelock)
    stat = ft_connectivityanalysis(cfg, freq)
    stat = ft_connectivityanalysis(cfg, source)
    where the first input argument is a configuration structure (see below)
    and the second argument is the output of `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`,
    FT_TIMELOCKANLAYSIS, `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`, `<a href=/reference/ft_mvaranalysis>``<font color=green>`FT_MVARANALYSIS`</font>``</a>` or `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`.
 
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
      the input data is univariate. See `<a href=/reference/ft_channelselection>``<font color=green>`FT_CHANNELSELECTION`</font>``</a>`
    cfg.channelcmb = Nx2 cell-array containing the channel combinations on
      which to compute the connectivity. This only has an effect when the
      input data is univariate. See `<a href=/reference/ft_channelcombination>``<font color=green>`FT_CHANNELCOMBINATION`</font>``</a>`
    cfg.trials     = Nx1 vector specifying which trials to include for the
      computation. This only has an effect when the input data contains
      repetitions.
    cfg.feedback   = string, specifying the feedback presented to the user.
      Default is 'none'. See `<a href=/reference/ft_progress>``<font color=green>`FT_PROGRESS`</font>``</a>`
 
    For specific methods the cfg can also contain
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
 
    See also `<a href=/reference/ft_preprocessing>``<font color=green>`FT_PREPROCESSING`</font>``</a>`, `<a href=/reference/ft_timelockanalysis>``<font color=green>`FT_TIMELOCKANALYSIS`</font>``</a>`, `<a href=/reference/ft_freqanalysis>``<font color=green>`FT_FREQANALYSIS`</font>``</a>`,
    `<a href=/reference/ft_mvaranalysis>``<font color=green>`FT_MVARANALYSIS`</font>``</a>`, `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`, `<a href=/reference/ft_networkanalysis>``<font color=green>`FT_NETWORKANALYSIS`</font>``</a>`.
 
    For the implemented methods, see also `<a href=/reference/ft_connectivity_corr>``<font color=green>`FT_CONNECTIVITY_CORR`</font>``</a>`,
    `<a href=/reference/ft_connectivity_granger>``<font color=green>`FT_CONNECTIVITY_GRANGER`</font>``</a>`, `<a href=/reference/ft_connectivity_ppc>``<font color=green>`FT_CONNECTIVITY_PPC`</font>``</a>`, `<a href=/reference/ft_connectivity_wpli>``<font color=green>`FT_CONNECTIVITY_WPLI`</font>``</a>`,
    `<a href=/reference/ft_connectivity_pdc>``<font color=green>`FT_CONNECTIVITY_PDC`</font>``</a>`, `<a href=/reference/ft_connectivity_dtf>``<font color=green>`FT_CONNECTIVITY_DTF`</font>``</a>`, `<a href=/reference/ft_connectivity_psi>``<font color=green>`FT_CONNECTIVITY_PSI`</font>``</a>`
`</pre>``</html>`

