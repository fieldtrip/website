---
title: MEG-UK 2015 meeting
tags: [meg-uk-2015, mmfaces]
---

# MEG-UK 2015 meeting

The workshop highlights complementary analysis methods offered by FieldTrip and SPM. It is aimed at people who already have some MEG/EEG experience, who would like to improve their analysis skills and get a better overview of the features offered by FieldTrip and SPM. The topics that will be discussed include: statistical inference, source reconstruction, and connectivity. The aim of the workshop will be to demonstrate the different analysis methods available within FieldTrip and SPM, and how to apply them. Advantages/disadvantages of the different methods will be discussed.

## Organizational details

- When: Wednesday 7th January 2015 ([workshop](http://www.aston.ac.uk/lhs/research/centres-facilities/brain-centre/meg-uk-2015/workshop))
- When: Thursday 8th and Friday 9th January 2015 ([meeting](http://www.aston.ac.uk/lhs/research/centres-facilities/brain-centre/meg-uk-2015))
- Where: Aston University, Birmingham, UK.
- Who: Klaus Kessler is the local organiser and host.
- Faculty: Vladimir Litvak, Robert Oostenveld, Bernadette van Wijk, Gareth Barnes, Guillaume Flandin, Saskia Helbling, Ryszard Auksztulewicz, Johanna Zumer, Stephen Whitmarsh, Hongfang Wang.

## How should participants prepare for the workshop?

This workshop is an **advanced** workshop in which we will move beyond the material covered in the previous [FieldTrip course](/workshop/birmingham) or the [SPM EEG/MEG](http://www.fil.ion.ucl.ac.uk/spm/course/slides14-meeg) course.

Some familiarity with FieldTrip and SPM is required. Please read the [SPM EEG/MEG](http://www.hindawi.com/journals/cin/2011/852961) and [FieldTrip](http://www.hindawi.com/journals/cin/2011/156869/) reference papers to understand the toolbox design.

As time is limited for the lectures, we strongly recommend to watch the following online videos prior to the workshop. Note that these lectures are about one hour each, which means that you should **plan ahead and take your time** to go through them. It is your own responsibility to come well-prepared. Starting one day in advance will not cut it!

For SPM (all taken from <http://www.fil.ion.ucl.ac.uk/spm/course/video>)

- [The general linear model](http://www.fil.ion.ucl.ac.uk/spm/course/video/#MEEG_GLM)
- [Multiple comparisons problem and solutions](http://www.fil.ion.ucl.ac.uk/spm/course/video/#MEEG_MCP)
- [M/EEG source analysis in SPM](http://www.fil.ion.ucl.ac.uk/spm/course/video/#MEEG_Source)
- [Principles of Dynamic Causal Modelling](http://www.fil.ion.ucl.ac.uk/spm/course/video/#MEEG_PrincipleDCM)
- [DCM for evoked responses](http://www.fil.ion.ucl.ac.uk/spm/course/video/#MEEG_DCM_ERP)

For FieldTrip (all taken from <https://www.fieldtriptoolbox.org/video>)

- [FieldTrip toolbox introduction](https://www.youtube.com/watch?v=zOxCqcYmIfA)
- [Beamformer source reconstruction](https://www.youtube.com/watch?v=7eS11DtbIPw)
- [Measures of Connectivity](https://www.youtube.com/watch?v=LKrxdrntWcQ)
- [Cluster based randomisation statistics](https://www.youtube.com/watch?v=vOSfabsDUNg)

## Program

The programme mixes short theoretical sessions with hands-on computer assignments. The day ends with a supervised computer session where people are free to work on their dataset of choice.

{% include markup/blue %}
Please look at the [general instructions](/workshop/meg-uk-2015/general) for the hands-on sessions to start MATLAB and navigate to the data directory on the Aston computer-lab machines.
{% include markup/end %}

| 9:30 | [lecture](/assets/pdf/workshop/meg-uk-2015/lecture1.pdf) | General Linear Model | SPM | Vladimir Litvak |
| 10:00 | [hands-on](/workshop/meg-uk-2015/spm_stats) | General Linear Model | SPM | Guillaume Flandin |
| 10:30 | [lecture](/assets/pdf/workshop/meg-uk-2015/lecture2.pdf) | Non-Parametric Statistics | FieldTrip | Robert Oostenveld |
| 10:45 | [hands-on](/workshop/meg-uk-2015/fieldtrip-stats-demo) | Non-Parametric Statistics | FieldTrip | |
| 11:15 | | **Coffee** | | |
| 11:45 | [lecture](/assets/pdf/workshop/meg-uk-2015/lecture3.pdf) | Source analysis: Bayesian perspective | SPM | Gareth Barnes |
| 12:00 | [hands-on](/workshop/meg-uk-2015/spm_source) | Source analysis: Bayesian perspective | SPM | Saskia Helbling |
| 12:45 | [lecture](/assets/pdf/workshop/meg-uk-2015/lecture4.pdf) | Source analysis: beamforming | FieldTrip | Robert Oostenveld |
| 13:00 | [hands-on](/workshop/meg-uk-2015/fieldtrip-beamformer-demo) | Source analysis: beamforming | FieldTrip | |
| 13:30 | | **Lunch** | | |
| 14:30 | [lecture](/assets/pdf/workshop/meg-uk-2015/lecture5.pdf) | Connectivity measures | FieldTrip | Robert Oostenveld |
| 14:45 | [hands-on](/workshop/meg-uk-2015/fieldtrip-connectivity-demo) | Connectivity measures | FieldTrip | |
| 15:30 | [lecture](/assets/pdf/workshop/meg-uk-2015/lecture6.pdf) | Dynamic causal modeling | SPM | Bernadette van Wijk |
| 16:00 | [hands-on](/workshop/meg-uk-2015/dcm_tutorial) | Dynamic causal modeling | SPM | Ryszard Auksztulewicz |
| 16:30 | | **Tea** | | |
| 17:00-18:30 | hands-on | Playground | FieldTrip/SPM | |

All demonstrations will be using the same [dataset](/workshop/meg-uk-2015/dataset).

{% include markup/yellow %}
Following the workshop, the data has also been made available on the [download server](https://download.fieldtriptoolbox.org/example/meg-uk-2015/). You can download all example data that we used in Aston, except for the toolbox code itself. You should get the latest version of [FieldTrip](/download) and [SPM](http://www.fil.ion.ucl.ac.uk/spm/software/download.html) from their respective download pages.

Downloading the data to your own computer should allow you to go through the demonstrations once more, but now at your own pace.
{% include markup/end %}
