---
title: How can I debug a problematic distributed job?
tags: [faq, peer, debug]
---

# How can I debug a problematic distributed job?

A distributed job may fail for various reasons. If the error is properly caught by the slave that executed the job, **[peercellfun](/reference/peercellfun)** will display the error on the master. If **[peercellfun](/reference/peercellfun)** fails to return the output arguments of the jobs that it sent out, you'll have to dig deeper...

This page describes a number of strategies that you can use.

## Try the normal cellfun

Peercellfun replicates the functionality ofthestandard MATLAB cellfun function, except that the jobs are distributed. You can try

    cellfun(@yourfunction, {arg1, arg2, ...})

instead of the distributed

    peercellfun(@yourfunction, {arg1, arg2, ...})

## Run the MATLAB code as another user

The problem may be related to file and/or directory permissions because the peer slaves are running as another user. You can log in as that user and start an interactive MATLAB. Subsequently in that interactive session you can try to execute the MATLAB commands or script that you want the slaves to execute. Within the interactive session you will easily recognize the permission problems, and you can change your own directory and file permissions so that the other user can access them.

## Start an interactive peerslave

You can start another interactive MATLAB session, preferably on another computer, and within that MATLAB session start a **[peerslave](/reference/peerslave)**. To ensure that the master will pick this slave, and not one of the other idle slaves on the network, you have to specify both to your master and your slave that they should restict them selves based on username using the allowuser option.

In the master MATLAB session you do
peermaster('allowuser, 'roboos');
and in the slave MATLAB session you start
peerslave('allowuser', 'roboos');

Since both MATLAB sessions will run under your own account (here with the account name "roboos"), the master and slave will exclusively communicate.

Subsequently, you can restart the **[peercellfun](/reference/peercellfun)** command in the master and look at what happens inside the slave MATLAB session.

## Start a slave as another user

A common, but difficult to diagnose, problem is that the slave does not have the permissions to read the function m-file that you are requesting to be evaluated, e.g. because your home directory is not accessible to other users.

To test this, you can log in using the public account, which has the password "public".

    ssh public@mentatXXX

The public user does not have any privileges or disk quota, so logging in under this account is normally not of interest to you or anyone else.

Once logged in as other user, you start an interactive MATLAB session and a **[peerslave](/reference/peerslave)** inside it. To ensure that your master will send the job to this slave, and not to another one in the network, you can use the allowgroup option.

You start the **[peermaster](/reference/peermaster)** using

    peermaster('allowgroup', 'xyz');

and the **[peerslave](/reference/peerslave)** as

    peerslave('group', 'xyz');

This will place the slave in the xyz group, and the master will only send its jobs to that group. To make the master and the slave talking exclusively to each other in either way, you can use

    peermaster('group', 'xyz', 'allowgroup', 'xyz');

and

    peerslave('group', 'xyz', 'allowgroup', 'xyz');

Subsequently you retry the **[peercellfun](/reference/peercellfun)** and look at the screen of the interactive slave MATLAB session.

## Start a slave in non-graphical mode

It might be that the problem is related to the graphical output of the function that you are trying to evaluate. The slaves that are running by default on the DCCN Linux cluster do not have a graphical output. Some graphical functions (like plotting) has been reported to work, but others (like drawing a GUI) have been reported to fail.

To ensure that a non-graphical slave can execute your jobs, you can use putty to connect to a Linux cluster node. Subsequently you start MATLAB in the putty window and start **[peerslave](/reference/peerslave)** with
peerslave('allowuser', 'yourid');

Subsequently you can restrict your **[peermaster](/reference/peermaster)** to the same userid (you can also use groups for this, see above) and retry the execution of the jobs with **[peercellfun](/reference/peercellfun)**.

## Use the MATLAB debugger in the slave

If all of the methods described above fail, you'll have to resort to using the MATLAB debugging facilities. For this to work, you also should start a single interactive slave and make sure that your master sends his job there. I see two options for this

In the function that is executed you insert a "keyboard" statement. Since the slave runs like a normal MATLAB, it will jump to debug mode on that line and you can continue step-by-step.

You can also try to resolve the problem by typing "dbstop if caught error" in MATLAB prior to starting the **[peerslave](/reference/peerslave)**. The slave will evaluate the function using peerexec, which does feval in a large try-catch loop. Note that a normal "dbstop if error" will not be sufficient, because the error is caught with the purpose of sending it back to the master.
