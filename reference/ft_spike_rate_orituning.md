---
title: ft_spike_rate_orituning
---
```
 FT_SPIKE_RATE_ORITUNING computes a model of the firing rate as a function
 of orientation or direction.

 Use as
   [stat] = ft_spike_rate_tuning(cfg, rate1, rate2, ... rateN)

 The inputs RATE should be the output from FT_SPIKE_RATE. 

 Configurations:
   cfg.stimuli  = should be an 1 x nConditions array of orientations or
                  directions in radians
                  varargin{i} corresponds to cfg.stimuli(i)
   cfg.method   = model to apply, implemented are 'orientation' and 'direction'

 Outputs:
   stat.ang       = mean angle of orientation / direction (1 x nUnits)
   stat.osi       = orientation selectivity index (Womelsdorf et al., 2012,
                    PNAS), that is resultant length.
                    if cfg.method = 'orientation', then orientations are
                    first projected on the unit circle.
   stat.di        = direction index, 1 - min/max response
```
