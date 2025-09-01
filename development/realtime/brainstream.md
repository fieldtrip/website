---
title: Streaming realtime data from and to BrainStream
tags: [realtime]
---

[BrainStream ](http://www.brainstream.nu) is a MATLAB application that is being developed in the context of the [BrainGain ](http://www.braingain.nl) project by Philip van den Broek, Peter Desain and coworkers at the [Donders Centre for Cognition](https://www.ru.nl/cognition) (formerly the NICI).

BrainStream focuses on building a generic easy-to-use user/programmer interface for setting up any BCI-application. Using a set of modular-based, easy readable and modifiable tables, a broad range of BCI-applications can be defined in a very quick and simple way. Considering the availability of appropriate analyses, no programming experience is needed for setting up a new BCI experiment. Essentially, the ultimate goal of BrainStream is to allow researchers to solely focus on their BCI-specific analyses. BrainStream will encourage the sharing of BCI-applications between partners with different BCI-setups.

## Integration with FieldTrip

BrainStream makes use of the [FieldTrip fileio module](/development/module/fileio) to read data. The fileio interface allows BrainStream to read offline data (i.e. from disk) from any of the ~30 supported fileformats. Furthermore, the fileio interface allows BrainStream to read data and events in real-time from the [FieldTrip buffer](/development/realtime/buffer).

Instructions on how to use BrainStream in general can be found [here](http://www.nici.ru.nl/brainstream/twiki/bin/view/BrainStreamDocs), or take a look at the [sentences](http://www.nici.ru.nl/brainstream/twiki/bin/view/BrainStreamDocs/DocsSectionsExampleSentences) and [speller](http://www.nici.ru.nl/brainstream/twiki/bin/view/BrainStreamDocs/DocsSectionsExampleSpellerIntro) examples.
