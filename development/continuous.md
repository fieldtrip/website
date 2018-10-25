---
title: Handling of continuous data
layout: default
---

`<note warning>`

The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas. 

The code development project mentioned on this page has been finished by now. Chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
`</note>`

# Handling of continuous data

## Introduction

At the moment most of the fieldtrip functions work with segmented data in memory. The segments or trials are specified by DEFINETRIAL and the segments are read with PREPROCESSING. This also affects artifact detection, which is largely done prior to preprocessing, using data that still resides on disk. 

This data handling scheme was designed for large MEG data sets at the time where computer memory was often too small. Memory is less of a concern nowadays. Furthermore, a lot of people work with much smaller EEG datasets. Therefore we should reconsider this data handling.

One change that already reflects this reconsideration is that PREPROCESSING now not only works like

    data = preprocessing(cfg)

but also like

    dataFilt = preprocessing(cfg, dataRaw)

It is conceivable that similar changes can be made for other functions on the input side of fieldtrip. A list of functions to consider is

*  definetrial

*  artifact_eog/jump/muscle/xxx 

*  preprocessing

*  rejectartifact

*  rejectvisual

*  redefinetrial

*  recodeevent

## To do

*  Discuss the desired functionality and features

*  Discuss the dependencies and consistency of the features

*  Discuss the required modifications to the code

*  Implement the changes

*  Test and document the changes

example

    cfg = [];
    cfg.dataset = xxx
    cfg = definetrial(cfg);    % results in cfg.trl = [1 hdr.nSamples 0]
    data = preprocessing(cfg); % one very long trial

    cfg = [];
    cfg.dataset = xxx
    cfg = definetrial(cfg);          % look at events, make an interesting trl
    data = redefinetrial(cfg, data); % segment the data into small snippets
    

   count = zeros(1, 150);
   for i=1:size(trl,1)
     count(trl(i,1):trl(i,2)) = count(trl(i,1):trl(i,2))+1;
   end

addded by Esther 22 april 08

Done: 

After preprocessing without a trl (by which all data are preprocessed as 1 trial) redefinetrial can now segment these data based on a trl.

To d

* list all artifact functions

* study out how they work

* addapt the artifact functions so they can handle the described output of redefinetrial

