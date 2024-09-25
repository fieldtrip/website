---
title: How to get started with distributed computing using qsub?
category: faq
tags: [qsub]
---

# How to get started with distributed computing using qsub?

The [FieldTrip qsub toolbox](https://github.com/fieldtrip/fieldtrip/tree/master/qsub) is a small stand-alone toolbox to facilitate distributed computing. The idea of the qsub toolbox is to provide you with an easy MATLAB interface to distribute your jobs and not have to go to the Linux command-line to use the qsub command from there. Besides the Torque cluster (which we have at the Donders in Nijmegen) it also supports Linux clusters with other PBS versions, Sun Grid Engine (SGE), Oracle Grid Engine, Slurm and LSF as batch queueing systems.

You should start by adding the qsub toolbox to your MATLAB path:

    >> addpath /home/common/matlab/fieldtrip/qsub/

### Submitting a single MATLAB job to the cluster

To submit a job to the cluster, you will use **[qsubfeval](/reference/qsub/qsubfeval)**. It stands for “qsub – evaluation - function”. As an input you specify a name of your function, an argument, and time and memory requirements (see below).

Try the following:

    jobid = qsubfeval('rand', 100, 'timreq', 60, 'memreq', 1024*1024*1024)

{% include markup/skyblue %}
Besides the memory requirements for your computation, MATLAB also requires memory for itself. The **[qsubfeval](/reference/qsub/qsubfeval)** and **[qsubcellfun](/reference/qsub/qsubcellfun)** functions have the option `memoverhead` for this, which is by default 1GB (which is 1024\*1024\*1024 bytes). The `memreq` option itself does not have a default value. The torque job is started with a memory reservation of `memoverhead + memreq`, which adds up to 2GB in this example.
{% include markup/end %}

You will get the job ID as the output:

    submitting job username_dccn_c004_p23910_b1_j001... qstat job id 1066196.dccn-l014.dccn.nl

    jobid =
      username_dccn_c004_p23910_b1_j001

Note, that qsubfeval does not return the output of your function to the command window! You only get the job ID. Your function thus has to include a command for writing the output on disk.

You can check the status of your submitted job with qstat command in Linux terminal.

```bash
    bash-3.2$ qstat
    Job id                    Name             User            Time Use S Queue
  ------------------------- ---------------- --------------- -------- - -----
  1066196.dccn-l014         ...23910_b1_j001 username        00:00:00 C MATLAB
```

For detailed information on the submitted job use qstat -f JobI

```bash
    bash-3.2$ qstat -f 1066196
    Job Id: 1066196.dccn-l014.dccn.nl
      Job_Name = username_dccn_c004_p23910_b1_j001
      Job_Owner = username@dccn-c004.dccn.nl
      resources_used.cput = 00:00:00
      resources_used.mem = 91232kb
      resources_used.vmem = 4181060kb
      resources_used.walltime = 00:00:02
  ...
```

The **[qsubfeval](/reference/qsub/qsubfeval)** command creates a bunch of temporary files in your working directory. STDIN.oXXX is the standard output, i.e. the output that MATLAB normally prints in the command window. STDIN.eXXX is an error message file. For the job to complete successfully, this file should be empty.

To pick up the results of the job, you type in matlab
    
    result = qsubget(jobid);
    
The matrix with the results contains 100x100 random numbers, just as you would get when calling `rand(100)` on the MATLAB command line. 

Rather than specifying the function `'rand'` as a string, you can also specify it as a [function handle](https://www.mathworks.com/help/matlab/matlab_prog/creating-a-function-handle.html) with `@rand`.

{% include markup/red %}
If you write your own function `@myfunction`, to be executed by `qsubfeval`, beware **NOT** to do something like `clear all`, `clear mex`, or `clear functions` inside your function, as this messes up the environment in which the job gets executed. Rest assured that your job always starts in a fresh MATLAB instance, so there is no reason to clear anything.
{% include markup/end %}

### Submitting a batch of jobs

To execute few jobs in parallel as a batch you will use **[qsubcellfun](/reference/qsub/qsubcellfun)**. It is very similar to **[qsubfeval](/reference/qsub/qsubfeval)**, but instead of one input argument, you specify a cell-array of arguments. Qsubcellfun then evaluates your function with each element of the array. In fact it calls **[qsubfeval](/reference/qsub/qsubfeval)** as many times as the number of elements in the array.

Qsubcellfun is similar to the standard MATLAB Cellfun. Try the following:

    >> results = qsubcellfun('randn', {1,1,1,1}, 'timreq', 60, 'memreq', 1024*1024*1024)

    submitting job username_mentat284_p7284_b6_j001... qstat job id 25618.dccn-l014.dccn.nl
    submitting job username_mentat284_p7284_b6_j002... qstat job id 25619.dccn-l014.dccn.nl
    submitting job username_mentat284_p7284_b6_j003... qstat job id 25620.dccn-l014.dccn.nl
    submitting job username_mentat284_p7284_b6_j004... qstat job id 25621.dccn-l014.dccn.nl
    job username_mentat284_p7284_b6_j001 returned, it required 0 seconds and 832.0 KB
    job username_mentat284_p7284_b6_j002 returned, it required 0 seconds and 828.0 KB
    job username_mentat284_p7284_b6_j003 returned, it required 0 seconds and 830.0 KB
    job username_mentat284_p7284_b6_j004 returned, it required 0 seconds and 829.0 KB
    computational time = 0.1 sec, elapsed = 1.0 sec, speedup 0.0 x

    results =
     [0.1194] [0.3965] [-0.2523] [0.3803]

and compare it with

    >> cellfun(@randn, {1,1,1,1})

    ans =
     -2.2588 0.8622 0.3188 -1.3077

The difference in the output formats is due to the UniformOutput argument, which is default false in **[qsubcellfun](/reference/qsub/qsubcellfun)** and default true in CELLFUN.

When using **[qsubcellfun](/reference/qsub/qsubcellfun)** you have to specify the time and memory requirements of a single job.

Same as with **[qsubfeval](/reference/qsub/qsubfeval)**, you can use `qstat, qstat -f, qstat -al, cluster-qstat`{linux} commands to check the status and info on the submitted jobs.

Qsubcellfun works as a wrapper for qsubfeval. If you use qsubcellfun, all the temporally files created by qsubfeval are automatically deleted when the job is completed, or when it is terminated with Ctrl+C, or with an error.

#### Time and memory management

You will have noticed that you have to specify the time and memory requirements for the individual jobs using the 'timreq' and 'memreq' arguments to **[qsubcellfun](/reference/qsub/qsubcellfun)**. These time and memory requirements are passed to the batch queueing system, which uses them to find an appropriate execution host (i.e., one that has enough free memory) and to monitor the usage.

Do not set the requirements too tight, because if the job exceeds the requested resources, it will be killed. However, if you grossly overestimate them, your jobs will be scheduled in a “slow” queue, where only a few jobs can run simultaneously. The queueing and throttling policies on the number and the size of the jobs is to prevent a few large jobs from a single user from blocking all computational resources of the cluster. So the most optimal approach to get your jobs executed is to try and estimate the memory and time requirements as good as you can.

The help of **[qsubcellfun](/reference/qsub/qsubcellfun)** lists some suggestions on how to estimate the time and memory.

### Stacking of jobs

The execution of each job involves writing the input arguments to a file, submitting the job, to Torque, starting MATLAB, reading the file, evaluate the function, writing the output arguments to file and at the end collecting all output arguments of all jobs and rearranging them. Starting MATLAB for each job imposes quite some overhead on the jobs if they are small, that is why **[qsubcellfun](/reference/qsub/qsubcellfun)** implements "stacking" to combine multiple MATLAB jobs into one job for the Linux cluster. If the jobs that you pass to **[qsubcellfun](/reference/qsub/qsubcellfun)** are small (less than 180 seconds) they will be stacked automatically. You can control it in detail with the "stack" option in **[qsubcellfun](/reference/qsub/qsubcellfun)**. For example

    >> results = qsubcellfun(@randn, {1,1,1,1}, 'memreq', 1024, 'timreq', 60, 'stack', 4);
    stacking 4 MATLAB jobs in each qsub job
    submitting job username_mentat284_p7284_b7_j001... qstat job id 25677.dccn-l014.dccn.nl

...

    >> results = qsubcellfun(@randn, {1,1,1,1}, 'memreq', 1024, 'timreq', 60, 'stack', 1);
    submitting job username_mentat284_p7284_b8_j001... qstat job id 25678.dccn-l014.dccn.nl
    submitting job username_mentat284_p7284_b8_j002... qstat job id 25679.dccn-l014.dccn.nl
    submitting job username_mentat284_p7284_b8_j003... qstat job id 25680.dccn-l014.dccn.nl
    submitting job username_mentat284_p7284_b8_j004... qstat job id 25681.dccn-l014.dccn.nl

...

Note that the stacking implementation is not yet ideal, since with the default option it distributed the 4 jobs into 3+1, whereas 2+2 would be better.

### Submitting a batch and don't wait within MATLAB for them to return

If you run your interactive MATLAB session on a torque execution host with a limited walltime and want to submit a batch of jobs with qsubcellfun, you don't know when the batch of jobs will finish. Consequently, you cannot predict the walltime that your interactive session requires in order to see all jobs returning.

Rather than waiting for all jobs to return, you can submit the batch and close the interactive MATLAB session. The next day or week, when all batch jobs have finished (use "qstat" to check on them) you can start MATLAB again to collect the results.

With a single job you could simply do

    jobid = qsubfeval(@myfunction, inputarg);
    save jobid.mat jobid
    exit

    % start MATLAB again
    load jobid.mat
    result = qsubget(jobid);

A complete batch of jobs can be dealt with in a similar manner

    jobidarray = {};
    for i=1:10
      jobidarray{i} = qsubfeval(@myfunction, inputarg{i});
    end
    save jobidarray.mat jobidarray
    exit

    % start MATLAB again
    load jobidarray.mat
    results = {};
    for i=1:10
      results{i} = qsubget(jobidarray{i});
    end

Or with fewer lines of code using the standard [cellfun](http://www.mathworks.nl/help/matlab/ref/cellfun.html) function as

    jobidarray = cellfun(@qsubfeval, repmat(@myfunction, size(inputarg)), inputarg, 'UniformOutput', false);
    save jobidarray.mat jobidarray
    exit

    % start MATLAB again
    load jobidarray.mat
    results = cellfun(@qsubget, jobidarray, 'UniformOutput', false);
