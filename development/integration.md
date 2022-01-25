---
title: Integration between tools
---

# Integration between tools

For the documentation, communication and development of the FieldTrip project we use various tools. This page lists the tools and the integrations between them.

## Jekyll

We use <https://jekyllrb.com> for our website. The markdown documents are hosted on [GitHub](https://github.com/fieldtrip/website) and use a webhook to trigger the rebuild of the static html files on the web server. The web server is hosted as a virtual machine at the DCCN.

## Mailman

We use this for a number of email discussion lists. It is hosted by C&CZ at <http://mailman.science.ru.nl>.

## Twitter

We use <http://twitter.com/fieldtriptoolbx> to notify people about updates. Commits of new code are automatically tweeted.

## Bitly

We use <https://bitly.com> to automatically create short URLs that are included in the tweets.

## Shields

We use <https://shields.io> to generate badges for the DOIs, PMIDs and PMCIDs.

## YouTube

We use a YouTube [video channel](https://www.youtube.com/fieldtriptoolbox) that contains video recordings of lectures. More details are [here](/video) and [here](/development/guideline/video).

## GitHub

We use git and GitHub for version control of the software and of the website, and for managing external contributions. More details can be found [here](/development/git). We also maintain a copy of the repository on [BitBucket](#bitbucket) and on [Gitlab](#gitlab).

If changes are pushed to GitHub, a webhook is triggered. The code for that is maintained at <http://github.com/fieldtrip/automation>.

## Bitbucket

A copy of the git repository of the FieldTrip software is maintained on <https://bitbucket.org/fieldtriptoolbox/fieldtrip>, although the primary site is on [GitHub](#GitHub).

## Gitlab

A copy of the git repository of the FieldTrip software is stored on <https://gitlab.com/fieldtrip/fieldtrip>, although the primary site is on [GitHub](#GitHub).

## Google search

We use Google to provide the search functionality on the website and discussion list archives.

## Plausible

We use [Plausible](http://plausible.io/) on a self-hosted server to count website visitors and to see which pages are visited most.

## Ftp

We use the DCCN [FTP server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/) to distribute the software releases and tutorial data.

## Central storage

At the DCCN we have a central storage system (i.e. a large shared network drive) on which an up-to-date copy of the software is maintained. Also the test data used for development and regression testing with the [dashboard](#dashboard) is on central storage.

## Dashboard

We have a set of MATLAB and Bash scripts for regression testing. This allows to do semi-automatic runs of all the test scripts on the DCCN compute cluster. We refer to this as the [test dashboard](/development/testing). The code is hosted on [GitHub](https://github.com/fieldtrip/dashboard) and the MATLAB interface is implemented in **[ft_test](https://github.com/fieldtrip/fieldtrip/blob/release/ft_test.m)**, which you can find in the utilities folder.

## Mixpanel

We are experimenting with MixPanel for software usage tracking. More details are [here](/faq/tracking).

## Slack

We are experimenting with [Slack](https://fieldtriptoolbox.slack.com) as a messaging tool for the development team.

## Bugzilla - obsolete

In the past we used [Bugzilla](http://www.bugzilla.org) as an "issue tracker". This allows to maintain and distribute to-do lists and supports the follow up communication with users that report problems or suggestions. Our bugzilla server is still online for reference and can be found at <http://bugzilla.fieldtriptoolbox.org>.

## Dokuwiki - obsolete

In the past we used [dokuwiki](http://dokuwiki.org/) as the CMS system for our website.

## SVN - obsolete

We used to do the development with Subversion (also known as SVN). As of February 2016 we have moved all development over to git and GitHub.

## CVS - obsolete

We initially used Concurrent Versions System (CVS) as the version control system.  At a certain point we followed the example from the SPM developers and switched to SVN to facilitate collaboration between more contributors.

## Google Code - obsolete

We used to maintain a copy of the SVN repository with the software on [Google Code](http://code.google.com/p/fieldtrip) but in 2015 Google stopped support for it. Right now there is only a link to the FieldTrip website.

## Google Analytics - obsolete

We used Google Analytics to collect website usage statistics. In January 2022 we switched to Plausible.

## Sourceforge - obsolete

We used to maintain a copy of the SVN repository with the software on [SourceForge](https://sourceforge.net/projects/fieldtrip/) but are now not actively using it any more.

## Facebook - obsolete

We used <http://facebook.com/fieldtriptoolbox> to announce events and to post photos and messages that relate to the social interaction between developers and users. The Facebook page is **not** used to provide support. In the past we also listed people who like our Facebook page on the start page. or linked in news items to photos from Facebook albums. Due to privacy concerns we stopped using FaceBook.
