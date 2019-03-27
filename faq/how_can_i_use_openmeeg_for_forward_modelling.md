---
title: How can I use OpenMEEG for forward modeling?
tags: [faq, headmodel, source]
---

{% include markup/danger %}
This documentation is outdated, the latest version is available from <http://openmeeg.github.io>.
{% include markup/end %}

# How can I use OpenMEEG for forward modeling?

OpenMEEG is a package that solves the MEG and EEG forward problems.
It implements a Boundary Element Method (BEM) and provides accurate solutions
when dealing with realistic head models (1, 2 or 3 nested layers)

The OpenMEEG binaries are **not** included in the FieldTrip release, but the OpenMEEG MATLAB wrapper functions are.

## Installing OpenMEEG

OpenMEEG is available on Linux, macOS and Windows.
A 64bit machine is preferred due to the computational load of M/EEG forward modeling using the BEM.

OpenMEEG can be downloaded from <https://gforge.inria.fr/frs/?group_id=435>.

Installation procedure:

### For Linux

- check your local version of gcc compiler (type 'gcc -v' in a terminal).

  \$ gcc -v
  gcc version 4.3.2 (GCC)

- If your version of gcc is superior to 4.2 download OpenMEEG for gcc 4. Otherwise download OpenMEEG for gcc 3. The OpenMEEG version for gcc 4 provides support of OpenMP for parallel and faster computation.

#### Install from the tar.gz file

- untar the .tar file
- Set the PATH environment variable in the appropriate .rc configuration file (e.g. .bashrc or .bash_profile)
- Example (for a Bash shell): export PATH=\$PATH:openmeeg_folder/bin
- Set the LIB environment variable
- Example (for a Bash shell): export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:openmeeg_folder/lib

#### Install from the RPM

- open the RPM file with 'rpm' from command line in Linux or with an alternative front-end program (e.g. 'up2date' (CentOS) or 'yum' for Fedora/Red Hat)

  \$ rpm -ivh OpenMEEG-2.0-0.x86_64.rpm

### For Windows

- Run the installer
- Choose to agree the license terms
- Select option to add OpenMEEG to the Windows path

### For macOS

- Run the installer
- Choose to agree the license terms

### From source

The source code of OpenMEEG can be accessed by SVN

    svn checkout svn://scm.gforge.inria.fr/svn/openmeeg

OpenMEEG is build with CMake on all platforms.

It only depends on blas/lapack or atlas on Linux and macOS and the Intel MKL on Windows.

## Make sure that it works

After installing, you should check on the MATLAB command line that the OpenMEEG command-line executable can be found. This is done by typing in your MATLAB prompt:

    > system('om_assemble')

You should see something like this:

    > system('om_assemble');
    om_assemble version 2.0.svn (570) compiled at Mar 28 2010 07:25:26
    Not enough arguments
    Please try "om_assemble -h" or "om_assemble --help "

If the system call prints the correct version information, then you are all done and you can use the forward modeling of OpenMEEG in combination with the inverse methods implemented in FieldTrip.

A good start is the example script "openmeeg_eeg_leadfield_example.m" found in "external/openmeeg"

## If it does not seem to work

{% include markup/info %}
Some of the pre-compiled packages could have issues running on a particular Linux OS (e.g. Fedora, CentOS), if you use the OpenMEEG 2 packages. Try then to download the OpenMEEG statically linked version (OpenMEEG-2.1.0-Linux.amd64-gcc-4.1.2-OpenMP-static.tar.gz or OpenMEEG-2.1.0-Linux.i386-gcc-4.1.2-static.tar.gz for Linux)
{% include markup/end %}

If you still meet any difficulty do not hesitate to contact the OpenMEEG team: openmeeg-info@lists.gforge.inria.fr

Remember that OpenMEEG is Open Source but if you publish results using OpenMEEG you should cite the necessary related papers. More infos can be found a <http://openmeeg.gforge.inria.fr>.
