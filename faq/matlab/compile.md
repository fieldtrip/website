---
title: How can I compile the mex files and command-line executable?
category: faq
tags: [mex, compile]
redirect_from:
    - /faq/compile/
---

# How can I compile the mex files and command-line executable?

We try to provide FieldTrip with all the mex files compiled for the most common platforms. However, sometimes specific MATLAB versions and/or specific operating systems require that you (re)compile the mex files. FieldTrip also includes a number of (command-line) executable programs. These are also provided in a compiled form that allows you to use them directly. Sometimes it is also required to recompile those. This FAQ describes the compilation procedure for the various components.

Note that for compiling the mex files and/or executables you will need to have write access to the installation directory. If you are using a shared version that is installed on a network drive, that might not be the case.

{% include markup/yellow %}
Compilation of the mex files is only supported for the *full* version of FieldTrip, which you can download from our download server or from Github. It is not supported for the *lite* version that that is released along with some other toolboxes, such as EEGLAB. If you want to recompile mex files for the FieldTrip copy included with EEGLAB, please update it to the full version, preferably the one from Github.
{% include markup/end %}

## General compilation of most mex files

Compiling mex files in MATLAB requires that you run the following once.

    mex -setup

The FieldTrip main directory contains the **[ft_compile_mex](/reference/utilities/ft_compile_mex)** function, which compiles all regular mex files. For some of the mex files it is needed to have two copies, i.e. one in `fieldtrip/private` and another one in `fieldtrip/fileio/private`. The `fieldtrip.bin/synchronize-private.sh` Bash script copies them to the correct locations.

The **[ft_compile_mex](/reference/utilities/ft_compile_mex)** function will try to detect whether the c-code for the mex files has changed and only compile the updated ones. To recompile all mex files, you can do

    ft_compile_mex(true)

where the "true" argument tells the function to force a fresh compile for all mex files.

Note that there are some mex files that are not compiled with this function. Also the [command-line executable](/faq/compiled) version of FieldTrip is not compiled with this function.

## Autocompile

Some of the simple mex files come with a corresponding m-file that automatically compile the mex file if it detects that the mex file is missing for your platform.

## Realtime buffer library

The realtime buffer mex file is compiled on the MATLAB command line with

```matlab
cd realtime/buffer/matlab
compile
```

The command line utilities and the library can be compiled on the Unix command line with

```bash
cd realtime/buffer/src
make
cd ../test
make
```

Please see [this page](/development/realtime/buffer#compiling_the_code) for more detailed instructions.

## Peer distributed computing

The peer distributed computing toolbox has a number of mex files that are compiled on the MATLAB command line with

    peercompile

Furthermore, for the different Unix platforms there is a command-line peerworker client. Since we provide an executable for the different platforms, the executables need to have a different name. We are following the MathWorks naming scheme for the mex files, i.e.

- peerworker.maci    (32-bit macOS)
- peerworker.maci64  (64-bit macOS)
- peerworker.glnx86  (32-bit Linux)
- peerworker.glnxa64 (64-bit Linux)

Compiling the peerworker command line executable is done on the Unix command line. However, since the compilation process involves linking the object files to the MATLAB engine library, the location where your copy of MATLAB is installed should be specified. Please edit the Makefile and change it so that the following settings are correct for your platform. Note that maci is used for 32-bit MATLAB and maci64 is used for 64-bit MATLAB.

```Makefile
MATLABARCH = maci
MATLABPATH = /Applications/MATLAB_R2009a.app
MATLABLIBS = -L$(MATLABPATH)/bin/$(MATLABARCH) -leng -lmx
MATLABINC  = -I$(MATLABPATH)/extern/include
```

Then execute the following commands from the command line

```bash
cd peer/src
make
```

You should similarly modify MATLABARCH and MATLABPATH in `peer/peerworker`.

If you want to compile a 32-bit version on a 64-bit platform, e.g., if you are using an older 32-bit MATLAB version on a newer 64-bit operating system, you should also specify

```Makefile
# override the architecture defaults
CFLAGS += -arch i386
```

## Stand-alone executables in realtime directory

We generally only provide a `Makefile` for the GNU toolchain. This should be enough to compile the code using GCC on Linux/macOS and using MinGW and Cygwin on Windows. Please note that **not all tools will compile on all platforms**. Furthermore, you might need additional libraries or vendor-specific SDKs which we can't distribute (e.g., you can only compile the [emotiv2ft](/development/realtime/emotiv) application on Windows, and it requires the Emotiv SDK).

## Fixing MEX-compilation with 32-bit variants of MATLAB running under 64-bit Linux

In this situation you could encounter errors like the following

```bash
(...)

Compiling tprod for first use

/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-linux-gnu/4.3.5/libstdc++.so when searching for -lstdc++
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-linux-gnu/4.3.5/libstdc++.a when searching for -lstdc++
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-linux-gnu/4.3.5/libstdc++.so when searching for -lstdc++
/usr/bin/ld: skipping incompatible /usr/lib/gcc/x86_64-linux-gnu/4.3.5/libstdc++.a when searching for -lstdc++
/usr/bin/ld: cannot find -lstdc++ collect2: ld returned 1 exit status

mex: link of "tprod.mexglx" failed.

??? Error using ==> tprod at 132 unable to compile MEX version of '/home/user/fieldtrip/multivariate/external/farquhar/tprod/tprod', please make sure your MEX compiler is set up correctly (try 'mex -setup').
```

### Problem

The problem is that - even when the 'architecture' of the computer is explicitly specified to MATLAB (like by starting MATLAB with a command of the form: ''matlab -glnx86'') - in some cases MATLAB does not conform to that specified architecture, but to the architecture of the Linux operating system installed on your computer (in our case, 64-bit named "amd64" in Linux and "GLNXA64" in MATLAB terminology).

### Solution for Ubuntu Linux (10.10)

- Install the package "ia32-libs", for example with the easy-to-use _Synaptic Package Manager_.

- Let `MATLABROOT` stand for the directory where your MATLAB is installed. In the file` MATLABROOT/bin/mexopts.sh` change the line

```bash
CLIBS="\$CLIBS -lstdc++"
```

to

```bash
CLIBS="$CLIBS -L**MATLABROOT**/sys/os/glnx86 -lstdc++"
```

- Now make a _symbolic link_ so that the _linker_ can find the _C++ standard library_, for example by pressing CTRL-ALT-T on your keyboard to open a terminal window. In that terminal window type a command of this form:

```bash
  ln -s MATLABROOT/sys/os/glnx86/libstdc++.so.6 MATLABROOT/sys/os/glnx86/libstdc++.so
```

- Start MATLAB again, and be sure to explicitly specify the architecture to MATLAB.

### Source references

If the solution above fails for you, have a look at more extensive approaches presented in the original sources for this solution.

- <http://saravananthirumuruganathan.wordpress.com/2010/02/10/installingrunning-matlab-and-compiling-matlab-extensions-in-a-64-bit-ubuntu-system>
- <http://www.walkingrandomly.com/?p=1959>
