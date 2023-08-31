---
title: Infrastructure for testing
---

{% include /shared/development/warning.md %}

# Infrastructure for testing

FIXME See also [/development/testing](/development/project/testing)

suggested directory layout

/home/common/matlab/fieldtrip/testdata/original/...
/home/common/matlab/fieldtrip/testdata/raw/monkey256_pele.mat
/home/common/matlab/fieldtrip/testdata/raw/ctf151.mat
/home/common/matlab/fieldtrip/testdata/comp/...
/home/common/matlab/fieldtrip/testdata/bug42/...

 /home/common/matlab/fieldtrip/testcode/test_preproc_bandpassfilter.m
/home/common/matlab/fieldtrip/testcode/test_public_keyval.m
/home/common/matlab/fieldtrip/testcode/test_private_whatever.m
/home/common/matlab/fieldtrip/testcode/test_bug42.m

- Needed fo

* code stability testing in general
* frequently occurring problems:
* small changes in existing code to evoke compatibility with a newly created function (prevent by testing before committing)
* output structure is organised differently

- Should be

* easy to use with as little hassle as possible during code modification
* low on memory: simulate (e.g., random) as many datasets as possible on the fly
* make use of mtest from MathWorks (link needed), especially for reference checks
  http://www.mathworks.com/matlabcentral/fx_files/22846/7/content/matlab_xunit/doc/html/exQuickStart.html
* should test as many different aspects of function as reasonable
* datasets that are used should be easy to replace without editing test-scripts (for updating)

- Ideally after code-modification it should b

  `<change made to topoplotER>`
  cd test
  testtopoplotER.m
  `<process output>`
  `<continue working>`

* Can look like

- 1 testscript per 1 .m file
- 1 datadirectory per 1 .m file (if not possible to simulate)
- per individual test in a testscript, one datafile

Directory/file layout example:

    ./test/testtopoplotER.m
    ./test/testtopoplotER/data_cft275.mat
    ./test/testtopoplotER/data_EEG1020.mat
    ./test/testtopoplotER/data_....
    ./test/testfreqanalysis_mtmconvol.m
    ./test/testfreqanalysis_mtmconvol/data_dpss.m (or on the fly simulation of data)

- Example test-script for testtopoplotER:

  % test ctf275 layout
  load(datafile)
  perform test
  perform reference check

  % test EEG1020 layout
  load(datafile)
  `<perform test>`
  `<perform reference check>`

  % test ER-input
  load(datafile)
  perform test
  `<perform test>`
  `<perform reference check>`

  % test TFR-input
  load(datafile)
  `<perform test>`
  `<perform reference check>`

  % test COMP-input
  load(datafile)
  `<perform test>`
  `<perform reference check>`

  % test HIGHLIGHTING-input
  load(datafile)
  `<perform test>`
  `<perform reference check>`

* Open issues and challenges

- how and what to reference with?
- make a distinction between low-level math tests (e.g., specest_mtmconvol) and high-level tests (e.g., topoplotER)?
- how to reference the output of plotting functions?
