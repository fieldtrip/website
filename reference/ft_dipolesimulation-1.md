---
title: ft_dipolesimulation
---
```
 FT_DIPOLESIMULATION computes the field or potential of a simulated dipole
 and returns a datastructure identical to the FT_PREPROCESSING function.

 Use as
   data = ft_dipolesimulation(cfg)

 The dipoles position and orientation have to be specified with
   cfg.dip.pos     = [Rx Ry Rz] (size Nx3)
   cfg.dip.mom     = [Qx Qy Qz] (size 3xN)

 The timecourse of the dipole activity is given as a single vector or as a
 cell-array with one vectors per trial
   cfg.dip.signal
 or by specifying a sine-wave signal
   cfg.dip.frequency    in Hz
   cfg.dip.phase        in radians
   cfg.dip.amplitude    per dipole
   cfg.ntrials          number of trials
   cfg.triallength      time in seconds
   cfg.fsample          sampling frequency in Hz

 Random white noise can be added to the data in each trial, either by
 specifying an absolute or a relative noise level
   cfg.relnoise    = add noise with level relative to simulated signal
   cfg.absnoise    = add noise with absolute level
   cfg.randomseed  = 'yes' or a number or vector with the seed value (default = 'yes')

 Optional input arguments are
   cfg.channel    = Nx1 cell-array with selection of channels (default = 'all'),
                    see FT_CHANNELSELECTION for details
   cfg.dipoleunit = units for dipole amplitude (default nA*m)
   cfg.chanunit   = units for the channel data

 The volume conduction model of the head should be specified as
   cfg.headmodel     = structure with volume conduction model, see FT_PREPARE_HEADMODEL

 The EEG or MEG sensor positions should be specified as
   cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS
   cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS

 See also FT_SOURCEANALYSIS, FT_DIPOLEFITTING, FT_TIMELOCKSIMULATION,
 FT_FREQSIMULATION, FT_CONNECTIVITYSIMULATION
```
