---
layout: default
---

##  QSUBEXEC

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help qsubexec".

`<html>``<pre>`
    `<a href=/reference/qsubexec>``<font color=green>`QSUBEXEC`</font>``</a>` is a helper function to execute a job on the Torque, SGE, PBS
    or SLURM batch queue system. Normally you should not start this function
    yourself, but rather use `<a href=/reference/qsubcellfun>``<font color=green>`QSUBCELLFUN`</font>``</a>` or `<a href=/reference/qsubfeval>``<font color=green>`QSUBFEVAL`</font>``</a>`.
 
    This function performs the following tasks
 1.  load the function name, input arguments and further options from the input file
 2.  evaluate the desired function on the input arguments using `<a href=/reference/peerexec>``<font color=green>`PEEREXEC`</font>``</a>`
 3.  save the output arguments to an output file
 
    This function should be started from the linux command line as follows
    qsub /opt/bin/matlab -r "qsubexec(jobid); exit"
    which starts the MATLAB executable, executes this function and exits
    MATLAB to leave your batch job in a clean state. The jobid is
    automatically translated into the input and output file names, which
    have to reside on a shared network file system.
 
    See also `<a href=/reference/qsubcellfun>``<font color=green>`QSUBCELLFUN`</font>``</a>`, `<a href=/reference/qsubfeval>``<font color=green>`QSUBFEVAL`</font>``</a>`, `<a href=/reference/qsubget>``<font color=green>`QSUBGET`</font>``</a>`
`</pre>``</html>`

