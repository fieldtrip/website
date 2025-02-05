---
title: I am having problems downloading
category: faq
tags: [download, release]
redirect_from:
    - /faq/i_am_having_problems_downloading_from_the_ftp_server/
    - /faq/i_am_having_problems_downloading/
    - /faq/download_ftpproblem/
---

# I am having problems downloading

In the past we used an FTP server to distribute files, but as of April 2022 we switched to a new download server that can be found on <https://download.fieldtriptoolbox.org>.

It supports [WebDAV](https://en.wikipedia.org/wiki/WebDAV), which means that you can download individual files using your web browser. You can also download a complete directory (with subdirectories) at once using a specialized WebDAV client such as [CyberDuck](http://cyberduck.io/) or [FileZilla](http://filezilla-project.org/). On Windows and macOS you can even mount the WebDAV server as a “network file system” and treat it as a network drive.

## GitHub as alternative

The FieldTrip toolbox releases are also available as zip-files from <https://github.com/fieldtrip/fieldtrip/tags>.

Furthermore, you can use git to keep up to date with the stable release version or the latest development updates of the source code on the `release` or `master` branch, respectively. Using git allows you to revert to older versions, and to track and inspect all individual changes to the files.

Using the stable `release` or development `master` versions from GitHub requires that you have git client installed on your computer. When working on a Linux or macOS computer, git will probably be installed by default, so you can open a terminal and type

    git clone https://github.com/fieldtrip/fieldtrip.git fieldtrip
    cd fieldtrip
    git checkout release

To keep up to date with the latest release version, you would type

    cd fieldtrip
    git checkout release
    git pull upstream release
    
Although it is not required to just download the code, you could also make an account on GitHub and clone the FieldTrip repository there. That would allow you to contribute your suggestions and improvements back to the project as pull requests. See the [git tutorial](/development/git) for more details.
