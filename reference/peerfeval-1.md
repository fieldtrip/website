---
title: peerfeval
---
```
 PEERFEVAL execute the specified function on another peer.

 Use as
   jobid  = peerfeval(fname, arg1, arg2, ...)
   argout = peerget(jobid, ...)

 This function has a number of optional arguments that have to passed
 as key-value pairs at the end of the list of input arguments. All other
 input arguments (including other key-value pairs) will be passed to the
 function to be evaluated.
   timeout  = number, in seconds (default = inf)
   sleep    = number, in seconds (default = 0.01)
   memreq   = number, in bytes   (default = 0)
   timreq   = number, in seconds (default = 0)
   hostid   = number, only evaluate on a particular host
   diary    = string, can be 'always', 'warning' or 'error'

 Example
   jobid  = peerfeval('unique', randn(1,10));
   argout = peerget(jobid, 'timeout', inf);
   disp(argout);

 See also PEERGET, PEERCELLFUN, PEERMASTER, PEERSLAVE, FEVAL, DFEVAL, DFEVALASYNC
```
