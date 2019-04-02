---
title: enginepool
---
```
 ENGINEPOOL manages the pool of MATLAB engine workers that is available
 for distributed computing

 Use as
   enginepool open <number> <command>
   enginepool close
   enginepool info

 The number specifies how many MATLAB engines should be started. In general
 it is advisable to start as many engines as the number of CPU cores.

 The command is optional. It can be used to specify the MATLAB version
 and the command-line options. The default for Linux is
   command = "matlab -singleCompThread -nodesktop -nosplash"

 See also ENGINECELLFUN, ENGINEFEVAL, ENGINEGET
```
