---
layout: default
---

##  FT_WARNING

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_warning".

`<html>``<pre>`
    `<a href=/reference/ft_warning>``<font color=green>`FT_WARNING`</font>``</a>` prints a warning message on screen, depending on the verbosity 
    settings of the calling high-level FieldTrip function. This function works
    similar to the standard WARNING function, but also features the "once" mode.
 
    Use as
    ft_warning(...)
    with arguments similar to fprintf, or
    ft_warning(msgId, ...)
    with arguments similar to warning.
 
    You can switch of all warning messages using
    ft_warning off
    or for specific ones using
    ft_warning off msgId
 
    To switch them back on, you would use 
    ft_warning on
    or for specific ones using
    ft_warning on msgId
    
    Warning messages are only printed once per timeout period using
    ft_warning timeout 60
    ft_warning once
    or for specific ones using
    ft_warning once msgId
 
    You can see the most recent messages and identifier using
    ft_warning last
 
    You can query the current on/off/once state for all messages using
    ft_warning query
 
    See also `<a href=/reference/ft_error>``<font color=green>`FT_ERROR`</font>``</a>`, `<a href=/reference/ft_warning>``<font color=green>`FT_WARNING`</font>``</a>`, `<a href=/reference/ft_notice>``<font color=green>`FT_NOTICE`</font>``</a>`, FT_warning, `<a href=/reference/ft_debug>``<font color=green>`FT_DEBUG`</font>``</a>`, ERROR, WARNING
`</pre>``</html>`

