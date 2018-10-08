---
layout: default
---

{{tag>realtime ant}}

# ANT NeuroSDK

## Introduction

Advanced Neuro Technologies is an Dutch company that provides EEG hardware and software for research and clinical applications. They provide complete and user-friendly EEG systems composed of well-integrated hardware and software for acquisition, analysis and stimulus presentation.

{{http://static.ant-neuro.com//content/images/amp_72ch.jpg}}

The ANT NeuroSDK allows users to develop their own neurofeedback application, as created in Html/Jscript, C++, or Matlab. The acquisition can be performed through the ASA or Cognitrace recording modules, or using a direct connection to the EEG amplifier via a dedicated ActiveX control that handles the communication with the amplifiers driver. 

## ANT acquisition software interface

The ANT NeuroSDK and the ANT acquisition software have implemented the FieldTrip buffer. This requires that you have purchased the NeuroSDK toolkit from ANT. Interfacing the ANT acquisition systems with Matlab and/or FieldTrip therefore is as simple a

    ft_read_header(filename)
    ft_read_data(filename, ...)
    ft_read_event(filename, ...)

where you specify `'buffer://hostname:port'` as the filename to the reading functions. 

## MATLAB-based interface

An alternative interface to the ANT acquisition software is implemented in the **[ft_realtime_asaproxy](/reference/ft_realtime_asaproxy)** function. This Matlab-only function reads from the NeuroSDK interface and writes to the FieldTrip buffer. Subsequently in another Matlab session you can read from the FieldTrip buffer using the **[ft_read_header](/reference/ft_read_header)**, **[ft_read_data](/reference/ft_read_data)** and **[ft_read_event](/reference/ft_read_event)** functions by specifying %%'buffer://hostname:port'%% as the filename to the reading functions. 
