---
layout: default
---

##  FT_WRITE_EVENT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_write_event".

`<html>``<pre>`
    `<a href=/reference/ft_write_event>``<font color=green>`FT_WRITE_EVENT`</font>``</a>` writes an event structure to a file, a message daemon
    listening on a network socked, or to another computer connected through
    the serial port.
 
    Use as
    ft_write_event(filename, event, ...)
 
    The first argument is a string containing the filename. The second
    argument is a structure with the event. Multiple events can be
    represented as a structure array.
 
    Events are represented as
    event.type      string
    event.sample    expressed in samples, the first sample of a recording is 1
    event.value     number or string
    event.offset    expressed in samples
    event.duration  expressed in samples
    event.timestamp expressed in timestamp units, which vary over systems (optional)
 
    Events can also be written to special communication streams
    by specifying the target as URI instead of a filename. Supported are
    buffer://&lt;host&gt;:&lt;port&gt;
    fifo://&lt;filename&gt;
    tcp://&lt;host&gt;:&lt;port&gt;
    udp://&lt;host&gt;:&lt;port&gt;
    mysql://&lt;user&gt;:&lt;password&gt;@&lt;host&gt;:&lt;port&gt;
    rfb://&lt;password&gt;@&lt;host&gt;:&lt;port&gt;
    serial:&lt;port&gt;?key1=value1&key2=value2&...
    rfb://&lt;password&gt;@&lt;host&gt;:&lt;port&gt;
 
    See also `<a href=/reference/ft_read_header>``<font color=green>`FT_READ_HEADER`</font>``</a>`, `<a href=/reference/ft_read_data>``<font color=green>`FT_READ_DATA`</font>``</a>`, `<a href=/reference/ft_read_event>``<font color=green>`FT_READ_EVENT`</font>``</a>`, `<a href=/reference/ft_write_data>``<font color=green>`FT_WRITE_DATA`</font>``</a>`
`</pre>``</html>`

