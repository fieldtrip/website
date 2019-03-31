---
title: How do I install the OpenMEEG binaries?
---

# How do I install the OpenMEEG binaries?

## Install the binaries

Download a suitable version for your operating system (Mac, Linux 32 or 64-bits, Windows 32 or 64-bits) from http://gforge.inria.fr/frs/?group_id=435.

### For Linux

Check your local version of gcc compiler (type 'gcc -v' in a terminal

        $ gcc -v
        gcc version 4.3.2 (GCC)

OpenMEEG installers are provided for gcc >= 4.1.

The OpenMEEG version for Linux 64 provides support of OpenMP for parallel and faster computation.

#### Install from the tar.gz file

       * untar the .tar file
       * Set the PATH environment variable in the appropriate .rc configuration file
       * Example: export PATH=$PATH:openmeeg_folder/bin
       * Set the LIB environment variable
       * Example: export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:openmeeg_folder/lib

#### Install from the RPM

- open the RPM with your package manager.

### For Windows

    * Run the installer
    * Choose to agree the license terms
    * Select option to add OpenMEEG to the Windows path

### For macOS

    * Run the installer
    * Choose to agree the license terms

## Make sure that MATLAB can find them

You should add the location of the OpenMEEG binaries and dynamic link libraries to your path, e.g. by adding a line like this to your .profile script on macOS

    export PATH=$PATH:/opt/openmeeg/bin
    export DYLD_LIBRARY_PATH=/opt/openmeeg/lib:$DYLD_LIBRARY_PATH

or using LD_LIBRARY_PATH on Linux.

You can test the actual path that MATLAB will use by
system('echo $PATH');
    system('echo $DYLD_LIBRARY_PATH'); % or LD_LIBRARY_PATH on Linux

If it is not appropriate, you can do

    setenv('PATH', ['/opt/openmeeg/bin:' getenv('PATH')]);
    setenv('DYLD_LIBRARY_PATH', ['/opt/openmeeg/lib:' getenv('DYLD_LIBRARY_PATH')]);

on macOS, or

    setenv('PATH', ['/opt/openmeeg/bin:' getenv('PATH')]);
    setenv('LD_LIBRARY_PATH', ['/opt/openmeeg/lib:' getenv('LD_LIBRARY_PATH')]);

on Linux.
