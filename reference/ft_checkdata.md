---
title: ft_checkdata
---
```
 FT_CHECKDATA checks the input data of the main FieldTrip functions, e.g. whether the
 type of data strucure corresponds with the required data. If neccessary and possible,
 this function will adjust the data structure to the input requirements (e.g. change
 dimord, average over trials, convert inside from index into logical).

 If the input data does NOT correspond to the requirements, this function will give a
 warning message and if applicable point the user to external documentation (link to
 website).

 Use as
   [data] = ft_checkdata(data, ...)

 Optional input arguments should be specified as key-value pairs and can include
   feedback           = yes, no
   datatype           = raw, freq, timelock, comp, spike, source, mesh, dip, volume, segmentation, parcellation
   dimord             = any combination of time, freq, chan, refchan, rpt, subj, chancmb, rpttap, pos
   senstype           = ctf151, ctf275, ctf151_planar, ctf275_planar, neuromag122, neuromag306, bti148, bti248, bti248_planar, magnetometer, electrode
   inside             = logical, index
   ismeg              = yes, no
   iseeg              = yes, no
   isnirs             = yes, no
   hasunit            = yes, no
   hascoordsys        = yes, no
   haschantype        = yes, no
   haschanunit        = yes, no
   hassampleinfo      = yes, no, ifmakessense (applies to raw and timelock data)
   hascumtapcnt       = yes, no (only applies to freq data)
   hasdim             = yes, no
   hasdof             = yes, no
   cmbrepresentation  = sparse, full (applies to covariance and cross-spectral density)
   fsample            = sampling frequency to use to go from SPIKE to RAW representation
   segmentationstyle  = indexed, probabilistic (only applies to segmentation)
   parcellationstyle  = indexed, probabilistic (only applies to parcellation)
   hasbrain           = yes, no (only applies to segmentation)
   trialinfostyle     = matrix, table or empty

 For some options you can specify multiple values, e.g.
   [data] = ft_checkdata(data, 'senstype', {'ctf151', 'ctf275'}), e.g. in megrealign
   [data] = ft_checkdata(data, 'datatype', {'timelock', 'freq'}), e.g. in sourceanalysis

 See also FT_DATATYPE_XXX for each of the respective data types.
```
