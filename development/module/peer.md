---
title: Distributed computing using a peer-to-peer cluster
tags: [peer]
---

# Distributed computing using a peer-to-peer cluster

The FieldTrip-peer toolbox facilitates you to do distributed computing on an ad-hoc cluster. Setting up this peer-to-peer cluster does not require a system administrator, and using it does not require a lot of technical skills.

The peer toolbox is inspired by the situation that many neuroscience research environments have plenty of computational power in the form of workstations that are idling most of the time, but that only few research institutes have the resources to set up a full-fledged Torque, SGE or Condir Linux cluster. With the peer toolbox you can easily take a few of the computers of your room mates if they are not around, and combine those with your own workstation to speed up your computations.

This toolbox has been developed as part of the FieldTrip toolbox, but can be used separately. See http://www.fieldtriptoolbox.org for general details on the FieldTrip project, http://www.fieldtriptoolbox.org/development/module/peer for specific details on the peer toolbox or see http://www.fieldtriptoolbox.org/faq for questions.

## Requirements

The requirements of the peer toolbox are having normal MATLAB licenses, a network that is not blocked down too much and a shared filesystem. Each of these will be detailled further down, after explaining the basic usage.

## How does it work

The peer toolbox is a spin-off project from our real-time Brain-Computer interfacing project. After implementing the FieldTrip buffer for transmitting and buffering EEG and MEG data over the network, we realised that we could also use a slightly modified buffer for other stuff, such as distributed computing.

Each of the peers in the network consists of a MATLAB session. Withing that MATLAB session a mex file is running that runs several theads in the background. The most important thread is the buffer, which is a small TCP server that can receive and hold MATLAB variables that were sent from another peer. The buffer is used to receive the input variables of a computation that has to be performed on this peer, or the output variables of a computation that weer performed on another peer. Another thread that is running sends and receives UDP multicast packets. These are very small messages that are sent over the network to announce the presence of the peer and to inform the other peers of its status. These multicasts packets are sent to all computers on the local network, which allows all peers on that network to discover each other. That means that you don't have to list all peers in a configuration file: in fact, there are no configuration files at all.

Assume that you have started one peer on your own computer and three peers on the computers of your colleagues that already went home for the evening. Your peer is the master, and can send commands to the other slaves. For example

    >> peercellfun(@rand, {10, 20, 30}, 'UniformOutput', false)

    submitted 3/3, collected 3/3, busy 0, speedup 0.1
    computational time = 0.0 sec, elapsed = 0.2 sec, speedup 0.0 x (memreq = 8.0 KB, timreq = 0 seconds)

    ans =
      [10x10 double]    [20x20 double]    [30x30 double]

which will compute a random matrix on each of the three slaves. You can compare this to the standard MATLAB [cellfun](http://www.mathworks.nl/help/techdoc/ref/cellfun.html) function, which works almost identical but that executes the funcion locall

    >> cellfun(@rand, {10, 20, 30}, 'UniformOutput', false)

    ans =
      [10x10 double]    [20x20 double]    [30x30 double]

What happened in the peercellfun call is that each of the sets of input arguments {'rand', 10}, {'rand', 20} and {'rand', 30} was sent to one of the available slaves. The slave peer is waiting for something to arrive, and as soon as a job arrives, the slave executes rand(10), rand(20) or rand(30) and the output arguments are sent back to the master.

The example above demonstrates how you can use **[peercellfun](/reference/peercellfun)** to distribute jobs consisting of a single function that is executed on multiple input arguments. Another function that is available is **[peerfeval](/reference/peerfeval)**, which works similar to the normal MATLAB feval function.

### Starting the master on your computer

On your own computer you start a MATLAB session and type

    peermaster

The **[peermaster](/reference/peermaster)** command will start the network buffer and the peer discovery threads in the background and signal the other peers on the network that you are not willing to execute jobs for them.

In case you have a computer with a multi-core CPU (as most computers have nowadays), you can also start a peerslave for each of the idle cores. An efficient usage of your N-core CPU would consist of N slaves and one master.

### Starting the slaves on your own or on other computers

You start multiple MATLAB instances, one per available core. Within each MATLAB instance you type

    peerslave

The **[peerslave](/reference/peerslave)** command will start the network buffer and the peer discovery threads in the background, switch to slave mode to signal the other peers that it is willing to execute a job and wait until a request for execution comes in.

### Requirement: enough MATLAB licenses

The default usage as explained above is to start one exemplar of MATLAB for each of the peers. The MathWorks license agreement allows you to start multiple instances of MATLAB on a single computer. So if you run 4 peerslaved plus one peermaster on a quad-core computer, you require only a single MATLAB license (which you would have needed anyway). If you run one or multiple peerslaves on another computer, you will also need a MATLAB license for those. Also on other computers you will need one license per computer.

On Linux and macOS we have an alternative implementation that consists of a peerslave command-line executable which is started from the unix command line. The command-line executable does not require a MATLAB license when waiting for an incoming job, but will require a license as soon as a job comes in. It uses the MATLAB engine to execute the job. The peerslave command line executable allows you to set up a large number of peerslaves that wait in the background, with hardly any computational requirements, but that can kick in as soon as you want to run a bacth of distributed jobs.

### Requirement: network communication

The peers send and receive data over a TCP port and announce and discover each other over UDP multicast packets. The network switch should be configured to allow multicast network traffic: most of them are by default, but a network administra is able to switch multicasting off. Furthermore all the computers engaged in the peer nework should have their firewall sufficiently open to allow for the TCP and UDP communication.

### Requirement: shared filesystem

As soon as you want to execute a MATLAB function that you wrote yourself, you have to make sure the function can be found on the slave that should execute it. Also if your functions read and/or write data to disk, the directories with the data should be availale on all peers. This is most easily managed by having a shared network filesystem. On windows you can create your own share. The path settings (i.e. the location of your m-file) should be the same on all computers.

## License and Download

The peer toolbox has been developed as part of the [BrainGain](http://www.braingain.nu) project and is released as open source under the General Public License (GPLv2).

The **peer** toolbox is released along with FieldTrip, our toolbox for MEG/EEG data analysis. If you are not interested in EEG/MEG analysis, but ended up on this page because of a general MATLAB interest, you probably don't want to download the complete FieldTrip toolbox. The peer module can also be downloaded [from our ftp site](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/modules/) as separate and stand-alone toolbox.

Elsewhere on this website you can find more examples on the use of the peer toolbox in the list of [frequently asked questions](/faq#distributed_computing_in_matlab_using_the_peer-to-peer_toolbox).

## Frequently asked questions about distributed computing using this toolbox

{% include seealso tag1="faq" tag2="peer" %}

## Technical appendix

### How it works in detail

The idea is loosely based on the [FieldTrip buffer](/development/realtime/buffer), which is a multithreaded TCP server implemented as a mex file. The TCP server runs in a separate thread attached to MATLAB, but not blocked by MATLAB command execution. Let's refer to this as the **"peer server"**. The peer server has the following responsibilitie

1.  announce itself on the network
2.  discover the other peers
3.  send data to another peers
4.  receive data from other peers

Sending and receiving data implies sending the input arguments of a function that is remotely evaluated and receiving the output arguments of that function call.

On top of this peer server a number of regular MATLAB functions are implemented in a m-file. These regular functions encapsulate the low-level server details. On the master computer the commands could look like

    jobid  = peerfeval(functionname, argin);
    result = peerget(jobid);

and the command on a slave server would look like

    peerslave('maxtime', 3600);

which would keep running as a slave for one hour (3600 seconds) and evaluate the jobs that are sent.

### Implemented functionality in MATLAB

The peer-to-peer parallel toolbox for MATLAB consists of a compiled mex file that implements the low-level functionality, plus a collection of end-user functions. The most important end-user functions are descibed here.

#### Peercellfun(...)

This executes a function on all the elements of a cell-array. Each cell is executed on another peer, and the execution is in parallel. Once all cells have been executed, the results are gathered and returned to the user as cell-array. For example

    peercellfun('plus', {1, 2, 3}, {1, 2, 3})

would return

    {2, 4, 6}

and

    peercellfun('rand', {1, 2, 3}, 'UniformOutput', false)

would return

    {[1x1]  [2x2]  [3x3]}

Its interface is identical to the standard MATLAB cellfun() command except that only function handlers to external (non-anonymous) functions can be passed.

#### Peerfeval(...)

The MATLAB session that executes the peereval command searches for a peer that acts as slave, and sends the job (the function name and the input arguments) to the available slave peer. The slave peer evaluates the function on the input arguments and subsequently writes the output arguments back to the peer server of the host MATLAB session, i.e. the session that initiated the job.

Multiple peerevals can be executed without explicitely waiting for the results to return, hence the peer server (running on the master) should be able to receive and hold multiple "argouts".

The jobid should include information about the peer to which the job was assigned. Furthermore, information about the begin and end time would be usefull to estimate the time it takes to execute similar jobs.
Its interface is identical to the standard MATLAB feval() command.

#### Peerget(...)

This gets the input arguments (function name and input arguments) from the local server, or the output arguments that have been returned to local peer server.

When getting a job to be executed: the job should include the function name, the input arguments and the id of the host to which the results have to be returned.

When getting the result of a job: if the job has not finished yet, it should indicate that it is still in progress.

#### Peermaster(...)

Starts all peer threads (if needed) and switches to master mode. After switching to master mode, you can use submit jobs for remote execution.

When in master mode, the server will not accept incoming data for jobs that should be executed but it does accept incoming data corresponding to the output arguments of jobs that have been executed on other peers.

Note that peercellfun will automatically execute peermaster.

#### Peerzombie(...)

This ensures that all threads are running and sets the peer in zombie mode. As a zombie, the peer will not allow any job requests or job results to be written to it. It still announces itself to the other peers in the network and you can think of this as the default/unspecified mode.

#### Peerslave(...)

In slave mode a peer accepts the input arguments of a single job. It constantly checks for the availability of a job (on it's own server), and if a job is available it is executed.

The code inside peerslave looks like this

    while (true)
    job = peerget('job');
    if ~isempty(job)
      argout = feval(job.functionname, job.argin{:});
      peerput(job.hostid, argout);
    else
      sleep(0.1);
    end
    end

#### Peerreset(...)

Removes all existing jobs from the buffer and switches to zombie mode. This can be useful if you abort (with ctrl-c) a distributed job that you submitted with peercellfun.

#### Peerinfo(...)

Displays information about the local peer.

#### Peerlist(...)

Displays information about all the peers in the network.

### Command line peerslaves that do not need MATLAB

The disadvantage of running peerslave inside MATLAB is that each slave requires one active MATLAB license, even while waiting for a job. To allow for having a lot of idle slaves on the network that do not take licenses when not in use, I have implemented a command-line peerslave which is an executable that you start from the command line. The following compiled executables are currently included

- peerslave.glnxa64 (Linux, 64-bit)
- peerslave.glnx86 (Linux, 32-bit)
- peerslave.maci64 (macOS, 64-bit)
- peerslave.maci (macOS, 32-bit)

The command-line peerslave starts the threads, waits for an incoming job, and starts the MATLAB engine to evaluate the job. After MATLAB is done, the results are sent back to the master. If the MATLAB engine is idle for 30 seconds, it is closed and the license is returned to the network license server.

### Announce & Discover

All peers are able to locate each other automatically by two threads that are running in the background of the peer server. It is an ad-hoc network with auto-discovery, so is not necessary to manage a list with all the nodes that participate in the peer-to-peer network.

The **announce** thread multicasts a message with some host information (address, port, status) over the network. The announce packet is sent once every second.

The **discover** thread listens to the network. Each time an announce packet is detected, it is added to the list of known hosts. Besides adding the hostname, it attached (or updates) a timestamp at which the host was seen.

A third **expire** thread is running which removes old peers from the list. If a previously announced peer is not seen for a few seconds, it expires and is removed from the list of known hosts. This ensures that a peer which is shut down will be removed.

This list of known hosts is used to determine which peers are available for receiving a computational job.

### Communicating the input data for a job and returning the results

The tcpserver thread is constantly listening for incoming TCP connections.

If the peer is running in **idle slave** mode, it accepts a incoming connection that can write the input data for a job. If the peer is running in **busy slave** mode (i.e. busy executing a job), no connections are allowed. After finishing the computation, the slave writes the results of the job back to the tcpserver thread that the master is running.

The tcpserver thread of the master allows for multiple incoming connections, because multiple slaves might finish their computations at around the same time and hence send their results back simultaneously.

The tcpserver of a peer that runs as zombie does not allow any incoming connection.

### Some considerations

The following is a list with details that are already implemented and/or supported.

- each MATLAB session is either master (i.e. sending/receiving jobs) or slave (performing jobs)
- there can be multiple masters and multiple slaves on the same network (preferably many more slaves than masters)
- at the end of the day people would keep MATLAB running, and type "peerslave", resulting in the while-loop mentioned above
- the next morning people return to their computer and do ctrl-c
- the pwd and the path are passed along with the job, so that the peer can load users data and/or feval users scripts
- fair sharing is implemented based on the estimated execution time
- warnings and errors are captured and sent back to the master
- by using additional information from the announce packet (speed and/or memory), the master selects the preferred slave for job execution (typically the one with the best memory match)
- access to a peer can be restricted based on a list of users, or a list of host names
- localhost communication is possible with tcp/ip over the loopback device
- localhost communication is possible with unix domain sockets (linux only)
- it is possible to give a p2p network a name, c.f. WORKGROUP on windows networks, this can be combined with access restictions
- if a job does not return in a given amount of time, it will be resubmitted
- output on screen can be captured in a diary file and sent back to the master

The following is a list with unassorted ideas and considerations for improving and/or using the peer-to-peer parallel toolbox in an efficient manner in the typical research lab setting.

- localhost slaves should be preferred over remote hosts
- security is not part of this design, but can be implemented by running the MATLAB slave session in a sandbox (i.e. as unpriviledged user)

### Security

The whole mechanism does not have inherent security mechanisms implemented. An malevolent user could do

peerfeval('system', 'rm -rf \*')

erasing all users files on the computer hosting the slave. To solve this problem, the MATLAB session with the peerslave server should be running under an unpriviledged account, i.e. as a user without write access to the important parts of the file system.

### Relation between multiple peers

The schematic figure below shows how MATLAB and the peer server (running as a mex file) work together in writing and receiving data from other peers.

{% include image src="/assets/img/development/module/peer/peer1.png" %}
