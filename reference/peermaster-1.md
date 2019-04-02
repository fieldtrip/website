---
title: peermaster
---
```
 PEERMASTER starts the low-level peer services and switches to master
 mode. After switching to master mode, you can use submit jobs for
 remote execution. The server will not accept jobs to be executed,
 but does accept the output arguments of jobs that have been executed on
 other peers. Note that peercellfun will automatically execute peermaster.

 Use as
   peermaster(...)

 Optional input arguments should be passed as key-value pairs. The
 following options are available to limit the peer network, i.e. to
 form sub-networks.
   group       = string
   allowuser   = {...}
   allowgroup  = {...}
   allowhost   = {...}
   refuseuser   = {...}
   refusegroup  = {...}
   refusehost   = {...}
 The allow options will prevent peers that do not match the requirements
 to be added to the (dynamic) list of known peers. Consequently, these
 options limit which peers know each other. A master will not send jobs
 to peers that it does not know. A slave will not accept jobs from a peer
 that it does not know.

 See also PEERSLAVE, PEERRESET
```
