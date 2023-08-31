---
title: FieldTrip buffer reference implementation
tags: [realtime, development]
---

# FieldTrip buffer reference implementation

This page is part of the documentation series of the FieldTrip buffer for realtime acquisition. The FieldTrip buffer is a standard that defines a central hub (the [FieldTrip buffer](/development/realtime)) that facilitates realtime exchange of neurophysiological data. The documentation is organized in five main sections, being

1.  description and general [overview of the buffer](/development/realtime/buffer),
2.  definition of the [buffer protocol](/development/realtime/buffer_protocol),
3.  the [reference implementation](/development/realtime/reference_implementation), and
4.  specific [implementations](/development/realtime/implementation) that interface with acquisition software, or software platforms.
5.  the [getting started](/getting_started/realtime) documentation which takes you through the first steps of real-time data streaming and analysis in MATLAB

This page deals with the cross-platform reference implementation in C.

The MATLAB implementation (i.e. the mex file) is by default included in the normal FieldTrip toolbox release. If you just want to use the FieldTrip buffer from within MATLAB, most of the information you'll find here is not relevant for you.

## License

The FieldTrip buffer source code is available from <https://download.fieldtriptoolbox.org/modules/>.

The FieldTrip buffer source code is licensed under both the GNU General Public
License (GPL) and the Berkeley Software Distribution License (BSD).
You can choose the license that has the most advantages for yo

1.  Use the [BSD License](http://www.opensource.org/licenses/bsd-license.php) to use the FieldTrip buffer commercially or
2.  Use the [GNU General Public License](http://www.opensource.org/licenses/gpl-2.0.php) to use the FieldTrip buffer into your open source project.

A plain-text version of the GNU General Public License is included with the
FieldTrip buffer source code release in the file LICENSE_GPL. It can also be
found [here](http://www.opensource.org/licenses/gpl-2.0.php).

A plain-text version of the BSD License is included with the FieldTrip
buffer source code release in the file LICENSE_BSD. It can also be found
[here](http://www.opensource.org/licenses/bsd-license.php).

The FieldTrip buffer makes use of POSIX threads. This is available by default on UNIX-like operating systems. A well-tested implementation of POSIX threads is also available for windows at http://sourceware.org/pthreads-win32/. The pthreads-win32 library is released under the [GNU Lesser General Public License (LPGL)](http://sourceware.org/pthreads-win32/copying.html), which explicitly allows it to be used in closed-source commercial applications.

## Implementation of the C-library

The low-level code for the realtime buffering is implemented in C. Streaming of the data from the EEG/MEG acquisition system to the buffer is system-dependent. The access to the data in MATLAB is realized by mex files. The outline of the acquisition client, the buffer server and a MATLAB client that processes the data is given below. The names in the flowcharts correspond to the functions in the C-code.

{% include image src="/assets/img/development/realtime/reference_implementation/buffer_implementation.png" width="600" %}

The leftmost box represents the application that is writing data into the buffer. The rightmost box represents the application that is doing the analysis. You can see that reading and writing from/to the buffer is completely symmetric and that there is no fundamental difference between a client that is continuously streaming data to the buffer and another client that is processing segments of the data.

The box in the middle represents the actual buffer, with the actual data being stored in computer memory/RAM represented by the blue cloud at the bottom. The header, data and event information is managed by the dmarequest function, where dma refers to direct memory access. The tcpserver function at the top waits for incoming connections. If a connection comes in, it is handed over to the tcpsocket function which reads the incoming request from the network, hands it over to dmarequest, and subsequently writes the response to the client back onto the network.

Given the symmetry in the design, it is possible to have a standalone buffer, i.e. have the tcpserver run in its own application with its own memory. It is also possible to link the tcpserver with the associated buffer memory (the middle box) to the acquisition software. Finally it is also possible to link the tcpserver with the associated buffer memory to the application that is doing the processing. The MATLAB mex file includes the tcpserver, which can optionally be started as a separate thread.

## Compiling the code

Building the source code on different platforms can appear challenging. The buffer has been successfully compiled and tested on Linux (32 and 64-bit), Windows (32-bit) and macOS (32-bit PowerPC and 32 and 64-bit Intel platform). We try to facilitate the compilation of the source code by supplying various build methods.

Generally, please note that no matter which platform, there are three different parts of the code, which are compiled in different steps.

- `.../buffer/src` contains the core buffer functions written in C. These are compiled into a library "libbuffer.[a/lib]" by using Makefiles or project files **outside** of MATLAB.
- `.../buffer/test` contains demos and test applications written in C. These are also compiled outside of MATLAB, but since they depend on "libbuffer", they can only be compiled after that.
- `.../buffer/matlab` contains the sources of the MEX file "buffer.mex???". Since MATLAB installations vary so much, we rely on the command "mex" to compile this part **inside** MATLAB. As of October 2010, the MEX files are not linked against "libbuffer" anymore, but rather the same source files are directly pulled in using "mex".

The best tested method for compilation of the stand-alone tools is by using the Makefile (only for Linux, macOS and MinGW). For Windows, Borland C++ (version 6.0) project files are supplied. The buffer can also be compiled on Linux, macOS, and Windows using [cmake](http://www.cmake.org). Compiling on Linux and macOS is pretty straight forward while doing that on Windows is a bit more tricky.

### Linux and macOS

On Linux and macOS almost all dependencies should be pre-installed. You need a build-environment. This should be available by default on macOS. On Linux it can be installed by installing a package called something like "build-essentials", which is probably available through the distribution's package-system (like apt on debian).

Compiling the buffer library should simply work by changing into the directory "...realtime/buffer/src" and typing "make", with the expected outcome of a new file "libbuffer.a". You can also build the demos and test applications by changing into "...realtime/buffer/test" and typing "make" again.

The MEX-file is compiled within MATLAB. Just change into "...realtime/buffer/matlab" and type "compile". This should only fail in case your version of GCC is either too old or (more likely) too recent, and MATLAB will give you a corresponding warning. In particular, GCC>=4.2 doesn't seem to be supported by MATLAB versions as new as 2009b.

If you have an unsupported GCC version, you should check whether your Linux distribution offers older packages of GCC. You can also compile GCC from source and install multiple versions of GCC alongside, but please refer to <http://gcc.gnu.org> for more information on this. If you have multiple versions of GCC, you will also have to tweak the file "~/.matlab/matlabXXXX/mexopts.sh" where "XXXX" denotes the version of MATLAB you are using: First locate the right "case" segment for your operation system, e.g., glnx86 for 32-bit Linux flavours. Then, modify the variables "CC" and "CXX" such that they point to the binaries of the right version. As a hint, these are often called "gcc-4.2" and "g++-4.2", that is, the version number forms part of the name. Maybe try and find the right files on the command line first.

#### Buffer MEX-file with various MATLAB versions

The following was tested from 16-03-2010 to 18-03-2010.

| MATLAB version | 32-bit ArchLinux, GCC 4.2 and 4.4                                                      | 32-bit Red Hat (mentat069), GCC 3.4.3 | 64-bit Red Hat (mentat 20x), GCC 4.1.2 |
| -------------- | -------------------------------------------------------------------------------------- | ------------------------------------- | -------------------------------------- |
| 6.1            | compiles, but does not run due to missing mxCreateDoubleScalar                         |                                       | n.a.                                   |
| 6.5.1          | compiles with GCC 3.4 -- 4.4 and runs, but not binary compatible with MEX files >= 7.0 |                                       | n.a.                                   |
| 7.0            | n.a.                                                                                   | compiles, but does not run (see 7.1)  | n.a.                                   |
| 7.1            | compiles, but does not run (complains about missing GCC 3.3 libraries)                 |                                       | compiles and runs                      |
| 7.2 (R2006a)   | compiles and runs (GCC up to 4.2)                                                      |                                       | compiles and runs                      |
| 7.3 (R2006b)   | compiles and runs (GCC up to 4.2)                                                      |                                       | compiles and runs                      |
| 7.4 (R2007a)   | compiles and runs (GCC up to 4.2)                                                      |                                       | compiles and runs                      |
| 7.5 (R2007b)   | compiles and runs (GCC up to 4.2)                                                      |                                       | compiles and runs                      |
| 7.6 (R2008a)   | n.a.                                                                                   |                                       | compiles and runs                      |
| 7.7 (R2008b)   | does not compile (libraries missing), can run other version                            |                                       | compiles and runs                      |
| 7.8 (R2009a)   | compiles and runs (GCC up to 4.2)                                                      |                                       | compiles and runs                      |
| 7.9 (R2009b)   | compiles and runs (GCC up to 4.2)                                                      |                                       | compiles and runs                      |

Fields marked with "n.a." refer to unavailable or non-functioning MATLAB configurations. Note that although you can run 32-bit MATLAB versions
on a 64-bit machine, you will not be able to compile MEX-files with your native 64-bit compiler in this case.

**Cross-version compatibility**: It seems MEX-files compiled on any version >= 7.2 can be run on any other version >= 7.2 on the same type of machine.
**Possible trap**: If you're trying to compile both 32 and 64-bit versions from the same source directory, make sure you always compile "libbuffer.a"
using the same platform. If you get strange build errors, you might try to link a 64-bit MEX file to a 32-bit library, or vice versa.

#### Building with cmake (probably outdated)

On macOS the cmake software has to be downloaded and installed from [here](http://www.cmake.org), or using FinkCommander.

In the top-level directory of the source-tree (the place where you see e.g., the "src" folder) create a new directory called e.g., "build" and enter it. Now issue "cmake ../". This checks for dependencies. If cmake complains about not finding something, it must be installed first.

Typing "make" compiles and links the libaries and some executables all of which can be found in the "src" directory (n.b. not the "src" directory where the sources are but the newly created one in the folder cmake was called from).

### Windows

One possibility of using the buffer on Windows is by downloading and installing the [cygwin](http://cygwin.com/) environment. In the setup.exe of cygwin you have to mark "cmake" and "make" to be installed. Afterwards it's the same as for Linux and Mac. The downside of this approach is that the libraries and executables depend on the cygwin-dll.

#### MATLAB-supplied LCC compiler (MEX file only)

On 32-bit Windows platforms, MATLAB ships with the LCC compiler, which can be used to compile the buffer MEX file: Within MATLAB, change to the "...buffer\matlab" directory and type "compile". This should produce the file "buffer.mexw32" in the "...\fileio\private" directory.

#### MinGW and Gnumex

[MinGW](http://www.mingw.org/) is a port of GCC that produces executables without special dependencies (or rather, they only depend on the Microsoft C run-time which is present on any Windows system). For compiling the code in both the "src" and "test" directories, you can just use the same "Makefile" as the one on Linux and macOS.

Unfortunately, MATLAB doesn't recognise MinGW by itself, so for compiling the MEX-file, you will need to get [Gnumex](http://gnumex.sourceforge.net/). This is a small collection of tools that wrap the MinGW utilities for usage by the "mex" command. Both MinGW and Gnumex are relatively easy to install, and you should stick to the defaults (in particular, please place MinGW in "C:\MinGW"). You should also put "C:\MinGW\bin" into your path. After installing, you do the following:

1.  In a command prompt window, change to the "src" directory and type "mingw32-make". If everything works, you should get a "libbuffer.a" file
2.  Change to the "test" directory and type "mingw32-make". This should produce "demo_buffer.exe" and further executables.
3.  Within MATLAB, change to the "...buffer\matlab" directory and type "compile('mingw')". This should produce the file "buffer.mexw32" in the "...\fileio\private" directory.

#### Borland C++ 5.5 (Free command line tools)

Assuming you've installed the tools and put the corresponding "bin" directory (e.g., "C:\BCC55\bin") on the path, you may need to select BCC as the compiler in MATLAB using "mex -setup". Then you can use "Makefile_BCC" for compiling the core buffer functions and test applications, and "compile.m" for compiling the buffer.

1.  In a command prompt window, change to the "src" directory and type "make -f Makefile_BCC". If everything works, you should get a "libbuffer.lib" file
2.  Change to the "test" directory and type the same. This should produce "demo_buffer.exe" and further executables.
3.  Within MATLAB, change to the "...buffer\matlab" directory and type "compile('bcc55')". This should produce the file "buffer.mexw32" in the "...\fileio\private" directory.

#### Visual C++

The "src" directory contains a VC2008 project and solution file, which you can use to compile the core functions. You should get a "libbuffer.lib" file as a result, which you can then link your own applications against.

We also provide a file "Makefile.mak" for compiling the buffer library and the stand-alone demos from the command line. This should work across different versions of Visual C++ and Windows SDK compilers. In order to build the library, open a command line window with the environment variables properly set up for your compiler (usually the installation routine of the compiler will provide a corresponding item in your start menu), change to "...\buffer\src" and type "nmake -f Makefile.mak". This should work for both 32-bit and 64-bit platforms and compilers. In the same manner, you can compile the demos by typing the same command in "...\buffer\test".

Compilation of the MEX file is again done in MATLAB. Make sure that Visual C++ is selected as the compiler ("mex -setup"), change to "...\buffer\matlab" and type "compile('vc')". This should work on both 32- and 64-bit platforms.

#### Other build environments / Troubleshooting

If your favorite compiler is not listed above, or you have some special non-standard installation that gives you problems compiling the MEX file, you can tweak "realtime/buffer/compile.m" to suit your needs. You should try to only modify the contents of the variables 'cflags', 'extra_cflags', and 'ldflags' for compilation and linking options, ideally by adding a new case inside the switch statement. In any case, you should first make sure that you are able to compile the buffer C library and build/run the demos.

## Cross-platform compatibility

### Endiannes

As of 18-05-2010, the FieldTrip buffer TCP server provides an automatic adaptation of requests and its responses to the [endianness](https://en.wikipedia.org/wiki/Endianness) of the client. For example, if the buffer resides on an Intel x86 computer, and data is written to it from a PPC G4 computer, the server will automatically convert the incoming packets (data/events/header information) to its own (little-endian) format, process the request, and then convert the response back to the (big-endian) format of the client. The opposite happens if the PPC G4 is the server, and the PC the client. No conversion is done if both the server and the client run on the same type of machine (which includes the _dmarequest_ as a notable case).

Besides the G4 and G5 Apple PPC platform, the Raspberry Pi is also a big-endian computer.
