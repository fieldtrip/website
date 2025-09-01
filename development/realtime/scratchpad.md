---
title: Scratchpad for the realtime buffer interface
tags: [realtime, development]
---

This page contains some loose ends and random pieces that don't fit elsewhere.

- [closing the loop](/development/realtime/closing_the_loop) lists some methods for interacting with, and controlling the external world (i.e. outside the analysis computer)
- [pipeline](/development/realtime/pipeline) contains example fMRI pipeline description
- [Siemens fMRI](/getting_started/realtime/fmri) also contains some fMRI details

## Various notes and comments

Portability note: non-unix systems may not allow read()/write() on
sockets, but recv()/send() are usually ok. This is true on Windows and
OS/2, for example.

On a 32-bits Linux/RHEL4 machine (mentat068) I got the following error
"libgcc_s.so.1 must be installed for pthread_cancel to work"
Searching the internet did not give much helpful suggestions, but using
strace did help. It turned out that there was a version of libgcc_s on
the LD_LIBRARY_PATH that was loaded prior to the system one. Changing
it to first having /lib and then the rest solved it.

The following macro names are defined at compile time and may be handy for debuggin
**LINE** Integer value representing the current line in the source code file being compiled.
**FILE** A string literal containing the presumed name of the source file being compiled.
**DATE** A string literal in the form "Mmm dd yyyy" containing the date in which the compilation process began.
**TIME** A string literal in the form "hh:mm:ss" containing the time at which the compilation process began.
\_\_cplusplus An integer value. All C++ compilers have this constant defined to some value. If the compiler is fully
compliant with the C++ standard its value is equal or greater than 199711L depending on the version
of the standard they comply.

The threaded functions should be checked with https://en.wikipedia.org/wiki/Reentrant in mind

## Suggestions for improvement

### Connection

The suggested solution with different string results in letting the
open_connection function guess (=parsing the string) which kind of connection
is wanted. It is better to define a parameter which states which kind of
connection is wanted, and then the string which must be used to open that
connection. Another omission from the draft protocol is an outline of the
commutation sequence. How is a connection initiated? Is a handshake required?
Is authentication required?

Missing from the draft protocol is a explicit description of the transport
mechanism: apparently it is based on TCP/IP over Ethernet. An explicit
description of the transport mechanism of the packets would be helpful,
including a discussion of the consequences of the physical transport layer
(e..g 100Mbps, 1Gbps, 10Gbps, wifi) on the timing aspects of the buffer.
Furthermore, the implementation is based on IPv4, what would be required to
extend this to IPv6? Useful would be a discussion in which the different
choices of the transport layer are discussed. Why not UDP over ethernet? Why
not over communicate over RS-232 (serial), IEE-1394 (firewire), IEEE-802
(zigbee), X10, Bluetooth, or similar communication protocol.

It is unclear whether the TCP connection should remain open throughout the
communication or whether it should be closed. It is just a mechanism for
networked data exchange between processes running on different computers. It
could be more compared to HTTP (see
http://www.w3.org/Protocols/rfc2616/rfc2616.html). Some additional "meta" data
can be transferred (with limitations).

### Priorities of the buffer server

You should describe how you deal with the data in the buffer: is it stored on a
hard drive or only in RAM? What happens, if the data rate is too high? What has
priority: reading or writing the data? Is there a notion of fairness in server
clients (against starvation)? Are there any guarantees for timeliness of
responses?

An omission in the definition of the buffer is that it is not specified how
much old data is to be maintained in RAM, nor is it possible to have clients
influence that parameter.

In the reference implementation the data is stored in RAM. In case it were
implemented on an embedded device, I could also imagine a two-tier storage
(with the most recent data in RAM, slightly older data on SSD, and even older
data getting dropped). Your question should be addressed in the documentation,
and it should be clarified that it is a (large) ring-buffer.

### Header

A PUT_HDR reinitializes the buffer, similar to a FLUSH_HDR, FLUSH_DAT. Should be documented.

What is referred to as the "header" in the FieldTrip buffer can be thought of
as all the fixed meta data. What is referred to as "events" in the fieldtrip
buffer is can be thought of as time-varying meta-data. What remains is the
data, which is the representation of a physical property that was measured (or
computed from a measurement). But for example representing the volumetric data
as separate slices does not fit well in the design. Different DICOM headers per
slice does not fit. DICOM headers that change over time do not fit.

Het is aan de client om te controleren dat het aantal kanalen niet klopt na een PUT_HDR.

### Chunks

Only by looking in the message.h you get an idea what kind of chuck are already
developed. Chunks are arbitrary binary blobs that can be stored on the server
and hence be exchanged between one (acquisition) client and another (analysis)
client without the server requiring any understanding of the blobs.

What are the chunk requirements? Does the extension of the protocol with
another chunk require recompilation of the server? What are the chunk
requirements? How should clients know how to interpret a chunk. How are chunk
identified? How is chunk identity standardized between labs? Is it possible to
store two chunks at the same time, and if so, how are they transmitted in a put
and in a get request?

The chunks seem a logical extension of the header structure, as such it seems
more logical to extend the GET and PUT commands with a GET_CHUNK and PUT_CHUNK,
where the respective packet would contain the chunk type and length. Predefined
chunks (such as Siemens, NIfTI and CTF res4) can remain as they are, but would
not be sent along with each GET_HDR. This removes the requirement to switch
from the polling to the blocking-read operation as implemented with WAIT_DAT.
See also the light-header proposal.

It would be nice to mention a list of some available chunks. For
example, the gradiometer positions are not mentioned in that page.

### Timestamps

We are missing discussion on multi-platform (Windows+Linux+macOS) issues, due to
different resolutions available on each platform
(http://msdn.microsoft.com/en-us/library/ms724397). In the situation where
application and FieldTrip server are located on different PC's, how is the time
(roughly) synchronized? One solution could be to configure the NTP client on
each PC to use the same (external) NTP server. In particular situations time
information will certainly be useful. Regarding acquisition devices it remains
difficult how to interpret the relation between buffer time and samples
received.
Why is time relevant? Probably to synchronize _events and samples_, or
simultaneous recordings?

> You should timestamp every event and data, but I would not use machine
> specific timing, but a global time. Otherwise it will be difficult to combine
> different modalities. Maybe you have two time stamp fields: one for the
> machine generating the data and one where the FieldTrip buffer is running.

We introduced the timestamp field, but sofar have not started using it. The
time synchronisation of different computers is challenging. At the moment the
data is implicitly timestamped by the sample number that depends on the
acquisition computer. Events are presently timestamped using the sample number
that relates the event to the acquired data. This time stamping is not
explicitly addressed in the documentation.

It would be possible to (optionally) add an explicit timestamp channel in the continuous data stream. Ideally a timestamp would be assigned to every sample by the acquisition software. If the acquisition software does not assign timestamps, the buffer server could do it for the incoming data and for the incoming events.

### Atomic PUT_DAT + PUT_EVT

Because TMSi frontend continuously samples all the channels, including the
event channels, we suggest that an atomic put_dat and put_evt be made, in which
in one call all data received from the frontend is stored in the FieldTrip
buffer.

The proposed sequence of always first write events and then samples makes sense
and should be preferred in non-atomic implementation, although something can be
said to the approach of driving people into a guaranteed safe solution by
combining both PUT_DAT and PUT_EVT operations.

Viewed from an online perspective, polling of events can already be achieved
based on the nevents field returned by the header and assuming fifo behavior.
In the offline case, adding index information to the events is useful since it
reflects the incoming following order of events, which may differ from the
ordering based on the sample field.

### Homogeneous sample rate

The assumption here is that all channels have the same sampling frequency. TMSi
has frontends where each channel can have a different sample rate. However, the
samples of these channels are upscaled to the sample frequency of the fastest
channel. Options to set the desired size of the buffers for both samples and
events can be useful in case requesting events from far history or in case many
events occur in a relatively short time interval. Also, prior information about
the buffer sizes seems not available. This would be useful since in the current
version such change is reflected in a sudden decrease in the number of samples.

### Versions and compatibility

If the server needs to support all different versions of the protocol, the
maintenance effort increases significantly. We suggest that server supports
only the most recently released version of the protocol. Draft V2 mentions how
to deal with a client and a server application that speak different implement
of the protocol, but that description is rather limited. Is there a fallback
mechanism in place to drop back to the highest common denominator as in RFB?
Should backward compatibility be defined at the level of the protocol, or
should it (optionally) be part of the reference implementation? Is this a
requirement of the protocol? Although all available implementations for the
various acquisition systems have been made based on the reference
implementation, the protocol should outline the minimum requirements and the
limitations that are imposed on any implementation.

A certification procedure should be considered, according to which a particular
implementation can be certified as adhering to a particular version of the
protocol. The reference implementation should contain an independent mechanism
for verifying the compliance with particular versions of the protocol.

### Doc and site

It is not clear from the page, how to call the functions in practice. For
instance, if I want to use GET_HDR, what should I do? There should be some
examples of different functions with some specified parameters as a guideline
to be used.

Er moet een centrale tabel moeten hebben met alle constanten. Chunk information is hardly available. De pagina buffer_protocol zou alleen volgens mij alleen
constanten moeten hebben die niet specifiek zijn voor de referentie
implementatie.

#### FAQ

FAQ: Combining modalities: Furthermore, they might require different numeric
representations. Experimental settings that require this should use two buffers
for the raw data and a single piece of real-time analysis software that reads
from both and integrates the two (if desired). Writing two modalities into one
buffer representation (e.g., fMRI and simultaneous EEG) is not supported. In
general it is unlikely that the two modalities have the same sampling rate and
are synchronized.

FAQ: The documentation should indeed make better clear that the data is not
necessarily EEG or MEG channels, but that any set of N measurements of a
physical parameter that pertains to the brain (be it EEG/MEG channels, optodes
or voxels) that is sampled with a fixed dT between subsequent samples can be
represented. Of course also a difference is that the sampling rate is rather
different (about once per millisecond versus once per second), but that does not
affect the core representation of the data.

FAQ: Does the extension of the protocol with another chunk require
recompilation of the server?

FAQ: Buffer for volumetric data: The conceptual switch from EEG channel level
data to volumetric data is to consider that (in BCI terminology) a feature
vector is being sampled at a regular interval. The feature (or data vector) for
MEG is 275x1 for the channels which have a spatial 3D location, the feature
vector for MRI is for example (64*64*32)x1 which is 1x131072 values that also
have a 3D location. The location of the MRI voxel-level data vector can be
mapped directly back on the volume by reshaping the vector for a single
time point into a 64x64x32 array. A limitation that this touches upon (and that
we should document) is that the data vector can not have a different length for
different sample points.

FAQ: "Can I use the buffer to transfer XXX data over the network?", where the
answer would detail for different XXX what the data is that can be transferred
and hence also what the information is that would consequently get lost in the
transfer. Given that NIfTI is much more limited in what can be represented, it
is possible to transfer NIfTI data without loss of information, whereas it is
not possible to to transfer DICOM data. It is also not possible to transfer
data from EEG and MEG systems without loss of information that in those systems
is normally represent on disk.

FAQ: How is time synchronised?

## See also

- [draft network](/development/realtime/draft_network)
- [draft implementation](/development/realtime/draft_implementation)
- [draft header chunks](/development/realtime/draft_header_chunks)
- [draft compatibility](/development/realtime/draft_compatability)
- [scratchpad](/development/realtime/scratchpad)
