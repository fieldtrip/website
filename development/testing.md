---
title: Code testing and release versions
tags: [development, release]
redirect_from:
  - /development/dashboard/
---

# Code testing and release versions


## Why testing is important?

FieldTrip is a toolbox with many functions, designed to be compatible with each other. This means that one function often relies on the output of another function. Functions are categorized as [high, low-level, or private](https://www.fieldtriptoolbox.org/development/architecture/#high-level-low-level-and-private-functions), with high-level functions depending on low-level and private functions.

To make sure everything works correctly, we use **testing**. This way, we can be confident that when we add, modify, or remove a function, we won't break the existing ones. Testing also helps us find and fix any issues early on, ensuring that FieldTrip functions smoothly for all users.

## How are the tests organised in FieldTrip?

Once a reported bug has been fixed and/or the new functionality has been implemented, we keep the test scripts for [regression testing](https://en.wikipedia.org/wiki/Regression_testing).

All the test scripts (technically they are functions) are located in [`fieldtrip/test` directory](https://github.com/fieldtrip/fieldtrip/tree/master/test). Tests are called as `test_xxx.m` when they can run without user interaction, or `inspect_xxx.m` when user interaction is needed, e.g., judging whether the figure is correct, clicking on a button, or closing a figure to continue the analysis.

The test scripts are further split into tests related to bugs, issues or pull requests, tests related to a FieldTrip function, tests related to example, tutorial pipelines and failed-obsolete tests:

### Tests related to bugs, issues or pull requests

To link related scripts to the background information on bug reports and/or online discussions that we have when making changes to the code, test scripts that relate to a bug on <http://bugzilla.fieldtriptoolbox.org/> are named as `text_bugXXX.m`. Test scripts that relate to an issue on <https://github.com/fieldtrip/fieldtrip/issues/> are named as `test_issueXXX.m`, and test script that relate to a pull request on <https://github.com/fieldtrip/fieldtrip/pulls/> are named as `test_pullXXX.m`. Where `XXX` is the reference number of the bug, issue or pull request. This allows future contributors to look up the online discussion and details on basis of the file name. Of course you can also add help with additional links inside the test script yourself.


{% include markup/info %}
If you suspect a problem with the FieldTrip code, the best way to resolve it is to post it on [GitHub as an issue](https://github.com/fieldtrip/fieldtrip/issues) and to contribute a (small) test script that helps us to reproduce the problem. After fixing the problem, we add the script to the test directory to ensure future code quality. More information on that topic is provided in the [reporting issues](https://www.fieldtriptoolbox.org/development/issues/) FieldTrip webpage.
{% include markup/end %}

### Tests related to a FieldTrip function

Test scripts that relate to [a specific FieldTrip function](https://www.fieldtriptoolbox.org/reference/) are named as `test_ft_xxx`.

### Tests related to example and tutorial pipelines

Example pipelines used by researchers when they perform their own data analysis and the tutorial pipelines provided in the [FieldTrip website](https://www.fieldtriptoolbox.org/tutorial/) are also provided as test scripts. They are named as `test_example_xxx` and `test_tutorial_xxx` respectively.

### Failed and obsolete tests

The directory `fieldtrip/test/invalid` has the failed and obsolete tests. The failed tests usually relate to bugs that could not be fixed and obsolete tests to tests that are not important anymore for the development of FieldTrip. This directory exists for historical reasons and the tests that it includes are not used anymore.

### List of dependencies

In the beginning of each test script a list of dependencies is provided. This helps to select an appropriate subset of tests to run based on:
1. **WALLTIME**: The duration that a test needs to run. This duration is usually more than the actual duration needed since it also includes the time that MATLAB itself takes to start (which is about 30-60 seconds) and the time that it takes to load the test data.
2. **MEM**: MEM stands for memory, and it represents the amount of memory required for a test to run.
3. **DEPENDENCY**: The dependencies, i.e. high- or low-level FieldTrip functions to which the test script is particularly sensitive.
4. **DATA**: The type of data that the test requires to run. More specifically, ``DATA no`` means that the test doesn't need any data to run since it uses simulated data. ``DATA public`` means that the test needs data that are available in the [WebDAV download server](https://download.fieldtriptoolbox.org/) of FieldTrip. ``DATA private`` means that the test needs data that are not publicly accesible and hence only available to users that have connection to the [DCCN intranet](https://intranet.donders.ru.nl/).

An example is of a list of dependencies provided in the beginning of each test script is: 

    % WALLTIME 00:10:00
    % MEM 2gb
    % DEPENDENCY ft_definetrial ft_preprocessing
    % DATA no / DATA private / DATA public



## Testing guidelines to external contributors

{% include markup/info %}
When you add, modify, or remove a FieldTrip function, it is strongly recommended that you first run the relevant test scripts to your local computer. If all the test scripts pass, only then you should submit a [pull request](https://github.com/fieldtrip/fieldtrip/pulls). Please note that test scripts that include ``DATA no`` and ``DATA public`` can be run by every user.
{% include markup/end %} 

When you contribute code to FieldTrip, you should select to run on your local computer only a subset of test scripts that are relevant to your contribution. To help you with that we provide two functions: **[dccnpath](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/dccnpath.m)** and **[ft_test](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_test.m)**.

### How **[dccnpath](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/dccnpath.m)** works?

For test scripts that read data from disk, it is required that the data files are present on the Donders computer cluster. There are two types of test data: the private and the public test data.  

The private test data is stored in the network directory `/home/common/matlab/fieldtrip/data/test` (which on the Donders Windows desktops is available on `H:\common\matlab\fieldtrip\data\test`). The private test data is only available to users that have connection to the [DCCN intranet](https://intranet.donders.ru.nl/).

The public test data is stored in the network directory `/home/common/matlab/fieldtrip/data/ftp` (which on the Donders Windows desktops is available on `H:\common\matlab\fieldtrip\data\ftp`). The public test data is available to all the users through the [WebDAV download server](https://download.fieldtriptoolbox.org/) of FieldTrip.

{% include markup/info %}
It is important to keep in mind that the test files or directories related to a  GitHub issue or Bugzilla report are named after the GitHub issue or Bugzilla number.
{% include markup/end %}

**[dccnpath](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/dccnpath.m)** function is included in all the test scripts that use test data (i.e., test scripts that include in their dependency list ``DATA private`` and ``DATA public``) and ensures every user has the correct path to the test data. More specifically, it takes as **input** the path to where the test data are downloaded in the DCCN computer cluster, e.g., ``/home/common/matlab/fieldtrip/data/test`` for private data or ``/home/common/matlab/fieldtrip/data/ftp`` for public data. And it **outputs** the corresponding path to these input test data, for the DCCN computer cluster, a local computer with connection to the [DCCN intranet](https://intranet.donders.ru.nl/) or a local computer with no connection to the [DCCN intranet](https://intranet.donders.ru.nl/). **[dccnpath](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/dccnpath.m)** works for Windows, Mac and Linux.

For users that work in the DCCN computer cluster the **[dccnpath](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/dccnpath.m)** output is `/home/common/matlab/fieldtrip` (Linux, Mac) or `H:\common\matlab\fieldtrip` (Windows). For users that use their own computer when the file can be found in the present working directory **[dccnpath](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/dccnpath.m)** will return that working directory. For example, when MATLAB runs on Windows it will try to find the file in `H:\common` and when running on Linux or Mac it will try `/home/common`. If the file can't be found in the present working directory then **[dccnpath](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/dccnpath.m)** will automatically download **public** test data in the local computer from the [WebDAV download server](https://download.fieldtriptoolbox.org/) of FieldTrip, if they are not already downloaded. More specifically, if the user defines
    
    global ft_default
    ft_default.dccnpath='path/to/local/copy'

 
then the test data will be downloaded inside ``path/to/local/copy``, if they are not already downloaded there.

If the user **doesn't** define
    
    global ft_default
    ft_default.dccnpath='path/to/local/copy'
    
then the test data will automatically be downloaded in the **temporary directory**, if they are not already downloaded there.



###  How **[ft_test](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_test.m)** works?

When you want to contribute by modifying or removing a pre-existing FieldTrip function you should use **[ft_test](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_test.m)**. The function **[ft_test](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_test.m)** selects and runs a **subset** of test scripts based on the inputs given by the contributor. The inputs given by the contributor can be the maximum memory and duration that the tests will take to run in the local computer, the FieldTrip functions that the test depends on and the data usage (i.e., no, public or private data). In the end, **[ft_test](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_test.m)** will print a list of the tests that failed (if any) and need to be manually inspected.

For example, a contributor modified **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/master/ft_preprocessing.m)** by adding a new functionality. Now he/she has to run the corresponding test scripts to ensure that after this modification the pre-existing FieldTrip functionality does not break. He has to run **[ft_test](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/ft_test.m)** with inputs:

    ft_test dependency ft_preprocessing data no data public

In this case the contributor doesn't give any inputs about the maximum memory and duration that the tests will need to run in his/her computer.


{% include markup/info %}
The DCCN computer cluster and a local computer with connection to the [DCCN intranet](https://intranet.donders.ru.nl/) can run all the tests that are labeled as ``DATA no``, ``DATA public`` and ``DATA private``. On the other hand, a local computer with **no** connection to the [DCCN intranet](https://intranet.donders.ru.nl/) can only run tests labeled as ``DATA no`` and ``DATA public``.
{% include markup/end %}
 


## Adding a new test script 

When you [contribute code](https://www.fieldtriptoolbox.org/development/contribute/), it is good practice to also include a short test script. This helps the maintainers to evaluate your contribution, and in the future to ensure that future changes to code elsewhere do not break your contribution.

Test "scripts" should actually not be MATLAB scripts, but MATLAB functions. They start with `function test_xxx` and take (in general) no input arguments and produce no output arguments. The test can print diagnostic information on screen, but most important is that the test passes or that it fails with an error. You can use the [error](https://nl.mathworks.com/help/matlab/ref/error.html) or the [assert](https://nl.mathworks.com/help/matlab/ref/assert.html) functions.


### How to name the new test scripts

When adding a test script, please call them `test_xxx.m` when it can run without user interaction, or `inspect_xxx.m` when user interaction is needed, e.g., judging whether the figure is correct, clicking on a button, or closing a figure to continue the analysis.

To link related scripts to the background information on bug reports and/or online discussions that we have when making changes to the code, test scripts that relate to a bug on <http://bugzilla.fieldtriptoolbox.org/> should be named `text_bugXXX.m`. Test scripts that relate to an issue on <https://github.com/fieldtrip/fieldtrip/issues/> should be named `test_issueXXX.m`, and test script relating to a pull request on <https://github.com/fieldtrip/fieldtrip/pulls/> should be named `test_pullXXX.m`. This allows future contributors to look up the online discussion and details on basis of the file name. Of course you can also add help with additional links inside the test script yourself.

### How to implement algorithmic tests

Tests that need to load test data should include **[dccnpath](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/dccnpath.m)** to ensure that every user has the correct path to the test data. Also, when you create a new test script you should always include a **list of dependencies** in the beginning of the script. For instance:

    % WALLTIME 00:10:00
    % MEM 2gb
    % DEPENDENCY ft_definetrial ft_preprocessing
    % DATA no / DATA private / DATA public

 
Regarding the list of dependencies:

#### Memory & Walltime

Test that are execured automatically (i.e. files with the name `test_xxx.m`) MUST include the **amount of memory** that the execution takes and the **duration** that the test script runs. This is needed to schedule the test scripts on the Donders compute cluster. The memory should include the amount of memory that MATLAB takes itself (which is about 500MB); it does not have to be very accurate, rounding it off to the nearest GB is fine. The time should include the time that MATLAB itself takes to start (which is about 30-60 seconds), but also the time that it takes to load data, etcetera. Again, there is no reason to make this very tight, if it is too short the execution of the test job might be aborted before it has completed. We suggest using for example 10 or 20 minutes, or 1 or 2 hours.

#### Dependency on other FieldTrip functions 

All test scripts SHOULD if possible include a line that lists the **dependencies**, i.e. (high- or low-level) FieldTrip functions to which the test script is particularly sensitive. This allows developers to quickly search for existing test scripts and evaluate them whenever they change the specific FieldTrip function. In that way *your* test script helps to ensure that existing functionality does not break.

#### Data usage

**Method A:** If possible, the scripts should check against an internal reference solution, i.e., the outcome of the algorithm on particular ideal data is known, therefore the correctness of the algorithm can be tested using *simulated data*. In this case you should include ``DATA no`` in your list of dependencies.

**Method B:** If that is not possible or difficult, the scripts should check the consistency of one implementation with another implementation.

**Method C:** If that is also not possible, the result of the algorithm on a particular *real-world dataset* has to be interpreted as being correct, and that solution should be reused as reference solution (i.e. regression testing). If the *real-world dataset* is publicly accessible, you should include ``DATA public`` in your list of dependencies. On the other hand, if the dataset is not publicly accessible, you should include ``DATA private`` in your list of dependencies.



{% include markup/info %}
Perhaps the best way to learn how to write a test script is by looking at some other random [test scripts](https://github.com/fieldtrip/fieldtrip/tree/master/test) and using them as example.
{% include markup/end %}





## Testing and releasing the code in the DCCN

Except for the testing done by every contributor separately, **all** the test scripts are executed in the DCCN computer cluster every evening. Daily releases of FieldTrip are made available on the download server. The corresponding commits (i.e. point in time in the git repository) are tagged, such that the releases are also [available from GitHub](https://github.com/fieldtrip/fieldtrip/releases). **FieldTrip is released only if all tests pass**. So, on some days there will not be a release.

### Testing
The [master branch](https://github.com/fieldtrip/fieldtrip/tree/master) is tested every evening; all functions in the test directory are executed using the FieldTrip [dashboard scripts](https://github.com/fieldtrip/dashboard) that are running as a cron job on the [DCCN compute cluster](https://dccn-hpc-wiki.readthedocs.io). If the complete test batch passes, the changes on the master branch are automatically merged into the [release branch](https://github.com/fieldtrip/fieldtrip/tree/release). If there is a problems with one of the test scripts, an email is sent to the main developers and the updates are *not* merged from master into release.

### Releasing
Every evening one of the FieldTrip [automation scripts](https://github.com/fieldtrip/automation) is executed as a cron job. It checks whether there are new commits on the [release branch](https://github.com/fieldtrip/fieldtrip/tree/release), and if so, it makes a new zip file of fieldtrip, fieldtrip-lite, and some of the modules, and copies those to the FTP server. It also tags the corresponding commit on the release branch on GitHub with the date (YYYYMMDD), consistent with the naming of the zip files.