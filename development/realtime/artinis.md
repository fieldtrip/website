---
title: Streaming realtime data from Artinis Medical Systems
tags: [realtime, artinis]
---

## Introduction

Artinis Medical Systems is a Dutch company manufacturing wired and wireless NIRS devices for clinical and research purposes. Artinis is an independent manufacturer, allowing them to design NIRS products for specific customer purposes. Their multichannel NIRS devices are highly modular, allowing cumulative upgrading.

{% include image src="/assets/img/development/realtime/artinis/Single_Oxymon.png" %}

## Interface with FieldTrip

Artinis has developed their own software Oxysoft for data collection and viewing, storage and analysis. Oxysoft features the ability to stream data directly to the FieldTrip buffer, which needs to be enable in the PortaSoft.ini located in ".../Public Documents/Artinis Medical Systems BV/common". you have to manually add these lines

    [FieldTrip]
    Enable = 1
    StartServer = 1

Oxysoft assumes the default buffer port to be 1972. Oxysoft will start an own shared memory segment that data will be buffered to.

Once configured, you can read the streamed data from MATLAB, e.g., with FieldTrip

    ft_read_header(filename)
    ft_read_data(filename, ...)
    ft_read_event(filename, ...)

where you specify `filename='buffer://hostname:port'` as the location to read the data from, where hostname refers to the IP-address or hostname of the computer that runs Oxysoft (can be 'localhost'). Additional information can be requested via the helpdesk by mailing to askforinfo@artinis.com
