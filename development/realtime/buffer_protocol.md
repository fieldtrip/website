---
title: Low-level FieldTrip buffer TCP network protocol
tags: [realtime]
---

# Low-level FieldTrip buffer TCP network protocol

This page is part of the documentation series of the FieldTrip buffer for realtime acquisition. The FieldTrip buffer is a standard that defines a central hub (the [FieldTrip buffer](/development/realtime)) that facilitates realtime exchange of neurophysiological data. The documentation is organized in five main sections, being:

1.  description and general [overview of the buffer](/development/realtime/buffer),
2.  definition of the [buffer protocol](/development/realtime/buffer_protocol),
3.  the [reference implementation](/development/realtime/reference_implementation), and
4.  specific [implementations](/development/realtime/implementation) that interface with acquisition software, or software platforms.
5.  the [getting started](/getting_started/realtime) documentation which takes you through the first steps of real-time data streaming and analysis in MATLAB

This page provides a formal description of how the communication over the network is performed between the FieldTrip buffer server and clients.

The MATLAB implementation (i.e. the mex file) is by default included in the normal FieldTrip toolbox release. If you just want to use the FieldTrip buffer from within MATLAB, most of the information you'll find here is not relevant for you.

## What we aim to provide

The FieldTrip buffer is designed to facilitate transporting of data samples and events (also called markers) from an acquisition device (e.g., an EEG amplifier) to one or more (analysis) programs in real-time. Hereafter, we will refer to both the acquisition part and the analysis part(s) as **clients**, and we do not distinguish between clients that mostly write and clients that mostly read. Since we explicitly wish to include MATLAB scripts and other single-threaded programming environments as possible clients, it is apparent that we need some sort of buffering of data and events. The application (or part thereof) that does this is referred to as the **server**.

The FieldTrip buffer represents three elements: the header structure, the data matrix and a list of event structures. Since we target real-time usage, both the data matrix and the list of events will usually be implemented as a **ring buffer**, which means that after a time, old data samples and events will not be accessible anymore.

The binary TCP/IP network protocol allows client applications to be developed in an arbitrary programming language, e.g., C, MATLAB, Java or Python. The [network protocol](/development/realtime/buffer_protocol) documents the low-level protocol used for serializing requests and responses.

### Outside our scope

We do **not** aim to provide or specify:

- any kind of remote procedure calls, or direct communication between clients,
- an explicit way of setting up experiments,
- merging data from different acquisition systems,
- writing data to disk,
- a complete implementation for all possible programming languages (e.g., FORTRAN, COBOL),
- a complete implementation for all possible operating systems (e.g., Amiga, OS/2 Warp, Windows 95).

## FieldTrip buffer definition

For the communication the client sends a request, which always results in a response from the server. The request can for example be GET_DAT, and the response would contain the data. In case the request cannot be fulfilled (e.g., the requested data are not available), the server responds with an error. The request and the response consist of a binary message sent over TCP, which is described in detail below.

The buffer represents three elements: the header structure, the data matrix, and a list of event structures. The data matrix and the event list are both implemented as a ring buffer.

We are still unsure about how to support backwards-compatibility in the buffer. Currently (V1) request will only succeed if the client and the server use the same protocol version number.

We can stick to the fixed 8-byte prefix containing `version`, `command` and `bufsize` (indicating the size of the remaining message), but one of the more important issues is a strategy that allows for both flexibility and compatibility when it comes to fixes and extensions.

## Network protocol

Every request and response starts with the following fixed-size 8 byte structure which
corresponds to the definition of `messagedef_t` in "message.h" in the [reference implementation](/development/realtime/reference_implementation).

| field     | type   | description                                                        |
| --------- | ------ | ------------------------------------------------------------------ |
| `version` | uint16 | always = 1                                                         |
| `command` | uint16 | encodes the type of request (see further below)                    |
| `bufsize` | uint32 | describes the size (in bytes) of the remaining part of the message |

### Endianness

The buffer always stores data in its native format, that is, on a x86 compatible processor all numbers are stored in little-endian format, and on a PowerPC (G4/G5/...) numbers are stored in big-endian format. The server will automatically convert incoming requests and its responses to the endianness of the client, which is detected by the 16-bit `version` field. Clients can always transmit requests in their own native format, and can assume that the data they receive is in their native format.

Because we are relying on detecting endianness by looking at the 16-bit version number, we will get problems if we ever want to bump the version number to 256 or bigger.

### PUT_HDR: Put header information into the buffer

This request is used for initialising the buffer and setting header information like the number of channels and the sampling frequency. Clients need to transmit a fixed structure and optionally a set of _chunks_ (`chunk_t` in "message.h"). The `command` number of this request is 0x101 (=257 in decimal notation).

The fixed part (24 bytes) consists of the following (`headerdef_t` in "message.h")

| field       | type    | description                                                                |
| ----------- | ------- | -------------------------------------------------------------------------- |
| `nchans`    | uint32  | number of channels                                                         |
| `nsamples`  | uint32  | number of samples, must be 0 for PUT_HDR                                   |
| `nevents`   | uint32  | number of events, must be 0 for PUT_HDR                                    |
| `fsamp`     | float32 | sampling frequency (Hz)                                                    |
| `data_type` | uint32  | type of the sample data (see table above)                                  |
| `bufsize`   | uint32  | size of remaining parts of the message in bytes (total size of all chunks) |

The fixed part of the header is sufficient to interpret the data as a feature vector of length nchans, which is sampled at regular intervals (fsamp). Additional information that are system specific such as channel names for EEG/MEG, or calibration values (in case the EEG/MEG data type is int16 or int32) are not represented in the fixed part of the header. In order to transmit this type of extended header information, one needs to use the backwards-compatible extension of _chunks_ (see at the bottom of this page).

For this request, the buffer server will only return a fixed 8-byte message consisting of the already known `version`;`command`;`bufsize` triple. If the request was successful, the returned `command` will have the value 0x104 for PUT_OK. Otherwise, for example if the server could not allocate the required memory, `command` will contain the value 0x105 (=261) for PUT_ERR. Since there is no additional information attached to the response, `bufsize` should be 0. Every other response means that a communication error occurred and should be treated as such.

#### Example

Suppose you want to write header information that corresponds to a NIFTI-1 file for transmitting fMRI scans. For this you could pick the dedicated NIFTI-1 chunk type (FT_CHUNK_NIFTI1=5), the length of which is always 348 bytes. Lets assume the data are given as 16-bit integers (DATATYPE_INT16=6), the sampling frequency is 0.5 Hz (for a repetition time of 2 sec.) and that your volumes contain 64x64x20 = 81920 voxels. The complete request would then look like this

| message definition (request)                | fixed header definition                                                              | NIFTI-1 chunk                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------ |
| `version`=1, `command`=0x101, `bufsize`=380 | `nchans`=81920, `nsamples`=0, `nevents`=0, `fsamp`=0.5, `data_type`=6, `bufsize`=356 | `type`=5, `size`=348, NIFTI-1 header (348 bytes) |

Note that for every additional chunk, you need to increase the `bufsize` field of both the message definition and the header definition by the size of the chunk (including the 8 bytes for its `type` and `size` field).

### GET_HDR: Get header information from the buffer

This request is the opposite of PUT_HDR and uses the same data structures. Its command number is 0x201 (=513). The client just sends the 8-byte triple

| message definition (request)              |
| ----------------------------------------- |
| `version`=1, `command`=0x201, `bufsize`=0 |

and on success will receive the fixed message definition with `command` containing 0x204 (=516) for GET_OK, followed by the fixed header definition structure and optional chunks. The client should determine whether chunks are present by looking at the `bufsize` fields. In contrast to the PUT_HDR request, the returned header definition structure will contain the actual number of samples and events that have been written to the buffer so far.

If an error occurs, or no header information has been written yet, the buffer server will only return the 8-byte triplet `version`;`command`;`bufsize`, with the `command` value set to 0x205 (=517) for GET_ERR, and `bufsize`=0 to indicate no extra message payload.

### PUT_DAT: Append data (=samples) to the buffer

This request is used for storing samples in the buffer by `appending` them to those already present. Clients need to transmit a fixed structure followed by the actual data samples, where samples (= one value each from multiple channels) need to be transmitted contiguously. The `command` number of this request is 0x102 (=258 in decimal notation).

The fixed part (16 bytes) consists of the following (`datadef_t` in "message.h")

| field       | type   | description                                                             |
| ----------- | ------ | ----------------------------------------------------------------------- |
| `nchans`    | uint32 | number of channels                                                      |
| `nsamples`  | uint32 | number of samples                                                       |
| `data_type` | uint32 | type of the samples                                                     |
| `bufsize`   | uint32 | number of remaining bytes in the message, i.e. size of the data samples |

The response will be the 8-byte triple `version=1`,`command`,`bufsize=0`. On success, `command` will contain 0x104 (=260) for PUT_OK. In case of an error, for example if the `data_type` or `nchans` fields do not match the values previously written together with the header information, or if no header information has been written at all so far, `command` will contain 0x105 (=261) for PUT_ERR. Again, every other response should be treated as a communication error.

#### Example

Suppose you want to append 200 samples from 32 channels of single precision data. In this case, the `data_type` field contains the value 9 (DATATYPE_FLOAT32 in "message.h"), and the size of all samples is 200\*32\*4 = 25600 bytes. The complete request would look like this:

| message definition (request)                  | fixed data definition                                       | data samples                                       |
| --------------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------- |
| `version`=1, `command`=0x102, `bufsize`=25616 | `nchans`=32, `nsamples`=200, `data_type`=9, `bufsize`=25600 | sample 0 [channel 0-31], sample 1, ..., sample 199 |

### GET_DAT: Retrieve data (=samples) from the buffer

This request is used for retrieving data samples from the buffer and comes in two flavours. The first variant just asks for `all` samples that are currently present in the buffer (note that this does not necessarily correspond to all samples that have been written so far, since old samples might have fallen out of the internally used ring buffer already). For this, the client just sends 8 bytes like the following:

| message definition (request)              |
| ----------------------------------------- |
| `version`=1, `command`=0x202, `bufsize`=0 |

The client can also request a specific interval of samples by transmitting 2 indices as unsigned 32-bit integers (see `datasel_t` in "message.h"). For example, to retrieve samples with index 4 up to (and including) 15, you would send

| message definition (request)              | data selection                |
| ----------------------------------------- | ----------------------------- |
| `version`=1, `command`=0x202, `bufsize`=8 | `begsample=4`, `endsample=15` |

Note that changed `bufsize` reflects the extra message payload, and that indices are zero-offset. That is, the first sample ever written has the number 0, and the request above thus asks for 12 samples, starting with the 5th!

On success, the server will respond by the fixed message definition and the fixed data definition structures, followed by the actual data samples. Assuming 32 channel single precision data again, you would get:

| message definition (response)                         | fixed data definition                                     | data samples                                      |
| ----------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------- |
| `version`=1, `command`=0x204 (GET_OK), `bufsize`=1552 | `nchans`=32, `nsamples`=12, `data_type`=9, `bufsize`=1536 | sample 4 [channel 0-31], sample 5, ..., sample 12 |

If `begsample` and `endsample` have not been specified with the request, the response has the same form, and it will be hard to determine which samples the server actually returned.

If an error occurs, for example if the requested indices are outside of the range that is currently present in the ring buffer, the server responds with the triple `version`=1;`command`;`bufsize`=0, where `command`=0x205 (=517) for GET_ERR.

### PUT_EVT: Put events into the buffer

Using this request, clients can store events (in a ringbuffer similar to that used for the data samples). The `command` number of this request is 0x103 (=259). As for the PUT_DAT request, you can only `append` events, and at some point old events will fall out of the ring buffer. Every event is described by a fixed structure followed by a variable-length field that contains the event's _type_ and _value_.

The fixed part (32 bytes) consists of the following fields (`eventdef_t` in "message.h"):

| field         | type   | description                                      |
| ------------- | ------ | ------------------------------------------------ |
| `type_type`   | uint32 | data type of event _type_ field                  |
| `type_numel`  | uint32 | number of elements in event _type_ field         |
| `value_type`  | uint32 | data type of event _value_ field                 |
| `value_numel` | uint32 | number of elements in event _value_ field        |
| `sample`      | int32  | index of sample this event relates to            |
| `offset`      | int32  | offset of event w.r.t. sample (time)             |
| `duration`    | int32  | duration of the event                            |
| `bufsize`     | uint32 | number of remaining bytes (for _type_ + _value_) |

After the fixed part, you need to first transmit the _type_ in the form specified by `type_type` and `type_numel`, and after that the _value_ of this event. Multiple events can be transmitted one after another. Please note that the `bufsize` field above should always contain `type_numel` times the size per _type_ element plus the same product for the _value_ field.

The response of the buffer server will be the usual triple `version`=1,`command`,`bufsize`=0, with `command` equal to 0x104 (=260 / PUT_OK) on success, or 0x105 (=261 / PUT_ERR) in case an error occurred.

#### Example

Suppose you want to add two events that relate to sample 10 and 12, respectively, whose _type_ is the string "Button" and whose value is "Left" and "Right". We'll use `offset`=`duration`=0, and since both _type_ and _value_ are given as strings, the `type_type` and `value_type` fields both have the value 0 (for DATATYPE_CHAR, see "message.h"). The `type_numel` and `value_numel` fields contain the lengths of the respective strings, and since a character only takes one byte, the `bufsize` field is
the sum of both string lengths. All in all, the complete request for this would be:

| field                        | content       | class   | value  |
| ---------------------------- | ------------- | ------- | ------ |
| message definition (request) | `version`     | uint16  | 1      |
| :::                          | `command`     | uint16  | 0x103  |
| :::                          | `bufsize`     | uint32  | 85     |
| event 1 fixed part           | `type_type`   | uint32  | 0      |
| :::                          | `type_numel`  | uint32  | 6      |
| :::                          | `value_type`  | uint32  | 0      |
| :::                          | `value_numel` | uint32  | 4      |
| :::                          | `sample`      | int32   | 10     |
| :::                          | `offset`      | int32   | 0      |
| :::                          | `duration`    | int32   | 0      |
| :::                          | `bufsize`     | uint32  | 10     |
| event 1 variable part        | _type_        | char[6] | Button |
| :::                          | _value_       | char[4] | Left   |
| event 2 fixed part           | `type_type`   | uint32  | 0      |
| :::                          | `type_numel`  | uint32  | 6      |
| :::                          | `value_type`  | uint32  | 0      |
| :::                          | `value_numel` | uint32  | 4      |
| :::                          | `sample`      | int32   | 12     |
| :::                          | `offset`      | int32   | 0      |
| :::                          | `duration`    | int32   | 0      |
| :::                          | `bufsize`     | uint32  | 11     |
| event 2 variable part        | _type_        | char[6] | Button |
| :::                          | _value_       | char[5] | Right  |

### GET_EVT: Retrieve events from the buffer

This request is used for retrieving events from the buffer. Similarly to GET_DAT, it comes in two flavours. The first variant asks for `all` events that are currently present in the buffer, and is composed of an 8-byte triple as follows:

| message definition (request)                        |
| --------------------------------------------------- |
| `version`=1, `command`=0x203 (GET_EVT), `bufsize`=0 |

The client can also request a specific interval of events by transmitting 2 indices as unsigned 32-bit integers (see `eventsel_t` in "message.h"). For example, to retrieve samples with index 8 up to (and including) 10, you would send:

| message definition (request)              | event selection             |
| ----------------------------------------- | --------------------------- |
| `version`=1, `command`=0x203, `bufsize`=8 | `begevent=8`, `endevent=10` |

Note that the changed `bufsize` reflects the extra message payload, and that indices are zero-offset. That is, the first event ever written has the number 0, and the request above thus asks for 3 events, starting with the 9th!

On success, the server will respond by the fixed message definition followed by the actual events in the same format as for PUT_EVT. The only difference to PUT_EVT is indeed that on success, the returned `command` value has the code 0x204 (GET_OK). If an error occurs, the server does not transmit any events and just responds with the triple `version`=1;`command`;`bufsize`=0, where `command`=0x205 (=517) for GET_ERR.

### FLUSH_DAT: Remove all samples from the buffer

Using this request, the client can ask to remove all data from the buffer. All events and the header information are kept, although of course the `nsamples` field of the fixed header structure will be reset to 0.

The client sends the following 8 bytes:

| message definition (request)                          |
| ----------------------------------------------------- |
| `version`=1, `command`=0x302 (FLUSH_DAT), `bufsize`=0 |

and on success the server responds with:

| message definition (response)                        |
| ---------------------------------------------------- |
| `version`=1, `command`=0x304 (FLUSH_OK), `bufsize`=0 |

### FLUSH_EVT: Remove all events from the buffer

This request is for removing all events from the buffer. All data samples and the header information are kept, although of course the `nevents` field of the fixed header structure will be reset to 0.

The client sends the following 8 bytes:

| message definition (request)                          |
| ----------------------------------------------------- |
| `version`=1, `command`=0x303 (FLUSH_EVT), `bufsize`=0 |

and on success the server responds with:

| message definition (response)                        |
| ---------------------------------------------------- |
| `version`=1, `command`=0x304 (FLUSH_OK), `bufsize`=0 |

### FLUSH_HDR: Clear the buffer (header + samples + events)

This request is for clearing `all` contents of the buffer, including samples, events, and any chunks present in the header.

The client sends the following 8 bytes:

| message definition (request)                          |
| ----------------------------------------------------- |
| `version`=1, `command`=0x301 (FLUSH_HDR), `bufsize`=0 |

and the server responds with:

| message definition (response)                        |
| ---------------------------------------------------- |
| `version`=1, `command`=0x304 (FLUSH_OK), `bufsize`=0 |

### WAIT_DAT: Wait for samples and/or events

This request is intended to be used in a realtime processing loop to poll for newly arrived samples or events.
The client sends a fixed message consisting of:

| message definition (request)                         | threshold definition                    | timeout            |
| ---------------------------------------------------- | --------------------------------------- | ------------------ |
| `version`=1, `command`=0x402 (WAIT_DAT), `bufsize`=0 | `nsamples` (uint32), `nevents` (uint32) | `timeout` (uint32) |

where `timeout` is given in milliseconds. The server will respond only after either:

- the sample count of the buffer is `higher` than `nsamples`, or
- the event count of the buffer is `higher` than `nevents`, or
- `more` than `timeout` milliseconds have passed since the receipt of the request.

Then, the response consists of the fixed sequence:

| message definition (response)                       | current quantities                      |
| --------------------------------------------------- | --------------------------------------- |
| `version`=1, `command`=0x404 (WAIT_OK), `bufsize`=8 | `nsamples` (uint32), `nevents` (uint32) |

where `nsamples` and `nevents` contain the sample and event count of the buffer at the time the response is sent. Note that depending on timeout conditions, either or both of these quantities can be below the given threshold.

If no header information is present in the buffer, the server replies immediately with the triple:

| message definition (response)                        |
| ---------------------------------------------------- |
| `version`=1, `command`=0x405 (WAIT_ERR), `bufsize`=0 |

#### Examples / remarks

This request can also be used as a light-weight GET_HDR replacement where no chunks (see below) are transmitted. Just set `timeout`=0 and the server will respond with the `nsamples` and `nevents` quantities immediately.

If you only want to wait for new events, and do not care about data samples (yet), you can set the `nsamples` field in the request to a very high number (2^32-1 as the biggest uint32). The same works for the opposite case where you're interested in samples, not events.

### Chunks for transmitting extended header information

As already mentioned, the PUT_HDR request can contain a variable part consisting of _chunks_. These are transmitted one after another (`chunk_t` in "message.h"). Their structure is:

| field  | type   | description                                                      |
| ------ | ------ | ---------------------------------------------------------------- |
| `type` | uint32 | type of this chunk (see chunk documentation)                     |
| `size` | uint32 | size of this chunk in bytes (excluding the type and size fields) |
| `data` | var.   | contents of this chunk                                           |

The chunk type and the content of the chunk are system specific. If the client application does not recognize the chunk type, it can skip over it.

If chunks are present, they will be transmitted in every GET_HDR request, using the same format. Care must be taken to adapt the processing logic of the client in case the header contains a large chunk (such as a ~3MB big CTF ".res4" file), that is, the GET_HDR request should be made only as often as necessary, and replaced by WAIT_DAT.

The following is a list of currently defined and used chunk types.

#### Unspecified / site-specific binary blob

This chunk can represent unspecified binary data, which can for example be used during development of site-specific protocols. The buffer server will make no attempt to interpret the contents.

| field  | contents                 |
| ------ | ------------------------ |
| `type` | FT_CHUNK_UNSPECIFIED = 0 |
| `size` | arbitrary length (L)     |
| `data` | L bytes (uint8)          |

#### Channel names

This chunk is used for labelling the channels (or elements of the feature vector) that are represented in the buffer. The form of the representation is inspired by the BrainProducts RDA protocol.

| field  | contents                                                                    |
| ------ | --------------------------------------------------------------------------- |
| `type` | FT_CHUNK_CHANNEL_NAMES = 1                                                  |
| `size` | sum of length of name strings, including terminating zeros for each channel |
| `data` | a list of 0-terminated strings, one for each channel                        |

#### Channel flags

This chunk is useful for specifying that a channel can have one of a discrete number of different types, e.g., `data` = "meg_ad_eog\0\1\1\1\1\3\3\2\2" could be used for a system with 8 channels, the first four of which are for MEG, then 2 channels EOG, then 2 channels A/D.

This chunk is used for labelling the channels (or elements of the feature vector) that are represented in the buffer.

| field  | contents                                                                                                        |
| ------ | --------------------------------------------------------------------------------------------------------------- |
| `type` | FT_CHUNK_CHANNEL_FLAGS = 2                                                                                      |
| `size` | length of flag description string (including terminating 0) plus one byte per channel                           |
| `data` | a 0-terminated string describing the type of flags, and after that N (=#channels) bytes describing each channel |

#### Channel resolutions

This chunk is also inspired by the BrainProducts RDA protocol, and describes the mapping from A/D values to physical quantities such as micro-Volts in EEG.

| field  | contents                                |
| ------ | --------------------------------------- |
| `type` | FT_CHUNK_RESOLUTIONS = 3                |
| `size` | 8 bytes times number of channels        |
| `data` | one double precision values per channel |

#### ASCII format key/value pairs

This contains an arbitrary number of key/value pairs, each of which is given as a 0-terminated string. An empty key (=double 0) indicates the end of the list. For example: "amplifier_gain\0high\0noise_reduction\0active\0\0".

Not used so far.

| field  | contents                                                       |
| ------ | -------------------------------------------------------------- |
| `type` | FT_CHUNK_ASCII_KEYVAL = 4                                      |
| `size` | total length of key/value strings, including terminating zeros |
| `data` | list of 0-terminated strings (key,value,key,value,...)         |

#### NIFTI-1 header

Used for transporting a NIFTI-1 header structure for specifying fMRI data.

| field  | contents                      |
| ------ | ----------------------------- |
| `type` | FT_CHUNK_NIFTI1 = 5           |
| `size` | 348                           |
| `data` | NIFTI-1 header in binary form |

#### Siemens MR sequence protocol (ASCII)

Used for transporting the sequence protocol used in Siemens MR scanners (VB17). This is also part of the DICOM header (private tag 0029:0120) that these scanners write.

| field  | contents                      |
| ------ | ----------------------------- |
| `type` | FT_CHUNK_SIEMENS_AP = 6       |
| `size` | length of the protocol string |
| `data` | protocol string               |

#### CTF MEG system .res4 file

This chunk contains a .res4 file as written by the CTF MEG acquisition software in its normal binary (big-endian!) format.

| field  | contents                   |
| ------ | -------------------------- |
| `type` | FT_CHUNK_CTF_RES4 = 7      |
| `size` | size of the .res4 file     |
| `data` | contents of the .res4 file |

#### Neuromag/Elekta/Megin MEG system .fif file

These chunks contain .fif files as written by the neuromag2ft realtime interface. The header file is in its native platform (little-endian!) format, the isotrak and hpi_result files are in big-endian format.

| field  | contents                     |
| ------ | ---------------------------- |
| `type` | FT_CHUNK_NEUROMAG_HEADER = 8 |
| `size` | size of the .fif file        |
| `data` | contents of the .fif file    |

| field  | contents                      |
| ------ | ----------------------------- |
| `type` | FT_CHUNK_NEUROMAG_ISOTRAK = 9 |
| `size` | size of the .fif file         |
| `data` | contents of the .fif file     |

| field  | contents                         |
| ------ | -------------------------------- |
| `type` | FT_CHUNK_NEUROMAG_HPIRESULT = 10 |
| `size` | size of the .fif file            |
| `data` | contents of the .fif file        |

## See also

- [draft network](/development/realtime/draft_network)
- [draft implementation](/development/realtime/draft_implementation)
- [draft header chunks](/development/realtime/draft_header_chunks)
- [draft compatibility](/development/realtime/draft_compatability)
- [scratchpad](/development/realtime/scratchpad)
