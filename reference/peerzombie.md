---
layout: default
---

##  PEERZOMBIE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help peerzombie".

`<html>``<pre>`
    `<a href=/reference/peerzombie>``<font color=green>`PEERZOMBIE`</font>``</a>` starts the low-level peer servicesand switches to zombie
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
 
    See also `<a href=/reference/peermaster>``<font color=green>`PEERMASTER`</font>``</a>`, `<a href=/reference/peerslave>``<font color=green>`PEERSLAVE`</font>``</a>`, `<a href=/reference/peerreset>``<font color=green>`PEERRESET`</font>``</a>`
`</pre>``</html>`

