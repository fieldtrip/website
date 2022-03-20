---
title: Code testing and release versions
tags: [development, release]
redirect_from:
  - /development/dashboard/
---

# Code testing and release versions

Daily releases of FieldTrip are made available on the FTP server. The corresponding commits (i.e. point in time in the git repository) are tagged, such that the releases are also [available from GitHub](https://github.com/fieldtrip/fieldtrip/releases). FieldTrip is only released if all tests pass, so on some days there will not be a release.

## Testing the code

The `fieldtrip/test` directory contains many [test scripts](https://github.com/fieldtrip/fieldtrip/tree/master/test) (technically they are functions). We use these initially to reproduce and identifying the cause of a bug, or for designing new end-user scripts that matches some new functionality that we want to implement. Once a reported bug has been fixed and/or the new functionality has been implemented, we keep the test scripts for [regression testing](https://en.wikipedia.org/wiki/Regression_testing).

{% include markup/info %}
If you suspect a problem with the FieldTrip code, the best way to resolve it is to post it on [GitHub](https://github.com/fieldtrip/fieldtrip/issues) and to contribute a (small) test script that helps us to reproduce the problem. These test scripts help us reproduce the problem. After fixing the problem, we add the script to the test directory to ensure future code quality.  
{% include markup/end %}

The [master branch](https://github.com/fieldtrip/fieldtrip/tree/release) is tested every evening; all functions in the test directory are executed using the FieldTrip [dashboard scripts](https://github.com/fieldtrip/dashboard) that are running as a cron job on the [DCCN compute cluster](https://dccn-hpc-wiki.readthedocs.io). If the complete test batch passes, the changes on the master branch are automatically merged into the [release branch](https://github.com/fieldtrip/fieldtrip/tree/release). If there is a problems with one of the test scripts, an email is sent to the main developers and the updates are *not* merged from master into release.

### How to implement algorithmic tests

**Method A:** If possible, the scripts should check against an internal reference solution, i.e., the outcome of the algorithm on particular ideal data is known, therefore the correctness of the algorithm can be tested using simulated data.

**Method B:** If that is not possible or difficult, the scripts should check the consistency of one implementation with another implementation.

**Method C:** If that is also not possible, the result of the algorithm on a particular real-world dataset has to be interpreted as being correct, and that solution should be reused as reference solution (i.e. regression testing).

## Releasing the code

Every evening one of the FieldTrip [automation scripts](https://github.com/fieldtrip/automation) is executed as a cron job. It checks whether there are new commits on the [release branch](https://github.com/fieldtrip/fieldtrip/tree/release), and if so, it makes a new zip file of fieldtrip, fieldtrip-lite, and some of the modules, and copies those to the FTP server. It also tags the corresponding commit on the release branch on GitHub with the date (YYYYMMDD), consistent with the naming of the zip files.

## Adding test scripts

When you [contribute code](/development/contribute), it is good practice to also include a short test script. This helps the maintainers to evaluate your contribution, and in the future to ensure that future changes to code elsewhere do not break your contribution.

When adding a test script, please call them `text_xxx.m` when it can run without user interaction, or `inspect_xxx.m` when user interaction is needed, e.g., judging whether the figure is correct, clicking on a button, or closing a figure to continue the analysis.

Test "scripts" should actually not be MATLAB scripts, but MATLAB functions. They start with `function text_xxx` and take (in general) no input arguments and produce no output arguments. The test can print diagnostic information on screen, but most important is that the test passes or that it fails with an error. You can use the [error](https://nl.mathworks.com/help/matlab/ref/error.html) or the [assert](https://nl.mathworks.com/help/matlab/ref/assert.html) functions.

Test that are execured automatically (i.e. files with the name `test_xxx.m`) MUST include the amount of memory that the execution takes and the duration that the test script runs. This is needed to schedule the test scripts on the Donders compute cluster. The memory should include the amount of memory that MATLAB takes itself (which is about 500MB); it does not have to be very accurate, rounding it off to the nearest GB is fine. The time should include the time that MATLAB itself takes to start (which is about 30-60 seconds), but also the time that it takes to load data, etcetera. Again, there is no reason to make this very tight, if it is too shorrt the execution of the test job might be aborted before it has completed. We suggest using for example 10 or 20 minutes, or 1 or 2 hours.

All test scripts SHOULD if possible include a line that lists the dependencies, i.e. (high- or low-level) FieldTrip functions to which the test script is particularly sensitive. This allows developers to quickly search for existing test scripts and evaluate them whenever they change the specific FieldTrip function. In that way *your* test script helps to ensure that existing functionality does not break.

    % WALLTIME 00:10:00
    % MEM 2gb
    % DEPENDENCY ft_definetrial ft_preprocessing

To link relate scripts to the background information on bug reports and/or online discussions that we have when making changes to the code, test scripts that relate to a bug on <http://bugzilla.fieldtriptoolbox.org/> should be named `text_bugXXX.m`. Test scripts that relate to an issue on <http://github.com/fieldtrip/fieldtrip/issues/> should be named `test_issueXXX.m`, and test script relating to a pull request on <http://github.com/fieldtrip/fieldtrip/pulls/> should be named `test_pullXXX.m`. This allows future contributors to look up the online discussion and details on basis of the file name. Of course you an also add help with additional links inside the test script yourself

For test scripts that read data from disk, it is required that the data files are present on the Donders compute cluster. Usually we store the test data on the network directory `/home/common/matlab/fieldtrip/data/test` (which on the Donders windows desktops is available on `H:\common/matlab\fieldtrip\data\test`) and name the test files or directory according to the GitHub issue or Bugzilla number. To ensure that the test script can find the data both when executed on Linux or on windows, you should use the **[dccnpath](/reference/utilities/dccnpath)** function: when the file can be found in the present working  directory (e.g., on your laptop) it will return that, when MATLAB runs on Windows it will subsequently try to find the file in `H:\common` and when running on Linux it will try `/home/common`.

{% include markup/info %}
Perhaps the best way to learn how to write a test script is by looking at some other random [test scripts](https://github.com/fieldtrip/fieldtrip/tree/master/test) and using them as example.
{% include markup/end %}
