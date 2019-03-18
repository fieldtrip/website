---
title: Welcome to the FieldTrip website
---

# Welcome to the FieldTrip website

FieldTrip is the MATLAB software toolbox for MEG and EEG analysis that is being developed by a team of researchers at the [Donders Institute for Brain, Cognition and Behaviour](http://www.ru.nl/donders) in Nijmegen, the Netherlands in close collaboration with [collaborating institutes](/external_links#collaborating_institutes). The development of FieldTrip currently receives support from the [ChildBrain](http://www.childbrain.eu) project and from [the Netherlands Organization for Scientific Research (NWO)](http://www.nwo.nl) and has previously been supported by the [Human Connectome](http://humanconnectome.org) project and [BrainGain](http://www.braingain.nl).

The toolbox offers advanced analysis methods of MEG, EEG, and invasive electrophysiological data, such as time-frequency analysis, source reconstruction using dipoles, distributed sources and beamformers and non-parametric statistical testing. It supports the [data formats](/faq/dataformat) of all major MEG systems (CTF, Neuromag/Elekta/Megis, BTi/4D, Yokogawa/Ricoh) and of most popular EEG systems, and new formats can be added easily. FieldTrip contains high-level functions that you can use to construct your own analysis protocols in MATLAB. Furthermore, it easily allows methods researchers to incorporate new methods for EEG/MEG analysis.

The FieldTrip software is released free of charge as [open source software](http://en.wikipedia.org/wiki/Open_source) under the GNU [general public license](http://www.gnu.org/copyleft/gpl.html).

{% include markup/warning %}
Please cite the FieldTrip reference paper when you have used FieldTrip in your study.

Robert Oostenveld, Pascal Fries, Eric Maris, and Jan-Mathijs Schoffelen. **[FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data.](http://www.hindawi.com/journals/cin/2011/156869)** Computational Intelligence and Neuroscience, vol. 2011, Article ID 156869, 9 pages, 2011. doi:10.1155/2011/156869.
{% include markup/end %}

To get started with FieldTrip, please continue reading the [getting started](/getting_started) documentation.

{% include facebook %}

## News and announcements

### 13 March, 2019

Check it out! Matthias Treder has kindly contributed a tutorial and some code (streamlined a bit by yours truly) that now allows you to perform MVPA analysis in FieldTrip, using his awesome [MVPA-light toolbox](https://github.com/treder/MVPA-Light) ! For now it is well supported, documented and tested for channel level time domain data, but in the near future (and with your help) we will also ensure support for frequency domain and source level data. For now you can just use **[ft_timelockstatistics](/reference/ft_timelockstatistics)** with cfg.method='mvpa'. The tutorial can be found in the [tutorial section](/tutorial/mvpa_light)

### 11 January, 2019

All the best wishes for the new year to all of you on behalf of the FieldTrip team! According to Google Scholar, the FieldTrip paper has now been cited more than 3000 times. We are happy that the project provides so many of you with helpful tools that facilitate you to contribute to the scientific community.

### 20 December, 2018

Today we had our end-of-year poster session at the Donders Institute, during which also the Donders Cube has been awarded. This is an institutional award that acknowledges 'beyond-call-of-duty' contributions to the scientific and social life of the Donders Institute, and beyond. We are pleased that this year's award has been awarded to the FieldTrip team! We are proud to be able to work on such a nice project, which wouldn't be in its present shape if it weren't from the interactions with and contributions from the whole FieldTrip community! So, let's keep up the good work for the new year to come, and for now all the best for the holiday season.

{% include image src="/assets/img/index/donderscube.png" width="300" %}

### 5 December, 2018

We have completed the move to the new website which you are now seeing. See this [message on the mailing list](https://mailman.science.ru.nl/pipermail/fieldtrip/2018-December/012579.html) for details. The [old website](http://old.fieldtriptoolbox.org) is still available in case you want to look up something there.

If you want to edit any page on this website, please click the "Edit this page on GitHub" link at the bottom of each page. This brings you to [github](https://github.com/fieldtrip/website) where you can click the "pen" symbol in the upper right corner. Or have a look at our [git and github](/development/git/) tutorial.

### 09 October, 2018

Tzvetan has published a new paper, entitled [FieldTrip made easy: An Analysis Protocol for Group Analysis of the Auditory Steady State Brain Response in Time, Frequency, and Space](https://www.frontiersin.org/articles/10.3389/fnins.2018.00711/full). Go and check it out!

## Recent improvements to the code

All changes to the code can be tracked on [Twitter](http://twitter.com/fieldtriptoolbx) and [Github](/development/git).
