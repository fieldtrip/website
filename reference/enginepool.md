---
layout: default
---

##  ENGINEPOOL

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help enginepool".

`<html>``<pre>`
    `<a href=/reference/enginepool>``<font color=green>`ENGINEPOOL`</font>``</a>` manages the pool of MATLAB engine workers that is available
    for distributed computing
 
    Use as
    enginepool open &lt;number&gt; &lt;command&gt;
    enginepool close
    enginepool info
 
    The number specifies how many MATLAB engines should be started. In general
    it is advisable to start as many engines as the number of CPU cores.
 
    The command is optional. It can be used to specify the MATLAB version
    and the command-line options. The default for Linux is
    command = "matlab -singleCompThread -nodesktop -nosplash"
 
    See also `<a href=/reference/enginecellfun>``<font color=green>`ENGINECELLFUN`</font>``</a>`, `<a href=/reference/enginefeval>``<font color=green>`ENGINEFEVAL`</font>``</a>`, `<a href=/reference/engineget>``<font color=green>`ENGINEGET`</font>``</a>`
`</pre>``</html>`

