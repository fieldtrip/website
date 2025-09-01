---
title: Testing code quality
---

{% include /shared/development/warning.md %}

FIXME See also [/development/infrastructure_for_testing](/development/project/infrastructure_for_testing)


## Supported MATLAB versions and operating systems

An overview of MATLAB versions is available on the [MathWorks site](http://www.mathworks.com/support/sysreq/previous_releases.html).

| Operating system | MATLAB 6.1 | MATLAB 6.5 | MATLAB 7.0 | MATLAB 7.1 | MATLAB 7.2 | MATLAB 7.3 | MATLAB 7.4 |
| ---------------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| Linux 32-bit     | XX (1)     | XX (1)     | OK (2)     | OK (2)     | OK         | n.a.       |            |
| Linux 64-bit     | n.a.       | n.a.       | OK (3)     | OK         | OK         | OK         |            |
| Windows 32-bit   |            |            |            | OK         |            |            |            |
| Macintosh PPC    | n.a.       |            |            |            |            |            |            |
| Macintosh Intel  | n.a.       | n.a.       | n.a.       | n.a.       | n.a.       |            |            |
| Windows 64-bit   | n.a.       | n.a.       | n.a.       | n.a.       | n.a.       |            |            |

n.a. = MATLAB version is not available for this OS

XX = does not work

1. mySQL mex error: libmex.so: version v7.0 not found. Required by mysql.mexglx

2. mySQL mex error: libmex.so: version GCC_3.3 not found. Required by /usr/lib/libstdc++.so.6
   The solution requires export LD_PRELOAD=/lib/libgcc_s.so.1, see [MathWorks technical solution 1-2H64MF](http://www.mathworks.com/support/solutions/data/1-2H64MF.html?product=CO&solution=1-2H64MF)

3. this version is not yet installed on mentat in a clean fashion, furthermore it requires
   cd /opt/matlab70/sys/os/glnxa64
   mv libgcc_s.so.1 libgcc_s.so.1.BAK

## Available MATLAB versions within the FC Donders

Windows 32-bit

- MATLAB 6.1

- MATLAB 6.5

- MATLAB 7.0

- MATLAB 7.1

- MATLAB 7.2

- MATLAB 7.3

- MATLAB 7.4

Windows 64-bit

- MATLAB 7.3

- MATLAB 7.4

Linux 32-bit

- MATLAB 6.1

- MATLAB 6.5

- MATLAB 7.0

- MATLAB 7.1

- MATLAB 7.2

- MATLAB 7.4 (?)

Linux 64-bit

- MATLAB 7.0

- MATLAB 7.1

- MATLAB 7.2

- MATLAB 7.3

- MATLAB 7.4

Macintosh PPC

- MATLAB 6.5

- MATLAB 7.0

- MATLAB 7.1

- MATLAB 7.2

- MATLAB 7.3

- MATLAB 7.4

Macintosh Intel

- MATLAB 7.3

- MATLAB 7.4
