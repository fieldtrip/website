---
layout: default
tags: faq peer
---

## Why does peercellfun resubmit jobs that take too long to get started?

When using peercellfun you might see frequent warnings like

    Warning: resubmitting job XX because it takes too long to get started 

These indicate that a particular job was submitted to a slave, but that the slave is still not busy executing the job after 30 seconds. This happens if the command-line peerslaves fail to startup a matlab engine. I.e., the peerslave considers itself to be idle, it accepts a job, tries to start a MATLAB engine, and then figures out that it cannot get a MATLAB license. The job was already accepted, but cannot be executed. 

On the master inside peercellfun an eye is kept on all jobs that are submitted. Jobs that don't seem to get started are assumed to have ended up with a slave that cannot get a MATLAB license and therefore are resubmitted (hopefully to a slave that does have a license).

