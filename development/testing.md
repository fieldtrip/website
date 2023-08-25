---
title: Testing
tags: [development, testing, release]
redirect_from:
  - /development/dashboard/
---

# Testing

## Why is testing important?

FieldTrip is a toolbox with many functions, designed to be compatible with each other. This means that one function often relies on the output of another function. Functions are categorized as [high, low-level, or private](https://www.fieldtriptoolbox.org/development/architecture/#high-level-low-level-and-private-functions), with high-level functions depending on low-level and private functions.

To make sure everything works correctly, we use [regression testing](https://en.wikipedia.org/wiki/Regression_testing). This way, we can be confident that when we add, modify, or remove a function, we won't break the existing ones. Testing also helps us find and fix any issues early on, ensuring that FieldTrip functions smoothly for all users. We use nightly testing as part of the [release](/development/release) procedure.

## How are the tests organized in FieldTrip?

All the test scripts (technically they are functions) are located in [`fieldtrip/test` directory](https://github.com/fieldtrip/fieldtrip/tree/master/test). Tests are called as `test_xxx.m` when they can run without user interaction, or `inspect_xxx.m` when user interaction is needed, e.g., judging whether the figure is correct, clicking on a button, or closing a figure to continue the analysis.

The test scripts are further split into [unit tests](https://en.wikipedia.org/wiki/Unit_testing) related to specific FieldTrip function, tests related to tutorial and example documentation on the website, and tests related to bugs, issues or pull requests.

### Tests related to a FieldTrip function

Test scripts that relate to a specific FieldTrip function are commonly named `test_ft_xxx`, where `ft_xxx` is the function being tested. We try to make these tests exhaustive, so that they go over as many options as possible.

### Tests related to example and tutorial pipelines

Analysis scripts used by researchers are often based on the [tutorial](/tutorial) and [example](/example) documentation on the website. We test these with `test_example_xxx` and `test_tutorial_xxx` respectively. To ensure that new versions of FieldTrip remain compatible with existing scripts from users that were based on older tutorial documentation, we keep old versions of these test scripts.

### Tests related to bugs, issues or pull requests

To link related scripts to the background information on bug reports and/or online discussions that we have when making changes to the code, test scripts that relate to a bug on <http://bugzilla.fieldtriptoolbox.org/> are named as `text_bugXXX`, test scripts that relate to an issue on <https://github.com/fieldtrip/fieldtrip/issues/> are named as `test_issueXXX`, and test script that relate to a pull request on <https://github.com/fieldtrip/fieldtrip/pulls/> are named as `test_pullXXX`, where `XXX` is the number of the bug, issue or pull request. This allows everyone to look up the initial report and the follow-up discussion.

{% include markup/info %}
If you suspect a problem with the FieldTrip code, the best way to resolve it is to post it on [GitHub as an issue](https://github.com/fieldtrip/fieldtrip/issues) and to contribute a (small) test script that helps us to reproduce the problem. After fixing the problem, we then add the script to the test directory to ensure future code quality. More information on that topic is provided in the [reporting issues](/development/issues) FieldTrip webpage.
{% include markup/end %}

{% include markup/info %}
It is important to keep in mind that the test files or directories related to a GitHub issue or Bugzilla report are named after the GitHub issue or Bugzilla number.
{% include markup/end %}

### Failed and obsolete tests

The directory `fieldtrip/test/invalid` contains failed and obsolete tests. These usually relate to bugs that were hard to reproduce and/or could not be fixed directly, and to obsolete tests for functionality that is not important anymore. This directory exists for historical reasons and the tests that it includes are not considered for automatic execution.

### Requirements and dependencies

In the beginning of each test script a list of dependencies is provided. This helps to select an appropriate subset of tests to run based on:
1. **WALLTIME**: The duration that a test needs to run. This duration is usually more than the actual duration needed since it also includes the time that MATLAB itself takes to start (which is about 30-60 seconds) and the time that it takes to load the test data.
2. **MEM**: MEM stands for memory, and it represents the amount of memory required for a test to run.
3. **DATA**: The external data that the test requires to run. More specifically, `DATA no` means that the test doesn't need any external data to run. `DATA public` means it needs data available from the [download server](https://download.fieldtriptoolbox.org/). `DATA private` means that it needs data that are not publicly accessible but only to people working in the DCCN.
4. **DEPENDENCY**: The dependencies, i.e. high- or low-level FieldTrip functions to which the test script is particularly sensitive.

An example of the requirements and dependencies is:

    % WALLTIME 00:10:00
    % MEM 2gb
    % DATA no
    % DEPENDENCY ft_definetrial ft_preprocessing

## Running existing tests

Running a FieldTrip test is as easy as writing the name of the test in the command line. For example, to run one of the tests, you would type:

    test_bug103

More background information about this test and others that are named `test_bugXXX` can be found on [bugzilla](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=103). Tests that are named `test_issueXXX` have more information in a [GitHub issue](https://github.com/fieldtrip/fieldtrip/issues), and those named `test_pullXXX` have more information in a [GitHub pull request](https://github.com/fieldtrip/fieldtrip/pull).

## Finding tests

When you modify or remove pre-existing code, you should find the necessary [test scripts](https://github.com/fieldtrip/fieldtrip/tree/master/test) and run them on your local computer. Note that these test scripts are also included in your own `fieldtrip/test` directory.

For example, let's say you made a modification to the **[ft_preprocessing](/ft_preprocessing)** function. You can list all test scripts together with their list of requirements and dependencies in a [MATLAB table](https://nl.mathworks.com/help/matlab/ref/table.html):

    % find your copy of FieldTrip
    [ftver, ftpath] = ft_version;
    
    % list all m-files in the test directory
    d = dir(fullfile(ftpath, 'test', 'test_*.m'));
    
    name        = cell(numel(d), 1);
    walltime    = cell(numel(d), 1);
    mem         = cell(numel(d), 1);
    data        = cell(numel(d), 1);
    dependency  = cell(numel(d), 1);
    skip        = false(numel(d), 1);

    for i=1:numel(d)
      lines  = readlines(fullfile(d(i).folder, d(i).name));

      line1 = find(startsWith(lines, '% WALLTIME'));
      line2 = find(startsWith(lines, '% MEM'));
      line3 = find(startsWith(lines, '% DATA'));
      line4 = find(startsWith(lines, '% DEPENDENCY'));

      if length(line1)==1 && length(line2)==1 && length(line3)==1 && length(line4)==1
        name{i}        = d(i).name(1:end-2); % remove the .m
        walltime{i}    = lines{line1}(length('% WALLTIME ')+1:end);
        mem{i}         = lines{line2}(length('% MEM ')+1:end);
        data{i}        = lines{line3}(length('% DATA ')+1:end);
        dependency{i}  = lines{line4}(length('% DEPENDENCY ')+1:end);
      else
        % something is wrong
        skip(i) = true;
      end
    end % for all files

    test = table(name, walltime, mem, data, dependency);

    % continue with the ones that specify the WALLTIME, MEG, DATA and DEPENDENCY
    filtered_test = test(~skip,:);

You can then select the tests that for example depend on `ft_preprocessing`.
    
    keepRows = contains(test.dependency, 'ft_preprocessing');
    filtered_test = filtered_test(keepRows, :)

If you are an external contributor outside the DCCN network, you can only run tests that use publicly available data or that do not use data. In that case you have to remove the test scripts that require private data:

    keepRows = ~strcmp(filtered_test.data, 'private');
    filtered_test = filtered_test(keepRows, :)

To quickly find errors, it can be more efficient to run the short and small tests first. You can sort the tests with increasing walltime and memory:

    filtered_test = sortrows(filtered_test, 'walltime', 'ascend');
    filtered_test = sortrows(filtered_test, 'mem',      'ascend');

To run the first 10 tests, you can do:

    for i=1:10
        fprintf('\n ------------------------ \n');
        fprintf('Running test: %s \n\n', filtered_test.name{i})
        eval(filtered_test.name{i});
    end

## Extending existing tests

Test scripts validate specific functionality that is used in tutorials and/or in the analysis scripts that other people are writing or have written in the past. For this reason, you should in general _not change_ or remove perceived problems from existing test scripts, as that might break backward compatibility.

If you modify a function and subsequently encounter errors in its corresponding test script, it is likely due to your change to the code. You should correct your changes and rerun the test script until it passes.

If you add a new functionality to an existing FieldTrip function, you should extend its corresponding test script with this new functionality.

## Adding a new test script

When you add a new FieldTrip function, you should write a new test script to accompany it.

Test "scripts" should actually not be MATLAB scripts, but MATLAB functions. They start with `function test_xxx` and take (in general) no input arguments and produce no output arguments. The test can print diagnostic information on screen, but most important is that the test passes or that it fails with an error. You can use the [error](https://nl.mathworks.com/help/matlab/ref/error.html) or the [assert](https://nl.mathworks.com/help/matlab/ref/assert.html) functions.

### How to name new test scripts

When adding a test script, please call them `test_xxx.m` when it can run without user interaction, or `inspect_xxx.m` when user interaction is needed, e.g., judging whether the figure is correct or clicking on a button.

To link related scripts to background information on issues, please first file an issue on [github](http://github.com/fieldtrip/fieldtrip/issues), note the number that it receives, and name the test script `text_issueXXX.m`. This links the code to the online documentation and also allows allows future contributors to look up the details. Of course you can also add add additional URL links inside the test script yourself, for example to published methods or publicly available data.

### How to implement algorithmic tests

**Method A**: If possible, the scripts should check against an internal reference solution, i.e., the outcome of the algorithm on particular ideal data is known, therefore the correctness of the algorithm can be tested using simulated data. For instance, the MATLAB function `multiply(2, 3)` has to be tested against the expected outcome which is 6.

**Method B**: If that is not possible or difficult, the scripts should check the consistency of one implementation with another implementation. For example, you create a custom-made function to calculate the square of a number. Then you need to compare its result with the result obtained by using MATLAB's built-in [power](https://nl.mathworks.com/help/matlab/ref/power.html).

**Method C**: If that is also not possible, the result of the algorithm on a particular real-world dataset has to be interpreted as being correct, and that solution should be reused as reference solution (i.e. regression testing). For example, if a function calculates the [forward solution](https://www.fieldtriptoolbox.org/tutorial/headmodel_meg/) for a certain subject then it should be tested against a reference solution, which could be the forward solution of a subject in MNI coordinates.

Tests that need to load test data should include **[dccnpath](/utilities/dccnpath)** to ensure that every user has the correct path to the test data. This function takes as _input_ the path to where the file is located on DCCN central storage and compute cluster; the _output_ is the corresponding path to the file on your local computer. Publicly available data is downloaded automatically from the [download server](https://download.fieldtriptoolbox.org/).

When you create a new test script, you should always include a _list of requirements and dependencies_ at the beginning of the script. For instance:

    % WALLTIME 00:10:00
    % MEM 2gb
    % DATA public
    % DEPENDENCY ft_definetrial ft_preprocessing
 
Regarding the list of dependencies:

#### Memory & Walltime

Test that are executed automatically (i.e., files with the name `test_xxx.m`) MUST include the amount of memory that the execution takes and the duration that the test script runs. This is needed to schedule the test scripts on the [Donders compute cluster](https://hpc.dccn.nl).

The memory should include the amount that MATLAB takes itself (which is about 2gb); it does not have to be very accurate, rounding it up to the nearest GB is fine. The time should include the time that MATLAB itself takes to start (which is about 30-60 seconds), but also the time that it takes to load data, etcetera. Again, there is no reason to make this very tight, if it is too short the execution of the test job might be aborted before it has completed. We suggest using for example 10 or 20 minutes, or 1 or 2 hours.

#### Data usage

You SHOULD include a line that lists whether your test script uses private, public, or no data. In case you contribute a test script that requires data, please [share it with the developers](/faq/how_should_i_send_example_data_to_the_developers) or attach it to the pull request.

#### Dependency on other FieldTrip functions

All test scripts SHOULD ideally include a line that lists the dependencies, i.e. (high- or low-level) toolbox functions to which the test script is particularly sensitive. This allows to quickly search for existing test scripts and evaluate them upon changing the specific toolbox function.

## Working with data

Some test scripts use simulated data generated in the test script and don't need any external data to run.

For test scripts that do read data from disk, data files must be present on the DCCN central storage. There are two types of test data: private and public.

Private test data is stored in the directory `/home/common/matlab/fieldtrip/data/test`, which on the DCCN Windows desktops is available on `H:\common\matlab\fieldtrip\data\test`. This is only available to users inside the DCCN.

Public test data is stored in the directory `/home/common/matlab/fieldtrip/data/ftp`, which on the Donders Windows desktops is available on `H:\common\matlab\fieldtrip\data\ftp`. This data is also available from the [download server](https://download.fieldtriptoolbox.org/).

{% include markup/info %}
Note that test scripts that depend on public data or that do not require any data can be executed by everyone. If needed, the **[dccnpath](/utilities/dccnpath)** function will download the public data automatically.
{% include markup/end %}
