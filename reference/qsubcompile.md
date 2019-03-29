---
title: qsubcompile
---
```
 QSUBCOMPILE compiles your function into an standalone executable that can easily
 be distributed on a cluster by QSUBCELLFUN. Running a compiled version of your
 function does not take any additional MATLAB licenses. Note that it does require
 that the corresponding MATLAB run-time environment (MCR) is installed on your
 cluster.

 Use as
   compiledfun = qsubcompile(fname)
   argout      = qsubcellfun(compiledfun, argin, ...)
 or
   compiledfun = qsubcompile(fname)
   jobid       = qsubfeval(compiledfun, argin, ...)
   argout      = qsubget(jobid)

 Optional input arguments should be specified in key-value pairs
 and can include
   batchid     = string that is used for the compiled application filename 
                 and to identify the jobs in the queue, the default is
                 automatically determined and looks like user_host_pid_batch.
   toolbox     = string or cell-array with strings, additional Mathworks 
                 toolboxes to include (see below).
   executable  = string with the name of a previous compiled executable 
                 to start, which usually takes the form "run_xxx.sh". This 
                 implies that compilation does not have to be done.
   numthreads  = number of threads, can be 1 or inf (default = 1)

 When executing a single batch of jobs using QSUBCELLFUN, you can also
 compile your function on the fly with the compile flag like this
   argout      = qsubcellfun(fname, argin, ..., 'compile', 'yes')
 Using this syntax, the compiled function will be automatically cleaned
 up immediately after execution.

 If you need to include additional functions that are not automatically
 detected as dependencies by the MATLAB compiler, e.g. because using
 constructs like feval(sprintf(...)), you can specify fname as a
 cell-array. For example
   compiledfun = qsubcompile({@ft_definetrial, @trialfun_custom})

 If you need to include Mathworks toolboxes that are not automatically
 detected as dependencies by the MATLAB compiler, you can specify them
 like this
   compiledfun = qsubcompile(fname, 'toolbox', {'signal', 'image', 'stats'})

 A common problem for compilation is caused by the use of addpath in
 your startup.m file. Please change your startup.m file into
   if ~isdeployed
    % here goes the original content of your startup file
    % ...
   end

 If you want to execute the same function multiple times with different input
 arguments, you only have to compile it once. The name of the executable can be
 specified as input parameter, and the specified function within the executable
 can be re-execured. An example is specyfying the executable as run_fieldtrip.sh,
 which is a compiled version of the complete FieldTrip toolbox.

 See also QSUBCELLFUN, QSUBFEVAL, MCC, ISDEPLOYED
```
