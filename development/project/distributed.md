---
title: Core idea
---

{% include /shared/development/warning.md %}

## Core idea

Standardize distributed computing ~~at the DCCN~~ from within open source MATLAB toolboxes, through the use of developed functions such as Torque (qsubfeval, qsubcellfun) or peer-to-peer computing (peerfeval, peercellfun).

This could be implemented into

- [automatic analysis](http://cambridgeneuroimaging.com/aawiki/index.php?title=Home)
- the SPM batch system
- FieldTrip
- EEGLAB
- BrainStorm
- ...

We could consider splitting the problem into three categorie

1.  end-user software: SPM, FieldTrip and the likes
2.  middleware: aa, matlabbatch, qsubcellfun
3.  computational backend: torque, sge, AC2
    My thought for making this double divide is to try and focus on the middleware, and try to stay sufficiently far away from 1 to make it flexible and to keep 3 for the sysadmins. Of course they all interact, but we should try to focus on a particular problem that can be solved. My idea with this focus on the middleware is to achieve the goal of more variants of "(1) end-user software" run on more variants of "(3) computational backends".

#### Some thoughts on using aa

There are two features (present in aa version 4) that I think will be especially useful for distributed neuroimaging analyse

1.  It knows about the dependencies between different stages - so which stages can be executed concurrently, and which must be completed before another can begin
2.  All data in and out of each module is explicitly described. This means that a single aa function is responsible for retrieving any piece of data, and another function is responsible for registering any outputs. These functions can be used to retrieve just the data that is needed for any given job. This is currently used to run jobs on Amazon EC2, with data stored on the object store S3.

#### Some thoughts on peercellfun/qsubcellfun

These are two functions that were implemented for different backends, but in both cases mimicking MATLAB cellfun/dfeval and specifically designed for single-process-multiple-data (SPMD) scenarios. These cellfun functions are not meant for jobs in which dependencies are important. The code that is underneath (peerfeval and qsubfeval) would be at the appropriate level to implement these dependencies.

Note that although these two were made within the FieldTrip project, the FieldTrip code itself does not call them. It is the end-user who calls them in his/her script. See [this](/faq/what_are_the_different_approaches_i_can_take_for_distributed_computing) to get a feeling for how they relate.

## To solve...

We may need to estimate the time and memory requirements of each process, potentially by a combination of memory estimation (fMRI: volumes and voxels in experiment) and profiling (memtic & memtoc).

Robert: an automatic estimation and updating of requirements for subsequent jobs was built into peercellfun, but turned out not to be very robust. In qsubcellfun I therefore forced the correct specification onto the user instead of attempting to have smart defaults.

The benefit to different modules being run in parallel may vary. Memory/processor intensive scripts (fMRI normalisation) vs. hard disk intensive (DICOM to Nifti conversion) depending on the site specific architecture.

Similarly, small jobs would benefit from stacking (running a series of jobs on a single distributed node). That is implemented in qsubcellfun.

### ...with aa

Here are some possible ways to estimate a module's requirements, ranging from simple to complex to implement

1.  Static (user provided) estimates of a module's hungriness. Obvious place within aa is in the XML wrapper that describes each module.
2.  Automatic estimate. We could gather statistics on how much each module uses.
3.  Automatic estimate with prediction. We could gather statistics and relate these to specific calling descriptors of the module (e.g., number of files) so that a prediction could be made for a specific instance of a module

## Tasks

1. Investigate different batch/distributed computing systems to find which might be most general/tight.

| Computational Backend | where                    |
| --------------------- | ------------------------ |
| SGE/OGE/GE            | Gio, Amsterdam           |
| peer-to-peer          | Craig or Robert, ESI     |
| Torque                | Robert, Donders          |
| Condor                | Rhodri                   |
| OSCAR                 | ?                        |
| Amazon Cloud          | ?                        |
| SLURM                 | ?                        |
| MathWorks DCE         | Robert, WashU and Chieti |

Q (Robert): How would you like to refer to the home-built Cambridge system for distributing the load (i.e. with aa_doprocessing_parallel in v3.01).

Q (Robert): are there other important generic backends that we want to support?

Q (Robert): what are the defining features of the various systems? E.g.

1.  allow for job dependencies
2.  managing specific hardware resource (e.g. GPUs)
3.  keep workers open between calls
4.  suitable for MPI
5.  ...

2) Get more people interested/involved.

(Robert): I have already listed some potential collaborators with access to specific setups that we might want to consider. The main reason for point 2 is to get the end-user software teams involved (e.g. Guillaume, Arno). Any ideas on trying to find relevant open source projects outside of neuroscience. And what about Octave?

### related links

- http://www.cambridgeneuroimaging.com/aawiki/

- http://code.google.com/p/psom/

- http://deltacloud.apache.org/

- http://aws.amazon.com/ec2/

- http://research.cs.wisc.edu/condor/

- http://www.adaptivecomputing.com/resources/docs/torque/2-5-9/index.php

- http://gridscheduler.sourceforge.net/

- http://svn.oscar.openclustergroup.org/trac/oscar/wiki

- http://www.mosix.org/
