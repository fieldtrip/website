---
title: Integration between tools
---

# Integration between tools

For the documentation, communication and development of the FieldTrip project we use various tools. This page lists the tools and the integration that we have implemented between them.

### Dokuwiki

We use [dokuwiki](http://dokuwiki.org/) as the CMS system on which our website is implemented. The CMS is hosted on a virtual machine at the DCCN. Upon an edit of the wiki, a tweet is send to http://twitter.com/fieldtriptoolbx.

### Mailman

We use this for a number of email discussion lists. It is hosted by C&CZ at http://mailman.science.ru.nl. Upon an email to the main FieldTrip mailing list, a tweet is send to http://twitter.com/fieldtriptoolbx.

### Facebook

We use http://facebook.com/fieldtriptoolbox to announce events and to post photo's and messages that relate to the social interaction between developers and users. The Facebook page is not used to provide support. People who like our Facebook page are displayed on the start page. Photo's from Facebook albums are often used in news messages on the start page.

### Twitter

We use http://twitter.com/fieldtriptoolbx to notify people about events. Wiki page edits, email messages to the discussion list and code commits are posted on the timeline.

### YouTube

We use a YouTube video channel to distribute video recordings of lectures. More details are [here](/video).

### Bugzilla

We use [Bugzilla](http://www.bugzilla.org) as an "issue tracker". It allows us to maintain and distribute to-do lists and supports the follow up communication with users that report problems or suggestions. It is hosted at the DCCN and details can be found [here](/bugzilla)

### GitHub

We use Git and GitHub for version control of the software and for managing external contributions. More details can be found [here](/development/git). We also maintain a copy of the same git repository on [BitBucket](#bitbucket).

Following a push to github, a web hook is triggered. The code for that is at http://github.com/fieldtrip/webhook and is running on a dedicated (Raspberry Pi) server.

### Bitbucket

A copy of the git repository of the FieldTrip software is maintained on BitBucket, although the primary site is on [GitHub](#GitHub).

### SVN - obsolete

We used to do the development with Subversion (also known as SVN). As of February 2016 we have moved all development over to git and github.

### Googlecode - obsolete

We used to maintain a copy of the SVN repository with the software on [Google code](http://code.google.com/p/fieldtrip) but in 2015 Google stopped support for it . Right now there is only a link to the FieldTrip website.

### Sourceforge - obsolete

We used to maintain a copy of the SVN repository with the software on [SourceForge](https://sourceforge.net/projects/fieldtrip/) but are now not actively using it any more.

### Bitly

We use [Bitly](https://bitly.com) to automatically create short URLs that are included in the tweets.

### Mixpanel

We are experimenting with MixPanel to track the software usage. More details are [here](/faq/tracking).

### Ftp

We use the DCCN ftp server to distribute a daily updated copy of the software.

### Central storage

Inside the DCCN we have a central storage system (i.e. a large and shared network drive) on which an up-to-date copy of the software is maintained. Also the test data used for development and for regression testing with the [dashboard](#dashboard) is on central storage.

### Google

We use Google to complement the internal [Dokuwiki](#Dokuwiki) search engine. If you start searching on the wiki, you'll get an initial results page that provides a Google search box for the wiki and for the discussion list archives.

### Dashboard

We have a set of MATLAB and Bash scripts for regression testing. This allows to do semi-automatic runs of all the test scripts on the DCCN compute cluster. We refer to this as the quality [dashboard](/development/dashboard). The code is hosted on [github](https://github.com/fieldtrip/dashboard) and the MATLAB interface is implemented in **[ft_test](/reference/ft_test)**, which you can find in the utilities folder.

### Slack

We are experimenting with [Slack](https://slack.com) as a messaging tool for the development team.
