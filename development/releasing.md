---
title: Release and quality control
tags: [development, release]
redirect_from:
  - /development/dashboard/
---

# Release and quality control

Daily releases of FieldTrip are made available on the download server. The corresponding commits (i.e., point in time in the git repository) are tagged, such that the releases are also [available from GitHub](https://github.com/fieldtrip/fieldtrip/releases). New FieldTrip versions are released only if all tests pass. So, on some days there will not be a release.

## Releasing the code

Every evening one of the FieldTrip [automation scripts](https://github.com/fieldtrip/automation) is executed as a cron job. It checks whether there are new commits on the [release branch](https://github.com/fieldtrip/fieldtrip/tree/release), and if so, it makes a new zip file of fieldtrip, fieldtrip-lite, and some of the modules, and copies those to the download server. It also tags the corresponding commit on the release branch on GitHub with ""YYYYMMDD", consistent with the naming of the zip files.

## Quality control prior to every release

The [fieldtrip/test](https://github.com/fieldtrip/fieldtrip/tree/master/test) directory contains many test scripts (technically they are functions). We use these initially to reproduce and identifying the cause of a bug, or for designing new end-user scripts that matches some new functionality that we want to implement. Once a reported bug has been fixed and/or the new functionality has been implemented, we keep the test scripts for [regression testing](https://en.wikipedia.org/wiki/Regression_testing).

{% include markup/info %}
If you suspect a problem with the FieldTrip code, the best way to resolve it is to post it on [GitHub](https://github.com/fieldtrip/fieldtrip/issues) and to contribute a (small) test script that helps us to reproduce the problem. These test scripts help us reproduce the problem. After fixing the problem, we add the script to the test directory to ensure future code quality.  
{% include markup/end %}

The [master branch](https://github.com/fieldtrip/fieldtrip/tree/master) is tested _every evening_ by executing all test functions using the [dashboard scripts](https://github.com/fieldtrip/dashboard) that are running as a cron job on the [DCCN compute cluster](https://dccn-hpc-wiki.readthedocs.io). If the complete test batch passes, the changes on the master branch are automatically merged into the [release branch](https://github.com/fieldtrip/fieldtrip/tree/release). If there is a problems with one of the test scripts, an email is sent to the main developers and the updates are _not_ merged from master into release.

## Guidelines to contributors

{% include markup/info %}
When you [contribute](/development/contribute) to FieldTrip, it is recommended that you [test your changes](/development/testing). If the necessary test scripts pass, you can submit a [pull request](https://github.com/fieldtrip/fieldtrip/pulls).
{% include markup/end %}

When you [add a new FieldTrip function](/development/testing#adding-a-new-test-script), it is good practice to also include a short test script. This helps the maintainers to evaluate your contribution, and in the future to ensure that future changes to code elsewhere do not break your contribution. When you [modify existing code](/development/testing), you should check for existing [test scripts](/development/testing#running-existing-tests) and run them locally prior to sending a pull-request.
