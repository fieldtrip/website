---
title: I am having problems downloading from the FTP server
tags: [faq, download]
---

# I am having problems downloading from the FTP server

The FieldTrip source code and the example and tutorial datasets are released to the general public on our [FTP server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/). This server requires an anonymous login; you should use the username "anonymous" and you can your your email address as password. In case you don't want to share your email address, you can use any string that is formatted as a valid email address (e.g. anonymous@example.com).

The FTP service runs on a shared server which occasionally has a performance bottleneck. If you cannot connect, please try again at a later time (i.e. one hour later, or the next day).

If downloading from the FTP server in  the web browser gives problems, please try with another web browser, or a specific [ftp client](http://www.google.com/search?q=ftp+client) such as [CyberDuck](https://cyberduck.io) or [FileZilla](https://filezilla-project.org).

If your difficulties are with a specialized FTP client (especially using a macOS or Linux command line ftp client), you can try to turn off "Extended Passive Mode" by typing "epsv".

## GitHub as alternative to the FTP download

The FieldTrip release versions are also available from <https://github.com/fieldtrip/fieldtrip/releases>.

You can also use git to keep up to date with the stable release version or the latest development updates of the source code on the `release` or `master` branch. This allows you to revert to older versions, and to track and inspect all individual changes to the files. Using the GitHub development version requires you to install a git client on your computer. See the [git tutorial](/development/git) for details.
