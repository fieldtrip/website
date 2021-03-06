---
title: How does the smartmem algorithm work?
tags: [faq, peer, memory]
---

# How does the smartmem algorithm work?

A problem in distributed computing occurs if a job needs more resources than available in the worker/worker that has to execute the job. The CPU speed is one such resource, but it is not critical: picking a slow computer to execute the job will just mean that the job takes longer to finish. The available memory however is a critical resource: if you send the job to a computer that does not have enough (free) RAM available might cause the computer to start swapping, to abort execution with an explicit error, or to crash the process executing the job altogether (e.g. if the kernel decides to kill the process).

Each peerworker broadcasts the amount of memory that it has available for job execution. On the controller an estimate will have to be made (either by you, or by peercellfun) how much memory is required to run one of the jobs. The peerfeval function will only sendthejob to a peerworker that (according to its announcement) has enough memory available. You can configure the amount of memory that is broadcasted by the peerworker. For example, if you have 4 workers on a quad-core computer with 8GB of RAM, you might want to configure each peerworker to announce that it has 2GB of RAM available. The peerworkers in that case will not accept jobs that are larger.

In the case that the computers are also used for interactive processing (e.g. other people logged in and using other software), the free memory will vary over time. The command-line peerworker implements an algorithm to estimate the available free memory and to announce that. Inside the peerworker executable, the total free memory of the computer is determined and divided by the number of **idle** peerworkers on the same computer. I.e. two idle peerworkers on a computer that has 5GB of memory free will both estimate that they have 2,5GB of available memory and will announce this. Once one of them accepts a job and switches to busy, it is assumed that it will allocate its memory immediately. This assumption might be wrong, in which case the remaining peerworker will still see 5GB of available memory and will start announcing that. In that case it might happen that the 2nd peerworker accepts a job that is larger than in total can be acomodated on the computer.
