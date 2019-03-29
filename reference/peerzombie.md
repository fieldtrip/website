---
title: peerzombie
---
```
 PEERZOMBIE starts the low-level peer servicesand switches to zombie
 mode. As a zombie, the peer will not allow any job requests or job results
 to be written to it. It still announces itself to the other peers in the
 network and you can think of this as the "default" or "unspecified" mode.

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

 See also PEERMASTER, PEERSLAVE, PEERRESET
```
