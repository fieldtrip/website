---
title: qsubfeval
---
```
 QSUBFEVAL evaluates the specified MATLAB function on the input arguments
 using the Torque, SGE, PBS or SLURM batch queue system.

 Use as
   jobid  = qsubfeval(fname, arg1, arg2, ...)
   argout = qsubget(jobid, ...)

 This function has a number of optional arguments that have to passed
 as key-value pairs at the end of the list of input arguments. All other
 input arguments (including other key-value pairs) will be passed to the
 function to be evaluated.
   memreq      = number in bytes, how much memory does the job require (no default)
   memoverhead = number in bytes, how much memory to account for MATLAB itself (default = 1024^3, i.e. 1GB)
   timreq      = number in seconds, how much time does the job require (no default)
   timoverhead = number in seconds, how much time to allow MATLAB to start (default = 180 seconds)
   backend     = string, can be 'torque', 'sge', 'slurm', 'lsf', 'system', 'local' (default is automatic)
   diary       = string, can be 'always', 'never', 'warning', 'error' (default = 'error')
   queue       = string, which queue to submit the job in (default is empty)
   waitfor     = string or cell-array of strings, jobids of jobs to wait on finishing
                 before executing the current job (default is empty)
   options     = string, additional options that will be passed to qsub/srun (default is empty)
   batch       = number, of the bach to which the job belongs. When called by QSUBCELLFUN
                 it will be a number that is automatically incremented over subsequent calls.
   batchid     = string that is used for the compiled application filename and to identify
                 the jobs in the queue, the default is automatically determined and looks
                 like user_host_pid_batch.
   matlabcmd   = string, the Linux command line to start MATLAB on the compute nodes (default is automatic
   display     = 'yes' or 'no', whether the nodisplay option should be passed to MATLAB (default = 'no', meaning nodisplay)
   jvm         = 'yes' or 'no', whether the nojvm option should be passed to MATLAB (default = 'yes', meaning with jvm)
   rerunable   = 'yes' or 'no', whether the job can be restarted on a torque/maui/moab cluster (default = 'no')

 See also QSUBCELLFUN, QSUBGET, FEVAL, DFEVAL, DFEVALASYNC
```
