---
title: Streaming realtime data from Neuralynx
tags: [realtime, neuralynx]
---

# Streaming realtime data from Neuralynx

The Neuralynx electrophysiology system is used at the DCCN for high-density recordings of LFP and spike activity of up to 256 channels. Furthermore, at the DCC a 32 channel Neuralynx setup is used.

The acquisition setup consists of the Digital Lynx amplifier hardware and the Cheetah acquisition software. The Cheetah software runs on a Windows computer that is connected with the amplifier through a fiber-optic cable.

{% include image src="/assets/img/development/realtime/neuralynx/digital_lynx_16sx-front.png" width="300" %}

## MATLAB-based interface

{% include markup/skyblue %}
The MATLAB implementation is mainly for educational and testing purposes. For proper real-time analyses we recommend you to use the standalone interface, which is faster and requires less system resources.
{% include markup/end %}

The **[ft_realtime_neuralynxproxy](/reference/realtime/example/ft_realtime_neuralynxproxy)** function implements the interface between the Cheetah software and the [FieldTrip buffer](/development/realtime/buffer). Using the dll files that have been made available by Neuralynx, it reads the data and event streams over the network from the Cheetah system and copies them into the buffer. The **[ft_realtime_neuralynxproxy](/reference/realtime/example/ft_realtime_neuralynxproxy)** function should be started in a stand-alone MATLAB session because Neuralynx only provides the dlls for Windows.

There is also an older attempt implemented in the code which allows to access the data in pseudo-real time while it is written to disk (i.e. end-of-file chasing). It turned out that that resulted in highly varying delays of up to 10 seconds and therefore we did not pursue this further.

## Standalone program nlx2ft

There's a new tool called **nlx2ft** which operates with the same principle as **[ft_realtime_neuralynxproxy](/reference/realtime/example/ft_realtime_neuralynxproxy)**, but achieves much lower blocksizes + latencies due to being written in C and using separate threads for grabbing the data and streaming it out again. Currently **nlx2ft** can only write the data to a FieldTrip buffer over TCP (as opposed to spawning its own buffer server). The sources and the Windows binary are available in the "realtime/datasource/neuralynx" directory, and those are the steps to use i

1.  Start the Neuralynx acquisition software (or the Cheetah demo for testing).
2.  Start a FieldTrip buffer server on a machine of your choice.
3.  Start **nlx2ft** with command line arguments "hostname" and "port" as usual. Defaults are "localhost" and "1972".
4.  Start the acquisition by clicking the relevant buttons in the Neuralynx software.

### Compilation

On the command line (Windows), change to the "realtime/datasource/neuralynx" directory and type "make" or "mingw32-make",
depending on the setup of your MinGW compiler. Note that you might need to [compile](/development/realtime/buffer) the **libbuffer** library first.

## External links

- http://www.neuralynx.com
