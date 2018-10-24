---
layout: default
tags: faq engine
---

# How to get started with distributed computing using engine?

The [FieldTrip engine toolbox](http://github.com/fieldtrip/fieldtrip/tree/master/engine) is a small stand-alone toolbox to facilitate distributed computing. You can use the engine toolbox on a single computer with multiple CPUs or multiple cores. In principle it is also possible to start the engines on other (UNIX) computers using ssh, although that has not been tested.

Let's assume that you have a quad-core CPU and that you want to run some jobs in parallel. You start MATLAB and type 

    enginepool open 4

This will start 4 threads within MATLAB, each connected to a separate MATLAB "engine" instance. These engines are full-fledged MATLAB sessions, but without the graphical user interface.  

The following shows the current configuratio

    >> enginepool
    there are 4 engines  
    0 of them have a job 
    0 of them are busy

Each of the engines is now waiting for a job to be executed. 

Subsequently you can type 

    y = enginecellfun(@power, {1, 2, 3}, {2, 2, 2})

which should return

    [1, 4, 9]

What happened is that **[enginecellfun](/reference/enginecellfun)** distributed the execution of these three jobs over all separate threads

    power(1, 2)
    power(2, 2)
    power(3, 2)

Most applications of **[: reference:enginecellfun](/ reference/enginecellfun)** will return non-scalar values, which cannot be appended into a single vector. In that case, consistent with cellfun, it will return an error unless you specify that the output will be non-uniform. E.g. 

    enginecellfun(@rand, {1, 2, 3}, 'UniformOutput', false)

which returns

    {[1x1]  [2x2]  [3x3]}

In these small computations the overhead of the communication with the engines takes more time than the actual computations, so parallelization will not result in a speed increase. To get a speed increase, the ratio between the computational effort and the data size should be more balanced towards the first. The following example demonstrates a computationally heavy job which can benefit from parallelization

    a = randn(400,400);
    tic;       cellfun(@pinv, {a, a, a, a}, 'UniformOutput', false); toc 
    tic; enginecellfun(@pinv, {a, a, a, a}, 'UniformOutput', false); toc

You probably have to play with the size of the matrix "a" and with the number of jobs to see the largest effect on the timing of the non-parallel (cellfun) and parallel (enginecellfun) version of the computations. 

Note that in the example above there might or might not be a speed increase. Recent versions of MATLAB have a (partially) parallel pinv function, which means that a single pinv already keeps all your CPU cores busy. Furthermore, there is some overhead in sending and receiving every job independent of the job size. On top of that there is the overhead of sending the input data and receiving the results, which increases linearly with the size of the data. If the computation itself is relatively short compared to the fixed and variable overhead, then enginecellfun will not speed up the computations. An example with very little overhead and guaranteed speed increases is the following

    t = repmat({6}, 1, 100);
    tic;       cellfun(@pause, t, 'UniformOutput', false); toc 
    tic; enginecellfun(@pause, t, 'UniformOutput', false); toc

which evaluates 100 times a 6 second pause, resulting in 600 seconds of "work" in total. 

Whether your specific computational job can be efficiently distributed depends on the amount of data per individual job (i.e. the fixed plus variable overhead in sending/receiving) compared to the computational time per job.

   
 
