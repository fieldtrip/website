---
title: Example real-time classification
parent: Real-time analysis
grand_parent: Examples
category: example
tags: [realtime]
redirect_from:
    - /example/ft_realtime_classification/
---

# Example real-time classification

## Flowchart

{% include image src="/assets/img/example/ft_realtime_classification/realtime_classification.png" width="400" %}

## Example use

The simplest is to try and classify the tutorial MEG dataset which is available from the download server. More information is on the dataset is available [here](/tutorial/meg_language). That dataset contains the stimulus classes FC, IC and FIC, corresponding to trigger values 9, 5 and 3.

    cfg = [];
    cfg.dataset  = 'Subject01.ds';
    cfg.trialfun = 'trialfun_twoclass_classification';
    cfg.trialdef.numtrain    = 20;
    cfg.trialdef.eventtype   = 'backpanel trigger';
    cfg.trialdef.eventvalue1 = 9; % FC
    cfg.trialdef.eventvalue2 = 3; % FIC
    cfg.trialdef.prestim     = 0.3;
    cfg.trialdef.poststim    = 0.7;

The trial definition function _trialfun_twoclass_classification _ that is being used is included in the fieldtrip/trialfun directory. Based on the code above you can already do

    dummy = ft_definetrial(cfg);

to see how the configuration and especially the trial definition looks lik

    >> dummy.trl
    ans =
           211         510          90         NaN           0
          1111        1410          90           2           0
          2011        2310          90         NaN           0
          2911        3210          90           2           0
          3811        4110          90           1           0
          4711        5010          90         NaN           0
          5611        5910          90         NaN           0
          6511        6810          90           2           0
          7411        7710          90           1           0
          ...

The first column is the beginsample, the second the endsample, the third column the offset of each segment. The fourth column indicates the class of each data segment (NaN means unknown, which happens for the third trigger type in this dataset) and the fifth column whether it should be used for training (0) or testing (1).

However, here we are not interested in the trial definition for offline processing, but instead for online classification. So based on the cfg structure above, you can run

    ft_realtime_classification(cfg);

The **[ft_realtime_classification](/reference/realtime/example/ft_realtime_classification)** function will print the classification result on screen and will open a figure in which the timing is displayed. It being an offline application here, the timing is measured relative to the amount of data that is processed. An acceleration factor larger than 1 means that data is processed faster than realtime, whereas smaller than 1 would indicate that it cannot keep up with the realtime speed. Note that there is quite some time spent on plotting the timing figure. Furthermore note that the timing is relative to the processed data, whereas there is also time between the trials for which the data does not have to be processed.

## MATLAB code

The code for **[ft_realtime_classification](/reference/realtime/example/ft_realtime_classification)** is included in the FieldTrip release under `fieldtrip/realtime/example` and can also be found on GitHub.
