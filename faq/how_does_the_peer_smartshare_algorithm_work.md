---
title: How does the peer smartshare algorithm work?
tags: [faq, peer]
---

# How does the peer smartshare algorithm work?

If multiple end-users are simultaneously distributing their computational jobs, a problem can arise in distributing the limited resources to these users. One limited resource is cpu time, another is memory. A fair-sharing algorithm has been implemented to improve the distribution of resources over multiple concurrent users.

Optimizing CPU time requirements of the jobs is challenging. Consider the following example: There are two controller (i.e. end-user) nodes in the peer-to-peer network, and a single worker node. That means that the two controller nodes compete for the worker. Subsequently consider the following two distributed processes on the two controller node

    tic; peercellfun('pause', {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}); toc

and

    tic; peercellfun('pause', {10, 10, 10, 10, 10, 10, 10, 10, 10, 10}); toc

The second job takes 10x as much (virtual) CPU time in total. However, if both processes have an equal probability of getting their job submitted to and executed on the worker, you would expect the two processes to take the same amount of time. Fair allocation of the CPU time should result in the process on the first controller finishing approximately 10x faster than the process on the second controller.

Fair sharing of CPU time is currently implemented by manipulating the likelihood that a job is accepted by the worker. A Job that takes a long time to finish, is more likely to be rejected. As long as a job is rejected, the controller will retry submitting the job. In the mean time, the other controller with the short jobs has more success in getting his jobs accepted and executed. In the example above, the change of accepting a job from the second controller should be 1/10th of the change of accepting a job from the first controller.

Both the efficient memory planning and the fair sharing of CPU time require that an estimate of the memory and CPU time need to be present. A fixed initial estimate is used, which is refined once the single job results are returned to the controller.

## Optimizing memory use

Peers that run in worker mode announce their host details, including the available memory. The optimization of jobs with respect to memory is currently implemented in peerfeval, which selects the worker that has the best fit. It first selects all worker with sufficient memory, and from those it selects the one with the least memory available.

The first job that is evaluated by peercellfun will have a default (large) memory requirement. The worker that evaluated the job will try to estimate the real memory requirements (using memprofile) and send those back with the job results. The peercellfun function collects the memory requirements of all incoming jobs, and will commit new jobs with a setting of the memory requirement corresponding with that of the largest job that has returned.
