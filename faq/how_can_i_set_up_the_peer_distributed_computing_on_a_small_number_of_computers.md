---
title: How can I set up the peer distributed computing on a small number of computers?
tags: [faq, peer]
---

# How can I set up the peer distributed computing on a small number of computers?

It is common for researchers to share their office with multiple people, each one with a workstation computer under their desk. In the evening, when everyone has gone home, those computers just stand around, unused. The peer distributed computing toolbox allows you to easily make use of them!

In the evening, when your colleagues are gone, you log in on their computer. Subsequently you start MATLAB and start **[peerslave](/reference/peerslave)** on the MATLAB command line. For a computer with a multicore CPU the best is to start multiple MATLAB sessions as peerslave, one per CPU core.

After starting the slaves on your colleagues computer, you go to your own computer, start a MATLAB session and type **[peerlist](/reference/peerlist)**.

This should show you the idle slaves on your colleagues' computers other computers. Subsequently you can get started with **[peercellfun](/reference/peercellfun)**.

Instead of using only peerslaves on your colleagues' computers, you should also start a few peerslaves on your own computer. The master will not be really busy, it just hands out the jobs and collects the results. To use the CPU in your own computer efficiently, you should have N+1 MATLAB sessions running on your computer, one for the master and N for the slaves (where N is the number of CPU cores). This should result in 100% CPU usage on your computer.

Please note that [firewall settings](/faq/does_a_firewall_affect_the_communication_between_peers) can affect the peer network.

## Access control

To ensure that the slaves that you have started cannot be accessed by another user on the same network, you can do

    peerslave('allowuser', `<yourusername>`)

If you explicitly want to share the computers with multiple people, you can do

    peerslave('allowuser', {`<username1>`, `<username2>`, ...})

If you want to control the computers to which the master submits the jobs, you can use the allowuser or allowhost options in **[peermaster](/reference/peermaster)**, i.e.

    peermaster('allowuser', `<yourusername>`)
    peercellfun(@funname, {...})

will only execute the jobs on your own slaves.

## The next morning...

In the morning, your colleagues might arrive earlier to their desk than you, and of course then they want their computer back. If the slaves are idle, they can simply exit the MATLAB sessions you started and regain control. If the slaves are still busy executing their job, they can simply kick you out (e.g. reboot, or ctrl-c your MATLAB slaves). The **[peercellfun](/reference/peercellfun)** will automatically resubmit the jobs that fail, i.e. if one of the slaves disappears, the job that it was running will be resubmitted elsewhere.

That is why you want also to have a few slaves running on your own computer: these will take over the remaining jobs, once all your colleagues' computers are confiscated again by their respective owners.
