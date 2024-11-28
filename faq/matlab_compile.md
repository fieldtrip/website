---
title: How to compile MATLAB code into stand-alone executables?
category: faq
tags: [qsub]
redirect_from:
    - /faq/how_to_compile_matlab_code_into_stand-alone_executables/
---

# How to compile MATLAB code into stand-alone executables?

Using **[qsubcellfun](/reference/qsub/qsubcellfun)** and/or **[qsubcompile](/reference/qsub/qsubcompile)** it is possible to compile your jobs prior to submitting them to the cluster batch queuing system. These compiled jobs do not require a MATLAB license for execution at run-time. The compilation itself (which is done once per batch) does require that you have a license for the [MATLAB compiler](http://www.mathworks.com/products/compiler) on the computer from which you are submitting the jobs. Furthermore, it requires that the MCR is installed on the cluster worker nodes.

When compiling your qsub jobs, or when compiling MATLAB code in general, you might run into some issues that have to do with the compile process. This page tries to list the problems that you might expect and the solutions.

## Using addpath in your startup

The compiled application includes all code that it requires to run and cannot incorporate MATLAB functions or scripts that were not compiled into the application. Consequently, you cannot use the addpath MATLAB command to extend the search path.

A common use is to have a "startup.m" script in which the path is set. If present, your startup.m will be compiled into your application. The "isdeployed" MATLAB command can be used to exclude a part (or the complete) startup.m from being executed within your compiled application. So instead of

    addpath /home/common/matlab/fieldtrip
    addpath /home/common/matlab/spm12
    ft_defaults

you should change your startup.m into

    if ~isdeployed
    addpath /home/common/matlab/fieldtrip
    addpath /home/common/matlab/spm12
    ft_defaults
    end
