---
layout: default
---

{{tag>faq peer}}

## What happens with a job that has an error on the slave?

The peer slave runs the command with feval in an try-catch loop. If the evaluation of the command results in an error, the error is caught and returned to the master. 

The default behavior of peercellfun is to retrow the error. That means that you will see exactly the same error that happened inside your job on the peer slave. Due to the error, peercellfun will stop evaluating other jobs and not return any results. You can identify the cause of the error and start the jobs once more with peercellfun.

To get more details on the error, you can use the diary option to peercellfun. It allows the vaues 'never' (default), 'error', 'warning' and 'always'. If set to something else than 'never', a diary file will be created on the peer slave and all screen output of your job running on the peer slave will be written to this diary file. After the job results or the job error message have been returned, peercellfun will display the content of the diary file in case of an error, a warning or always. Writing the diary file slows down the job evaluation, therefore it is disabled by default.



 
