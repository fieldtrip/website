---
title: FieldTrip buffer C implementation
layout: default
tags: [realtime, development]
---

## FieldTrip buffer C implementation

The best example for integrating the FieldTrip buffer in your own application is in the ''demo_sinewave'' and the ''demo_combined'' command-line applications. They implement a sinewave signal generator that writes its data to the buffer. The ''demo_sinewave'' has to be used in combination with the ''buffer'' application, whereas ''demo_combined'' contains both. Subsequently another application (e.g. implemented in MATLAB) can read from the buffer.

If you want to implement the buffer in your own application, you should consider whether your application should maintain the buffer itself, or whether your application would be writing to a buffer that is maintained by another application.

![image](/media/development/realtime/screen_shot_2018-03-28_at_14.14.39.png@600)

The best way to get started with incorporating the FieldTrip buffer in your own software project, is by looking at the example applications in the buffer/test directory. It contains a number of examples

*  ''buffer'' implements a standalone buffer (middle box in the figure above)

*  ''demo_sinewave'' implements a standalone data acquisition client (left box in the figure above)

*  ''demo_combined'' implements both the buffer and the data acquisition in a single executable (left+middle box)

*  ''demo_event'' writes events to the buffer, c.f. demo_sinewave which writes only data

### The buffer will be attached to your local application

Your application is responsible for starting up the tcpserver. The tcpserver is a multithreaded function, which will spawn a seperate tcpsocket thread for every incoming connection. The tcpsocket thread reads a request from the network, processes the request, and returns a response. Possible requests that the buffer can process are PUT_HDR, PUT_DAT, PUT_EVT, GET_HRD, GET_DAT, GET_EVT, FLUSH_HDR, FLUSH_DAT, FLUSH_EVT. The tcpserver is instantiated using the following pseudo-cod

    ... start the multithreading...
    tcpserver((void *)(&host));

or alternatively you can start the tcpserver in its own thread like this

    ... start the multithreading...
    pthread_create(&tid, &attr, tcpserver, (void *)(&host));

A real example for starting the tcpserver can be found in the code in buffer/test/demo_buffer.c (only the buffer) or in buffer/test/demo_combined.c (which starts the tcpserver and subsequently writes simulated data to it). 

After starting the tcpserver, your application can start writing to the buffer. The writing to the buffer should be done like in this pseudo cod

    ... construct a PUT_HDR request ...
    connection = open_connection(hostname, port);
    status = clientrequest(connection, request, &response);
    close_connection(connection);
    
    while (newdata)
    ... construct a PUT_DAT request ...
    connection = open_connection(hostname, port);
    status = clientrequest(connection, request, &response);
    close_connection(connection);
    end

In the example above, the network transparent communication is kept stateless. It is also possible to keep the connection open for multiple subsequent requests, like thi

    connection = open_connection(hostname, port);
    ... construct a PUT_HDR request ...
    status = clientrequest(connection, request, &response);
    
    while (newdata)
    ... construct a PUT_DAT request ...
    status = clientrequest(connection, request, &response);
    end
    close_connection(connection);

### The buffer is attached to a remote application

If your want your application only to write to a remote buffer, you can use the following pseudo cod

    connection = open_connection(hostname, port);
    ... construct a PUT_HDR request ...
    status = clientrequest(connection, request, &response);
    
    while (newdata)
    ... construct a PUT_DAT request ...
    status = clientrequest(connection, request, &response);
    end
    close_connection(connection);

Depending on how the host is specified, the open_connection function will open a network socket (remote buffer) or will do nothing (local buffer). The clientrequest function will automatically determine whether it should write to a remote or to a local buffer, and it will call tcprequest or dmarequest (dma = direct memory access) respectively. 

The dmarequest function always deals with the low-level memory management. If you want to keep all multithreaded code out of your application, which is only possible if you write to a remote buffer, then you can use the tcprequest function instead of the clientrequest function. The only c-functions that require multithreading are tcpserver which start a thread for every incoming connection, and dmarequest which uses a mutex to ensure that multiple memcopy requests are not interfering.

