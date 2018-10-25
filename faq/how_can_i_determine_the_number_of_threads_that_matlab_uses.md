---
title: How can I determine the number of threads that MATLAB uses?
layout: default
tags: [faq, peer, matlab]
---

## How can I determine the number of threads that MATLAB uses?

In MATLAB versions up to 7.7 (2008b) you can determine the maximum number of threads that it can use with

    N = maxNumCompThreads
    LASTN = maxNumCompThreads(N)
    LASTN = maxNumCompThreads('automatic') 

In MATLAB versions 7.8 and onward, the maxNumCompThreads function is not supported any more. Instead, you can tell MATLAB that it should use a single thread at startup by providing the -singleCompThread to the smartup command, e.g. 

    matlab78 -nodesktop -singleCompThread 

See http://www.mathworks.com/access/helpdesk/help/techdoc/ref/maxnumcompthreads.html for more details.
