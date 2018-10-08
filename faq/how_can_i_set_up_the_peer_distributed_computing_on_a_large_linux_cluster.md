---
layout: default
---

{{tag>faq peer}}

## How can I set up the peer distributed computing on a large Linux cluster?

At the Donders Centre we have a Linux cluster with approximately 50 quad-core desktop computers, each with 8-12 GB of RAM (mentat195 to mentat245). 

Additionally we have a small number of rack-mounted "big-memory" computers with 16-48 GB of RAM each (mentat001 to mentat005).

We run command-line peerslaves on a selection of the linux nodes in our mentat cluster. To ensure that there is always a certain minimum of slaves available, mentat005 (12 cores, 48 GB of RAM) serves as dedicated server. All other mentat cluster nodes also allow interactive logins of users (through ssh and vnc), and other software, e.g. FSL, FreeSurfer, or interactive MATLAB sessions can be started. To ensure that the peerslaves don't interfere with the interactive use, the smartmem and smartcpu algorithms have been implemented  

The peerslave shell script (included in the release) demonstrates how we start all the slaves and keep them running on all the nodes. On each linux node there is a "peerslave start" line in a cronjob, which ensures that slaves that have crashed will be restarted.

 

