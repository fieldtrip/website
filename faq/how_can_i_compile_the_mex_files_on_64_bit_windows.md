---
title: How can I compile the mex files on 64-bit Windows?
category: faq
tags: [mex, matlab]
---

# How can I compile the mex files on 64-bit Windows?

The 32-bit versions of MATLAB include the free lcc compiler. However, if you want to use a 64-bit version of MATLAB on a 64-bit Microsoft Windows operating system (WinXP, Vista or Win7), then you must install a compiler yourself. The Microsoft Visual Studio 2008 Express Edition can be used, which can be downloaded for free.

The installation procedure for the compiler is described by MathWorks at <http://www.mathworks.com/support/solutions/en/data/1-6IJJ3L/index.html?solution=1-6IJJ3L>.

Note that during installation of MSVC the following warning was issued.

    Warning: MEX-files generated using Microsoft Visual C++ 2008 require
           that Microsoft Visual Studio 2008 run-time libraries be
           available on the computer they are run on.
           If you plan to redistribute your MEX-files to other MATLAB
           users, be sure that they have the run-time libraries.

The support page on <http://support.microsoft.com/kb/326922> explains that the `msvcr90.dll` file needs to be redistributed along with compiled application (in this case the mex files). Since most Windows computers seem to have this file already installed (probably because it is redistributed with many other applications), we do not include it in the FieldTrip release. There are many places on the internet where you can [download the msvcr90.dll file](https://www.google.com/search?rls=en&q=msvcr90) if you find it missing on your computer. Note that it will be installed alongside the Microsoft Visual Studio 2008 Express Edition.

See also <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=1258> and
[compilation instructions in the code guidelines](/development/guideline/code#windows_64_bit).

## What if the compiler does not work? Is there an alternative?

You might want to try the Microsoft Visual C++ 2010 Redistributable Package for x64, which can be found at <http://www.microsoft.com/en-us/download/details.aspx?id=14632>.

See also <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=2098>.
