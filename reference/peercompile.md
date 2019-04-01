---
title: peercompile
---
```
 PEERCOMPILE  This script/function is used for compiling and linking the 'peer' MEX file.

 On Linux and MacOS X, you should just be able to call this function without arguments.

 On Windows, you need to select a compiler using one of the following options:
   compile('bcb')   - Borland C++ Builder
   compile('bcc55') - Borland C++ 5.5 (free command line tools)
   compile('mingw') - MinGW (GCC port without cygwin dependency)
   compile('vc')    - Visual Studio C++ 2005 or 2008

 Please note that this script does NOT set up your MEX environment for you, so in case
 you haven't selected a C compiler on Windows yet, you need to type 'mex -setup' first
 to choose either the Borland or Microsoft compiler. If you want to use MinGW, you also
 need to install Gnumex (http://gnumex.sourceforget.net), which comes with its own
 procedure for setting up the MEX environment.
```
