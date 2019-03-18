---
title: How can I stop the different threads created by peermaster and peerslave?
tags: [faq, peer]
---

# How can I stop the different threads created by peermaster and peerslave?

The easiest way to do it is by:

    clear all

If you don't want to lose your current workspace you can do:

    clear peer

or alternatively

    peer('tcpserver',   'stop')
    peer('announce',    'stop')
    peer('discover',    'stop')
    peer('expire',      'stop')

Either way will stop the threads created by the peer mex file (which is started by **[peermaster](/reference/peermaster)** and **[peerslave](/reference/peerslave)**).
