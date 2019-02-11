---
title: How can I compile the mex files and command-line executables ?
tags: [faq, mex, compile]
---

#  How can I compile the mex files and command-line executables ?

We try to provide FieldTrip with all the mex files compiled for the most common platforms. However, sometimes specific MATLAB versions and/or specific operating systems require that you (re)compile the mex files. FieldTrip also includes a number of (command-line) executable programs. These are also provided in a compiled form that allows you to use them directly. Sometimes it is also required to recompile those. This FAQ describes the compilation procedure for the various components.

Note that for compiling the mex files and/or executables you will need to have write access to the installation directory. If you are using a shared version that is installed on a network drive, that might not be the case.

## General compilation of most mex files

Compiling mex files in MATLAB requires that you have run

    mex -setup

once.

The FieldTrip main directory contains the **[ft_compile_mex](/reference/ft_compile_mex)** function, which compiles all regular mex files and copies them to the required locations. Due to the private directories, for some of the mex files it is needed to have two copies, i.e. one in private and another one in fileio/private.

The **[ft_compile_mex](/reference/ft_compile_mex)** function will try to detect whether the c-code for the mex files has changed and only compile the updated ones. To recompile all mex files, you can do

    ft_compile_mex(true)

where the "true" argument tells the function to force a new compile for all mex files.

Note that there are certain mex files that are not compiled with this function. ALso the command-line executables are not compiled with this function.

## Autocompile

Some of the simple mex files come with a corresponding m-file that automatically tries to compile the mex file if it detects that the mex file is missing for your platform.

## Config object

The config object is used by ft_checkconfig to keep track of cfg options that are used and changed. By default this is *not* enabled. The cfg-tracking is implemented with a number of mex files. To compile these, do

    cd @config/private
    compile

## Uint64 object

The uint64 object is used for reading some particular file formats (a.o. Neuralynx). The mex files in the object are compiled with

    cd fileio/@uint64
    compile

## Realtime buffer library

The realtime buffer mex file is compiled on the MATLAB command line with

    cd realtime/buffer/matlab
    compile

The command line utilities and the library can be compiled on the Unix command line with

    cd realtime/buffer/src
    make
    cd ../test
    make

Please see [this page](/development/realtime/buffer#compiling_the_code) for more detailed instructions.

## Peer distributed computing

The peer distributed computing toolbox has a number of mex files that are compiled on the MATLAB command line with

    peercompile

Furthermore, for the different Unix platforms there is a command-line peerslave client. Since we provide an executable for the different platforms, the executables need to have a different name. We are following the Mathworks naming scheme for the mex files, i.e.

    peerslave.maci    (32-bit OS X)
    peerslave.maci64  (64-bit OS X)
    peerslave.glnx86  (32-bit linux)
    peerslave.glnxa64 (64-bit linux)

Compiling the peerslave command line executable is done on the Unix command line. However, since the compilation process involves linking the object files to the Matlab engine library, the location where your copy of Matlab is installed should be specified. Please edit the Makefile and change it so that the following settings are correct for your platform. Note that maci is used for 32-bit Matlab and maci64 is used for 64-bit Matlab.

    MATLABARCH = maci
    MATLABPATH = /Applications/MATLAB_R2009a.app
    MATLABLIBS = -L$(MATLABPATH)/bin/$(MATLABARCH) -leng -lmx
    MATLABINC  = -I$(MATLABPATH)/extern/include

Then execute the following commands from the command line

    cd peer/src
    make

You should similarly modify MATLABARCH and MATLABPATH in peer/peerslave

If you want to compile a 32 bit version on a 64 bit platform, e.g. if you are using an older 32-bit MATLAB version on a newer 64-bit operating system, you should also specify

    # override the architecture defaults
    CFLAGS += -arch i386

##  Stand-alone executables in realtime directory

We generally only provide a ''Makefile'' for the GNU toolchain. This should be enough to compile the code using GCC on Linux/Mac OS X and using MinGW and Cygwin on Windows. Please note that not all tools will compile on all platforms, and that you might need additional libraries or vendor-specific SDKs which we can't distribute (e.g., you can only compile the [emotiv2ft](/development/realtime/Emotiv) application on Windows, and you need the Emotiv EDK).

##  Fixing MEX-compilation with 32-bit variants of MATLAB running under 64-bit Linux

In this situation you could encounter errors like the followin

	(...)

	Compiling tprod for first use

	/usr/bin/ld: skipping

	incompatible /usr/lib/gcc/x86_64-linux-gnu/4.3.5/libstdc++.so when searching for -lstdc++ /usr/bin/ld: skipping

	incompatible /usr/lib/gcc/x86_64-linux-gnu/4.3.5/libstdc++.a when searching for -lstdc++ /usr/bin/ld: skipping

	incompatible /usr/lib/gcc/x86_64-linux-gnu/4.3.5/libstdc++.so when searching for -lstdc++ /usr/bin/ld: skipping

	incompatible /usr/lib/gcc/x86_64-linux-gnu/4.3.5/libstdc++.a when searching for -lstdc++ /usr/bin/l
	  cannot find -lstdc++ collect2: ld returned 1 exit status

	mex: link of ' "tprod.mexglx"' failed.

	??? Error using ==> tprod at 132 unable to compile MEX version of '/mnt/data/FieldTrip/bin/fieldtrip-read-only/multivariate/external/farquhar/tprod/tprod', please make sure your MEX compiler is set up correctly (try 'mex -setup')."

### Problem

This error is caused by the unrobust MATLAB design. The problem is that even when the 'architecture' of the computer is explicitly specified to MATLAB (like by starting MATLAB with a command of the form: ''matlab -glnx86''), in some cases MATLAB does not conform to that specified architecture, but to the architecture that the Linux operating system on your computer reports (in our case, 64-bit named "amd64" in Linux and "GLNXA64" in MATLAB terminology) like it normally does.

### Solution for Ubuntu Linux (10.10)

*  Install the package "ia32-libs", for example with the easy-to-use *Synaptic Package Manager*.

*  Let ''__MATLABROOT__'' stand for the directory where your MATLAB is installed. In the file   ''__MATLABROOT__/bin/mexopts.sh'' change the line:
'' CLIBS="$CLIBS -lstdc++" ''
to:
'' CLIBS="$CLIBS -L__MATLABROOT__/sys/os/glnx86 -lstdc++" ''

*  Now make a *symbolic link* so that the *linker* can find the *C++ standard library*, for example in the following way.
    * Press CTRL-ALT-T on your keyboard to open a terminal window.
    * In that terminal window type a command of this form:
''ln -s __MATLABROOT__/sys/os/glnx86/libstdc++.so.6 __MATLABROOT__/sys/os/glnx86/libstdc++.so''.

*  Start MATLAB again, and be sure to explicity specify the architecture to MATLAB.
 * If this solution is inadequate or fails for you, have a look at more extensive approaches presented in the original sources for this solution.

### Source references

[http://saravananthirumuruganathan.wordpress.com/2010/02/10/installingrunning-matlab-and-compiling-matlab-extensions-in-a-64-bit-ubuntu-system/](http://saravananthirumuruganathan.wordpress.com/2010/02/10/installingrunning-matlab-and-compiling-matlab-extensions-in-a-64-bit-ubuntu-system/)

[http://www.walkingrandomly.com/?p=1959](http://www.walkingrandomly.com/?p=1959)
