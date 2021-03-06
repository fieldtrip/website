---
title: How can I stop the different threads created by peercontroller and peerworker?
tags: [faq, peer]
---

# How can I stop the different threads created by peercontroller and peerworker?

The easiest way to do it is by:

    clear all

If you don't want to lose your current workspace you can do:

    clear peer

or alternatively

    peer('tcpserver',   'stop')
    peer('announce',    'stop')
    peer('discover',    'stop')
    peer('expire',      'stop')

Either way will stop the threads created by the peer mex file (which is started by **[peercontroller](https://github.com/fieldtrip/fieldtrip/blob/release/peer/peercontroller.m)** and **[peerworker](https://github.com/fieldtrip/fieldtrip/blob/release/peer/peerworker.m)**).
