---
title: Distributed computing
tags: [distributed, qsub, parfor]
---

# Distributed computing

As alternative to the MathWorks [Parallel Computing Toolbox](https://www.mathworks.com/products/parallel-computing.html), FieldTrip includes the [qsub](/development/module/qsub) module to allow distributed computing on a Torque, Slurm or SGE cluster. Note that FieldTrip does not automatically distribute the workload; you have to implement the distributed computing in your own analysis scripts as explained in the [parfor](/tutorial/distributedcomputing_parfor) and [qsub](/tutorial/distributedcomputing_qsub) tutorials.
