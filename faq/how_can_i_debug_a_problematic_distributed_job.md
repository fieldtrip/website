---
title: How can I debug a problematic distributed job?
tags: [faq, peer, debug]
---

# How can I debug a problematic distributed job?

A distributed job may fail for various reasons. If the error is properly caught by the worker that executed the job, **[peercellfun](/reference/peer/peercellfun)** will display the error on the controller. If **[peercellfun](/reference/peer/peercellfun)** fails to return the output arguments of the jobs that it sent out, you'll have to dig deeper...

This page describes a number of strategies that you can use.

## Try the normal cellfun

Peercellfun replicates the functionality ofthestandard MATLAB cellfun function, except that the jobs are distributed. You can try

    cellfun(@yourfunction, {arg1, arg2, ...})

instead of the distributed

    peercellfun(@yourfunction, {arg1, arg2, ...})

## Run the MATLAB code as another user

The problem may be related to file and/or directory permissions because the peer workers are running as another user. You can log in as that user and start an interactive MATLAB. Subsequently in that interactive session you can try to execute the MATLAB commands or script that you want the workers to execute. Within the interactive session you will easily recognize the permission problems, and you can change your own directory and file permissions so that the other user can access them.

## Start an interactive peerworker

You can start another interactive MATLAB session, preferably on another computer, and within that MATLAB session start a **[peerworker](/reference/peer/peerworker)**. To ensure that the controller will pick this worker, and not one of the other idle workers on the network, you have to specify both to your controller and your worker that they should restict them selves based on username using the allowuser option.

In the controller MATLAB session you do
peercontroller('allowuser, 'roboos');
and in the worker MATLAB session you start
peerworker('allowuser', 'roboos');

Since both MATLAB sessions will run under your own account (here with the account name "roboos"), the controller and worker will exclusively communicate.

Subsequently, you can restart the **[peercellfun](/reference/peer/peercellfun)** command in the controller and look at what happens inside the worker MATLAB session.

## Start a worker as another user

A common, but difficult to diagnose, problem is that the worker does not have the permissions to read the function m-file that you are requesting to be evaluated, e.g., because your home directory is not accessible to other users.

To test this, you can log in using the public account, which has the password "public".

    ssh public@mentatXXX

The public user does not have any privileges or disk quota, so logging in under this account is normally not of interest to you or anyone else.

Once logged in as other user, you start an interactive MATLAB session and a **[peerworker](/reference/peer/peerworker)** inside it. To ensure that your controller will send the job to this worker, and not to another one in the network, you can use the allowgroup option.

You start the **[peercontroller](/reference/peer/peercontroller)** using

    peercontroller('allowgroup', 'xyz');

and the **[peerworker](/reference/peer/peerworker)** as

    peerworker('group', 'xyz');

This will place the worker in the xyz group, and the controller will only send its jobs to that group. To make the controller and the worker talking exclusively to each other in either way, you can use

    peercontroller('group', 'xyz', 'allowgroup', 'xyz');

and

    peerworker('group', 'xyz', 'allowgroup', 'xyz');

Subsequently you retry the **[peercellfun](/reference/peer/peercellfun)** and look at the screen of the interactive worker MATLAB session.

## Start a worker in non-graphical mode

It might be that the problem is related to the graphical output of the function that you are trying to evaluate. The workers that are running by default on the DCCN Linux cluster do not have a graphical output. Some graphical functions (like plotting) has been reported to work, but others (like drawing a GUI) have been reported to fail.

To ensure that a non-graphical worker can execute your jobs, you can use putty to connect to a Linux cluster node. Subsequently you start MATLAB in the putty window and start **[peerworker](/reference/peer/peerworker)** with
peerworker('allowuser', 'yourid');

Subsequently you can restrict your **[peercontroller](/reference/peer/peercontroller)** to the same userid (you can also use groups for this, see above) and retry the execution of the jobs with **[peercellfun](/reference/peer/peercellfun)**.

## Use the MATLAB debugger in the worker

If all of the methods described above fail, you'll have to resort to using the MATLAB debugging facilities. For this to work, you also should start a single interactive worker and make sure that your controller sends his job there. I see two options for this

In the function that is executed you insert a "keyboard" statement. Since the worker runs like a normal MATLAB, it will jump to debug mode on that line and you can continue step-by-step.

You can also try to resolve the problem by typing "dbstop if caught error" in MATLAB prior to starting the **[peerworker](/reference/peer/peerworker)**. The worker will evaluate the function using peerexec, which does feval in a large try-catch loop. Note that a normal "dbstop if error" will not be sufficient, because the error is caught with the purpose of sending it back to the controller.
