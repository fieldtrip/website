---
title: engineget
---
```
 ENGINEGET get the output arguments after the remote job has been executed.

 Use as
   jobid  = enginefeval(fname, arg1, arg2, ...)
   argout = engineget(jobid, ...)

 Optional arguments can be specified in key-value pairs and can include
   StopOnError    = boolean (default = true)
   timeout        = number, in seconds (default = 0, i.e. return immediately if output cannot be retrieved)
   sleep          = number, in seconds (default = 0.01)
   output         = string, 'varargout' or 'cell' (default = 'varargout')
   diary          = string, can be 'always', 'warning', 'error' (default = 'error')

 See also ENGINEFEVAL, ENGINECELLFUN, ENGINEPOOL
```
