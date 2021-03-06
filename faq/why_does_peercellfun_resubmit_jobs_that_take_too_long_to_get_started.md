---
title: Why does peercellfun resubmit jobs that take too long to get started?
tags: [faq, peer]
---

# Why does peercellfun resubmit jobs that take too long to get started?

When using peercellfun you might see frequent warnings like

    Warning: resubmitting job XX because it takes too long to get started

These indicate that a particular job was submitted to a worker, but that the worker is still not busy executing the job after 30 seconds. This happens if the command-line peerworkers fail to startup a MATLAB engine. I.e., the peerworker considers itself to be idle, it accepts a job, tries to start a MATLAB engine, and then figures out that it cannot get a MATLAB license. The job was already accepted, but cannot be executed.

On the controller inside peercellfun an eye is kept on all jobs that are submitted. Jobs that don't seem to get started are assumed to have ended up with a worker that cannot get a MATLAB license and therefore are resubmitted (hopefully to a worker that does have a license).
