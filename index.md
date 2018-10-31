---
title: Welcome to the FieldTrip wiki
layout: default
tags:
---

# Welcome to the FieldTrip website

FieldTrip is the MATLAB software toolbox for MEG and EEG analysis that is being developed by a team of researchers at the [Donders Institute for Brain, Cognition and Behaviour](http://www.ru.nl/donders) in Nijmegen, the Netherlands in close collaboration with [collaborating institutes](/external_links#collaborating_institutes). The development of FieldTrip currently receives support from the [ChildBrain](http://www.childbrain.eu) project and from [the Netherlands Organization for Scientific Research (NWO)](http://www.nwo.nl) and has previously been supported by the [Human Connectome](http://humanconnectome.org) project and [BrainGain](http://www.braingain.nl).

The toolbox offers advanced analysis methods of MEG, EEG, and invasive electrophysiological data, such as time-frequency analysis, source reconstruction using dipoles, distributed sources and beamformers and non-parametric statistical testing. It supports the [data formats](/dataformat) of all major MEG systems (CTF, Elekta/Neuromag, 4D/BTi, Yokogawa) and of most popular EEG systems, and new formats can be added easily. FieldTrip contains high-level functions that you can use to construct your own analysis protocols in MATLAB. Furthermore, it easily allows developers to incorporate low-level algorithms for new EEG/MEG analysis methods.

The FieldTrip software is released free of charge as [open source software](http://en.wikipedia.org/wiki/Open_source) under the GNU [general public license](http://www.gnu.org/copyleft/gpl.html).

{% include markup/warning %}
Please cite the FieldTrip reference paper when you have used FieldTrip in your study.

Robert Oostenveld, Pascal Fries, Eric Maris, and Jan-Mathijs Schoffelen. **[FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data.](http://www.hindawi.com/journals/cin/2011/156869)** Computational Intelligence and Neuroscience, vol. 2011, Article ID 156869, 9 pages, 2011. doi:10.1155/2011/156869.
{% include markup/end %}

To get started with FieldTrip, please continue reading the [getting started](/getting_started) documentation.

{% include facebook %}

# News and announcements

## 10 September, 2018

This website has been migrated to a new server.

## 04 September, 2018

Eleven EU countries have decided that all scientific publications funded by their respective national science councils should be full Open Access immediately upon publication. See this [blog post from PLOS](https://blogs.plos.org/plos/2018/09/open-access-publishing-forges-ahead-in-europe/), there is more news to follow in the coming days.

## 03 September, 2018

Here are the slides of the topics that we presented and discussed in the Open Science Panel session at the [BIOMAG 2018](http://www.biomag2018.org) conference in Philadelphia last week:

*  [Robert Oostenveld - Introduction](https://www.slideshare.net/RobertOostenveld/biomag2018-robert-oostenveld-open-science-intro)
*  [Guiomar Niso - BIDS and Omega](https://www.slideshare.net/RobertOostenveld/biomag2018-guiomar-niso-bids-and-omega)
*  [Darren Price - CamCAN](https://www.slideshare.net/RobertOostenveld/biomag2018-darren-price-camcan)
*  [Jan-Mathijs Schoffelen - COBIDAS](https://www.slideshare.net/RobertOostenveld/biomag2018-janmathijs-schoffelen-cobidas)
*  [Vladimir Litvak - Group Analyses in Frontiers](https://www.slideshare.net/RobertOostenveld/biomag2018-vladimir-litvak-frontiers)
*  [Tzvetan Popov - HCP User's Perspective](https://www.slideshare.net/RobertOostenveld/biomag2018-tzvetan-popov-hcp-from-a-users-perspective)
*  [Dennis Engemann - MNE-HCP](https://www.slideshare.net/RobertOostenveld/biomag2018-denis-engemann-mnehcp)

## 01 July, 2018

On June 29th, Robert and Jan-Mathijs taught at the Human Connectome Project's workshop, which this year took place in Oxford. During an intense one-week program, 105 participants learnt about the ins and outs of the Human Connectome Project (HCP). Did you know that the HCP consortium also collected (and partially analysed) MEG data from about 100 participants? And that this data is freely available for download? And that the analysis pipelines and software are also available to the community? Check it out on [https://www.humanconnectome.org](https://www.humanconnectome.org).

{% include image src="/static/img/ft_in_oxford.jpg" %}

## 12 June, 2018

On 17 June 2018 Maria Carla Piastra, Sophie Schrader and Simon Homölle will host a workshop the OHBM2018 conference. The course is aimed at researchers who want to learn how to do MEG and/or EEG source reconstruction. This intense one-day workshop will explain state-of-the-art MEG and EEG source reconstruction methods. Special emphasis will be given to new features available now in FieldTrip to solve the EEG and MEG forward solution with advanced finite element methods. The workshop will consist of a number of lectures, followed by hands-on sessions in which you will be tutored through the complete analysis of a MEG, EEG and MRI data set using the FieldTrip toolbox. As the focus is on source reconstruction, topics that will NOT be covered in great detail are segmenting, artifact handling, averaging, frequency and time-frequency analysis, statistics. For the hands-on sessions you should bring a laptop with MATLAB installed. More information about the program can be found at the OHBM website or [here](/workshop/ohbm2018).

## 6 March, 2018

Springer Nature has updated its policies - Nature journals now ask researchers who submit papers that rely on bespoke software to provide the programs for peer review. More details are in [this editorial](https://www.nature.com/articles/d41586-018-02741-4), the [guidelines to authors](https://www.nature.com/authors/policies/availability.html#code) have been updated and a [code and software submission checklist](http://www.nature.com/documents/GuidelinesCodePublication.pdf) is available.

# Recent improvements to the code

All changes to the code can be tracked on [Twitter](http://twitter.com/fieldtriptoolbx) and [Github](/development/git).
