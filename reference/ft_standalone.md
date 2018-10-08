---
layout: default
---

##  FT_STANDALONE

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_standalone".

`<html>``<pre>`
    `<a href=/reference/ft_standalone>``<font color=green>`FT_STANDALONE`</font>``</a>` is the entry function of the compiled FieldTrip application.
    The compiled application can be used to execute FieldTrip data analysis
    scripts.
 
    This function can be started on the interactive MATLAB command line as
    ft_standalone script.m
    ft_standalone script1.m script2.m ...
    ft_standalone jobfile.mat
    or after compilation on the Linux/macOS command line as
    fieldtrip.sh &lt;MATLABROOT&gt; script.m
    fieldtrip.sh &lt;MATLABROOT&gt; script1.m script2.m ...
    fieldtrip.sh &lt;MATLABROOT&gt; jobfile.mat
 
    It is possible to pass additional options on the MATLAB command line like
    this on the MATLAB command line
    ft_standalone --option value scriptname.m
    or on the Linux/macOS command line
    fieldtrip.sh &lt;MATLABROOT&gt; --option value scriptname.m
    The options and their values are automaticallly made available as local
    variables in the script execution environment.
 
    See also `<a href=/reference/ft_compile_standalone>``<font color=green>`FT_COMPILE_STANDALONE`</font>``</a>`
`</pre>``</html>`

