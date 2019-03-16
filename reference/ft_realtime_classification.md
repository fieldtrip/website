---
title: ft_realtime_classification
---
```
 FT_REALTIME_CLASSIFICATION is an example realtime application for online
 classification of the data. It should work both for EEG and MEG.

 Use as
   ft_realtime_classification(cfg)
 with the following configuration options
   cfg.channel    = cell-array, see FT_CHANNELSELECTION (default = 'all')
   cfg.trialfun   = string with the trial function

 The source of the data is configured as
   cfg.dataset       = string
 or alternatively to obtain more low-level control as
   cfg.datafile      = string
   cfg.headerfile    = string
   cfg.eventfile     = string
   cfg.dataformat    = string, default is determined automatic
   cfg.headerformat  = string, default is determined automatic
   cfg.eventformat   = string, default is determined automatic

 This function works with two-class data that is timelocked to a trigger.
 Data selection is based on events that should be present in the
 datastream or datafile. The user should specify a trial function that
 selects pieces of data to be classified, or pieces of data on which the
 classifier has to be trained.The trialfun should return segments in a
 trial definition (see FT_DEFINETRIAL). The 4th column of the trl matrix
 should contain the class label (number 1 or 2). The 5th colum of the trl
 matrix should contain a flag indicating whether it belongs to the test or
 to the training set (0 or 1 respectively).

 Example useage:
   cfg = [];
   cfg.dataset  = 'Subject01.ds';
   cfg.trialfun = 'trialfun_Subject01';
   ft_realtime_classification(cfg);

 To stop the realtime function, you have to press Ctrl-C
```
