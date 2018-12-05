---
title: Dashboard
tags: [development]
---

# Dashboard

We use the FieldTrip dashboard in development and for maintaining the quality of the FieldTrip code. The test directory in the FieldTrip toolbox contains many [test scripts](https://github.com/fieldtrip/fieldtrip/tree/master/test) (technically they are functions). These test scripts are used initially for reproducing and identifying the cause of a bug, or for designing the end-user script that matches some new functionality. Once a reported bug has been fixed and/or the new functionality has been implemented, we keep the test scripts for [regression testing](https://en.wikipedia.org/wiki/Regression_testing).

{% include markup/info %}
If you suspect that there is an problem with the FieldTrip code, the best way for you to report is is to post it on [github](https://github.com/fieldtrip/fieldtrip/issues) and to contribute a (small) test script that helps us to reproduce the problem.
{% include markup/end %}

All functions in the test directory are executed regularly. If there are problems with the test scripts, an email sent to the main developers.

You can check the results of the test scripts yourself using the **[ft_test](/reference/ft_test)** function like this

    ft_test report test_tutorial_preprocessing
to get the results of a specific test script, or

    ft_test report test_tutorial_preprocessing matlabversion 2017b
to get the results of a specific test script for a specific MATLAB version, or

    ft_test report matlabversion 2012b arch maci64
to get all results of a specific MATLAB version and specific platform.
