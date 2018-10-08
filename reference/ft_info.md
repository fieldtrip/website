---
layout: default
---

##  FT_INFO

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_info".

`<html>``<pre>`
    `<a href=/reference/ft_info>``<font color=green>`FT_INFO`</font>``</a>` prints an info message on screen, depending on the verbosity 
    settings of the calling high-level FieldTrip function.
 
    Use as
    ft_info(...)
    with arguments similar to fprintf, or
    ft_info(msgId, ...)
    with arguments similar to warning.
 
    You can switch of all messages using
    ft_info off
    or for specific ones using
    ft_info off msgId
 
    To switch them back on, you would use 
    ft_info on
    or for specific ones using
    ft_info on msgId
    
    Messages are only printed once per timeout period using
    ft_info timeout 60
    ft_info once
    or for specific ones using
    ft_info once msgId
 
    You can see the most recent messages and identifier using
    ft_info last
 
    You can query the current on/off/once state for all messages using
    ft_info query
 
    See also `<a href=/reference/ft_error>``<font color=green>`FT_ERROR`</font>``</a>`, `<a href=/reference/ft_warning>``<font color=green>`FT_WARNING`</font>``</a>`, `<a href=/reference/ft_notice>``<font color=green>`FT_NOTICE`</font>``</a>`, `<a href=/reference/ft_info>``<font color=green>`FT_INFO`</font>``</a>`, `<a href=/reference/ft_debug>``<font color=green>`FT_DEBUG`</font>``</a>`, ERROR, WARNING
`</pre>``</html>`

