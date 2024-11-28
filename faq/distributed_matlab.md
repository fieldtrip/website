---
title: How to get started with the MATLAB distributed computing toolbox?
category: faq
tags: [distcomp, parfor]
redirect_from:
    - /faq/how_to_get_started_with_the_matlab_distributed_computing_toolbox/
---

# How to get started with the MATLAB distributed computing toolbox?

The MATLAB [parallel computing toolbox](https://nl.mathworks.com/products/parallel-computing.html), formerly known as the distributed computing toolbox (DCT) is a commercial toolbox provided by MathWorks. It allows you to execute distributed computations on multiple cores in a single computer, or if you have access to [distributed computing engines](http://www.mathworks.com/products/distriben/index.html) on a compute cluster. To figure out whether you have it, you can try

    help distcomp

or using FieldTrip

    ft_hastoolbox('distcomp')

This page provides a short introduction into the most relevant functions that allow you to distribute your FieldTrip analysis over multiple computers or cores and run them in parallel.

The distributed computing toolbox requires that you begin by starting up the "workers", either on your local computer or on the distributed computing engines on your cluster. This is done with e.g.

    matlabpool local 4

which starts 4 workers with the "local" configuration. Subsequently you can use parfor instead of the normal for to iterate over a number of computations, as in

    dataset = {
    'Subject01.ds'
    'Subject02.ds'
    'Subject03.ds'
    };

    parfor i=1:3
      cfg = [];
      cfg.dataset = dataset{i}
      data{i} = ft_preprocessing(cfg);
    end

Alternatively you can use the [batch](https://www.mathworks.com/help/distcomp/batch.html) function from the MATLAB Parallel Computing toolbox like this

    for i=1:3
      cfg{i} = [];
      cfg{i}.dataset = dataset{i};
    end

    data = batch(@ft_preprocessing, 3, cfg);

The batch function works similar to the standard MATLAB cellfun function, and thereby to the FieldTrip **[qsubcellfun](/reference/qsub/qsubcellfun)** function.

A third approach that is available in the distributed computing toolbox is to use the [spmd](https://nl.mathworks.com/help/parallel-computing/spmd.html) construct. Given the same definition of the dataset as a cell-array with three strings as above, this would look like

    matlabpool local 3
    spmd 3
      cfg = [];
      cfg.dataset = dataset{spmdIndex};
      data{spmdIndex} = ft_preprocessing(cfg);
    end

The labindex variable is automatically replaced by the number of the worker. Note that this only works if your matlabpool is greater than or equal to the number of jobs.

### Some closing remarks

Many of the FieldTrip functions allow to specify the cfg.inputfile and cfg.outputfile option, which allow you to run large analyses in parallel without all the analysis results being returned to your primary MATLAB session. This is especially relevant if your primary computer is not able to hold the results of all computations in memory at the same time.

Elsewhere on this FieldTrip website you can find more documentation, such as the tutorials on using [qsub](/tutorial/distributedcomputing_qsub) and [parfor](/tutorial/distributedcomputing_qsub). Some of the FAQs on distributed computing with [qsub](/tag/qsub/) and [parfor](/tag/parfor/) will also be informative.
