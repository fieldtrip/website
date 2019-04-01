---
title: ft_datatype_sens
---
```
 FT_DATATYPE_SENS describes the FieldTrip structure that represents an EEG, ECoG, or
 MEG sensor array. This structure is commonly called "elec" for EEG, "grad" for MEG,
 "opto" for NIRS, or general "sens" for either one.

 For all sensor types a distinction should be made between the channel (i.e. the
 output of the transducer that is A/D converted) and the sensor, which may have some
 spatial extent. E.g. with EEG you can have a bipolar channel, where the position of
 the channel can be represented as in between the position of the two electrodes.

 The structure for MEG gradiometers and/or magnetometers contains
    sens.label    = Mx1 cell-array with channel labels
    sens.chanpos  = Mx3 matrix with channel positions
    sens.chanori  = Mx3 matrix with channel orientations, used for synthetic planar gradient computation
    sens.tra      = MxN matrix to combine coils into channels
    sens.coilpos  = Nx3 matrix with coil positions
    sens.coilori  = Nx3 matrix with coil orientations
    sens.balance  = structure containing info about the balancing, See FT_APPLY_MONTAGE
 and optionally
    sens.chanposold = Mx3 matrix with original channel positions (in case
                      sens.chanpos has been updated to contain NaNs, e.g.
                      after ft_componentanalysis)
    sens.chanoriold = Mx3 matrix with original channel orientations
    sens.labelold   = Mx1 cell-array with original channel labels

 The structure for EEG or ECoG channels contains
    sens.label    = Mx1 cell-array with channel labels
    sens.elecpos  = Nx3 matrix with electrode positions
    sens.chanpos  = Mx3 matrix with channel positions (often the same as electrode positions)
    sens.tra      = MxN matrix to combine electrodes into channels
 In case sens.tra is not present in the EEG sensor array, the channels
 are assumed to be average referenced.

 The structure for NIRS channels contains
   sens.optopos        = contains information about the position of the optodes
   sens.optotype       = contains information about the type of optode (receiver or transmitter)
   sens.chanpos        = contains information about the position of the channels (i.e. average of optopos)
   sens.tra            = NxC matrix, boolean, contains information about how receiver and transmitter form channels
   sens.wavelength     = 1xM vector of all wavelengths that were used
   sens.transmits      = NxM matrix, boolean, where N is the number of optodes and M the number of wavelengths per transmitter. Specifies what optode is transmitting at what wavelength (or nothing at all, which indicates that it is a receiver)
   sens.laserstrength  = 1xM vector of the strength of the emitted light of the lasers

 The following fields apply to MEG and EEG
    sens.chantype = Mx1 cell-array with the type of the channel, see FT_CHANTYPE
    sens.chanunit = Mx1 cell-array with the units of the channel signal, e.g. 'V', 'fT' or 'T/cm', see FT_CHANUNIT

 The following fields are optional
    sens.type     = string with the type of acquisition system, see FT_SENSTYPE
    sens.fid      = structure with fiducial information

 Historical fields:
    pnt, pos, ori, pnt1, pnt2

 Revision history:
 (2016/latest) The chantype and chanunit have become required fields.
  Original channel details are specified with the suffix "old" rather than "org".
  All numeric values are represented in double precision.
  It is possible to convert the amplitude and distance units (e.g. from T to fT and
  from m to mm) and it is possible to express planar and axial gradiometer channels
  either in units of amplitude or in units of amplitude/distance (i.e. proper
  gradient).

 (2011v2) The chantype and chanunit have been added for MEG.

 (2011v1) To facilitate determining the position of channels (e.g. for plotting)
  in case of balanced MEG or bipolar EEG, an explicit distinction has been made
  between chanpos+chanori and coilpos+coilori (for MEG) and chanpos and elecpos
  (for EEG). The pnt and ori fields are removed

 (2010) Added support for bipolar or otherwise more complex linear combinations
  of EEG electrodes using sens.tra, similar to MEG.

 (2009) Noice reduction has been added for MEG systems in the balance field.

 (2006) The optional fields sens.type and sens.unit were added.

 (2003) The initial version was defined, which looked like this for EEG
    sens.pnt     = Mx3 matrix with electrode positions
    sens.label   = Mx1 cell-array with channel labels
 and like this for MEG
    sens.pnt     = Nx3 matrix with coil positions
    sens.ori     = Nx3 matrix with coil orientations
    sens.tra     = MxN matrix to combine coils into channels
    sens.label   = Mx1 cell-array with channel labels

 See also FT_READ_SENS, FT_SENSTYPE, FT_CHANTYPE, FT_APPLY_MONTAGE, CTF2GRAD, FIF2GRAD,
 BTI2GRAD, YOKOGAWA2GRAD, ITAB2GRAD
```
