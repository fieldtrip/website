---
title: What are the different approaches I can take for distributed computing?
tags: [faq, qsub, parfor, distcomp, matlab]
---

# What are the different approaches I can take for distributed computing?

At the Donders Centre we have a Linux cluster that we use for the analysis of the neuroimaging data (MEG, fMRI, DTi, ...). On this cluster we have explored various options for distributed computing to speed up the analysis. Particular considerations have resulted so far in own development of an add-on toolbox that is distributed along with FieldTrip as `fieldtrip/qsub`. We are of course also aware of the MathWorks parallel computing toolbox and the accompanying distributed computing engines, although we don't have a license for those.

Distributed computing in short means cutting up a large computational problem into smaller sections, i.e. jobs, and distributing those over many CPUs. Managing each of the jobs has some overhead: the more jobs, the more overhead. If the jobs get too small (e.g., an FFT of a single vector of 1000 datapoints), the overhead becomes larger than the actual computation and distribution of the jobs is not beneficial any more. If there are fewer jobs than available CPUs, the cluster is not optimally busy. If there are many more jobs than available CPUs, the overhead of the many small jobs might deteriorate the performance. Finding the right granularity (not too large, not too small) of the job size is quite challenging and depends on a lot of parameters

The approach that we have adopted so far in FieldTrip is the end-user (i.e. you) is doing the distribution of the jobs in his/her analysis script and that individual jobs are defined at the level of subjects or conditions. Many cognitive research projects have in the order of say 20 subjects, which means that a natural split of the total computational load into 20 jobs. This matches quite well with the resources that we have available for an individual researcher at the Donders Centre.

Let me outline the different approaches below. Note that although in the examples below a FieldTrip toolbox function is distributed without the function being aware of it, we have made some changes to the FieldTrip toolbox main functions to facilitate their distribution, i.e. the cfg.inputfile and cfg.outputfile options. Please have a look at the tutorials using distributed computing using [qsub](/tutorial/distributedcomputing_qsub) and [parfor](/tutorial/distributedcomputing_parfor) for a more thorough description of the interaction between a FieldTrip analysis pipeline and the distributed computing.

### MathWorks parallel computing toolbox and distributed computing engines

The [MATLAB Parallel Computing toolbox](http://www.mathworks.nl/products/parallel-computing) allows you to start multiple MATLAB "labs" on your desktop computer and distribute the computational load over these labs. This for example looks like this:

    matlabpool open 4
    parfor i=1:Nsubj
      cfg         = ...
      cfg.dataset = sprintf('subject%d.eeg');
      rawdata{i}  = ft_preprocessing(cfg);
    end

This will keep 4 MATLAB workers on your own computer busy with preprocessing. Note that this example is probably not so efficient to distribute: presumably your local hard disk speed is the bottleneck, not the CPU speed.

Another way to distribute jobs is using [batch](https://www.mathworks.com/help/distcomp/batch.html) like this:

    for i=1:Nsubj
      cfg{i}         = ...
      cfg{i}.dataset = sprintf('subject%d.eeg');
    end
    rawdata = batch(@ft_preprocessing, Nsubj, cfg);

If you also have the [MATLAB Parallel Server](https://nl.mathworks.com/products/matlab-parallel-server.html), which has to be installed on a compute cluster, you can use those as remote engines for executing the separate jobs.

### FieldTrip qsub toolbox

At the Donders we have a Linux compute cluster that is managed with a batch queueing system that allows users to submit large batches of jobs to run in parallel. The Donders cluster runs Torque/Maui, but other PBS systems, SLURM, LSF, Sun Grid Engine and Oracle Grid Engine are also supported. More documentation on the qsub toolbox is found [here](/development/module/qsub).

To facilitate distributed computing, we have implemented the **[qsubcellfun](/reference/qsub/qsubcellfun)** wrapper function within MATLAB, which for the end-user works similar to [cellfun](https://nl.mathworks.com/help/matlab/ref/cellfun.html) and [batch](https://nl.mathworks.com/help/parallel-computing/batch.html).

    for i=1:Nsubj
      cfg{i}         = ...
      cfg{i}.dataset = sprintf('subject%d.eeg');
    end
    rawdata = qsubcellfun(@ft_preprocessing, cfg);

See **[qsubcellfun](/reference/qsub/qsubcellfun)**, **[qsubfeval](/reference/qsub/qsubfeval)** and **[qsubget](/reference/qsub/qsubget)** for details.
