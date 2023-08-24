---
title: Testing
tags: [development, testing]
redirect_from:
  - /development/dashboard/
---

# Testing

## Why testing is important?

FieldTrip is a toolbox with many functions, designed to be compatible with each other. This means that one function often relies on the output of another function. Functions are categorized as [high, low-level, or private](https://www.fieldtriptoolbox.org/development/architecture/#high-level-low-level-and-private-functions), with high-level functions depending on low-level and private functions.

To make sure everything works correctly, we use **testing**. This way, we can be confident that when we add, modify, or remove a function, we won't break the existing ones. Testing also helps us find and fix any issues early on, ensuring that FieldTrip functions smoothly for all users.

## How are the tests organised in FieldTrip?

Once a reported bug has been fixed and/or the new functionality has been implemented, we keep the test scripts for [regression testing](https://en.wikipedia.org/wiki/Regression_testing).

All the test scripts (technically they are functions) are located in [`fieldtrip/test` directory](https://github.com/fieldtrip/fieldtrip/tree/master/test). Tests are called as `test_xxx.m` when they can run without user interaction, or `inspect_xxx.m` when user interaction is needed, e.g., judging whether the figure is correct, clicking on a button, or closing a figure to continue the analysis.

The test scripts are further split into tests related to bugs, issues or pull requests, tests related to a FieldTrip function, tests related to example, tutorial pipelines and failed-obsolete tests:

### Tests related to a FieldTrip function

Test scripts that relate to [a specific FieldTrip function](https://www.fieldtriptoolbox.org/reference/) are named as `test_ft_xxx`.

### Tests related to example and tutorial pipelines

Example pipelines used by researchers when they perform their own data analysis and the tutorial pipelines provided in the [FieldTrip website](https://www.fieldtriptoolbox.org/tutorial/) are also provided as test scripts. They are named as `test_example_xxx` and `test_tutorial_xxx` respectively.

### Tests related to bugs, issues or pull requests

To link related scripts to the background information on bug reports and/or online discussions that we have when making changes to the code, test scripts that relate to a bug on <http://bugzilla.fieldtriptoolbox.org/> are named as `text_bugXXX.m`. Test scripts that relate to an issue on <https://github.com/fieldtrip/fieldtrip/issues/> are named as `test_issueXXX.m`, and test script that relate to a pull request on <https://github.com/fieldtrip/fieldtrip/pulls/> are named as `test_pullXXX.m`. Where `XXX` is the reference number of the bug, issue or pull request. This allows future contributors to look up the online discussion and details on basis of the file name. Of course you can also add help with additional links inside the test script yourself.


{% include markup/info %}
If you suspect a problem with the FieldTrip code, the best way to resolve it is to post it on [GitHub as an issue](https://github.com/fieldtrip/fieldtrip/issues) and to contribute a (small) test script that helps us to reproduce the problem. After fixing the problem, we add the script to the test directory to ensure future code quality. More information on that topic is provided in the [reporting issues](https://www.fieldtriptoolbox.org/development/issues/) FieldTrip webpage.
{% include markup/end %}

{% include markup/info %}
It is important to keep in mind that the test files or directories related to a  GitHub issue or Bugzilla report are named after the GitHub issue or Bugzilla number.
{% include markup/end %}



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
    % DATA no 



## Running existing tests 
Running a Fieldtrip test is as easy as writing the name of the test in the command line. For example, to run test_bug103 type: 
    test_bug103

To find the background info about this test can be found in [bugzilla]()
similarly, issues: ... and pull requests: ...

## Finding tests
When you modify or remove pre-existing code, you should find the necessary [test scripts](https://github.com/fieldtrip/fieldtrip/tree/master/test) and then run them in your local computer. Here we demostrate a small tutorial of how to do that. 

For example, let's say you made a modification to  **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/master/ft_preprocessing.m)**. Firstly, you should list all the [test scripts](https://github.com/fieldtrip/fieldtrip/tree/master/test) together with their list of dependencies in a [MATLAB table](https://nl.mathworks.com/help/matlab/ref/table.html):

    [ftver, ftpath] = ft_version;

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
        name{i}        = d(i).name(1:end-2); % remove .m
        walltime{i}    = lines{line1}(length('% WALLTIME ')+1:end);
        mem{i}         = lines{line2}(length('% MEM ')+1:end);
        data{i}        = lines{line3}(length('% DATA ')+1:end);
        dependency{i}  = lines{line4}(length('% DEPENDENCY ')+1:end);
    else
        % something is wrong
        skip(i) = true;
    end
    end

    test = table(name, walltime, mem, data, dependency);
    test = test(~skip,:);


You should select the [test scripts](https://github.com/fieldtrip/fieldtrip/tree/master/test) that depend on **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/master/ft_preprocessing.m)**. 
    
    indices=contains(test.dependency, 'ft_preprocessing');

    filtered_name = test.name(indices);
    filtered_walltime = test.walltime(indices);
    filtered_mem = test.mem(indices);
    filtered_data = test.data(indices);
    filtered_dependency = test.dependency(indices);

    filtered_test = table(filtered_name, filtered_walltime, filtered_mem, filtered_data, filtered_dependency);

Since you are an external contribitor with no access to the [DCCN intranet](https://intranet.donders.ru.nl/), you can only run tests that don't use data and use publicly available data. So, you have to delete from your table the test scripts that use private data:

    keepRows = ~strcmp(filtered_test.filtered_data, 'private');
    filtered_table = filtered_test(keepRows, :)

Finally, it is more efficient to select tests that run fast and do not consume much memory. For this reason you should sort the tests in increasing walltime and memory:

    filtered_table = sortrows(filtered_table,'filtered_walltime','ascend');
    filtered_table = sortrows(filtered_table,'filtered_mem','ascend');

To run the first 10 tests from the filtered table:

    findTests=string(filtered_table.filtered_name(1:10));
    for i=1:numel(findTests)
        fprintf("\n ------------------------ \n Running test: %s \n\n", findTests(i))
        eval(findTests(i)); % run tests
    end



## Extending existing tests

Test scripts validate specific functionalities that are integral to Fieldtrip. For this reason, you should not change or extend existing test scripts.

 If you modify a function and encounter errors in its corresponding test script, you should correct the modified function according to the test script's error. Then you should rerun the test script.

However, if you add a new functionality to a pre-existing function, then you should extend its test script to also test this new functionality.




## Adding a new test script 

When you add a new Fieldtrip function, you should also write a new test script to accompany this function.

Test "scripts" should actually not be MATLAB scripts, but MATLAB functions. They start with `function test_xxx` and take (in general) no input arguments and produce no output arguments. The test can print diagnostic information on screen, but most important is that the test passes or that it fails with an error. You can use the [error](https://nl.mathworks.com/help/matlab/ref/error.html) or the [assert](https://nl.mathworks.com/help/matlab/ref/assert.html) functions.


### How to name the new test scripts

When adding a test script, please call them `test_xxx.m` when it can run without user interaction, or `inspect_xxx.m` when user interaction is needed, e.g., judging whether the figure is correct, clicking on a button, or closing a figure to continue the analysis.

To link related scripts to the background information on bug reports and/or online discussions that we have when making changes to the code, test scripts that relate to a bug on <http://bugzilla.fieldtriptoolbox.org/> should be named `text_bugXXX.m`. Test scripts that relate to an issue on <https://github.com/fieldtrip/fieldtrip/issues/> should be named `test_issueXXX.m`, and test script relating to a pull request on <https://github.com/fieldtrip/fieldtrip/pulls/> should be named `test_pullXXX.m`. This allows future contributors to look up the online discussion and details on basis of the file name. Of course you can also add help with additional links inside the test script yourself.

### How to implement algorithmic tests

**Method A**: If possible, the scripts should check against an internal reference solution, i.e., the outcome of the algorithm on particular ideal data is known, therefore the correctness of the algorithm can be tested using simulated data. For instance, the MATLAB function `multiply(2, 3)` has to be tested against the expected outcome which is 6.

**Method B**: If that is not possible or difficult, the scripts should check the consistency of one implementation with another implementation. For example, you create a custom-made function to calculate the square of a number. Then you need to compare its result with the result obtained by using MATLAB's built-in [power](https://nl.mathworks.com/help/matlab/ref/power.html). 

**Method C**: If that is also not possible, the result of the algorithm on a particular real-world dataset has to be interpreted as being correct, and that solution should be reused as reference solution (i.e. regression testing). For example, if a function calculates the [forward solution](https://www.fieldtriptoolbox.org/tutorial/headmodel_meg/) for a certain subject then it should be tested against a reference solution, which could be the forward solution of a subject in MNI coordinates.

Tests that need to load test data should include **[dccnpath](/utilities/dccnpath)** to ensure that every user has the correct path to the test data. **[dccnpath](https://github.com/fieldtrip/fieldtrip/blob/master/utilities/dccnpath.m)**  takes as _input_ the path to where the test data are downloaded in the Donders Centre for Cognitive Neuroimaging (DCCN) computer cluster and it _outputs_ the corresponding path to these input test data in your local computer. For the [publicly available data](https://download.fieldtriptoolbox.org/), it checks if they are downloaded in your local computer, and if not it downloads them automatically.

Also, when you create a new test script you should always include a _list of dependencies_ in the beginning of the script. For instance:

    % WALLTIME 00:10:00
    % MEM 2gb
    % DEPENDENCY ft_definetrial ft_preprocessing
    % DATA public

 
Regarding the list of dependencies:

#### Memory & Walltime

Test that are executed automatically (i.e. files with the name `test_xxx.m`) MUST include the **amount of memory** that the execution takes and the **duration** that the test script runs. This is needed to schedule the test scripts on the Donders compute cluster. The memory should include the amount of memory that MATLAB takes itself (which is about 500MB); it does not have to be very accurate, rounding it off to the nearest GB is fine. The time should include the time that MATLAB itself takes to start (which is about 30-60 seconds), but also the time that it takes to load data, etcetera. Again, there is no reason to make this very tight, if it is too short the execution of the test job might be aborted before it has completed. We suggest using for example 10 or 20 minutes, or 1 or 2 hours.

#### Dependency on other FieldTrip functions 

All test scripts SHOULD if possible include a line that lists the **dependencies**, i.e. (high- or low-level) FieldTrip functions to which the test script is particularly sensitive. This allows developers to quickly search for existing test scripts and evaluate them whenever they change the specific FieldTrip function. In that way *your* test script helps to ensure that existing functionality does not break.

#### Data usage

You SHOULD include a line that lists what **type of data** your test script uses. A test script might not use data (i.e., % DATA no) or use publicly available data (i.e., % DATA public) or not publicly available data (i.e., % DATA private). 

In case your test script uses data, you should also include them in your [pull request](https://github.com/fieldtrip/fieldtrip/pulls).



## Working with data

Some test scripts use simulated data generated in the test script and don't need to download any data to run. These test scripts include the dependency: ``% DATA no``

For test scripts that read data from disk, it is required that the data files are present on the DCCN computer cluster. There are two types of test data: the private and the public test data.  

The private test data is stored in the network directory `/home/common/matlab/fieldtrip/data/test` (which on the DCCN Windows desktops is available on `H:\common\matlab\fieldtrip\data\test`). The private test data is only available to users that have connection to the [DCCN intranet](https://intranet.donders.ru.nl/). Test scripts that use private test data include the dependency: ``% DATA private``

The public test data is stored in the network directory `/home/common/matlab/fieldtrip/data/ftp` (which on the Donders Windows desktops is available on `H:\common\matlab\fieldtrip\data\ftp`). The public test data is available to all the users through the [WebDAV download server](https://download.fieldtriptoolbox.org/) of FieldTrip. Test scripts that use public test data include the dependency: ``% DATA public``

{% include markup/info %}
Please note that test scripts that include ``DATA no`` and ``DATA public`` can be run by every user.
{% include markup/end %}









