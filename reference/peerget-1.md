---
title: peerget
---
```
 PEERGET get the output arguments after the remote job has been executed.

 Use as
   jobid  = peerfeval(fname, arg1, arg2, ...)
   argout = peerget(jobid, ...)

 Optional arguments can be specified in key-value pairs and can include
   StopOnError    = boolean (default = true)
   timeout        = number, in seconds (default = 1)
   sleep          = number, in seconds (default = 0.01)
   output         = string, 'varargout' or 'cell' (default = 'varargout')
   diary          = string, can be 'always', 'warning', 'error' (default = 'error')

 See also PEERFEVAL, PEERCELLFUN
```
