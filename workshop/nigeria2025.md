---
title: African Brain Data Network workshop in Nigeria
tags: [nigeria2025]
---

# African Brain Data Network workshop in Nigeria

Together with the [African Brain Data Network](https://africanbraindatanetwork.com) we are organizing an intensive one-week EEG Workshop in Nigeria (9-14 June, 2025) designed to empower researchers across Africa with hands-on training and foundational knowledge in Electroencephalography (EEG). EEG is a powerful, non-invasive tool for studying brain activity and advancing neurotechnological research.

This workshop aims to:

- Provide foundational knowledge about EEG technology and applications.
- Offer hands-on training in experimental design, EEG data collection, processing, and analysis.
- Facilitate interdisciplinary collaboration among researchers across Africa.
- Discuss the relevance of EEG research in addressing African health and societal challenges.

During this workshop, you will get:

- Expert-led lectures on EEG principles, signal processing, and analysis.
- Practical sessions on EEG equipment setup and data acquisition.
- Hands-on training in data analysis using popular tools and platforms.
- Networking opportunities with leading researchers and peers.
- Discussions on ethics, contextualization of neurotechnological research in Africa.

Participants will bring a laptop with a recent web browser for the hands-on data analysis sessions. We will provide WiFi and the analysis will be done using online and open-source tools, so you don’t need special software on your laptop.

## Company support

We would like to thank [TMSi, an Artinis company](https://www.tmsi.artinis.com/), for borrowing us an 64-channel [SAGA](https://www.tmsi.artinis.com/saga) EEG system for the practical hands-on sessions.

{% include image src="/assets/img/workshop/nigeria2025/artinis-tmsi.jpg" width="250" %}

We would like to thank [MathWorks](https://www.mathworks.com) for providing the licenses to run [MATLAB in the cloud](http://matlab.mathworks.com) for the data analysis hands-on sessions.  

{% include image src="/assets/img/workshop/nigeria2025/mathworks.jpg" width="250" %}

## Registration

Since it is a workshop with a hands-on format, we have a limited number of seats available. Pre-registration is now closed and we will make a selection of interested candidates with the aim to maximize the impact of the training.

## Practicalities

See the [African Brain Data Network](https://africanbraindatanetwork.com/) homepage for up to date information. If you have any queries please contact <africanbraindatanetwork@gmail.com>.

### Who

It is organized by Damian Eke, Eberechi Wogu, Victor Owoyele, Ore Ogundipe, Robert Oostenveld, Mikkel C. Vinding, and various others help with the organization.

The lectures and hands-on sessions will be presented by [Robert Oostenveld](https://www.ru.nl/personen/oostenveld-r) from Radboud University Nijmegen, the Netherlands, and [Mikkel C. Vinding](https://psychology.ku.dk/staff/academic_staff/?pure=en/persons/805933) from University of Copenhagen , Denmark. Both Robert and Mikkel have extensive experience with EEG, including designing the experiments, doing recordings, and analyzing data. You can find their publications [here](https://scholar.google.com/citations?user=eEbaa0UAAAAJ&hl=en&oi=ao) and [here](https://scholar.google.com/citations?user=v6A5dRgAAAAJ&hl=en&oi=sra).

### When

9-14 June, 2025

### Where

[Port Harcourt, Nigeria](https://www.google.com/maps/place/Port+Harcourt,+Rivers,+Nigeria/)

## Program

Day-by-Day Overview:

### Monday – Introduction & EEG Basics

The week begins with orientation and practical information, followed by foundational topics: what EEG is, its advantages over other neuroimaging techniques, and its applications in clinical, developmental, and cognitive research. Special emphasis is placed on African-specific challenges, such as dealing with natural hairstyles and electrode types. Sessions also address ethics, informed consent, and experimental design essentials, including noise, artifacts, attention, and stimulus control.

- registration and welcome
- introduction and format (lecture)
- background on EEG (lecture, 1st half)
- lunch
- background on EEG (lecture, 2nd half)
- EEG in Africa (lecture)
- experimental design part A (lecture)
- experimental design Q&A (discussion)

### Tuesday – Experimental Design & EEG Recording

Hands-on sessions guide participants through installing stimulus software (e.g., [PsychoPy](https://psychopy.org/)), designing behavioral tasks, and handling hardware (e.g., EEG caps, electrodes). Participants split into groups to practice recording EEG, focusing on setup, troubleshooting, ethical handling, and documentation.

- how does an EEG system work (lecture, 1st half)
- recording of EEG (hands-on)
- lunch
- experimental design part B (lecture)
- designing a task and recording it ([hands-on](/nigeria2025/stimuli))

### Wednesday – EEG Data & Analysis Tools

Lectures cover EEG data formats, metadata (e.g., BIDS), and an overview of the FieldTrip toolbox and alternatives. A comparison of clinical vs. cognitive EEG applications is provided, along with an introduction to analyzing event-related potentials (ERP), followed by practical exercises.

- synchronisation and triggers (lecture)
- synchronisation and triggers (demonstration)
- where to get EEG data (lecture)
- How to analyze EEG data (lecture)
- lunch
- preprocessing of EEG (lecture)
- preprocessing of EEG ([hands-on](/workshop/nigeria2025/preprocessing))
- wrap up (discussion)

### Thursday – Frequency & Time-Frequency Analysis

Participants explore frequency-based EEG analysis (e.g., eyes open vs. closed, group comparisons), and are introduced to time-frequency and connectivity analysis—highlighting both their promise and complexity. These topics include short lectures with hands-on practice.

- EEG and ethics (lecture)
- analysis of ERPs (lecture)
- analysis of ERPs ([hands-on](/workshop/nigeria2025/erp))
- lunch
- frequency analysis (lecture)
- frequency analysis ([hands-on](/workshop/nigeria2025/frequency))
- EEG and ethics - the African perspective (lecture by Damian)

### Friday – Statistical & Advanced Analyses

Topics include experimental design types, statistical approaches (e.g., mixed models, Bayesian methods), and multiple comparison correction. Advanced methods such as source reconstruction, BCI applications, and neurofeedback are discussed, with an emphasis on high-density EEG setups (32/64 channels).

- how does an EEG system work (lecture, 2nd half)
- source localization (lecture)
- lunch
- real-time analysis and BCI (lecture)
- experimental design (hands-on)
- recording of EEG (hands-on)

### Saturday – Wrap-up & Additional Practice

The final day is flexible, used for review, additional practice, or wrapping up unfinished work. Reflections on the week’s learning and experiences conclude the course.

- to be determined
- lunch
- to be determined

## Slides

The slides will be shared as PDF throughout the week. You can access them at [this google drive folder](https://drive.google.com/drive/folders/1NxpOnxtXyMpjNN8MBCh8ij7eOWDZbueO?usp=sharing).

## Questions

Please ask questions during or after the lectures. Your questions are also relevant for the other participants, who will learn from them as well. If you want, you can also type your questions in a [this shared google doc](https://docs.google.com/document/d/19gOTo8fyZUaatmGnmroixB9Un0by1j2CDvIelckCLSE/edit?usp=sharing). Feel free to add your name, or type your question anonymously. We will address the questions diring the day and/or towards the end of the afternoon.

## How to prepare

### Installing FieldTrip

Open MATLAB online and enter the following in the command window to download and install FieldTrip. Subsequently you should download the data as well.

    unzip('https://download.fieldtriptoolbox.org/workshop/nigeria2025/fieldtrip-20250517.zip')
    addpath('/MATLAB Drive/fieldtrip-20250517')
    ft_defaults

    unzip('https://download.fieldtriptoolbox.org/workshop/nigeria2025/data.zip')
    cd('/MATLAB Drive/data')

### Restarting MATLAB online

Whenever you restart MATLAB or when you are kicked out because of poor internet connectivity, you have to set up FieldTrip again.

    addpath('/MATLAB Drive/fieldtrip-20250517')
    ft_defaults
    cd('/MATLAB Drive/data')

It is important to save your edited m-files regularly, so that you can continue when you reconnect.

## Suggested reading material

### EEG background

- Buzsáki, G., Anastassiou, C. A., & Koch, C. (2012). The origin of extracellular fields and currents—EEG, ECoG, LFP and spikes. Nature Reviews Neuroscience, 13(6), 407–420. {% include badge doi="10.1038/nrn3241" %}
- Lopes da Silva, F. (2013). EEG and MEG: Relevance to Neuroscience. Neuron, 80(5), 1112–1128. {% include badge doi="10.1016/j.neuron.2013.10.017" %}
- Luck, S. J. (2014). An introduction to the event-related potential technique (Second edition). The MIT Press.

### Software

- Oostenveld, R., Fries, P., Maris, E., & Schoffelen, J.-M. (2011). FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data. Computational Intelligence and Neuroscience, 2011, 1–9. {% include badge doi="10.1155/2011/156869" %}
- Peirce, J., Gray, J. R., Simpson, S., MacAskill, M., Höchenberger, R., Sogo, H., Kastman, E., & Lindeløv, J. K. (2019). PsychoPy2: Experiments in behavior made easy. Behavior Research Methods, 51(1), 195–203. {% include badge doi="10.3758/s13428-018-01193-y" %}

### EEG in Africa

- Parker, T. C., & Ricard, J. A. (2022). Structural racism in neuroimaging: Perspectives and solutions. The Lancet Psychiatry, 9(5), e22. {% include badge doi="10.1016/S2215-0366(22)00079-7" %}
- Caspar, E. A. (2024). Guidelines for Inclusive and Diverse Human Neuroscience Research Practices. The Journal of Neuroscience, 44(48), e1971242024. {% include badge doi="10.1523/JNEUROSCI.1971-24.2024" %}
- Köhler, J., Reis, A. A., & Saxena, A. (2021). A survey of national ethics and bioethics committees. Bulletin of the World Health Organization, 99(2), 138–147. {% include badge doi="10.2471/BLT.19.243907" %}
- TRUST. (2018). The TRUST code -A Global Code of Conduct for Equitable Research Partnerships (Version 1). TRUST. {% include badge doi="10.48508/GCC/2018.05" %}
- The Inclusive EEG Handbook. (n.d.). Retrieved April 15, 2025, from <https://www.inclusiveneuro.com/home>.
- Etienne, A., Laroia, T., Weigle, H., Afelin, A., Kelly, S. K., Krishnan, A., & Grover, P. (2020). Novel Electrodes for Reliable EEG Recordings on Coarse and Curly Hair. BioRxiv. {% include badge doi="10.1101/2020.02.26.965202" %}
