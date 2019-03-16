---
title: ft_version
---
```
 FT_VERSION returns the version and installation directory of FieldTrip

 FieldTrip is not released with version numbers as "2.0", "2.1", etc. Instead, we
 share our development version on http://github.com/fieldtrip. You can use git or
 subversion (svn) to make a local version of the repository. Furthermore, we release
 daily version as zip-file on our FTP server.

 If you access the development version using git, it is labeled with the hash of the
 latest commit like "128c693". You can access the specific version "XXXXXX" at
 https://github.com/fieldtrip/fieldtrip/commit/XXXXXX.

 If you access the development version using svn, it is labeled with the revision
 number like "rXXXXX", where XXXX is the revision number.

 The daily FTP release version is packaged as a zip file and its version is
 indicated with "YYMMDD" (year, month, day).

 Use as
   ft_version
 to display the latest revision number on screen, or
   [ftver, ftpath] = ft_version
 to get the version and the installation root directory.

 When using git for version control, you can also get additional information with
   ft_version revision
   ft_version branch
   ft_version clean

 See also FT_PLATFORM_SUPPORTS, VERSION, VER, VERLESSTHAN
```
