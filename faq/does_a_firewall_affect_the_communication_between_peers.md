---
title: Does a firewall affect the communication between peers?
tags: [faq, peer]
---

# Does a firewall affect the communication between peers?

All communication between peers is done over the TCP/IP network. Peers announce themselves to the whole network with a multicast packet, a "master" peers send the input data for a job after connecting to a TCP socket on a "slave" peer, and a "slave" peer returns the output data after connecting to a TCP socket on the master.

To speed up the communication between peers that are running on the same physical computer (i.e. two MATLAB sessions on a single computer), the peers use the localhost TCP/IP interface. Besides sending a multicast packet that can be picked up by all computers in the network (if firewall settings allow), the peers are also sending a packet to localhost. This packet will be received by the localhost, regardless of the firewall or presence of a network connection. Upon receiving a packet, the peer will automatically determine whether that packet is from a peer running on the same computer. If that is the case, they will automatically communicate over the localhost interface.

The communication between peers that are running on a single computer is not affected by the presence of a software firewall on the computer. The communication between peers on different computers is affected by the presence of a firewall. The announcements are sent to UDP port 1700. Sending the the input and output data of jobs is done with TCP on the network ports 170x, where x is the peer number. Typically for a quad-core computer the peers will be running on port 1701, 1702, 1703 and 1703.

You can see the ports used for the TCP connection in MATLAB by typing

    peerinfo

which results in something like this

    >> peerinfo
    there are   1 peers running as master
    there are   2 peers running as idle slave
    there are   0 peers running as busy slave
    there are   0 peers running as zombie
    master      at roboos@mentat001.fcdonders.nl:1701, group = unknown, hostid = 274009645
    idle slave  at roboos@mentat003.fcdonders.nl:1701, group = unknown, hostid = 902023272
    idle slave  at roboos@mentat002.fcdonders.nl:1701, group = unknown, hostid = 194834309
