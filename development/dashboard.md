---
title: Dashboard
tags: [development]
---

# Dashboard

We use the FieldTrip dashboard for testing the FieldTrip code. The `fieldtrip/test` directory contains many [test scripts](https://github.com/fieldtrip/fieldtrip/tree/master/test) (technically they are functions). We use these initially to reproduce and identifying the cause of a bug, or for designing new end-user scripts that matches some new functionality that we want to implement. Once a reported bug has been fixed and/or the new functionality has been implemented, we keep the test scripts for [regression testing](https://en.wikipedia.org/wiki/Regression_testing).

{% include markup/info %}
If you suspect a problem with the FieldTrip code, the best way to resolve it is to post it on [GitHub](https://github.com/fieldtrip/fieldtrip/issues) and to contribute a (small) test script that helps us to reproduce the problem. These test scripts help us reproduce the problem. After fixing the problem, we add the script to the test directory to ensure future code quality.  
{% include markup/end %}

## Executing the tests

All functions in the test directory are executed regularly using the FieldTrip [dashboard scripts](https://github.com/fieldtrip/dashboard) that are running as a cron job on the [DCCN compute cluster](https://dccn-hpc-wiki.readthedocs.io). If there are problems with one of the test scripts, an email is sent to the main developers.

You can also run (some of) the tests yourself using the **[ft_test](/reference/ft_test)** function like this

    ft_test run test_bug46

## Results of the tests

You can check the results of the test scripts yourself using the **[ft_test](/reference/ft_test)** function like this

    ft_test report test_bug46

to get the results of a specific test script, or

    ft_test report test_bug46 matlabversion 2017b

to get the results of a specific test script for a specific MATLAB version, or

    ft_test report matlabversion 2012b arch maci64

to get the results of all tests with a specific MATLAB version and on a specific platform.
