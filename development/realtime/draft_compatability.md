---
title: Suggested improvements for compatibility across versions
tags: [realtime, development]
---

# Suggested improvements for compatibility across versions

This section pertains to the implementation of backward compatibility in the C language reference implementation.

The formal description of the communication protocol should independent of the implementation also specify how to deal with network messages (e.g., requests and responses) that are not known.

### Providing backward compatibility within the server

This section discusses an alternative approach, where the TCP server can handle multiple protocol versions by calling different versions
of the "dmarequest" function in a switch statement based on the incoming version number. This would make it possible to connect older clients
to a more recent server.

On the client side (MATLAB), the different protocol versions would be handled by different MEX files (old versions frozen) and glue code in MATLAB.
This would make it possible to connect a client from a recent FieldTrip version (say, talking protocol version 3 natively) to an older server (V1).
The logic would involve detecting the server version by sending requests with decreasing client versions (using different MEX-files) until a call succeeds.

#### Advantages

- High compatibility, easy for (naive) users

#### Disadvantages

- Probably hard to maintain for developers in the long run
- Might be frustrating for power users (e.g., for debugging), since the involved version switches add one more layer of code and complexity.
- Hard to introduce changes on data structure level, e.g., for adding a _timestamp_ field to events: If two different versions of "dmarequest" can write events to the same ringbuffer, we effectively get mixed data structures in there. If such a change becomes necessary at V5, we would need to change the server code for V1-V4 as well.
- Since the client cannot be sure that a certain feature is available (e.g., polling for new samples with a timeout, asking for events by number), higher-level code needs to stick to V1-type operations for compatibility.
- Existing users (providers of acquisition clients) have little incentive to upgrade to a more recent, more powerful protocol, since new users can already connect. This makes the point mentioned above more severe.
- How to add new language bindings (e.g., Python / Java)? Should a language binding initiated at V4 include support for V1-V3 as well?

#### Practical notes

- Old versions of the "dmarequest" function should be kept, starting with V2 it should get a version number suffix. Protocol data structures, when modified, should also be duplicated and renamed to get a version number suffix, so the old functions (based on old data structures) still compile.
- It would probably be worthwhile to clean up the code in the sense that (now) static variables get moved to a C "struct" that corresponds to a logical unit and a specific version number. This includes the various pointers to data, events, and header information, but also the mutexes to protect them. If all data fields that make up a V1-buffer are contained in a struct called, e.g., "ft_buffer_container_v1", later versions can derive similar data structures by including the previous one as a field, and adding new facilities (e.g., an array of chunks) at the end of their own (native-version) structure.

### Providing adapters for compatibility

Instead of providing compatibility at the level of the server or the client or both, we could implement stand-alone **adapters**, that is, we could provide a V2 server that acts as a V1 client to grab data (samples + events) out of a V1 server, but then provide that data conveniently to V2 clients.

#### Advantages and disadvantages

- Yet another tool needs to be maintained (but the tool is relatively simple)
- The main FieldTrip buffer code (C) can be kept clean (one version only)
- The language binding code can be kept clean (one version only)
- A second buffer adds a bit more latency (but the 2nd connection can always be local TCP), and complicates the setup
- Existing users (with older protocol version) can still be talked to, but there is clear incentive to upgrade

## See also

- [draft network](/development/realtime/draft_network)
- [draft implementation](/development/realtime/draft_implementation)
- [draft header chunks](/development/realtime/draft_header_chunks)
- [draft compatibility](/development/realtime/draft_compatability)
- [scratchpad](/development/realtime/scratchpad)
