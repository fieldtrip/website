---
layout: default
---

##  ENGINEGET

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help engineget".

`<html>``<pre>`
    `<a href=/reference/engineget>``<font color=green>`ENGINEGET`</font>``</a>` get the output arguments after the remote job has been executed.
 
    Use as
    jobid  = enginefeval(fname, arg1, arg2, ...)
    argout = engineget(jobid, ...)
 
    Optional arguments can be specified in key-value pairs and can include
    StopOnError    = boolean (default = true)
    timeout        = number, in seconds (default = 0, i.e. return immediately if output cannot be retrieved)
    sleep          = number, in seconds (default = 0.01)
    output         = string, 'varargout' or 'cell' (default = 'varargout')
    diary          = string, can be 'always', 'warning', 'error' (default = 'error')
 
    See also `<a href=/reference/enginefeval>``<font color=green>`ENGINEFEVAL`</font>``</a>`, `<a href=/reference/enginecellfun>``<font color=green>`ENGINECELLFUN`</font>``</a>`, `<a href=/reference/enginepool>``<font color=green>`ENGINEPOOL`</font>``</a>`
`</pre>``</html>`

