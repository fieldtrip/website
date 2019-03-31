---
title: How can I set up the peer distributed computing on a single multicore computer?
tags: [faq, peer]
---

# How can I set up the peer distributed computing on a single multicore computer?

There are in principle two options for setting up the peer-to-peer computing system. The first, using an interactive MATLAB session for each peer is recommended for occasional or novice users. The second, using the command-line peerslave is recommended for frequent users and if your computer remains switched on and is only put to sleep during the night.

## Using an interactive MATLAB session for each peer

Per core you should start one MATLAB session to run as slave, i.e. 4 sessions for a quad-core CPU. In each of the slave MATLAB sessions, you start the peer as slave by typing **[peerslave](/reference/peerslave)**. This will (among others) start the announce and tcpserver thread and subsequently it will wait for an incoming job. Every second while waiting it will print a line with the current time on screen, which allow you to check that it is still running.

Subsequently you start one more MATLAB session which will be the master session from which you distribute the jobs. In that MATLAB session you type **[peermaster](/reference/peermaster)**, which will (among others) start the discover thread. In the master you can then use **[peercellfun](/reference/peercellfun)** to send a batch of jobs for execution on the slaves.

In the end you should have N+1 peers, with N slaves and one master.

As example and proof-of concept, you should try
peercellfun(@pause, {5, 5, 5, 5})
which should result in each slave pausing for 5 seconds.

Another example is
peercellfun(@plot, {randn(1, 10), randn(1, 10), randn(1, 10), randn(1, 10)}, {'b.', 'r.', 'g.', 'm.'})
which will make a plot in each peerslave with different colored random points. After creating the figure and drawing the points, the slave should close the figure again.

You can type
peerinfo
to get information about the peer itself (i.e. in the MATLAB session where you type it) and
peerlist
to get information on all visible peers on the network.

Starting N+1 instances of MATLAB on a single computer as a single user will only result in a single (network) license being used. Since the slaves are running within the MATLAB session, the license will also be claimed it the slaves are waiting.

## Using the command-line peerslave

A disadvantage of starting the peerslaves within an interactive MATLAB session is that they require a license, also when the slave is idle. The command-line peerslave is a stand-alone executable that implements the announce, discover, tcpserver and expire threads and that waits for an incoming job. Once a job arrives for local execution, the MATLAB engine is started, the job is evaluated, and the results are sent back. After finishing the job, the engine remains running for 30 seconds to quickly evaluate another incoming job. After being idle for more than 30 seconds, the engine is stopped.

The command line peerslave is currently implemented for Linux (32 and 64-bit) and macOS (32-bit Intel only). The command-line executable is included in the release version for the different architectures and is started with one of the following commands:

- peerslave.glnx86
- peerslave.glna64
- peerslave.maci

There is also a Linux shell script with the name peerslave, which is designed to be used at the DCCN to start up a large number of slaves on our mentat Linux cluster. The release version of the peerslave command-line startup script is not useful for most end-users, although you may want to have a look inside the bash-script and make your own version.

Please type on the unix command line
peerslave.arch --help
(where arch is glnx86, glnxa64 or maci) to get an overview of all the options. In principle most of the options have the same behavior as the MATLAB **[peerslave](/reference/peerslave)** function.
