---
title: How do I install the OpenMEEG binaries
category: faq
tags: [openmeeg, headmodel]
redirect_from:
    - /faq/how_do_i_install_the_openmeeg_binaries/
    - /faq/openmeeg/
---

OpenMEEG is a package that solves the MEG and EEG forward problems. It implements a Boundary Element Method (BEM) and provides accurate solutions when dealing with realistic head models (1, 2 or 3 nested layers)

The OpenMEEG binaries are **not** included in the FieldTrip release, but the OpenMEEG MATLAB wrapper functions are.

{% include markup/red %}
This documentation is most likely outdated. The latest version, more up to date installation instructions and support are available from <http://openmeeg.github.io>.
{% include markup/end %}

OpenMEEG is available on Linux, macOS and Windows. A 64-bit machine is preferred due to the computational load of M/EEG forward modeling using the BEM.

OpenMEEG can be downloaded from <https://openmeeg.github.io>.

## Installation procedure for Linux

### Install from the tar.gz file

-   untar the .tar file
-   Set the PATH environment variable in the appropriate .rc configuration file (e.g., .bashrc or .bash_profile)
-   Example (for a Bash shell): `export PATH=\$PATH:openmeeg_folder/bin`
-   Set the LIB environment variable
-   Example (for a Bash shell): `export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:openmeeg_folder/lib`

### Install from the RPM

-   open the RPM file with `rpm` from command line in Linux or with an alternative front-end program (e.g., `up2date` for CentOS or `yum` for Fedora/RedHat)

```bash
$ rpm -ivh OpenMEEG-2.0-0.x86_64.rpm
```

## Installation procedure for Windows

-   Run the installer
-   Choose to agree the license terms
-   Select option to add OpenMEEG to the Windows path

## Installation procedure for macOS

-   Run the installer
-   Choose to agree the license terms

## Installing from source

The source code of OpenMEEG can be accessed on <https://github.com/openmeeg/openmeeg/>

OpenMEEG is build with CMake on all platforms.

It only depends on blas/lapack or atlas on Linux and macOS and the Intel MKL on Windows.

-   check your local version of gcc compiler (type 'gcc -v' in a terminal).

```bash
$ gcc -v
gcc version 4.3.2 (GCC)
```

-   If your version of gcc is superior to 4.2 download OpenMEEG for gcc 4. Otherwise download OpenMEEG for gcc 3. The OpenMEEG version for gcc 4 provides support of OpenMP for parallel and faster computation.

## Make sure that MATLAB can find them

You should add the location of the OpenMEEG binaries and dynamic link libraries to your path, e.g., by adding a line like this to your .profile script on macOS

```bash
export PATH=$PATH:/opt/openmeeg/bin
export DYLD_LIBRARY_PATH=/opt/openmeeg/lib:$DYLD_LIBRARY_PATH
```

or using `LD_LIBRARY_PATH` on Linux.

You can test the actual path that MATLAB will use by

```matlab
system('echo $PATH');
system('echo $DYLD_LIBRARY_PATH'); % or LD_LIBRARY_PATH on Linux
```

If it is not appropriate, you can do

```matlab
setenv('PATH', ['/opt/openmeeg/bin:' getenv('PATH')]);
setenv('DYLD_LIBRARY_PATH', ['/opt/openmeeg/lib:' getenv('DYLD_LIBRARY_PATH')]);
```

in MATLAB on macOS, or

```matlab
setenv('PATH', ['/opt/openmeeg/bin:' getenv('PATH')]);
setenv('LD_LIBRARY_PATH', ['/opt/openmeeg/lib:' getenv('LD_LIBRARY_PATH')]);
```

on Linux.

## Make sure that it works

After installing, you should check on the MATLAB command line that the OpenMEEG command-line executable can be found. This is done by typing in your MATLAB prompt:

    > system('om_assemble')

You should see something like this:

    > system('om_assemble');
    om_assemble version 2.0.svn (570) compiled at Mar 28 2010 07:25:26
    Not enough arguments
    Please try "om_assemble -h" or "om_assemble --help "

If the system call prints the correct version information, then you are all done and you can use the forward modeling of OpenMEEG in combination with the inverse methods implemented in FieldTrip.

A good start is the example script `openmeeg_eeg_leadfield_example.m` found in `external/openmeeg`.

## If it does not seem to work

{% include markup/skyblue %}
Some of the pre-compiled packages could have issues running on a particular Linux OS (e.g., Fedora, CentOS), if you use the OpenMEEG 2 packages. Try then to download the OpenMEEG statically linked version (OpenMEEG-2.1.0-Linux.amd64-gcc-4.1.2-OpenMP-static.tar.gz or OpenMEEG-2.1.0-Linux.i386-gcc-4.1.2-static.tar.gz for Linux)
{% include markup/end %}

If you still meet any difficulty do not hesitate to contact the OpenMEEG team: openmeeg-info@lists.gforge.inria.fr

Remember that OpenMEEG is Open Source, but if you publish results using OpenMEEG, you should cite the necessary related papers. More infos can be found at <https://openmeeg.github.io>.
