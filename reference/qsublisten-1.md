---
title: qsublisten
---
```
 QSUBLISTEN checks whether jobs, submitted by qsubfeval, have been
 completed. Whenever a job returns, it executes the provided callback function
 (should be a function handle), with the job ID as an input argument. Results
 can then be retrieved by calling QSUBGET. If a cell-array is provided as
 a the 'filter' option (see below), the second input argument passed to the
 callback function will be an index into this cell-array (to facilitate
 checking which job returned in the callback function).

 Note that this function is blocking; i.e., it only returns after a
 certain criterion has been met.

 Arguments can be supplied with key-value pairs:
     maxnum      = maximum number of jobs to collect, function will return
                   after this is reached. Default = Inf; so it is highly
                   recommended you provide something here, since with
                   maxnum=Inf the function will never return.
     filter      = regular expression filter for job IDs to respond to.
                   The default tests for jobs generated from the current
                   MATLAB process. A cell-array of strings can be
                   provided; in that case, exact match is required.
     sleep       = number of seconds to sleep between checks (default=0)

 This function returns the number of jobs that were collected and for
 which the callback function was called.
```
