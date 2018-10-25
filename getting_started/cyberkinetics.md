---
title: Getting started with Cyberkinetics data
layout: default
tags: [cyberkinetics, lfp, spike, dataformat]
---

`<note warning>`
The support for the 'cyberkinetics' format using neuroshare has never been fully operational. Moreover, the limited functionality was restricted to the Windows platform. Nowadays, this file format has been adopted by Blackrock microsystems, and cross-platform support for the file format in FieldTrip is being implemented. Please see http://www.fieldtriptoolbox.org/getting_started/blackrock and http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=2964 for more information.
`</note>`

# Getting started with Cyberkinetics data

## Introduction

To read Cyberkinetics data into FieldTrip, you will need the Neuroshare toolbox, see http://www.neuroshare.org. Neuroshare is created to support the collaborative development of open library and data file format specifications for neurophysiology and distribute open-source data handling software tools for neuroscientists.

You will need to download the "Matlab Import Filter" and the Cyberkinetics library files. Currently this will run on WINDOWS platforms only. Make sure all the Neuroshare files are available on the Matlab path.

The low-level FieldTrip reading function that is used to read Cyberkinetics dat
fieldtrip/fileio/private/read_neuroshare.m

To get started, you should add the FieldTrip main directory to your path, and execute the **[ft_defaults](/reference/ft_defaults)** function, which sets the defaults and configures up the minimal required path settings (see the [faq](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path)

	
	addpath `<full_path_to_fieldtrip>`
	ft_defaults

## Reading header information

To read header information, us

	
	filename = 'your_cyberkinetics_file.nev';
	
	hdr = ft_read_header(filename, 'headerformat', 'neuroshare');

This calls the neuroshare toolbox and gives back the header structure in FieldTrip format, which includes the original header information (included as hdr.orig) as retrieved with the neuroshare functions *ns_GetXXXInfo*.

## Reading triggers and other events

To read events, us

	
	filename = 'your_cyberkinetics_file.nev';
	
	event = ft_read_event(filename, 'eventformat', 'neuroshare');

This calls the neuroshare toolbox (using the functions *ns_GetEventData* and *ns_GetIndexByTime*) and gives back the event structure in FieldTrip format.

## Reading LFP data

To read analog data, us

	
	filename = 'your_cyberkinetics_file.nev';
	
	data = ft_read_data(filename, 'headerformat', 'neuroshare', 'dataformat', 'neuroshare');

This calls the neuroshare toolbox (using the function *ns_GetAnalogData*) and gives back the data structure in FieldTrip format.

Optional input arguments should be specified in key-value pairs and may includ

	
	%   'chanindx'   = list with channel indices to read
	%   'begsample   = first sample to read
	%   'endsample   = last sample to read

## Reading spike data

To read spike data, us

	
	filename = 'your_cyberkinetics_file.nev';
	
	spike = ft_read_spike(filename, 'spikeformat', 'neuroshare');

This calls the neuroshare toolbox (using the functions *ns_GetSegmentData* or *ns_GetNeuralData*) and gives back the spike structure in FieldTrip format.

## External links

*  [http://neuroshare.org](http://neuroshare.org)

*  http://www.blackrockmicro.com  Blackrock Microsystems (formerly the Research Products Division of Cyberkinetics Inc.)
