---
layout: default
---

##  PEERGET

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help peerget".

`<html>``<pre>`
    `<a href=/reference/peerget>``<font color=green>`PEERGET`</font>``</a>` get the output arguments after the remote job has been executed.
 
    Use as
    jobid  = peerfeval(fname, arg1, arg2, ...)
    argout = peerget(jobid, ...)
 
    Optional arguments can be specified in key-value pairs and can include
    StopOnError    = boolean (default = true)
    timeout        = number, in seconds (default = 1)
    sleep          = number, in seconds (default = 0.01)
    output         = string, 'varargout' or 'cell' (default = 'varargout')
    diary          = string, can be 'always', 'warning', 'error' (default = 'error')
 
    See also `<a href=/reference/peerfeval>``<font color=green>`PEERFEVAL`</font>``</a>`, `<a href=/reference/peercellfun>``<font color=green>`PEERCELLFUN`</font>``</a>`
`</pre>``</html>`

