---
title: Distributed computing using the MATLAB engine system
tags: [development, distributed, engine]
---

# Distributed computing using the MATLAB engine system

The FieldTrip-engine toolbox facilitates distributed computing
on a massive multicore computer without requiring the MATLAB parallel toolbox.
It uses the MATLAB engine interface to start multiple instances of MATLAB and
distributes the work between them.

The goal of this toolbox is to provide you with an easy MATLAB interface to
distribute your jobs that is compatible with the MATLAB feval and cellfun
functions.

This FieldTrip-engine toolbox is compatible with the FieldTrip-qsub toolbox
that allows you to distribute your computations to a distributed Linux cluster.
The qsub toolbox supports Linux clusters with Torque and other PBS versions,
Sun Grid Engine (SGE), Oracle Grid Engine and with SLURM as the batch queueing
system.

This toolbox has been developed as part of the FieldTrip toolbox, but can be
used separately. See http://www.fieldtriptoolbox.org for general details on the
FieldTrip project, http://www.fieldtriptoolbox.org/development/module/qsub for specific
details on the qsub toolbox or see http://www.fieldtriptoolbox.org/faq for questions.

## Frequently asked questions about distributed computing using this toolbox

{% include seealso tag1="faq" tag2="engine" %}
