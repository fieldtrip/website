---
title: Suggested improvements for handling header and chunks
tags: [realtime, development]
---

This is a draft for the calls involved in writing and reading header information and chunks, where the server
keeps a running identifier for the fixed part of the header, as well as for each chunk that is attached to
the current header.

### PUT_HDR

The client would send the following structure (after the usual `version;command;msgsize` triple):

| field         | type    | description                                                                 |
| ------------- | ------- | --------------------------------------------------------------------------- |
| `nchans`    | uint32  | number of channels                                                          |
| `fsamp`     | float32 | sampling frequency (Hz)                                                     |
| `data_type` | uint32  | type of the sample data (see table above)                                   |
| `bufsize`   | uint32  | size of remaining parts of the message in bytes (total size of all chunks)  |

and optionally a list of chunks (see V1 documentation for an overview).

The server would respond with a `version;errorcode;msgsize=0` triple.

### GET_HDR

The client would send the triple `version;command=GET_HDR;msgsize=0`, and the server would respond with:

| field         | type    | description                                                                  |
| ------------- | ------- | ---------------------------------------------------------------------------- |
| `nchans`    | uint32  | number of channels                                                           |
| `fsamp`     | float32 | sampling frequency (Hz)                                                      |
| `data_type` | uint32  | type of the sample data (see table above)                                    |
| `nsamples`  | uint32  | number of samples, must be 0 for PUT_HDR                                     |
| `nevents`   | uint32  | number of events, must be 0 for PUT_HDR                                      |
| `header_id` | uint32  | running ID of header, starts at 0, gets incremented after every PUT_HDR call |
| `bufsize`   | uint32  | size of remaining parts of the message in bytes                              |

and optionally a list of tuples

| `chunk_type` | uint32 | type of chunk (e.g., FT_CHUNK_CHANNEL_NAMES) |
| -------------- | ------ | -------------------------------------------- |
| `chunk_id`   | uint32 | running ID of this chunk type                |

From this response, the client can determine whether the header or any chunk has been (re-)written since
the last call to GET_HDR. At the same time, the amount of data transmitted is very small.

### PUT_CHUNK

With this request, a client can write a chunk to the buffer. If there already is a chunk of this type,
it will be **replaced** and the running ID of this chunk type will be increased. Otherwise, it will just
be added to the list of chunks the server maintains, and the running ID of this chunk will be 0.

The client would send the triple `version;command=PUT_CHUNK;msgsize`, as well as a chunk definition of the form

| field    | type   | description                                                      |
| -------- | ------ | ---------------------------------------------------------------- |
| `type` | uint32 | type of this chunk (see chunk documentation in V1)               |
| `size` | uint32 | size of this chunk in bytes (excluding the type and size fields) |
| `data` | var.   | contents of this chunk                                           |

The server would respond with a `version;errorcode;size=0` triple.

### GET_CHUNK

With this request, clients can retrieve particular chunks from the buffer.

The client would either just send the triple `version;command=GET_CHUNK;msgsize=0` for retrieving all chunks,
or it would also send a list of chunk `types` (uint32), with the `msgsize` indicating the length (in bytes) of this list.

The server will respond with the usual `version;errorcode;msgsize` triple, plus the list of requested chunks.
If any of the chunks the client asked for is not available, the server will only reply with an error (no chunks attached).

## See also

- [draft network](/development/realtime/draft_network)
- [draft implementation](/development/realtime/draft_implementation)
- [draft header chunks](/development/realtime/draft_header_chunks)
- [draft compatibility](/development/realtime/draft_compatability)
- [scratchpad](/development/realtime/scratchpad)
