---
title: Implemention of realistic electrode properties in forward volume conduction models
---

{% include /shared/development/warning.md %}

# Implemention of realistic electrode properties in forward volume conduction models

## Description

In applications like epilepsy and brain-computer interface, electrocorticography electrode grids are often implanted in patients to detect normal and abnormal brain activity. For both applications, there is the need for assessing the sensitivity of current or newly-designed ECoG grids, whether the sensitivity could be improved, and how to eventually optimize the grid. These investigations can be conducted numerically, with adequate and adapted volume conduction models.

Commonly, in such models, electrodes are considered to record the potential in just a single point. However, we have [shown](https://iopscience.iop.org/article/10.1088/1741-2552/abb11d/meta) the importance of explicitly including electrode properties in volume conduction models for accurately interpreting ECoG measurements. To achieve this type of simulation, the Finite Element Method for useful neuroscience simulations ([FEMfuns](https://github.com/meronvermaas/FEMfuns)) was developed, which allows knowledgeable neuroscientists to solve the forward problem in a variety of different geometrical domains, including various types of source models and electrode properties, such as resistive and capacitive materials, and the double layer that exists at the electrode-tissue interface. Here, as part of the project Into the Brain, we will incorporate FEMfuns into FieldTrip.

## Organization of FEMfuns in FieldTrip

FEMfuns is a python based open-source pipeline and will be called externally from FieldTrip. Within FieldTrip, the headmodel and electrode positions are created, after which the forward solution is found using FEMfuns code under the hood. We split incorporating FEMfuns into Fieldtrip in three steps:

- integrate complex meshing routines in FieldTrip
- test on sphere: compute the forward solutions in FieldTrip using a compiled binary of FEMfuns
- test on real dataset: compute forward solution in a realistically shaped head model (test the interaction of forward solutions computed with FEMfuns and pre-processing/source analysis routines implemented in FieldTrip)

{% include image src="/assets/img/development/project/femfuns/workflow.jpg" width="500" %}

The workflow consists of calling many subroutines (comparable to a Russian doll), start-ing within the toolbox FieldTrip. First, a FieldTrip script in MATLAB loads data and calls the routine to compute the forward solution. Via this routine, a shell script is written and executed under the hood. This shell script sets up the required version of Python and associated packages (using Anaconda), passes the volume conduction parameters (e.g., mesh, tissue and electrode type, source model), and launches FEMfuns. Then, FEMfuns runs the forward simulation. Finally, the lead field matrices are imported back into FieldTrip for further analysis, e.g., source reconstruction analysis.

Currently (September 2021), the MATLAB fuctions to add electrodes to an existing finite element head model are available [here](https://github.com/meronvermaas/fieldtrip/tree/femfuns/external/femfuns)

This work is supported by a grant from stichting IT projecten ([StITPro](https://stitpro.nl/)).
