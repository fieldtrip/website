---
layout: default
---

##  QSUBLIST

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help qsublist".

`<html>``<pre>`
    `<a href=/reference/qsublist>``<font color=green>`QSUBLIST`</font>``</a>` is a helper function that is used to keep track of all the jobs in a
    submitted batch. specifically, it is used to maintain the mapping between the
    job identifier in the batch queueing system and MATLAB.
 
    Use as
    qsublist('list')
    qsublist('killall')
    qsublist('kill', jobid)
    qsublist('getjobid', pbsid)
    qsublist('getpbsid', jobid)
 
    The jobid is the identifier that is used within MATLAB for the file names,
    for example 'roboos_mentat242_p4376_b2_j453'.
 
    The pbsid is the identifier that is used within the batch queueing system,
    for example '15260.torque'.
 
    The following commands can be used by the end-user.
    'list'      display all jobs
    'kill'      kill a specific job, based on the jobid
    'killall'   kill all jobs
    'getjobid'  return the mathing jobid, given the pbsid
    'getpbsid'  return the mathing pbsid, given the jobid
 
    The following low-level commands are used by `<a href=/reference/qsubfeval>``<font color=green>`QSUBFEVAL`</font>``</a>` and `<a href=/reference/qsubget>``<font color=green>`QSUBGET`</font>``</a>` for job
    maintenance and monitoring.
    'add'
    'del'
    'completed'
 
    See also `<a href=/reference/qsubcellfun>``<font color=green>`QSUBCELLFUN`</font>``</a>`, `<a href=/reference/qsubfeval>``<font color=green>`QSUBFEVAL`</font>``</a>`, `<a href=/reference/qsubget>``<font color=green>`QSUBGET`</font>``</a>`
`</pre>``</html>`

