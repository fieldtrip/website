---
title: How can I use the command-line peerworker and optimize the MATLAB licenses?
tags: [faq, peer]
---

# How can I use the command-line peerworker and optimize the MATLAB licenses?

Most of the examples on the website demonstrate for simplicity how you can start the peerworker within a MATLAB session. The disadvantage of that is that the peerworkers are always using a MATLAB license, even if they are not doing any computations. Furthermore the MATLAB process takes a lot of your system memory. To solve these inefficiency we have implemented a command-line peerworker executable.

The command-line peerworker executable runs the peer network maintenance threads and uses the MATLAB engine. If a job arrives, the MATLAB engine is started (at that point it takes a license), executes the job inside the engine and sends the results back to the controller. If the peerworker is idle for some time, the engine is stopped and the license returned. Executing multiple jobs in a row is only slowed down by the first time that the engine has to be started, which typically takes 10-30 seconds. The engine will keep running until all jobs are done.

To start the command-line peerworker, you type
peerworker.xxx
where xxx is your computer architecture (glnx86, glnxa64, maci, maci64).

If you want to start multiple peerworkers at once, for example because you have a quad-core CPU, you can do
peerworker.xxx --number 4
