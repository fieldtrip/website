---
layout: default
---

##  PEERMASTER

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help peermaster".

`<html>``<pre>`
    `<a href=/reference/peermaster>``<font color=green>`PEERMASTER`</font>``</a>` starts the low-level peer services and switches to master
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
 
    See also `<a href=/reference/peerslave>``<font color=green>`PEERSLAVE`</font>``</a>`, `<a href=/reference/peerreset>``<font color=green>`PEERRESET`</font>``</a>`
`</pre>``</html>`

