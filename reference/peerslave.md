---
title: peerslave
---
```
 PEERSLAVE starts the low-level peer services and switches to slave mode.
 Subsequently it will wait untill a job comes in and execute it.

 Use as
   peerslave(...)

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

 The following options are available to limit the number and duration
 of the jobs that the slave will execute.
   maxnum      = number (default = inf)
   maxtime     = number (default = inf)
   maxidle     = number (default = inf)

 The following options are available to limit the available resources
 that available for job execution.
   memavail    = number, amount of memory available       (default = inf)
   cpuavail    = number, speed of the CPU                 (default = inf)
   timavail    = number, maximum duration of a single job (default = inf)

 See also PEERMASTER, PEERRESET, PEERFEVAL, PEERCELLFUN
```
