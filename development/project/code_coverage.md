---
title: Code coverage
---

{% include /shared/development/warning.md %}

# Code coverage

Using the `untested_functions` command for **[ft_test](/reference/utilities/ft_test)**, we can find which high-level FieldTrip functions are not directly called by any test scripts, i.e., which functions seem to have no coverage at all.

    ft_test untested_functions

The result we get by running this command are:

    Untested functions:
    
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
    
    Number of untested functions: 20

A more complete and detailed code coverage can be obtained with line-by-line coverage of the high-level FieldTrip functions. To do that we first create a test case that includes of the FieldTrip tests, which ensures all of the tests follow the [unit testing MATLAB framework](https://nl.mathworks.com/help/matlab/matlab-unit-test-framework.html?s_tid=CRUX_lftnav).

To generate the report as an HTML file we used the `ReportCoverageFor` name-value argument of the **[runtests](https://nl.mathworks.com/help/matlab/ref/runtests.html)** MATLAB function. 

All of that can be done with the code below

## Determine code coverage

```matlab
%%%%%%% Save this to a file "inspect_codecoverage.m" %%%%%%%%%%

function tests = inspect_codecoverage

if nargout
  % This will be executed by RUNTESTS
  tests = functiontests(localfunctions);
else
  error('This is not to be called from the command-line')
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function testEverything(testCase)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Get FieldTrip version and path
[~, ftpath] = ft_version;

% Define the folder containing test scripts
testFolder = fullfile(ftpath, 'test');

% List all m-files in the test folder that start with test_
list = dir(fullfile(testFolder, 'test_*.m'));
% Remove the ".m" extension from test script names
[~, testScripts] = cellfun(@fileparts, {list.name}, 'Uniformoutput', false);

% Some test scripts were causing MATLAB to crash on a DCCN Windows PC, these need to be excluded
indices = ~contains(testScripts, 'test_bug1818');
testScripts = testScripts(indices);
indices = ~contains(testScripts, 'test_old_buffer_latency_bandwidth');
testScripts = testScripts(indices);
indices = ~contains(testScripts, 'test_bug472');
testScripts = testScripts(indices);
success = false(size(testScripts));

% Loop through the test scripts
for i = 1:length(testScripts)
  try
    % Execute the current test script
    fprintf('\nRunning **%s**\n', testScripts{i});
    eval(testScripts{i});
    success(i) = true;
  catch
    success(i) = true;
  end
end

if all(success)
  fprintf('\nAll test scripts ran successfully.\n');
else
  fprintf('\nThe following test scripts failed:\n');
  for i=find(~success)
    fprintf('%s\n', testScripts{i});
  end
end
```

With the code above saved as a local `inspect_codecoverage.m` function, we run it using the [runtests](https://nl.mathworks.com/help/matlab/ref/runtests.html) MATLAB function. 

Additionally, we define the functions we want to find the coverage for. Here I opt only for the high-level FieldTrip functions:

```matlab
%%%%%%% Run this in the command window %%%%%%%%%%

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

Using the code above we determined the "full" coverage provided by all the 955 `test_xxx` scripts. We also determined the "partial" coverage provided by the 202 `test_ft_xxx` scripts. 

It was found that the line-by-line full coverage is **41 %**, which can and can be found [here](/assets/coverage/full/). The line-by-line partial coverage is **37 %**, which can be found [here](/assets/coverage/partial/). 

This reveals that the `test_ft_xxx` scripts already provide most of the current coverage. The remaining test scripts (especially the `test_bugXXX` and `test_issueXXX`) were more designed for [regression testing](https://en.wikipedia.org/wiki/Regression_testing) and can be continued to be used for that.
{% include markup/end %}

{% include markup/blue %}
A future goal is to also find the coverage of FieldTrip functions that are part of the modules (fileio, preproc, etc.) and other low-level functions.
{% include markup/end %}

## Alternative way

Another way to find the line-by-line coverage is by adding an instance of the [CodeCoveragePlugin](https://nl.mathworks.com/help/matlab/ref/matlab.unittest.plugins.codecoverageplugin-class.html) class to a test runner. This is part of the [class-based unit testing MATLAB framework](https://nl.mathworks.com/help/matlab/class-based-unit-tests.html). 

First create the `inspect_codecoverage.m` function as above and put it inside a new folder `codecoverage` at the root level. Then run in the command window:

```matlab
%%%%%%% Run this in the command window %%%%%%%%%%

import matlab.unittest.plugins.CodeCoveragePlugin
import matlab.unittest.plugins.codecoverage.CoverageReport

[~, ftpath] = ft_version;

runner = testrunner('textoutput');
sourceCodeFolder = fullfile(ftpath, '*.m');
reportFolder = 'coverageReport';
reportFormat = CoverageReport(reportFolder);

p = CodeCoveragePlugin.forFolder(sourceCodeFolder,'Producing',reportFormat);
runner.addPlugin(p)

suite = testsuite(fullfile(ftpath, 'codecoverage')); % 'inpect_codecoverage.m' is the only one inside this folder
results = runner.run(suite);
```

We opted for the first method using [runtests](https://nl.mathworks.com/help/matlab/ref/runtests.html) and not the alternative with [CodeCoveragePlugin](https://nl.mathworks.com/help/matlab/ref/matlab.unittest.plugins.codecoverageplugin-class.html), because it has less lines of code, it is easier to interpret for a non-software engineer and provides the same results.

{% include markup/yellow %}
The alternative above does not work; the function `inpect_codecoverage.m` is not picked up. If you rename it to `inspect_test.m` or something else with "test" in the filename, it does get picked up.

From the MATLAB documentation: _The name of the test file must start or end with the word 'test', which is case-insensitive. If the file name does not start or end with the word 'test', the tests in the file might be ignored in certain cases._
{% include markup/end %}

## Parallel execution

All the tests need to run _sequentially_ in one MATLAB session in order to acquire a full coverage report. Hence, at first sight, it seems that the HPC cluster of the DCCN cannot be used to speed up the code coverage process. We can investigate more efficient execution of the coverage tests in the future.

## Make compatible test scripts

In FieldTrip we have a lot of test scripts (actually functions) that were written without consideration of the MATLAB testing framework. To make these compatible with [runtests](https://nl.mathworks.com/help/matlab/ref/runtests.html), a little bit of code can be added to the top, like this:

```matlab
function tests = test_whatever

if nargout
  % assume that this is called by RUNTESTS
  tests = functiontests(localfunctions);
else
  % assume that this is called from the command line
  fn = localfunctions;
  for i = 1:numel(fn)
    feval(fn{i});
  end
end % nargout

function executeTest(testCase)
% this subfunction contains the actual code to be tested
% ...
```