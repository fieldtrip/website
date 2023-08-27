---
title: Suggested changes to the reference implementation
tags: [realtime, development]
---

# Suggested changes to the reference implementation

### Provide a unified open_connection call

Currently, MATLAB users type 'buffer://hostname:port' for talking to a buffer, and thanks to some intelligence in
the MEX file, this translates into either opening a new TCP connection, reusing a connection, or talking directly to
a buffer embedded in the MEX file.

The C interface, however, is less consistent. For example, a TCP connection is opened using "open_connection(hostname, port)",
a connection using the new UNIX sockets facility is opened using "open_unix_connection(pathname)", and for direct memory access,
no such call is made. Robert proposed to provide a unified API also on the C level, that is, we would have one function that is called like

    con = open_connection("localhost:1972");   // open a TCP connection
    con = open_connection("/some/unix/path");  // open a UNIX/local domain connection
    con = open_connection("<dma>");            // "open" a direct memory "connection"

and that returns a data structure with information about the type of connection instead of a simple integer (or socket identifier).
This would naturally extend to future implementations (e.g., Windows pipes).

One small difficulty remains: Currently there is always only one buffer per process, which is identified by a socket number=0. If we ever want
to support having multiple buffers in the same process, we need some way to distinguish between them, and do so by using a string (as above).
However, the most natural way would be to encapsulate all variables of an embedded buffer in one C struct, and refer to that struct
by a pointer. How should we turn this into a string in a sensible way? Have a static array of pointers and use an index into that array?
Use the address of the pointer as a hex-string?

### Add prefixes to all C API functions and data structures

C does not know namespaces, so we should try to avoid too short names like "append" which might yield problems when linking
to other libraries at the same time. "ft*" or "ftb*" looks like a reasonable choice.

### Add higher-level C API calls for standard requests

Currently every C program using the FieldTrip buffer needs to do the same steps (fill request data structure, check response data
structure, clean up) over and over again. At least some of this could be made easier. This will also make it less painful to migrate
to newer protocol versions. C++ users can already use wrapper classes in FtBuffer.h for handling requests and responses,
which provide automatic cleanup.

## See also

- [draft network](/development/realtime/draft_network)
- [draft implementation](/development/realtime/draft_implementation)
- [draft header chunks](/development/realtime/draft_header_chunks)
- [draft compatibility](/development/realtime/draft_compatability)
- [scratchpad](/development/realtime/scratchpad)
