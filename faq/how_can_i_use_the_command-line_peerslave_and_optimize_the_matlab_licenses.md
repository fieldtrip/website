---
title: How can I use the command-line peerslave and optimize the MATLAB licenses?
tags: [faq, peer]
---

# How can I use the command-line peerslave and optimize the MATLAB licenses?

Most of the examples on the website demonstrate for simplicity how you can start the peerslave within a MATLAB session. The disadvantage of that is that the peerslaves are always using a MATLAB license, even if they are not doing any computations. Furthermore the MATLAB process takes a lot of your system memory. To solve these inefficiency we have implemented a command-line peerslave executable.

The command-line peerslave executable runs the peer network maintenance threads and uses the MATLAB engine. If a job arrives, the MATLAB engine is started (at that point it takes a license), executes the job inside the engine and sends the results back to the master. If the peerslave is idle for some time, the engine is stopped and the license returned. Executing multiple jobs in a row is only slowed down by the first time that the engine has to be started, which typically takes 10-30 seconds. The engine will keep running until all jobs are done.

To start the command-line peerslave, you type
peerslave.xxx
where xxx is your computer architecture (glnx86, glnxa64, maci, maci64).

If you want to start multiple peerslaves at once, for example because you have a quad-core CPU, you can do
peerslave.xxx --number 4
