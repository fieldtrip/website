---
title: Distributed computing
tags: [distributed, engine, peer, qsub]
redirect_from:
---

# Distributed computing

As alternative to the MathWorks [Parallel Computing Toolbox](https://www.mathworks.com/products/parallel-computing.html), FieldTrip includes three stand-alone [modules](/development/architecture/#modular-organization) for distributed computing. These range from small to large scale distributed computing. Note that FieldTrip does not automatically distribute the workload; you have to implement the distributed computing in your own analysis scripts as explained in the [distributed computing](/tutorial/distributedcomputing) tutorial.

- [engine](/development/module/engine) distributed computing on a (massive) multi-core computer
- [peer](/development/module/peer) distributed computing on an ad-hoc multi-core and/or multi-node peer-to-peer cluster
- [qsub](/development/module/qsub) distributed computing on a Torque, Slurm or SGE cluster
