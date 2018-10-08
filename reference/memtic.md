---
layout: default
---

##  MEMTIC

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help memtic".

`<html>``<pre>`
    `<a href=/reference/memtic>``<font color=green>`MEMTIC`</font>``</a>` start a MATLAB memory recorder
 
    `<a href=/reference/memtic>``<font color=green>`MEMTIC`</font>``</a>` and `<a href=/reference/memtoc>``<font color=green>`MEMTOC`</font>``</a>` functions work together to measure memory usage.
    `<a href=/reference/memtic>``<font color=green>`MEMTIC`</font>``</a>`, by itself, saves the current memory footprint that `<a href=/reference/memtoc>``<font color=green>`MEMTOC`</font>``</a>`
    uses later to measure the memory that was used between the two.
 
    Use as
    `<a href=/reference/memtic>``<font color=green>`MEMTIC`</font>``</a>`
    `<a href=/reference/memtoc>``<font color=green>`MEMTOC`</font>``</a>`
    to print the estimated memory use on screen, or
    `<a href=/reference/memtic>``<font color=green>`MEMTIC`</font>``</a>`
    M = `<a href=/reference/memtoc>``<font color=green>`MEMTOC`</font>``</a>`
    to return the estimated memory (in bytes) in variable M, or
    C = `<a href=/reference/memtic>``<font color=green>`MEMTIC`</font>``</a>`
    M = `<a href=/reference/memtoc>``<font color=green>`MEMTOC`</font>``</a>`(C)
    to specifically estimate the memory use between a well-defined tic/toc pair.
 
    Note that MATLAB uses internal memory allocation, garbage collection, shallow
    copies of variables, and virtual memory. Due to the advanced handling of
    memory for its variables, it is not easy and in certain cases not possible to
    make a reliable and reproducible estimate based on the memory information
    provided by the operating system.
 
    Example: measure the memory increase due to allocating a lot of memory.
    Doing a "clear x" following the allocation and priot to `<a href=/reference/memtoc>``<font color=green>`MEMTOC`</font>``</a>` does not
    affect the memory that is reported.
 
    memtic
    n = 125; x = cell(1,n);
    for i=1:n
      x{i} = randn(1000,1000); % 8kB per item
      disp(i);
    end
    whos x
    memtoc
 
    See also TIC, TOC
`</pre>``</html>`

