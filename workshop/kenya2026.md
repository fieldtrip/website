---
title: Pre-conference workshop in Nairobi, Kenya
tags: [kenia2026]
---

{% include image src="/assets/img/workshop/kenya2026/alma.png" link="https://almaafrica.org" width=200 %}

Preceding the [Institute for Human Development International Conference](https://www.aku.edu/ihd/Pages/ihd-conference.aspx), a pre-conference EEG/ERP  [workshop](https://www.aku.edu/ihd/Pages/pre-conference-workshops.aspx) was organized by [ALMA](https://almaafrica.org) where Robert Oostenveld presented.  

When: 8 June 2026  
Where: Pan Pacific Serviced Suites, Nairobi, Kenya  
Who: Robert Oostenveld  

This page lists all materials used/generated during that workshop for the attendees and others to review.

## Slides

1. [Introduction to EEG and ERPs](https://download.fieldtriptoolbox.org/workshop/kenya2026/slides/1%20-%20introduction%20to%20EEG%20and%20ERPs.pdf)
2. [Analysis of EEG and ERPs](https://download.fieldtriptoolbox.org/workshop/kenya2026/slides/2%20-%20analysis%20of%20EEG%20and%20ERPs.pdf)
3. [Research questions for EEG and ERPs](https://download.fieldtriptoolbox.org/workshop/kenya2026/slides/3%20-%20research%20questions%20for%20EEG%20and%20ERPs.pdf)

{% include markup/yellow %}
Last year in Port Harcour (Nigeria) we presented a week-long workshop that more-or-less covered the same topics, but in more detail. The [slides](/workshop/nigeria2025/#slides) presented there are also shared, and many of the presentations were recorded on [video](/workshop/nigeria2025/#video-recordings). So if you want to go in more detail into something, you can check those out.
{% include markup/end %}

## EEG demonstration

Following the EEG introduction lecture, we did a live EEG demonstration with the [MBrainTrain](https://mbraintrain.com) Smarting 24-channel wireless EEG system of the Institute for Human Development. Following capping of a volunteer from the audience and preparation of the EEG and stimulus presentation laptop, three short experiments (four recordings) were done:

1. resting state eyes open and eyes closed
2. visual oddball experiment
3. auditory oddball experiment

Note that the oddball experiments were not designed for scientific rigor, but mostly for didactical and demonstration purposes. These recordings were done with the subject sitting at the front of the conference room, with both the stimulation and a partial view of the live EEG data stream projected on the large LCD screen so that the audience could look along.

The eyes open and closed conditions were both recorded for 2 minutes.

The stimulus presentation scripts were implemented with [Psychopy](https://psychopy.org/) and are together with a number of demonstration scripts shared on our [download server](https://download.fieldtriptoolbox.org/workshop/kenya2026/psychopy). We used LSL for the synchronization of the oddball experiments. The scripts `visual5.py` and `auditory3.py` were the ones used for the actual recording. Eash presented 150 stimuli, with an ITI of about 1 second, resulting in about 2.5 minutes of data for each.

The EEG data is stored in the [XDF](https://github.com/sccn/xdf) format and also available from [download server](https://download.fieldtriptoolbox.org/workshop/kenya2026/data). We recorded `sub02` on the day of the workshop itself, and recorded the EEG data of another volunteer `sub01` with the same experimental paradigms while preparing the on day before.

## EEG analysis demonstration

The data analysis scripts were implemented in FieldTrip based on the data of `sub01` and were live demonstrated during the workshop on the data of `sub02` that was just recorded. The MATLAB analysis scripts are stored alongside the data on the [download server](https://download.fieldtriptoolbox.org/workshop/kenya2026/data).

The eyes open versus eyes closed contrast showed the expected alpha increase for both subjects, and especially clear in the live data when subject 2 closed their eyes.

The auditory task had the expected overall AEP and somewhat of a discernable ERP difference wave for both subjects.

The visual task showed the expected VEP for subject 1, but not a clear ERP difference wave. The visual task for subject 2 did not show the expected VEP, but a later (300 ms) ERP component, and no clear ERP difference wave.

The ERP difference waves not being clear was actually expected, guven the short duration of the experiments and the small number of trials (especially following rejection of trials with eye artifacts). CLeaning the data with ICA would probably have been the better strategy, but did not fit within the limited time of the workshop.
