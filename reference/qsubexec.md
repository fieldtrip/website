---
title: qsubexec
---
```
 QSUBEXEC is a helper function to execute a job on the Torque, SGE, PBS
 or SLURM batch queue system. Normally you should not start this function
 yourself, but rather use QSUBCELLFUN or QSUBFEVAL.

 This function performs the following tasks
 - load the function name, input arguments and further options from the input file
 - evaluate the desired function on the input arguments using PEEREXEC
 - save the output arguments to an output file

 This function should be started from the linux command line as follows
   qsub /opt/bin/matlab -r "qsubexec(jobid); exit"
 which starts the MATLAB executable, executes this function and exits
 MATLAB to leave your batch job in a clean state. The jobid is
 automatically translated into the input and output file names, which
 have to reside on a shared network file system.

 See also QSUBCELLFUN, QSUBFEVAL, QSUBGET
```
