---
title: Code testing and release
tags: [development]
---

# Code testing and release

Daily releases of FieldTrip are made available on the FTP server. The corresponding commits (i.e. point in time in the git repository) are tagged, such that the releases are also [available from GitHub](https://github.com/fieldtrip/fieldtrip/releases). FieldTrip is only released if all tests pass, so on some days there will not be a release.

## Testing the code

The `fieldtrip/test` directory contains many [test scripts](https://github.com/fieldtrip/fieldtrip/tree/master/test) (technically they are functions). We use these initially to reproduce and identifying the cause of a bug, or for designing new end-user scripts that matches some new functionality that we want to implement. Once a reported bug has been fixed and/or the new functionality has been implemented, we keep the test scripts for [regression testing](https://en.wikipedia.org/wiki/Regression_testing).

{% include markup/info %}
If you suspect a problem with the FieldTrip code, the best way to resolve it is to post it on [GitHub](https://github.com/fieldtrip/fieldtrip/issues) and to contribute a (small) test script that helps us to reproduce the problem. These test scripts help us reproduce the problem. After fixing the problem, we add the script to the test directory to ensure future code quality.  
{% include markup/end %}

The [master branch](https://github.com/fieldtrip/fieldtrip/tree/release) is tested every evening; all functions in the test directory are executed using the FieldTrip [dashboard scripts](https://github.com/fieldtrip/dashboard) that are running as a cron job on the [DCCN compute cluster](https://dccn-hpc-wiki.readthedocs.io). If the complete test batch passes, the changes on the master branch are automatically merged into the [release branch](https://github.com/fieldtrip/fieldtrip/tree/release). If there is a problems with one of the test scripts, an email is sent to the main developers and the updates are *not* merged from master into release.

## Releasing the code

Every evening one of the FieldTrip [automation scripts](https://github.com/fieldtrip/automation) is executed as a cron job. It checks whether there are new commits on the [release branch](https://github.com/fieldtrip/fieldtrip/tree/release), and if so, it makes a new zip file of fieldtrip, fieldtrip-lite, and some of the modules, and copies those to the FTP server. It also tags the corresponding commit on the release branch on GitHub with the date (YYYYMMDD), consistent with the naming of the zip files.

## Running the tests yourself

You can simply execute the tests that don't rely on data on our network share. You can also run them using the **[ft_test](/reference/ft_test)** function like this

    ft_test run test_bug46

When using `ft_test`, the results are stored (together with details on the MATLAB version and operating system) in the dashboard database. You can query previous results of the tests using the **[ft_test](/reference/ft_test)** function like this

    ft_test report test_bug46

to get the results of a specific test script, or

    ft_test report test_bug46 matlabversion 2017b

to get the results of a specific test script for a specific MATLAB version, or

    ft_test report matlabversion 2012b arch maci64

to get the results of all tests with a specific MATLAB version and on a specific platform.
