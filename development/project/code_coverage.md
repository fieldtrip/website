---
title: Code coverage
---

{% include /shared/development/warning.md %}

## Code coverage

Using **[ft_untested_functions](/utilities/private/ft_test_untested_functions.m)** we can find which high-level FieldTrip functions are not tested by any test scripts. So which functions have 0% line coverage. To run **[ft_untested_functions](/utilities/private/ft_test_untested_functions.m)** you should use the wrapper function **[ft_test](/utilities/ft_test.m)**:

    ft_test untested_functions

The results we get by running this command are:

>Untested functions:<br>
bis2fieldtrip              
fieldtrip2besa             
fieldtrip2bis              
fieldtrip2spss             
ft_anonymizedata           
ft_audiovideobrowser       
ft_examplefunction         
ft_geometryplot            
ft_multiplotCC             
ft_reproducescript         
ft_sourcemovie             
ft_statistics_analytic     
ft_statistics_crossvalidate
ft_statistics_mvpa         
ft_statistics_stats        
ft_wizard                  
imotions2fieldtrip         
loreta2fieldtrip           
nutmeg2fieldtrip           
spass2fieldtrip            
>
> Number of untested functions: 20

 
However, to have a more complete code coverage it is important to acquire a line-by-line coverage of the high-level FieldTrip functions.

To do that we first created a test case for each of the FieldTrip tests. That way all of the tests follow the [unit testing MATLAB framework](https://nl.mathworks.com/help/matlab/matlab-unit-test-framework.html?s_tid=CRUX_lftnav). To generate the report as an HTML file we used the ``ReportCoverageFor`` name-value argument of the **[runtests](https://nl.mathworks.com/help/matlab/ref/runtests.html)** MATLAB function. All of that is done with the **``inspect_codecoverage``** function.

## MATLAB Code: inspect_codecoverage.m

```matlab
function tests = inspect_codecoverage

if nargout
    % assume that this is called by RUNTESTS
    tests = functiontests(localfunctions);
else
    % assume that this is called from the command line
    fn = localfunctions;
    for i = 1:numel(fn)
        feval(fn{i});
    end
end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function testOptions(testCase)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Get FieldTrip version and path
[~, ftpath] = ft_version;

% Define the folder containing test scripts
testFolder = fullfile(ftpath, 'test');

% List all files in the test folder that start with test_*
list = dir(fullfile(testFolder, 'test_*'));
testScripts = {list.name};

% Remove the ".m" extension from test script names
for i = 1:length(testScripts)
    testScripts{i} = strrep(testScripts{i}, '.m', '');
end

% The test scripts were ran in the DCCN PC and some of them gave error. Initialize an empty cell array to store the names of scripts that gave errors
errorScripts = {};

% Some test scripts were crashibg MATLAB in the DCCN PC without giving an error. We need to exclude those too
indices = ~contains(testScripts, 'test_bug1818'); 
testScripts = testScripts(indices);
indices = ~contains(testScripts, 'test_old_buffer_latency_bandwidth');
testScripts = testScripts(indices);
indices = ~contains(testScripts, 'test_bug472'); 
testScripts = testScripts(indices);

% Loop through the test scripts
for i = 1:length(testScripts)
    try
        % Execute the current test script
        disp(i);
        fprintf('\n Running **%s** \n', testScripts{i});
        eval(testScripts{i});
    catch exception
        % If an error occurs, store the script name in the errorScripts array
        errorScripts{end + 1} = testScripts{i};
        fprintf('Error in script %s:\n', testScripts{i});
        disp(exception.message); % Display the error message
    end

    % Clear the memory so we the RAM won't be overloaded
    close all;
    clc;
    clear functions;
end

% Print the list of test scripts that gave errors
if ~isempty(errorScripts)
    fprintf('\nTest scripts with errors:\n');
    for i = 1:length(errorScripts)
        fprintf('%s\n', errorScripts{i});
    end
else
    fprintf('\nAll test scripts ran successfully.\n');
end
```

Once we have defined the **``inspect_codecoverage``** function, we need to run it using the **[runtests](https://nl.mathworks.com/help/matlab/ref/runtests.html)** MATLAB function. Additionally, we need to define what functions we want to find the coverage for. Here I opt only for the high-level FieldTrip functions:

```matlab
%%%%%%% Run that in the command window %%%%%%%%%%

% Get FieldTrip version and path
[~, ftpath] = ft_version;
list = dir(ftpath);

% List all .m files in the FieldTrip path
indices = endsWith({list.name}, {'.m'});
list = list(indices); 

% Exclude "Contents.m"
indices = ~contains({list.name}, {'Contents.m'});
sourceFunctions = list(indices);

% List the high-level FieldTrip functions
sourceFunctions = {sourceFunctions.name};

% Replace "sourceFunctions" with its full filename, including its path
for i = 1:length(sourceFunctions)
    fullname = which(sourceFunctions{i});
    sourceFunctions{i} = fullname;
end

% Run the coverage report
runtests('inspect_codecoverage.m', 'ReportCoverageFor', sourceFunctions);
```
{% include markup/info %}
Using **``inspect_codecoverage``** we found the full FieldTrip coverage (i.e., the coverage provided by the [``test_*``](https://github.com/fieldtrip/fieldtrip/tree/master/test) test scripts. In total 955 such test scripts exist)  and the partial FieldTrip coverage (i.e., the coverage provided by the [``test_ft_*``](https://github.com/fieldtrip/fieldtrip/tree/master/test) test scripts. In total 202 such test scripts exist). Interestingly, it was found that for the high-level FieldTrip functions the line-by-line full coverage provided by the [``test_*``](https://github.com/fieldtrip/fieldtrip/tree/master/test) test scripts is **41 %** (the full coverage report can be found [here](/assets/coverage/full/)) and the line-by-line partial coverage provided by the [``test_ft_*``](https://github.com/fieldtrip/fieldtrip/tree/master/test) test scripts is **37 %** (the partial coverage report can be found [here](/assets/coverage/partial/)). This proves that the [``test_ft_*``](https://github.com/fieldtrip/fieldtrip/tree/master/test) test scripts can be used for line-by-line coverage, while the rest of the test scripts can be used for [regression testing](https://en.wikipedia.org/wiki/Regression_testing) of the FieldTrip toolbox.
{% include markup/end %}


{% include markup/info %}
Future goal is to also find the coverage of the low-level FieldTrip functions.
{% include markup/end %}


## Alternative way

{% include markup/warning %}
This alternative way needs to be checked more. The line
```matlab 
sourceCodeFolder = fullfile(ftpath, '*.m'); % List the high-level FieldTrip functions (Contents.m is not excluded in this case)
``` 
might need to be edited.
{% include markup/end %}

Another way to find the line-by-line coverage is by adding an instance of the [CodeCoveragePlugin](https://nl.mathworks.com/help/matlab/ref/matlab.unittest.plugins.codecoverageplugin-class.html) class to a test runner. This is part of the [class-based unit testing MATLAB framework](https://nl.mathworks.com/help/matlab/class-based-unit-tests.html). 

First create and add **``inspect_codecoverage``** function inside a new folder called ``code_coverage`` in the main FieldTrip repository. Then run in the command window:

```matlab
%%%%%%% Run that in the command window %%%%%%%%%%

import matlab.unittest.plugins.CodeCoveragePlugin
import matlab.unittest.plugins.codecoverage.CoverageReport

[~, ftpath] = ft_version;

runner = testrunner("textoutput");
sourceCodeFolder = fullfile(ftpath, '*.m'); % List the high-level FieldTrip functions (Contents.m is not excluded in this case)
reportFolder = "coverageReport";
reportFormat = CoverageReport(reportFolder);


p = CodeCoveragePlugin.forFolder(sourceCodeFolder,"Producing",reportFormat);
runner.addPlugin(p)

suite1 = testsuite(fullfile(ftpath, code_coverage)); % "inpect_codecoverage.m" is inside the folder called "code_coverage"
results = runner.run(suite1);
```

We decided to apply the first method using **[runtests](https://nl.mathworks.com/help/matlab/ref/runtests.html)**, and not this alternative way, because it has less lines of code, it is easier to interpret for a non-software engineer and provides the same results.

## Using HPC cluster to speed up the process

At first sight it seems that the HPC cluster of the Donders Institute can not be used to speed up the code coverage process. All the tests need to run _sequentially_ in one MATLAB session in order to acquire a full coverage report. However, we can look back to it in the future.
