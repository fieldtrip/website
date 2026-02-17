---
title: Provide an interface to the OpenMEEG software for BEM modelling
---

{% include /shared/development/warning.md %}

The OpenMEEG software is developed within the Odyssee project-team at INRIA Sophia-Antipolis and at ENPC. This package provides tools for solving forward and inverse problems for Magneto- and Electro-encephalography (MEG and EEG). The forward problem uses symmetric Boundary Element Method (symmetric BEM) [Kybic et al, A common formalism for the integral formulations of the forward EEG Problem, IEEE Transactions on Medical Imaging, vol. 24, no.1, 2005]. This method provides excellent accuracy notably for superficial cortical sources.

## Goals

Integrate the OpenMEEG forward models into FieldTrip as better quality alternative to dipoli and bemcp.

## Steps to be taken

- schedule conference call (done)
- create accounts on cvs machine (done)
- commit skeleton (done)
- make licensing clear to users (persistent/1-time) (done)
- commit code for the glue functions (done)
- provide test scenario
  - spherical model (done, only low-level sofar)
  - human subject MEG -> alexandre
  - human subject EEG -> cristiano
  - monkey ECoG -> cristiano
- testing
  - test in-house -> robert, cristiano
  - external test (selected users)
- add glue code and perhaps binaries to FieldTrip release -> robert
- communicate it and ensure that it gets used -> all

## Steps to be taken (cristiano)

- Document the steps to build a bem model for a generic conductor (done)
  - See [this examples](/example/source/bem_evaluation)
- Test OpenMEEG binaries under the different OS (Linux32, Linux64, Windows)
  - For Linux: (done)
    - check the environment variables (done)
    - check correct binary (32-64-bit) (done)
    - check correct gcc version (3-4) (done)
  - For Windows
    - check the installer (done)
- Test installation for a new user (done)

## External links

- <https://openmeeg.github.io>
- <https://gforge.inria.fr/frs/?group_id=435>
