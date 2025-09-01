---
title: Improve regression testing
---

{% include /shared/development/warning.md %}


The goal is to extend the coverage of the unit and integration testing functions. The general principle is explained [here](/development/testing). The functions (we often refer to them as “scripts”) are used to ensure the quality of released versions and we execute them prior to every release. A function either passes or gives an error, which indicates that the code is not ready for release. The test scripts are located in https://github.com/fieldtrip/fieldtrip/tree/master/test, for some we also have test data which is on a file server in the Donders Institute (not shared).

The FieldTrip code base is organized in high-level (or “main”) functions, and lower-level functions that are organized in modules, see [here](/development/architecture). The functions in the modules (plotting, forward, inverse, specest, connectivity, fileio) have an agreed-upon (hence fixed) API so that other toolboxes (a.o. SPM, EEGLAB) and end-users’ scripts can use them reliably. Therefore they should behave consistently over the years, with different MATLAB versions and operating systems. Hence they also need test scripts. Some of them already have scripts (plotting, fileio), others not. Since fileio depends on a large database with different files that are now not shared and tricky to share, it falls out of scope for this MSoC.

Furthermore, there is documentation on the FieldTrip website that shows how to use the functions (examples, tutorials, workshop material). The documentation on the website should run with the latest release of the toolbox, for which test scripts for all tutorials and relevant examples would be needed. This can use data that is shared on the download server, as this is also mirrored on the Donders internal file server where the compute cluster can access it.

## MATLAB for Neurosciece summer projects

Improving the scope of the regression testing scripts is part of the MATLAB for Neurosciece summer projects [#1](https://github.com/fieldtrip/fieldtrip/issues?q=is%3Aissue+project%3Afieldtrip/fieldtrip/3) and [#2](https://github.com/fieldtrip/fieldtrip/issues?q=is%3Aissue+project%3Afieldtrip/fieldtrip/4).
