---
title: SDG Global Summer School in Hangzhou, China
tags: [hangzhou2026, opm]
---

The [SDG Global Summer School](https://sdg-gss.zju.edu.cn) is an international academic summer program hosted by Zhejiang University (ZJU) in Hangzhou, China. We will teach on MEG and OPM as part of the "Future Human Health – Theory of Brain-machine Integration and Application" track within the summer school.

When: MEG/OPM on Saturday 15 August 2026  
Where: Zhejiang University in Hangzhou, China  
Who: Robert Oostenveld and Haiteng Jiang  

This one-day workshop offers a practical and conceptual introduction to magnetoencephalography with optically pumped magnetometers (OPMs), a rapidly maturing technology that is reshaping the landscape of non-invasive human neuroimaging. The day combines two lectures with hands-on data analysis sessions, following the format established by the FieldTrip MEG/EEG toolkit course in Nijmegen.

The workshop is aimed at neuroscientists and clinical researchers who are new to OPM-MEG, as well as experienced MEG users who want to understand how OPM systems differ from conventional SQUID-based setups and what that means in practice for experimental design, data quality, and analysis pipelines.

{% include image src="/assets/img/workshop/hangzhou2026/sdg.jpg" width="300" %}

## Lecture 1 — Introduction to OPM-MEG: Technology and Acquisition

The first lecture introduces the physical principles underlying OPM sensors and contrasts them with conventional SQUID-based MEG. Where SQUIDs require cryogenic cooling and a fixed, helmet-shaped dewar, OPMs are compact, room-temperature sensors that can be placed flexibly on the scalp, worn close to the head, and repositioned between or within participants. This proximity to the source comes with significant gains in signal amplitude, but also with new challenges: participants can move during recordings, sensors measure the background field rather than a gradient, and the magnetic environment must be carefully managed. The lecture covers the design of magnetically shielded recording environments, strategies for field zeroing and active shielding, sensor co-registration with individual anatomy, and practical considerations for stimulus delivery, participant preparation, and experimental paradigm design. Real examples from OPM recordings will illustrate both the promise and the current constraints of the technology.

## Lecture 2 — Analysis Methods: Preprocessing, Sensor-Level Analysis, and Beamforming

The second lecture walks through the full analysis pipeline for OPM-MEG data, from raw recordings to source-localised results. After an overview of preprocessing steps — artefact identification and rejection, handling of movement, and channel-level data inspection — the lecture covers sensor-level analysis of event-related fields and time-frequency responses. The core of the session is dedicated to beamformer source reconstruction. Beamformers are spatially adaptive filters that estimate neural activity at each point in the brain by minimising interference from other locations. The lecture explains the principles behind the linearly constrained minimum variance (LCMV) beamformer for time-domain analysis and the DICS approach for oscillatory, frequency-domain data; it covers the construction of forward models (head model, source model, and lead field matrix) that are required as inputs, and discusses strategies for defining appropriate active and baseline contrast windows. The session concludes with an overview of how source estimates can be visualised and interpreted, and where common pitfalls arise.

## Hands-On Sessions

Both lectures are accompanied by guided hands-on sessions using MATLAB and FieldTrip. Participants will preprocess an example OPM-MEG dataset, compute event-related fields and time-frequency representations at the sensor level, and apply a beamformer to localise oscillatory sources. All scripts and data will be made available before the workshop. Participants are expected to bring their own laptops with MATLAB and a recent version of FieldTrip installed.

Course material and tutorial data will be distributed through this website at a later moment, and will also be available on USB sticks for on-site participants.

## Who Should Attend

Researchers considering setting up an OPM-MEG system; current MEG and EEG users wanting to understand the OPM landscape; graduate students and postdocs working in cognitive or clinical neuroimaging. No prior experience with OPM systems is required, but familiarity with basic MEG or EEG concepts is assumed.
