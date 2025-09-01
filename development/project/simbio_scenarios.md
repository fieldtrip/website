---
title: FieldTrip/SIMBIO integration scenarios
---

{% include /shared/development/warning.md %}


This page describe the experimental situations in which some typical users find themselves in need of a tool like SIMBIO to calculate a FEM forward model.

## Scenario #1

Cristiano is an engineer working in collaboration with psychologists and medical doctors who are responsible for the acquisition of ECoG data from hospitalized epilepsy patients.
During their time in the hospital, these patients undergo a set of cognitive experiments during which their brain activity is recorded along with triggers.

Cristiano would like to make source reconstruction on these datasets and comes about the SIMBIO platform, containing an engine for FEM forward solution calculating lead fields.

Apart from the electrophysiological data, some other data is at hand, like the anatomy of the patients, which consists of: a pre-surgery MRI T1 scan of each subject and a post-surgery CT scan for each subject. The electrodes positions are visible in the CT scan.
What does he need to run his pipeline from raw data to source reconstruction/visualization?

## Scenario #2

Gomez is a physicist working in team with psychologists on resting state data acquired with EEG and MEG and sleep recordings, acquired with EEG.
He is trying to answer some crucial cognitive questions such as

- What are the effects of sleep (or sleep deprivation) in learning and memory?
- What are the neural correlates of chronic insomnia?

For that purpose he wants to run connectivity analysis at the source level and for that he needs a tool for localizing the sources and to reconstruct their time courses. The goal is to apply inverse solution methods like beamformer and MNE to the raw data.

He also has anatomical MRI of the single subjects at hand, and typical lab PC are windows computer with no more than 2Gb RAM and a Windows XP OS.

How does his pipeline look like?

## Scenario #3

Carsten is a mathematician working in the area of Bioelectromagnetism. His main interests are

- Building realistic models of the human head for modeling bioelectromagnetic phenomena such as the electric potential and the magnetic field evoked by a current distribution originating from brain activity. This way, EEG, MEG and ECoG recordings can be simulated (forward computation) which can be used by methods to infer brain activity from real recordings of the former modalities. Building a head model for these purposes essentially consists of defining volumes of different electrical conductivity which represent the different brain tissues. The information needed to do that has to be inferred from anatomical imaging techniques, such as MRI which have to be registered and segmented. Carsten is especially interested in the question which tissues have the most impact on the forward computation and should thus be modeled as accurate as possible.
- Comparing different numerical approaches the forward computation such as different finite element methods (FEM) or boundary element methods (BEM).
- Apply the above methods to applications such as presurgical epilepsy diagnosis with the aim to improve the reliability of EEG and MEG recordings, making long-term invasive ECoG recordings less necessary.

He disposes of MRI T1/T2 scans, DW-MRI (diffusion weighted) scans (a modality that allows for the estimation of the electrical conductivity of the head tissue. In that context it is often called DTI for diffusion tensor imaging) and EEG, MEG and possibly also ECoG recordings.

How does he combine all this information in a thorough pipeline?
