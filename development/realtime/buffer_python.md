---
title: FieldTrip buffer Python interface
tags: [realtime, development]
---

# FieldTrip buffer Python interface

## Client side pure Python implementation

The directory "fieldtrip/realtime/src/buffer/python" contains a single-file Python module called "FieldTrip.py". This provides classes that wrap FieldTrip-style header structures, events, and client connections to a server, including functions for the various requests to read and write samples and events. The module depends on [Numpy](http://numpy.scipy.org) for representing data matrices and type and value fields of events.

The following Python code example demonstrates how to use the interfac

```python
    import sys
    import FieldTrip

    ftc = FieldTrip.Client()
    ftc.connect('localhost', 1972)    # might throw IOError
    H = ftc.getHeader()
    if H is Non
      print 'Failed to retrieve header!'
      sys.exit(1)

    print H
    print H.labels

    if H.nSamples >
      print 'Trying to read last sample...'
      index = H.nSamples - 1
      D = ftc.getData([index, index])
      print D

    if H.nEvents >
      print 'Trying to read (all) events...'
      E = ftc.getEvents()
      for e in
          print e

    ftc.disconnect()
```
