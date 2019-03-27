---
title: I am having problems downloading from the FTP server
tags: [faq, download]
---

# I am having problems downloading from the FTP server

The FieldTrip source code and example datasets are released to the general public on our ftp server. This server requires an anonymous login. This means that you use the username "anonymous" and your password as email address. In case you don't want to share your email address, you can use any string that is formatted as a valid email address (e.g. anonymous@example.com).

The ftp service runs on a shared server which occasionally has a performance bottleneck. If you cannot connect, please try again at a later time (i.e. one hour later, or the next day).

If you have difficulties using the ftp server (especially using a macOS or Linux command line ftp client), you can try to turn off "Extended Passive Mode" by typing "epsv".

Some ftp clients may have problems with specific firewall configurations. This can be due to both the firewall on your side and the firewall on our side. If you have problems downloading, please try with another [ftp client](http://www.google.com/search?q=ftp+client).

## GitHub as alternative to the FTP download

The FieldTrip source code is maintained and also available from <http://github.com/fieldtrip/fieldtrip/>. You can use git and github to keep up to date with the latest updates of the source code, to revert to older versions, and to track all individual changes to the files. Furthermore, you can suggest improvements to the code by forking the FieldTrip project on github, making the change in your clone and by sending us a pull request.

Using the GitHub version is the easiest if you install a git client on your computer. However, it is also possible to simply download the latest version of the code as a [zip file](https://github.com/fieldtrip/fieldtrip/archive/master.zip).
