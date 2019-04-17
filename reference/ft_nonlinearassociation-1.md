---
title: ft_nonlinearassociation
---
```
 NONLINEARASSOCIATION calculate the association coefficient as a
 function of delay.

 In order to estimate the amount of association between all possible
 pairs of MEG sensors the nonlinear association analysis is used.
 It was first developed for EEG data analysis by Pijn and co-workers
 (Lopes da Silva, et al. 1989; Pijn, et al. 1990). The basic principle
 is similar to that of coherence and (cross) correlation, with the
 exception that this nonlinear association method can be applied
 independent of the type of relationship (linear or nonlinear) in
 the data.
 
 The method is based on the idea that if two signals x and y are
 correlated, a nonlinear regression curve can be calculated that
 represents their relationship. In practice, that regression curve
 is estimated by creating a scatterplot of y versus x, dividing the
 data in segments and describing each segment with a linear regression
 curve. The estimated correlation ratio h2, which gives the reduction
 in variance of y as a result of predicting its values according to
 the regression curve, can be calculated as follows:
 
 h^2 = (sum(Yi - mean(Y))^2 - sum(Yi - f(Xi))^2) / sum(Yi - mean(Y))^2
 
 With the sum going over N samples and f(Xi) the estimated value of
 Yi according to the regression line. The h2 coefficient has values
 between 0 (y is completely independent of x) and 1 (y is completely
 determined by x). In the case of a linear relationship between x
 and y, h2 is equal to the well known Pearson correlation coefficient
 (r2). As is the case with cross-correlation, it is possible to
 estimate h2 as a function of time shift () between the signals. The
 h2 is then iteratively calculated for different values of , by
 shifting the signals in comparison to each other, and the value for
 which the maximal h2 is reached can be used as an estimate of the
 time lag between both signals. In deciding what epoch length to use
 in the association analysis, a trade-off has to be made between
 successfully determining the correct delay and h2-value (for which
 large epoch lengths are necessary) and a small enough time-resolution
 (for which small epoch lengths are necessary).
 
 Use as
   [association] = nonlinearassociation(cfg, data)

 The input data should be organised in a structure as obtained from
 the PREPROCESSING function.

 The configuration should contain
   cfg.channel    = Nx1 cell-array with selection of channels (default = 'all'), see CHANNELSELECTION for details
   cfg.keeptrials = 'yes' or 'no', process the individual trials or the concatenated data (default = 'no')
   cfg.trials     = 'all' or a selection given as a 1xN vector (default = 'all')
   cfg.fsample    = 1200
   cfg.maxdelay   = 32/cfg.fsample
   cfg.delaystep  = 2/cfg.fsample
   cfg.nr_bins    = 7
   cfg.offset     = 0
   cfg.order      = 'Hxy'
   cfg.timwin     = 0.2
   cfg.toi        = []

 References
 - Lopes da Silva F, Pijn JP, Boeijinga P. (1989): Interdependence of
 EEG signals: linear vs. nonlinear associations and the significance
 of time delays and phase shifts. Brain Topogr 2(1-2):9-18.
 - Pijn JP, Vijn PC, Lopes da Silva FH, Van Ende Boas W, Blanes W.
 (1990): Localization of epileptogenic foci using a new signal
 analytical approach. Neurophysiol Clin 20(1):1-11.
```
