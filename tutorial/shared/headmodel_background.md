---
title:
layout: default
---

In FieldTrip a volume conduction model is represented as a MATLAB structure which is usually indicated with the variable name **vol**. It describes how the currents flow through the tissue, not where they originate from. In general it consists of a description of the geometry of the head, a description of the conductivity of the tissue, and mathematical parameters that are derived from these. Whether and how the mathematical parameters are described depends on the computational solution to the forward problem either by numerical approximations, such as the boundary element and finite element method (BEM and FEM), or by exact analytical solutions (e.g. for spherical models).

The more accurate the description of the geometry of the head or the source, the better the quality of the forward model. There are many types of head models which, to various degrees, take the individual anatomy into account. The different head models available in FieldTrip are listed [here](/faq/what_kind_of_volume_conduction_models_are_implemented). 
