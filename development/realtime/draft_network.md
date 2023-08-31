---
title: Suggested changes to the network protocol
tags: [realtime, development]
---

# Suggested changes to the network protocol

### GET_REQ_VER: Get supported request and version numbers

The client sends an 8-byte triple with **version**=2, **command**=GET_REQ_VER (number to be specified later) and **bufsize=0**.
The server responds with the 8-byte message definition, followed by a list of triples in the form **command**,**oldest_version**,**newest_version**,
that is, for each command the server might be able to handle different versions. In this way, clients can check whether the server understands
all the requests that will be used on the client side.

Having this scheme means that we can easily add a new request without changing any of those already specified and used by clients,
e.g., we could introduce a "version 3" variant of a GET_EVT call, but leave all other calls unchanged (including the V2 GET_EVT call).
In this way V2 clients would be able to talk to the V2-3 server without problems, but a newer client would be able to make use
of the new call (and, say, talk V2 for all other requests). As an extreme, we could actually keep all V1 requests as they are, and
V1 clients would never notice a change to the server (SK: I would advise against this, because this means we also need to stick to
the limited error reporting we have in V1). Newer clients could send this directly after connecting, and then either report an error
(if the server does not provide all the requests they need), or adapt their protocol to the capabilities of the server.

### Better error reporting

Currently (V1) the server sends an error identifier that is specific to each request, e.g., GET_ERR for GET_XXX requests, and PUT_ERR for PUT_XXX requests, but it does not specify the type of error. We could drop the GET/PUT/... distinction since this provides almost no value, and should rather define more informative symbols like this (numerical values to follow

| error code               | meaning                                                                                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| FT_OK                    | the request was handled successfully                                                                                                            |
| FT_ERR_MEMORY            | the server could not fulfill the request due to failed memory allocation                                                                       |
| FT_ERR_UNKNOWN_REQUEST   | the server does not know how to handle the given **version**/**command** tuple                                                                 |
| FT_ERR_MALFORMED_REQUEST | the server recognised **version** and **command**, but the remainder of the request was invalid (e.g., too short / bad type fields)            |
| FT_ERR_NO_HEADER         | no header information is present yet (all GET requests fail in this case, as well as PUT_EVT + PUT_DAT)                                        |
| FT_ERR_DATA_MISMATCH     | returned when the client tries to write data of a different type or number of channels                                                         |
| FT_ERR_BAD_SELECT        | returned when the client tries to grab a specific interval of samples or events, which is not completely contained in the buffer [anymore/yet] |

### Retrieving events

When retrieving events, the server should always send the index of each event along with the response,
as this makes filtering and housekeeping much easier. With a minimal change versus V1, we can just amend the GET_EVT
request so it transmits the event index before the rest of its definition, so for this request only, events
would be transported by the following structure (fixed part = 36 bytes now

| field           | type   | description                                      |
| --------------- | ------ | ------------------------------------------------ |
| **index**       | uint32 | index of event                                   |
| **type_type**   | uint32 | data type of event _type_ field                  |
| **type_numel**  | uint32 | number of elements in event _type_ field         |
| **value_type**  | uint32 | data type of event _value_ field                 |
| **value_numel** | uint32 | number of elements in event _value_ field        |
| **sample**      | int32  | index of sample this event relates to            |
| **offset**      | int32  | offset of event w.r.t. sample (time)             |
| **duration**    | int32  | duration of the event                            |
| **bufsize**     | uint32 | number of remaining bytes (for _type_ + _value_) |

After this, we would transmit the _type_ and _value_ fields in the same way as V1.

On top of that, we can think about providing filter mechanisms on the server side.
For the **sample**, **offset** and **duration** field, we can easily support filtering on a (min/max) condition.
_type_ and _value_ could be filtered for an exact match. All filter conditions would be combined with
a logical _AND_ by the server.

How to serialize this request? After a fixed 8-byte
header, you could send

| field            | type   | intent                             | don't care condition           |
| ---------------- | ------ | ---------------------------------- | ------------------------------ |
| **min_index**    | uint32 | smallest allowed event index       | 0                              |
| **max_index**    | uint32 | biggest allowed event index        | MAX_UINT32                     |
| **min_sample**   | uint32 | smallest allowed sample index      | 0                              |
| **max_sample**   | uint32 | biggest allowed sample index       | MAX_UINT32                     |
| **min_offset**   | int32  | smallest allowed offset            | MIN_INT32                      |
| **max_offset**   | int32  | biggest allowed offset             | MAX_INT32                      |
| **min_duration** | int32  | smallest allowed duration          | MIN_INT32                      |
| **max_duration** | int32  | biggest allowed duration           | MAX_INT32                      |
| **type_type**    | uint32 | type of _type_ to match exactly    | MAX_UINT32=DATATYPE_UNKNOWN    |
| **type_numel**   | uint32 | length of _type_ to match exactly  | 0 (=> _type_ not transmitted)  |
| **value_type**   | uint32 | type of _value_ to match exactly   | MAX_UINT32=DATATYPE_UNKNOWN    |
| **value_numel**  | uint32 | length of _value_ to match exactly | 0 (=> _value_ not transmitted) |
| **bufsize**      | uint32 | size of remaining part in bytes    | _not used for filtering_       |
| _type_           | var.   | contents of the _type_ field       | always exact match, if present |
| _value_          | var.   | contents of the _value_ field      | always exact match, if present |

Remark 1: Why is the **sample** field defined to be a (signed) int32 originally?
Remark 2: Note that a logical _OR_ can still be achieved by sending multiple requests and then
filtering out duplicate events on the client side. _AND_ seems more useful.

### Timestamp field of events

Some of the offline file formats supported by FieldTrip have a _timestamp_ field for events. We should think about including this in the FieldTrip buffer as well. The type should be 64-bit double precision, with the IEEE standard NaN (not a number) indicating that this field is not filled. Otherwise, the content can be application specific, or for example contain the system time of a specific machine at which an event happened, maybe encoded as UNIX time (seconds and fractions thereof since the epoch / 1970). Currently the timing is based on samples alone, which makes it hard to fuse data from different sources.

#### WAIT_GET_DAT: Block the request until the desired data samples are available

Instead of requiring a separate WAIT_DAT and GET_DAT, it should be possible to request data that is not yet in the buffer, upon which the server would block until the requested data is available. This should include a error given a user-specified timeout. Requesting previous data that is not in the buffer (and will not get into the buffer any more) should also result in an error.

### GET_DAT: Retrieving samples with start and end index

Instead of reporting the number of samples inside the **datadef_t** field in the response to a GET_DAT (as in V1), the server should rather send the index of the first and last sample that is being transmitted. The number of samples can be inferred from that, but the opposite direction is not possible. This is useful because the ring buffer will loose old samples after some time, where the V1 GET_DAT without a (begsample;endsample) tuple makes it impossible for the client to infer which samples it got. Another possible extension is to include a filter condition to grab samples within certain limits (as opposed to grabbing the specific interval in V1).

(This would also be more consistent with the new GET_EVT call, where you get event indices as well).

### Atomic PUT_DAT + PUT_EVT

Many acquisition systems (e.g., Biosemi EEG + CTF MEG) provide continuously sampled trigger channels. Markers contained
in these channels will be turned into discrete events by the acquisition tools. However, while originally the continuous samples
and the markers in the trigger channels come from the same data block (e.g., from the USB driver or a shared memory segment),
it is not well defined whether the tools should first write the events or the samples to the FieldTrip buffer. This has consequences
for the analysis side: For example, if a client polls for new data, and does so just in the time between the acquisition tool writing
the samples and the events to the buffer, this client will only notice the new samples, might process them, and then move on to the next block.
The events will only be visibile in the next polling operation. The reverse situation is also conceivable, but here the problem is less
severe because the client "knows" that if there are new events present, the corresponding samples must at some point follow.

Things to think about: Should it be mandatory to always write events first, then samples? Or should we add a request for writing samples
and events at the same time (atomically with respect to access from other clients)? Should this request replace the old PUT_DAT call?

### PUT_HDR

We should think about setting the desired size of the ring buffers for both events and samples in this request, since this is
where the memory gets allocated (also depends on the number of channels), and as such also where possible errors will be reported.

On the other hand, often the acquisition client will care less about the length of the buffer than the processing client, and in this
case it would be better to have a separate call (from the processing client) to define the desired ring buffer size, before the acquisition
client puts the header.

#### Running identifier

It would also be useful to include something like a running ID in the header information, which automatically gets incremented for every
PUT_HDR call. Currently, it's possible that clients A writes a header, client B reads it, client A writes another header, client B goes on without
noticing. Re-writing the header often occurs when acquisition devices are restarted (e.g., acq2ft will re-write the header when the user enables head-localization in Acq).

### Chunks: Semantics and handling

Chunks have been introduced recently in version 1 to enable transmitting meta information such as channel names, calibration values, or MR protocol data.
The current (V1) way of handling those is simple: they are always written and retrieved together with the header. In fact, the buffer server does not
care at all about the contents and types of the chunks. As a downside, GET_HDR requests get slow if large chunks are present (e.g., CTF system).

Robert has proposed adding separate requests for adding and reading chunks. Issues to think abou

- Clients need a way to determine which chunks are present - this is easy.
- Uniqueness of chunks: Do we allow multiple chunks of the same type (e.g., for representing different general purpose key/value pairs)?
- Do we allow a chunk to change over time? If so, clients need a way to determine whether a certain chunk has been updated since it was last read.

## See also

- [draft network](/development/realtime/draft_network)
- [draft implementation](/development/realtime/draft_implementation)
- [draft header chunks](/development/realtime/draft_header_chunks)
- [draft compatibility](/development/realtime/draft_compatability)
- [scratchpad](/development/realtime/scratchpad)
