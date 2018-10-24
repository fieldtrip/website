---
layout: default
tags: faq tutorial documentation
---

## Can I get an offline version of the wiki documentation?

The FieldTrip wiki is implemented using Dokuwiki, which does not allow for easy generation of a pdf version. However, an (outdated) offline version of the documentation in html format is available {{:faq:fieldtrip-wiki.zip|here}}. Note that this offline version is not kept up to date and reflects the documentation around September 2009.  

You can download an offline copy with ''wget'', using the following comman

    wget --recursive --level=3 --domain fieldtrip.fcdonders.nl --page-requisites --html-extension --convert-links --reject pdf,"*backlink*","*revisions*","*edit*" fieldtrip.fcdonders.nl

Please not that the downloaded file names might contain characters that can be problematic on Windows machines.
