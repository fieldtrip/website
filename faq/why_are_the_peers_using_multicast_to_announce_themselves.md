---
layout: default
tags: faq peer
---

## Why are the peers using multicast to announce themselves?

The feature of a peer-to-peer network is that peers can find each other and request resources (e.g. pieces of a file). The FieldTrip peer-to-peer distributed computing toolbox allows to share computational resources. The network is not managed, i.e. there is not a single location where all information about available peers is collected. Instead, all peers communicate their presence and status to all other peers. This is achieved by the peers joining a multicast network. 

Besides sending a multicast package over the network, which can be picked up by peers that are running on other computers, each peer also sends an announce packet to localhost over the loopback device, i.e. 127.0.0.1. That packet is not sent over the network, but can be picked up by other peer instances (i.e. multiple matlab sessions) on the same computer. All peer communication is done over the TCP/IP network, also when running multiple peers on a single computer. If two peers on one computer communicate, they will do so over the localhost connection and the data will actually not be sent over the network.

Below you'll find an explanation of the difference between unicast, multicast and broadcast (taken from [here](http://www.inetdaemon.com/tutorials/internet/ip/addresses/unicast_vs_broadcast.shtml)).

### Unicast

Unicast packets are sent from host to host. The communication is from a single host to another single host. There is one device transmitting a message destined for one reciever.

### Broadcast

Broadcast is when a single device is transmitting a message to all other devices in a given address range. This broadcast could reach all hosts on the subnet, all subnets, or all hosts on all subnets. Broadcast packets have the host (and/or subnet) portion of the address set to all ones. By design, most modern routers will block IP broadcast traffic and restrict it to the local subnet.

### Multicast

Multicast is a special protocol for use with IP. Multicast enables a single device to communicate with a specific set of hosts, not defined by any standard IP address and mask combination. This allows for communication that resembles a conference call. Anyone from anywhere can join the conference, and everyone at the conference hears what the speaker has to say. The speaker's message isn't broadcasted everywhere, but only to those in the conference call itself. A special set of addresses is used for multicast communication.
