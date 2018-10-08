---
layout: default
---

##  FT_DEBUG

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_debug".

`<html>``<pre>`
    `<a href=/reference/ft_debug>``<font color=green>`FT_DEBUG`</font>``</a>` prints a debug message on screen, depending on the verbosity 
    settings of the calling high-level FieldTrip function.
 
    Use as
    ft_debug(...)
    with arguments similar to fprintf, or
    ft_debug(msgId, ...)
    with arguments similar to warning.
 
    You can switch of all messages using
    ft_debug off
    or for specific ones using
    ft_debug off msgId
 
    To switch them back on, you would use 
    ft_debug on
    or for specific ones using
    ft_debug on msgId
    
    Messages are only printed once per timeout period using
    ft_debug timeout 60
    ft_debug once
    or for specific ones using
    ft_debug once msgId
 
    You can see the most recent messages and identifier using
    ft_debug last
 
    You can query the current on/off/once state for all messages using
    ft_debug query
 
    See also `<a href=/reference/ft_error>``<font color=green>`FT_ERROR`</font>``</a>`, `<a href=/reference/ft_warning>``<font color=green>`FT_WARNING`</font>``</a>`, `<a href=/reference/ft_notice>``<font color=green>`FT_NOTICE`</font>``</a>`, FT_debug, `<a href=/reference/ft_debug>``<font color=green>`FT_DEBUG`</font>``</a>`, ERROR, WARNING
`</pre>``</html>`

