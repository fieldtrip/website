---
title: Implement [FEMfuns](https://github.com/meronvermaas/FEMfuns) volume conduction models with complete electrodes
---

{% include /shared/development/warning.md %}

## Implement [FEMfuns](https://github.com/meronvermaas/FEMfuns) volume conduction models with complete electrodes

##
Description

In applications like epilepsy and brain-computer interface, electrocorticography electrode grids are often implanted in patients to detect normal and abnormal brain activity. For both applications, there is the need for assessing the sensitivity of current or newly-designed ECoG grids, whether the sensitivity could be improved, and how to eventually optimize the grid. These investigations can be conducted numerically, with adequate and adapted volume conduction models.

Commonly, in such models, electrodes are considered to record the potential in just a point. However, we have [shown](https://iopscience.iop.org/article/10.1088/1741-2552/abb11d/meta) the importance of explicitly including electrode properties in volume conduction models for accurately interpreting ECoG measurements. To achieve this type of simulation, the Finite Element Method for useful neuroscience simulations ([FEMfuns](https://github.com/meronvermaas/FEMfuns)) was developed, which allows neuroscientists to solve the forward problem in a variety of different geometrical domains, including various types of source models and electrode properties, such as resistive and capacitive materials. Here, as part of the project Into the Brain, we will incorporate FEMfuns into FieldTrip.

##
Organization of FEMfuns in FieldTrip

FEMfuns is a python based open-source pipeline and will be called externally from FieldTrip. Within FieldTrip, the headmodel and channel positions are created, after which the forward solution is found using FEMfuns code under the hood. We split incorporating FEMfuns into Fieldtrip in three steps:

- integrate complexe meshing routines in FielTrip
- in a sphere, compute the forward solutions in FieldTrip using a compiled binary of FEMfuns
- test on real dataset: test the interaction of forward solutions computed with FEMfuns and pre-processing/source analysis routines implemented in FieldTrip


{% include image src="/assets/img/development/project/femfuns/workflow.jpg" width="500" %}

The workflow consists of calling a shell script from FieldTrip passing the volume conduction parameters (e.g., mesh, tissue and electrode type, source model) which sets up the right anaconda environment after which FEMfuns runs the forward simulation. Subsequently, the lead field matrices are imported back into FieldTrip for source reconstruction analysis.

This work is financed by stichting IT projecten ([StITPro](https://stitpro.nl/)).
