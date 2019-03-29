---
title: qsubcellfun
---
```
 QSUBCELLFUN applies a function to each element of a cell-array. The
 function execution is done in parallel using the Torque, SGE, PBS or
 SLURM batch queue system.

 Use as
   argout = qsubcellfun(fname, x1, x2, ...)

 This function has a number of optional arguments that have to passed
 as key-value pairs at the end of the list of input arguments. All other
 input arguments (including other key-value pairs) will be passed to the
 function to be evaluated.
   UniformOutput  = boolean (default = false)
   StopOnError    = boolean (default = true)
   diary          = string, can be 'always', 'never', 'warning', 'error' (default = 'error')
   timreq         = number, the time in seconds required to run a single job
   timoverhead    = number in seconds, how much time to allow MATLAB to start (default = 180 seconds)
   memreq         = number, the memory in bytes required to run a single job
   memoverhead    = number in bytes, how much memory to account for MATLAB itself (default = 1024^3, i.e. 1GB)
   stack          = number, stack multiple jobs in a single qsub job (default = 'auto')
   backend        = string, can be 'torque', 'sge', 'slurm', 'lsf', 'system', 'local' (default is automatic)
   batchid        = string, to identify the jobs in the queue (default is user_host_pid_batch)
   compile        = string, can be 'auto', 'yes', 'no' (default = 'no')
   queue          = string, which queue to submit the job in (default is empty)
   options        = string, additional options that will be passed to qsub/srun (default is empty)
   matlabcmd      = string, the Linux command line to start MATLAB on the compute nodes (default is automatic
   display        = 'yes' or 'no', whether the nodisplay option should be passed to MATLAB (default = 'no', meaning nodisplay)
   jvm            = 'yes' or 'no', whether the nojvm option should be passed to MATLAB (default = 'yes', meaning with jvm)
   rerunable      = 'yes' or 'no', whether the job can be restarted on a torque/maui/moab cluster (default = 'no')
   sleep          = number, time in seconds to wait between checks for job completion (default = 0.5 s)

 It is required to give an estimate of the time and memory requirements of
 the individual jobs. The memory requirement of the MATLAB executable
 itself will automatically be added, just as the time required to start
 up a new MATLAB process. If you don't know what the memory and time
 requirements of your job are, you can get an estimate for them using
 TIC/TOC and MEMTIC/MEMTOC around a single execution of one of the jobs in
 your interactive MATLAB session. You can also start with very large
 estimates, e.g. 4*1024^3 bytes for the memory (which is 4GB) and 28800
 seconds for the time (which is 8 hours) and then run a single job through
 qsubcellfun. When the job returns, it will print the memory and time it
 required.

 Example
   fname = 'power';
   x1    = {1, 2, 3, 4, 5};
   x2    = {2, 2, 2, 2, 2};
   y     = qsubcellfun(fname, x1, x2, 'memreq', 1024^3, 'timreq', 300);

 Using the compile=yes or compile=auto option, you can compile your
 function into a stand-alone executable that can be executed on the cluster
 without requiring additional MATLAB licenses. You can also call the
 QSUBCOMPILE function prior to calling QSUBCELLFUN. If you plan multiple
 batches of the same function, compiling it prior to QSUBCELLFUN is more
 efficient. In that case you will have to delete the compiled executable
 yourself once you are done.

 In case you abort your call to qsubcellfun by pressing ctrl-c,
 the already submitted jobs will be canceled. Some small temporary
 files might remain in your working directory.

 To check the the status and healthy execution of the jobs on the Torque
 batch queuing system, you can use
   qstat
   qstat -an1
   qstat -Q
 comands on the linux command line. To delete jobs from the Torque batch
 queue and to abort already running jobs, you can use
   qdel <jobnumber>
   qdel all

 See also QSUBCOMPILE, QSUBFEVAL, CELLFUN, PEERCELLFUN, FEVAL, DFEVAL, DFEVALASYNC
```
