---
title: Streaming realtime fMRI from Siemens scanners
category: getting_started
tags: [realtime, siemens, fmri]
redirect_from:
    - /getting_started/realtime/fmri/
---

# Streaming realtime fMRI from Siemens scanners

The present system for acquiring fMRI data in real time consists of three main blocks:

1. a stand-alone executable that runs directly on the scanner host,
2. a FieldTrip buffer running on another machine in the network, and
3. MATLAB scripts or other client applications that retrieve their data from the buffer.

Further to that, a small modification needs to be made to the applied MR sequence such that protocol information is written to a specific location. By now, all the sequences commonly used at the DCCN contain this modification.

## Design considerations

Recent Siemens software versions (VB17) include an option for realtime export of DICOM images, however it seems there is considerable jitter in the arrival of those files. Alternatively, there is an example of how to export data directly from within an ICE component. However, that piece of code would run on the imager, which is not directly connected to the outside world network. It was therefore decided to build a custom solution based on accessing files on the scanner host.

There are essentially two steps involved for using this mechanism

1. Start a FieldTrip buffer server on some machine and port number in the network, e.g., on mentat069:1972.
2. On the scanner console, start **gui_streamer** and enter "mentat069" as well as "1972" in the "hostname" and "port" input fields, then press "Connect".

If the connection could be made, the color of the input fields will switch to green. You can now start scanning and have a look at the **gui_streamer** window
to monitor the number of scans etc.

{% include image src="/assets/img/getting_started/realtime/fmri/siemens_gui_streamer.png" %}

The input fields at the bottom of the dialog window are for setting up an extra mechanism that sends a simple "RESET" message as a UDP packet to the given address, each time a new protocol is read. This is only relevant for realtime fMRI experiments and is intended to help with synchronising the experiment. Usually this would be used in conjunction with a tool that runs on the presentation machine, and that turns incoming TTL pulses (indicating the start of a new scan) into FieldTrip buffer events. Listening for "RESET" messages allows this tool to reset its internal sample counter, so that the events it sends correctly correspond to the scans that are written to the buffer from the streaming tool or the pipeline.

## Pipeline for quality assurance and online head movement monitoring

The directory "fieldtrip/realtime/online_mri" contains some functions that are useful for realtime processing of fMRI data. In the MRI lab of the FC Donders centre, we use the function **[ft_omri_quality](/reference/realtime/online_mri/ft_omri_quality)** to monitor head movement and signal quality. In order to start this, e.g., on the lab machine "lab-mri004" close to the Avanto scanner, simply click on the icon labeled "fMRI quality control". This will first fire up a FieldTrip buffer server on port 1972, and subsequently a MATLAB session that automatically runs **[ft_omri_quality](/reference/realtime/online_mri/ft_omri_quality)**. Once the buffer server has started (visible in a new terminal window), you can start the **gui_streamer** on the scanner host and connect to the address (in the Donders centre, a link in the start menu of the scanner host starts the tool with the right hostname:port combination).

Everytime you start a new sequence on the scanner, the **[ft_omri_quality](/reference/realtime/online_mri/ft_omri_quality)** script will detect this, and will use the first scan of each sequence as the template for aligning all subsequent images to. You can choose to skip any number of ("dummy") samples at the beginning by running

    cfg.numDummy = 5;
    ft_omri_quality(cfg);

Please see the documentation of **[ft_omri_quality](/reference/realtime/online_mri/ft_omri_quality)** for more options.

## Pipeline for realtime experiments

For realtime fMRI experiments (e.g., involving neurofeedback), it is sometimes easier to separate standard preprocessing steps from more specialised analysis. This can easily achieved by using two FieldTrip buffers and MATLAB for the preprocessing. We provide a script **ft_omri_pipeline** that reads unprocessed scans from one buffer, carries out motion correction and slice-time correction, and writes the resulting volumes to a second buffer, which can then be read from by another script for further analysis.

{% include image src="/assets/img/getting_started/realtime/fmri/fmri_two_buffers_small.png" width="600" %}

### Example setup

Apart from motion correction and other pre-processing steps, it is necessary to have a good handle on the timing on the experiment. In contrast to EEG or MEG data, fMRI data arrives in the buffer at a much slower rate (typically at a sampling rate of 0.5 Hz). Moreover, there is a lag of more than 1 TR between the time when the acquisition of a scan starts (marked by a TTL pulse), and the time the data is available. The former is what you need to link your stimulus presentation and analysis to, and you can do so by [turning each TTL pulse into a FieldTrip buffer event](/development/realtime/serial_event), for which you then need to poll repeatedly.

{% include image src="/assets/img/getting_started/realtime/fmri/fmri_two_buffers_events.png" width="640" %}

#### Starting the various applications

1. you should start up the FieldTrip buffer servers. In case you **do not** want to save the incoming scans and events, you can use the plain **buffer** application `/home/common/matlab/fieldtrip/realtime/bin/glnxa64/buffer`. In case you *do want to save* the data for later offline analysis or for debugging, you should use the **recording** application. In detail, open a terminal window and type `/home/common/matlab/fieldtrip/realtime/bin/glnxa64/playback path_to_raw_data 1972` where "path_to_raw_data" is the name of a new directory (will be created for you) that will receive the unprocessed scans. Then, in a second terminal, similarly type `/home/common/matlab/fieldtrip/realtime/bin/glnxa64/playback path_to_processed_data 1973` to spawn a second buffer server on another port.
2. you should start **serial_event**, the tool for translating the TTL pulses to FieldTrip events. In the DCCN MRI labs, this application is available on "D:\TTL_to_FieldTrip" on the machine "Presentation010" close to the Avanto. The configuration file "serial_event.conf" should already contain the right settings.
3. you should start the MATLAB script that does the preprocessing, e.g., **ft_omri_pipeline**. The script takes a "cfg" structure as an input argument, where you can tweak some settings, which notably includes the address of the two FieldTrip buffers. If you run the script on the same machine as the two buffer servers, the default options of "localhost:1972" and "localhost:1973" for "cfg.input" and "cfg.output" are already fine.
4. you should start **gui_streamer** on the scanner host. Make sure that the address of the buffer servers is correct (in the example above, this should be "lab-mri004" and "1972"), and that the connection is made (press "Connect", after which the address fields should be green). Also make sure that you enter the name of the presentation machine (e.g., "Presentation010") in the input field on the bottom of the **gui_streamer** dialog window, and that the port number (e.g., 1990) is the same as in the **serial_event** configuration file. Press "Enable" to send "RESET" messages at the start of each MR sequence.
5. you should now be ready to start the sequence on the scanner.

## Background information

### Mosaic files

With the current Siemens scanner software (VB17A), a new file "E:\IMAGE\xx-yyyy\zzzzzzz.PixelData" is created on the "E:\" drive of the host computer (the Windows box the scanner is operated from) immediately after each scan. This file contains pixel data as unsigned 16-bit integers, where different slices show up as tiles of a mosaic. The mosaic seems to be always square, and blank tiles are appended if the number of slices is smaller than the number of tiles in the mosaic.

Example: The MR sequence is set up to scan N=32 slices with readout resolution R=64 pixels and phase resolution P=48 pixels. In this case, the mosaic will contain 6x6 tiles with 4 empty tiles marked by "--" and slices ordered as follow

```plaintext
01  02  03  04  05  06
07  08  09  10  11  12
13  14  15  16  17  18
19  20  21  22  23  24
25  26  27  28  29  30
31  32  --  --  --  --
```

The pixel dimensions of the mosaic will be `(64*6)x(48*6)`, that is, `384x288`, and thus the total number of pixels is 110592, corresponding to a file size of 221184 bytes. Within the file, the pixels are written row after row, that is, the first 768 bytes contain the 384 pixels of the first row, corresponding to the first rows of slices 01-06, and so on.

Within the FieldTrip buffer, each scan is represented as ONE sample with RxPxN channels, with data ordering as in MATLAB, that is, the pixel data is reshaped such that slices (and their rows) are contiguous in memory, and empty tiles are dropped. For the above example, we would have `64x48x32` = 98304 "channels". The data format is kept as INT16_T.

### PixelDataGrabber

In order to react efficiently to a new scan, which shows up as a file with name and location not known in advance (apart from its suffix), the Windows API function [ReadDirectoryChangesW](<http://msdn.microsoft.com/en-us/library/windows/desktop/aa365465(v=vs.85).aspx>) is used to monitor "E:\IMAGE" and all of its subdirectories. Whenever a new file is created or modified anywhere in that tree, a Windows event is triggered and the corresponding path is made available. This mechanism is wrapped up in the C++ class "FolderWatcher".

A second C++ class, "PixelDataGrabber", encapsulates the actual real-time fMRI acquisition mechanism based on the "FolderWatcher" and client-side code of the FieldTrip buffer. Detailed Doxygen-style documentation is
provided in "PixelDataGrabber.h", and developers can also look at "pixeldata_to_remote_buffer.cc" for a simple example of using this class in a command-line application. A slightly more complex program is compiled from "gui_streamer.cc", which combines the PixelDataGrabber with a small GUI written with [FLTK](http://www.fltk.org). This program provides a few buttons for starting and stopping to monitor for new files, and to connect to/disconnect from a FieldTrip buffer (see above).

### Protocol information

How does the "PixelDataGrabber" determine the number of slices and their dimensions? For this to work, the best way is to modify the MR sequence by adding

```plaintext
#ifndef VXWORKS
  pMrProt->fwrite("E:imagemrprot.txt")
#endif
```

to the function "fSeqCheck" in the sequence code, which is executed once before the first scan. This will dump the complete protocol information to the specified location. With the "PixelDataGrabber" listening for files in "E:\image", it will note this and immediately parse the new protocol. The information written to that file is the same that is contained in one of the private tags of the DICOM headers, which the scanner writes using the normal (offline) mechanisms. The filename "mrprot.txt" is currently hard-coded in both the "PixelDataGrabber" and the standard sequences used at the DCCN.

If you run an unmodified MR sequence that does not dump the information, you can try to create your own "mrprot.txt" and place it in "E:\image" before running the scans. In this case, the "PixelDataGrabber" will read that file when the first scan arrives. In case the "PixelDataGrabber" encounters a mismatch between protocol specifications and the size of the ".PixelData" files, it will report an error and not write the sample. The most important ingredients for a hand-made protocol file are shown in the following example:

```plaintext
alTR = 2900000
lContrasts = 5
sKSpace.lBaseResolution = 64
sSliceArray.lSize = 32
sSliceArray.asSlice[0].dPhaseFOV = 224.0
sSliceArray.asSlice[0].dReadoutFOV = 168.0
sSliceArray.asSlice[0].dThickness = 3.0
```

There are many more variables that the "PixelDataGrabber" will react to, but describing this here would be too much detail.

### Decoding the protocol file

"Siemensap", a plain C library in "fieldtrip/realtime/src/acquisition/siemens" provides some functions and datatypes to parse the ASCII format Siemens protocol data into a list or tree of key/value items. Currently supported value types are strings, long integers, and double precision numbers. Field types are determined automatically to a large extend (e.g., a dot in a number implies a double precision value), but some special rules are added. For example, a field name that starts with "d" will always be parsed as a double precision value, even if the value given in ASCII form looks like an integer. Please see `siemensap.h` for Doxygen-style documentation of the API.

The same C library is also used within the **sap2matlab** MEX file for decoding the ASCII protocol into a MATLAB data structure. However, this gets automatically called in **[ft_read_header](/reference/fileio/ft_read_header)**, so users won't need to worry if they stick to the usual FieldTrip functions.

### Compilation

We provide a simple "Makefile" for the MinGW compiler on Windows or GCC on other platforms. Please go to the "realtime/datasource/siemens" directory and type "make" or "mingw32-make". You will need to have the [FLTK](http://www.fltk.org) library installed for your platform. Note that you also might need to [compile](/development/realtime/buffer) the **buffer** library first.

## Testing with pre-recorded fMRI data

You can use the MATLAB function **[ft_realtime_fmriproxy](/reference/realtime/example/ft_realtime_fmriproxy)**, which emulates an fMRI acquisition system by writing volumes in a cycle of about 2 seconds. The data is simulated on the fly.

Alternatively, you can use **[ft_realtime_dicomproxy](/reference/realtime/example/ft_realtime_dicomproxy)**, which emulates an fMRI acquisition system by reading a series of DICOM files from disk.
