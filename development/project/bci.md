---
title: Implement online data processing and classification for BCI
---

{% include /shared/development/warning.md %}

# Implement online data processing and classification for BCI

Note: real-time analysis of EEG and MEG data is currently in development within the F.C. Donders Centre. Not all functionality in FieldTrip will be immediately released to the general public. If you think something is missing in the release version that should be there, or if you want to have a pre-release of specific code, you can [contact](/contact) us.

The following BCI input agents are desired

- Offline data from a file
- Online data from CTF MEG system
- Online data from BioSemi EEG system
- Online data from BrainAmp EEG system
- ...

The following BCI classifying agents are desired

- CSP (common spatial pattern)
- invariant CSP
- 2-channel power t-score
- ...

The following BCI actor agents are desired

- virtual keyboard (using VNC)
- virtual mouse (using VNC)
- serial port
- parallel port
- NBS Presentation
- E-Prime
- wheelchair
- LEGO robot arm
- Pong game, single and dual player mode
- Hex-o-spell
- ...

Using the different actors, it is possible to implement a complete BCI system. The following BCI systems are desired

- Pong game, single and dual player mode
- EOG artifact detector
- head movement detector (only for MEG)
- ...
