---
layout: default
---

{{tag>distributed}}

# Distributed computing using a Linux compute cluster

The FieldTrip-qsub toolbox facilitates distributed computing on
a Linux compute cluster without requiring the MATLAB parallel toolbox or distributed
computing engines. It only requires a standard MATLAB installation on the
cluster nodes. Alternatively, it can use the MATLAB compiler to run on clusters
where MATLAB is not available.

The goal of this toolbox is to provide you with an easy MATLAB interface to
distribute your jobs that is compatible with the MATLAB feval and cellfun
functions.  It offers a simple MATLAB interface to distribute your jobs and you
do not have to go to the Linux command-line to use the qsub command from there.

The toolbox supports Linux clusters with Torque and other PBS versions, LSF, SLURM, Sun
Grid Engine (SGE) and Oracle Grid Engine as the batch queueing
system.

This toolbox has been developed as part of the FieldTrip toolbox, but can be
used separately. See http://www.fieldtriptoolbox.org for general details on the
FieldTrip project, http://www.fieldtriptoolbox.org/development/qsub for specific
details on the qsub toolbox or see http://www.fieldtriptoolbox.org/faq for questions.

## Frequently asked questions about distributed computing using this toolbox

{{topic>qsub +faq &list}}


