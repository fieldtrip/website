---
title: Making a memory efficient analysis pipeline
category: tutorial
tags: [matlab, script, memory]
redirect_from:
    - /tutorial/memory/
---

# Making a memory efficient analysis pipeline

{% include markup/yellow %}
If you are new to FieldTrip, we recommend that you skip this tutorial for now. You can read the [introduction tutorial](/tutorial/intro/introduction) and then move on with the tutorials on [preprocessing](/tutorial/#reading-and-preprocessing-data). Once you get the hang of it, you can return to this tutorial which is more on the technical and coding aspects.
{% include markup/end %}

## Introduction

This tutorial gives advice about how to do data analysis in a memory-efficient way when large amount of data is analyzed. It does not provide information about any FieldTrip functions or any analysis steps.

## Background

Neurophysiological data can become quite large with the result that disk space, RAM and processing time can become compromised. It is important to pay attention on how much memory is used because a non-efficient analysis can result in "out of memory" errors in MATLAB. However, how to program MATLAB in a memory-efficient way is also not always obvious. Some common issues are discussed below.

## Memory efficient coding tips

- Work on your programming _style_. Take a look [here](http://www.datatool.com/downloads/matlab_style_guidelines.pdf) for a concise summary of the recommended style of programming.
- Downsample your data (but backup your original data), e.g., using **[ft_resampledata](/reference/ft_resampledata)**
- Change data to single-precision (after preprocessing by using **[ft_struct2single](/reference/utilities/ft_struct2single)** or by using `cfg.precision='single'` in certain functions)
- Check if you really have to `cfg.keeptrials='yes'` in **[ft_freqanalysis](/reference/ft_freqanalysis)**.
- If you are working on a single subject, make sure other subjects are no longer in memory. This might seem trivial, but many people assign unique variables to subjects and forget to clear them.
- Perhaps most importantly – once in a while let someone else go through your scripts to see if they can be optimized.
- Within a script or function make sure you clear large variables that you don't need anymore using the clear statement. Note that MATLAB's memory use might not be intuitive. For instance, reloading a large dataset into the same variable may result in MATLAB allocating twice the memory you actually need.
- The `cfg` field in your FieldTrip data structures stores the history of the processing steps performed on the data. This field can get quite large after many such steps and specifically after appending several data structures, because each `cfg` is stored in a cell array within the `cfg.previous` field. You can look at the cfg using **[ft_analysispipeline](/reference/ft_analysispipeline)**. Simply emptying this field (e.g., by doing `freq.cfg = []`) will free up space. Remember to keep a copy of the cfg field on disk if you want to keep track of your analysis pipeline.

## Save your data to disk

Remember to always backup your original data that was acquired on external hard disks, CDs or DVDs for long-term storage. If possible, the backup should include the presentation code that was used in the experiment and a small ASCII .txt file with the recording details.

When using FieldTrip for large analyses, it is recommended to save one MATLAB variable to a single file. That will result in a lot of files in your data directory and in first instance you may consider that to look messy. However, the advantage is that you can easily manage the data, delete results that you don't need any more, check that the results are complete for all subjects, check that the timestamps of the files with certain results are consistent for all subjects (e.g., after you have updated some parameters and rerun part of the analysis), ...

When writing intermediate results, consider if you really need to save all intermediate steps in your analysis pipeline. For instance with MEG data it might not take that much time to calculate your planar gradient. It will save you a lot of disk space if you only have to write your axial data to disk. When using a high sampling frequency during acquisition, you may be able to downsample your data to save disk space and speed up all subsequent processing steps.

Do make sure you save the important parameters (e.g., rejected trials) so you can always rerun your script. Subject specific information should be added to the subject-specific script.

## Load only as much data as you need

Only import into MATLAB as much of a large data set as you need for the problem you are trying to solve. Many users are tempted to try and load the entire file first, and then process it with MATLAB. This is not always necessary. Use the `whos` function with the `-file` option to preview the file. This command displays each array in the MAT-file that you specify and the number of bytes in the array.

    >> whos -file session1.mat
    
    Name      Size            Bytes  Class     Attributes
    S2        1x1               723  struct
    x         100x200            72  double    sparse
    Mat4      4x20              640  double
    A         3151872x1     3151872  uint8
    Seq       1x912211       912211  int8

If there are large arrays in the MAT-file that you do not need for your current task, you can selectively import only those variables that you want using load, for instance:

    seq = load('session1.mat','A').

## Avoid creating temporary arrays

Avoid creating large temporary variables, and also make it a practice to clear those temporary variables you do use when they are no longer needed. For example, when you create a large array of zeros, instead of saving to a temporary variable A, and then converting A to a single

    A = zeros(1e6,1);
    As = single(A);

use just the one command to do both operation

    A = zeros(1e6,1,'single');

Using the repmat function, array preallocation and for loops are other ways to work on nondouble data without requiring temporary storage in memory.

## Use nested functions to pass fewer arguments

When working with large data sets, be aware that MATLAB makes a temporary copy of an input variable if the called function modifies its value. This temporarily doubles the memory required to store the array.
One way to use less memory in this situation is to use nested functions. A nested function shares the workspace of all outer functions, giving the nested function access to data outside of its usual scope. In the example shown here, nested function setrowval has direct access to the workspace of the outer function myfun, making it unnecessary to pass a copy of the variable in the function call. When setrowval modifies the value of A, it modifies it in the workspace of the calling function. There is no need to use additional memory to hold a separate array for the function being called, and there also is no need to return the modified value of A.

    function myfun
    A = magic(500);
      function setrowval(row, value)
        A(row,:) = value;
      end
    setrowval(400, 0);
    disp('The new value of A(399:401,1:10) is')
    A(399:401,1:10)
    end % function

## Using Appropriate Data Storage

MATLAB provides you with different sizes of data classes, such as double and uint8, so you do not need to use large classes to store your smaller segments of data. For example, it takes 7,000 KB less memory to store 1,000 small unsigned integer values using the uint8 class than it does with double.

## Preallocate contiguous memory when creating arrays

In the course of a MATLAB session, memory can become fragmented due to dynamic memory allocation and deallocation. For and while loops that incrementally increase the size of a data structure each time through the loop can add to this fragmentation as they have to repeatedly find and allocate larger blocks of memory to store the data. When memory is fragmented, there may be plenty of free space, but not enough contiguous memory to store a new large variable.

To make more efficient use of your memory, preallocate a block of memory large enough to hold the matrix at its final size before entering the loop. When you preallocate memory for an array, MATLAB reserves sufficient contiguous space for the entire full-size array at the beginning of the computation. Once you have this space, you can add elements to the array without having to continually allocate new space for it in memory.

The following code creates a scalar variable x, and then gradually increases the size of x in a for loop instead of preallocating the required amount of memory at the start.

    x = 0;
    for k = 2:1000
      x(k) = x(k-1) + 5;
    end

Change the first line to preallocate a 1-by-1000 block of memory for x initialized to zero. This time there is no need to repeatedly reallocate memory and move data as more values are assigned to x in the loop.

    x = zeros(1, 1000);
    for k = 2:1000
     x(k) = x(k-1) + 5;
    end

## Clear old variables from memory when no longer needed

When you are working with a very large data set repeatedly or interactively, clear the old variable first to make space for the new variable. Otherwise, MATLAB requires temporary storage of equal size before overriding the variable. For example,

    a = rand(100e6,1) % 800 MB array
    a = rand(100e6,1) % New 800 MB array
    ??? Error using ==> rand
    Out of memory. Type HELP MEMORY for your options.

    clear a
    a = rand(100e6,1)              % New 800 MB array

## Summary and suggested further reading

This tutorial gave some advice for scripting your analysis in a memory-efficient way. We also advise to read this [technical note](http://www.mathworks.com/support/tech-notes/1100/1106.html) from MathWorks. Further suggestions for computational efficiency are given in the tutorial on distributed computing using [qsub](/tutorial/scripting/distributedcomputing_qsub) and [parfor](/tutorial/scripting/distributedcomputing_parfor).

These are FAQs that are related to memory issues:

{% include seealso category="faq" tag1="memory" %}
