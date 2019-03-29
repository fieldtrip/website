---
title: Integration between tools
---

# Integration between tools

For the documentation, communication and development of the FieldTrip project we use various tools. This page lists the tools and the integrations between them.

## Jekyll

We use [Jekyll](https://jekyllrb.com) for our website. The markdown documents are hosted on [GitHub](https://github.com/fieldtrip/website) and use a webhook to trigger the rebuild of the static html files on the webserver. The webserver is hosted as a virtual machine at the DCCN.

## Mailman

We use this for a number of email discussion lists. It is hosted by C&CZ at <http://mailman.science.ru.nl>. Upon an email to the main FieldTrip mailing list, a tweet is send to <http://twitter.com/fieldtriptoolbx>. The Google search on the website also searches the email list archives.

## Facebook

We use <http://facebook.com/fieldtriptoolbox> to announce events and to post photos and messages that relate to the social interaction between developers and users. The Facebook page is not used to provide support. People who like our Facebook page are displayed on the start page. Photos from Facebook albums are often used in news messages on the start page.

## Twitter

We use <http://twitter.com/fieldtriptoolbx> to notify people about events. Commits of new code are automatically tweeted.

## Bitly

We use [Bitly](https://bitly.com) to automatically create short URLs that are included in the tweets.

## YouTube

We use a YouTube [video channel](https://www.youtube.com/fieldtriptoolbox) to distribute video recordings of lectures. More details are [here](/video) and [here](/development/guideline/video).

## GitHub

We use Git and GitHub for version control of the software and of the website, and for managing external contributions. More details can be found [here](/development/git). We also maintain a copy of the repository on [BitBucket](#bitbucket) and on [Gitlab](#gitlab).

If changes are pushed to github, a webhook is triggered. The code for that is maintained at <http://github.com/fieldtrip/webhook>.

## Bitbucket

A copy of the git repository of the FieldTrip software is stored on BitBucket, although the primary site is on [GitHub](#GitHub).

## Gitlab

A copy of the git repository of the FieldTrip software is stored on Gitlab, although the primary site is on [GitHub](#GitHub).

## Bugzilla

We use [Bugzilla](http://www.bugzilla.org) as an "issue tracker". It allows us to maintain and distribute to-do lists and supports the follow up communication with users that report problems or suggestions. It is hosted at the DCCN, more details can be found [here](/bugzilla)

## Google

We use Google to provide the search functionality on the website and discussion list archives. Furthermore, we use Google Analytics to collect usage statistics.

## Ftp

We use the DCCN [ftp server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/) to distribute a daily updated copy of the software and to distribute the tutorial data.

## Central storage

At the DCCN we have a central storage system (i.e. a large and shared network drive) on which an up-to-date copy of the software is maintained. Also the test data used for development and regression testing with the [dashboard](#dashboard) is on central storage.

## Dashboard

We have a set of MATLAB and Bash scripts for regression testing. This allows to do semi-automatic runs of all the test scripts on the DCCN compute cluster. We refer to this as the quality [dashboard](/development/dashboard). The code is hosted on [github](https://github.com/fieldtrip/dashboard) and the MATLAB interface is implemented in **[ft_test](/reference/ft_test)**, which you can find in the utilities folder.

## Mixpanel

We are experimenting with MixPanel to track the software usage. More details are [here](/faq/tracking).

## Slack

We are experimenting with [Slack](https://fieldtriptoolbox.slack.com) as a messaging tool for the development team.

## Dokuwiki - obsolete

In the past we used [dokuwiki](http://dokuwiki.org/) as the CMS system for our website.

## SVN - obsolete

We used to do the development with Subversion (also known as SVN). As of February 2016 we have moved all development over to git and github.

## Google Code - obsolete

We used to maintain a copy of the SVN repository with the software on [Google Code](http://code.google.com/p/fieldtrip) but in 2015 Google stopped support for it. Right now there is only a link to the FieldTrip website.

## Sourceforge - obsolete

We used to maintain a copy of the SVN repository with the software on [SourceForge](https://sourceforge.net/projects/fieldtrip/) but are now not actively using it any more.
