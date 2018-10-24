---
layout: default
tags: faq peer
---


# How to get started with peer distributed computing on my own desktop computer?

The [FieldTrip peer toolbox](https://github.com/fieldtrip/fieldtrip/tree/master/peer) is a small stand-alone toolbox to facilitate distributed computing on an ad-hoc cluster. You can use the peer system on multiple computers or on a single computer with multiple CPUs or multiple cores. Note that starting multiple MATLAB sessions on a single computer only requires one MATLAB license. 

Let's assume that you have a single computer with a dual- or quad-core CPU and that you want to run some jobs in parallel. Or even better, lets assume that you have N computers (e.g. those of your room-mates) on which you want to run jobs. 

On the first (your own) computer, you start MATLAB and type 

    peermaster

On all N-1 subsequent computers (or the same computer if has multiple CPUs or cores), you start MATLAB and type

    peerslave

You will see the **[peerslave](/reference/peerslave)** printing the date and time every second. Each of the slaves is now waiting for a job to be executed. 

Then you go back to the first "master" MATLAB session and type 

    peercellfun(@power, {1, 2, 3}, {2, 2, 2})

which should return

    [1, 4, 9]

What happened is that **[peercellfun](/reference/peercellfun)** distributed the execution of these three jobs over all slaves

    power(1, 2)
    power(2, 2)
    power(3, 2)

Most applications of **[peercellfun](/reference/peercellfun)** will return non-scalar values, which cannot be appended into a single vector. In that case, consistent with cellfun, it will return an error unless you specify that the output will be non-uniform. E.g. 

    peercellfun(@rand, {1, 2, 3}, 'UniformOutput', false)

which returns

    {[1x1]  [2x2]  [3x3]}

In these small computations the overhead of the communication between the peers takes more time than the actual computations, so parallelization will not result in a speed increase. To get a speed increase, the ratio between the computational effort and the data size should be more balanced towards the first. The following example demonstrates a computationally heavy job which can benefit from parallelization

    a = randn(400,400);
    tic;     cellfun(@pinv, {a, a, a, a, a}, 'UniformOutput', false); toc 
    tic; peercellfun(@pinv, {a, a, a, a, a}, 'UniformOutput', false); toc

You probably have to play with the size of the matrix "a" and with the number of jobs to see the largest effect on the timing of the non-parallel (cellfun) and parallel (peercellfun) version of the computations. 

Note that in the example above there might or might not be a speed increase. Recent versions of MATLAB have a (partially) parallel pinv function, which means that a single pinv already keeps all your CPU cores busy. Furthermore, there is some overhead in sending and receiving every job independent of the job size. On top of that there is the overhead of sending the input data and receiving the results, which increases linearly with the size of the data. If the computation itself is relatively short compared to the fixed and variable overhead, then peercellfun will not speed up the computations. An example with very little overhead and guaranteed speed increases is the following

    t = repmat({6}, 1, 100);
    tic;     cellfun(@pause, t, 'UniformOutput', false); toc 
    tic; peercellfun(@pause, t, 'UniformOutput', false); toc

which evaluates 100 times a 6 second pause, resulting in 600 seconds of "work" in total. 

Whether your specific computational job can be efficiently distributed depends on the amount of data per individual job (i.e. the fixed plus variable overhead in sending/receiving) compared to the computational time per job.
# Peerslave command-line executable

The example above describes how to start the peerslaves within a MATLAB session. The disadvantage of that is that the peerslaves are always using a MATLAB license, even if they are not doing any computations. To solve this license inefficiency we have implemented a [command-line peerslave executable](/faq/how_can_i_use_the_command-line_peerslave_and_optimize_the_matlab_licenses).


    
   



 
