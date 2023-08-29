---
title: Advanced MEG/EEG toolkit at the Donders
tags: [toolkit2021]
---

# Advanced MEG/EEG toolkit at the Donders

From 19-23 April 2021 we will host the “Advanced MEG/EEG toolkit”. Although we would have loved to welcome you in-person in Nijmegen, the ongoing COVID situation restricts traveling and large meetings. However, [last year](/workshop/toolkit2020) we experienced that in an online format the toolkit course is also really fun, effective and rewarding!

Organizers: Robert Oostenveld and Jan-Mathijs Schoffelen.

The toolkit course is aimed at PhD and postdoctoral researchers that already have some experience with EEG and/or MEG data acquisition (either a pilot or a full study) and that have a good understanding of their own experimental design. Furthermore, we expect that you know the basics of MATLAB and that you already have some experience with MEG/EEG preprocessing and analysis. We will teach you advanced data analysis methods and cover preprocessing, frequency analysis, source reconstruction, connectivity and various statistical methods. Furthermore, we will give attention to good practices for reproducible research, Open Data and Open Science.

The toolkit will consist of a number of interactive online lectures, followed by Q&A sessions. Besides lectures we will have interactive hands-on sessions in which you will be tutored through the complete analysis of a MEG/EEG data set using the FieldTrip toolbox. There will be plenty of opportunity to interact and also ask questions about your research and data. On the final day you will have the opportunity to work on your own dataset under supervision of skilled tutors.

{% include markup/info %}
The number of participants is limited to ensure good interaction and sufficient individual attention to participants. The pre-registration has closed and participants that have been selected have been informed about this.
{% include markup/end %}

## Program

All interactive sessions will take place between 10:00 and 17:00 CET, i.e. centered on the Central European time zone. To benefit from the format and interaction, we require participants to attend in that time. For some participants that might mean that they have to get up very early, while others might have to stay up very late. Please check <http://time.is/CET> to see how our time zone compares to yours.

We will also record the lectures and provide them for offline viewing at another moment, but especially the participation in Q&A and hands-on sessions requires you being online at the same time as us. If you cannot attend online, but want to watch the lectures anyway, have a look at the [online videos](/video) from previous years.

To try and accommodate time-zone differences a little bit, we will also provide opportunities for more informal interactions among each other and with the tutors early in the morning and in the evening. Note that these do not replace interaction during the core of the day.

This is the [public URL to the calendar](https://calendar.google.com/calendar/embed?src=lqm5cfqalbdfi1hen59r889rdg%40group.calendar.google.com) that you can view online.

This is the [public address in iCal format](https://calendar.google.com/calendar/ical/lqm5cfqalbdfi1hen59r889rdg%40group.calendar.google.com/public/basic.ics) that you can add to your calendar application.

<div class="video-container">
<iframe src="https://calendar.google.com/calendar/embed?src=lqm5cfqalbdfi1hen59r889rdg%40group.calendar.google.com&ctz=Europe%2FAmsterdam" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
</div>

## Zoom meeting links

The links to the Zoom meeting rooms will be shared in due time with the participants. Please do not distribute them, we do not want to be zoom-bombed. We will have a different link every day, but will stay in the same Zoom room throughout the day, also for the Q&A and hands-on sessions.

## Q&A sessions

During the Q&A following the lectures we will go through any remaining questions that we have collected in the Google doc that we will share with you at the start of each lecture. This will be an interactive session and you can also directly ask your questions here or contribute to the discussion.

## Hands-on sessions

In the hands-on sessions we will take you through selected FieldTrip tutorials. You execute these yourself on your own computer, that is why you need to have access to MATLAB. In the hands-on sessions we will focus on consolidating the knowledge you acquired during the lectures and we translate it into practical steps in your analysis.

## Playground

During the "playground" sessions you will apply your newly acquired skills to the analysis of your own data. We will be there to help you with questions and help you to build an analysis pipeline for your research question. We do expect that participants have (some) experience with experimental design and data collection, but in case you don't have suitable data yet: we caln provide you with data from a variety of EEG or MEG systems and with a variety of experimental paradigms.

## Practicalities

### 1. Slack for communication

It is easy to get lost in the online world. Not finding the right Zoom link or Google doc, or not knowing which specific URL to follow. Also, when working in breakout rooms you may have a question and get the attention of one of the tutors.

To ensure that we always can find each other, that we can share links and material, and that you can reach the team of tutors (which changes a bit from day to day), we will use Slack. All participants will receive an invitation to join and we will already start using this a few days in advance.

### 2. Ensure that you have MATLAB installed on your computer

This should be a MATLAB version > 2016b. For people who use a computer at the DCCN we recommend using a VNC session on the compute cluster, rather than using a remote desktop connection to your PC.

### 3. Ensure that you have an up-to-date version of FieldTrip

For people that **do not** use a computer at the DCCN:

Download the latest release version of the FieldTrip toolbox from [here](https://github.com/fieldtrip/fieldtrip/releases). For those of you familiar with git, you can also clone directly from GitHub with

      git clone https://github.com/fieldtrip/fieldtrip.git
      git checkout release

Please note that the stable release version corresponds to the "release" branch, and the cutting-edge development version to the "master" branch (which might be a few steps ahead).

For people that **do** use a computer at the DCCN (either a PC via remote desktop or the DCCN cluster):

FieldTrip is installed on the cluster, on /home/common/matlab/fieldtrip. (on Windows PCs, this is usually mounted on H:\\common\\matlab\\fieldtrip. So you don’t need to download the latest release version of the FieldTrip toolbox from here or from here.

### 4. Download the handson data in advance, or check whether you can access it

For people that **do not** use a computer at the DCCN:

Download the [Subject01.zip](https://download.fieldtriptoolbox.org/tutorial/Subject01.zip) tutorial data required for the hands-on.

You should also download some pre-computed intermediate results for each tutorial. Please download all tutorial files in each directory, and keep them organized per directory.

-  [eventrelatedaveraging](https://download.fieldtriptoolbox.org/tutorial/eventrelatedaveraging/)
-  [timefrequencyanalysis](https://download.fieldtriptoolbox.org/tutorial/timefrequencyanalysis/)
-  [beamformer](https://download.fieldtriptoolbox.org/tutorial/beamformer/)
-  [statistics](https://download.fieldtriptoolbox.org/tutorial/cluster_permutation_timelock/)

Downloading will take some time, especially if everyone tries to do it at the same moment. So please download in advance!

For people that **do** use a computer at the DCCN (either a desktop PC via remote desktop or the DCCN compute cluster):

The data needed for the tutorials are available on `/home/common`, so if you are working on the compute cluster at the DCCN, you don’t need to download this in advance. If you insist on downloading the data in advance, you can follow the instructions below.

The raw MEG data set of ‘Subject01’, and associated data are located in `/home/common/matlab/fieldtrip/data`. Additional hands-on session specific data are located in  `/home/common/matlab/fieldtrip/data/ftp/tutorial`. These data are needed once we get to the respective hands-on session:

-   `/home/common/matlab/fieldtrip/data/ftp/tutorial/eventrelatedaveraging`
-   `/home/common/matlab/fieldtrip/data/ftp/tutorial/timefrequencyanalysis`
-   `/home/common/matlab/fieldtrip/data/ftp/tutorial/beamformer`
-   `/home/common/matlab/fieldtrip/data/ftp/tutorial/cluster_permutation_timelock`

### 5. Test your MATLAB and FieldTrip installation in advance

Since you will be working at home on your own computer (and occasionally share your screen with us), we recommend that you [test your MATLAB and FieldTrip installation in advance](/workshop/toolkit2021/test_installation). This check does not only serve to test your installation, but also checks that you know how to share your notes in a Google doc with the tutors.

## Code of conduct

Please spend a couple of minutes to have a look at our [Code of Conduct](/workshop/toolkit2021/code_of_conduct) to make sure we all are taking responsibility to look after each other and make sure we are contributing towards an inclusive and supportive community. Please let us know if you have any questions regarding it. All toolkit participants are responsible to follow the rules listed here, as well as making sure that everyone in the toolkit follows it.
