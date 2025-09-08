---
title: How can I compile the mex files on macOS?
tags: [mex]
category: faq
redirect_from:
    - /faq/how_can_i_compile_the_mex_files_on_os_x/
    - /faq/compile_osx/
---

To compile the mex files with MATLAB 2012b on macOS 10.9 using the gcc version that is shipped with Xcode 6.2, the following changes are needed:

In `/Users/yourname/.matlab/R2012b/mexopts.sh` under the maxi64 section you need to

- add _-std=c++11_ to CXXFLAGS.
- change CC into gcc (instead of gcc-4.2)
- change CXX into g++ (instead of g++-4.2)

In _/Applications/MATLAB_R2012b.app/extern/include/tmwtypes.h_ towards the end, the lines

    #if defined(**STDC_UTF_16**) || (defined(\_HAS_CHAR16_T_LANGUAGE_SUPPORT) && \_HAS_CHAR16_T_LANGUAGE_SUPPORT)
    typedef char16_t CHAR16_T;
    #elif defined(\_MSC_VER)
    typedef wchar_t CHAR16_T;
    #else
    typedef UINT16_T CHAR16_T;
    #endif

need to be replaced by

    #if (defined(**cplusplus) && (**cplusplus >= 201103L)) || (defined(\_HAS_CHAR16_T_LANGUAGE_SUPPORT) && \_HAS_CHAR16_T_LANGUAGE_SUPPORT)
    typedef char16_t CHAR16_T;
    #define U16_STRING_LITERAL_PREFIX u
    #elif defined(\_MSC_VER)
    typedef wchar_t CHAR16_T;
    #define U16_STRING_LITERAL_PREFIX L
    #else
    typedef UINT16_T CHAR16_T;
    #endif
