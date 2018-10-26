---
title: Testing code quality
layout: default
---

<div class="alert-danger">
The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas. 

After making changes to the code and/or documentation, this page should remain on the wiki as a reminder of what was done and how it was done. However, there is no guarantee that this page is updated in the end to reflect the final state of the project

So chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
</div>

FIXME See also [/development/infrastructure_for_testing](/development/infrastructure_for_testing)

# Testing code quality

## Supported Matlab versions and operating systems

An overview of Matlab versions is available on the [Mathworks site](http://www.mathworks.com/support/sysreq/previous_releases.html).

 | Operating system | Matlab 6.1 | Matlab 6.5 | Matlab 7.0 | Matlab 7.1 | Matlab 7.2 | Matlab 7.3 | Matlab 7.4 | 
 | ---------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | 
 | Linux 32 bit     | XX (1)     | XX (1)     | OK (2)     | OK (2)     | OK         | n.a.       |            | 
 | Linux 64 bit     | n.a.       | n.a.       | OK (3)     | OK         | OK         | OK         |            | 
 | Windows 32 bit   |            |            |            | OK         |            |            |            | 
 | Macintosh PPC    | n.a.       |            |            |            |            |            |            | 
 | Macintosh Intel  | n.a.       | n.a.       | n.a.       | n.a.       | n.a.       |            |            | 
 | Windows 64 bit   | n.a.       | n.a.       | n.a.       | n.a.       | n.a.       |            |            | 

n.a. = matlab version is not available for this OS

XX = does not work

1) mySQL mex error: libmex.so: version v7.0 not found. Required by mysql.mexglx

2) mySQL mex error: libmex.so: version GCC_3.3 not found. Required by /usr/lib/libstdc++.so.6
The solution requires export LD_PRELOAD=/lib/libgcc_s.so.1, see [Mathworks technical solution 1-2H64MF](http://www.mathworks.com/support/solutions/data/1-2H64MF.html?product=CO&solution=1-2H64MF)

3) this version is not yet installed on mentat in a clean fashion, furthermore it requires
cd /opt/matlab70/sys/os/glnxa64
mv libgcc_s.so.1 libgcc_s.so.1.BAK

## Available Matlab versions within the FC Donders

Windows 32 bit

*  matlab 6.1

*  matlab 6.5

*  matlab 7.0

*  matlab 7.1

*  matlab 7.2

*  matlab 7.3

*  matlab 7.4

Windows 64 bit

*  matlab 7.3

*  matlab 7.4

Linux 32 bit

*  matlab 6.1

*  matlab 6.5

*  matlab 7.0

*  matlab 7.1

*  matlab 7.2

*  matlab 7.4 (?)

Linux 64 bit

*  matlab 7.0

*  matlab 7.1

*  matlab 7.2

*  matlab 7.3

*  matlab 7.4

Macintosh PPC

*  matlab 6.5

*  matlab 7.0

*  matlab 7.1

*  matlab 7.2

*  matlab 7.3

*  matlab 7.4

Macintosh Intel

*  matlab 7.3

*  matlab 7.4

