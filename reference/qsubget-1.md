---
title: qsubget
---
```
 QSUBGET get the output arguments after the remote job has been executed
 on the Torque, SGE, PBS or SLURM batch queue system.

 Use as
   jobid  = qsubfeval(fname, arg1, arg2, ...)
   argout = qsubget(jobid, ...)

 Optional arguments can be specified in key-value pairs and can include
   StopOnError    = boolean (default = true)
   timeout        = number, in seconds (default = 0; return immediately if output cannot be gotten)
   sleep          = number, in seconds (default = 0.01)
   output         = string, 'varargout' or 'cell' (default = 'varargout')
   diary          = string, can be 'always', 'warning', 'error' (default = 'error')

 See also QSUBFEVAL, QSUBCELLFUN
```
