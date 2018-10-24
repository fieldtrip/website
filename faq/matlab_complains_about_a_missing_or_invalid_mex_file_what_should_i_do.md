---
layout: default
tags: faq matlab mex
---

## MATLAB complains about a missing or invalid MEX file, what should I do?

The FieldTrip version that we release includes compiled mex files for the most common platforms (Windows, Linux, macOS). However, it might be that you have a combination of operating system and MATLAB on which the precompiled mex files are not included or on which they do not work. In that case you have to (re)compile them yourself.

`<note warning>`Note that in general the toolboxes in fieldtrip/external are **not** maintained by the FieldTrip team but come from an external source.

If you run into problems with mex files from SPM, i.e. the ones included in fieldtrip/external/spmX, you should have a look at https://en.wikibooks.org/wiki/SPM/MATLAB. See also further down on this page.
`</note>`
 
The source code for the mex files is mostly contained in the fieldtrip/src directory. Some mex files are contained in fieldtrip/external, for example for SPM. Those are not the responsibility of the FieldTrip team.

### Recommended way of recompiling

To (re)compile all mex files at once, you can use the **[ft_compile_mex](/reference/ft_compile_mex)** function. 

### Alternative way of recompiling

You can recompile individual mex files for your platform using the following command

    cd fieldtrip/src
    mex meg_leadfield1.c
    mex plgndr.c
    mex read_24bit.c

The following files all depend on some shared code in geometry.c and geometry.h, hence the compilation process is slighty different for thes

    mex -I. -c geometry.c		
    mex -I. -c solid_angle.c ; mex -o solid_angle solid_angle.o geometry.o
    mex -I. -c lmoutr.c      ; mex -o lmoutr      lmoutr.o      geometry.o
    mex -I. -c ptriproj.c    ; mex -o ptriproj    ptriproj.o    geometry.o
    mex -I. -c ltrisect.c    ; mex -o ltrisect    ltrisect.o    geometry.o
    mex -I. -c routlm.c      ; mex -o routlm      routlm.o      geometry.o
    mex -I. -c plinproj.c    ; mex -o plinproj    plinproj.o    geometry.o

If you are on a Windows computer, the compiled object files with have extension .obj instead of .o and hence you then should do 

    mex -I. -c geometry.c
    mex -I. -c solid_angle.c ; mex solid_angle.c solid_angle.obj geometry.obj
    mex -I. -c lmoutr.c      ; mex lmoutr.c      lmoutr.obj      geometry.obj
    mex -I. -c ptriproj.c    ; mex ptriproj.c    ptriproj.obj    geometry.obj
    mex -I. -c ltrisect.c    ; mex ltrisect.c    ltrisect.obj    geometry.obj
    mex -I. -c routlm.c      ; mex routlm.c      routlm.obj      geometry.obj
    mex -I. -c plinproj.c    ; mex plinproj.c    plinproj.obj    geometry.obj

After compilation the mex files are automatically at the right location.

Note that most of the mex files include a m-file wrapper which will try to do an auto compilation. Again, the autocompilation has not (and can not) be tested on all possible platforms, so your mileage may vary. 

If you are using the Visual Studio Compiler and get an error similar t
    error LNK2005: mexFunction already defined in ptriproj.obj
then try this line replacing ptriproj with the file you are trying to compile.
    mex -I. -c ptriproj.c    ; mex ptriproj.c  geometry.obj

Note in Linu
If you are get the error message "cannot find -lstdc++", you can install the libstdc++5 package using your package manager.
If, after the install of libtdc++5, the lstdc++ error persists, just do a symbolic link like

    ln -s /usr/lib64/libstdc++.so.6 /usr/lib64/libstdc++.so 

and it should work.

## Known issues with SPM MEX files and workarounds

Some MEX files have been recompiled but have not been tested on all platform combinations with FieldTrip, and hence are not yet included in the current release. Examples thereof are the MEX files provided by external software packages. Below is a list of currently known issues (January, 2018) and their workarounds, other than recompiling the incompatible MEX files yourself. 

#### SPM8 mexmaci64 MEX files fail on MATLAB 2017 and up

Producing the following error
    Invalid MEX-file '/Users/roboos/matlab/fieldtrip/external/spm8/spm_conv_vol.mexmaci64
    dlopen(/Users/roboos/matlab/fieldtrip/external/spm8/spm_conv_vol.mexmaci64, 6): Library not loaded: @loader_path/libmex.dylib
    Referenced from: /Users/roboos/matlab/fieldtrip/external/spm8/spm_conv_vol.mexmaci64
    Reason: image not found. 

1) You can recompile the SPM8 mex files. A makefile and instructions are provided on https://www.wikibooks.org/wiki/SPM#Installation.

2) You can use the maintenance version of SPM8 which has newer mex files, see https://github.com/spm/spm8/tree/maint
    
3) Mex file issues should be resolved using the latest version of SPM12. You can specify the use of SPM12 at function call
    cfg.spmversion = 'spm12' or 'spm8up'
 
4) For a more permanent solution that applies to all functions from the FieldTrip toolbox, you can set SPM12 as the default version in your startup.m 
   global ft_default
   ft_default.spmversion = 'spm12'
   ft_defaults % this loads the rest of the defaults

#### GIFTI mexmaci64 MEX file on MATLAB 2017 and up

Producing the following error

   Error using read_gifti_file (line 17)
   [GIFTI] Loading of XML file /Users/arjsto/Projects/Ecog/data/IR30/recon/freesurfer/SUMA/std.141.lh.pial.gii failed.

You can replace the xml_findstr.mexmaci64 in external/gifti/@xmltree/private by the version hosted at https://github.com/spm/spm12/blob/master/%40xmltree/private/xml_findstr.mexmaci64
   
