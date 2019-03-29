---
title: peercellfun
---
```
 PEERCELLFUN applies a function to each element of a cell-array. The
 function execution is done in parallel on all avaialble peers.

 Use as
   argout = peercellfun(fname, x1, x2, ...)

 This function has a number of optional arguments that have to passed
 as key-value pairs at the end of the list of input arguments. All other
 input arguments (including other key-value pairs) will be passed to the
 function to be evaluated.
   UniformOutput  = boolean (default = false)
   StopOnError    = boolean (default = true)
   RetryOnError   = number, number of retries for failed jobs expressed as ratio (default = 0.05)
   MaxBusy        = number, amount of slaves allowed to be busy (default = inf)
   diary          = string, can be 'always', 'never', 'warning', 'error' (default = 'error')
   timreq         = number, initial estimate for the time required to run a single job (default = 3600)
   mintimreq      = number, minimum time required to run a single job (default is automatic)
   memreq         = number, initial estimate for the memory required to run a single job (default = 2*1024^3)
   minmemreq      = number, minimum memory required to run a single job (default is automatic)
   order          = string, can be 'random' or 'original' (default = 'random')

 Example
   fname = 'power';
   x1    = {1, 2, 3, 4, 5};
   x2    = {2, 2, 2, 2, 2};
   y     = peercellfun(fname, x1, x2);

 See also PEERMASTER, PEERSLAVE, PEERLIST, PEERINFO, PEERFEVAL, CELLFUN, DFEVAL
```
